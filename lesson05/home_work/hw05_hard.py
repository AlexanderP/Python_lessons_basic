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

import os
import shutil
import sys

from easy import check_name, my_chdir

print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> <copy_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл")
    print("cd <full_path or relative_path> - меняет текущую директорию на"
          " указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def my_cd():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    my_chdir(dir_name)


def my_cp():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if not copy_name:
        print("Необходимо указать имя нового файла третьим параметром")
        return
    if dir_name == copy_name or (
            os.name == 'nt' and dir_name.lower() == copy_name.lower()):
        print("Ошибка. Название файла и нового файла одинаковые")
        return
    if not check_name(dir_name):
        print("Ошибка. Недопустимое имя файла")
        return
    if not check_name(copy_name):
        print("Ошибка. Недопустимое имя нового файла")
        return
    copy_path = os.path.join(os.getcwd(), copy_name)
    file_path = os.path.join(os.getcwd(), dir_name)
    if os.path.exists(copy_path):
        print(f"Ошибка. Файл(директория) с именем {copy_name} существует.")
        return
    if os.path.isdir(file_path):
        print(f"Ошибка. {dir_name} директория.")
        return
    elif os.path.isfile(file_path):
        shutil.copy(file_path, copy_path)
        print(f"Файл скопирован. {dir_name} --> {copy_name}")
    else:
        print(f"Ошибка. Файла с именем {dir_name} не существует.")
        return


def my_rm():
    if not dir_name:
        print("Необходимо указать имя файла вторым параметром")
        return
    if not check_name(dir_name):
        print("Ошибка. Недопустимое имя файла")
        return
    file_path = os.path.join(os.getcwd(), dir_name)
    if os.path.isdir(file_path):
        print(f"Ошибка. {dir_name} директория.")
        return
    elif os.path.isfile(file_path):
        answer = input(f'Удалить файл {dir_name}[y/n]: ')
        if answer.lower() == 'y':
            try:
                os.remove(file_path)
                print(f"Файл {dir_name} удален")
            except (OSError, PermissionError):
                print(f"Невозможно удалить файл {file_path}")
        else:
            print('Отмена удаления')
    else:
        print(f"Ошибка. Файла с именем {dir_name} не существует.")
        return


def my_ls():
    print('Полный путь к текущей директории:')
    print(os.getcwd())


do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": my_cp,
    "cd": my_cd,
    "rm": my_rm,
    "ls": my_ls
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    copy_name = sys.argv[3]
except IndexError:
    copy_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
