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
import task_setjy
def setjy(vis='', field='', spw='', selectdata=False, timerange='', scan='', intent='', observation='', scalebychan=True, standard='Perley-Butler 2017', model='', modimage='', listmodels=False, fluxdensity=-1, spix=0.0, reffreq='1GHz', polindex=[], polangle=[], rotmeas=0.0, fluxdict=[], useephemdir=False, interpolation='nearest', usescratch=False, ismms=False):

        """Fills the model column with the visibilities of a calibrator
FOR MORE INFORMATION, SEE THE TASK PAGES OF SETJY IN CASA DOCS:
https://casa.nrao.edu/casadocs/

        """
        if type(polindex)==float: polindex=[polindex]
        if type(polangle)==float: polangle=[polangle]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['selectdata'] = selectdata
        mytmp['timerange'] = timerange
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['observation'] = observation
        mytmp['scalebychan'] = scalebychan
        mytmp['standard'] = standard
        mytmp['model'] = model
        mytmp['modimage'] = modimage
        mytmp['listmodels'] = listmodels
        mytmp['fluxdensity'] = fluxdensity
        mytmp['spix'] = spix
        mytmp['reffreq'] = reffreq
        mytmp['polindex'] = polindex
        mytmp['polangle'] = polangle
        mytmp['rotmeas'] = rotmeas
        mytmp['fluxdict'] = fluxdict
        mytmp['useephemdir'] = useephemdir
        mytmp['interpolation'] = interpolation
        mytmp['usescratch'] = usescratch
        mytmp['ismms'] = ismms
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'setjy.xml')

        casalog.origin('setjy')
        if trec.has_key('setjy') and casac.utils().verify(mytmp, trec['setjy']) :
            result = task_setjy.setjy(vis, field, spw, selectdata, timerange, scan, intent, observation, scalebychan, standard, model, modimage, listmodels, fluxdensity, spix, reffreq, polindex, polangle, rotmeas, fluxdict, useephemdir, interpolation, usescratch, ismms)

        else :
          result = False
        return result
