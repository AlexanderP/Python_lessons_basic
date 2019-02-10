import os
import os.path
import re
import shutil
import sys


def check_name(name):
    pattern_win = r'[\<\>\:"/\\\|\?\*]'
    pattern_posix = r'[\0/]'
    system = os.name
    if system == 'posix':
        if re.search(pattern_posix, name):
            # print('Недопустимое имя.')
            return False
    else:
        if re.search(pattern_win, name) or name.endswith('.'):
            # print('Недопустимое имя.')
            return False
    if name == '':
        # print('Пустое имя.')
        return False
    return True


def my_chdir(dir_name):
    if os.path.isdir(dir_name):
        try:
            os.chdir(dir_name)
            print(f'Успешно перешли в директорию {dir_name}')
        except (OSError, PermissionError):
            print(f"Невозможно перейти в директорию {dir_name}")
    else:
        print(f'Невозможно перейти в директорию {dir_name}')


def my_mkdirs(*dirs):
    for _dir in dirs:
        if not check_name(_dir) or os.path.exists(_dir):
            print(f'Невозможно создать директорию {_dir}')
        else:
            try:
                os.mkdir(_dir)
                print(f"Директория {_dir} успешно создана")
            except (OSError, PermissionError):
                print(f"Невозможно создать директорию {_dir}")


def my_ls_dir(dir=os.curdir):
    print("Список директорий:")
    print(*sorted([f'{x}' for x in os.listdir(dir) if os.path.isdir(x)]),
          sep='\n')


def my_ls(dir=os.curdir):
    print("Список файлов:")
    print(*sorted([f'{x}' for x in os.listdir(dir)]),
          sep='\n')


def my_rmdirs(*dirs):
    for _dir in dirs:
        if os.path.isdir(_dir):
            try:
                shutil.rmtree(_dir, ignore_errors=False)
                print(f"Директория {_dir} удаленна")
            except Exception:
                print(f"Невозможно удалить директорию {_dir}")
        elif os.path.isfile(_dir):
            print(f"{_dir} является файлом")
        else:
            print(f"Директория {_dir} не существует")


def my_cp(name, copy_name):
    copy_path = os.path.join(os.getcwd(), copy_name)
    file_path = os.path.join(os.getcwd(), name)
    if os.path.exists(copy_path):
        print(f"Ошибка. Файл(директория) с именем {copy_name} существует.")
        return
    if os.path.isdir(file_path):
        print(f"Ошибка. {name} директория.")
        return
    elif os.path.isfile(file_path):
        shutil.copy(file_path, copy_path)
        print(f"Файл скопирован. {name} --> {copy_name}")
    else:
        print(f"Ошибка. Файла с именем {name} не существует.")
        return


# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

if __name__ == '__main__':
    dir = os.curdir
    # создадим директории:
    my_mkdirs(*[f'dir_{x}' for x in range(1, 10)])
    # выведем их
    my_ls_dir()
    # удалим их
    my_rmdirs(*[f'dir_{x}' for x in range(1, 10)])
    name_file = sys.argv[0]
    my_cp(name_file, name_file + '.copy')
