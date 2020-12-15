from objects import *


def read_space_objects_data_from_file(input_filename):
    """
    Reads data of celestial bodies from file, creates objects and their images.

    :param input_filename: the uploaded file name
    """

    objects = []
    with open(input_filename) as input_file:
        lines = input_file.readlines()

        if len(lines) == 0:
            raise ImportError("Empty file is uploaded.")

        for line in lines:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            obj = PhysicalBall()
            parse_space_object_parameters(line, obj)
            objects.append(obj)
    return objects


def parse_space_object_parameters(line, obj):
    """
    Reads object data from line. Input line has the following syntax:
    Planet <radius> <color> <mass> <x> <y> <Vx> <Vy>

    :param line: string with planet's data.
    :param obj: PhysicalBall object
    :return: None
    """
    x = line.split()  # skipping first element
    res = []

    if len(x) < 8:
        raise ImportError("Wrong file is uploaded. Please check data syntax.")

    for i, word in enumerate(x):
        if word.isalpha():
            value = word.lower()
        else:
            value = float(word)

        if i in [0, 2]:
            if not value.isalpha():
                raise ImportError("Wrong file is uploaded. Please check data syntax.")
        else:
            if not isinstance(value, float):
                raise ImportError("Wrong file is uploaded. Please check data syntax.")

        res.append(value)

    obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy = res


def write_space_objects_data_to_file(output_filename, objects):
    """
    Saves celestial bodies data into file in the following format:
    Planet <radius> <color> <mass> <x> <y> <Vx> <Vy>

    :param output_filename: file in which will be written the data
    :param objects: list with planets
    :return: None
    """

    for obj in objects:
        if obj.type == 'moon':
            Moon = PhysicalBall()
            Moon.type, Moon.R, Moon.color, Moon.m, Moon.x, Moon.y, Moon.Vx, Moon.Vy = obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy
        if obj.type == 'earth':
            Earth = PhysicalBall()
            Earth.type, Earth.R, Earth.color, Earth.m, Earth.x, Earth.y, Earth.Vx, Earth.Vy = obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy
    orbit_parameters_Earth = Earth.calculate_orbit_parameters (Moon)
    orbit_parameters_Moon = Moon.calculate_orbit_parameters (Earth)
            
    with open(output_filename, 'w') as out_file:
        for obj in objects:
            object_data_string = ''
            features = [obj.type, obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy]
            if obj.type == 'moon':
                features += orbit_parameters_Moon
            if obj.type == 'earth':
                features += orbit_parameters_Earth
            for feature in features:
                object_data_string += str(feature) + ' '

            out_file.write(object_data_string + '\n')


if __name__ == "__main__":
    print("This module is not for direct call!")
