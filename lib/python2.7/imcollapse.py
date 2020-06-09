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
import task_imcollapse
def imcollapse(imagename='', function='', axes=[0], outfile='', box='', region='', chans='', stokes='', mask='', overwrite=False, stretch=False):

        """Collapse image along one axis, aggregating pixel values along that axis.
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMCOLLAPSE IN CASA DOCS:
https://casa.nrao.edu/casadocs/

        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['function'] = function
        mytmp['axes'] = axes
        mytmp['outfile'] = outfile
        mytmp['box'] = box
        mytmp['region'] = region
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['overwrite'] = overwrite
        mytmp['stretch'] = stretch
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'imcollapse.xml')

        casalog.origin('imcollapse')
        if trec.has_key('imcollapse') and casac.utils().verify(mytmp, trec['imcollapse']) :
            result = task_imcollapse.imcollapse(imagename, function, axes, outfile, box, region, chans, stokes, mask, overwrite, stretch)

        else :
          result = False
        return result
