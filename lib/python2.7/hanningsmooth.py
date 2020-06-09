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
import task_hanningsmooth
def hanningsmooth(vis='', outputvis='', keepmms=True, field='', spw='', scan='', antenna='', correlation='', timerange='', intent='', array='', uvrange='', observation='', feed='', datacolumn='all'):

        """Hanning smooth frequency channel data to remove Gibbs ringing
FOR MORE INFORMATION, SEE THE TASK PAGES OF HANNINGSMOOTH IN CASA DOCS:
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
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'hanningsmooth.xml')

        casalog.origin('hanningsmooth')
        if trec.has_key('hanningsmooth') and casac.utils().verify(mytmp, trec['hanningsmooth']) :
            result = task_hanningsmooth.hanningsmooth(vis, outputvis, keepmms, field, spw, scan, antenna, correlation, timerange, intent, array, uvrange, observation, feed, datacolumn)

        else :
          result = False
        return result
