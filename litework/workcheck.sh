#!/bin/bash

# make sure script is being run as source
if [ "${BASH_SOURCE[0]}" == "${0}" ]; then
    echo "[-] You must source this script to run it."
    exit
fi

########################################

# make sure environment variables exist
if [ -z "$VENVDIR" ]; then
    echo "[!] Must define '\$VENVDIR' as environment variable (default ~/.venvs/)."
fi

if [ -z "$WORKDIR" ]; then
    echo "[!] Must define '\$WORKDIR' as environment variable."
fi

if [ -z "$VENVLABEL" ]; then
    echo "[!] Must define '\$VENVLABEL' as environment variable (default 'venv.txt')."
fi

if [ -z "$VENVDIR" ] || [ -z "$WORKDIR" ] || [ -z "$VENVLABEL" ]; then
    return
fi

# (for reference)