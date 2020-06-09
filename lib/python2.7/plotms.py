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
import task_plotms
def plotms(vis='', gridrows=1, gridcols=1, rowindex=0, colindex=0, plotindex=0, xaxis='', xdatacolumn='', xframe='', xinterp='', yaxis='', ydatacolumn='', yframe='', yinterp='', yaxislocation='', selectdata=True, field='', spw='', timerange='', uvrange='', antenna='', scan='', correlation='', array='', observation='', intent='', feed='', msselect='', averagedata=True, avgchannel='', avgtime='', avgscan=False, avgfield=False, avgbaseline=False, avgantenna=False, avgspw=False, scalar=False, transform=True, freqframe='', restfreq='', veldef='RADIO', shift=[0.0, 0.0], extendflag=False, extcorr=False, extchannel=False, iteraxis='', xselfscale=False, yselfscale=False, xsharedaxis=False, ysharedaxis=False, customsymbol=False, symbolshape='autoscaling', symbolsize=2, symbolcolor='0000ff', symbolfill='fill', symboloutline=False, coloraxis='', customflaggedsymbol=False, flaggedsymbolshape='circle', flaggedsymbolsize=2, flaggedsymbolcolor='ff0000', flaggedsymbolfill='fill', flaggedsymboloutline=False, xconnector='', timeconnector=False, plotrange=[], title='', titlefont=0, xlabel='', xaxisfont=0, ylabel='', yaxisfont=0, showmajorgrid=False, majorwidth=1, majorstyle='', majorcolor='B0B0B0', showminorgrid=False, minorwidth=1, minorstyle='', minorcolor='D0D0D0', showlegend=False, legendposition='', plotfile='', expformat='', verbose=True, exprange='', highres=False, dpi=-1, width=-1, height=-1, overwrite=False, showgui=True, clearplots=True, callib=[''], headeritems='', showatm=False, showtsky=False, showimage=False):

        """A plotter/interactive flagger for visibility data.

        Task for plotting and interacting with visibility
        data.  Limited support for caltable plotting is also
        included as of CASA v4.1.

        A variety of axes choices (including data column) along 
        with MS selection and averaging options are provided for data 
        selection.  Flag extension parameters are also available for
        flagging operations in the plotter.
        
        All of the provided parameters can also be set using the GUI once
        the application has been launched.  Additional and more specific
        operations are available through the GUI and/or through the plotms
        tool (pm).

        Most basic functions (plotting, iteration, locate, flagging)
        will work for most CalTables. Parameterized CalTables
        (delays, antpos, gaincurve, opacity), will, at best, currently 
        just plot the simple parameters contained in the
        table, not the effective amplitudes or phases sampled at
        observing times, frequencies etc.  BPOLY and GSPLINE tables
        are not yet supported.   Features currently unsupported for
        CalTables include Averaging, Transformations (velocity 
        conversions, etc.), and some details of selection (channel and 
        polarization selection are not yet enabled) and axes choices 
        (geometry options are not yet enabled).  In the plotms gui,
        many options irrelevant for CalTables are not yet hidden when
        interacting with a CalTable, and such settings will be ignored
        (when benign) or cause an error message.

    Keyword arguments:
    vis -- input MS or CalTable
           default: ''  (will merely launch the gui)
    gridrows -- Number of subplot rows
                    default: 1 
    gridcols -- Number of subplot columns
                    default: 1
    rowindex -- Row location of the subplot (0-based).
                    default: 0
    colindex -- Column location of the subplot (0-based).
                    default: 0
    plotindex -- Index to address a subplot (0-based). 
                    default: 0                         
    xaxis, yaxis -- what to plot on the two axes
                    default: '' (defaults are xaxis='time',
                                 yaxis='amp' on first execution;
                                 thereafter the most recent
                                 settings are used)
              valid options (=indicates valid synonyms): 
               MS Ids and other meta info:
                 'scan'   (number)
                 'field'  (index)
                 'time',  
                 'interval'='timeint'='timeinterval'='time_interval'
                 'spw'    (index)
                 'chan'='channel'    (index)  
                 'freq'='frequency'  (GHz)
                 'vel'='velocity'   (km/s)
                 'corr'='correlation'  (index)
                 'ant1'='antenna1'   (index)
                 'ant2'='antenna2'   (index)
                 'baseline'  (a baseline index) 
                 'row'   (absoute row Id from the MS)
                 'observation' (index)
                 'intent'      (index)
                 'feed1'       (index)
                 'feed2'       (index)
               Visibility values, flags:
                 'amp'='amplitude'
                 'phase'  (deg)
                 'real'  
                 'imag'='imaginary'
                 'wt'='weight'  (unchannelized)
                 'wtsp'='weightspectrum'
                 'flag'
                 'flagrow'
               Observational geometry:
                 'uvdist'  (meters)
                 'uvwave'='uvdistl'='uvdist_l'  (wavelengths, per channel)
                 'u'  (meters)
                 'v'  (meters)
                 'w'  (meters)
                 'uwave'  ('u' in wavelengths, per channel)
                 'vwave'  ('v' in wavelengths, per channel)
                 'wwave'  ('w' in wavelengths, per channel)
                 'azimuth'  (at array reference; degrees)
                 'elevation'  (at array reference; degrees)
                 'hourang'='hourangle'  (at array reference; hours)
                 'parang'='parangle'='parallacticangle'  (at array reference; degrees)
               Antenna-based (only works vs. data Ids):
                 'ant'='antenna'
                 'ant-azimuth' 
                 'ant-elevation'
                 'ant-ra'
                 'ant-dec'
                 'ant-parang'='ant-parangle'
               Calibration:
                 'gainamp'='gamp'
                 'gainphase'='gphase'
                 'gainreal'='greal'
                 'gainimag'='gimag'
                 'delay'='del'
                 'opacity'='opac'
                 'swpower'='swp'='switchedpower'='spgain'


      >>> xaxis, yaxis expandable parameters
        xdatacolumn, 
        ydatacolumn  -- data column to use for Visibility values:
                        default: '' ('data' on first execution;
                                     thereafter the most recent
                                     setting is used)
                        valid options:  'data'      (observed)
                                        'corrected'='corr'
                                        'model'
                                        'residual'  (aliases 'corrected-model')
                                        'corrected-model'
                                        'data-model'
                                        'data/model'
                                        'corected/model'
                                        'float'
                        Note that residuals are complex (vector) differences or ratios.
    
    selectdata -- data selection parameters flag
                  default: True  (reveals data selection parameters
                                  described below)
                  Consult listobs output for data selection values,
                  and see help par.selectdata for more detailed 
                  information on syntax; also, visit
                  http://casa.nrao.edu/other_doc.shtml and click
                  on "Measurement Set selection syntax" for more
                  tips on using data selection parameters in CASA)

      >>> selectdata expandable parameters:

      field -- Select field using field id(s) or field name(s).
              default: ''=all fields
              If field string is a non-negative integer, it is assumed a
                field index,  otherwise, it is assumed a field name
              field='0~2'; field ids 0,1,2
              field='0,4,5~7'; field ids 0,4,5,6,7
              field='3C286,3C295'; field named 3C286 and 3C295
              field = '3,4C*'; field id 3, all names starting with 4C
      spw -- Select spectral window/channels
               type 'help par.selection' for more examples.
             spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
             spw='<2';  spectral windows less than 2 (i.e. 0,1)
             spw='0:5~61'; spw 0, channels 5 to 61, INCLUSIVE
             spw='*:5~61'; all spw with channels 5 to 61
             spw='0,10,3:3~45'; spw 0,10 all channels, spw 3, channels 3 to 45.
             spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
             spw='0:0~10;15~60'; spectral window 0 with channels 0-10,15-60
                       NOTE ';' to separate channel selections

      timerange  -- Select data based on time range:
              default = '' (all); examples,
              timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
              Note: if YYYY/MM/DD is missing date defaults to first day in data set
              timerange='09:14:0~09:54:0' picks 40 min on first day
              timerange= '25:00:00~27:30:00' picks 1 hr to 3 hr 30min on NEXT day
              timerange='09:44:00' pick data within one integration of time
              timerange='>10:24:00' data after this time
      uvrange -- Select data within uvrange (default units meters)
              default: '' (all); example:
              uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
              uvrange='>4klambda';uvranges greater than 4 kilo lambda

      antenna -- Select data based on antenna/baseline
              default: '' (all, including auto-correlations, if present)
              If antenna string is a non-negative integer, it is assumed an
                antenna index, otherwise, it is assumed as an antenna name
              antenna='5&6'; baseline between antenna index 5 and index 6.
              antenna='!ea02'; exclude EVLA antenna 2.
              antenna='ea13;!ea22'; EVLA antenna 13, excluding antenna 22.
              antenna='VA05&VA06'; baseline between VLA antenna 5 and 6.
              antenna='5&6;7&8'; baselines with indices 5-6 and 7-8
              antenna='5'; all baselines with antenna index 5
              antenna='05'; all baselines with antenna number 05 (VLA old name)
              antenna='5,6,10'; all baselines with antennas 5,6,10 index numbers
              NB: For explicit selections, use a single ampersand (&) to
              select only cross-correlations among the specified antennas, 
              double ampersands (&&) to select cross- and
              auto-correlations among the specified antennas, and
              triple ampersands (&&&) to select only
              auto-correlations.  E.g.:
              antenna='*&'; selects all cross-correlation baseline
                            (excludes all auto-correlations)
              antenna='*&&&'; selects all auto-correlation baselines
                              (excludes all cross-correlations)
              antenna='1&&1,2,3'; selects baselines 1-1 (auto), 1-2,1-3 (cross)
              antenna='VA05&&&'; selects the VA05 autocorrelation
              See the link noted above for more information.
      scan -- Scan numbers or ranges.
              default: ''  (all scans)
              scan='1,2,6,43'; scans 1, 2, 6, and 43
              scan='3~14'; scans 3 through 14, inclusive
      correlation -- Select by correlation (polarization when plotting cal tables)
                default: ''  (all correlations/polarizations)
                For measurement sets: 'RR','RL','LR','LL','XX','XY','YX','YY'
                For cal tables: 'R','L','RL','X','Y','XY','/' (for ratio plots)
                or any comma-separated combination;
                use basis (R/L or X/Y) appropriate to the table
      array -- Select the array id
               default: ''  (all array ids)
      observation -- Select by observation ID(s).
                     default: ''-->all;
                     observation='0' (select obsID 0)
      intent -- Select observing intent  
                default: ''  (no selection by intent)  
                intent='*BANDPASS*'  (selects data labelled with  
                    BANDPASS intent)
      feed -- Select by feed IDs
              default: '' (all feeds)
              feed='1~2'
      msselect -- Optional TaQL data selection

    averagedata -- data averaging parameters flag
                   default: True   (reveals expandable parameters
                                    described below)
      >>> averagedata expandable parameters
        avgchannel -- average over channel?  either blank for none, or a value
                      in channels.
                      default: '' (no channel averaging).
        avgtime -- average over time?  either blank for none, or a value in
                   seconds.
                   default: '' (no time averaging).
        avgscan -- average over scans?  only valid if time averaging is turned
                   on.
                   default: False.
        avgfield -- average over fields?  only valid if time averaging is
                    turned on.
                    default: False.
        avgbaseline -- average over selected baselines; mutually 
                       exclusive with avgantenna.
                       default: False.  (no averaging over baseline)
        avgantenna -- form per-antenna averages; mutually exclusive with
                      avgbaseline.
                      default: False.   (no per-antenna averaging)
        avgspw -- average over selected spectral windows?
                  default: False.  (no average of spectral windows)
        scalar -- scalar averaging?
                  default: False  (i.e., do vector averaging)
    
    transform -- apply various transformations on data for plotting
                 default: True
      >>> transform expandable parameters
        freqframe -- the coordinate frame in which to render frequency and velocity axes
                 default: ''  (unspecified: will use frame in which data were taken)
                 options: LSRK, LSRD, BARY, GEO, TOPO, GALACTO, LGROUP, CMB
        restfreq -- the rest frequency to use in velocity conversions (MHz)
                 default: '' (use spw central frequency and show relative velocity)
                 example: '22235.08MHz'
        veldef -- the velocity definition to use
                 default: 'RADIO'
                 options: 'RADIO','OPT','TRUE'
        shift -- adjust phase according to a phase center shift [dx,dy] (arcsec)
                 NB: the phase shift in plotms is an approximate transformation
                 default: [0,0]  (no shift)

    extendflag -- have flagging extend to other data points?
                  default: False.
      >>> extendflag expandable parameters
        extcorr -- extend flags based on correlation? 
                   default: False.
        extchannel -- extend flags based on channel?

    iteraxis -- axis upon which iterate plots (one plot per page, for now)
                default: '' (no iteration)
                options: 'scan','field','spw','baseline','antenna','time','corr',''
      >>> iteraxis expandable parameters
        xselfscale -- When True, iterated plots have a common x-axis range (scale).
        yselfscale -- When True, iterated plots have a common y-axis range (scale).
                      default: false, which will scale all plots individually
        xsharedaxis -- Iterated plots on a grid share a common external x-axis per column (must also set xselfscale=True and gridcols>1) 
                      default: false, each plot will have its own x-axis.
        ysharedaxis -- Iterated plots on a grid share a common external y-axis per row (must also set yselfscale=True and gridrows>1)
                      default: false, each plot will have its own y-axis.              

    customsymbol -- If true, use a custom symbol for drawing unflagged points
                    default: False
      >>> customsymbol expandable parameters
        symbolshape -- If true, use a custom shape to draw unflagged symbols
                       default: 'autoscaling' (ignores symbolsize)
                       options: 'autoscaling', 'circle', 'square', 'diamond', 'pixel', 'nosymbol'
        symbolsize -- size of the unflagged symbols in pixels
                      default: 2
        symbolcolor -- color to use for unflagged symbols; can be a RGB hex code or a color name
                       default: '0000ff'
                       example: 'purple'
        symbolfill -- type of fill to use for unflagged symbols
                      default: 'fill'
                      options: 'fill', 'mesh1', 'mesh2', 'mesh3', 'nofill'
        symboloutline -- If true, outline unflagged symbols in black

    coloraxis -- axis upon which to colorize the plotted points
                options (= indicates synonyms):
                    'scan',  'field',  'spw',  'antenna1'='ant1',  'antenna2'='ant2',
                    'baseline',  'channel'='chan',  'corr'='correlation', 'time', 
                    'observation', 'intent'
                default: ''  (use a single color for all points)

    customflaggedsymbol -- If true, use a custom symbol for drawing flagged points
                           default: False
      >>> customflaggedsymbol expandable parameters
        symbolshape -- If true, use a custom shape to draw flagged symbols
                       default: 'nosymbol'
                       options: 'autoscaling', 'circle', 'square', 'diamond', 'pixel', 'nosymbol'
        symbolsize -- size of the flagged symbols in pixels
                      default: 2
        symbolcolor -- color to use for flagged symbols; can be a RGB hex code or a color name
                       default: '0000ff'
                       example: 'purple'
        symbolfill -- type of fill to use for flagged symbols
                      default: 'fill'
                      options: 'fill', 'mesh1', 'mesh2', 'mesh3', 'nofill'
        symboloutline -- If true, outline flagged symbols in black

    plotrange -- manual plot axis ranges: [xmin,xmax,ymin,ymax]
                 Does not affect data selection.
                 default: []; both axes will be autoscaled according
                 to the ranges found in the selected data
                 If xmin=xmax (or ymin=ymax) then that axis will
                 be autoscaled, e.g.:
                 [0,0,-2.0,14.0]; autoscale the xaxis, and use 
                                  ymin=-2.0, ymax=14.0

    title  -- title along top of plot (called "canvas" in some places)
    titlefont -- plot title font size
                 default: 0 (autosize depending on grid)
    xlabel -- text to label horizontal axis, with formatting using '%%'
    xaxisfont -- x-axis font size
                 default: 0 (autosize)
    ylabel -- text to label horizontal axis, with formatting using '%%' 
    yaxisfont -- y-axis font size
                 default: 0 (autosize)
    
    
    showmajorgrid  -- show major grid lines 
                  default: False
      >>>  showmajorgrid expandable parameters
        majorwidth  -- line width in pixels of major grid lines
        majorstyle  -- major grid line style: solid dash dot none
        majorcolor  -- color in hex code of major grid lines

    showminorgrid  -- show minor grid lines
                  default: False
      >>>  showminorgrid expandable parameters
        minorwidth  --  line width in pixels of minor grid lines
        minorstyle  --  minor grid line style: solid dash dot none
        minorcolor  --  color in hex code of minor grid lines

    plotfile -- name of plot file to save automatically
                default: ''  (i.e., draw an interactive plot in the gui)
      >>> plotfile expandable parameters
        expformat -- export format type; if 'txt' is used an ASCII dump of the plotted points is generated (also available in the export tab)
                     default:  ''   (plotfile extension will be used)
                     options: 'jpg', 'png', 'ps', 'pdf', 'txt'
        verbose -- when export format is 'txt', print metadata for x and y values
                   default: True 
        exprange -- pages to export for iteration plots
                    default:   ''
                    options: 'current', 'all'             
        highres -- use high resolution in exported plot 
                   default: False (use screen resolution)
        dpi -- DPI of exported plot
               default: -1 (not set)
        width -- width of exported plot
                 default: -1 (not set)
        height -- height of exported plot
                  default: -1 (not set)
        overwrite -- overwrite plot file if it already exists
                     default: False
      
    callib -- calibration library string, list of strings, or filename
              default: '' 
    
    showgui - Whether or not to display the plotting GUI
              default: True
              
    headeritems -- append header items specific to this plot to the current list
                of page header items.
                Comma-separated string of header item selection keywords.
                Allowed keywords: 'obsdate','obstime','filename','projid',
                                  'targname','targdir','telescope','observer',
                                  'ycolumn'
                default: ''
                example: 'filename,projid,targname'




        """
        if type(shift)==float: shift=[shift]
        if type(plotrange)==float: plotrange=[plotrange]
        if type(callib)==str: callib=[callib]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['gridrows'] = gridrows
        mytmp['gridcols'] = gridcols
        mytmp['rowindex'] = rowindex
        mytmp['colindex'] = colindex
        mytmp['plotindex'] = plotindex
        mytmp['xaxis'] = xaxis
        mytmp['xdatacolumn'] = xdatacolumn
        mytmp['xframe'] = xframe
        mytmp['xinterp'] = xinterp
        mytmp['yaxis'] = yaxis
        mytmp['ydatacolumn'] = ydatacolumn
        mytmp['yframe'] = yframe
        mytmp['yinterp'] = yinterp
        mytmp['yaxislocation'] = yaxislocation
        mytmp['selectdata'] = selectdata
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['timerange'] = timerange
        mytmp['uvrange'] = uvrange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['correlation'] = correlation
        mytmp['array'] = array
        mytmp['observation'] = observation
        mytmp['intent'] = intent
        mytmp['feed'] = feed
        mytmp['msselect'] = msselect
        mytmp['averagedata'] = averagedata
        mytmp['avgchannel'] = avgchannel
        mytmp['avgtime'] = avgtime
        mytmp['avgscan'] = avgscan
        mytmp['avgfield'] = avgfield
        mytmp['avgbaseline'] = avgbaseline
        mytmp['avgantenna'] = avgantenna
        mytmp['avgspw'] = avgspw
        mytmp['scalar'] = scalar
        mytmp['transform'] = transform
        mytmp['freqframe'] = freqframe
        mytmp['restfreq'] = restfreq
        mytmp['veldef'] = veldef
        mytmp['shift'] = shift
        mytmp['extendflag'] = extendflag
        mytmp['extcorr'] = extcorr
        mytmp['extchannel'] = extchannel
        mytmp['iteraxis'] = iteraxis
        mytmp['xselfscale'] = xselfscale
        mytmp['yselfscale'] = yselfscale
        mytmp['xsharedaxis'] = xsharedaxis
        mytmp['ysharedaxis'] = ysharedaxis
        mytmp['customsymbol'] = customsymbol
        mytmp['symbolshape'] = symbolshape
        mytmp['symbolsize'] = symbolsize
        mytmp['symbolcolor'] = symbolcolor
        mytmp['symbolfill'] = symbolfill
        mytmp['symboloutline'] = symboloutline
        mytmp['coloraxis'] = coloraxis
        mytmp['customflaggedsymbol'] = customflaggedsymbol
        mytmp['flaggedsymbolshape'] = flaggedsymbolshape
        mytmp['flaggedsymbolsize'] = flaggedsymbolsize
        mytmp['flaggedsymbolcolor'] = flaggedsymbolcolor
        mytmp['flaggedsymbolfill'] = flaggedsymbolfill
        mytmp['flaggedsymboloutline'] = flaggedsymboloutline
        mytmp['xconnector'] = xconnector
        mytmp['timeconnector'] = timeconnector
        mytmp['plotrange'] = plotrange
        mytmp['title'] = title
        mytmp['titlefont'] = titlefont
        mytmp['xlabel'] = xlabel
        mytmp['xaxisfont'] = xaxisfont
        mytmp['ylabel'] = ylabel
        mytmp['yaxisfont'] = yaxisfont
        mytmp['showmajorgrid'] = showmajorgrid
        mytmp['majorwidth'] = majorwidth
        mytmp['majorstyle'] = majorstyle
        mytmp['majorcolor'] = majorcolor
        mytmp['showminorgrid'] = showminorgrid
        mytmp['minorwidth'] = minorwidth
        mytmp['minorstyle'] = minorstyle
        mytmp['minorcolor'] = minorcolor
        mytmp['showlegend'] = showlegend
        mytmp['legendposition'] = legendposition
        mytmp['plotfile'] = plotfile
        mytmp['expformat'] = expformat
        mytmp['verbose'] = verbose
        mytmp['exprange'] = exprange
        mytmp['highres'] = highres
        mytmp['dpi'] = dpi
        mytmp['width'] = width
        mytmp['height'] = height
        mytmp['overwrite'] = overwrite
        mytmp['showgui'] = showgui
        mytmp['clearplots'] = clearplots
        mytmp['callib'] = callib
        mytmp['headeritems'] = headeritems
        mytmp['showatm'] = showatm
        mytmp['showtsky'] = showtsky
        mytmp['showimage'] = showimage
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'plotms.xml')

        casalog.origin('plotms')
        if trec.has_key('plotms') and casac.utils().verify(mytmp, trec['plotms']) :
            result = task_plotms.plotms(vis, gridrows, gridcols, rowindex, colindex, plotindex, xaxis, xdatacolumn, xframe, xinterp, yaxis, ydatacolumn, yframe, yinterp, yaxislocation, selectdata, field, spw, timerange, uvrange, antenna, scan, correlation, array, observation, intent, feed, msselect, averagedata, avgchannel, avgtime, avgscan, avgfield, avgbaseline, avgantenna, avgspw, scalar, transform, freqframe, restfreq, veldef, shift, extendflag, extcorr, extchannel, iteraxis, xselfscale, yselfscale, xsharedaxis, ysharedaxis, customsymbol, symbolshape, symbolsize, symbolcolor, symbolfill, symboloutline, coloraxis, customflaggedsymbol, flaggedsymbolshape, flaggedsymbolsize, flaggedsymbolcolor, flaggedsymbolfill, flaggedsymboloutline, xconnector, timeconnector, plotrange, title, titlefont, xlabel, xaxisfont, ylabel, yaxisfont, showmajorgrid, majorwidth, majorstyle, majorcolor, showminorgrid, minorwidth, minorstyle, minorcolor, showlegend, legendposition, plotfile, expformat, verbose, exprange, highres, dpi, width, height, overwrite, showgui, clearplots, callib, headeritems, showatm, showtsky, showimage)

        else :
          result = False
        return result
