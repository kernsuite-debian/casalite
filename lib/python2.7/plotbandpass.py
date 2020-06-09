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
import task_plotbandpass
def plotbandpass(caltable='', antenna='', field='', spw='', yaxis='amp', xaxis='chan', figfile='', plotrange=[0,0,0,0], caltable2='', overlay='', showflagged=False, timeranges='', buildpdf=False, caltable3='', markersize=3, density=108, interactive=True, showpoints='auto', showlines='auto', subplot='22', zoom='', poln='', showatm=False, pwv='auto', gs='gs', convert='convert', chanrange='', solutionTimeThresholdSeconds=30.0, debug=False, phase='', vis='', showtsky=False, showfdm=False, showatmfield='', lo1='', showimage=False, showatmpoints=False, parentms='', pdftk='pdftk', channeldiff=False, edge=8, resample=1, platformingThreshold=10.0, platformingSigma=10.0, basebands='', showBasebandNumber=False, scans='', figfileSequential=False, chanrangeSetXrange=False):

        """Makes detailed plots of Tsys and bandpass solutions.

plotbandpass('X3c1.tsys',overlay='antenna',yaxis='amp',field='0~1,4',xaxis='chan',figfile='tsys.png')

plotbandpass('bandpass.bcal',caltable2='bandpass.bcal_smooth',xaxis='freq')  

plotbandpass('bandpass.bcal',caltable2='bandpass.bcal_smooth',xaxis='freq',poln='X',showatm=T)

plotbandpass('bandpass.bcal',channeldiff='5')

This task returns void unless the channeldiff option is selected, in which case it returns a
dictionary containing the statistics of the solutions, keyed by the antenna name, followed
by the spw, timerange, polarization, and finally 'amp' and/or 'phase' depending
on the yaxis selection.  

   Keyword arguments:

 antenna: must be either an ID (int or string or list), or a single antenna name or list
 basebands: show only spws from the specified baseband or list of basebands (default: ''=[]=all)
 buildpdf: True/False, if True and figfile is set, assemble pngs into a pdf
 caltable: a bandpass table, of type B or BPOLY
 caltable2: a second cal table, of type BPOLY or B, to overlay on a B table
 caltable3: a third cal table, of type BPOLY, to overlay on the first two
 channeldiff: set to value > 0 to plot derivatives of amplitude, the value is also used as sigma, and any outliers beyond this sigma will be printed to the logger
 chanrange: set xrange (e.g. "5~100") over which to autoscale y-axis for xaxis='freq'
 chanrangeSetXrange: if True, then chanrange also sets the xrange to display
 convert: full path for convert command (in case it's not found)
 density: dpi to use in creating PNGs and PDFs (default=108)
 edge: the number of edge channels to ignore in finding outliers (for channeldiff>0)
 field: must be an ID, source name, or list thereof; can use trailing *: 'J*'
 figfile: the base_name of the png files to save: base_name.antX.spwY.png
 figfileSequential: naming scheme, False: name by spw/antenna (default)
                    True: figfile.1.png, figfile.2.png, etc.
 gs: full path for ghostscript command (in case it's not found)
 interactive: if False, then figfile will run to completion automatically
 lo1: specify the LO1 setting (in GHz) for the observation
 overlay: 'antenna','time','spw', or 'baseband', make 1 plot with different items in colors
 markersize: size of points (default=3)
 ms: name of the ms for this table, in case it does not match the string in the caltable
 parentms: name of the parent ms, in case the ms has been previously split
 pdftk: full path for pdftk command (in case it's not found)
 phase: the y-axis limits to use for phase plots when yaxis='both'
 platformingSigma: declare platforming if the amplitude derivative exceeds this many times the MAD
 platformingThreshold: if platformingSigma=0, then declare platforming if the amplitude
                       derivative exceeds this percentage of the median
 plotrange: define axis limits: [x0,x1,y0,y1] where 0,0 means auto
 poln: polarizations to plot (e.g. 'XX','YY','RR','LL' or '' for both)
 pwv: define the pwv to use for the showatm option: 'auto' or value in mm
 resample: channel expansion factor to use when computing MAD of derivative (for channeldiff>0)
 scans: show only solutions for the specified scans (int, list, or string)
 showatm: compute and overlay the atmospheric transmission curve (on B or Tsys solutions)
 showatmfield: use first observation of this fieldID or name
 showatmPoints: draw atmospheric curve with points instead of a line
 showBasebandNumber: put the BBC_NO in the title of each plot
 showfdm: when showing TDM spws with xaxis='freq', draw locations of FDM spws
 showflagged:  show the values of data, even if flagged
 showimage: also show the atmospheric curve for the image sideband (in black)
 showtsky: compute and overlay the sky temperature curve instead of transmission
 showlines: draw lines connecting the data (default=T for amp, F for phase)
 showpoints: draw points for the data (default=F for amp, T for phase)
 solutionTimeThresholdSeconds: consider 2 solutions simultaneous if within this interval (default=60)
 spw: must be single ID or list or range (e.g. 0~4, not the original ID)
 subplot: 11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is ignored
 timeranges: show only these timeranges, the first timerange being 0
 xaxis: 'chan' or 'freq'
 yaxis: 'amp', 'tsys', 'phase', or 'both' amp+phase == 'ap'. Append 'db' for dB
 zoom: 'intersect' will zoom to overlap region of caltable with caltable2

  
        """
        if type(plotrange)==float: plotrange=[plotrange]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['caltable'] = caltable
        mytmp['antenna'] = antenna
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['yaxis'] = yaxis
        mytmp['xaxis'] = xaxis
        mytmp['figfile'] = figfile
        mytmp['plotrange'] = plotrange
        mytmp['caltable2'] = caltable2
        mytmp['overlay'] = overlay
        mytmp['showflagged'] = showflagged
        mytmp['timeranges'] = timeranges
        mytmp['buildpdf'] = buildpdf
        mytmp['caltable3'] = caltable3
        mytmp['markersize'] = markersize
        mytmp['density'] = density
        mytmp['interactive'] = interactive
        mytmp['showpoints'] = showpoints
        mytmp['showlines'] = showlines
        mytmp['subplot'] = subplot
        mytmp['zoom'] = zoom
        mytmp['poln'] = poln
        mytmp['showatm'] = showatm
        mytmp['pwv'] = pwv
        mytmp['gs'] = gs
        mytmp['convert'] = convert
        mytmp['chanrange'] = chanrange
        mytmp['solutionTimeThresholdSeconds'] = solutionTimeThresholdSeconds
        mytmp['debug'] = debug
        mytmp['phase'] = phase
        mytmp['vis'] = vis
        mytmp['showtsky'] = showtsky
        mytmp['showfdm'] = showfdm
        mytmp['showatmfield'] = showatmfield
        mytmp['lo1'] = lo1
        mytmp['showimage'] = showimage
        mytmp['showatmpoints'] = showatmpoints
        mytmp['parentms'] = parentms
        mytmp['pdftk'] = pdftk
        mytmp['channeldiff'] = channeldiff
        mytmp['edge'] = edge
        mytmp['resample'] = resample
        mytmp['platformingThreshold'] = platformingThreshold
        mytmp['platformingSigma'] = platformingSigma
        mytmp['basebands'] = basebands
        mytmp['showBasebandNumber'] = showBasebandNumber
        mytmp['scans'] = scans
        mytmp['figfileSequential'] = figfileSequential
        mytmp['chanrangeSetXrange'] = chanrangeSetXrange
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'plotbandpass.xml')

        casalog.origin('plotbandpass')
        if trec.has_key('plotbandpass') and casac.utils().verify(mytmp, trec['plotbandpass']) :
            result = task_plotbandpass.plotbandpass(caltable, antenna, field, spw, yaxis, xaxis, figfile, plotrange, caltable2, overlay, showflagged, timeranges, buildpdf, caltable3, markersize, density, interactive, showpoints, showlines, subplot, zoom, poln, showatm, pwv, gs, convert, chanrange, solutionTimeThresholdSeconds, debug, phase, vis, showtsky, showfdm, showatmfield, lo1, showimage, showatmpoints, parentms, pdftk, channeldiff, edge, resample, platformingThreshold, platformingSigma, basebands, showBasebandNumber, scans, figfileSequential, chanrangeSetXrange)

        else :
          result = False
        return result
