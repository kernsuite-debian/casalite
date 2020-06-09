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
import task_bandpass
def bandpass(vis='', caltable='', field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='scan', refant='', minblperant=4, minsnr=3.0, solnorm=False, bandtype='B', smodel=[], append=False, fillgaps=0, degamp=3, degphase=3, visnorm=False, maskcenter=0, maskedge=5, docallib=False, callib='', gaintable=[''], gainfield=[''], interp=[''], spwmap=[], parang=False):

        """Calculates a bandpass calibration solution

For more information, see the task pages of bandpass in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if type(smodel)==float: smodel=[smodel]
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
        mytmp['refant'] = refant
        mytmp['minblperant'] = minblperant
        mytmp['minsnr'] = minsnr
        mytmp['solnorm'] = solnorm
        mytmp['bandtype'] = bandtype
        mytmp['smodel'] = smodel
        mytmp['append'] = append
        mytmp['fillgaps'] = fillgaps
        mytmp['degamp'] = degamp
        mytmp['degphase'] = degphase
        mytmp['visnorm'] = visnorm
        mytmp['maskcenter'] = maskcenter
        mytmp['maskedge'] = maskedge
        mytmp['docallib'] = docallib
        mytmp['callib'] = callib
        mytmp['gaintable'] = gaintable
        mytmp['gainfield'] = gainfield
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        mytmp['parang'] = parang
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'bandpass.xml')

        casalog.origin('bandpass')
        if trec.has_key('bandpass') and casac.utils().verify(mytmp, trec['bandpass']) :
            result = task_bandpass.bandpass(vis, caltable, field, spw, intent, selectdata, timerange, uvrange, antenna, scan, observation, msselect, solint, combine, refant, minblperant, minsnr, solnorm, bandtype, smodel, append, fillgaps, degamp, degphase, visnorm, maskcenter, maskedge, docallib, callib, gaintable, gainfield, interp, spwmap, parang)

        else :
          result = False
        return result
