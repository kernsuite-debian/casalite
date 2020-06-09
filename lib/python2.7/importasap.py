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
import task_importasap
def importasap(infile='', outputvis='', flagbackup=True, overwrite=False, parallel=False):

        """Convert ASAP Scantable data  into a CASA visibility file (MS)

  
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['outputvis'] = outputvis
        mytmp['flagbackup'] = flagbackup
        mytmp['overwrite'] = overwrite
        mytmp['parallel'] = parallel
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'importasap.xml')

        casalog.origin('importasap')
        if trec.has_key('importasap') and casac.utils().verify(mytmp, trec['importasap']) :
            result = task_importasap.importasap(infile, outputvis, flagbackup, overwrite, parallel)

        else :
          result = False
        return result
