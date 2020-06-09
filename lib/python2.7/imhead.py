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
import task_imhead
def imhead(imagename='', mode='summary', hdkey='', hdvalue='', verbose=False):

        """List, get and put image header parameters
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMHEAD IN CASA DOCS:
https://casa.nrao.edu/casadocs/    

        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['mode'] = mode
        mytmp['hdkey'] = hdkey
        mytmp['hdvalue'] = hdvalue
        mytmp['verbose'] = verbose
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'imhead.xml')

        casalog.origin('imhead')
        if trec.has_key('imhead') and casac.utils().verify(mytmp, trec['imhead']) :
            result = task_imhead.imhead(imagename, mode, hdkey, hdvalue, verbose)

        else :
          result = False
        return result
