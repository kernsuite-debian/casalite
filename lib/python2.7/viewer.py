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
import task_viewer
def viewer(infile='', displaytype='raster', channel=0, zoom=1, outfile='', outscale=1.0, outdpi=300, outformat='jpg', outlandscape=False, gui=True):

        """View an image or visibility data set

        examples of usage:

        viewer
        viewer "myimage.im"
        viewer "mymeasurementset.ms"
        viewer "myrestorefile.rstr"
        
        viewer "myimage.im", "contour"

        viewer "'myimage1.im' - 2 * 'myimage2.im'", "lel"
        
        
        Keyword arguments:
        infile -- Name of file to visualize
                default: ''
                example: infile='ngc5921.image'
                If no infile is specified the Load Data window
                will appear for selecting data.
        displaytype -- (optional): method of rendering data
                visually (raster, contour, vector or marker).  
                You can also set this parameter to 'lel' and
                provide an lel expression for infile (advanced).
                default: 'raster'
                example: displaytype='contour'

        Note: the filetype parameter is optional; typing of
        data files is now inferred:
                example:  viewer infile='my.im'
                obsolete: viewer infile='my.im', filetype='raster'
        the filetype is still used to load contours, etc.

    
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
        trec = casac.utils().torecord(pathname+'viewer.xml')

        casalog.origin('viewer')
        if trec.has_key('viewer') and casac.utils().verify(mytmp, trec['viewer']) :
            result = task_viewer.viewer(infile, displaytype, channel, zoom, outfile, outscale, outdpi, outformat, outlandscape, gui)

        else :
          result = False
        return result
