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
import task_exportasdm
def exportasdm(vis='', asdm='', datacolumn='data', archiveid='S0', rangeid='X1', subscanduration='24h', sbduration='2700s', apcorrected=False, verbose=True, showversion=True, useversion='v3'):

        """Convert a CASA visibility file (MS) into an ALMA or EVLA Science Data Model

For more information, see the task pages of exportasdm in CASA Docs:

https://casa.nrao.edu/casadocs/

  
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['asdm'] = asdm
        mytmp['datacolumn'] = datacolumn
        mytmp['archiveid'] = archiveid
        mytmp['rangeid'] = rangeid
        mytmp['subscanduration'] = subscanduration
        mytmp['sbduration'] = sbduration
        mytmp['apcorrected'] = apcorrected
        mytmp['verbose'] = verbose
        mytmp['showversion'] = showversion
        mytmp['useversion'] = useversion
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'exportasdm.xml')

        casalog.origin('exportasdm')
        if trec.has_key('exportasdm') and casac.utils().verify(mytmp, trec['exportasdm']) :
            result = task_exportasdm.exportasdm(vis, asdm, datacolumn, archiveid, rangeid, subscanduration, sbduration, apcorrected, verbose, showversion, useversion)

        else :
          result = False
        return result
