import click
import re
import os
import sys

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
    files = os.listdir(src)
    return filter(file_filter, files)
     
def valid_extensions(extensions_str):
    valid = []
    if extensions_str:
        valid = extensions_str.split(',')

    return valid
    
@click.command()
@click.argument('src', type=click.Path(exists=True, resolve_path=True))
@click.argument('dest',type=click.Path(exists=False, writable=True, resolve_path=True))
@click.option('--extensions', type=click.STRING, help='List of extensions to move separated by comma')
@click.option('--override/--no-override', default=False)
@click.option('-v', '--verbose', count=True)
def main(src, dest, extensions, override, verbose):
    file_filter = create_filter(valid_extensions(extensions))
    src_files = get_files(src, file_filter)

if __name__ == '__main__':
    main()


