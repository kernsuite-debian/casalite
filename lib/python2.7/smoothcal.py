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
import task_smoothcal
def smoothcal(vis='', tablein='', caltable='', field=[''], smoothtype='median', smoothtime=60.0):

        """Smooth calibration solution(s) derived from one or more sources:


        A G- or T-type gain calibration can be smoothed.  The amplitude and
        phase smoothing times are currently the same.  Calibration values
        will be smoothed for only the specified fields.  Smoothing is
        performed independently per field, per spw, and per antenna.

        Keyword arguments:
        vis -- Name of input visibility file
                default: none; example: vis='ngc5921.ms'
        tablein -- Input calibration table (G or T)
                default: none; example: tablein='ngc5921.gcal'
        caltable -- Output calibration table (smoothed)
                default: ''  (will overwrite tablein); 
                example: caltable='ngc5921_smooth.gcal'
        field -- subset of fields to select and smooth
                default: '' means all; example: field='0319_415_1,3C286'
        smoothtype -- The smoothing filter to be used for both amp and phase
                default: 'median'; example: smoothtype='mean'
                Options: 'median','mean'
        smoothtime -- Smoothing filter time (sec)
                default: 300.0; example: smoothtime=60.
 
        """
        if type(field)==str: field=[field]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['tablein'] = tablein
        mytmp['caltable'] = caltable
        mytmp['field'] = field
        mytmp['smoothtype'] = smoothtype
        mytmp['smoothtime'] = smoothtime
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'smoothcal.xml')

        casalog.origin('smoothcal')
        if trec.has_key('smoothcal') and casac.utils().verify(mytmp, trec['smoothcal']) :
            result = task_smoothcal.smoothcal(vis, tablein, caltable, field, smoothtype, smoothtime)

        else :
          result = False
        return result
