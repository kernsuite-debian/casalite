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
import task_importvla
def importvla(archivefiles=[''], vis='', bandname='', frequencytol='150000.0Hz', project='', starttime='', stoptime='', applytsys=True, autocorr=False, antnamescheme='new', keepblanks=False, evlabands=False):

        """Import VLA archive file(s) to a measurement set
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTVLA IN CASA DOCS:
https://casa.nrao.edu/casadocs/
   
        """
        if type(archivefiles)==str: archivefiles=[archivefiles]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['archivefiles'] = archivefiles
        mytmp['vis'] = vis
        mytmp['bandname'] = bandname
        mytmp['frequencytol'] = frequencytol
        mytmp['project'] = project
        mytmp['starttime'] = starttime
        mytmp['stoptime'] = stoptime
        mytmp['applytsys'] = applytsys
        mytmp['autocorr'] = autocorr
        mytmp['antnamescheme'] = antnamescheme
        mytmp['keepblanks'] = keepblanks
        mytmp['evlabands'] = evlabands
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'importvla.xml')

        casalog.origin('importvla')
        if trec.has_key('importvla') and casac.utils().verify(mytmp, trec['importvla']) :
            result = task_importvla.importvla(archivefiles, vis, bandname, frequencytol, project, starttime, stoptime, applytsys, autocorr, antnamescheme, keepblanks, evlabands)

        else :
          result = False
        return result
