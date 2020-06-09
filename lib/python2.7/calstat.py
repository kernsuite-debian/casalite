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
import task_calstat
def calstat(caltable='', axis='amplitude', datacolumn='gain', useflags=True):

        """Displays statistical information on a calibration table
  

For more information, see the task pages of calstat in CASA Docs:

https://casa.nrao.edu/casadocs/


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['caltable'] = caltable
        mytmp['axis'] = axis
        mytmp['datacolumn'] = datacolumn
        mytmp['useflags'] = useflags
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'calstat.xml')

        casalog.origin('calstat')
        if trec.has_key('calstat') and casac.utils().verify(mytmp, trec['calstat']) :
            result = task_calstat.calstat(caltable, axis, datacolumn, useflags)

        else :
          result = False
        return result
