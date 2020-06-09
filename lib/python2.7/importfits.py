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
import task_importfits
def importfits(fitsimage='', imagename='', whichrep=0, whichhdu=-1, zeroblanks=True, overwrite=False, defaultaxes=False, defaultaxesvalues=[], beam=[]):

        """Convert an image FITS file into a CASA image
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTFITS IN CASA DOCS:
https://casa.nrao.edu/casadocs/
 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['fitsimage'] = fitsimage
        mytmp['imagename'] = imagename
        mytmp['whichrep'] = whichrep
        mytmp['whichhdu'] = whichhdu
        mytmp['zeroblanks'] = zeroblanks
        mytmp['overwrite'] = overwrite
        mytmp['defaultaxes'] = defaultaxes
        mytmp['defaultaxesvalues'] = defaultaxesvalues
        mytmp['beam'] = beam
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'importfits.xml')

        casalog.origin('importfits')
        if trec.has_key('importfits') and casac.utils().verify(mytmp, trec['importfits']) :
            result = task_importfits.importfits(fitsimage, imagename, whichrep, whichhdu, zeroblanks, overwrite, defaultaxes, defaultaxesvalues, beam)

        else :
          result = False
        return result
