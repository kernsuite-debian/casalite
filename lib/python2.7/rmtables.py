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
import task_rmtables
def rmtables(tablenames=['']):

        """Remove tables cleanly, use this instead of rm -rf
        Removes tables cleanly.
        Arguments may contain * or ?. Ranges [] are support but
        not ~ expansion.
 
        """
        if type(tablenames)==str: tablenames=[tablenames]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['tablenames'] = tablenames
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'rmtables.xml')

        casalog.origin('rmtables')
        if trec.has_key('rmtables') and casac.utils().verify(mytmp, trec['rmtables']) :
            result = task_rmtables.rmtables(tablenames)

        else :
          result = False
        return result
