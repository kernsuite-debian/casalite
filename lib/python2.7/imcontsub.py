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
import task_imcontsub
def imcontsub(imagename='', linefile='', contfile='', fitorder=0, region='', box='', chans='', stokes=''):

        """Estimates and subtracts continuum emission from an image cube
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMCONTSUB IN CASA DOCS:
https://casa.nrao.edu/casadocs/

        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['linefile'] = linefile
        mytmp['contfile'] = contfile
        mytmp['fitorder'] = fitorder
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'imcontsub.xml')

        casalog.origin('imcontsub')
        if trec.has_key('imcontsub') and casac.utils().verify(mytmp, trec['imcontsub']) :
            result = task_imcontsub.imcontsub(imagename, linefile, contfile, fitorder, region, box, chans, stokes)

        else :
          result = False
        return result
