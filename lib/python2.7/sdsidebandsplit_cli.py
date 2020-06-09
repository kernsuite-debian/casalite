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
from task_sdsidebandsplit import sdsidebandsplit
class sdsidebandsplit_cli_:
    __name__ = "sdsidebandsplit"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (sdsidebandsplit_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'outfile':None, 'overwrite':None, 'signalshift':None, 'imageshift':None, 'getbothside':None, 'refchan':None, 'refval':None, 'otherside':None, 'threshold':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, outfile=None, overwrite=None, signalshift=None, imageshift=None, getbothside=None, refchan=None, refval=None, otherside=None, threshold=None, ):

        """[EXPERIMENTAL] invoke sideband separation using FFT

        Detailed Description:
[EXPERIMENTAL] SD sideband separation and supression task:
        Invoke sideband separation / supression using FFT

        Arguments :
                imagename: a list of names of input images. At least two valid images are required for processing
                   Default Value: 

                outfile: Prefix of output image name.
      A suffix, ".signalband" or ".imageband" is added to 
      output image name depending on the side band side being solved.
                   Default Value: 

                overwrite: overwrite option
                   Default Value: False

                signalshift: a list of channel number shifts in signal side band.
      The number of elements must be equal to that of imagename
                   Default Value: 

                imageshift:  a list of channel number shifts in image side band.
      The number of elements must be either zero or equal to that of imagename.
      In case of zero length array, the values are obtained from signalshift
      assuming the shifts are the same magnitude in opposite direction.
                   Default Value: 

                getbothside: sideband separation (True) or supression (False)
                   Default Value: False

                refchan: reference channel of spectral axis in image sideband
                   Default Value: 0.0

                refval: frequency at the reference channel of spectral axis in image sideband (e.g., "100GHz")
                   Default Value: 

                otherside: solve the solution of the other side band side and subtract the solution
                   Default Value: False

                threshold: Rejection limit of solution. The value must be greater than 0.0 and less than 1.0.
                   Default Value: 0.2
                   Allowed Values:
                                0.0
                                1.0

        Returns: void

        Example :

Solve signal sideband

    sdsidebandsplit(imagename=['shift_0ch.image', 'shift_132ch.image', 'shift_neg81ch.image'],
                  outfile='separated.image', signalshift=[0.0, +132.0, -81.0],
                  imageshift=[0.0, -132.0, +81.0])

The output image is 'separated.image.signalband'.

Solve both signal and image sidebands (need to set frequency of image sideband explicitly)

    sdsidebandsplit(imagename=['shift_0ch.image', 'shift_132ch.image', 'shift_neg81ch.image'],
                  outfile='separated.image', signalshift=[0.0, +132.0, -81.0],
                  imageshift=[0.0, -132.0, +81.0],
                  getbothside=True, refchan=0.0, refval='805.8869GHz')

The output images are 'separated.image.signalband' and 'separated.image.imageband'
for signal and image sideband, respectively.

Obtain signal sideband image by solving image sideband

    sdsidebandsplit(imagename=['shift_0ch.image', 'shift_132ch.image', 'shift_neg81ch.image'],
                  outfile='separated.image', signalshift=[0.0, +132.0, -81.0],
                  imageshift=[0.0, -132.0, +81.0], otherside=True)

Solution of image sidband is obtained and subtracted from the original (double sideband) spectra
to derive spectra of signal sideband.

  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'sdsidebandsplit'
        self.__globals__['taskname'] = 'sdsidebandsplit'
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
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['signalshift'] = signalshift = self.parameters['signalshift']
            myparams['imageshift'] = imageshift = self.parameters['imageshift']
            myparams['getbothside'] = getbothside = self.parameters['getbothside']
            myparams['refchan'] = refchan = self.parameters['refchan']
            myparams['refval'] = refval = self.parameters['refval']
            myparams['otherside'] = otherside = self.parameters['otherside']
            myparams['threshold'] = threshold = self.parameters['threshold']

        if type(imagename)==str: imagename=[imagename]
        if type(signalshift)==float: signalshift=[signalshift]
        if type(imageshift)==float: imageshift=[imageshift]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        mytmp['signalshift'] = signalshift
        mytmp['imageshift'] = imageshift
        mytmp['getbothside'] = getbothside
        mytmp['refchan'] = refchan
        mytmp['refval'] = refval
        mytmp['otherside'] = otherside
        mytmp['threshold'] = threshold
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'sdsidebandsplit.xml')

        casalog.origin('sdsidebandsplit')
        try :
          #if not trec.has_key('sdsidebandsplit') or not casac.casac.utils().verify(mytmp, trec['sdsidebandsplit']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['sdsidebandsplit'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('sdsidebandsplit', 'sdsidebandsplit.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'sdsidebandsplit'
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
          result = sdsidebandsplit(imagename, outfile, overwrite, signalshift, imageshift, getbothside, refchan, refval, otherside, threshold)

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
             tname = 'sdsidebandsplit'
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
#        paramgui.runTask('sdsidebandsplit', myf['_ip'])
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
        a['imagename']  = ['']
        a['outfile']  = ''
        a['overwrite']  = False
        a['signalshift']  = []
        a['imageshift']  = []
        a['getbothside']  = False
        a['otherside']  = False
        a['threshold']  = 0.2

        a['getbothside'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'refchan':0.0}, {'refval':''}])}

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
    def description(self, key='sdsidebandsplit', subkey=None):
        desc={'sdsidebandsplit': '[EXPERIMENTAL] invoke sideband separation using FFT',
               'imagename': 'a list of names of input images',
               'outfile': 'Prefix of output image name',
               'overwrite': 'overwrite option',
               'signalshift': 'a list of channel number shifts in signal side band',
               'imageshift': 'a list of channel number shifts in image side band',
               'getbothside': 'sideband separation (True) or supression (False)',
               'refchan': 'reference channel of spectral axis in image sideband',
               'refval': 'frequency at the reference channel of spectral axis in image sideband (e.g., "100GHz")',
               'otherside': 'solve the solution of the other side band side and subtract the solution',
               'threshold': 'Rejection limit of solution',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ['']
        a['outfile']  = ''
        a['overwrite']  = False
        a['signalshift']  = []
        a['imageshift']  = []
        a['getbothside']  = False
        a['refchan']  = 0.0
        a['refval']  = ''
        a['otherside']  = False
        a['threshold']  = 0.2

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['getbothside']  == True:
            a['refchan'] = 0.0
            a['refval'] = ''

        if a.has_key(paramname) :
              return a[paramname]
sdsidebandsplit_cli = sdsidebandsplit_cli_()
