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
import task_split
def split(vis='', outputvis='', keepmms=True, field='', spw='', scan='', antenna='', correlation='', timerange='', intent='', array='', uvrange='', observation='', feed='', datacolumn='corrected', keepflags=True, width=1, timebin='0s', combine=''):

        """Create a visibility subset from an existing visibility set

For more information, see the task pages of split in CASA Docs:

https://casa.nrao.edu/casadocs/


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['outputvis'] = outputvis
        mytmp['keepmms'] = keepmms
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['scan'] = scan
        mytmp['antenna'] = antenna
        mytmp['correlation'] = correlation
        mytmp['timerange'] = timerange
        mytmp['intent'] = intent
        mytmp['array'] = array
        mytmp['uvrange'] = uvrange
        mytmp['observation'] = observation
        mytmp['feed'] = feed
        mytmp['datacolumn'] = datacolumn
        mytmp['keepflags'] = keepflags
        mytmp['width'] = width
        mytmp['timebin'] = timebin
        mytmp['combine'] = combine
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'split.xml')

        casalog.origin('split')
        if trec.has_key('split') and casac.utils().verify(mytmp, trec['split']) :
            result = task_split.split(vis, outputvis, keepmms, field, spw, scan, antenna, correlation, timerange, intent, array, uvrange, observation, feed, datacolumn, keepflags, width, timebin, combine)

        else :
          result = False
        return result
