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
import task_conjugatevis
def conjugatevis(vis='', spwlist="", outputvis='', overwrite=False):

        """Change the sign of the phases in all visibility columns.

For more information, see the task pages of conjugatevis in CASA Docs:

https://casa.nrao.edu/casadocs/


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['spwlist'] = spwlist
        mytmp['outputvis'] = outputvis
        mytmp['overwrite'] = overwrite
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'conjugatevis.xml')

        casalog.origin('conjugatevis')
        if trec.has_key('conjugatevis') and casac.utils().verify(mytmp, trec['conjugatevis']) :
            result = task_conjugatevis.conjugatevis(vis, spwlist, outputvis, overwrite)

        else :
          result = False
        return result
