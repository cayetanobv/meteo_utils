#! /usr/bin/env python

"""

A script to rename files (batch on a folder tree) 
with regular expressions

Author: Cayetano Benavent, 2014

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
MA 02110-1301, USA.

"""

import os
import sys
import re
import shutil

def batchRegExRename(folder, new_folder, pattern, new_str):
    
    if os.path.exists(new_folder):
        shutil.rmtree(new_folder)
        
    shutil.copytree(folder, new_folder)
    
    for subdir, dirs, files in os.walk(new_folder):
        #Walking through folders
        for fl in files:
            filepath = '%s/%s' % (subdir, fl)
            fname = os.path.splitext(fl)[0]
            ext = os.path.splitext(fl)[1]
            
            if re.search(pattern, fname):
                new_file_name = re.sub(pattern, new_str, fname)
                new_path = os.path.join(subdir, new_file_name + ext)
                shutil.copy(os.path.join(subdir, fl), new_path)
                os.remove(filepath)
                print 'Filename changed: ', new_path
          

if __name__ == '__main__':
    
    
    if len(sys.argv) < 5:
        print '''
    \n --Must provide 4 arguments: 
        1) Source folder path
        2) Destiny folder path
        3) Pattern to find (regular expression)
        4) string to replace
        
        python batch_regex_rename.py [src] [dst] [regex] [new_str]
        
        Use simple quotes for regular expressions\n
        '''
        exit()
    elif len(sys.argv) > 5:
        print '\n --Too many arguments\n'
        exit()

    src = sys.argv[1]
    dst = sys.argv[2]
    pattern = sys.argv[3]
    new_str = sys.argv[4]

    if not os.path.exists(src):
        print '\n --Argument error: Source path does not exist.\n'
        exit()
    
    try:
        print '\nRenaming...'
        batchRegExRename(src, dst, pattern, new_str)
        print '\nFinished work!\n'
    except:
        print '\nUhmmm... something happened.\n'

