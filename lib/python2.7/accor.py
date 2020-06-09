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
import task_accor
def accor(vis='', caltable='', field='', spw='', intent='', selectdata=True, timerange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='', append=False, docallib=False, callib='', gaintable=[''], gainfield=[''], interp=[''], spwmap=[]):

        """Normalize visibilities based on auto-correlations
For more information, see the task pages of accor in CASA Docs:

https://casa.nrao.edu/casadocs/

        """
        if type(gaintable)==str: gaintable=[gaintable]
        if type(gainfield)==str: gainfield=[gainfield]
        if type(interp)==str: interp=[interp]
        if type(spwmap)==int: spwmap=[spwmap]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['caltable'] = caltable
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['intent'] = intent
        mytmp['selectdata'] = selectdata
        mytmp['timerange'] = timerange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['observation'] = observation
        mytmp['msselect'] = msselect
        mytmp['solint'] = solint
        mytmp['combine'] = combine
        mytmp['append'] = append
        mytmp['docallib'] = docallib
        mytmp['callib'] = callib
        mytmp['gaintable'] = gaintable
        mytmp['gainfield'] = gainfield
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'accor.xml')

        casalog.origin('accor')
        if trec.has_key('accor') and casac.utils().verify(mytmp, trec['accor']) :
            result = task_accor.accor(vis, caltable, field, spw, intent, selectdata, timerange, antenna, scan, observation, msselect, solint, combine, append, docallib, callib, gaintable, gainfield, interp, spwmap)

        else :
          result = False
        return result
