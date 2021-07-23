import sys
import os
import pathlib

from cst import remove_u_prefix

EXTENSION = '.py'


def get_files(root_path: str, extension: str):
    for root, dirs, files in os.walk(root_path):
        source_files = [
            f'{root}/{f}'
            for f in files
            if f.endswith(extension)
        ]
        yield from source_files


def read_file(path: str) -> str:
    return pathlib.Path(path).read_text()


def write_file(path: str, content: str) -> None:
    pathlib.Path(path).write_text(content)


def run(root_path: str) -> None:
    for file in get_files(root_path, EXTENSION):
        print('Process file %s' % file)
        try:
            code = read_file(file)
            write_file(file, remove_u_prefix(code))
        except Exception as e:
            print(e)
            continue

    print('Processing complete')


if __name__ == '__main__':
    _, root_path = sys.argv
    run(root_path)
