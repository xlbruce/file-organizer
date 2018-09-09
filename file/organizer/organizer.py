import argparse
import imp
import os
import shutil
import sys


def operate(func, src, dst):
    if not args.overwrite:
        if os.path.exists(dst):
            answer = str(input('Overwrite file "{}"?   (y/n/a) '.format(dst))).lower()
            if answer == 'a':
                args.overwrite = True
            elif answer != 'y':
                return

    if args.verbosity:
        action = 'Moving'
        if args.copy:
            action = 'Copying'
        print('{} file [{}] to [{}]'.format(action, src, dst))

    func(src, dst)


def process_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('origin', help='folder which files will be filtered')
    parser.add_argument('-c', '--copy', help='copy files instead move them',
                        action='store_true')
    parser.add_argument('-o', '--overwrite', help='overwrite existing files',
                        action='store_true')
    parser.add_argument('-v', '--verbosity', help='prints each operation executed', action='store_true')
    parser.add_argument('--config', help='.ini file containing file extensions to organize')
    return parser.parse_args()

def main(args):
    origin = os.path.abspath(args.origin)

    if args.config:
        config_path = os.path.abspath(os.path.expanduser(args.config))
    else:
        config_path = os.path.abspath('config.py')

    if not os.path.exists(config_path):
        print('File not found: {}'.format(config_path))
        sys.exit(1)

    config = imp.load_source('config', config_path)

    if not os.path.exists(origin):
       print('Folder "{}" not found'.format(origin))
       sys.exit(1)

    action = shutil.move
    if args.copy:
        action = shutil.copy

    for dir, subdirs, files in os.walk(origin):
        for file in files:
            for extension, ext_destination in config.file_extensions:
                if file.endswith(extension):
                    abs_file = os.path.abspath('{}/{}'.format(dir,file))
                    abs_destination = os.path.abspath(os.path.expanduser(ext_destination))
                    if not os.path.exists(abs_destination):
                        os.makedirs(abs_destination)

                    operate(action, abs_file, os.path.join(abs_destination, file))
                    break

    print('Done')

if __name__ == '__main__':
    args = process_args()
    main(args)
