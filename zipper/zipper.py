#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys
import os
import time

# $ 7za a  -pmy_password archive.7z a_directory
# $ 7za a -p0000 test_dir.7zip ./temp/
# $ 7za x -p0000 -y test_dir.7zip
# $ za x -p0000 -y -O./backup test_dir.7zip
# $ 7za a -p0000 -y -O./backup_dir test_dir.7zip
# On Linux/Unix, in order to backup directories you must use tar :
# - to backup a directory  : tar cf - directory | 7za a -si -y directory.tar.7z
# - to restore your backup : 7za x -so directory.tar.7z | tar xf -

def backup(archive_dir, backup_dir, password=True, max_files=10):
    curdate = time.strftime('%Y%m%d-%H%M%S', time.localtime(time.time()))

    dirName = os.path.basename(archive_dir)
    if (dirName == ""):
        dirName = os.path.basename(os.path.dirname(archive_dir))
    
    zipfile = os.path.join(backup_dir, dirName +'_'+ curdate+'.7z')

    passwd =''
    if password == True:
        passwd += '-p' + time.strftime('%Y%m%d', time.localtime(time.time())) + ' '

    cmd = '7za a -y -bso0 '
    cmd +=  passwd + ' '
    cmd +=  zipfile + ' '
    cmd +=  archive_dir + ' '
    # print (cmd)

    os.system(cmd)

    if os.path.exists(backup_dir):
        backuplist = [f for f in os.listdir(backup_dir) if f.endswith('.7z')]
        backuplist.sort()

        while ( len(backuplist) > max_files):
            cmd = 'rm ' + os.path.join (backup_dir, backuplist[0])
            os.system(cmd)
            del backuplist[0]

def main():
    archive_dir = os.path.join (os.getcwd(), 'working_dir')
    backup_dir = os.path.join (os.getcwd(), 'test_dir')

    for i in range(1, len(sys.argv)):
        if (i == 1):
            archive_dir = sys.argv[1]
        elif (i == 2):
            backup_dir = sys.argv[2]
        else:
            print('*** Error *** : Unknown parametMGer')
            exit(1)

    if (len(sys.argv) < 2):
        print('Usage: ./zipper.py [archive_dir] [backup_dir]')
        exit(-1)

    backup (archive_dir, backup_dir, password=True)

if __name__ == "__main__":
    main()