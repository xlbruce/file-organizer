# File organizer

## Description
A Python file organizer based on optional user defined file extensions.

## Installation

Just run `pip install file-organizer`.

> Python 3.7+ required

## Command line synopsys

```
Usage: organize [OPTIONS] SRC DEST

Options:
  --extensions TEXT       List of extensions to move separated by comma
  --delete / --no-delete  Whether source files must be deleted after they're
                          organized
  -v, --verbose
  --help                  Show this message and exit.
```

## Basic usage example
``` $ organize ~/Downloads ~/Organized```

Executing the above command, will __move__ all files inside `~/Downloads` into separate folders inside `~/Organized` based each file extension.
To __copy__ instead, you can pass the `--no-delete` flag.



### Pull requests are welcome

## TODO

- [ ] Add a dry-run option
- [ ] Improve code
