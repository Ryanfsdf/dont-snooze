#! python3

import os


def reverse_file(current_path):
    for files in os.listdir(current_path):
        if os.path.isdir(os.path.join(current_path, files)):
            reverse_file(os.path.join(current_path, files))
        else:
            file = files.split('.')[0]
            if file != '':
                os.rename(os.path.join(current_path, files),
                          os.path.join(current_path, file[::-1]) + '.' +
                          files.split('.')[1])


