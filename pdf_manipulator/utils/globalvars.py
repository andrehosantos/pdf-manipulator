import os


def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

BASE_PATH = '.'
BASE_TMP_PATH = os.path.join(BASE_PATH, 'tmp')
PRINT_PATH = os.path.join(BASE_PATH, 'print')

create_directory(BASE_TMP_PATH)
create_directory(PRINT_PATH)
