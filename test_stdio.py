#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys

def readFile(filepath):
    try:
        f = open(filepath, "rb")
    except:
        print('*** Error *** : File open error', filepath)
        exit(1)

    data = f.read()
    print ('readFile()', len(data))
    f.close()
    return len(data)

def readLargeFile(filepath):
    buffer = bytearray()
    try:
        f = open(filepath, "rb")
    except:
        print('*** Error *** : File open error', filepath)
        exit(1)
    while True:
        data = f.read()
        if not data:
            break
        buffer.extend(data)
    print ('readLargetFile()', len(buffer))
    f.close()
    return buffer

def test_stdio():
    print (sys.stdin)
    print ('python arguments: ')
    for i in range(1, len(sys.argv)):
        print('\t', sys.argv[i])

    print ('stin buffer: ')
    buffer = bytearray()
    if sys.stdin.isatty():
        print ('terminal mode: do nothing')
    else:
        buffer=sys.stdin.read()
    
    print (buffer)


if __name__ == "__main__":
    test_stdio()
