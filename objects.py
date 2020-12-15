import math

from physics import *

gravitational_constant = 6.67408E-11

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

        ax = self.Fx / self.m
        self.x += self.Vx * dt + ax * dt ** 2 / 2
        self.Vx += ax * dt

        ay = self.Fy / self.m
        self.y += self.Vy * dt + ay * dt ** 2 / 2
        self.Vy += ay * dt

    def create_image(self, canv):
        """
        Creates image for PhysicalBall objects

        :param canv: Tk Canvas object
        :return: None
        """
        R = self.R
        self.image = canv.create_oval([0, 0], [2 * R, 2 * R], fill=self.color, outline='')

    def calculate_orbit_parameters (self, obj):
        """
        calculates orbit parametrs of an object in double system
        VcmX, VcmY - correspondent components of velocity of system's center of mass

        returns: list of parametrs
        """
        orbit_parametrs = []
        VcmX = (self.Vx * self.m + obj.Vx * obj.m) / (self.m + obj.m)
        VcmY = (self.Vy * self.m + obj.Vy * obj.m) / (self.m + obj.m)
        V_relative_x = VcmX - self.Vx
        V_relative_y = VcmY - self.Vy
        V_relative = (V_relative_x ** 2 + V_relative_y ** 2) ** 0.5
        x_cm = (self.x * self.m + obj.x * obj.m) / (self.m + obj.m)
        y_cm = (self.y * self.m + obj.y * obj.m) / (self.m + obj.m)
        dist_cm = ((x_cm - self.x) ** 2 + (y_cm - self.y)) ** 0.5
        energy = (V_relative ** 2) / 2 - gravitational_constant * obj.m / dist_cm
        if energy > 0:
            orbit_parametrs += "orpit type = hyperbola, "
        if energy == 0:
            orbit_parametrs += "orpit type = parabola, "
            orbit_parametrs += "eccentricity = 0"
        if energy < 0:
            orbit_parametrs += "orpit type = ellipse, "

        if energy != 0:    
            a = - gravitational_constant * obj.m / (2 * energy)
            orbit_parametrs += "big semiaxis = " + str(a) + ", "

            angle_velocity_radius_vector = abs (math.atan (self.Vy / self.Vx) - math.atan ((y_cm - self.y) / (x_cm - self.x)))

            L = V_relative * dist_cm * math.sin(angle_velocity_radius_vector)

            b = L * (a / (gravitational_constant * obj.m)) ** 0.5
            orbit_parametrs += "small semiaxis = " + str(b)

            e = (1 + 2 * energy * (L / (gravitational_constant * obj.m))**2)
            orbit_parametrs += "eccentricity = " + str(e)

        return orbit_parametrs
        

def create_water(planet, N=80, density=25):
    """
    Creates N water balls around planet.

    :param N: number of molecules
    :return: new list of objects
    """
    molecules = []
    r = 0.7 * math.pi * planet.R / N  # radius of molecule
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
