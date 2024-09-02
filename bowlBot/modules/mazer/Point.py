class Point:
    def __init__(self, posX, posY):
        self._posX = posX
        self._posY = posY

    @property
    def x(self):
        return self._posX

    @property
    def y(self):
        return self._posY
