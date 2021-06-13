#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import shutil


print ('os.getcwd()', os.getcwd())

os.chdir('/home/kibua/git/devDocs')
print ('os.getcwd()', os.getcwd())

os.chdir('/home/kibua/git/devDocs/file')
print ('os.getcwd()', os.getcwd())

print (os.path.join('home', 'kibua', 'git'))

print (os.listdir( os.getcwd()))
print (os.listdir( '/home/kibua/git/devDocs'))

print (os.path.exists('/home/kibua/git/devDocs/file'))
print (os.path.isdir('/home/kibua/git/devDocs/file'))
print (os.path.isfile('/home/kibua/git/devDocs/file'))

print (os.path.abspath(os.getcwd()))
print (os.path.relpath('/home/kibua/git/devDocs/file', '/home/kibua/git'))
print (os.path.commonprefix( ['/home/kibua/git/devDocs/file', '/home/kibua/git']))


base=os.path.basename('/root/dir/sub/file.ext')
print(base)
print (os.path.splitext(base))
print (os.path.splitext(base)[0])
print (os.path.splitext(base)[1])


