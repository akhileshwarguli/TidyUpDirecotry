from pathlib import Path
import shutil
from config import FILE_TYPES_DICT


def make_target_folders(target_dir_str):
    for TYPE in FILE_TYPES_DICT:
        try:
            Path(target_dir_str + '/' + TYPE).mkdir()
        except FileExistsError as e:
            print(f"The file '{e.filename}' already exists.")


def move_to_respective_dir(file_object):
    for file_type, extensions in FILE_TYPES_DICT.items():
        if file_object.suffix.lower() in extensions:
            shutil.move(str(file_object.absolute()), str(str(file_object.absolute().parent) + '/' + file_type+'/'))
