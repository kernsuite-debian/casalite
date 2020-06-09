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
import task_plotants
def plotants(vis='', figfile='', antindex=False, logpos=False, exclude='', checkbaselines=False, title='', showgui=True):

        """Plot the antenna distribution in the local reference frame:
       Plot the antenna distribution in the local reference frame:

       The location of the antennas in the MS will be plotted with
       X-toward local east; Y-toward local north. The name of each
       antenna is shown next to its respective location.

       Keyword arguments:
       vis -- Name of input visibility file (required)
            Default: none, example: vis='ngc5921.ms'

       figfile -- Save the plotted figure in this file
            Default: '', example: figfile='antplot.png'

       antindex -- Label antennas with id in addition to name
            Default: False, example: antindex=True

       logpos -- Produce a logarithmic position plot
            Default: False, example: logpos=True

       exclude -- Antenna selection string to exclude from plotting
            Note: integers are treated as names first then as index
            Default: '', examples: "DV23,DA02" "1,5,7" "0~3"

       checkbaselines -- Only plot antennas in the MAIN table
            This can be useful after a split.  WARNING: Setting
            checkbaselines to True will add to runtime in
            proportion to the number of rows in the dataset.
            Default: False, example: checkbaselines=True

       title -- Title written along top of plot
            Default: '', example: "ALMA Antenna Positions"
       showgui -- Whether or not to display the plotting GUI
            Default: True; example showgui=False

       You can zoom in by pressing the magnifier button (bottom,
       third from right) and making a rectangular region with
       the mouse.  Press the home button (leftmost button) to
       remove zoom.

       A hard-copy of this plot can be obtained by pressing the
       button on the right at the bottom of the display. A file
       dialog will allow you to choose the directory, filename,
       and format of the export. 
 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['figfile'] = figfile
        mytmp['antindex'] = antindex
        mytmp['logpos'] = logpos
        mytmp['exclude'] = exclude
        mytmp['checkbaselines'] = checkbaselines
        mytmp['title'] = title
        mytmp['showgui'] = showgui
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'plotants.xml')

        casalog.origin('plotants')
        if trec.has_key('plotants') and casac.utils().verify(mytmp, trec['plotants']) :
            result = task_plotants.plotants(vis, figfile, antindex, logpos, exclude, checkbaselines, title, showgui)

        else :
          result = False
        return result
