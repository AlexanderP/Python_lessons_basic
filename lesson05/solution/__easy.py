# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os


def create_directory(path):
    if not os.path.exists(path):
        try:
            os.mkdir(path)
            print(f"Successfully created ({path})")
        except:
            print("Error with creating directory")
    else:
        print('Directory already exists')

    # try:
    #     os.mkdir(path)
    #     print(f"Successfully created ({path})")
    # except FileExistsError:
    #     print('Directory already exists')


def remove_directory(path):
    if os.path.exists(path):
        try:
            os.rmdir(path)
            print(f"Successfully deleted ({path})")
        except:
            print("Error with deleting directory")
    else:
        print('Directory already exists')


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def list_dir(path, only_directories=False):
    try:
        dir_content = os.listdir(path)

        if only_directories:
            dir_content = filter(lambda x: os.path.isdir(x), dir_content)

        print(dir_content)
    except:
        print('Error with listing directory')


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
def copy_file():
    import shutil

    cur_file = __file__
    shutil.copy(cur_file, f'{cur_file}.copy')
