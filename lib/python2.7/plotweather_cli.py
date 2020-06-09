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
from task_plotweather import plotweather
class plotweather_cli_:
    __name__ = "plotweather"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (plotweather_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'seasonal_weight':None, 'doPlot':None, 'plotName':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, seasonal_weight=None, doPlot=None, plotName=None, ):

        """Plot elements of the weather table; estimate opacity.
        Arguments :
                vis: MS name
                   Default Value: 

                seasonal_weight: weight of the seasonal model
                   Default Value: 0.5

                doPlot: set this to True to create a plot
                   Default Value: True

                plotName: (Optional) the name of the plot file
                   Default Value: 


        Example :

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
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'plotweather'
        self.__globals__['taskname'] = 'plotweather'
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

            myparams['vis'] = vis = self.parameters['vis']
            myparams['seasonal_weight'] = seasonal_weight = self.parameters['seasonal_weight']
            myparams['doPlot'] = doPlot = self.parameters['doPlot']
            myparams['plotName'] = plotName = self.parameters['plotName']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['seasonal_weight'] = seasonal_weight
        mytmp['doPlot'] = doPlot
        mytmp['plotName'] = plotName
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'plotweather.xml')

        casalog.origin('plotweather')
        try :
          #if not trec.has_key('plotweather') or not casac.casac.utils().verify(mytmp, trec['plotweather']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['plotweather'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('plotweather', 'plotweather.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'plotweather'
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
          result = plotweather(vis, seasonal_weight, doPlot, plotName)

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
             tname = 'plotweather'
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
#        paramgui.runTask('plotweather', myf['_ip'])
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
        a['vis']  = ''
        a['seasonal_weight']  = 0.5
        a['doPlot']  = True
        a['plotName']  = ''


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
    def description(self, key='plotweather', subkey=None):
        desc={'plotweather': 'Plot elements of the weather table; estimate opacity.',
               'vis': 'MS name',
               'seasonal_weight': 'weight of the seasonal model',
               'doPlot': 'set this to True to create a plot',
               'plotName': '(Optional) the name of the plot file',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['seasonal_weight']  = 0.5
        a['doPlot']  = True
        a['plotName']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
plotweather_cli = plotweather_cli_()