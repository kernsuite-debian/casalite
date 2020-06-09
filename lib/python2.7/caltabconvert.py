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
import task_caltabconvert
def caltabconvert(caltabold='', vis='', ptype='complex', caltabnew=''):

        """Convert old-style caltables into new-style caltables.

For more information, see the task pages of caltabconvert in CASA Docs:

https://casa.nrao.edu/casadocs/

  
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['caltabold'] = caltabold
        mytmp['vis'] = vis
        mytmp['ptype'] = ptype
        mytmp['caltabnew'] = caltabnew
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'caltabconvert.xml')

        casalog.origin('caltabconvert')
        if trec.has_key('caltabconvert') and casac.utils().verify(mytmp, trec['caltabconvert']) :
            result = task_caltabconvert.caltabconvert(caltabold, vis, ptype, caltabnew)

        else :
          result = False
        return result
