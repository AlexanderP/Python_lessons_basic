# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.


# Данный скрипт можно запускать с параметрами:
# python with_args.py param1 param2 param3
import os
import sys

args = sys.argv[1:]


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создание копии файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> - переход в папку")
    print("ls - показать текущий путь")


def get_normal_path(path):
    # if os.path.isabs(path):
    if path[0] == '/' or path[1] == ':':  # не лучшее решение
        return path
    else:
        return os.path.join(os.getcwd(), path)


def make_dir():
    # такую проверку нужно ставить во всех методах, либо вынести в функцию
    if not first:
        print("Необходимо указать имя директории вторым параметром")
        return

    dir_path = get_normal_path(first)

    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(first))
    except FileExistsError:
        print('директория {} уже существует'.format(first))


def copy_file():
    filename = get_normal_path(first)

    if os.path.exists(filename):
        import shutil

        shutil.copy(filename, f'{filename}.copy')
        print(f"Copied {filename}")
    else:
        print("File doesn't exists")
    pass


def remove_file():
    filename = get_normal_path(first)

    if os.path.exists(filename):
        if os.path.isdir(filename):
            if input("Are You sure want to delete this folder? [Y/N] ").lower() == 'y':
                os.rmdir(filename)
        else:
            if input("Are You sure want to delete this file? [Y/N] ").lower() == 'y':
                os.remove(filename)

    print(f"Removed {filename}")
    pass


def change_directory():
    try:
        dir_path = get_normal_path(first)
        os.chdir(dir_path)
        print(f"Changed path to {dir_path}")
    except:
        print("Can't change directory")
    pass


def show_directory_path():
    cur_path = os.getcwd()

    print(f"Current path is {cur_path}")
    pass


do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_directory,
    "ls": show_directory_path,
}

try:
    action = args[0]
except:
    action = None

try:
    first = args[1]
except:
    first = None

try:
    second = args[2]
except:
    second = None

if action:
    if do.get(action):
        do[action]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
else:
    print("Type command arg please!")
    print_help()
