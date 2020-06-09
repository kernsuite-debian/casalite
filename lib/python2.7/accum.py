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
import task_accum
def accum(vis='', tablein='', incrtable='', caltable='', field=[''], calfield=[''], interp='linear', accumtime=1.0, spwmap=[-1]):

        """Accumulate incremental calibration solutions into a calibration table

For more information, see the task pages of accum in CASA Docs:

https://casa.nrao.edu/casadocs/

 
        """
        if type(field)==str: field=[field]
        if type(calfield)==str: calfield=[calfield]
        if type(spwmap)==int: spwmap=[spwmap]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['tablein'] = tablein
        mytmp['incrtable'] = incrtable
        mytmp['caltable'] = caltable
        mytmp['field'] = field
        mytmp['calfield'] = calfield
        mytmp['interp'] = interp
        mytmp['accumtime'] = accumtime
        mytmp['spwmap'] = spwmap
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'accum.xml')

        casalog.origin('accum')
        if trec.has_key('accum') and casac.utils().verify(mytmp, trec['accum']) :
            result = task_accum.accum(vis, tablein, incrtable, caltable, field, calfield, interp, accumtime, spwmap)

        else :
          result = False
        return result
