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
import task_clearcal
def clearcal(vis='', field='', spw='', intent='', addmodel=False):

        """Re-initializes the calibration for a visibility data set

For more information, see the task pages of clearcal in CASA Docs:

https://casa.nrao.edu/casadocs/

 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['intent'] = intent
        mytmp['addmodel'] = addmodel
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'clearcal.xml')

        casalog.origin('clearcal')
        if trec.has_key('clearcal') and casac.utils().verify(mytmp, trec['clearcal']) :
            result = task_clearcal.clearcal(vis, field, spw, intent, addmodel)

        else :
          result = False
        return result
