#! python3

import os
import shutil


def delete_file(current_path):
    for files in os.listdir(current_path):
        if os.path.isdir(os.path.join(current_path, files)):
            shutil.rmtree(os.path.join(current_path, files))
        else:
            os.remove(os.path.join(current_path, files))


