#
# This file was generated using xslt from its XML file
#
# Copyright 2014, Associated Universities Inc., Washington DC
#
import sys
import os
import datetime
#from casac import *
import casac
import string
import time
import inspect
import numpy
from casa_stack_manip import stack_frame_find
from odict import odict
from types import *
from task_plotbandpass import plotbandpass
class plotbandpass_cli_:
    __name__ = "plotbandpass"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (plotbandpass_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'caltable':None, 'antenna':None, 'field':None, 'spw':None, 'yaxis':None, 'xaxis':None, 'figfile':None, 'plotrange':None, 'caltable2':None, 'overlay':None, 'showflagged':None, 'timeranges':None, 'buildpdf':None, 'caltable3':None, 'markersize':None, 'density':None, 'interactive':None, 'showpoints':None, 'showlines':None, 'subplot':None, 'zoom':None, 'poln':None, 'showatm':None, 'pwv':None, 'gs':None, 'convert':None, 'chanrange':None, 'solutionTimeThresholdSeconds':None, 'debug':None, 'phase':None, 'vis':None, 'showtsky':None, 'showfdm':None, 'showatmfield':None, 'lo1':None, 'showimage':None, 'showatmpoints':None, 'parentms':None, 'pdftk':None, 'channeldiff':None, 'edge':None, 'resample':None, 'platformingThreshold':None, 'platformingSigma':None, 'basebands':None, 'showBasebandNumber':None, 'scans':None, 'figfileSequential':None, 'chanrangeSetXrange':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, caltable=None, antenna=None, field=None, spw=None, yaxis=None, xaxis=None, figfile=None, plotrange=None, caltable2=None, overlay=None, showflagged=None, timeranges=None, buildpdf=None, caltable3=None, markersize=None, density=None, interactive=None, showpoints=None, showlines=None, subplot=None, zoom=None, poln=None, showatm=None, pwv=None, gs=None, convert=None, chanrange=None, solutionTimeThresholdSeconds=None, debug=None, phase=None, vis=None, showtsky=None, showfdm=None, showatmfield=None, lo1=None, showimage=None, showatmpoints=None, parentms=None, pdftk=None, channeldiff=None, edge=None, resample=None, platformingThreshold=None, platformingSigma=None, basebands=None, showBasebandNumber=None, scans=None, figfileSequential=None, chanrangeSetXrange=None, ):

        """Makes detailed plots of Tsys and bandpass solutions.

        Detailed Description:
Developed at the NAASC, this is a generic task to display CASA 
  Tsys and bandpass solution tables with options to overlay them in various
  combinations, and/or with an atmospheric transmission or sky temperature
  model.  It works with both the 'new' (casa 3.4) and 'old' calibration
  table formats, and allows for mixed mode spws (e.g. TDM and FDM for ALMA).
  It uses the new msmd tool to access the information about an ms.  This
  task is still being developed as new ALMA observing modes are commissioned.
  So if you encounter problems, please report them.
  
        Arguments :
                caltable: Input table name, either a bandpass solution or a Tsys solution
                   Default Value: 

                antenna: A comma-delimited string list of antennas (either names or integer indices) for which to display solutions.  Default = all antennas.
                   Default Value: 

                field: A comma-delimited string list of fields (either names or integer indices) for which to display solutions.  Default = all fields.
                   Default Value: 

                spw: A comma-delimited string list of spws for which to display solutions.  Default = all spws.
                   Default Value: 

                yaxis: The quantity to plot on the y-axis ("amp", "phase", "both", "tsys", append "db" for dB).
                   Default Value: amp
                   Allowed Values:
                                amp
                                ampdb
                                phase
                                tsys
                                both
                                bothdb
                                ap
                                apdb

                xaxis: The quantity to plot on the x-axis ("chan" or "freq").
                   Default Value: chan
                   Allowed Values:
                                chan
                                freq

                figfile: The name of the plot file to produce.
                   Default Value: 

                plotrange: The axes limits to use [x0,x1,y0,y1].
                   Default Value: 0,0,0,0

                caltable2: A second cal table, of type BPOLY or B, to overlay on a B table
                   Default Value: 

                overlay: Show multiple solutions in same frame in different colors (time, antenna, spw, baseband, or time,antenna)
                   Default Value: 
                   Allowed Values:
                                
                                antenna
                                baseband
                                spw
                                time
                                antenna,time
                                time,antenna

                showflagged: Show the values of the solution, even if flagged
                   Default Value: False

                timeranges: Show only these timeranges, the first timerange being 0
                   Default Value: 

                buildpdf: If True, assemble all the pngs into a pdf
                   Default Value: False

                caltable3: A third cal table, of type BPOLY, to overlay on the first two tables
                   Default Value: 

                markersize: Size of points
                   Default Value: 3

                density: dpi to use in creating PNGs and PDFs (default=108)
                   Default Value: 108

                interactive: if False, then run to completion automatically without pause
                   Default Value: True

                showpoints: Draw points for the data (default=F for amp, T for phase)
                   Default Value: auto

                showlines: Draw lines connecting the data (default=T for amp, F for phase)
                   Default Value: auto

                subplot: 11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is ignored
                   Default Value: 22
                   Allowed Values:
                                11
                                21
                                31
                                41
                                51
                                61
                                71
                                81
                                22
                                32
                                42

                zoom: "intersect" will zoom to overlap region of caltable with caltable2
                   Default Value: 
                   Allowed Values:
                                intersect
                                

                poln: Polarizations to plot: "" = all, or "RR","RL","LR","LL","XX","XY","YX","YY","RR,LL","XX,YY"
                   Default Value: 

                showatm: Compute and overlay the atmospheric transmission curve
                   Default Value: False

                pwv: Define the pwv to use for the showatm option: "auto" or value in mm
                   Default Value: auto

                gs: For buildpdf=T, full path for ghostscript command (in case it is not found)
                   Default Value: gs

                convert: For buildpdf=T, full path for the ImageMagick convert command (in case it is not found)
                   Default Value: convert

                chanrange: Set xrange ("5~100") over which to autoscale y-axis for xaxis="freq"
                   Default Value: 

                solutionTimeThresholdSeconds: Consider 2 solutions simultaneous if within this interval in seconds
                   Default Value: 30.0

                debug: Print verbose messages for debugging purposes
                   Default Value: False

                phase: The y-axis limits to use for phase plots when yaxis="both"
                   Default Value: 

                vis: name of the ms for this table, in case it does not match the string in the caltable
                   Default Value: 

                showtsky: Compute and overlay the sky temperature curve instead of transmission
                   Default Value: False

                showfdm: when showing TDM spws, draw the locations of the corresponding FDM spws
                   Default Value: False

                showatmfield: for overlay="time", use first observation of this fieldID or name
                   Default Value: 

                lo1: specify the LO1 setting (in GHz) for the observation ('' = automatic)
                   Default Value: 

                showimage: also show the atmospheric curve for the image sideband (in black)
                   Default Value: False

                showatmpoints: Draw atmospheric curve with points instead of a line
                   Default Value: False

                parentms: if showimage=T, name of the parent ms (only needed if the ms has been previously split)
                   Default Value: 

                pdftk: For buildpdf=T, full path for pdftk command (in case it is not found)
                   Default Value: pdftk

                channeldiff: Set to a value > 0 (sigma) to plot derivatives of the solutions
                   Default Value: False

                edge: The number of edge channels to ignore in finding outliers (for channeldiff>0)
                   Default Value: 8

                resample: The channel expansion factor to use when computing MAD of derivative (for channeldiff>0)
                   Default Value: 1

                platformingThreshold: if platformingSigma=0, then declare platforming if the amplitude derivative exceeds this percentage of the median
                   Default Value: 10.0

                platformingSigma: declare platforming if the amplitude derivative exceeds this many times the MAD
                   Default Value: 10.0

                basebands: A baseband number or list of baseband numbers for which to display solutions.  Default = all.
                   Default Value: 

                showBasebandNumber: Put the baseband converter number (BBC_NO) in the title of each plot
                   Default Value: False

                scans: A scan or list of scans for which to display solutions.  Default = all. Does not work with overlay="time".
                   Default Value: 

                figfileSequential: naming scheme for pngs: False: name by spw/antenna (default), True: figfile.000.png, figfile.001.png, etc.
                   Default Value: False

                chanrangeSetXrange: If True, then chanrange also sets the xrange to display
                   Default Value: False

        Returns: variant

        Example :


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
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'plotbandpass'
        self.__globals__['taskname'] = 'plotbandpass'
        ###
        self.__globals__['update_params'](func=self.__globals__['taskname'],printtext=False,ipython_globals=self.__globals__)
        ###
        ###
        #Handle globals or user over-ride of arguments
        #
        if type(self.__call__.func_defaults) is NoneType:
            function_signature_defaults={}
        else:
            function_signature_defaults=dict(zip(self.__call__.func_code.co_varnames[1:],self.__call__.func_defaults))
        useLocalDefaults = False

        for item in function_signature_defaults.iteritems():
                key,val = item
                keyVal = eval(key)
                if (keyVal == None):
                        #user hasn't set it - use global/default
                        pass
                else:
                        #user has set it - use over-ride
                        if (key != 'self') :
                           useLocalDefaults = True

        myparams = {}
        if useLocalDefaults :
           for item in function_signature_defaults.iteritems():
               key,val = item
               keyVal = eval(key)
               exec('myparams[key] = keyVal')
               self.parameters[key] = keyVal
               if (keyVal == None):
                   exec('myparams[key] = '+ key + ' = self.itsdefault(key)')
                   keyVal = eval(key)
                   if(type(keyVal) == dict) :
                      if len(keyVal) > 0 :
                         exec('myparams[key] = ' + key + ' = keyVal[len(keyVal)-1][\'value\']')
                      else :
                         exec('myparams[key] = ' + key + ' = {}')

        else :
            print ''

            myparams['caltable'] = caltable = self.parameters['caltable']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['yaxis'] = yaxis = self.parameters['yaxis']
            myparams['xaxis'] = xaxis = self.parameters['xaxis']
            myparams['figfile'] = figfile = self.parameters['figfile']
            myparams['plotrange'] = plotrange = self.parameters['plotrange']
            myparams['caltable2'] = caltable2 = self.parameters['caltable2']
            myparams['overlay'] = overlay = self.parameters['overlay']
            myparams['showflagged'] = showflagged = self.parameters['showflagged']
            myparams['timeranges'] = timeranges = self.parameters['timeranges']
            myparams['buildpdf'] = buildpdf = self.parameters['buildpdf']
            myparams['caltable3'] = caltable3 = self.parameters['caltable3']
            myparams['markersize'] = markersize = self.parameters['markersize']
            myparams['density'] = density = self.parameters['density']
            myparams['interactive'] = interactive = self.parameters['interactive']
            myparams['showpoints'] = showpoints = self.parameters['showpoints']
            myparams['showlines'] = showlines = self.parameters['showlines']
            myparams['subplot'] = subplot = self.parameters['subplot']
            myparams['zoom'] = zoom = self.parameters['zoom']
            myparams['poln'] = poln = self.parameters['poln']
            myparams['showatm'] = showatm = self.parameters['showatm']
            myparams['pwv'] = pwv = self.parameters['pwv']
            myparams['gs'] = gs = self.parameters['gs']
            myparams['convert'] = convert = self.parameters['convert']
            myparams['chanrange'] = chanrange = self.parameters['chanrange']
            myparams['solutionTimeThresholdSeconds'] = solutionTimeThresholdSeconds = self.parameters['solutionTimeThresholdSeconds']
            myparams['debug'] = debug = self.parameters['debug']
            myparams['phase'] = phase = self.parameters['phase']
            myparams['vis'] = vis = self.parameters['vis']
            myparams['showtsky'] = showtsky = self.parameters['showtsky']
            myparams['showfdm'] = showfdm = self.parameters['showfdm']
            myparams['showatmfield'] = showatmfield = self.parameters['showatmfield']
            myparams['lo1'] = lo1 = self.parameters['lo1']
            myparams['showimage'] = showimage = self.parameters['showimage']
            myparams['showatmpoints'] = showatmpoints = self.parameters['showatmpoints']
            myparams['parentms'] = parentms = self.parameters['parentms']
            myparams['pdftk'] = pdftk = self.parameters['pdftk']
            myparams['channeldiff'] = channeldiff = self.parameters['channeldiff']
            myparams['edge'] = edge = self.parameters['edge']
            myparams['resample'] = resample = self.parameters['resample']
            myparams['platformingThreshold'] = platformingThreshold = self.parameters['platformingThreshold']
            myparams['platformingSigma'] = platformingSigma = self.parameters['platformingSigma']
            myparams['basebands'] = basebands = self.parameters['basebands']
            myparams['showBasebandNumber'] = showBasebandNumber = self.parameters['showBasebandNumber']
            myparams['scans'] = scans = self.parameters['scans']
            myparams['figfileSequential'] = figfileSequential = self.parameters['figfileSequential']
            myparams['chanrangeSetXrange'] = chanrangeSetXrange = self.parameters['chanrangeSetXrange']

        if type(plotrange)==float: plotrange=[plotrange]

        result = None

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
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'plotbandpass.xml')

        casalog.origin('plotbandpass')
        try :
          #if not trec.has_key('plotbandpass') or not casac.casac.utils().verify(mytmp, trec['plotbandpass']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['plotbandpass'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('plotbandpass', 'plotbandpass.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'plotbandpass'
          spaces = ' '*(18-len(tname))
          casalog.post('\n##########################################'+
                       '\n##### Begin Task: ' + tname + spaces + ' #####')
          # Don't do telemetry from MPI servers (CASR-329)
          if do_full_logging and casa['state']['telemetry-enabled']:
              #casalog.poststat('Begin Task: ' + tname)
              task_starttime = str(datetime.datetime.now())
          if type(self.__call__.func_defaults) is NoneType:
              casalog.post(scriptstr[0]+'\n', 'INFO')
          else:
              casalog.post(scriptstr[1][1:]+'\n', 'INFO')

          # Effective call to the task as defined in gcwrap/python/scripts/task_*
          result = plotbandpass(caltable, antenna, field, spw, yaxis, xaxis, figfile, plotrange, caltable2, overlay, showflagged, timeranges, buildpdf, caltable3, markersize, density, interactive, showpoints, showlines, subplot, zoom, poln, showatm, pwv, gs, convert, chanrange, solutionTimeThresholdSeconds, debug, phase, vis, showtsky, showfdm, showatmfield, lo1, showimage, showatmpoints, parentms, pdftk, channeldiff, edge, resample, platformingThreshold, platformingSigma, basebands, showBasebandNumber, scans, figfileSequential, chanrangeSetXrange)

          if do_full_logging and casa['state']['telemetry-enabled']:
              task_endtime = str(datetime.datetime.now())
              casalog.poststat( 'Task ' + tname + ' complete. Start time: ' + task_starttime + ' End time: ' + task_endtime )
          casalog.post('##### End Task: ' + tname + '  ' + spaces + ' #####'+
                       '\n##########################################')

        except Exception, instance:
          if(self.__globals__.has_key('__rethrow_casa_exceptions') and self.__globals__['__rethrow_casa_exceptions']) :
             raise
          else :
             #print '**** Error **** ',instance
             tname = 'plotbandpass'
             casalog.post('An error occurred running task '+tname+'.', 'ERROR')
             pass
        casalog.origin('')

        return result
#
#
#
#    def paramgui(self, useGlobals=True, ipython_globals=None):
#        """
#        Opens a parameter GUI for this task.  If useGlobals is true, then any relevant global parameter settings are used.
#        """
#        import paramgui
#        if not hasattr(self, "__globals__") or self.__globals__ == None :
#           self.__globals__=stack_frame_find( )
#
#        if useGlobals:
#            if ipython_globals == None:
#                myf=self.__globals__
#            else:
#                myf=ipython_globals
#
#            paramgui.setGlobals(myf)
#        else:
#            paramgui.setGlobals({})
#
#        paramgui.runTask('plotbandpass', myf['_ip'])
#        paramgui.setGlobals({})
#
#
#
#
    def defaults(self, param=None, ipython_globals=None, paramvalue=None, subparam=None):
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        if ipython_globals == None:
            myf=self.__globals__
        else:
            myf=ipython_globals

        a = odict()
        a['caltable']  = ''
        a['antenna']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['yaxis']  = 'amp'
        a['xaxis']  = 'chan'
        a['figfile']  = ''
        a['plotrange']  = [0,0,0,0]
        a['caltable2']  = ''
        a['overlay']  = ''
        a['showflagged']  = False
        a['timeranges']  = ''
        a['markersize']  = 3
        a['interactive']  = True
        a['showpoints']  = 'auto'
        a['showlines']  = 'auto'
        a['subplot']  = '22'
        a['poln']  = ''
        a['showatm']  = False
        a['solutionTimeThresholdSeconds']  = 30.0
        a['debug']  = False
        a['vis']  = ''
        a['showtsky']  = False
        a['channeldiff']  = False
        a['basebands']  = ''
        a['showBasebandNumber']  = False
        a['scans']  = ''
        a['figfileSequential']  = False

        a['figfile'] = {
                    0:odict([{'notvalue':''}, {'density':108}, {'buildpdf':False}, {'convert':'convert'}, {'gs':'gs'}, {'pdftk':'pdftk'}])}
        a['showatm'] = {
                    0:odict([{'notvalue':False}, {'pwv':'auto'}, {'showimage':False}, {'parentms':''}, {'lo1':''}, {'showatmpoints':False}])}
        a['showtsky'] = {
                    0:odict([{'notvalue':False}, {'pwv':'auto'}, {'showimage':False}, {'parentms':''}, {'lo1':''}, {'showatmpoints':False}])}
        a['xaxis'] = {
                    0:{'value':'chan'}, 
                    1:odict([{'value':'freq'}, {'chanrange':''}, {'showfdm':False}, {'chanrangeSetXrange':False}])}
        a['yaxis'] = {
                    0:{'value':'amp'}, 
                    1:odict([{'value':'both'}, {'phase':''}])}
        a['overlay'] = {
                    0:{'value':''}, 
                    1:odict([{'value':'time'}, {'showatmfield':''}])}
        a['channeldiff'] = {
                    0:odict([{'notvalue':False}, {'edge':8}, {'resample':1}, {'platformingSigma':5.0}, {'platformingThreshold':10.0}])}
        a['caltable2'] = {
                    0:odict([{'notvalue':''}, {'zoom':''}, {'caltable3':''}])}

### This function sets the default values but also will return the list of
### parameters or the default value of a given parameter
        if(param == None):
                myf['__set_default_parameters'](a)
        elif(param == 'paramkeys'):
                return a.keys()
        else:
            if(paramvalue==None and subparam==None):
               if(a.has_key(param)):
                  return a[param]
               else:
                  return self.itsdefault(param)
            else:
               retval=a[param]
               if(type(a[param])==dict):
                  for k in range(len(a[param])):
                     valornotval='value'
                     if(a[param][k].has_key('notvalue')):
                        valornotval='notvalue'
                     if((a[param][k][valornotval])==paramvalue):
                        retval=a[param][k].copy()
                        retval.pop(valornotval)
                        if(subparam != None):
                           if(retval.has_key(subparam)):
                              retval=retval[subparam]
                           else:
                              retval=self.itsdefault(subparam)
                     else:
                        retval=self.itsdefault(subparam)
               return retval


#
#
    def check_params(self, param=None, value=None, ipython_globals=None):
      if ipython_globals == None:
          myf=self.__globals__
      else:
          myf=ipython_globals
#      print 'param:', param, 'value:', value
      try :
         if str(type(value)) != "<type 'instance'>" :
            value0 = value
            value = myf['cu'].expandparam(param, value)
            matchtype = False
            if(type(value) == numpy.ndarray):
               if(type(value) == type(value0)):
                  myf[param] = value.tolist()
               else:
                  #print 'value:', value, 'value0:', value0
                  #print 'type(value):', type(value), 'type(value0):', type(value0)
                  myf[param] = value0
                  if type(value0) != list :
                     matchtype = True
            else :
               myf[param] = value
            value = myf['cu'].verifyparam({param:value})
            if matchtype:
               value = False
      except Exception, instance:
         #ignore the exception and just return it unchecked
         myf[param] = value
      return value
#
#
    def description(self, key='plotbandpass', subkey=None):
        desc={'plotbandpass': 'Makes detailed plots of Tsys and bandpass solutions.',
               'caltable': 'Input table name, either a bandpass solution or a Tsys solution',
               'antenna': 'A comma-delimited string list of antennas (either names or integer indices) for which to display solutions.  Default = all antennas.',
               'field': 'A comma-delimited string list of fields (either names or integer indices) for which to display solutions.  Default = all fields.',
               'spw': 'A comma-delimited string list of spws for which to display solutions.  Default = all spws.',
               'yaxis': 'The quantity to plot on the y-axis ("amp", "phase", "both", "tsys", append "db" for dB).',
               'xaxis': 'The quantity to plot on the x-axis ("chan" or "freq").',
               'figfile': 'The name of the plot file to produce.',
               'plotrange': 'The axes limits to use [x0,x1,y0,y1].',
               'caltable2': 'A second cal table, of type BPOLY or B, to overlay on a B table',
               'overlay': 'Show multiple solutions in same frame in different colors (time, antenna, spw, baseband, or time,antenna)',
               'showflagged': 'Show the values of the solution, even if flagged',
               'timeranges': 'Show only these timeranges, the first timerange being 0',
               'buildpdf': 'If True, assemble all the pngs into a pdf',
               'caltable3': 'A third cal table, of type BPOLY, to overlay on the first two tables',
               'markersize': 'Size of points',
               'density': 'dpi to use in creating PNGs and PDFs (default=108)',
               'interactive': 'if False, then run to completion automatically without pause',
               'showpoints': 'Draw points for the data (default=F for amp, T for phase)',
               'showlines': 'Draw lines connecting the data (default=T for amp, F for phase)',
               'subplot': '11..81,22,32 or 42 for RowsxColumns (default=22), any 3rd digit is ignored',
               'zoom': '"intersect" will zoom to overlap region of caltable with caltable2',
               'poln': 'Polarizations to plot: "" = all, or "RR","RL","LR","LL","XX","XY","YX","YY","RR,LL","XX,YY"',
               'showatm': 'Compute and overlay the atmospheric transmission curve',
               'pwv': 'Define the pwv to use for the showatm option: "auto" or value in mm',
               'gs': 'For buildpdf=T, full path for ghostscript command (in case it is not found)',
               'convert': 'For buildpdf=T, full path for the ImageMagick convert command (in case it is not found)',
               'chanrange': 'Set xrange ("5~100") over which to autoscale y-axis for xaxis="freq"',
               'solutionTimeThresholdSeconds': 'Consider 2 solutions simultaneous if within this interval in seconds',
               'debug': 'Print verbose messages for debugging purposes',
               'phase': 'The y-axis limits to use for phase plots when yaxis="both"',
               'vis': 'name of the ms for this table, in case it does not match the string in the caltable',
               'showtsky': 'Compute and overlay the sky temperature curve instead of transmission',
               'showfdm': 'when showing TDM spws, draw the locations of the corresponding FDM spws',
               'showatmfield': 'for overlay="time", use first observation of this fieldID or name',
               'lo1': 'specify the LO1 setting (in GHz) for the observation ('' = automatic)',
               'showimage': 'also show the atmospheric curve for the image sideband (in black)',
               'showatmpoints': 'Draw atmospheric curve with points instead of a line',
               'parentms': 'if showimage=T, name of the parent ms (only needed if the ms has been previously split)',
               'pdftk': 'For buildpdf=T, full path for pdftk command (in case it is not found)',
               'channeldiff': 'Set to a value > 0 (sigma) to plot derivatives of the solutions',
               'edge': 'The number of edge channels to ignore in finding outliers (for channeldiff>0)',
               'resample': 'The channel expansion factor to use when computing MAD of derivative (for channeldiff>0)',
               'platformingThreshold': 'if platformingSigma=0, then declare platforming if the amplitude derivative exceeds this percentage of the median',
               'platformingSigma': 'declare platforming if the amplitude derivative exceeds this many times the MAD',
               'basebands': 'A baseband number or list of baseband numbers for which to display solutions.  Default = all.',
               'showBasebandNumber': 'Put the baseband converter number (BBC_NO) in the title of each plot',
               'scans': 'A scan or list of scans for which to display solutions.  Default = all. Does not work with overlay="time".',
               'figfileSequential': 'naming scheme for pngs: False: name by spw/antenna (default), True: figfile.000.png, figfile.001.png, etc.',
               'chanrangeSetXrange': 'If True, then chanrange also sets the xrange to display',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['caltable']  = ''
        a['antenna']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['yaxis']  = 'amp'
        a['xaxis']  = 'chan'
        a['figfile']  = ''
        a['plotrange']  = [0,0,0,0]
        a['caltable2']  = ''
        a['overlay']  = ''
        a['showflagged']  = False
        a['timeranges']  = ''
        a['buildpdf']  = False
        a['caltable3']  = ''
        a['markersize']  = 3
        a['density']  = 108
        a['interactive']  = True
        a['showpoints']  = 'auto'
        a['showlines']  = 'auto'
        a['subplot']  = '22'
        a['zoom']  = ''
        a['poln']  = ''
        a['showatm']  = False
        a['pwv']  = 'auto'
        a['gs']  = 'gs'
        a['convert']  = 'convert'
        a['chanrange']  = ''
        a['solutionTimeThresholdSeconds']  = 30.0
        a['debug']  = False
        a['phase']  = ''
        a['vis']  = ''
        a['showtsky']  = False
        a['showfdm']  = False
        a['showatmfield']  = ''
        a['lo1']  = ''
        a['showimage']  = False
        a['showatmpoints']  = False
        a['parentms']  = ''
        a['pdftk']  = 'pdftk'
        a['channeldiff']  = False
        a['edge']  = 8
        a['resample']  = 1
        a['platformingThreshold']  = 10.0
        a['platformingSigma']  = 10.0
        a['basebands']  = ''
        a['showBasebandNumber']  = False
        a['scans']  = ''
        a['figfileSequential']  = False
        a['chanrangeSetXrange']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['figfile']  != '':
            a['density'] = 108
            a['buildpdf'] = False
            a['convert'] = 'convert'
            a['gs'] = 'gs'
            a['pdftk'] = 'pdftk'

        if self.parameters['showatm']  != False:
            a['pwv'] = 'auto'
            a['showimage'] = False
            a['parentms'] = ''
            a['lo1'] = ''
            a['showatmpoints'] = False

        if self.parameters['showtsky']  != False:
            a['pwv'] = 'auto'
            a['showimage'] = False
            a['parentms'] = ''
            a['lo1'] = ''
            a['showatmpoints'] = False

        if self.parameters['xaxis']  == 'freq':
            a['chanrange'] = ''
            a['showfdm'] = False
            a['chanrangeSetXrange'] = False

        if self.parameters['yaxis']  == 'both':
            a['phase'] = ''

        if self.parameters['overlay']  == 'time':
            a['showatmfield'] = ''

        if self.parameters['channeldiff']  != False:
            a['edge'] = 8
            a['resample'] = 1
            a['platformingSigma'] = 5.0
            a['platformingThreshold'] = 10.0

        if self.parameters['caltable2']  != '':
            a['zoom'] = ''
            a['caltable3'] = ''

        if a.has_key(paramname) :
              return a[paramname]
plotbandpass_cli = plotbandpass_cli_()
