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
import task_applycal
def applycal(vis='', field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', msselect='', docallib=False, callib='', gaintable=[''], gainfield=[''], interp=[''], spwmap=[], calwt=[True], parang=False, applymode='', flagbackup=True):

        """Apply calibrations solutions(s) to data

For more information, see the task pages of applycal in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if type(gaintable)==str: gaintable=[gaintable]
        if type(gainfield)==str: gainfield=[gainfield]
        if type(interp)==str: interp=[interp]
        if type(spwmap)==int: spwmap=[spwmap]
        if type(calwt)==bool: calwt=[calwt]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
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
        mytmp['docallib'] = docallib
        mytmp['callib'] = callib
        mytmp['gaintable'] = gaintable
        mytmp['gainfield'] = gainfield
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        mytmp['calwt'] = calwt
        mytmp['parang'] = parang
        mytmp['applymode'] = applymode
        mytmp['flagbackup'] = flagbackup
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'applycal.xml')

        casalog.origin('applycal')
        if trec.has_key('applycal') and casac.utils().verify(mytmp, trec['applycal']) :
            result = task_applycal.applycal(vis, field, spw, intent, selectdata, timerange, uvrange, antenna, scan, observation, msselect, docallib, callib, gaintable, gainfield, interp, spwmap, calwt, parang, applymode, flagbackup)

        else :
          result = False
        return result
