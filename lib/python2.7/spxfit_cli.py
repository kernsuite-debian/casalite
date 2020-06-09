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
from task_spxfit import spxfit
class spxfit_cli_:
    __name__ = "spxfit"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (spxfit_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'box':None, 'region':None, 'chans':None, 'stokes':None, 'axis':None, 'mask':None, 'minpts':None, 'multifit':None, 'spxtype':None, 'spxest':None, 'spxfix':None, 'div':None, 'spxsol':None, 'spxerr':None, 'model':None, 'residual':None, 'wantreturn':None, 'stretch':None, 'logresults':None, 'logfile':None, 'append':None, 'sigma':None, 'outsigma':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, box=None, region=None, chans=None, stokes=None, axis=None, mask=None, minpts=None, multifit=None, spxtype=None, spxest=None, spxfix=None, div=None, spxsol=None, spxerr=None, model=None, residual=None, wantreturn=None, stretch=None, logresults=None, logfile=None, append=None, sigma=None, outsigma=None, ):

        """Fit a 1-dimensional model(s) to an image(s) or region for determination of spectral index.

        Detailed Description:


        Arguments :
                imagename: Name of the input image(s)
                   Default Value: 

                box: Rectangular region to select in direction plane. Default is to use the entire direction plane.
                   Default Value: 

                region: Region selection. Default is to use the full image.
                   Default Value: 

                chans: Channels to use. Default is to use all channels.
                   Default Value: 

                stokes: Stokes planes to use. Default is to use all Stokes planes.
                   Default Value: 

                axis: The profile axis. Default: use the spectral axis if one exists, axis 0 otherwise (<0).
                   Default Value: -1

                mask: Mask to use. Default is none.
                   Default Value: 

                minpts: Minimum number of unmasked points necessary to attempt fit.
                   Default Value: 1

                multifit: If true, fit a profile along the desired axis at each pixel in the specified region. If false, average the non-fit axis pixels and do a single fit to that average profile. Default False.
                   Default Value: False

                spxtype: Type of function to fit. "plp" = power logarithmic polynomial, "ltp" = logarithmic transformed polynomial.
                   Default Value: plp

                spxest: REQUIRED. Initial estimates as array of numerical values for the spectral index function coefficients. eg [1.5, -0.8] if fitting a plp function thought to be close to 1.5*(x/div)**(-0.8) or [0.4055, -0.8] if fitting an lpt function thought to be close to ln(1.5) - 0.8*ln(x/div).
                   Default Value: 

                spxfix: Fix the corresponding spectral index function coefficients during the fit. True means hold fixed.
                   Default Value: 

                div: Divisor (numerical value or quantity) to use in the logarithmic terms of the plp or ltp function. 0 means calculate a useful value on the fly.
                   Default Value: 0

                spxsol: Name of the spectral index function coefficient solution image to write.
                   Default Value: 

                spxerr: Name of the spectral index function coefficient error image to write.
                   Default Value: 

                model: Name of model image. Default: do not write the model image ("").
                   Default Value: 

                residual: Name of residual image. Default: do not write the residual image ("").
                   Default Value: 

                wantreturn: Should a record summarizing the results be returned?
                   Default Value: True

                stretch: Stretch the mask if necessary and possible? 
                   Default Value: False

                logresults: Output results to logger?
                   Default Value: True

                logfile: File in which to log results. Default is not to write a logfile.
                   Default Value: 

                append: Append results to logfile? Logfile must be specified. Default is to append. False means overwrite existing file if it exists.
                   Default Value: True

                sigma: Standard deviation array or image name(s).
                   Default Value: 

                outsigma: Name of output image used for standard deviation. Ignored if sigma is empty.
                   Default Value: 

        Returns: record

        Example :


This task fits a power logarithmic polynomial or a logarithmic tranformed polynomial to one dimensional profiles for determination of spectral indices.

PARAMETER SUMMARY
imagename       Name of the input image(s). More than one image name can be given as an
                array, in which case the images are concatenated along the specified axis
                and the resultant image is what is used by the fitter. In this case,
                all images must have the same dimensions along all axes other than the fit axis.
box             Rectangular region to select in direction plane.
                Default is to use the entire direction plane.
region          Region selection. Default is to use the full image.
chans           Channels to use. Default is to use all channels.
stokes          Stokes planes to use. Default is to use all Stokes planes.
axis            Axis along which to do the fit(s). <0 means use the spectral axis or the
                zeroth axis if a spectral axis is not present.
mask            Mask to use. Default is none.
stretch         Stretch the input mask if necessary and possible? Only used if a mask is specified.

minpts          Minimum number of points necessary to attempt a fit.
multifit        Fit models at each pixel in region (true) or average profiles and fit a single model (false).
spxtype         Type of function to fit. "plp" => power logarithmic polynomial, "ltp" => logarithmic
                transformed polynomial.
spxest          REQUIRED. Initial estimates as array of numerical values for the spectral index
                function coefficients. eg [1.5, -0.8] if fitting a plp function thought to be close to
                1.5*(x/div)**(-0.8), or [0.4055, -0.8] if fitting an lpt function thought to be close to
                ln(1.5) - 0.8*ln(x/div).
spxfix          Fix the corresponding spx function coefficients during the fit. True=>hold fixed
div             Divisor (numerical value or quantity) to use in the logarithmic terms of the plp or ltp
                function. 0 => calculate a useful value on the fly.
spxsol          Name of the function coeffecients solution image to write.
spxerr          Name of the function coeffecients error image to write.
model           Name of model image to write.
residual        Name of residual image to write.
wantreturn      If true, return a record summarizing the fit results, if false, return false.
stretch         Stretch the mask if necessary and possible?
logresults      Output results to logger?
logfile         File in which to log results. Default is not to write a logfile.
append          Append results to logfile? Logfile must be specified. Default is to append. False means overwrite existing file if it exists.
sigma           Standard deviation numerical array, image name (string), or string array of names of images which will be
                concatenated to create the sigma image that is used by the fitter.
outsigma        Name of output image used for standard deviation. Ignored if sigma is empty.

This application performs a non-linear, least squares fits using the Levenberg-Marquardt algorithm of either a power logarithmic polynomial or a
logarithmic tranformed polynomial to pixel values along a specified axis of an image or images. A description of the fitting algorithm may be found
in AIPS++ Note 224 (http://www.astron.nl/casacore/trunk/casacore/doc/notes/224.html) and in Numerical Recipes by W.H. Press et al., Cambridge
University Press. These functions are most often used for fitting the spectral index and higher order terms of a spectrum. A power logarithmic
polynomial (plp) has the form

y = c0*(x/div)**(c1 + c2*ln(x/div) + c3*ln(x/div)**2 + ... + cn*ln(x/div)**(n - 1))

and a logarithmic transformed polynomial (ltp) is simply the result of this equation after taking the natural log of both sides so that it has the form

ln(y) = c0 + c1*ln(x/div) + c2*ln(x/div)**2 +  ... + cn*ln(x/div)**n

Because the logarithm of the ordinate values must be taken before fitting a logarithmic transformed polynomial,
all non-positive pixel values are effectively masked for the purposes of fitting.

The coefficients of the two forms are equal to each other except that c0 in the second equation is equal to
ln(c0) of the first. In the case of fitting a spectral index, which is traditionally represented as alpha, is
equal to c1.

In both cases, div is a numerical value used to scale abscissa values so they are closer to unity when they are sent to the fitter. This generally
improves the probability that the fit will converge. This parameter may be specified via the div parameter. A value of 0
(the default) indicates that the application should determine a reasonable value for div, which is determined via

div = 10**int(log10(sqrt(min(x)*max(x))))

where min(x) and max(x) are the minimum and maximum abscissa values, respectively.

So, for example, if S(nu) is proportional to nu**alpha and you expect alpha to be near -0.8 and the value of S(nu) is 1.5 at
1e9 Hz and your image(s) have spectral units of Hz, you would specify spxest=[1.5, -0.8] and div=1e9 when fitting a plp function,
or spxest=[0.405, -0.8] and div=1e9 if fitting an ltp function close to ln(1.5) - 0.8*ln(x/div).


A CAUTIONARY NOTE
Note that the likelihood of getting a reliable solution increases with the number of good data points as well as the goodness
of the initial estimate. It is possible that the first solution found might not be the best one, and
so, if a solution is found, it is recommended that the fit be repeated using the solution of the previous fit as the
initial estimatE for the new fit. This process should be repeated until the solutions from one fit to the next differ only insignificantly.
The convergent solution is very likely the best solution.

AXIS
The axis parameter indicates on which axis profiles should be fit; a value <0 indicates the spectral axis should be used,
or if one does not exist, that the zeroth axis should be used.

MINIMUM NUMBER OF PIXELS
The minpts parameter indicates the minimum number of unmasked pixels that must be present in order for a fit
to be attempted. When multifit=T, positions with too few good points will be masked in any output images.

ONE FIT OF REGION AVERAGE OR PIXEL BY PIXEL FIT
The multifit parameter indicates if profiles should be fit at each pixel in the selected region (true), or if the profiles in that region should be
averaged and the fit done to that average profile (false).

FUNCTION TYPE
Which function to fit is specified in the spxtype parameter. Only two values (case insensitive) are supported. A value of
"plp" indicates that a power logarithmic polynomial should be fit. A value of "ltp" indicates a logarithmic transformed
polynomial should be fit.

INCLUDING STANDARD DEVIATIONS OF PIXEL VALUES
If the standard deviations of the pixel values in the input image are known and they vary in the image (eg they are higher for pixels
near the edge of the band), they can be included in the sigma parameter. This parameter takes either an array or an image name. The
array or image must have one of three shapes: 1. the shape of the input image, 2. the same dimensions as the input image with the lengths
of all axes being one except for the fit axis which must have length corresponding to its length in the input image, or 3. be one
dimensional with lenght equal the the length of the fit axis in the input image. In cases 2 and 3, the array or pixels in sigma will
be replicated such that the image that is ultimately used is the same shape as the input image. The values of sigma must be non-negative.
It is only the relative values that are important. A value of 0 means that pixel should not be used in the fit. Other than that, if pixel
A has a higher standard deviation than pixel B, then pixel A is noisier than pixel B and will receive a lower weight when the fit is done.
The weight of a pixel is the usual

weight = 1/(sigma*sigma)

In the case of multifit=F, the sigma values at each pixel along the fit axis in the hyperplane perpendicular to the fit axis which includes
that pixel are averaged and the resultant averaged standard deviation spectrum is the one used in the fit. Internally, sigma values are normalized
such that the maximum value is 1. This mitigates a known overflow issue.

One can write the normalized standard deviation image used in the fit by specifying its name in outsigma. This image can then be
used as sigma for subsequent runs.

RETURNED DICTIONARY STRUCTURE
The returned dictionary has a (necessarily) complex structure. First, there are keys "xUnit" and "yUnit" whose values are
the abscissa unit and the ordinate unit described by simple strings. Next there are arrays giving a broad overview of the
fit quality. These arrays have the shape of the specified region collapsed along the fit axis with the axis corresponding to the fit
axis having length of 1:

attempted: a boolean array indicating which fits were attempted (eg if too few unmasked points, a fit will not be attempted).
converged: a boolean array indicating which fits converged. False if the fit was not attempted.
valid:     a boolean array indicating which solutions fall within the specified valid ranges of parameter space. Any solution for
           which a value or error is NaN is automatically marked as invalid.
niter:     an int array indicating the number of iterations for each profile, <0 if the fit did not converge
direction: a string array containing the world direction coordinate for each profile

There is a "type" array having number of dimensions equal to the number of dimensions in the above arrays plus one. The shape of
the first n-1 dimensions is the same as the shape of the above arrays. The length of the last dimension is equal to the number of
components fit. The values of this array are all "POWER LOGARITHMIC POLYNOMIAL" or "LOGARITHMIC TRANSFORMED POLYNOMIAL", depending
on which type function was fit.

There will be a subdictionary accessible via the "plp" or "ltp" key (depending on which type of function was fit) which will have
subkeys "solution" and "error" which will each have an array of values. Each of these arrays will have one more dimension than the overview arrays
described above. The shape of the first n-1 dimensions will be the same as the shape of the overview arrays described above, while the
final dimension will have length equal to the number of parameters that were fit. Along this axis will be the
corresponding fit result or associated error (depending on the array's associated key) of the fit. In cases where
the fit was not attempted or did not converge, a value of NAN will be present.

OUTPUT IMAGES
In addition to the returned dictionary, optionally one or more of any combination of output images can be written.
The model and residual parameters indicate the names of the model and residual images to be written; empty values inidcate that these images
should not be written.

The parameters spxsol and spxerr are the names of the solution and error images to write, respectively. In cases
where more than one coefficient are fit, the image names will be appended with an underscore followed by the relevant
coefficient number ("_0", "_1", etc). These images contain the arrays for the associated parameter solutions or errors
described in previous sections. Pixels for which fits were not attempted, did not converge, or converged but have values
of NaN (not a number) or INF (infinity) will be masked as bad.

LPT vs PLP
Ultimately, the choice of which functional form to use in determining the spectral index is up to the user and should be based
on the scientific goals. However, below is a summary of one user's experience and preferences as an example:

If the weights are known or can be determined from the images (eg. the source-free image rms and a fractional calibration error) then I
favor a weighted fit using the non-linear (power-law) model. An unweighted fit using the non-linear model will, in general, give far
too much leverage to large flux values.

If the weights are unknown or will not be considered by the fitting algorithm, then I prefer the log-transformed polynomial model. However,
this does not work well in low signal-to-noise regions. A conservative mask could be created such that only high s/n areas are fit,
but this could hinder many science objectives.

EXAMPLES

res = spxfit(imagename=["im0.im","im1.im"], multifit=true, spxtype="plp", spxest=[0.5,2,0.1], div="1GHz", spxsol="myplpsolutions.im")


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'spxfit'
        self.__globals__['taskname'] = 'spxfit'
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
            myparams['box'] = box = self.parameters['box']
            myparams['region'] = region = self.parameters['region']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['axis'] = axis = self.parameters['axis']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['minpts'] = minpts = self.parameters['minpts']
            myparams['multifit'] = multifit = self.parameters['multifit']
            myparams['spxtype'] = spxtype = self.parameters['spxtype']
            myparams['spxest'] = spxest = self.parameters['spxest']
            myparams['spxfix'] = spxfix = self.parameters['spxfix']
            myparams['div'] = div = self.parameters['div']
            myparams['spxsol'] = spxsol = self.parameters['spxsol']
            myparams['spxerr'] = spxerr = self.parameters['spxerr']
            myparams['model'] = model = self.parameters['model']
            myparams['residual'] = residual = self.parameters['residual']
            myparams['wantreturn'] = wantreturn = self.parameters['wantreturn']
            myparams['stretch'] = stretch = self.parameters['stretch']
            myparams['logresults'] = logresults = self.parameters['logresults']
            myparams['logfile'] = logfile = self.parameters['logfile']
            myparams['append'] = append = self.parameters['append']
            myparams['sigma'] = sigma = self.parameters['sigma']
            myparams['outsigma'] = outsigma = self.parameters['outsigma']

        if type(spxest)==float: spxest=[spxest]
        if type(spxfix)==bool: spxfix=[spxfix]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['box'] = box
        mytmp['region'] = region
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['axis'] = axis
        mytmp['mask'] = mask
        mytmp['minpts'] = minpts
        mytmp['multifit'] = multifit
        mytmp['spxtype'] = spxtype
        mytmp['spxest'] = spxest
        mytmp['spxfix'] = spxfix
        mytmp['div'] = div
        mytmp['spxsol'] = spxsol
        mytmp['spxerr'] = spxerr
        mytmp['model'] = model
        mytmp['residual'] = residual
        mytmp['wantreturn'] = wantreturn
        mytmp['stretch'] = stretch
        mytmp['logresults'] = logresults
        mytmp['logfile'] = logfile
        mytmp['append'] = append
        mytmp['sigma'] = sigma
        mytmp['outsigma'] = outsigma
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'spxfit.xml')

        casalog.origin('spxfit')
        try :
          #if not trec.has_key('spxfit') or not casac.casac.utils().verify(mytmp, trec['spxfit']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['spxfit'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('spxfit', 'spxfit.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'spxfit'
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
          result = spxfit(imagename, box, region, chans, stokes, axis, mask, minpts, multifit, spxtype, spxest, spxfix, div, spxsol, spxerr, model, residual, wantreturn, stretch, logresults, logfile, append, sigma, outsigma)

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
             tname = 'spxfit'
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
#        paramgui.runTask('spxfit', myf['_ip'])
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
        a['box']  = ''
        a['region']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['axis']  = -1
        a['mask']  = ''
        a['minpts']  = 1
        a['multifit']  = False
        a['spxtype']  = 'plp'
        a['spxest']  = []
        a['spxfix']  = []
        a['div']  = 0
        a['wantreturn']  = True
        a['logresults']  = True
        a['logfile']  = ''
        a['sigma']  = ''

        a['mask'] = {
                    0:odict([{'notvalue':''}, {'stretch':False}])}
        a['multifit'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'spxsol':""}, {'spxerr':""}, {'model':""}, {'residual':""}])}
        a['logfile'] = {
                    0:odict([{'notvalue':''}, {'append':True}])}
        a['sigma'] = {
                    0:odict([{'notvalue':''}, {'outsigma':''}])}

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
    def description(self, key='spxfit', subkey=None):
        desc={'spxfit': 'Fit a 1-dimensional model(s) to an image(s) or region for determination of spectral index.',
               'imagename': 'Name of the input image(s)',
               'box': 'Rectangular region to select in direction plane. Default is to use the entire direction plane.',
               'region': 'Region selection. Default is to use the full image.',
               'chans': 'Channels to use. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Default is to use all Stokes planes.',
               'axis': 'The profile axis. Default: use the spectral axis if one exists, axis 0 otherwise (<0).',
               'mask': 'Mask to use. Default is none.',
               'minpts': 'Minimum number of unmasked points necessary to attempt fit.',
               'multifit': 'If true, fit a profile along the desired axis at each pixel in the specified region. If false, average the non-fit axis pixels and do a single fit to that average profile. Default False.',
               'spxtype': 'Type of function to fit. "plp" = power logarithmic polynomial, "ltp" = logarithmic transformed polynomial.',
               'spxest': 'REQUIRED. Initial estimates as array of numerical values for the spectral index function coefficients. eg [1.5, -0.8] if fitting a plp function thought to be close to 1.5*(x/div)**(-0.8) or [0.4055, -0.8] if fitting an lpt function thought to be close to ln(1.5) - 0.8*ln(x/div).',
               'spxfix': 'Fix the corresponding spectral index function coefficients during the fit. True means hold fixed.',
               'div': 'Divisor (numerical value or quantity) to use in the logarithmic terms of the plp or ltp function. 0 means calculate a useful value on the fly.',
               'spxsol': 'Name of the spectral index function coefficient solution image to write.',
               'spxerr': 'Name of the spectral index function coefficient error image to write.',
               'model': 'Name of model image. Default: do not write the model image ("").',
               'residual': 'Name of residual image. Default: do not write the residual image ("").',
               'wantreturn': 'Should a record summarizing the results be returned?',
               'stretch': 'Stretch the mask if necessary and possible? ',
               'logresults': 'Output results to logger?',
               'logfile': 'File in which to log results. Default is not to write a logfile.',
               'append': 'Append results to logfile? Logfile must be specified. Default is to append. False means overwrite existing file if it exists.',
               'sigma': 'Standard deviation array or image name(s).',
               'outsigma': 'Name of output image used for standard deviation. Ignored if sigma is empty.',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['box']  = ''
        a['region']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['axis']  = -1
        a['mask']  = ''
        a['minpts']  = 1
        a['multifit']  = False
        a['spxtype']  = 'plp'
        a['spxest']  = []
        a['spxfix']  = []
        a['div']  = 0
        a['spxsol']  = ''
        a['spxerr']  = ''
        a['model']  = ''
        a['residual']  = ''
        a['wantreturn']  = True
        a['stretch']  = False
        a['logresults']  = True
        a['logfile']  = ''
        a['append']  = True
        a['sigma']  = ''
        a['outsigma']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if self.parameters['multifit']  == True:
            a['spxsol'] = ""
            a['spxerr'] = ""
            a['model'] = ""
            a['residual'] = ""

        if self.parameters['logfile']  != '':
            a['append'] = True

        if self.parameters['sigma']  != '':
            a['outsigma'] = ''

        if a.has_key(paramname) :
              return a[paramname]
spxfit_cli = spxfit_cli_()
