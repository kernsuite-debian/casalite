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
import task_asdmsummary
def asdmsummary(asdm=''):

        """Summarized description of an ASDM dataset.
For more information, see the task pages of asdmsummary in CASA Docs:

https://casa.nrao.edu/casadocs/
  
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['asdm'] = asdm
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'asdmsummary.xml')

        casalog.origin('asdmsummary')
        if trec.has_key('asdmsummary') and casac.utils().verify(mytmp, trec['asdmsummary']) :
            result = task_asdmsummary.asdmsummary(asdm)

        else :
          result = False
        return result
