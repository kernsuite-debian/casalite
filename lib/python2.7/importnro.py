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
import task_importnro
def importnro(infile='', outputvis='', overwrite=False, parallel=False):

        """Convert NOSTAR data into a CASA visibility file (MS)
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTNRO IN CASA DOCS:
https://casa.nrao.edu/casadocs/
  
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['outputvis'] = outputvis
        mytmp['overwrite'] = overwrite
        mytmp['parallel'] = parallel
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'importnro.xml')

        casalog.origin('importnro')
        if trec.has_key('importnro') and casac.utils().verify(mytmp, trec['importnro']) :
            result = task_importnro.importnro(infile, outputvis, overwrite, parallel)

        else :
          result = False
        return result
