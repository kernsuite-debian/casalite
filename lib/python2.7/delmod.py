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
import task_delmod
def delmod(vis='', otf=True, field='', scr=False):

        """Deletes model representations in the MS
  

For more information, see the task pages of delmod in CASA Docs:

https://casa.nrao.edu/casadocs/

 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['otf'] = otf
        mytmp['field'] = field
        mytmp['scr'] = scr
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'delmod.xml')

        casalog.origin('delmod')
        if trec.has_key('delmod') and casac.utils().verify(mytmp, trec['delmod']) :
            result = task_delmod.delmod(vis, otf, field, scr)

        else :
          result = False
        return result
