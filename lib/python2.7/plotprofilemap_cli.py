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
from task_plotprofilemap import plotprofilemap
class plotprofilemap_cli_:
    __name__ = "plotprofilemap"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (plotprofilemap_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'figfile':None, 'overwrite':None, 'transparent':None, 'pol':None, 'spectralaxis':None, 'restfreq':None, 'plotrange':None, 'title':None, 'linecolor':None, 'linestyle':None, 'linewidth':None, 'separatepanel':None, 'plotmasked':None, 'maskedcolor':None, 'showaxislabel':None, 'showtick':None, 'showticklabel':None, 'figsize':None, 'numpanels':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, figfile=None, overwrite=None, transparent=None, pol=None, spectralaxis=None, restfreq=None, plotrange=None, title=None, linecolor=None, linestyle=None, linewidth=None, separatepanel=None, plotmasked=None, maskedcolor=None, showaxislabel=None, showtick=None, showticklabel=None, figsize=None, numpanels=None, ):

        """Makes profile map.

        Detailed Description:

  The plotprofilemap makes spectral profile map from specified image. 
  The task accepts both CASA image and FITS cube as an input.
  
        Arguments :
                imagename: Input image name (CASA image or FITS)
                   Default Value: 

                figfile: Output figure name
                   Default Value: 

                overwrite: Overwrite existing figfile
                   Default Value: False

                transparent: Output transparent figure
                   Default Value: False

                pol: Polarization component to be plotted
                   Default Value: 0

                spectralaxis: Type of spectral axis
                   Default Value: 
                   Allowed Values:
                                
                                frequency
                                channel
                                velocity

                restfreq: Rest frequency
                   Default Value: 

                plotrange: Spectral axis range to plot
                   Default Value: 

                title: Title of the plot
                   Default Value: 

                linecolor: Line color
                   Default Value: b

                linestyle: Line style
                   Default Value: -

                linewidth: Line width in points
                   Default Value: 0.2

                separatepanel: Separate plots
                   Default Value: True

                plotmasked: Masked data handling
                   Default Value: empty
                   Allowed Values:
                                empty
                                text
                                zero
                                none
                                plot

                maskedcolor: Line color for masked data
                   Default Value: gray

                showaxislabel: Show axis labels on the bottom left panel
                   Default Value: False

                showtick: Show axis ticks
                   Default Value: False

                showticklabel: Show axis tick labels on the bottom left panel
                   Default Value: False

                figsize: Size of the figure
                   Default Value: 

                numpanels: Number of panels
                   Default Value: 

        Returns: variant

        Example :


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
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'plotprofilemap'
        self.__globals__['taskname'] = 'plotprofilemap'
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

            myparams['imagename'] = imagename = self.parameters['imagename']
            myparams['figfile'] = figfile = self.parameters['figfile']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['transparent'] = transparent = self.parameters['transparent']
            myparams['pol'] = pol = self.parameters['pol']
            myparams['spectralaxis'] = spectralaxis = self.parameters['spectralaxis']
            myparams['restfreq'] = restfreq = self.parameters['restfreq']
            myparams['plotrange'] = plotrange = self.parameters['plotrange']
            myparams['title'] = title = self.parameters['title']
            myparams['linecolor'] = linecolor = self.parameters['linecolor']
            myparams['linestyle'] = linestyle = self.parameters['linestyle']
            myparams['linewidth'] = linewidth = self.parameters['linewidth']
            myparams['separatepanel'] = separatepanel = self.parameters['separatepanel']
            myparams['plotmasked'] = plotmasked = self.parameters['plotmasked']
            myparams['maskedcolor'] = maskedcolor = self.parameters['maskedcolor']
            myparams['showaxislabel'] = showaxislabel = self.parameters['showaxislabel']
            myparams['showtick'] = showtick = self.parameters['showtick']
            myparams['showticklabel'] = showticklabel = self.parameters['showticklabel']
            myparams['figsize'] = figsize = self.parameters['figsize']
            myparams['numpanels'] = numpanels = self.parameters['numpanels']


        result = None

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
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'plotprofilemap.xml')

        casalog.origin('plotprofilemap')
        try :
          #if not trec.has_key('plotprofilemap') or not casac.casac.utils().verify(mytmp, trec['plotprofilemap']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['plotprofilemap'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('plotprofilemap', 'plotprofilemap.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'plotprofilemap'
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
          result = plotprofilemap(imagename, figfile, overwrite, transparent, pol, spectralaxis, restfreq, plotrange, title, linecolor, linestyle, linewidth, separatepanel, plotmasked, maskedcolor, showaxislabel, showtick, showticklabel, figsize, numpanels)

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
             tname = 'plotprofilemap'
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
#        paramgui.runTask('plotprofilemap', myf['_ip'])
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
        a['imagename']  = ''
        a['figfile']  = ''
        a['pol']  = 0
        a['spectralaxis']  = ''
        a['plotrange']  = ''
        a['title']  = ''
        a['linecolor']  = 'b'
        a['linestyle']  = '-'
        a['linewidth']  = 0.2
        a['separatepanel']  = True
        a['plotmasked']  = 'empty'
        a['showaxislabel']  = False
        a['showtick']  = False
        a['figsize']  = ''
        a['numpanels']  = ''

        a['figfile'] = {
                    0:odict([{'notvalue':''}, {'overwrite':False}, {'transparent':False}])}
        a['spectralaxis'] = {
                    0:{'value':''}, 
                    1:odict([{'value':'velocity'}, {'restfreq':''}])}
        a['plotmasked'] = {
                    0:{'value':'empty'}, 
                    1:odict([{'value':'plot'}, {'maskedcolor':'gray'}]), 
                    2:odict([{'value':'zero'}, {'maskedcolor':'gray'}])}
        a['showtick'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'showticklabel':False}])}

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
    def description(self, key='plotprofilemap', subkey=None):
        desc={'plotprofilemap': 'Makes profile map.',
               'imagename': 'Input image name (CASA image or FITS)',
               'figfile': 'Output figure name',
               'overwrite': 'Overwrite existing figfile',
               'transparent': 'Output transparent figure',
               'pol': 'Polarization component to be plotted',
               'spectralaxis': 'Type of spectral axis',
               'restfreq': 'Rest frequency',
               'plotrange': 'Spectral axis range to plot',
               'title': 'Title of the plot',
               'linecolor': 'Line color',
               'linestyle': 'Line style',
               'linewidth': 'Line width in points',
               'separatepanel': 'Separate plots',
               'plotmasked': 'Masked data handling',
               'maskedcolor': 'Line color for masked data',
               'showaxislabel': 'Show axis labels on the bottom left panel',
               'showtick': 'Show axis ticks',
               'showticklabel': 'Show axis tick labels on the bottom left panel',
               'figsize': 'Size of the figure',
               'numpanels': 'Number of panels',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['figfile']  = ''
        a['overwrite']  = False
        a['transparent']  = False
        a['pol']  = 0
        a['spectralaxis']  = ''
        a['restfreq']  = ''
        a['plotrange']  = ''
        a['title']  = ''
        a['linecolor']  = 'b'
        a['linestyle']  = '-'
        a['linewidth']  = 0.2
        a['separatepanel']  = True
        a['plotmasked']  = 'empty'
        a['maskedcolor']  = 'gray'
        a['showaxislabel']  = False
        a['showtick']  = False
        a['showticklabel']  = False
        a['figsize']  = ''
        a['numpanels']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['figfile']  != '':
            a['overwrite'] = False
            a['transparent'] = False

        if self.parameters['spectralaxis']  == 'velocity':
            a['restfreq'] = ''

        if self.parameters['plotmasked']  == 'plot':
            a['maskedcolor'] = 'gray'

        if self.parameters['plotmasked']  == 'zero':
            a['maskedcolor'] = 'gray'

        if self.parameters['showtick']  == True:
            a['showticklabel'] = False

        if a.has_key(paramname) :
              return a[paramname]
plotprofilemap_cli = plotprofilemap_cli_()
