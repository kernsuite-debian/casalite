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
import task_polfromgain
def polfromgain(vis='', tablein='', caltable='', paoffset=0.0):

        """Derive linear polarization from gain ratio


        TBD...

        Keyword arguments:
        vis -- Name of input visibility file
                default: none; 
        tablein -- Input calibration table (G or T)
                default: none; 
        caltable -- Output calibration table
                default: ''  (no new table)
                if specified, new caltable with polarization removed is generated
        paoffset -- Manual position angle offset
              default: 0.0  (no extra offset)
              example: paoffset=10.0  (10 degree offset)

 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['tablein'] = tablein
        mytmp['caltable'] = caltable
        mytmp['paoffset'] = paoffset
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'polfromgain.xml')

        casalog.origin('polfromgain')
        if trec.has_key('polfromgain') and casac.utils().verify(mytmp, trec['polfromgain']) :
            result = task_polfromgain.polfromgain(vis, tablein, caltable, paoffset)

        else :
          result = False
        return result
