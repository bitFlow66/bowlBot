from modules.mazer.Wall import Wall
from modules.mazer.Point import Point


class Cell:
    def __init__(self, canvas, rowPos: int, collumnPos: int, size: int):
        self._canvas = canvas
        self._rowPos = rowPos
        self._collumnPos = collumnPos
        self._size = size

        # Walls for a cell
        _x = self._collumnPos * self._size
        _y = self._rowPos * self._size
        self._walls = {
            "up": Wall(self._canvas, Point(_x, _y), Point(_x + self._size, _y)),
            "down": Wall(self._canvas, Point(_x, _y + self._size), Point(_x + self._size, _y + self._size)),
            "left": Wall(self._canvas, Point(_x, _y), Point(_x, _y + self._size)),
            "right": Wall(self._canvas, Point(_x + self._size, _y), Point(_x + self._size, _y + self._size))
        }

    def show(self):
        for _, wall in self._walls.items():
            wall.show()
