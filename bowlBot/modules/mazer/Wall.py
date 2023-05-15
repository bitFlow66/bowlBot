from PIL import ImageDraw

from modules.mazer.Point import Point


class Wall:

    def __init__(self, canvas, start: Point, end: Point):
        self._canvas = canvas
        self._start = start
        self._end = end
        self._showWall = True

    def show(self):
        if self._showWall:
            self._canvas.line(self._start, self._end, fill=0)
