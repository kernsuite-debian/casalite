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
import task_importgmrt
def importgmrt(fitsfile='', flagfile='', vis=''):

        """Convert a UVFITS file to a CASA visibility data set
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTGMRT IN CASA DOCS:
https://casa.nrao.edu/casadocs/
 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['fitsfile'] = fitsfile
        mytmp['flagfile'] = flagfile
        mytmp['vis'] = vis
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'importgmrt.xml')

        casalog.origin('importgmrt')
        if trec.has_key('importgmrt') and casac.utils().verify(mytmp, trec['importgmrt']) :
            result = task_importgmrt.importgmrt(fitsfile, flagfile, vis)

        else :
          result = False
        return result
