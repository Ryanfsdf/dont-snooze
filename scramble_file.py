#! python3

import os
from random import shuffle


def scramble_file(current_path):
    for files in os.listdir(current_path):
        if os.path.isdir(os.path.join(current_path, files)):
            scramble_file(os.path.join(current_path, files))
        else:
            file = files.split('.')[0]
            if file != '':
                list_char = list(file)
                shuffle(list_char)
                os.rename(os.path.join(current_path, files),
                          os.path.join(current_path, ''.join(list_char)) +
                          '.' + files.split('.')[1])


