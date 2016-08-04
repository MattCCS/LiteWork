#!/usr/bin/env python3

import os
import pathlib
import subprocess
import sys

TRUE_STDOUT = sys.stdout  # http://stackoverflow.com/questions/21202403/how-to-redirect-the-raw-input-to-stderr-not-stdout
sys.stdout = sys.stderr  # ALL output will go to stderr


def send(lst):
    assert isinstance(lst, list)
    s = subprocess.list2cmdline(lst)
    TRUE_STDOUT.write(s + '\n')
    TRUE_STDOUT.flush()  # https://www.turnkeylinux.org/blog/unix-buffering


_HOME = os.path.expanduser('~')
CD_BACK = ['cd', '-']


def CD(path):
    return ['cd', path]

CD_HOME = CD(_HOME)

# path = raw_input("Favorite folder? ")

send(['ps'])

# send(['echo', _HOME])
# send(CD_HOME)
# send(CD_BACK)

send(['cd', '/Users/matt/Documents'])
send(['pwd'])
# send(CD(os.path.expanduser(path)))
send(CD_BACK)

send(['echo', 'good'])
send(['stophere'])
send(['echo', 'bad'])
