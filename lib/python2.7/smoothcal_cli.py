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
from task_smoothcal import smoothcal
class smoothcal_cli_:
    __name__ = "smoothcal"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (smoothcal_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'tablein':None, 'caltable':None, 'field':None, 'smoothtype':None, 'smoothtime':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, tablein=None, caltable=None, field=None, smoothtype=None, smoothtime=None, ):

        """Smooth calibration solution(s) derived from one or more sources:

        Detailed Description:

        A G- or T-type gain calibration can be smoothed.  Amplitude and
        phase are currently smoothed with the same time.  Calibration values
        will be smoothed over all fields.
        
        Arguments :
                vis: Name of input visibility file (MS)
                   Default Value: 

                tablein: Input calibration table
                   Default Value: 

                caltable: Output calibration table (overwrite tablein if unspecified)
                   Default Value: 

                field: Field name list
                   Default Value: 

                smoothtype: Smoothing filter to use
                   Default Value: median
                   Allowed Values:
                                median
                                mean

                smoothtime: Smoothing time (sec)
                   Default Value: 60.0

        Returns: void

        Example :



        A G- or T-type gain calibration can be smoothed.  The amplitude and
        phase smoothing times are currently the same.  Calibration values
        will be smoothed for only the specified fields.  Smoothing is
        performed independently per field, per spw, and per antenna.

        Keyword arguments:
        vis -- Name of input visibility file
                default: none; example: vis='ngc5921.ms'
        tablein -- Input calibration table (G or T)
                default: none; example: tablein='ngc5921.gcal'
        caltable -- Output calibration table (smoothed)
                default: ''  (will overwrite tablein); 
                example: caltable='ngc5921_smooth.gcal'
        field -- subset of fields to select and smooth
                default: '' means all; example: field='0319_415_1,3C286'
        smoothtype -- The smoothing filter to be used for both amp and phase
                default: 'median'; example: smoothtype='mean'
                Options: 'median','mean'
        smoothtime -- Smoothing filter time (sec)
                default: 300.0; example: smoothtime=60.
 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'smoothcal'
        self.__globals__['taskname'] = 'smoothcal'
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
            myparams['tablein'] = tablein = self.parameters['tablein']
            myparams['caltable'] = caltable = self.parameters['caltable']
            myparams['field'] = field = self.parameters['field']
            myparams['smoothtype'] = smoothtype = self.parameters['smoothtype']
            myparams['smoothtime'] = smoothtime = self.parameters['smoothtime']

        if type(field)==str: field=[field]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['tablein'] = tablein
        mytmp['caltable'] = caltable
        mytmp['field'] = field
        mytmp['smoothtype'] = smoothtype
        mytmp['smoothtime'] = smoothtime
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'smoothcal.xml')

        casalog.origin('smoothcal')
        try :
          #if not trec.has_key('smoothcal') or not casac.casac.utils().verify(mytmp, trec['smoothcal']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['smoothcal'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('smoothcal', 'smoothcal.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'smoothcal'
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
          result = smoothcal(vis, tablein, caltable, field, smoothtype, smoothtime)

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
             tname = 'smoothcal'
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
#        paramgui.runTask('smoothcal', myf['_ip'])
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
        a['tablein']  = ''
        a['caltable']  = ''
        a['field']  = ['']
        a['smoothtype']  = 'median'
        a['smoothtime']  = 60.0


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
    def description(self, key='smoothcal', subkey=None):
        desc={'smoothcal': 'Smooth calibration solution(s) derived from one or more sources:',
               'vis': 'Name of input visibility file (MS)',
               'tablein': 'Input calibration table',
               'caltable': 'Output calibration table (overwrite tablein if unspecified)',
               'field': 'Field name list',
               'smoothtype': 'Smoothing filter to use',
               'smoothtime': 'Smoothing time (sec)',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['tablein']  = ''
        a['caltable']  = ''
        a['field']  = ['']
        a['smoothtype']  = 'median'
        a['smoothtime']  = 60.0

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
smoothcal_cli = smoothcal_cli_()
