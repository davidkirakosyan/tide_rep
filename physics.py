import numpy as np

gravitational_constant = 6.67408E-11


def calculate_force(body, objects):
    """
    Calculates force applied to the body.

    :param body: object on which are applied forces.
    :param objects: list of all physical objects
    :return: None
    """

    body.Fx = body.Fy = 0
    for obj in objects:
        if body == obj:
            continue  # doesn't affect on itself
        r = ((body.x - obj.x) ** 2 + (body.y - obj.y) ** 2) ** 0.5
        if body.type == 'earth':
            force_factor = 0.001
        elif obj.type == 'earth':
            force_factor = 0.01
        elif obj.type == 'moon':
            force_factor = 0.01
        elif obj.type == 'water':
            force_factor = 0.001
        elif obj.type == 'moon' and body.type == 'water':
            force_factor = 15
        else:
            force_factor = 1
        body.Fx += gravitational_constant * body.m * obj.m * (obj.x - body.x) / (r ** 3) * force_factor
        body.Fy += gravitational_constant * body.m * obj.m * (obj.y - body.y) / (r ** 3) * force_factor


def colliders(body, objects):
    """
    Determines which objects are colliding with body.

    :param body: PhysicalBall object with which others are colliding
    :param objects: list of all celestial bodies.
    :return: list of colliding objects.
    """
    colliders = []
    for obj in objects:
        if body == obj:
            continue  # doesn't affect on itself
        if (obj.x - body.x) ** 2 + (obj.y - body.y) ** 2 <= (obj.R + body.R) ** 2:
            colliders.append(obj)

    return colliders


def collisions(body, objects):
    """
    Recalculates velocity of the body after collisions with objects.
    Prevents objects to pass through each other.

    :param body: PhysicalBall object
    :param objects: list of all celestial bodies.
    :return: None
    """
    M = body.m
    V = np.array([body.Vx, body.Vy])
    X, Y = body.x, body.y

    V_new = V
    for obj in colliders(body, objects):
        m = obj.m
        v = np.array([obj.Vx, obj.Vy])
        x, y = obj.x, obj.y

        l = np.array([x - X, y - Y])
        if obj.type != 'earth':
            l_normalized = l / np.linalg.norm(l)
            x, y = np.array([X, Y]) + l_normalized * (body.R + obj.R)
            obj.x, obj.y = x, y

        Vc = (M * V + m * v) / (M + m)  # velocity of center of mass
        P1 = m * M / (M + m) * (
                V - v)  # momentum of the body in the frame of reference of the center of mass before collision
        delta_P = -2 * np.dot(P1, l) * l / np.sum(l ** 2)
        P2 = P1 + delta_P  # after collision
        if body.type == 'earth':
            recovery_factor = 0
        if body.type == 'water':
            recovery_factor = 0
        else:
            recovery_factor = 1
        V_new = P2 / M + Vc * recovery_factor

    body.Vx, body.Vy = V_new

if __name__ == "__main__":
    print("This module is not for direct call!")
