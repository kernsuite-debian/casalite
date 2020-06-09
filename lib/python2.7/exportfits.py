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
import task_exportfits
def exportfits(imagename='', fitsimage='', velocity=False, optical=False, bitpix=-32, minpix=0, maxpix=-1, overwrite=False, dropstokes=False, stokeslast=True, history=True, dropdeg=False):

        """Convert a CASA image to a FITS file
FOR MORE INFORMATION, SEE THE TASK PAGES OF EXPORTFITS IN CASA DOCS:
https://casa.nrao.edu/casadocs/

        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['fitsimage'] = fitsimage
        mytmp['velocity'] = velocity
        mytmp['optical'] = optical
        mytmp['bitpix'] = bitpix
        mytmp['minpix'] = minpix
        mytmp['maxpix'] = maxpix
        mytmp['overwrite'] = overwrite
        mytmp['dropstokes'] = dropstokes
        mytmp['stokeslast'] = stokeslast
        mytmp['history'] = history
        mytmp['dropdeg'] = dropdeg
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'exportfits.xml')

        casalog.origin('exportfits')
        if trec.has_key('exportfits') and casac.utils().verify(mytmp, trec['exportfits']) :
            result = task_exportfits.exportfits(imagename, fitsimage, velocity, optical, bitpix, minpix, maxpix, overwrite, dropstokes, stokeslast, history, dropdeg)

        else :
          result = False
        return result
