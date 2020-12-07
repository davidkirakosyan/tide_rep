import math
from objects import *


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов
    Параметры:
    **input_filename** — имя входного файла
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


def create_water(planet, N=70, density=100):
    '''
    :param: 
    N - mumber of molecules
    :return:
    new list of objects
    '''
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


def parse_space_object_parameters(line, obj):
    """Считывает данные об объекте из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Здесь (x, y) — координаты объекта, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4
    Параметры:
    **line** — строка с описание звезды.
    **space_object** — объект.ф
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
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Параметры:
    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
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
