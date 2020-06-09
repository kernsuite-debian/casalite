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
import task_rerefant
def rerefant(vis='', tablein='', caltable='', refantmode='flex', refant=''):

        """Re-apply refant to a caltable


        TBD...

        Keyword arguments:
        vis -- Name of input visibility file
                default: none; example: vis='ngc5921.ms'
        tablein -- Input calibration table (G or T)
                default: none; example: tablein='ngc5921.gcal'
        caltable -- Output calibration table
                default: ''  (will overwrite tablein); 
                example: caltable='ngc5921_newrefant.gcal'
        refantmode -- The phase refant algorithm to use
                default: 'flex'; example: refantmode='flex'
                Options: 'flex','strict'
        refant -- Reference antenna name(s); a prioritized list may be specified
              default: '' => no refant applied
              example: refant='4' (antenna with index 4)
                       refant='VA04' (VLA antenna #4)
                       refant='EA02,EA23,EA13' (EVLA antenna EA02, use
                                EA23 and EA13 as alternates if/when EA02
                                drops out)
              Use taskname=listobs for antenna listing
 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['tablein'] = tablein
        mytmp['caltable'] = caltable
        mytmp['refantmode'] = refantmode
        mytmp['refant'] = refant
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'rerefant.xml')

        casalog.origin('rerefant')
        if trec.has_key('rerefant') and casac.utils().verify(mytmp, trec['rerefant']) :
            result = task_rerefant.rerefant(vis, tablein, caltable, refantmode, refant)

        else :
          result = False
        return result
