import numpy as np


gravitational_constant = 6.67408E-11


def calculate_force(body, objects):
    """
    Calculates force applied to the body

    :return: None
    """

    body.Fx = body.Fy = 0
    for obj in objects:
        if body == obj:
            continue  # doesn't affect on itself
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx += gravitational_constant * body.m * obj.m * (obj.x - body.x) / (r**3)
        body.Fy += gravitational_constant * body.m * obj.m * (obj.y - body.y) / (r**3)


def colliders(body, objects):
    """
    :return: list of objects which are colliding with the body
    """
    colliders = []
    for obj in objects:
        if (obj.x - body.x)**2 + (obj.y - body.y)**2 <= (obj.R + body.R)**2:
            colliders.append(obj)
    
    return colliders


def collisions(body, objects):
    """
    Recalculates velocity of the body after collisions with objects

    :return: None
    """
    M = body.m
    V = np.array([body.Vx, body.Vy])
    X, Y = body.X, body.Y

    for obj in colliders(body, objects):
        m = obj.m
        v = np.array([body.vx, body.vy])
        x, y = obj.x, obj.y

        #FIXME
        # in case objects intersect because of not enough small dt, we pull the body out of the object before collision calculations

        Vc = (M*V + m*v) / (M + m)  # velocity of center of mass
        P1 = m * M / (M + m) * (V - v)  # momentum of the body in the frame of reference of the center of mass before collision
        l = np.array([x - X, y - Y])  
        delta_P = -2 * np.dot(P1, l) * l / np.sum(l**2)
        P2 = P1 + delta_P  # after collision
        V_new = P2 / M + Vc  
    
    body.Vx, body.Vy = V_new