from physics import *


class PhysicalBall:
    """
    Class that describes solid ball
    """
    def __init__(self, m, x, y, Vx, Vy, R, color, drag_reasiness = False):
        self.m = m
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.R = R
        self.color = color
        self.image = None
        self.Fx = self.Fy = 0
        self.drag_readiness = False

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

    def drag_start (objects, event):
        """
        Grabs an object via clicking on it by mouse
        """
        for self in objects:
            dist_event_obj = ((event.x - self.x)**2 + (event.y - self.y)**2)**0.5
            if dist_event_obj <= self.R:
                self.drag_readiness = True

    def drag_finish (self, event):
        """
        Releases an object after dragging it by mouse
        """
        self.drag_readiness = False
        self.x = event.x
        self.y = event.y

    def drag (objects, event):
        """
        moves an object via to dragging it by mouse

        :return: None
        """
        for self in objects:
            if self.drag_readiness:
               self.x = event.x
               self.y = event.y
               
        
                
            

