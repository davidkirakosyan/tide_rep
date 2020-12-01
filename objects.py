from physics import *


class PhysicalBall:
    """
    Class that describes solid ball
    """
    def __init__(self, m, x, y, Vx, Vy, R):
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.R = R
        self.color = color
        self.image = image
        self.Fx = self.Fy = 0
    
    def move(self, objects, dt):
        """
        recalculates parameters of the body
        
        :return: None
        """
        calculate_force(self, objects)

        ax = body.Fx / body.m
        body.x += body.Vx * dt + ax * dt**2 / 2
        body.Vx += ax * dt

        ay = body.Fy / body.m
        body.y += body.Vy * dt + ay * dt**2 / 2
        body.Vy += ay * dt

        collisions(self, objects)

    