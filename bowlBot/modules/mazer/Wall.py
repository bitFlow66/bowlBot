from enum import Enum

from modules.mazer.Point import Point


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Wall:

    def __init__(self, canvas, start: Point, end: Point):
        self._canvas = canvas
        self._start = start
        self._end = end
        self.showWall = True

    def show(self):
        if self.showWall:
            self._canvas.line((self._start.x, self._start.y, self._end.x, self._end.y), fill=0)
