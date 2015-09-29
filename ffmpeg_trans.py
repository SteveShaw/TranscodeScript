#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on Thu Dec 18 22:59:05 2014

@author: Administrator
"""

import sys
import os
import string
from glob import glob

path = sys.argv[1]
valid_exts = ['.flv','.mp4','.avi','.mkv','.wmv','.m4v']

# width = sys.argv[2]

if __name__ == '__main__':

    cmd_list = []

    width = -1;
    
    if len(sys.argv) == 3:
        width = string.atoi(sys.argv[2])

    files = [y for x in os.walk(path) for y in glob(os.path.join(x[0],'*.*'))]
    for item in files:
        (name, ext) = os.path.splitext(item)
        #if ext.lower()!='.mp4' or ext.lower()!='.avi' or ext.lower()!='.mkv' or ext.lower()!='.wmv': continue
        if ext.lower() not in valid_exts: continue
        output = name + '_00_'
        output += '.mp4'

        if width > 0:
            cmd = \
            'ffmpeg -i "%s" -c:v libx264 -profile:v high -preset slow -vf scale=%d:-1 -c:a copy "%s"' \
            % (item, width, output)
            print cmd
            cmd_list.append(cmd)
        else:
            cmd = \
            'ffmpeg -i "%s" -c:v libx264 -profile:v high -preset slow -c:a copy "%s"'\
            %(item, output)
            print cmd
            cmd_list.append(cmd)
    

    bat_fpath = path + os.path.sep + 'job.sh'
    print bat_fpath
    print len(cmd_list)
    with open(bat_fpath, 'w') as f:
        for cmd in cmd_list:
            f.write(cmd + '\n')
