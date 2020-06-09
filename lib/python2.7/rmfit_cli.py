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
from task_rmfit import rmfit
class rmfit_cli_:
    __name__ = "rmfit"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (rmfit_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'rm':None, 'rmerr':None, 'pa0':None, 'pa0err':None, 'nturns':None, 'chisq':None, 'sigma':None, 'rmfg':None, 'rmmax':None, 'maxpaerr':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, rm=None, rmerr=None, pa0=None, pa0err=None, nturns=None, chisq=None, sigma=None, rmfg=None, rmmax=None, maxpaerr=None, ):

        """Calculate rotation measure.
        Arguments :
                imagename: Name(s) of the input image(s). Must be specified.
                   Default Value:  

                rm: Output rotation measure image name. If not specified, no image is written.
                   Default Value: 

                rmerr: Output rotation measure error image name. If not specified, no image is written.
                   Default Value: 

                pa0: Output position angle (degrees) at zero wavelength image name. If not specified, no image is written.
                   Default Value: 

                pa0err: Output position angle (degrees) at zero wavelength error image name. If not specified, no image is written.
                   Default Value: 

                nturns: Output number of turns image name. If not specified, no image is written.
                   Default Value: 

                chisq: Output reduced chi squared image name. If not specified, no image is written.
                   Default Value: 

                sigma: Estimate of the thermal noise.  A value less than 0 means auto estimate.
                   Default Value: -1

                rmfg: Foreground rotation measure in rad/m/m to subtract.
                   Default Value: 0.0

                rmmax: Maximum rotation measure in rad/m/m for which to solve. IMPORTANT TO SPECIFY.
                   Default Value: 0.0

                maxpaerr: Maximum input position angle error in degrees to allow in solution determination.
                   Default Value: 1e30

        Returns: bool

        Example :

PARAMETER SUMMARY
imagename        Name(s) of the input image(s).
rm               Output rotation measure image name. If not specified, no image is written.
rmerr            Output rotation measure error image name. If not specified, no image is written.
pa0              Output position angle (degrees) at zero wavelength image name. If not specified, no image is written.
pa0err           Output position angle (degrees) at zero wavelength error image name. If not specified, no image is written.
nturns           Output number of turns image name. If not specified, no image is written.
chisq            Output reduced chi squared image name. If not specified, no image is written.
sigma            Estimate of the thermal noise.  A value less than 0 means auto estimate.
rmfg             Foreground rotation measure in rad/m/m to subtract.
rmmax            Maximum rotation measure in rad/m/m for which to solve. IMPORTANT TO SPECIFY.

This task generates the rotation measure image from stokes Q and U  measurements at several
different frequencies.  You are required to specify the name of at least one image with a polarization
axis containing stokes Q and U planes and with a frequency axis containing more than two pixels. The
frequencies do not have to be equally spaced (ie the frequency coordinate can be a tabular coordinate).
It will work out the position angle images for you. You may also specify multiple image names, in which
case these images will first be concatenated along the spectral axis using ia.imageconcat(). The requirments
are that for all images, the axis order must be the same and the number of pixels along each axis must
be identical, except for the spectral axis which may differ in length between images. The spectral axis need
not be contiguous from one image to another.

See also the fourierrotationmeasure 
function for a new Fourier-based approach.

Rotation measure algorithms that work robustly are few.  The main
problem is in trying to account for the $n- \pi$ ambiguity (see Leahy et
al, Astronomy \& Astrophysics, 156, 234 or Killeen et al;
http://www.atnf.csiro.au/\verb+~+nkilleen/rm.ps). 

The algorithm that this task uses is that of Leahy et al. in see
Appendix A.1.  But as in all these algorithms, the basic process is that
for each spatial pixel, the position angle vs frequency data is fit to
determine the rotation measure and the position angle at zero wavelength
(and associated errors).   An image containing the number of $n- \pi$ turns
that were added to the data at each spatial pixel and for which the best fit
was found can be written. The reduced chi-squared image for the fits can
also be written.

Note that no assessment of curvature (i.e. deviation
from the simple linear position angle - $\lambda^2$ functional form)
is made.  

Any combination of output images can be written.

The parameter sigma gives the thermal noise in Stokes Q and U.
By default it is determined automatically using the image data.  But if it
proves to be inaccurate (maybe not many signal-free pixels), it may be
specified. This is used for calculating the error in the position angles (via 
propagation of Gaussian errors).

The argument maxpaerr specifies the maximum allowable error in
the position angle that is acceptable.  The default is an infinite
value.  From the standard propagation of errors, the error in the
linearly polarized position angle is determined from the Stokes Q and
U images (at each directional pixel for each frequency). If the position angle
error for any pixel exceeds the specified value, the position angle at that pixel
is omitted from the fit. The process generates an error for the
fit and this is used to compute the errors in the output
images.  

Note that maxpaerr is not used to mask pixels in the output images.

The argument rmfg is used to specify a foreground RM value.  For
example, you may know the mean RM in some direction out of the Galaxy,
then including this can improve the algorithm by reducing ambiguity.

The parameter rmmax specifies the maximum absolute RM value that
should be solved for.  This quite an important parameter.  If you leave
it at the default, zero, no ambiguity handling will be
used.  So some apriori information should be supplied; this
is the basic problem with rotation measure algorithms.

EXAMPLES

# Calculate the rotation measure for a single polarization image
rmfit(imagename="mypol.im", rm="myrm.im", rmmax=50.0)

# calculate the rotation measure using a set of polarization images from
# different spectral windows or bands.

rmfit(imagename=["pol1.im", "pol2.im", "pol3.im", rm="myrm2.im", rmmax=50.0)


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'rmfit'
        self.__globals__['taskname'] = 'rmfit'
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
            myparams['rm'] = rm = self.parameters['rm']
            myparams['rmerr'] = rmerr = self.parameters['rmerr']
            myparams['pa0'] = pa0 = self.parameters['pa0']
            myparams['pa0err'] = pa0err = self.parameters['pa0err']
            myparams['nturns'] = nturns = self.parameters['nturns']
            myparams['chisq'] = chisq = self.parameters['chisq']
            myparams['sigma'] = sigma = self.parameters['sigma']
            myparams['rmfg'] = rmfg = self.parameters['rmfg']
            myparams['rmmax'] = rmmax = self.parameters['rmmax']
            myparams['maxpaerr'] = maxpaerr = self.parameters['maxpaerr']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['rm'] = rm
        mytmp['rmerr'] = rmerr
        mytmp['pa0'] = pa0
        mytmp['pa0err'] = pa0err
        mytmp['nturns'] = nturns
        mytmp['chisq'] = chisq
        mytmp['sigma'] = sigma
        mytmp['rmfg'] = rmfg
        mytmp['rmmax'] = rmmax
        mytmp['maxpaerr'] = maxpaerr
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'rmfit.xml')

        casalog.origin('rmfit')
        try :
          #if not trec.has_key('rmfit') or not casac.casac.utils().verify(mytmp, trec['rmfit']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['rmfit'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('rmfit', 'rmfit.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'rmfit'
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
          result = rmfit(imagename, rm, rmerr, pa0, pa0err, nturns, chisq, sigma, rmfg, rmmax, maxpaerr)

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
             tname = 'rmfit'
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
#        paramgui.runTask('rmfit', myf['_ip'])
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
        a['imagename']  = '', 
        a['rm']  = ''
        a['rmerr']  = ''
        a['pa0']  = ''
        a['pa0err']  = ''
        a['nturns']  = ''
        a['chisq']  = ''
        a['sigma']  = -1
        a['rmfg']  = 0.0
        a['rmmax']  = 0.0
        a['maxpaerr']  = 1e30


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
    def description(self, key='rmfit', subkey=None):
        desc={'rmfit': 'Calculate rotation measure.',
               'imagename': 'Name(s) of the input image(s). Must be specified.',
               'rm': 'Output rotation measure image name. If not specified, no image is written.',
               'rmerr': 'Output rotation measure error image name. If not specified, no image is written.',
               'pa0': 'Output position angle (degrees) at zero wavelength image name. If not specified, no image is written.',
               'pa0err': 'Output position angle (degrees) at zero wavelength error image name. If not specified, no image is written.',
               'nturns': 'Output number of turns image name. If not specified, no image is written.',
               'chisq': 'Output reduced chi squared image name. If not specified, no image is written.',
               'sigma': 'Estimate of the thermal noise.  A value less than 0 means auto estimate.',
               'rmfg': 'Foreground rotation measure in rad/m/m to subtract.',
               'rmmax': 'Maximum rotation measure in rad/m/m for which to solve. IMPORTANT TO SPECIFY.',
               'maxpaerr': 'Maximum input position angle error in degrees to allow in solution determination.',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = '', 
        a['rm']  = ''
        a['rmerr']  = ''
        a['pa0']  = ''
        a['pa0err']  = ''
        a['nturns']  = ''
        a['chisq']  = ''
        a['sigma']  = -1
        a['rmfg']  = 0.0
        a['rmmax']  = 0.0
        a['maxpaerr']  = 1e30

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
rmfit_cli = rmfit_cli_()
