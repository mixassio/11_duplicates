import os
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--filepath', nargs='?', type=str)
    return parser


def create_filelist(filepath):
    tree = os.walk(filepath)
    files = {}
    for element in tree:
        for file in element[2]:
            dir_file = element[0] + '/' + file
            if os.path.isfile(dir_file):
                size_file = os.path.getsize(dir_file)
                try:
                    files[size_file][file].append(dir_file)
                except KeyError:
                    files[size_file] = {file: [dir_file, ]}
    return files


def print_result(files):
    for size, file in files.items():
        for file, paths in file.items():
            if len(paths) > 1:
                print('file = "{}", size = "{}"'.format(file, size))
                print(paths)

if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    if namespace.filepath:
        filepath_in = os.path.abspath(namespace.filepath)
    else:
        filepath_in = os.path.abspath('/')

    files = create_filelist(filepath_in)
    print_result(files)
