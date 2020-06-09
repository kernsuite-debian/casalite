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
import task_fixvis
def fixvis(vis='', outputvis='', field="", refcode='', reuse=True, phasecenter='', distances="", datacolumn='all'):

        """Recalculates (u, v, w) and/or changes Phase Center 

For more information, see the task pages of fixvis in CASA Docs:

https://casa.nrao.edu/casadocs/


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['outputvis'] = outputvis
        mytmp['field'] = field
        mytmp['refcode'] = refcode
        mytmp['reuse'] = reuse
        mytmp['phasecenter'] = phasecenter
        mytmp['distances'] = distances
        mytmp['datacolumn'] = datacolumn
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'fixvis.xml')

        casalog.origin('fixvis')
        if trec.has_key('fixvis') and casac.utils().verify(mytmp, trec['fixvis']) :
            result = task_fixvis.fixvis(vis, outputvis, field, refcode, reuse, phasecenter, distances, datacolumn)

        else :
          result = False
        return result
