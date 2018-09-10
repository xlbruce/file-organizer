#!/usr/bin/env python3

import click
import re
import os
import shutil

from itertools import groupby

def file_extension(filename):
    m = re.search(r'(?<=[^/\\]\.).*$', filename) 
    if not m:
        return None

    return m.group(0)


def filter_all(filename):
    return bool(file_extension(filename))


def create_filter(extensions=list()):
    if not extensions:
        return filter_all

    def filter(filename):
        if not filename:
            return False

        return file_extension(filename) in extensions
    return filter
     

def get_files(src, file_filter):
    filenames = next(os.walk(src))[2]
    filenames = filter(file_filter, filenames)
    fullnames = (os.path.join(src, filename) for filename in filenames)
    return list(filter(file_filter, fullnames))
     

def validate_extensions(extensions_str):
    valid = []
    if extensions_str:
        valid = extensions_str.split(',')

    return valid
    

def create_operate(delete):
    operate = shutil.move
    if not delete:
        operate = shutil.copy

    def wrapper(src, dest):
        try:
            return operate(src, dest) 
        except shutil.Error as e:
            print(f"Error while operating over ({src},{dest})")
            print(e)
            return None

    return wrapper
    
    
@click.command()
@click.argument('src', type=click.Path(exists=True, resolve_path=True))
@click.argument('dest',type=click.Path(exists=False, writable=True, resolve_path=True))
@click.option('--extensions', type=click.STRING, help='List of extensions to move separated by comma')
@click.option('--delete/--no-delete', default=True, help="Whether source files must be deleted after they're organized")
@click.option('-v', '--verbose', count=True)
def main(src, dest, extensions, delete, verbose):
    valid_extensions = validate_extensions(extensions)
    file_filter = create_filter(valid_extensions)
    operate_file = create_operate(delete)
    src_files = get_files(src, file_filter)

    groups = groupby(src_files, file_extension)
    for extension, files in groups:
        dest_path = os.path.join(dest, extension)
        if not os.path.exists(dest_path):
            os.makedirs(dest_path)
        for src_file in list(files):
            operate_file(src_file, dest_path)

    print("Done")

if __name__ == '__main__':
    main()


