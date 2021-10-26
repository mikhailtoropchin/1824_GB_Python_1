# Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp

import os


def make_dir(path, names):
    """
    создает заготовку для проекта в виде структуры папок
    :path: путь, где будет создана заготовка
    :names: список или кортеж с названиями папок
    """
    if not os.path.exists("my_project"):
        os.mkdir(os.path.join(path, "my_project")) # можно как вариант сюда переменную, чтобы менять общее название
    else:
        print("Директория 'my_project' по данному пути уже существует, папки будут созданы внутри, если их не было.")
    my_project = os.path.join(path, "my_project")
    for name in names:
        if not os.path.exists(f"{my_project}\{name}"):
            temp = os.path.join(my_project, name)
            os.makedirs(temp, exist_ok=True)
        else:
            print(f"папка {name} уже существует")


project_dir = os.path.dirname(__file__) # путь
dir_names = ['settings', 'adminapp', 'authapp', 'mainapp'] # названия папок

make_dir(project_dir, dir_names)

# print(os.listdir("my_project"))
