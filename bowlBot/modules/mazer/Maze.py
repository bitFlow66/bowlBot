from PIL import Image, ImageDraw, ImageShow

import modules.mazer.mazerConf as conf
from modules.mazer.Cell import Cell
from modules.mazer.Point import Point


class Maze:
    def __init__(self, cellsX=20, cellsY=15, size=20):
        self.cellsX = cellsX
        self.cellsY = cellsY
        self.size = size
        self.width = size * self.cellsX
        self.height = size * self.cellsY

        self.image = Image.new("RGB", (self.width, self.height), conf.WHITE)
        self.canvas = ImageDraw.Draw(self.image)

        self._maze = self._generateMaze()

        for row in self._maze:
            for cell in row:
                cell.show()

        self.image.save("test.png")
        print("Image")

    def _generateMaze(self) -> list:
        maze = []
        for row in range(self.cellsY):
            maze.append([Cell(self.canvas, row, collumn, self.size) for collumn in range(self.cellsX)])
        return maze




    def up(self, cell: Cell):
        pass

    def down(self):
        pass

    def left(self):
        pass

    def right(self):
        pass
