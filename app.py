import click
import re
import os
import shutil

def file_extension(filename):
    m = re.search(r'(?<=\.).*$', filename) 
    if not m:
        return None

    return m.group(0)


def filter_all(filename):
    return True


def create_filter(extensions=list()):
    if not extensions:
        return filter_all

    def filter(filename):
        if not filename:
            return False

        extension = file_extension(filename)
        return extension in extensions
    return filter
     

def get_files(src, file_filter):
    filenames = os.listdir(src)
    fullnames = (os.path.join(src, filename) for filename in filenames)
    return filter(file_filter, fullnames)
     

def valid_extensions(extensions_str):
    valid = []
    if extensions_str:
        valid = extensions_str.split(',')

    return valid
    

def create_operate(override):
    operate = shutil.move
    if not override:
        operate = shutil.copy

    def wrapper(src, dest):
        return operate(src, dest) 

    return wrapper
    

@click.command()
@click.argument('src', type=click.Path(exists=True, resolve_path=True))
@click.argument('dest',type=click.Path(exists=False, writable=True, resolve_path=True))
@click.option('--extensions', type=click.STRING, help='List of extensions to move separated by comma')
@click.option('--override/--no-override', default=False)
@click.option('-v', '--verbose', count=True)
def main(src, dest, extensions, override, verbose):
    file_filter = create_filter(valid_extensions(extensions))
    src_files = list(get_files(src, file_filter))
    operate_file = create_operate(override)
    for src_file in list(src_files):
        operate_file(src_file, dest)

    print("Done")

if __name__ == '__main__':
    main()


