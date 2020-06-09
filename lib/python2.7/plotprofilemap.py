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
import task_plotprofilemap
def plotprofilemap(imagename='', figfile='', overwrite=False, transparent=False, pol=0, spectralaxis='', restfreq='', plotrange='', title='', linecolor='b', linestyle='-', linewidth=0.2, separatepanel=True, plotmasked='empty', maskedcolor='gray', showaxislabel=False, showtick=False, showticklabel=False, figsize='', numpanels=''):

        """Makes profile map.

The plotprofilemap makes spectral profile map from specified image. 
The task accepts both CASA image and FITS cube as an input.
    
It is necessary to specify existing CASA image or FITS cube as an 
imagename. Otherwise, the task will fail. If figfile is specified, 
profile map is saved as an PNG image. Please set overwrite to False 
if you don't want to overwrite existing file. 

    Keyword arguments:
    imagename -- input image name (CASA image or FITS cube)
    figfile -- output PNG image name. No output if figfile is empty
               default: '' (no output)
    overwrite -- overwrite existing output file
                 default: False
    transparent -- output transparent figure
                   default: False
    pol -- polarization component to be plotted. It is an index for stokes axis 
           of the image.
           default: 0
    spectralaxis -- spectral axis type
                    default: '' (use image's spectral axis)
                    options: 'channel', 'freuquency', 'velocity'
    restfreq -- rest frequency 
                default: '' (use image's rest frequency)
                example: '100GHz'
    plotrange -- spectral axis range to plot. unit for the range depends on 
                 what spectral axis is chosen: channel for 'channel', GHz for 
                 'frequency', and km/s for 'velocity'
                 default: '' (whole range)
                 example: '0~1000' (from 0.0 to 1000.0)
                          '~1000' (from minimul value to 1000.0)
                          '24~' (from 24.0 to maximum value)
    title -- title of the plot
             default: '' (no title)
    linecolor -- line color in matplotlib format
                 default: 'b' (blue)
                 example: 'r' (red), 'black', '#ff99ff'
    linestyle -- line style in matplotlib format
                 default: '-' (solid line)
                 example: '..' (dotted line), '.-' (solid line with point marker) 
    linewidth -- line width in points
                 default: 0.2
    separatepanel -- separate panels
                     default: True
    plotmasked -- masked data handling
                  default: 'empty' (show empty panel)
                  option: 'zero' (plot zero level)
                          'none' (show nothing)
                          'text' (show text indicating 'NO DATA')
                          'plot' (plot masked data with different 
                                  color specified by maskedcolor)
    maskedcolor -- line color for masked data
    showaxislabel -- Show axis labels on the bottom left panel
                     default: False
    showtick -- Show ticks
                default: False
    showticklabel -- Show tick labels on the bottom left panel
                     default: False
    figsize -- size of the figure
               default: '' (matplotlib default)
               example: '10cm' (10cm square)
                        '122mm,10cm' (122mm width and 10cm height)
    numpanels -- Number of panels
                 default: '' (auto)
                 example: '6,8' (nx=6, ny=8)
                          '8' (nx=8, ny=8)
                          
Number of panels along horizontal and vertical direction can be specified 
via the parameter 'numpanels'. It should be a string containing numerical 
value indicating number of panels. If only one number is given it will be 
applied to both axes. If you want to provide different numbers to horizontal 
and vertical axes, you should give two numbers as a string separated by comma. 
See example of the above parameter description section. 

If the number of panels is less than the number of pixels of input image, 
more than one pixels are assigned to one panel. In that case, spectra to be 
shown are the average of the assigned spectra in each pixel.
  
Default value for numpanels is empty string ('') which corresponds to an auto 
calculation of the number of panels based on the number of pixels of input 
image. Formula for the number of horizontal and vertical panels, nh and nv, 
are as follows:

    npanel = min(max(nx, ny), 8)
    step = (max(nx, ny) - 1) / npanel + 1
    nh = nx / step + 1
    nv = ny / step + 1
  
where nx and ny are the number of pixels along direction axes. In the above 
calculation, upper limit for nh and nv is 9.

  
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['figfile'] = figfile
        mytmp['overwrite'] = overwrite
        mytmp['transparent'] = transparent
        mytmp['pol'] = pol
        mytmp['spectralaxis'] = spectralaxis
        mytmp['restfreq'] = restfreq
        mytmp['plotrange'] = plotrange
        mytmp['title'] = title
        mytmp['linecolor'] = linecolor
        mytmp['linestyle'] = linestyle
        mytmp['linewidth'] = linewidth
        mytmp['separatepanel'] = separatepanel
        mytmp['plotmasked'] = plotmasked
        mytmp['maskedcolor'] = maskedcolor
        mytmp['showaxislabel'] = showaxislabel
        mytmp['showtick'] = showtick
        mytmp['showticklabel'] = showticklabel
        mytmp['figsize'] = figsize
        mytmp['numpanels'] = numpanels
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'plotprofilemap.xml')

        casalog.origin('plotprofilemap')
        if trec.has_key('plotprofilemap') and casac.utils().verify(mytmp, trec['plotprofilemap']) :
            result = task_plotprofilemap.plotprofilemap(imagename, figfile, overwrite, transparent, pol, spectralaxis, restfreq, plotrange, title, linecolor, linestyle, linewidth, separatepanel, plotmasked, maskedcolor, showaxislabel, showtick, showticklabel, figsize, numpanels)

        else :
          result = False
        return result
