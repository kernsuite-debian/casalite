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
import task_importfitsidi
def importfitsidi(fitsidifile=[''], vis='', constobsid=False, scanreindexgap_s=0., specframe='GEO'):

        """Convert a FITS-IDI file to a CASA visibility data set
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTFITSIDI IN CASA DOCS:
https://casa.nrao.edu/casadocs/
 
        """
        if type(fitsidifile)==str: fitsidifile=[fitsidifile]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['fitsidifile'] = fitsidifile
        mytmp['vis'] = vis
        mytmp['constobsid'] = constobsid
        mytmp['scanreindexgap_s'] = scanreindexgap_s
        mytmp['specframe'] = specframe
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'importfitsidi.xml')

        casalog.origin('importfitsidi')
        if trec.has_key('importfitsidi') and casac.utils().verify(mytmp, trec['importfitsidi']) :
            result = task_importfitsidi.importfitsidi(fitsidifile, vis, constobsid, scanreindexgap_s, specframe)

        else :
          result = False
        return result
