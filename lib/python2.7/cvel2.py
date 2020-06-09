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
import task_cvel2
def cvel2(vis='', outputvis='', keepmms=True, passall=False, field='', spw='', scan='', antenna='', correlation='', timerange='', intent='', array='', uvrange='', observation='', feed='', datacolumn='all', mode='channel', nchan=-1, start=0, width=1, interpolation='linear', phasecenter='', restfreq='', outframe='', veltype='radio', hanning=False):

        """Regrid an MS or MMS to a new spectral window, channel structure or frame

For more information, see the task pages of cvel2 in CASA Docs:

https://casa.nrao.edu/casadocs/


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['outputvis'] = outputvis
        mytmp['keepmms'] = keepmms
        mytmp['passall'] = passall
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
        mytmp['mode'] = mode
        mytmp['nchan'] = nchan
        mytmp['start'] = start
        mytmp['width'] = width
        mytmp['interpolation'] = interpolation
        mytmp['phasecenter'] = phasecenter
        mytmp['restfreq'] = restfreq
        mytmp['outframe'] = outframe
        mytmp['veltype'] = veltype
        mytmp['hanning'] = hanning
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'cvel2.xml')

        casalog.origin('cvel2')
        if trec.has_key('cvel2') and casac.utils().verify(mytmp, trec['cvel2']) :
            result = task_cvel2.cvel2(vis, outputvis, keepmms, passall, field, spw, scan, antenna, correlation, timerange, intent, array, uvrange, observation, feed, datacolumn, mode, nchan, start, width, interpolation, phasecenter, restfreq, outframe, veltype, hanning)

        else :
          result = False
        return result
