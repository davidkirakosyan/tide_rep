import math

from physics import *


class PhysicalBall:
    """
    Class that describes solid ball
    """

    def __init__(self, m=0, x=0, y=0, Vx=0, Vy=0,
                 R=0, color='white', drag_readiness=False, type=None):
        self.type = type
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.R = R
        self.color = color
        self.image = None
        self.Fx = self.Fy = 0
        self.drag_readiness = drag_readiness

    def move(self, objects, dt):
        """
        Recalculates parameters of the body.

        :param objects: list of all physical objects.
        :param dt: moving time interval
        :return: None
        """
        calculate_force(self, objects)

        ax = self.Fx / self.m
        self.x += self.Vx * dt + ax * dt ** 2 / 2
        self.Vx += ax * dt

        ay = self.Fy / self.m
        self.y += self.Vy * dt + ay * dt ** 2 / 2
        self.Vy += ay * dt

        collisions(self, objects)

    def create_image(self, canv):
        """
        Creates image for PhysicalBall objects

        :param canv: Tk Canvas object
        :return: None
        """
        R = self.R
        self.image = canv.create_oval([0, 0], [2 * R, 2 * R], fill=self.color, outline='')


def create_water(planet, N=70, density=100):
    """
    Creates N water balls around planet.

    :param N: number of molecules
    :return: new list of objects
    """
    molecules = []
    r = math.pi * planet.R / N  # radius of molecule
    for i in range(N):
        obj = PhysicalBall()
        obj.R = r
        obj.color = 'white'
        obj.m = density * 4 / 3 * math.pi * r ** 3
        obj.x = planet.x + (planet.R + r) * math.cos(2 * math.pi / N * i)
        obj.y = planet.y + (planet.R + r) * math.sin(2 * math.pi / N * i)
        obj.type = 'water'
        molecules += [obj]

    return molecules

if __name__ == "__main__":
    print("This module is not for direct call!")
