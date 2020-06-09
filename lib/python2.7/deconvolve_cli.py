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
from task_deconvolve import deconvolve
class deconvolve_cli_:
    __name__ = "deconvolve"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (deconvolve_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'model':None, 'psf':None, 'alg':None, 'niter':None, 'gain':None, 'threshold':None, 'mask':None, 'scales':None, 'sigma':None, 'targetflux':None, 'prior':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, model=None, psf=None, alg=None, niter=None, gain=None, threshold=None, mask=None, scales=None, sigma=None, targetflux=None, prior=None, ):

        """Image based deconvolver

        Detailed Description:

Several algorithms are available to deconvolve an image with a
known psf (dirty beam), or a Gaussian beam.  The algorithms
available are clark and hogbom clean, a multiscale clean and a
mem clean.

NOTE: Recommend using taskname=clean if psf is a dirty beam


  
        Arguments :
                imagename: Input image to deconvolve
                   Default Value: 

                model: Output image containing deconvolved point model
                   Default Value: 

                psf: Point spread function (dirty beam)
                   Default Value: 

                alg: Algorithm to use (clark, hogbom, multiscale, mem) 
                   Default Value: clark
                   Allowed Values:
                                clark
                                hogbom
                                mem
                                multiscale

                niter: number of iteration in deconvolution process
                   Default Value: 10
                   Allowed Values:
                                0

                gain: CLEAN gain parameter
                   Default Value: 0.1
                   Allowed Values:
                                 0
                                1.0

                threshold: level below which sources will not be deconvolved
                   Default Value: 0.0

                mask: image mask to limit region of deconvolution
                   Default Value: 

                scales: scale sizes (pixels) to deconvolve
                   Default Value: 
            0310
        

                sigma: mem parameter: Expected noise in image
                   Default Value: 0.0

                targetflux: mem parameter: Estimated total flux in image
                   Default Value: 1.0

                prior: mem parameter: prior image for mem search
                   Default Value: 

        Returns: void

        Example :


        Several algorithms are available to deconvolve an image with a
        known psf (dirty beam), or a Gaussian beam.  The algorithms
        available are clark and hogbom clean, a multiscale clean and a
        mem clean.  For more deconvolution control, use clean.

        Keyword arguments:
        imagename -- Name of input image to be deconvolved
        model     -- Name of output image containing the clean components
        psf       -- Name of psf image (dirty beam) to use
                     example: psf='casaxmlf.image' .
                     If the psf has 3 parameter, then a Gaussian
                     psf is assumed with the values representing
                     the major , minor and position angle  values
                     e.g  psf=['3arcsec', '2.5arcsec', '10deg']
        alg       -- algorithm to use: default = 'clark'
                       options: clark, hogbom, multiscale or mem.
        niter     -- Maximum number of iterations
        gain      -- CLEAN gain parameter; fraction to remove from peak
        threshold -- Halt deconvolution if the maximum residual image is
                     below this threshold.
                     default = '0.0Jy'
        mask      -- mask image (same shape as image and psf) to limit region
                     where deconvoltion is to occur

        ------parameters useful for multiscale only
        scales     -- in pixel numbers; the size of component to deconvolve.
                      default value [0,3,10]
                      recommended sizes are 0 (point), 3 (points per clean beam), and
                      10 (about a factor of three lower resolution)
        ------parameters useful for mem only
        sigma      -- Estimated noise for image
        targetflux -- Target total flux in image 
        prior      -- Prior image to guide mem


  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'deconvolve'
        self.__globals__['taskname'] = 'deconvolve'
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
            myparams['model'] = model = self.parameters['model']
            myparams['psf'] = psf = self.parameters['psf']
            myparams['alg'] = alg = self.parameters['alg']
            myparams['niter'] = niter = self.parameters['niter']
            myparams['gain'] = gain = self.parameters['gain']
            myparams['threshold'] = threshold = self.parameters['threshold']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['scales'] = scales = self.parameters['scales']
            myparams['sigma'] = sigma = self.parameters['sigma']
            myparams['targetflux'] = targetflux = self.parameters['targetflux']
            myparams['prior'] = prior = self.parameters['prior']

        if type(psf)==str: psf=[psf]
        if type(scales)==int: scales=[scales]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['model'] = model
        mytmp['psf'] = psf
        mytmp['alg'] = alg
        mytmp['niter'] = niter
        mytmp['gain'] = gain
        if type(threshold) == str :
           mytmp['threshold'] = casac.casac.qa.quantity(threshold)
        else :
           mytmp['threshold'] = threshold
        mytmp['mask'] = mask
        mytmp['scales'] = scales
        if type(sigma) == str :
           mytmp['sigma'] = casac.casac.qa.quantity(sigma)
        else :
           mytmp['sigma'] = sigma
        if type(targetflux) == str :
           mytmp['targetflux'] = casac.casac.qa.quantity(targetflux)
        else :
           mytmp['targetflux'] = targetflux
        mytmp['prior'] = prior
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'deconvolve.xml')

        casalog.origin('deconvolve')
        try :
          #if not trec.has_key('deconvolve') or not casac.casac.utils().verify(mytmp, trec['deconvolve']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['deconvolve'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('deconvolve', 'deconvolve.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'deconvolve'
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
          result = deconvolve(imagename, model, psf, alg, niter, gain, threshold, mask, scales, sigma, targetflux, prior)

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
             tname = 'deconvolve'
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
#        paramgui.runTask('deconvolve', myf['_ip'])
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
        a['model']  = ''
        a['psf']  = ['']
        a['alg']  = 'clark'
        a['niter']  = 10
        a['gain']  = 0.1
        a['threshold']  = '0.0mJy'
        a['mask']  = ''

        a['alg'] = {
                    0:{'value':'clark'}, 
                    1:{'value':'hogbom'}, 
                    2:odict([{'value':'multiscale'}, {'scales':[0, 3, 10]}]), 
                    3:odict([{'value':'mem'}, {'sigma':1.0}, {'targetflux':1.0}, {'prior':''}])}

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
    def description(self, key='deconvolve', subkey=None):
        desc={'deconvolve': 'Image based deconvolver',
               'imagename': 'Input image to deconvolve',
               'model': 'Output image containing deconvolved point model',
               'psf': 'Point spread function (dirty beam)',
               'alg': 'Algorithm to use (clark, hogbom, multiscale, mem) ',
               'niter': 'number of iteration in deconvolution process',
               'gain': 'CLEAN gain parameter',
               'threshold': 'level below which sources will not be deconvolved',
               'mask': 'image mask to limit region of deconvolution',
               'scales': 'scale sizes (pixels) to deconvolve',
               'sigma': 'mem parameter: Expected noise in image',
               'targetflux': 'mem parameter: Estimated total flux in image',
               'prior': 'mem parameter: prior image for mem search',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['model']  = ''
        a['psf']  = ['']
        a['alg']  = 'clark'
        a['niter']  = 10
        a['gain']  = 0.1
        a['threshold']  = '0.0mJy'
        a['mask']  = ''
        a['scales']  = [0, 3, 10]
        a['sigma']  = '0.0mJy'
        a['targetflux']  = '1.0Jy'
        a['prior']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['alg']  == 'multiscale':
            a['scales'] = [0, 3, 10]

        if self.parameters['alg']  == 'mem':
            a['sigma'] = 1.0
            a['targetflux'] = 1.0
            a['prior'] = ''

        if a.has_key(paramname) :
              return a[paramname]
deconvolve_cli = deconvolve_cli_()
