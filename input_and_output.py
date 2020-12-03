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
    x = line.split()[1:]  # skipping first element
    res = []

    for word in x:
        if word.isalpha():
            value = word
        else:
            value = float(word)
        res.append(value)

    obj.R, obj.color, obj.m, obj.x, obj.y, obj.Vx, obj.Vy = res


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
            features = [obj.m, obj.x, obj.y, obj.Vx, obj.Vy,
                        obj.R, obj.color, obj.drag_readiness]
            for feature in features:
                object_data_string += str(feature) + ' '

            out_file.write(object_data_string + '\n')


if __name__ == "__main__":
    print("This module is not for direct call!")
