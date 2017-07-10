# Anti-Duplicator

The script searches for duplicate files by the specified path.
        The input accepts the directory, if it is not specified, by default - the root directory.
        A duplicate is a file with the same size and name.

# How use

Example of script launch on Linux, Python 3.5:

usage: duplicates.py [-filepath] filepath

if filepath is None, filepath = '/'

```#!bash

$ python3 duplicates.py -f /Users/mixassio/test
file = "java_error_in_pycharm_621.log", size = "82734"
['/Users/mixassio/test/java_error_in_pycharm_621.log', '/Users/mixassio/test/test2/java_error_in_pycharm_621.log'
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
