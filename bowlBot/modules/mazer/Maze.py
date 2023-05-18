from PIL import Image, ImageDraw, ImageShow

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

        self.image = Image.new("RGB", (self.width, self.height), conf.WHITE)
        self.canvas = ImageDraw.Draw(self.image)

        self._maze = self._generateGrid()

        self._show()

        self.image.save("test.png")

    def _generateGrid(self) -> list[list[Cell]]:
        maze = []
        for row in range(self.rows):
            maze.append([Cell(self.canvas, row, collumn, self.size) for collumn in range(self.collumns)])
        return maze

    def _show(self):
        for row in self._maze:
            for cell in row:
                cell.show()


    def getImageAsBytes(self) -> bytes:
        return self.image.tobytes()

    def up(self, cell: Cell):
        if cell.rowPos - 1 < 0:
            raise CellOutOfBoundsError(cell.collumnPos, cell.rowPos - 1)
        cell.getWalls[Direction.UP].showWall = False
        nextCell = self._maze[cell.rowPos - 1][cell.collumnPos]
        nextCell.getWalls[Direction.DOWN].showWall = False
        return nextCell

    def down(self, cell: Cell):
        if cell.rowPos + 1 >= self.rows:
            raise CellOutOfBoundsError(cell.collumnPos, cell.rowPos + 1)
        cell.getWalls[Direction.DOWN].showWall = False
        nextCell = self._maze[cell.rowPos + 1][cell.collumnPos]
        nextCell.getWalls[Direction.UP].showWall = False
        return nextCell


    def left(self, cell: Cell):
        if cell.collumnPos - 1 < 0:
            raise CellOutOfBoundsError(cell.collumnPos - 1, cell.rowPos)
        cell.getWalls[Direction.LEFT].showWall = False
        nextCell = self._maze[cell.rowPos][cell.collumnPos - 1]
        nextCell.getWalls[Direction.RIGHT].showWall = False
        return nextCell

    def right(self, cell: Cell):
        if cell.collumnPos + 1 >= self.collumns:
            raise CellOutOfBoundsError(cell.collumnPos + 1, cell.rowPos)
        cell.getWalls[Direction.RIGHT].showWall = False
        nextCell = self._maze[cell.rowPos][cell.collumnPos + 1]
        nextCell.getWalls[Direction.LEFT].showWall = False
        return nextCell


