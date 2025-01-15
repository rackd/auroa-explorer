import os

def get_filenames_in_dir(dir):
    filenames = []

    for file in os.listdir(dir):
        if os.path.isfile(file):
            filenames.append(file)

def get_abs_paths_in_dir(dir):
    directory = dir
    paths = []

    for file in os.listdir(directory):
        absf = os.path.abspath(file)
        if os.path.isfile(file):
            paths.append(file)