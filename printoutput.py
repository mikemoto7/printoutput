#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Global printout function to allow us to use the --debug_linenum param.
"""

import sys, os, re

scriptName = os.path.basename(os.path.abspath(sys.argv[0])).replace('.pyc', '.py')

# If this script is called via a symbolic link:
# this returns the symbolic link's directory:
# scriptDir = os.path.dirname(os.path.abspath(sys.argv[0]))
# this returns the symbolic link's target's directory:
scriptDir = os.path.dirname(os.path.realpath(sys.argv[0]))

sys.path.append(scriptDir)

if sys.version_info[0] == 3:  # for python3
    xrange = range

#=============================================

# For error messages

import inspect

def srcLineNum(caller=1):
    callerframerecord = inspect.stack()[caller] # caller=0 represents this line
                                                # caller=1 represents line at caller
                                                # caller=2 represents line at the caller's caller
    frame = callerframerecord[0]
    info = inspect.getframeinfo(frame)
    # print info.filename                       # __FILE__     -> Test.py
    # print info.function                       # __FUNCTION__ -> Main
    # print info.lineno                         # __LINE__     -> 13
    return str(info.lineno), os.path.basename(info.filename)

#============================================= 

global printout_format
printout_format = 0

def printout(*params):
    global printout_format
    separator = ''
    for param in params:
        if printout_format == 1:
            line_num, filename = srcLineNum(caller=2)
            sys.stdout.write(filename + ',' + line_num + ':')
        sys.stdout.write(str(param) + '\n')


        """
        param_str = ''

        if 'byte' in str(type(param)):
            param_str = param.decode("UTF-8")

        elif 'int' in str(type(param)):
            param_str = str(param)

        elif 'list' in str(type(param)):
            # param_str = '\n'.join(param)
            for param2 in param:
                printout(param2)
            separator = ','
            continue

        for field in param_str.split('\n'):
            if printout_format == 1:
                line_num, filename = srcLineNum(caller=2)
                sys.stdout.write(filename + ',' + line_num + ':')
            sys.stdout.write(separator + str(field) + '\n')
        separator = ','
        """

#===================================================

# Example main code

if __name__ == '__main__':

    printout('a line of output')
    sys.exit(1)


