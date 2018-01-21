# File organizer

## Description
A Python file organizer based on user defined file extensions and destination directories.

## Command line synopsys

```
usage: organizer.py [-h] [-c] [-o] [-v] [--config CONFIG] origin

positional arguments:
  origin           folder which files will be filtered

optional arguments:
  -h, --help       show this help message and exit
  -c, --copy       copy files instead move them
  -o, --overwrite  overwrite existing files
  -v, --verbosity  prints each operation executed
  --config CONFIG  .ini file containing file extensions to organize
```

## Basic usage example
``` $ python organizer.py /Users/myuser/Downloads ```

Executing the above command, will __move__ all files matching your defined extensions into the corresponding also defined destination.

## Configuration file

The configuration file holds your desired extensions to organize and a corresponding folder path to archive it.
The file is a simple python file with the ```.py``` extension, with a arbitrary name. You should modify it as you want following this model:

```
file_extensions=[
    ('.mp3', '/Users/user/My music'),
    ('.pdf', '/Users/user/My pdf'),
    ('.docx','/Users/user/My docs')
]
```

As it is a regular python file, it is possible to use variables to reduce copy and paste jobs:

```
base_path = '/Users/user'
file_extensions=[
    ('.mp3', '%s/My music' % base_path),
    ('.pdf', '%s/My pdf' % base_path),
    ('.docx','%s/My docs' % base_path)
]
```


### Pull requests are welcome

## TODO

- [ ] Add a dry-run option
- [ ] Improve code
