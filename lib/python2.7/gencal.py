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
import task_gencal
def gencal(vis='', caltable='', caltype='', infile='', spw='', antenna='', pol='', parameter=[], uniform=True):

        """Specify Calibration Values of Various Types
FOR MORE INFORMATION, SEE THE TASK PAGES OF GENCAL IN CASA DOCS:
https://casa.nrao.edu/casadocs/
 
        """
        if type(parameter)==float: parameter=[parameter]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['caltable'] = caltable
        mytmp['caltype'] = caltype
        mytmp['infile'] = infile
        mytmp['spw'] = spw
        mytmp['antenna'] = antenna
        mytmp['pol'] = pol
        mytmp['parameter'] = parameter
        mytmp['uniform'] = uniform
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'gencal.xml')

        casalog.origin('gencal')
        if trec.has_key('gencal') and casac.utils().verify(mytmp, trec['gencal']) :
            result = task_gencal.gencal(vis, caltable, caltype, infile, spw, antenna, pol, parameter, uniform)

        else :
          result = False
        return result
