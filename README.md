# Line-Counter
Line-Counter is a simple tool that can help you to calculate the total lines of a file or directory

## Installation

- Requirements: python > 3.0

download the code and run

```shell
$ python setup.py install
```

## Usage

```
lc [-h] [--exclude [EXCLUDE [EXCLUDE ...]]] [--ext [EXT [EXT ...]]] path
positional arguments:
  path                  path of target

optional arguments:
  -h, --help            show this help message and exit
  --exclude [EXCLUDE [EXCLUDE ...]]
                        file or dir to be ignored
  --ext [EXT [EXT ...]]
                        extension of file to be counted
```

## TODO

1. optimizing performance
2. allow ignore file