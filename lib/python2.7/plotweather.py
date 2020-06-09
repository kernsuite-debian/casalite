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
import task_plotweather
def plotweather(vis='', seasonal_weight=0.5, doPlot=True, plotName=''):

        """Plot elements of the weather table; estimate opacity.
Generates opacity estimates from both the weather data and a seasonal model; intended for VLA use only.
By default the returned opacity is the mean of these predictions, but this can be adjusted with seasonal_weight.

These methods and models are described in detail in EVLA Memo 143, VLA Test Memo 232, VLA Scientific Memo 176, and references therein.

Saves the plot to the following default file:  MS name + .plotweather.png
Custom plot filenames must end in one of: .png, .pdf, .ps, .eps or .svg

If run as a function, will return the mean zenith opacity per spectral window.

The wind direction is defined as the direction where the wind is coming from.
The wind direction is thus in the opposite side of the arrow, with north at
the top and counterclockwise through west, south, and east.

Written by Josh Marvil, revised 02/06/12

example:
myTau = plotweather(vis='myMS.ms',seasonal_weight=0.5, doPlot=True)

        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['seasonal_weight'] = seasonal_weight
        mytmp['doPlot'] = doPlot
        mytmp['plotName'] = plotName
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'plotweather.xml')

        casalog.origin('plotweather')
        if trec.has_key('plotweather') and casac.utils().verify(mytmp, trec['plotweather']) :
            result = task_plotweather.plotweather(vis, seasonal_weight, doPlot, plotName)

        else :
          result = False
        return result
