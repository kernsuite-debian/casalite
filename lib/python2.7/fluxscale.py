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
import task_fluxscale
def fluxscale(vis='', caltable='', fluxtable='', reference=[''], transfer=[''], listfile='', append=False, refspwmap=[-1], gainthreshold=-1.0, antenna='', timerange='', scan='', incremental=False, fitorder=1, display=False):

        """Bootstrap the flux density scale from standard calibrators
For more information, see the task pages of fluxscale in CASA Docs:

https://casa.nrao.edu/casadocs/
 
        """
        if type(reference)==str: reference=[reference]
        if type(transfer)==str: transfer=[transfer]
        if type(refspwmap)==int: refspwmap=[refspwmap]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['caltable'] = caltable
        mytmp['fluxtable'] = fluxtable
        mytmp['reference'] = reference
        mytmp['transfer'] = transfer
        mytmp['listfile'] = listfile
        mytmp['append'] = append
        mytmp['refspwmap'] = refspwmap
        mytmp['gainthreshold'] = gainthreshold
        mytmp['antenna'] = antenna
        mytmp['timerange'] = timerange
        mytmp['scan'] = scan
        mytmp['incremental'] = incremental
        mytmp['fitorder'] = fitorder
        mytmp['display'] = display
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'fluxscale.xml')

        casalog.origin('fluxscale')
        if trec.has_key('fluxscale') and casac.utils().verify(mytmp, trec['fluxscale']) :
            result = task_fluxscale.fluxscale(vis, caltable, fluxtable, reference, transfer, listfile, append, refspwmap, gainthreshold, antenna, timerange, scan, incremental, fitorder, display)

        else :
          result = False
        return result
