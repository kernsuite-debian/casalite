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
from task_feather import feather
class feather_cli_:
    __name__ = "feather"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (feather_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'highres':None, 'lowres':None, 'sdfactor':None, 'effdishdiam':None, 'lowpassfiltersd':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, highres=None, lowres=None, sdfactor=None, effdishdiam=None, lowpassfiltersd=None, ):

        """Combine two images using their Fourier transforms

        Detailed Description:

This task can be used as one method of combining single-dish and
interferometric images after they have been separately made.

The algorithm converts each image to the gridded visibility plane,
combines them, and reconverts them into an combined image.  Each image
must include a well-defined beam shape (clean beam) in order for
feathering to work well.  The two images must have the same flux
density normalization scale.

        Arguments :
                imagename: Name of output feathered image
                          Default: none

                             Example: imagename='orion_combined.im'

                   Default Value: 

                highres: Name of high resolution (interferometer) image
                          Default: none

                             Example: imagename='orion_vla.im'

                   Default Value: 

                lowres: Name of low resolution (single dish) image
                          Default: none

                             Example: imagename='orion_gbt.im'

                   Default Value: 

                sdfactor: Value by which to scale the Single Dish image.
                          Default: 1.0

                          Basically modifying the flux scale of the SD image

                   Default Value: 1.0

                effdishdiam: New effective SingleDish diameter to use in m 
                          Default: -1.0 (leave as is)

                          Obviously one can only reduce the dish
                          effective dish diameter in feathering.

                   Default Value: -1.0

                lowpassfiltersd: Filter out the high spatial frequencies of the SD image
                          Default: False

                          If True the high spatial frequency in the SD
                          image is rejected.

                          Any data outside the maximum uv distance
                          that the SD has illuminated  is filtered
                          out.

                   Default Value: False


        Example :


For more information, see the task pages of feather in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'feather'
        self.__globals__['taskname'] = 'feather'
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
            myparams['highres'] = highres = self.parameters['highres']
            myparams['lowres'] = lowres = self.parameters['lowres']
            myparams['sdfactor'] = sdfactor = self.parameters['sdfactor']
            myparams['effdishdiam'] = effdishdiam = self.parameters['effdishdiam']
            myparams['lowpassfiltersd'] = lowpassfiltersd = self.parameters['lowpassfiltersd']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['highres'] = highres
        mytmp['lowres'] = lowres
        mytmp['sdfactor'] = sdfactor
        mytmp['effdishdiam'] = effdishdiam
        mytmp['lowpassfiltersd'] = lowpassfiltersd
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'feather.xml')

        casalog.origin('feather')
        try :
          #if not trec.has_key('feather') or not casac.casac.utils().verify(mytmp, trec['feather']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['feather'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('feather', 'feather.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'feather'
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
          result = feather(imagename, highres, lowres, sdfactor, effdishdiam, lowpassfiltersd)

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
             tname = 'feather'
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
#        paramgui.runTask('feather', myf['_ip'])
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
        a['highres']  = ''
        a['lowres']  = ''
        a['sdfactor']  = 1.0
        a['effdishdiam']  = -1.0
        a['lowpassfiltersd']  = False


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
    def description(self, key='feather', subkey=None):
        desc={'feather': 'Combine two images using their Fourier transforms',
               'imagename': 'Name of output feathered image',
               'highres': 'Name of high resolution (interferometer) image',
               'lowres': 'Name of low resolution (single dish) image',
               'sdfactor': 'Scale factor to apply to Single Dish image',
               'effdishdiam': 'New effective SingleDish diameter to use in m',
               'lowpassfiltersd': 'Filter out the high spatial frequencies of the SD image',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['highres']  = ''
        a['lowres']  = ''
        a['sdfactor']  = 1.0
        a['effdishdiam']  = -1.0
        a['lowpassfiltersd']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
feather_cli = feather_cli_()
