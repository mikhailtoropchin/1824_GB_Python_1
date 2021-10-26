# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#    |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
#
#
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации;
# это реальная задача, которая решена, например, во фреймворке django.


import os
import shutil


project_dir = "C:/Users/михаил/PycharmProjects/1824_GB_Python_1/Mikhail_Toropchin_dz_7/my_project"
os.makedirs(os.path.join(project_dir, "templates"), exist_ok=True)

for root, dirs, files in os.walk(project_dir): # гуляем
    for name in files:
        if name.endswith(".html"):
            file_path = os.path.join(root, name) # путь к найденному шаблону
            file_end = file_path.split("templates")  # делим путь по названию папки
            yet_another_path = file_end[0].split("\\") # находим название родительской папки
            if len(yet_another_path) > 2:
                if not os.path.exists(f"{project_dir}/templates/{yet_another_path[-2]}/{name}"):
                    os.makedirs(os.path.join(f"{project_dir}/templates", yet_another_path[-2]), exist_ok=True)
                    shutil.copy2(file_path, f"{project_dir}/templates/{yet_another_path[-2]}")
                else:
                    print(f"Файл {name} в папке templates/{yet_another_path[-2]} уже существует")

if not os.listdir(os.path.join(project_dir, "templates")):
    print("Шаблонов не найдено")
