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
import task_impbcor
def impbcor(imagename='', pbimage="", outfile='', overwrite=False, box='', region='', chans='', stokes='', mask='', mode='divide', cutoff=-1.0, stretch=False):

        """Construct a primary beam corrected image from an image and a primary beam pattern.
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPBCOR IN CASA DOCS:
https://casa.nrao.edu/casadocs/
    
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['pbimage'] = pbimage
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        mytmp['box'] = box
        mytmp['region'] = region
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['mode'] = mode
        mytmp['cutoff'] = cutoff
        mytmp['stretch'] = stretch
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'impbcor.xml')

        casalog.origin('impbcor')
        if trec.has_key('impbcor') and casac.utils().verify(mytmp, trec['impbcor']) :
            result = task_impbcor.impbcor(imagename, pbimage, outfile, overwrite, box, region, chans, stokes, mask, mode, cutoff, stretch)

        else :
          result = False
        return result
