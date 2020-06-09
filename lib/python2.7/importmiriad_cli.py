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
from task_importmiriad import importmiriad
class importmiriad_cli_:
    __name__ = "importmiriad"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (importmiriad_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'mirfile':None, 'vis':None, 'tsys':None, 'spw':None, 'vel':None, 'linecal':None, 'wide':None, 'debug':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, mirfile=None, vis=None, tsys=None, spw=None, vel=None, linecal=None, wide=None, debug=None, ):

        """Convert a Miriad visibility file into a CASA MeasurementSet

        Detailed Description:

Convert a Miriad visibility file into a CASA MeasurementSet with
optional selection of spectral windows and weighting scheme
        
        Arguments :
                mirfile: Name of input Miriad visibility file
                     Default: none

                        Example: mirfile='mydata.uv'

                   Default Value: 

                vis: Name of output MeasurementSet
                     Default: none

                        Example: vis='mydata.ms'

                   Default Value: 

                tsys: Use the Tsys to set the visibility weights
                     Default: False
                     Options: False|True

                   Default Value: False

                spw: Select spectral window/channels
                     Default: '' (all spectral windows and channels)
           
                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                        spw='<2';  spectral windows less than 2 (i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
                        3 - chans 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
                        through 6 in each.
                        spw = '*:3~64'  channels 3 through 64 for all sp id's
                        spw = ' :3~64' will NOT work.

                   Default Value: -1

                vel: Select velocity reference
                     Default: telescope dependent, ATCA -> TOPO, CARMA
                     -> LSRK
                     Options: TOPO|LSRK|LSRD

                        Example: vel='LSRK'

                   Default Value: 

                linecal: (CARMA) Apply line calibration
                     Default: False
                     Options: False|True
 
                     Only useful for CARMA data

                   Default Value: False

                wide: (CARMA) Select wide window averages

                     Select which of the wide-band channels should be loaded 
                     Only useful for CARMA data

                   Default Value: 

                debug: Display increasingly verbose debug messages
                     Default: 0

                        Example: debug=1

                   Default Value: 0

        Returns: void

        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTMIRIAD IN CASA DOCS:
https://casa.nrao.edu/casadocs/
 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'importmiriad'
        self.__globals__['taskname'] = 'importmiriad'
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

            myparams['mirfile'] = mirfile = self.parameters['mirfile']
            myparams['vis'] = vis = self.parameters['vis']
            myparams['tsys'] = tsys = self.parameters['tsys']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['vel'] = vel = self.parameters['vel']
            myparams['linecal'] = linecal = self.parameters['linecal']
            myparams['wide'] = wide = self.parameters['wide']
            myparams['debug'] = debug = self.parameters['debug']

        if type(spw)==int: spw=[spw]
        if type(wide)==int: wide=[wide]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['mirfile'] = mirfile
        mytmp['vis'] = vis
        mytmp['tsys'] = tsys
        mytmp['spw'] = spw
        mytmp['vel'] = vel
        mytmp['linecal'] = linecal
        mytmp['wide'] = wide
        mytmp['debug'] = debug
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'importmiriad.xml')

        casalog.origin('importmiriad')
        try :
          #if not trec.has_key('importmiriad') or not casac.casac.utils().verify(mytmp, trec['importmiriad']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['importmiriad'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('importmiriad', 'importmiriad.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'importmiriad'
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
          result = importmiriad(mirfile, vis, tsys, spw, vel, linecal, wide, debug)

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
             tname = 'importmiriad'
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
#        paramgui.runTask('importmiriad', myf['_ip'])
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
        a['mirfile']  = ''
        a['vis']  = ''
        a['tsys']  = False
        a['spw']  = [-1]
        a['vel']  = ''
        a['linecal']  = False
        a['wide']  = []
        a['debug']  = 0


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
    def description(self, key='importmiriad', subkey=None):
        desc={'importmiriad': 'Convert a Miriad visibility file into a CASA MeasurementSet',
               'mirfile': 'Name of input Miriad visibility file',
               'vis': 'Name of output MeasurementSet',
               'tsys': 'Use the Tsys to set the visibility weights',
               'spw': 'Select spectral window/channels',
               'vel': 'Select velocity reference (TOPO,LSRK,LSRD)',
               'linecal': '(CARMA) Apply line calibration',
               'wide': '(CARMA) Select wide window averages',
               'debug': 'Display increasingly verbose debug messages',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['mirfile']  = ''
        a['vis']  = ''
        a['tsys']  = False
        a['spw']  = [-1]
        a['vel']  = ''
        a['linecal']  = False
        a['wide']  = []
        a['debug']  = 0

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
importmiriad_cli = importmiriad_cli_()
