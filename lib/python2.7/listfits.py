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
import task_listfits
def listfits(fitsfile=''):

        """List the HDU and typical data rows of a fits file:

        The HDU and typical data rows in a fits file are listed in the logger.

        Keyword arguments:
        fitsfile -- Name of input fits file 
                default: none; example: fitsfile='ngc5921.uvfits'
        async -- Run asynchronously 
                default = False; do not run asychronously
 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['fitsfile'] = fitsfile
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'listfits.xml')

        casalog.origin('listfits')
        if trec.has_key('listfits') and casac.utils().verify(mytmp, trec['listfits']) :
            result = task_listfits.listfits(fitsfile)

        else :
          result = False
        return result
