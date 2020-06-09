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
from task_plotants import plotants
class plotants_cli_:
    __name__ = "plotants"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (plotants_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'figfile':None, 'antindex':None, 'logpos':None, 'exclude':None, 'checkbaselines':None, 'title':None, 'showgui':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, figfile=None, antindex=None, logpos=None, exclude=None, checkbaselines=None, title=None, showgui=None, ):

        """Plot the antenna distribution in the local reference frame:

        Detailed Description:

       The location of the antennas in the MS will be plotted with
       X-toward local east; Y-toward local north.
     
        Arguments :
                vis: Name of input visibility file (MS)
                   Default Value: 

                figfile: Save the plotted figure to this file
                   Default Value: 

                antindex: Label antennas with name and antenna ID
                   Default Value: False

                logpos: Whether to plot logarithmic positions
                   Default Value: False

                exclude: Antenna name/id selection to exclude from plot
                   Default Value: 

                checkbaselines: Whether to check baselines in the main table.
                   Default Value: False

                title: Title for the plot
                   Default Value: 

                showgui: Show plot on gui.
                   Default Value: True

        Returns: void

        Example :

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
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'plotants'
        self.__globals__['taskname'] = 'plotants'
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
            myparams['figfile'] = figfile = self.parameters['figfile']
            myparams['antindex'] = antindex = self.parameters['antindex']
            myparams['logpos'] = logpos = self.parameters['logpos']
            myparams['exclude'] = exclude = self.parameters['exclude']
            myparams['checkbaselines'] = checkbaselines = self.parameters['checkbaselines']
            myparams['title'] = title = self.parameters['title']
            myparams['showgui'] = showgui = self.parameters['showgui']


        result = None

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
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'plotants.xml')

        casalog.origin('plotants')
        try :
          #if not trec.has_key('plotants') or not casac.casac.utils().verify(mytmp, trec['plotants']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['plotants'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('plotants', 'plotants.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'plotants'
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
          result = plotants(vis, figfile, antindex, logpos, exclude, checkbaselines, title, showgui)

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
             tname = 'plotants'
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
#        paramgui.runTask('plotants', myf['_ip'])
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
        a['figfile']  = ''
        a['antindex']  = False
        a['logpos']  = False
        a['exclude']  = ''
        a['checkbaselines']  = False
        a['title']  = ''
        a['showgui']  = True


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
    def description(self, key='plotants', subkey=None):
        desc={'plotants': 'Plot the antenna distribution in the local reference frame:',
               'vis': 'Name of input visibility file (MS)',
               'figfile': 'Save the plotted figure to this file',
               'antindex': 'Label antennas with name and antenna ID',
               'logpos': 'Whether to plot logarithmic positions',
               'exclude': 'Antenna name/id selection to exclude from plot',
               'checkbaselines': 'Whether to check baselines in the main table.',
               'title': 'Title for the plot',
               'showgui': 'Show plot on gui.',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['figfile']  = ''
        a['antindex']  = False
        a['logpos']  = False
        a['exclude']  = ''
        a['checkbaselines']  = False
        a['title']  = ''
        a['showgui']  = True

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
plotants_cli = plotants_cli_()
