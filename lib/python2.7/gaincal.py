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
import task_gaincal
def gaincal(vis='', caltable='', field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='', preavg=-1.0, refant='', refantmode='flex', minblperant=4, minsnr=3.0, solnorm=False, normtype='mean', gaintype='G', smodel=[], calmode='ap', solmode='', rmsthresh=[], append=False, splinetime=3600.0, npointaver=3, phasewrap=180.0, docallib=False, callib='', gaintable=[''], gainfield=[''], interp=[''], spwmap=[], parang=False):

        """Determine temporal gains from calibrator observations

For more information, see the task pages of gaincal in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if type(smodel)==float: smodel=[smodel]
        if type(rmsthresh)==float: rmsthresh=[rmsthresh]
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
        mytmp['preavg'] = preavg
        mytmp['refant'] = refant
        mytmp['refantmode'] = refantmode
        mytmp['minblperant'] = minblperant
        mytmp['minsnr'] = minsnr
        mytmp['solnorm'] = solnorm
        mytmp['normtype'] = normtype
        mytmp['gaintype'] = gaintype
        mytmp['smodel'] = smodel
        mytmp['calmode'] = calmode
        mytmp['solmode'] = solmode
        mytmp['rmsthresh'] = rmsthresh
        mytmp['append'] = append
        mytmp['splinetime'] = splinetime
        mytmp['npointaver'] = npointaver
        mytmp['phasewrap'] = phasewrap
        mytmp['docallib'] = docallib
        mytmp['callib'] = callib
        mytmp['gaintable'] = gaintable
        mytmp['gainfield'] = gainfield
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        mytmp['parang'] = parang
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'gaincal.xml')

        casalog.origin('gaincal')
        if trec.has_key('gaincal') and casac.utils().verify(mytmp, trec['gaincal']) :
            result = task_gaincal.gaincal(vis, caltable, field, spw, intent, selectdata, timerange, uvrange, antenna, scan, observation, msselect, solint, combine, preavg, refant, refantmode, minblperant, minsnr, solnorm, normtype, gaintype, smodel, calmode, solmode, rmsthresh, append, splinetime, npointaver, phasewrap, docallib, callib, gaintable, gainfield, interp, spwmap, parang)

        else :
          result = False
        return result
