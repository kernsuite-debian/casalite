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
from task_plotcal import plotcal
class plotcal_cli_:
    __name__ = "plotcal"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (plotcal_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'caltable':None, 'xaxis':None, 'yaxis':None, 'poln':None, 'field':None, 'antenna':None, 'spw':None, 'timerange':None, 'subplot':None, 'overplot':None, 'clearpanel':None, 'iteration':None, 'plotrange':None, 'showflags':None, 'plotsymbol':None, 'plotcolor':None, 'markersize':None, 'fontsize':None, 'showgui':None, 'figfile':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, caltable=None, xaxis=None, yaxis=None, poln=None, field=None, antenna=None, spw=None, timerange=None, subplot=None, overplot=None, clearpanel=None, iteration=None, plotrange=None, showflags=None, plotsymbol=None, plotcolor=None, markersize=None, fontsize=None, showgui=None, figfile=None, ):

        """An all-purpose plotter for calibration results 

        Detailed Description:

An all-purpose plotter for calibration results.  The values for all
calibration solutions (G, T, GSPLINE, B, BPOLY, D) can be displayed
for a variety of polarization combinations and calibrations.  The
solutions may be iterated through antennas/spw/fields during one execution.

    
        Arguments :
                caltable: Name of input calibration table
                   Default Value: 

                xaxis: Value to plot along x axis (time,chan,freq, antenna,antenna1,antenna2,scan, amp,phase,real,imag,snr, tsys,delay,rate,spgain)
                   Default Value: 
                   Allowed Values:
                                
                                time
                                chan
                                freq
                                antenna
                                antenna1
                                antenna2
                                scan
                                amp
                                phase
                                real
                                imag
                                snr
                                tsys
                                tec
                                delay
                                rate
                                spgain

                yaxis: Value to plot along y axis (amp,phase,real,imag,snr, antenna,antenna1,antenna2,scan, tsys,delay,rate,spgain,tec)
                   Default Value: 
                   Allowed Values:
                                
                                amp
                                phase
                                real
                                imag
                                snr
                                antenna
                                antenna1
                                antenna2
                                scan
                                tsys
                                tec
                                delay
                                rate
                                spgain

                poln: Antenna polarization to plot (RL,R,L,XY,X,Y,/)
                   Default Value: 
                   Allowed Values:
                                
                                RL
                                R
                                L
                                X
                                Y
                                /

                field: field names or index of calibrators: \'\'==>all
                   Default Value: 

                antenna: antenna/baselines: \'\'==>all, antenna = \'3,VA04\'
                   Default Value: 

                spw: spectral window:channels: \'\'==>all, spw=\'1:5~57\'
                   Default Value: 

                timerange: time range: \'\'==>all
                   Default Value: 

                subplot: Panel number on display screen (yxn)
                   Default Value: 111

                overplot: Overplot solutions on existing display
                   Default Value: False

                clearpanel: Specify if old plots are cleared or not (ignore)
                   Default Value: Auto
                   Allowed Values:
                                Current
                                None
                                Auto
                                All

                iteration: Iterate plots on antenna,time,spw,field
                   Default Value: 

                plotrange: plot axes ranges: [xmin,xmax,ymin,ymax]
                   Default Value: 
            

                showflags: If true, show flagged solutions
                   Default Value: False

                plotsymbol: pylab plot symbol
                   Default Value: o

                plotcolor: initial plotting color
                   Default Value: blue

                markersize: Size of plotted marks
                   Default Value: 5.0

                fontsize: Font size for labels
                   Default Value: 10.0

                showgui: Show plot on gui
                   Default Value: True

                figfile: \'\'= no plot hardcopy, otherwise supply name
                   Default Value: 

        Returns: void

        Example :

    
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
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'plotcal'
        self.__globals__['taskname'] = 'plotcal'
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
            myparams['xaxis'] = xaxis = self.parameters['xaxis']
            myparams['yaxis'] = yaxis = self.parameters['yaxis']
            myparams['poln'] = poln = self.parameters['poln']
            myparams['field'] = field = self.parameters['field']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['subplot'] = subplot = self.parameters['subplot']
            myparams['overplot'] = overplot = self.parameters['overplot']
            myparams['clearpanel'] = clearpanel = self.parameters['clearpanel']
            myparams['iteration'] = iteration = self.parameters['iteration']
            myparams['plotrange'] = plotrange = self.parameters['plotrange']
            myparams['showflags'] = showflags = self.parameters['showflags']
            myparams['plotsymbol'] = plotsymbol = self.parameters['plotsymbol']
            myparams['plotcolor'] = plotcolor = self.parameters['plotcolor']
            myparams['markersize'] = markersize = self.parameters['markersize']
            myparams['fontsize'] = fontsize = self.parameters['fontsize']
            myparams['showgui'] = showgui = self.parameters['showgui']
            myparams['figfile'] = figfile = self.parameters['figfile']

        if type(plotrange)==float: plotrange=[plotrange]

        result = None

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
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'plotcal.xml')

        casalog.origin('plotcal')
        try :
          #if not trec.has_key('plotcal') or not casac.casac.utils().verify(mytmp, trec['plotcal']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['plotcal'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('plotcal', 'plotcal.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'plotcal'
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
          result = plotcal(caltable, xaxis, yaxis, poln, field, antenna, spw, timerange, subplot, overplot, clearpanel, iteration, plotrange, showflags, plotsymbol, plotcolor, markersize, fontsize, showgui, figfile)

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
             tname = 'plotcal'
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
#        paramgui.runTask('plotcal', myf['_ip'])
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
        a['xaxis']  = ''
        a['yaxis']  = ''
        a['poln']  = ''
        a['field']  = ''
        a['antenna']  = ''
        a['spw']  = ''
        a['timerange']  = ''
        a['subplot']  = 111
        a['overplot']  = False
        a['clearpanel']  = 'Auto'
        a['iteration']  = ''
        a['plotrange']  = [
            ]
        a['showflags']  = False
        a['plotsymbol']  = 'o'
        a['plotcolor']  = 'blue'
        a['markersize']  = 5.0
        a['fontsize']  = 10.0
        a['showgui']  = True
        a['figfile']  = ''


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
    def description(self, key='plotcal', subkey=None):
        desc={'plotcal': 'An all-purpose plotter for calibration results ',
               'caltable': 'Name of input calibration table',
               'xaxis': 'Value to plot along x axis (time,chan,freq, antenna,antenna1,antenna2,scan, amp,phase,real,imag,snr, tsys,delay,rate,spgain)',
               'yaxis': 'Value to plot along y axis (amp,phase,real,imag,snr, antenna,antenna1,antenna2,scan, tsys,delay,rate,spgain,tec)',
               'poln': 'Antenna polarization to plot (RL,R,L,XY,X,Y,/)',
               'field': 'field names or index of calibrators: \'\'==>all',
               'antenna': 'antenna/baselines: \'\'==>all, antenna = \'3,VA04\'',
               'spw': 'spectral window:channels: \'\'==>all, spw=\'1:5~57\'',
               'timerange': 'time range: \'\'==>all',
               'subplot': 'Panel number on display screen (yxn)',
               'overplot': 'Overplot solutions on existing display',
               'clearpanel': 'Specify if old plots are cleared or not (ignore)',
               'iteration': 'Iterate plots on antenna,time,spw,field',
               'plotrange': 'plot axes ranges: [xmin,xmax,ymin,ymax]',
               'showflags': 'If true, show flagged solutions',
               'plotsymbol': 'pylab plot symbol',
               'plotcolor': 'initial plotting color',
               'markersize': 'Size of plotted marks',
               'fontsize': 'Font size for labels',
               'showgui': 'Show plot on gui',
               'figfile': '\'\'= no plot hardcopy, otherwise supply name',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['caltable']  = ''
        a['xaxis']  = ''
        a['yaxis']  = ''
        a['poln']  = ''
        a['field']  = ''
        a['antenna']  = ''
        a['spw']  = ''
        a['timerange']  = ''
        a['subplot']  = 111
        a['overplot']  = False
        a['clearpanel']  = 'Auto'
        a['iteration']  = ''
        a['plotrange']  = [
            ]
        a['showflags']  = False
        a['plotsymbol']  = 'o'
        a['plotcolor']  = 'blue'
        a['markersize']  = 5.0
        a['fontsize']  = 10.0
        a['showgui']  = True
        a['figfile']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
plotcal_cli = plotcal_cli_()
