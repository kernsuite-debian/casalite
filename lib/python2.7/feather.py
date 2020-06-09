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
import task_feather
def feather(imagename='', highres='', lowres='', sdfactor=1.0, effdishdiam=-1.0, lowpassfiltersd=False):

        """Combine two images using their Fourier transforms

For more information, see the task pages of feather in CASA Docs:

https://casa.nrao.edu/casadocs/


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['highres'] = highres
        mytmp['lowres'] = lowres
        mytmp['sdfactor'] = sdfactor
        mytmp['effdishdiam'] = effdishdiam
        mytmp['lowpassfiltersd'] = lowpassfiltersd
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'feather.xml')

        casalog.origin('feather')
        if trec.has_key('feather') and casac.utils().verify(mytmp, trec['feather']) :
            result = task_feather.feather(imagename, highres, lowres, sdfactor, effdishdiam, lowpassfiltersd)

        else :
          result = False
        return result
