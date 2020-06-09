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
import task_apparentsens
def apparentsens(vis='', field='', spw='', intent='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', imsize=[100], cell=["1arcsec"], stokes='I', specmode='mfs', weighting='natural', robust=0.5, npixels=0, uvtaper=['']):

        """Imaging sensitivity estimataion

     TBD.

  
        """
        if type(uvtaper)==str: uvtaper=[uvtaper]

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
        mytmp['imsize'] = imsize
        mytmp['cell'] = cell
        mytmp['stokes'] = stokes
        mytmp['specmode'] = specmode
        mytmp['weighting'] = weighting
        mytmp['robust'] = robust
        mytmp['npixels'] = npixels
        mytmp['uvtaper'] = uvtaper
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'apparentsens.xml')

        casalog.origin('apparentsens')
        if trec.has_key('apparentsens') and casac.utils().verify(mytmp, trec['apparentsens']) :
            result = task_apparentsens.apparentsens(vis, field, spw, intent, selectdata, timerange, uvrange, antenna, scan, observation, imsize, cell, stokes, specmode, weighting, robust, npixels, uvtaper)

        else :
          result = False
        return result
