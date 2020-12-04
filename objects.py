from physics import *


class PhysicalBall:
    """
    Class that describes solid ball
    """
    def __init__(self, m = 0, x = 0, y = 0, Vx = 0, Vy = 0,
                 R = 0, color = 'white', drag_readiness = False, type=None):
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
        recalculates parameters of the body
        
        :return: None
        """
        calculate_force(self, objects)

        ax = self.Fx / self.m
        self.x += self.Vx * dt + ax * dt**2 / 2
        self.Vx += ax * dt

        ay = self.Fy / self.m
        self.y += self.Vy * dt + ay * dt**2 / 2
        self.Vy += ay * dt

        collisions(self, objects)

    def create_image(self, canv):
        '''
        creates image for PhysicalBall objects
        '''
        R = self.R
        self.image = canv.create_oval([0, 0], [2 * R, 2 * R], fill=self.color)
            

