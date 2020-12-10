from objects import *


def read_space_objects_data_from_file(input_filename):
    """
    Reads data of celestial bodies from file, creates objects and their images.

    :param input_filename: the uploaded file name
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
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

    for word in x:
        if word.isalpha():
            value = word.lower()
        else:
            value = float(word)
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
    with open(output_filename, 'w') as out_file:
        for obj in objects:
            object_data_string = ''
            features = [obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy]
            for feature in features:
                object_data_string += str(feature) + ' '

            out_file.write(object_data_string + '\n')


if __name__ == "__main__":
    print("This module is not for direct call!")
