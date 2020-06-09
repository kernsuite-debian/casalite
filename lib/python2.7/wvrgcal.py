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
import task_wvrgcal
def wvrgcal(vis='', caltable='', toffset=0, segsource=True, sourceflag=[''], tie=[''], nsol=1, disperse=False, wvrflag=[''], statfield='', statsource='', smooth='', scale=1., spw=[], wvrspw=[], reversespw='', cont=False, maxdistm=500., minnumants=2, mingoodfrac=0.8, usefieldtab=False, refant=[''], offsetstable=''):

        """Generate a gain table based on Water Vapour Radiometer data

   wvrgcal(vis='uid___A002_X1d54a1_X5.ms', caltable='cal-wvr-uid___A002_X1d54a1_X5.W',
           toffset=-1, segsource=True, tie=['Titan,1037-295,NGC3256'], statsource='1037-295')

  
        """
        if type(sourceflag)==str: sourceflag=[sourceflag]
        if type(tie)==str: tie=[tie]
        if type(wvrflag)==str: wvrflag=[wvrflag]
        if type(spw)==int: spw=[spw]
        if type(wvrspw)==int: wvrspw=[wvrspw]
        if type(refant)==str: refant=[refant]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['caltable'] = caltable
        mytmp['toffset'] = toffset
        mytmp['segsource'] = segsource
        mytmp['sourceflag'] = sourceflag
        mytmp['tie'] = tie
        mytmp['nsol'] = nsol
        mytmp['disperse'] = disperse
        mytmp['wvrflag'] = wvrflag
        mytmp['statfield'] = statfield
        mytmp['statsource'] = statsource
        mytmp['smooth'] = smooth
        mytmp['scale'] = scale
        mytmp['spw'] = spw
        mytmp['wvrspw'] = wvrspw
        mytmp['reversespw'] = reversespw
        mytmp['cont'] = cont
        mytmp['maxdistm'] = maxdistm
        mytmp['minnumants'] = minnumants
        mytmp['mingoodfrac'] = mingoodfrac
        mytmp['usefieldtab'] = usefieldtab
        mytmp['refant'] = refant
        mytmp['offsetstable'] = offsetstable
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'wvrgcal.xml')

        casalog.origin('wvrgcal')
        if trec.has_key('wvrgcal') and casac.utils().verify(mytmp, trec['wvrgcal']) :
            result = task_wvrgcal.wvrgcal(vis, caltable, toffset, segsource, sourceflag, tie, nsol, disperse, wvrflag, statfield, statsource, smooth, scale, spw, wvrspw, reversespw, cont, maxdistm, minnumants, mingoodfrac, usefieldtab, refant, offsetstable)

        else :
          result = False
        return result
