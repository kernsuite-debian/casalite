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
import task_clearstat
def clearstat():

        """Clear all autolock locks

For more information, see the task pages of clearstat in CASA Docs:

https://casa.nrao.edu/casadocs/

  
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'clearstat.xml')

        casalog.origin('clearstat')
        if trec.has_key('clearstat') and casac.utils().verify(mytmp, trec['clearstat']) :
            result = task_clearstat.clearstat()

        else :
          result = False
        return result
