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
import task_oldsplit
def oldsplit(vis='', outputvis='', datacolumn='corrected', field='', spw='', width=1, antenna='', timebin='0s', timerange='', array='', uvrange='', scan='', intent='', correlation='', observation='', combine='', keepflags=True, keepmms=False):

        """Create a visibility subset from an existing visibility set

For more information, see the oldsplit task-list pages in the CASA
documentation "CASA Docs":

https://casa.nrao.edu/casadocs/


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['outputvis'] = outputvis
        mytmp['datacolumn'] = datacolumn
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['width'] = width
        mytmp['antenna'] = antenna
        mytmp['timebin'] = timebin
        mytmp['timerange'] = timerange
        mytmp['array'] = array
        mytmp['uvrange'] = uvrange
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['correlation'] = correlation
        mytmp['observation'] = observation
        mytmp['combine'] = combine
        mytmp['keepflags'] = keepflags
        mytmp['keepmms'] = keepmms
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'oldsplit.xml')

        casalog.origin('oldsplit')
        if trec.has_key('oldsplit') and casac.utils().verify(mytmp, trec['oldsplit']) :
            result = task_oldsplit.oldsplit(vis, outputvis, datacolumn, field, spw, width, antenna, timebin, timerange, array, uvrange, scan, intent, correlation, observation, combine, keepflags, keepmms)

        else :
          result = False
        return result
