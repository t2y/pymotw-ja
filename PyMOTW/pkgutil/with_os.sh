#!/bin/sh
#
# $Id$
#
#end_pymotw_header

export PYTHONPATH=os_${1}
echo "PYTHONPATH=$PYTHONPATH"
echo

python pkgutil_os_specific.py
