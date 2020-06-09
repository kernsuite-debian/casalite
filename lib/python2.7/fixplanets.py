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
import task_fixplanets
def fixplanets(vis='', field="", fixuvw=False, direction='', refant=0, reftime='first'):

        """Changes FIELD and SOURCE table entries based on user-provided direction or POINTING table, optionally fixes the UVW coordinates

For more information, see the task pages of fixplanets in CASA Docs:

https://casa.nrao.edu/casadocs/


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['fixuvw'] = fixuvw
        mytmp['direction'] = direction
        mytmp['refant'] = refant
        mytmp['reftime'] = reftime
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'fixplanets.xml')

        casalog.origin('fixplanets')
        if trec.has_key('fixplanets') and casac.utils().verify(mytmp, trec['fixplanets']) :
            result = task_fixplanets.fixplanets(vis, field, fixuvw, direction, refant, reftime)

        else :
          result = False
        return result
