# 6

import math


class sphere():
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def surfaceArea(self):
        return self.radius * self.radius * math.pi * 4

    def volume(self):
        return (4 / 3) * math.pi * self.radius * self.radius * self.radius

