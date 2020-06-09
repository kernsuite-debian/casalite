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
import task_splattotable
def splattotable(filenames=[''], table=''):

        """Convert a downloaded Splatalogue spectral line list to a casa table.
For more information, see the task pages of splattotable in CASA Docs:

https://casa.nrao.edu/casadocs/

        """
        if type(filenames)==str: filenames=[filenames]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['filenames'] = filenames
        mytmp['table'] = table
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'splattotable.xml')

        casalog.origin('splattotable')
        if trec.has_key('splattotable') and casac.utils().verify(mytmp, trec['splattotable']) :
            result = task_splattotable.splattotable(filenames, table)

        else :
          result = False
        return result
