# -*- coding: utf-8 -*-
"""

A script to parse meteorological reports folder and find patterns

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

import sys
import os
import re

          
def regexMeteoFinder(files, pattern):
    wmoheader_list = []
    n = 0
    for fl in files:
        filepath = '%s/%s' % (subdir, fl)
        f = open(filepath, 'r')
        msg_str = f.read()
        f.close()
        regex = pattern
        regex_matches = re.findall(regex, msg_str)
        if regex_matches:
        #if len(regex_matches) > 1:
            n += 1
            print '\t-- File: %s' % (fl)
            print '\t\tMatches: %s' % (len(regex_matches))
    
        wmoheader = fl.split('_')[-1]
        wmoheader_list.append(wmoheader)
    
    print '\tTotal matches (regex "%s"): %i\n' % (regex, n)
    
    return wmoheader_list

def findDuplicateHeaders(files, wmoheader_list):
    m = 0
    for fl in files:
        wmoheader = fl.split('_')[-1]
        ct = wmoheader_list.count(wmoheader)
        if ct > 1:
            m += 1
            print '\t-- Find duplicate WMO Header: %s' % (fl) 
    
    print '\tTotal matches (duplicate WMO headers): %i\n' % (m)


if __name__ == '__main__':
    
    if len(sys.argv) < 3:
        print '''
        \n --Must provide two arguments: 1) Folder path and 2) Pattern to find.\n 
            python parse_meteoreportsfolder.py [folderpath] [pattern]\n
            Use simple quotes for complex expressions.
        '''
        exit()
    elif len(sys.argv) > 3:
        print '\n --Too many arguments\n'
        exit()

    folder = sys.argv[1]
    pattern = sys.argv[2]

    if not os.path.exists(folder):
        print '\n --Argument error: invalid or missing path.\n'
        exit()
    
    for subdir, dirs, files in os.walk(folder):
        # Walking through folders
        print '\n- Folder: %s' % (subdir)
        
        try:
            wmoheader_list = regexMeteoFinder(files, pattern)
        
            findDuplicateHeaders(files, wmoheader_list)
        except:
            print 'Uhmmm... something happened.'
