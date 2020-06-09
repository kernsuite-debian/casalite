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
import task_listhistory
def listhistory(vis=''):

        """List the processing history of a dataset:

        The list of all task processing steps in a visibility data set
        are listed in the logger.

        Keyword arguments:
        vis -- Name of input visibility file 
                default: none; example: vis='ngc5921.ms'
        async -- Run asynchronously 
                default = False; do not run asychronously
 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'listhistory.xml')

        casalog.origin('listhistory')
        if trec.has_key('listhistory') and casac.utils().verify(mytmp, trec['listhistory']) :
            result = task_listhistory.listhistory(vis)

        else :
          result = False
        return result
