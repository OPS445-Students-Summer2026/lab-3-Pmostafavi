#!/usr/bin/env python3

# Author ID: Pmostafvi

import subprocess

def free_space():
    p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    output = p.communicate()[0]
    return output.decode('utf-8').strip()

print(free_space())