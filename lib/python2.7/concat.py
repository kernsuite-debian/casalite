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
import task_concat
def concat(vis=[''], concatvis='', freqtol='', dirtol='', respectname=False, timesort=False, copypointing=True, visweightscale=[], forcesingleephemfield=''):

        """Concatenate several visibility data sets.

For more information, see the task pages of concat in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if type(vis)==str: vis=[vis]
        if type(visweightscale)==float: visweightscale=[visweightscale]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['concatvis'] = concatvis
        mytmp['freqtol'] = freqtol
        mytmp['dirtol'] = dirtol
        mytmp['respectname'] = respectname
        mytmp['timesort'] = timesort
        mytmp['copypointing'] = copypointing
        mytmp['visweightscale'] = visweightscale
        mytmp['forcesingleephemfield'] = forcesingleephemfield
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'concat.xml')

        casalog.origin('concat')
        if trec.has_key('concat') and casac.utils().verify(mytmp, trec['concat']) :
            result = task_concat.concat(vis, concatvis, freqtol, dirtol, respectname, timesort, copypointing, visweightscale, forcesingleephemfield)

        else :
          result = False
        return result
