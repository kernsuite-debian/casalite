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
import task_exportuvfits
def exportuvfits(vis='', fitsfile='', datacolumn='corrected', field='', spw='', antenna='', timerange='', writesyscal=False, multisource=True, combinespw=True, writestation=True, padwithflags=False, overwrite=False):

        """Convert a CASA visibility data set to a UVFITS file:

For more information, see the task pages of exportuvfits in CASA Docs:

https://casa.nrao.edu/casadocs/


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['fitsfile'] = fitsfile
        mytmp['datacolumn'] = datacolumn
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['antenna'] = antenna
        mytmp['timerange'] = timerange
        mytmp['writesyscal'] = writesyscal
        mytmp['multisource'] = multisource
        mytmp['combinespw'] = combinespw
        mytmp['writestation'] = writestation
        mytmp['padwithflags'] = padwithflags
        mytmp['overwrite'] = overwrite
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'exportuvfits.xml')

        casalog.origin('exportuvfits')
        if trec.has_key('exportuvfits') and casac.utils().verify(mytmp, trec['exportuvfits']) :
            result = task_exportuvfits.exportuvfits(vis, fitsfile, datacolumn, field, spw, antenna, timerange, writesyscal, multisource, combinespw, writestation, padwithflags, overwrite)

        else :
          result = False
        return result
