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
from task_msview import msview
class msview_cli_:
    __name__ = "msview"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (msview_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'infile':None, 'displaytype':None, 'channel':None, 'zoom':None, 'outfile':None, 'outscale':None, 'outdpi':None, 'outformat':None, 'outlandscape':None, 'gui':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, infile=None, displaytype=None, channel=None, zoom=None, outfile=None, outscale=None, outdpi=None, outformat=None, outlandscape=None, gui=None, ):

        """View a visibility data set

        Detailed Description:

        The msview task will display measurements in raster form.
        Many display and editing options are available.

        Executing the msview task will bring up a display panel
        window, which can be resized.  If no data file was specified,
        a Load Data window will also appear. Click on the desired measurement
        set,and the rendered data should appear on the display panel.

        A Data Display Options window will also appear.  It has drop-down
        subsections for related options, most of which are self-explanatory.

        The state of the msview task -- loaded data and related display
        options -- can be saved in a 'restore' file for later use.
        You can provide the restore filename on the command line or
        select it from the Load Data window.

        See the cookbook for more details on using the msview task.

    
        Arguments :
                infile:  (Optional)  Name of file to visualize.
                   Default Value: 

                displaytype:  (Optional)  Type of visual rendering (raster, contour, vector or marker).  lel  if an lel expression is given for infile  (advanced).
                   Default Value: raster

                channel:  (Optional)  access a specific channel in the image cube
                   Default Value: 0

                zoom:  (Optional)  zoom in/out by increments
                   Default Value: 1

                outfile:  (Optional)  name of the output file to generate
                   Default Value: 

                outscale:  (Optional)  amount to scale output bitmap formats (non-PS, non-PDF)
                   Default Value: 1.0

                outdpi:  (Optional)  output DPI for PS/PDF
                   Default Value: 300

                outformat:  (Optional)  format of the output e.g. jpg or pdf (this is overridden by the output files extension
                   Default Value: jpg

                outlandscape:  (Optional)  should the output mode be landscape (PS or PDF)
                   Default Value: False

                gui:  (Optional)  Display the panel in a GUI.
                   Default Value: True

        Returns: void

        Example :


        examples of usage:

        msview
        msview "mymeasurementset.ms"
        msview "myrestorefile.rstr"
        
        Keyword arguments:
        infile -- Name of file to visualize
                default: ''
                example: infile='my.ms'
                If no infile is specified the Load Data window
                will appear for selecting data.
        displaytype -- (optional): method of rendering data
                visually (raster, contour, vector or marker).  
                You can also set this parameter to 'lel' and
                provide an lel expression for infile (advanced).
                default: 'raster'

        Note: there is no longer a filetype parameter; typing of
        data files is now done automatically.
                example:  msview infile='my.ms'
                obsolete: msview infile='my.ms', filetype='ms'

    
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'msview'
        self.__globals__['taskname'] = 'msview'
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

            myparams['infile'] = infile = self.parameters['infile']
            myparams['displaytype'] = displaytype = self.parameters['displaytype']
            myparams['channel'] = channel = self.parameters['channel']
            myparams['zoom'] = zoom = self.parameters['zoom']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['outscale'] = outscale = self.parameters['outscale']
            myparams['outdpi'] = outdpi = self.parameters['outdpi']
            myparams['outformat'] = outformat = self.parameters['outformat']
            myparams['outlandscape'] = outlandscape = self.parameters['outlandscape']
            myparams['gui'] = gui = self.parameters['gui']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['displaytype'] = displaytype
        mytmp['channel'] = channel
        mytmp['zoom'] = zoom
        mytmp['outfile'] = outfile
        mytmp['outscale'] = outscale
        mytmp['outdpi'] = outdpi
        mytmp['outformat'] = outformat
        mytmp['outlandscape'] = outlandscape
        mytmp['gui'] = gui
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'msview.xml')

        casalog.origin('msview')
        try :
          #if not trec.has_key('msview') or not casac.casac.utils().verify(mytmp, trec['msview']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['msview'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('msview', 'msview.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'msview'
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
          result = msview(infile, displaytype, channel, zoom, outfile, outscale, outdpi, outformat, outlandscape, gui)

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
             tname = 'msview'
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
#        paramgui.runTask('msview', myf['_ip'])
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
        a['infile']  = ''
        a['displaytype']  = 'raster'
        a['channel']  = 0
        a['zoom']  = 1
        a['outfile']  = ''
        a['outscale']  = 1.0
        a['outdpi']  = 300
        a['outformat']  = 'jpg'
        a['outlandscape']  = False
        a['gui']  = True


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
    def description(self, key='msview', subkey=None):
        desc={'msview': 'View a visibility data set',
               'infile': ' (Optional)  Name of file to visualize.',
               'displaytype': ' (Optional)  Type of visual rendering (raster, contour, vector or marker).  lel  if an lel expression is given for infile  (advanced).',
               'channel': ' (Optional)  access a specific channel in the image cube',
               'zoom': ' (Optional)  zoom in/out by increments',
               'outfile': ' (Optional)  name of the output file to generate',
               'outscale': ' (Optional)  amount to scale output bitmap formats (non-PS, non-PDF)',
               'outdpi': ' (Optional)  output DPI for PS/PDF',
               'outformat': ' (Optional)  format of the output e.g. jpg or pdf (this is overridden by the output files extension',
               'outlandscape': ' (Optional)  should the output mode be landscape (PS or PDF)',
               'gui': ' (Optional)  Display the panel in a GUI.',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['infile']  = ''
        a['displaytype']  = 'raster'
        a['channel']  = 0
        a['zoom']  = 1
        a['outfile']  = ''
        a['outscale']  = 1.0
        a['outdpi']  = 300
        a['outformat']  = 'jpg'
        a['outlandscape']  = False
        a['gui']  = True

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
msview_cli = msview_cli_()
