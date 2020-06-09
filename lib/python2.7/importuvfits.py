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
import task_importuvfits
def importuvfits(fitsfile='', vis='', antnamescheme='old'):

        """Convert a UVFITS file to a CASA visibility data set
        Convert a UVFITS file to a CASA visibility data set:

        Keyword arguments:
        fitsfile -- Name of input UV FITS file
                default = none; example='3C273XC1.fits'
        vis -- Name of output visibility file (MS)
                default = none; example: vis='3C273XC1.ms'
        antnamescheme -- Naming scheme for VLA/JVLA/CARMA antennas
                default = old;
                  old: Antenna name is a number, '04'
                       This option exists for backwards compatibility
                       but can lead to ambiguous results when antenna
                       indices are used for data selection.
                  new: Antenna name is not a number, e.g., 'VA04' or 'EA04'
                       With this scheme, data selection via
                       antenna names and indices is non-ambiguous.
        async --  Run asynchronously
               default = false; do not run asychronously

        Note: Don't forget to flag autocorrections using
           taskname flagdata, autocorr = true

 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['fitsfile'] = fitsfile
        mytmp['vis'] = vis
        mytmp['antnamescheme'] = antnamescheme
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'importuvfits.xml')

        casalog.origin('importuvfits')
        if trec.has_key('importuvfits') and casac.utils().verify(mytmp, trec['importuvfits']) :
            result = task_importuvfits.importuvfits(fitsfile, vis, antnamescheme)

        else :
          result = False
        return result
