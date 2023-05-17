from modules.mazer.Wall import Wall
from modules.mazer.Point import Point


class Cell:
    def __init__(self, canvas, pos: Point, size):
        self._canvas = canvas
        self._pos = pos
        self._size = size

        # Walls for a cell
        self._walls = {
            "up": Wall(self._canvas, self._pos, Point(self._pos.x + self._size, self._pos.y)),
            "down": Wall(self._canvas, Point(self._pos.x, self._pos.y + self._size), Point(self._pos.x + self._size, self._pos.y + self._size)),
            "left": Wall(self._canvas, self._pos, Point(self._pos.x, self._pos.y + self._size)),
            "right": Wall(self._canvas, Point(self._pos.x + self._size, self._pos.y), Point(self._pos.x + self._size, self._pos.y + self._size))
        }

    def show(self):
        for _, wall in self._walls.items():
            wall.show()
