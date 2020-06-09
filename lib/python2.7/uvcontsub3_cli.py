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
from task_uvcontsub3 import uvcontsub3
class uvcontsub3_cli_:
    __name__ = "uvcontsub3"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (uvcontsub3_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'fitspw':None, 'combine':None, 'fitorder':None, 'field':None, 'spw':None, 'scan':None, 'intent':None, 'correlation':None, 'observation':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, fitspw=None, combine=None, fitorder=None, field=None, spw=None, scan=None, intent=None, correlation=None, observation=None, ):

        """An experimental clone of uvcontsub

        Detailed Description:



        Arguments :
                vis: Name of input MS.  Output goes to vis + ".contsub"
                   Default Value: 

                fitspw: Spectral window:channel selection for fitting the continuum
                   Default Value: 

                combine: Data axes to combine for the continuum estimation (none ('') or spw)
                   Default Value: 

                fitorder: Polynomial order for the fits
                   Default Value: 0

                field: Select field(s) using id(s) or name(s)
                   Default Value: 

                spw: Spectral window selection for output
                   Default Value: 

                scan: Select data by scan numbers
                   Default Value: 

                intent: Select data by scan intents
                   Default Value: 

                correlation: Select correlations
                   Default Value: 

                observation: Select by observation ID(s)
                   Default Value: 


        Example :

  
        uvcontsub3 is an experimental clone of uvcontsub with the goal of taking
        less time and temporary disk space.

        Continuum fitting and subtraction in the uv plane:
        
        This task estimates the continuum emission by fitting polynomials to
        the real and imaginary parts of the spectral windows and channels
        selected by fitspw.  This fit represents a model of the continuum in 
        all channels.
        
        The fitted continuum spectrum is subtracted from all channels 
        selected in spw, and the result (presumably only line emission)
        is stored in a new MS (vis + ".contsub").
        It will read from the CORRECTED_DATA column of vis if it is present,
        or DATA if it is not.  Whichever column is read is presumed to have
        already been calibrated.

        Keyword arguments:
        vis -- Name of input visibility file
                default: none; example: vis='ngc5921.ms'

        fitspw -- Selection of spectral windows and channels to use in the
                  fit for the continuum, using general spw:chan syntax.
                  See the note under combine.
                default: '' (all)
                example: fitspw='0:5~30;40~55'

        combine -- Let the continuum estimation span multiple spectral windows.
                   default = '' (Make separate estimates for each spw.)
                   combine = 'spw': Necessary when one or more of the spws are
                                    completely blanketed by lines, so the estimate
                                    must be made in different spws.

        fitorder -- Polynomial order for the fits of the continuum w.r.t.
                    frequency.  fitorders > 1 are strongly discouraged
                    because high order polynomials have more flexibility, may
                    absorb line emission, and tend go wild at the edges of
                    fitspw, which is not what you want.

                default: 0 (constant); example: fitorder=1

        field -- Field selection for continuum estimation and subtraction.
                 The estimation and subtraction is done for each selected field
                 in turn.  (Run listobs to get lists of the ID and names.)
               default: ''=all fields.  If the field string is a non-negative
                        integer, it is assumed to be a field index
                        otherwise, it is assumed to be a field name
               field='0~2'; field ids 0,1,2
               field='0,4,5~7'; field ids 0,4,5,6,7
               field='3C286,3C295'; fields named 3C286 and 3C295
               field = '3,4C*'; field id 3, all names starting with 4C

        spw -- Select spectral windows for the output.
               default: ''=all spectral windows
               N.B. uvcontsub3 does not yet support exclusion by channels for
                    the output.  Meanwhile, use split to further reduce the size
                    of the output MS if desired.
               spw='0~2,4'; spectral windows 0,1,2,4
               spw='<2';  spectral windows less than 2 (i.e. 0,1)

        scan -- Scan number range
            default: ''=all

        intent -- Select by scan intent (state).  Case sensitive.
            default: '' = all
            Examples:
            intent = 'CALIBRATE_ATMOSPHERE_REFERENCE'
            intent = 'calibrate_atmosphere_reference'.upper() # same as above
            # Select states that include one or both of CALIBRATE_WVR.REFERENCE
            # or OBSERVE_TARGET_ON_SOURCE.
            intent = 'CALIBRATE_WVR.REFERENCE, OBSERVE_TARGET_ON_SOURCE'

        correlation -- Select correlations, e.g. 'rr, ll' or ['XY', 'YX'].
                       default '' (all).

        observation -- Select by observation ID(s).
                       default: '' = all


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'uvcontsub3'
        self.__globals__['taskname'] = 'uvcontsub3'
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
            myparams['fitspw'] = fitspw = self.parameters['fitspw']
            myparams['combine'] = combine = self.parameters['combine']
            myparams['fitorder'] = fitorder = self.parameters['fitorder']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['correlation'] = correlation = self.parameters['correlation']
            myparams['observation'] = observation = self.parameters['observation']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['fitspw'] = fitspw
        mytmp['combine'] = combine
        mytmp['fitorder'] = fitorder
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['correlation'] = correlation
        mytmp['observation'] = observation
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'uvcontsub3.xml')

        casalog.origin('uvcontsub3')
        try :
          #if not trec.has_key('uvcontsub3') or not casac.casac.utils().verify(mytmp, trec['uvcontsub3']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['uvcontsub3'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('uvcontsub3', 'uvcontsub3.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'uvcontsub3'
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
          result = uvcontsub3(vis, fitspw, combine, fitorder, field, spw, scan, intent, correlation, observation)

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
             tname = 'uvcontsub3'
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
#        paramgui.runTask('uvcontsub3', myf['_ip'])
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
        a['fitspw']  = ''
        a['combine']  = ''
        a['fitorder']  = 0
        a['field']  = ''
        a['spw']  = ''
        a['scan']  = ''
        a['intent']  = ''
        a['correlation']  = ''
        a['observation']  = ''


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
    def description(self, key='uvcontsub3', subkey=None):
        desc={'uvcontsub3': 'An experimental clone of uvcontsub',
               'vis': 'Name of input MS.  Output goes to vis + ".contsub"',
               'fitspw': 'Spectral window:channel selection for fitting the continuum',
               'combine': 'Data axes to combine for the continuum estimation (none ('') or spw)',
               'fitorder': 'Polynomial order for the fits',
               'field': 'Select field(s) using id(s) or name(s)',
               'spw': 'Spectral window selection for output',
               'scan': 'Select data by scan numbers',
               'intent': 'Select data by scan intents',
               'correlation': 'Select correlations',
               'observation': 'Select by observation ID(s)',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['fitspw']  = ''
        a['combine']  = ''
        a['fitorder']  = 0
        a['field']  = ''
        a['spw']  = ''
        a['scan']  = ''
        a['intent']  = ''
        a['correlation']  = ''
        a['observation']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
uvcontsub3_cli = uvcontsub3_cli_()
