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
import task_imhistory
def imhistory(imagename='', mode='list', verbose=True, origin='imhistory', message=''):

        """Retrieve and modify image history
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMHISTORY IN CASA DOCS:
https://casa.nrao.edu/casadocs/

        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['mode'] = mode
        mytmp['verbose'] = verbose
        mytmp['origin'] = origin
        mytmp['message'] = message
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'imhistory.xml')

        casalog.origin('imhistory')
        if trec.has_key('imhistory') and casac.utils().verify(mytmp, trec['imhistory']) :
            result = task_imhistory.imhistory(imagename, mode, verbose, origin, message)

        else :
          result = False
        return result
