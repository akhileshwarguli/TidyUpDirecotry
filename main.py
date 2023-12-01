from pathlib import Path
from utils import move_to_respective_dir, make_target_folder
from sys import argv

TARGET_DIR = '/Users/akhil/Downloads'
try:
    if argv[1]:
        TARGET_DIR = argv[1]
        print ('Target directory : '+TARGET_DIR)
except IndexError as e:
    print('No Target directory provided. Considering default : '+TARGET_DIR)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    download_dir_path = Path(TARGET_DIR)

    if download_dir_path.exists():
        # make_target_folders(TARGET_DIR)
        for file_obj in download_dir_path.glob('*.*'):
            move_to_respective_dir(file_obj)
    else:
        print(f'Target directory does not exists : {TARGET_DIR}')
