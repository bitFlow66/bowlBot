from modules.mazer.Wall import Wall, Direction
from modules.mazer.Point import Point


class Cell:
    def __init__(self, canvas, rowPos: int, collumnPos: int, size: int):
        self._canvas = canvas
        self._rowPos = rowPos
        self._collumnPos = collumnPos
        self._size = size

        # Walls for a cell
        # collumns = x-achsis
        # rows = y-achsis
        _x = self._collumnPos * self._size
        _y = self._rowPos * self._size
        self._walls: dict[Direction, Wall] = {
            Direction.UP: Wall(self._canvas, Point(_x, _y), Point(_x + self._size, _y)),
            Direction.DOWN: Wall(
                self._canvas,
                Point(_x, _y + self._size),
                Point(_x + self._size, _y + self._size),
            ),
            Direction.LEFT: Wall(
                self._canvas, Point(_x, _y), Point(_x, _y + self._size)
            ),
            Direction.RIGHT: Wall(
                self._canvas,
                Point(_x + self._size, _y),
                Point(_x + self._size, _y + self._size),
            ),
        }

    def show(self):
        for _, wall in self._walls.items():
            wall.show()

    def resetCellWalls(self):
        for wall in self._walls.values():
            wall.showWall = True

    @property
    def getWalls(self) -> dict[Direction, Wall]:
        return self._walls

    @property
    def rowPos(self):
        return self._rowPos

    @property
    def collumnPos(self):
        return self._collumnPos
