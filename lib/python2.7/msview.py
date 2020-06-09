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
import task_msview
def msview(infile='', displaytype='raster', channel=0, zoom=1, outfile='', outscale=1.0, outdpi=300, outformat='jpg', outlandscape=False, gui=True):

        """View a visibility data set

        examples of usage:

        msview
        msview "mymeasurementset.ms"
        msview "myrestorefile.rstr"
        
        Keyword arguments:
        infile -- Name of file to visualize
                default: ''
                example: infile='my.ms'
                If no infile is specified the Load Data window
                will appear for selecting data.
        displaytype -- (optional): method of rendering data
                visually (raster, contour, vector or marker).  
                You can also set this parameter to 'lel' and
                provide an lel expression for infile (advanced).
                default: 'raster'

        Note: there is no longer a filetype parameter; typing of
        data files is now done automatically.
                example:  msview infile='my.ms'
                obsolete: msview infile='my.ms', filetype='ms'

    
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['displaytype'] = displaytype
        mytmp['channel'] = channel
        mytmp['zoom'] = zoom
        mytmp['outfile'] = outfile
        mytmp['outscale'] = outscale
        mytmp['outdpi'] = outdpi
        mytmp['outformat'] = outformat
        mytmp['outlandscape'] = outlandscape
        mytmp['gui'] = gui
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'msview.xml')

        casalog.origin('msview')
        if trec.has_key('msview') and casac.utils().verify(mytmp, trec['msview']) :
            result = task_msview.msview(infile, displaytype, channel, zoom, outfile, outscale, outdpi, outformat, outlandscape, gui)

        else :
          result = False
        return result
