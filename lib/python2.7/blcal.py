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
import task_blcal
def blcal(vis='', caltable='', field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='scan', freqdep=False, calmode='ap', solnorm=False, gaintable=[''], gainfield=[''], interp=[''], spwmap=[], parang=False):

        """Calculate a baseline-based calibration solution (gain or bandpass)

For more information, see the task pages of blcal in CASA Docs:

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
        mytmp['uvrange'] = uvrange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['observation'] = observation
        mytmp['msselect'] = msselect
        mytmp['solint'] = solint
        mytmp['combine'] = combine
        mytmp['freqdep'] = freqdep
        mytmp['calmode'] = calmode
        mytmp['solnorm'] = solnorm
        mytmp['gaintable'] = gaintable
        mytmp['gainfield'] = gainfield
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        mytmp['parang'] = parang
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'blcal.xml')

        casalog.origin('blcal')
        if trec.has_key('blcal') and casac.utils().verify(mytmp, trec['blcal']) :
            result = task_blcal.blcal(vis, caltable, field, spw, intent, selectdata, timerange, uvrange, antenna, scan, observation, msselect, solint, combine, freqdep, calmode, solnorm, gaintable, gainfield, interp, spwmap, parang)

        else :
          result = False
        return result
