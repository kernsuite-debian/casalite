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
import task_ft
def ft(vis='', field='', spw='', model='', nterms=1, reffreq='', complist='', incremental=False, usescratch=False):

        """Insert a source model as a visibility set
FOR MORE INFORMATION, SEE THE TASK PAGES OF FT IN CASA DOCS:
https://casa.nrao.edu/casadocs/
 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['model'] = model
        mytmp['nterms'] = nterms
        mytmp['reffreq'] = reffreq
        mytmp['complist'] = complist
        mytmp['incremental'] = incremental
        mytmp['usescratch'] = usescratch
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'ft.xml')

        casalog.origin('ft')
        if trec.has_key('ft') and casac.utils().verify(mytmp, trec['ft']) :
            result = task_ft.ft(vis, field, spw, model, nterms, reffreq, complist, incremental, usescratch)

        else :
          result = False
        return result
