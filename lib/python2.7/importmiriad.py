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
import task_importmiriad
def importmiriad(mirfile='', vis='', tsys=False, spw=[-1], vel='', linecal=False, wide=[], debug=0):

        """Convert a Miriad visibility file into a CASA MeasurementSet
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTMIRIAD IN CASA DOCS:
https://casa.nrao.edu/casadocs/
 
        """
        if type(spw)==int: spw=[spw]
        if type(wide)==int: wide=[wide]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['mirfile'] = mirfile
        mytmp['vis'] = vis
        mytmp['tsys'] = tsys
        mytmp['spw'] = spw
        mytmp['vel'] = vel
        mytmp['linecal'] = linecal
        mytmp['wide'] = wide
        mytmp['debug'] = debug
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'importmiriad.xml')

        casalog.origin('importmiriad')
        if trec.has_key('importmiriad') and casac.utils().verify(mytmp, trec['importmiriad']) :
            result = task_importmiriad.importmiriad(mirfile, vis, tsys, spw, vel, linecal, wide, debug)

        else :
          result = False
        return result
