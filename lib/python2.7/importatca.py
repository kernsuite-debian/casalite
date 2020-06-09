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
import task_importatca
def importatca(files=[''], vis='', options='', spw=[-1], nscans=[0,0], lowfreq='0.1GHz', highfreq='999GHz', fields=[''], edge=8):

        """Import ATCA RPFITS file(s) to a measurement set
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTATCA IN CASA DOCS:
https://casa.nrao.edu/casadocs/ 
   
        """
        if type(files)==str: files=[files]
        if type(spw)==int: spw=[spw]
        if type(nscans)==int: nscans=[nscans]
        if type(fields)==str: fields=[fields]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['files'] = files
        mytmp['vis'] = vis
        mytmp['options'] = options
        mytmp['spw'] = spw
        mytmp['nscans'] = nscans
        if type(lowfreq) == str :
           mytmp['lowfreq'] = casac.quanta().quantity(lowfreq)
        else :
           mytmp['lowfreq'] = lowfreq
        if type(highfreq) == str :
           mytmp['highfreq'] = casac.quanta().quantity(highfreq)
        else :
           mytmp['highfreq'] = highfreq
        mytmp['fields'] = fields
        mytmp['edge'] = edge
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'importatca.xml')

        casalog.origin('importatca')
        if trec.has_key('importatca') and casac.utils().verify(mytmp, trec['importatca']) :
            result = task_importatca.importatca(files, vis, options, spw, nscans, lowfreq, highfreq, fields, edge)

        else :
          result = False
        return result
