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
usage: lc [-h] [-ef [EXCLUDE_FILE [EXCLUDE_FILE ...]]]
          [-ed [EXCLUDE_DIR [EXCLUDE_DIR ...]]]
          [-et [EXCLUDE_EXT [EXCLUDE_EXT ...]]]
          [-at [ACCEPT_EXT [ACCEPT_EXT ...]]]
          path

positional arguments:
  path                  path of target

optional arguments:
  -h, --help            show this help message and exit
  -ef [EXCLUDE_FILE [EXCLUDE_FILE ...]], --exclude-file [EXCLUDE_FILE [EXCLUDE_FILE ...]]
                        file to be ignored
  -ed [EXCLUDE_DIR [EXCLUDE_DIR ...]], --exclude-dir [EXCLUDE_DIR [EXCLUDE_DIR ...]]
                        dir to be ignored
  -et [EXCLUDE_EXT [EXCLUDE_EXT ...]], --exclude-ext [EXCLUDE_EXT [EXCLUDE_EXT ...]]
                        extension of file to be ignored
  -at [ACCEPT_EXT [ACCEPT_EXT ...]], --accept-ext [ACCEPT_EXT [ACCEPT_EXT ...]]
                        extension of file to be counted
```

