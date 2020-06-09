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
import task_plotcal
def plotcal(caltable='', xaxis='', yaxis='', poln='', field='', antenna='', spw='', timerange='', subplot=111, overplot=False, clearpanel='Auto', iteration='', plotrange=[
            ], showflags=False, plotsymbol='o', plotcolor='blue', markersize=5.0, fontsize=10.0, showgui=True, figfile=''):

        """An all-purpose plotter for calibration results 
    
        The values for all calibration solutions (G, T, GSPLINE, B, BPOLY, D, M) 
        can be displayed for a variety of polarization combinations and calibrations.
        The plot solutions may be iterated through antennas/spw/fields during one execution,
        and many frames can be obtained in each plot.

        The plotter permits zooming, listing and flagging of solutions, although
        the results of flagged solutions are not yet available.


        The plotter permits zooming, listing and flagging of solutions, although
        the implications of flagged solutions are not yet made.  See some hints at the end
        of this description.


        Keyword arguments:
        caltable -- Name of input calibration table 
                default: none; example: caltable='ngc5921.gcal'
                The type of calibration table is determined automatically.
        xaxis -- Value to plot on the x axis
                Options: 'time','scan','chan','freq','antenna','amp','phase','real','imag','snr'
                Default: cal type dependent, usually 'time'
        yaxis -- Value to plot on the y-axis
                Options: 'amp','phase','real','imag','snr','antenna','tsys','delay','rate','spgain'
                Default: cal type dependent, usually 'amp'
        poln -- Polarization (or combination) to plot
                default: '' (RL); all polarizations
                Options: '' = ('RL'),'R','L','XY','X','Y',
                               '/' --> form complex poln ratio
                                     (amp ratio and phase difference)
        field -- Select field using field id(s) or field name(s).
                  ['go listobs' to obtain the fieldt id's or names]
               default: ''=all fields
               If field string is a non-negative integer, it is assumed a
               field index, otherwise it is assumed a field name
               field='0~2'; field ids 0,1,2
               field='0,4,5~7'; field ids 0,4,5,6,7
               field='3C286,3C295'; field named 3C286 and 3C295
               field = '3,4C*'; field id 3, all names starting with 4C
        antenna -- Antenna selection (baseline syntax ignored)
               default: '' (all);
               example: antenna='1,3~5' means antenna
                  indices 1,3,4,5.  
        spw -- Select spectral window (channel syntax ignored, except for D)
               default: ''=all spectral windows
               spw='0~2,4'; spectral windows 0,1,2,4
               spw='<2';  spectral windows less than 2
        timerange -- Time selection
                  default: '' (all)
                  example: timerange='1995/04/13/09:15:00~1995/04/13/09:25:00'

        --- Plot Options ---
        subplot -- Panel number on the display screen
               default: 111 (full screen display);
               examples:
               if iteration = 'antenna'; subplot=321 then
                  a plot frame will contain the first 6 antennas, in three
                  rows and two columns.  Follow instructions on screen to
                  cycle through the frames
               if iteration = ''; then one frame can be filled with many
                  plots in a piecemeal fashion; for example
                  antenna='0'; subplot=221; plotcal()
                  antenna='1'; subplot=222; plotcal()
                  antenna='2'; subplot=223; plotcal()
                  antenna='3'; subplot=224; plotcal()
        overplot -- Overplot these values on current plot (if possible)
               default: False;
                  True (overplotting) can be done ONLY IF iteration=''
        clearpanel -- Ignore this parameter.
                  Clear nothing on the plot window, automatically
                  clear plotting area, clear the current plot area, or
                  clear the whole plot panel.
               options: None, Auto, Current, All (None and Auto not supported)
               default: Auto
               example: clearpanel='Current'
        iteration -- Create a sequence of plots, iterating over antenna, time,
                 field, and/or spw  
               default: '' --> create in all in one plot
               example: iteration='antenna' --> create a sequence of
                        separate plots separated by antenna. Flagging cannot
                        be done in iteration mode.
        plotrange -- Control the x and y ranges of the plot, as a list of
                 values, e.g., [xmin,xmax,ymin,ymax]
                 default=[] --> plot will self-scale
                 Note: time plotting ranges are cumbersome to use.
                       Use the zoom option
        showflags -- If true, only flagged solutions will be plotted
                 default: false --> only show unflagged solutions
        plotsymbol -- pylab plot symbol.  See cookbook for details
                   default: '.': large points
                   ',' = small points (see markersize)
                   '-' = connect points by line
                   colors are cycled automatically for multi-function plots
        plotcolor -- Initial color to use on each plot
                 default: 'blue'
        markersize -- Control the size of plot symbols
                  default: 5.0 --> a nice size for symbols
        fontsize -- Control the font size of title (axes labels will be
                  80% of this size)
                  default: 10.0
        showgui -- Whether or not to display the plotting GUI
                  default: True; example showgui=False
        figfile -- File name to save the plotted figure to.
                  default: ''; example figfile=myPlot.png

         Hints on using plotxy (see section 3.4 in cookbook)

         Useful Buttons at bottom left:
              5th--magnifying glass.  Click on this,
                       left mouse button rectangle drag will zoom
                       right mose button rectangle drag will unzoom a certain amount
              1st--restore original magnification

         Useful regions just above:
              Quit will terminate plotter
              Next will go to next plot as specified by iteration
              To locate, you must click 'Mark Region' first
                 then make appropriate region(s)
                 then click locate to list points on logger
                 DO NOT USE Flag, Unflag at the present time.

 
        """
        if type(plotrange)==float: plotrange=[plotrange]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['caltable'] = caltable
        mytmp['xaxis'] = xaxis
        mytmp['yaxis'] = yaxis
        mytmp['poln'] = poln
        mytmp['field'] = field
        mytmp['antenna'] = antenna
        mytmp['spw'] = spw
        mytmp['timerange'] = timerange
        mytmp['subplot'] = subplot
        mytmp['overplot'] = overplot
        mytmp['clearpanel'] = clearpanel
        mytmp['iteration'] = iteration
        mytmp['plotrange'] = plotrange
        mytmp['showflags'] = showflags
        mytmp['plotsymbol'] = plotsymbol
        mytmp['plotcolor'] = plotcolor
        mytmp['markersize'] = markersize
        mytmp['fontsize'] = fontsize
        mytmp['showgui'] = showgui
        mytmp['figfile'] = figfile
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'plotcal.xml')

        casalog.origin('plotcal')
        if trec.has_key('plotcal') and casac.utils().verify(mytmp, trec['plotcal']) :
            result = task_plotcal.plotcal(caltable, xaxis, yaxis, poln, field, antenna, spw, timerange, subplot, overplot, clearpanel, iteration, plotrange, showflags, plotsymbol, plotcolor, markersize, fontsize, showgui, figfile)

        else :
          result = False
        return result
