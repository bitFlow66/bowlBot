from PIL import Image, ImageDraw, ImageShow
from typing import Optional
from random import choice

import modules.mazer.mazerConf as conf
from modules.mazer.Cell import Cell
from modules.mazer.Wall import Direction

class CellOutOfBoundsError(Exception):
    def __init__(self, collumn: int, row: int) -> None:
        self.collumn = collumn
        self.row = row
        self.message = f"Cell is not on grid: collumn = {self.collumn}, row = {self.row}"
        super().__init__(self.message)

class Maze:
    def __init__(self, collumns=20, rows=15, size=20):
        self.collumns = collumns
        self.rows =rows
        self.size = size
        self.width = size * self.collumns
        self.height = size * self.rows

        self._visitedCells: list[Cell] = []

        self.image = Image.new("RGB", (self.width, self.height), conf.WHITE)
        self.canvas = ImageDraw.Draw(self.image)

        self._grid = self._generateGrid()


        self._visitedCells.append(self._grid[0][0])
        self.right(self._grid[0][0])

        self._randomWalk(self._grid[0][1])

        self._show()

        self.image.save("test.png")

    def _generateGrid(self) -> list[list[Cell]]:
        maze = []
        for row in range(self.rows):
            maze.append([Cell(self.canvas, row, collumn, self.size) for collumn in range(self.collumns)])
        return maze

    def _show(self):
        for row in self._grid:
            for cell in row:
                cell.show()


    def getImageAsBytes(self) -> bytes:
        return self.image.tobytes()

    def _cellPosInList(self, cellList: list[Cell], cell: Cell) -> Optional[int]:
        return cellList.index(cell) if cell in cellList else None



    def _getUnvisitedCell(self) -> Optional[Cell]:
        for row in self._grid:
            for cell in row:
                return cell if cell not in self._visitedCells else None


    def _generateMaze(self):
        while True:
            unvisitedCell = self._getUnvisitedCell()
            if not unvisitedCell:
                break
            newCells = self._randomWalk(unvisitedCell)
            self._visitedCells.extend(newCells)



    # Wilson's algorithm (loop-erased random walk, unbiased mace generation)
    # 1. Arbitrary chosen starting cell, add to mace
    # 2. New arbitrary cell to start the walk (unfilled cell in (say) left-to-right, top-to-bottom order)
    # 3. Walk as long as no already used cell is discovered again (mace or walk)
    # 3.1 Either hit the current loop -> delete loop up to this point
    # 3.2 Or hit the mace -> add to mace
    # 4. Repeat from step 2

    def _randomWalk(self, startingCell: Cell) -> list[Cell]:
        currentWalk: list[Cell] = [startingCell]
        currentCell: Cell = startingCell
        while True:
            randDirection = choice([self.up, self.down, self.left, self.right])
            try:
                nextCell = randDirection(currentCell)
            except CellOutOfBoundsError:
                continue
            except Exception as ex:
                raise ex
            if len(currentWalk) > 2 and nextCell == currentWalk[-2]:
                continue
            cellIndex = self._cellPosInList(currentWalk, nextCell)
            if cellIndex:
                cellReset = currentWalk[:cellIndex]
                currentWalk = currentWalk[cellIndex:]
                for cell in cellReset:
                    cell.resetCellWalls()
                continue
            if self._cellPosInList(self._visitedCells, nextCell):
                return currentWalk
            currentWalk.append(nextCell)
            currentCell = nextCell


    def up(self, cell: Cell) -> Cell:
        if cell.rowPos - 1 < 0:
            raise CellOutOfBoundsError(cell.collumnPos, cell.rowPos - 1)
        cell.getWalls[Direction.UP].showWall = False
        nextCell = self._grid[cell.rowPos - 1][cell.collumnPos]
        nextCell.getWalls[Direction.DOWN].showWall = False
        return nextCell

    def down(self, cell: Cell) -> Cell:
        if cell.rowPos + 1 >= self.rows:
            raise CellOutOfBoundsError(cell.collumnPos, cell.rowPos + 1)
        cell.getWalls[Direction.DOWN].showWall = False
        nextCell = self._grid[cell.rowPos + 1][cell.collumnPos]
        nextCell.getWalls[Direction.UP].showWall = False
        return nextCell


    def left(self, cell: Cell) -> Cell:
        if cell.collumnPos - 1 < 0:
            raise CellOutOfBoundsError(cell.collumnPos - 1, cell.rowPos)
        cell.getWalls[Direction.LEFT].showWall = False
        nextCell = self._grid[cell.rowPos][cell.collumnPos - 1]
        nextCell.getWalls[Direction.RIGHT].showWall = False
        return nextCell

    def right(self, cell: Cell) -> Cell:
        if cell.collumnPos + 1 >= self.collumns:
            raise CellOutOfBoundsError(cell.collumnPos + 1, cell.rowPos)
        cell.getWalls[Direction.RIGHT].showWall = False
        nextCell = self._grid[cell.rowPos][cell.collumnPos + 1]
        nextCell.getWalls[Direction.LEFT].showWall = False
        return nextCell


