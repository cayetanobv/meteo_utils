# -*- coding: utf-8 -*-
"""

Parse meteorological reports folder

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
import re

          
def regexMeteoFinder(files):
    wmoheader_list = []
    n = 0
    for fl in files:
        filepath = '%s/%s' % (subdir, fl)
        f = open(filepath, 'r')
        msg_str = f.read()
        f.close()
        regex = 'CNL'
        regex_matches = re.findall(regex, msg_str)
        if regex_matches:
        #if len(regex_matches) > 1:
            n += 1
            print '-- File: %s' % (fl)
            print '\tMatches: %s' % (len(regex_matches))
    
        wmoheader = fl.split('_')[-1]
        wmoheader_list.append(wmoheader)
    
    print 'Total matches (regex "%s"): %i\n' % (regex, n)
    
    return wmoheader_list

def findDuplicateHeaders(files, wmoheader_list):
    m = 0
    for fl in files:
        wmoheader = fl.split('_')[-1]
        ct = wmoheader_list.count(wmoheader)
        if ct > 1:
            m += 1
            print '-- Find duplicate WMO Header: %s' % (fl) 
    print 'Total matches (duplicate WMO headers): %i\n' % (m)


if __name__ == '__main__':
    folder = '/meteofolder'
    
    for subdir, dirs, files in os.walk(folder):
        # Walking through folders
        try:
            wmoheader_list = regexFinder(files)
        
            findDuplicateHeaders(files, wmoheader_list)
            
        except:
            print 'Uhmmm... something happened.'
