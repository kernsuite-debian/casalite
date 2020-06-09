#
# This file was generated using xslt from its XML file
#
# Copyright 2009, Associated Universities Inc., Washington DC
#
import sys
import os
from  casac import *
import string
from taskinit import casalog
from taskinit import xmlpath
#from taskmanager import tm
import task_browsetable
def browsetable(tablename='', mightedit=False, sortlist='', taql='', skipcols=''):

        """Browse a table (MS, calibration table, image)

For more information, see the task pages of browsetable in CASA Docs:

https://casa.nrao.edu/casadocs/


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['tablename'] = tablename
        mytmp['mightedit'] = mightedit
        mytmp['sortlist'] = sortlist
        mytmp['taql'] = taql
        mytmp['skipcols'] = skipcols
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'browsetable.xml')

        casalog.origin('browsetable')
        if trec.has_key('browsetable') and casac.utils().verify(mytmp, trec['browsetable']) :
            result = task_browsetable.browsetable(tablename, mightedit, sortlist, taql, skipcols)

        else :
          result = False
        return result
