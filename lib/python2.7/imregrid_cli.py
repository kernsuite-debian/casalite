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
from task_imregrid import imregrid
class imregrid_cli_:
    __name__ = "imregrid"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (imregrid_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'template':None, 'output':None, 'asvelocity':None, 'axes':None, 'shape':None, 'interpolation':None, 'decimate':None, 'replicate':None, 'overwrite':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, template=None, output=None, asvelocity=None, axes=None, shape=None, interpolation=None, decimate=None, replicate=None, overwrite=None, ):

        """regrid an image onto a template image

        Detailed Description:

Imregrid will regrid an input image onto a new coordinate system from a template image
or to a new directional reference frame. If a template image is used, then the input and
template images must have the same coordinate structure.

        Arguments :
                imagename: Name of the source image
                   Default Value: 

                template: A dictionary, refcode, or name of an image that provides the output shape and coordinate system
                   Default Value: get

                output: Name for the regridded image
                   Default Value: 

                asvelocity: Regrid spectral axis in velocity space rather than frequency space?
                   Default Value: True

                axes: The pixel axes to regrid. -1 => all.
                   Default Value: -1

                shape: Shape of the output image. Only used if template is an image. If not specified (-1), the output image shape will be the same as the template image shape along the axes that are regridded and the same as input image shape along the axes which are not regridded.
                   Default Value: -1

                interpolation: The interpolation method.  One of "nearest", "linear", "cubic".
                   Default Value: linear

                decimate: Decimation factor for coordinate grid computation
                   Default Value: 10

                replicate: Replicate image rather than regrid?
                   Default Value: False

                overwrite: Overwrite (unprompted) pre-existing output file?
                   Default Value: False


        Example :

The imregrid task currently finds the nearest input pixel center and interpolates to the output pixel center.
No averaging is done in any direction!

Imregrid will regrid an input image onto a new coordinate system from a template image
or to a new directional reference frame. If a template image is used, then the input and
template images must have the same coordinate structure.

Keyword arguments:

imagename       Name of the source image that needs to be regridded. Must be specified.
                example: imagename='orion.image'
template        Dictionary, directional reference code, or imagename defining the new
                shape and coordinate system, or 'get' to return the template
                dictionary for imagename.  Recognized directional reference codes are:
                'J2000', 'B1950', 'B1950_VLA', 'GALACTIC', 'HADEC', 'AZEL',
                'AZELSW', 'AZELNE', 'ECLIPTIC', 'MECLIPTIC', 'TECLIPTIC',
                and 'SUPERGAL'.
                default: 'get'; example: template='orion_j2000.im' (for a template image),
                template='J2000' (to regrid the input image to J2000 coordinates).
shape           Shape of the output image. Only used if template is an image.
                If not specified (-1), the output image will be the same as the template image
                shape along the axes which are regridded and the same as the input image shpae
                along the axes which are not regridded. If specified and the axis ordering between
                the input image and the template are not the same, the values in the array correspond
                to the axis ordering of the input image; the output image will have the same axis
                ordering as the input image. Ignored if template is set equal to a
                reference code. If template is a dictionary, the output shape is
                retrieved from the dictionary so the shape input parameter is ignored.
output          Name for the regridded image.  Must be specified.
                example: imagename='orion_shifted.im'
asvelocity      If True, regrid spectral axis with respect to velocity, not frequency. If False,
                regrid with respect to frequency. default: True
axes            The pixel axes to regrid. Default value [-1] => all except Stokes. Ignored
                if template is set equal to a reference code (in which case only the directional
                axes are regridded). If specified, this should
                be provided as an array. example axes=[0,1] (only regrid the first two axes, which
                are normally the directional axes).
interpolation   The interpolation method.  One of 'nearest', 'linear', 'cubic'.
decimate        Decimation factor for coordinate grid computation
replicate       Replicate image rather than regrid?
overwrite">     Overwrite (unprompted) pre-existing output file?
async           Run task in a separate process (return CASA prompt)
                default: False; example: async=True
                
The new coordinate system is defined by the template parameter, which can be:

    * a recognized directional reference frame string. This will rotate the image and the coordinate system so that
      the new reference frame's axes are aligned to the cardinal directions (left-right, up-down).
      Rotation occurs about the center direction pixel. If this pixel is not the reference pixel,
      a temporary copy of the original image is created and the coordinate system is adjusted so
      the center direction pixel is the reference pixel. The coordinate system of the input image
      is not modified and the output image's reference direction pixel is the center pixel.
      Note that the conversion between one frame and another in general becomes less accurate
      as distance from the output image's reference pixel increases. Before the rotation occurs, the
      image is padded with masked pixels to ensure that all good pixels are used in the rotation (ie the
      corners of the image are not cropped after the rotation). After the image is rotated, any masked slices
      remaining along the edges of the image in the directional coordinate are cropped, so that there are
      no masked slices in the directional coordinate along the edges of the final image.
    * a {'csys': [valid coordinate system dictionary], 'shap': [int array describing the output shape]} dictionary.
      This is normally obtained by first running regrid with template='get'. In this case imregrid returns the
      necessary dictionary.
    * 'get', which does not regrid but returns the template dictionary
      for imagename, suitable for modification and reuse (see the point immediately above), or
    * the name of an image from which to get the coordinate system and shape.
      The input and template images must have the same
      coordinate structure.
      
Regridding of complex-valued images is supported. The real and imaginary parts are
regridded independently and the resulting regridded pixel values are combined to
form the regridded, complex-valued image.

The argument {\stfaf replicate} can be used to simply replicate pixels
rather than regridding them.  Normally ({\stfaf replicate=F}), for every
output pixel, its world coordinate is computed and the corresponding
input pixel found (then a little interpolation grid is generated).  If
you set {\stfaf replicate=T}, then what happens is that for every output
axis, a vector of regularly sampled input pixels is generated (based on
the ratio of the output and input axis shapes).  So this just means the
pixels get replicated (by whatever interpolation scheme you use) rather
than regridded in world coordinate space.  This process is much faster,
but its not a true world coordinate based regrid. 

As decribed above, when {\stfaf replicate} is False, a coordinate is
computed for each output pixel; this is an expensive operation.  The
argument {\stfaf decimate} allows you to decimate the computation of
that coordinate grid to a sparse grid, which is then filled in via fast
interpolation.  The default for {\stfaf decimate} is 10.  The number of
pixels per axis in the sparse grid is the number of output pixels for
that axis divided by the decimation factor.  A factor of 10 does pretty
well.  You may find that for very non-linear coordinate systems (e.g. 
very close to the pole) that you have to reduce the decimation factor.
You may also have to reduce the decimation factor if the number of pixels
in the output image along an axis to be regridded is less than about 50, or
the output image may be completely masked.

If one of the axes to be regridded is a spectral axis and asvelocity=T,
the axis will be regridded to match the velocity, not the frequency,
coordinate of the template coordinate system. Thus the output pixel
values will correspond only to the velocity, not the frequency, of the
output axis.

A variety of interpolation schemes are provided (only
the first three characters to be specified).  The cubic interpolation
is substantially slower than linear, and often the improvement is
modest.  By default linear interpolation is used.

If an image has per-plane beams and one attempts to regrid the spectral axis,
an exception is thrown.

RULES USED FOR GENERATING OUTPUT IMAGES IN SPECIFIC CASES

There are numerous rules governing the shape and coordinate system of the output
image depending on the input image, template image, and wheher default values of the
axes and shape parameters are used. They are enumerated below. 

NOTE: If you want to be certain of what type of output you will get, it is highly
recommended you specify both axes and shape to avoid any ambiguity.

1. Rules governing Stokes axes
    1.1. If the input image has no stokes axis, then the output image will have no stokes axis.
    1.2. If the input image has a stokes axis, but the template image/coordinate system does not,
         and if the default value of the shape parameter is used or if shape is specified and the
         specified value for the length stokes axis in equal to the length of the input image
         stokes axis, then all stokes in the input
         image will be present in the output image
    1.3. If the input image has a stokes axis, but the template image/coordinate system does not,
         and if the value of the shape parameter is specified but the length of the resulting stokes
         axis is not equal to the length of the input image's stokes axis, a failure will occur.
    1.4. If the input image has a stokes axis, if the template parameter is an image name, and if the
         template image has a degenerate stokes axis, if the axes parameter is not specified or is specified
         but does not contain the input stokes axis number, and if the shape parameter is not specified, then
         all stokes planes in the input image will be present in the output image.
    1.5. If the input image has a stokes axis, if the template parameter is an image name, and if the
         template image has a degenerate stokes axis, if the axes parameter is not specified or is specified
         but does not contain the input stokes axis number, if the shape parameter is specified, and if the
         specified length of the stokes axis is not equal to the length of the input stokes axis, then
         a failure will occur.
    1.6. If the input image has a stokes axis, if the template parameter is an image name, if the
         template image has a degenerate stokes axis, if the axes parameter is specified contains the
         input stokes axis number, then use the applicable rule of rules 1.7. and 1.8. for the template
         image having a nondegenerate stokes axis.
    1.7. If the input image has a stokes axis, if the template parameter is an image name, if the
         template image has a nondegenerate stokes axis, and if axes is not specified or if it is, it contains
         the input stokes axis number, then only the stokes parameters common to both the input image and
         the template image will be present in the output image. If the input image and the template image
         have no common stokes parameters, failure will occur. If shape is specified and the length of the
         specified stokes axis is not equal to the number of common stokes parameters in the input image and
         the template image, then failure will result.
    1.8. If the input image has a stokes axis, if the template parameter is an image name, if the
         template image has a nondegenerate stokes axis, and if axes is specified but does not contain the input
         image stokes axis number, then all stokes present in the input image will be present in the output image.
         If shape is also specified but the length of the specified stokes axis does not equal the length of
         the input stokes axis, then failure will result.

2. Rules governing spectral axes
    In all cases, if the shape parameter is specified, the spectral axis length must be consistent with what
    one would normally expect in the special cases, or a failure will result.
    2.1. If the input image does not have a spectral axis, then the output image will not have a spectral axis.
    2.2. If the input image has a degenerate spectral axis, if the template parameter is an image name, and if the
         template image has a spectral axis, if axes is not specified or if it is and does not
         contain the input image spectral axis number, then the spectral coordinate of the input image is copied
         to the output image and the output image will have a degenerate spectral axis.
    2.3. If the input image has a degenerate spectral axis, if the template parameter is an image name, and if the
         template image has a spectral axis, if axes is specified and it
         contains the input image spectral axis number, then the spectral coordinate of the template image is copied
         to the output image. If shape is not specified, the output image will have the same number of channels
         as the input image. If shape is specified, the output image will have the number of channels as specified
         in shape for the spectral axis. In these cases, the pixel and mask values for all spectral hyperplanes
         will be identical; the regridded single spectral plane is simply replicated n times, where n is the
         number of channels in the output image.
    2.4. If the input image has a spectral axis, if the template parameter is an image name, and if the
         template image does not have a spectral axis, if axes is not specified or if it is and does not
         contain the input image spectral axis number, then the spectral coordinate of the input image is copied
         to the output image and the output image will have the same number of channels as the input image.
    2.5. If the input image has a spectral axis, if the template parameter is an image name, if the
         template image does not have a spectral axis, if axes is specified it 
         contains the input image spectral axis number, then failure will result.
    2.6. If the input image has a spectral axis, if the template parameter is an image name, if the
         template image has a degenerate spectral axis, and if axes is unspecified or if it is but does not
         contain the spectral axis number of the input image, the spectral coordinate of the input image is
         copied to the output image and the output image will have the same number of channels as the input
         image.
    2.7. If the input image has a spectral axis, if the template parameter is an image name, if the
         template image has a nondegenerate spectral axis, and if axes is unspecified or if it is and
         contains the spectral axis number of the input image, regrid the spectral axis of the input to
         match the spectral axis of the template.
         
IMPORTANT NOTE ABOUT FLUX CONSERVATION
in general regridding is inaccurate for images that the angular resolution is poorly
sampled. A check is done for such cases and a warning message is emitted if a beam present.
However, no such check is done if there is no beam present. To add a restoring beam to
an image, use ia.setrestoringbeam().
         
Basic Examples

# Regrid an image to the "B1950" or "GALACTIC" coordinate systems

   imregrid(imagename="input.image", output="output.image", template="B1950")
   imregrid(imagename="input.image", output="output.image", template="GALACTIC")

Note that when regridding to another coordinate system in the manner above, if the
input image's direction coordinate is already in the frame specified by template,
a straight copy of the image is made. No regridding is actually done.

# Obtain a template dictionary from an image and then use it to regrid another image

   temp_dict = imregrid(imagename="target.image", template="get")
   imregrid(imagename="input.image", output="output.image", template=temp_dict)

In this example, the template="get" option is used in the first command in order to
characterize the desired shape and coordinate system used, and a new dictionary,
temp_dict, is generated accordingly. This is then used when performing the actual
regridding of input.image in the second command. 


More Advanced Examples

It is also possible to directly use a template image for regridding with imregrid.
For this to work reliably and predictably, the dimensionality (i.e. which
dimensions are present in an image) and the axis ordering of the input image must
be the same. The type and ordering of the axes of both the input and template
images can (and should) first be examined using the CASA imhead task. Any
necessary reordering of axes can be performed using the CASA imtrans task.

Unless the user explicitly specifies which dimensions to regrid using the axes
parameter (see the following example), imregrid will also attempt to regrid
degenerate axes (i.e. image axes of length one pixel). Stokes axes are never
regridded.

In the case where template is an image name and the default value of shape is specified,
the output image's shape will be the same as the template image's shape along the axes which
are regridded and the same as the input image's shape along the axes which are not regridded.
So for example, if the input image has a shape of [20, 30, 40] and the template image has a shape
of [10, 40, 70] and only axes=[0, 1], the output image will have a shape of [10, 40, 40]. If axes=[2],
the output image will have a shape of [20, 30, 70].

# Regrid input.image by directly using target.image as a template

   imregrid(imagename="input.image", output="output.image", template="target.image", shape=[500,500,40,1])

In this example, it is assumed that the axis order of the input image is of the
form (direction_x, direction_y, spectral, Stokes), where 'direction_x' and 'direction_y'
are the directional coordinates on the sky (in some reference frame),
'spectral' is a velocity/frequency axis, and 'Stokes' contains polarization
information.  In this example, input.image might typically be a data cube of
shape [100, 100, 40, 1]. Note that the default value of asvelocity (True) will be used so that
the spectral axis will be regridded to the same velocity system as that of the template image.


# Regrid only the first two axes of an image

Firstly, the user should inspect the type and ordering of the axes with imhead,
and then correct with imtrans if necessary.

   imregrid(imagename="input.image", output="output.image", template="target.image", axes=[0,1])

The above command will regrid only the first two axes (normally the directional axes)  of input.image and
leave all other axes unchanged. The output image will have the shape of the template image along the regridded
axes [0, 1] and the shape of the  input image along the other axes since the shape parameter was not
explicitly specified.


# Regrid the third axis, considering velocity rather than frequency units

   imregrid(imagename="input.image", output="output.image", template="target.image", axes=[2], asvelocity=True)

This example regrids the spectral axis (zero-based axis number 2)  with respect to velocity because the asvelocity parameter
has been set to True. This is useful when eg, regridding a cube containing one spectral line to match the velocity coordinate
of another cube containing a different spectral line.


# Regrid the third axis, considering velocity rather than frequency units but first set the rest frequency

   imhead("input.image", mode="put", hdkey="restfreq", hdvalue="110GHz")
   imregrid(imagename="input.image", output="output.image", template="target.image", axes=[2], asvelocity=True)

The first command in this example uses the imhead task to set the value of the
image rest frequency to a value of 110GHz in input.image. The following
imregrid command then performs a frequency units regridding only of the third
axis listed (zero-based axis) (2), taking account of the input.image rest frequency in the input file.



        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'imregrid'
        self.__globals__['taskname'] = 'imregrid'
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
            myparams['template'] = template = self.parameters['template']
            myparams['output'] = output = self.parameters['output']
            myparams['asvelocity'] = asvelocity = self.parameters['asvelocity']
            myparams['axes'] = axes = self.parameters['axes']
            myparams['shape'] = shape = self.parameters['shape']
            myparams['interpolation'] = interpolation = self.parameters['interpolation']
            myparams['decimate'] = decimate = self.parameters['decimate']
            myparams['replicate'] = replicate = self.parameters['replicate']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']

        if type(axes)==int: axes=[axes]
        if type(shape)==int: shape=[shape]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['template'] = template
        mytmp['output'] = output
        mytmp['asvelocity'] = asvelocity
        mytmp['axes'] = axes
        mytmp['shape'] = shape
        mytmp['interpolation'] = interpolation
        mytmp['decimate'] = decimate
        mytmp['replicate'] = replicate
        mytmp['overwrite'] = overwrite
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'imregrid.xml')

        casalog.origin('imregrid')
        try :
          #if not trec.has_key('imregrid') or not casac.casac.utils().verify(mytmp, trec['imregrid']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['imregrid'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('imregrid', 'imregrid.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'imregrid'
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
          result = imregrid(imagename, template, output, asvelocity, axes, shape, interpolation, decimate, replicate, overwrite)

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
             tname = 'imregrid'
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
#        paramgui.runTask('imregrid', myf['_ip'])
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
        a['template']  = 'get'
        a['output']  = ''
        a['asvelocity']  = True
        a['axes']  = [-1]
        a['interpolation']  = 'linear'
        a['decimate']  = 10
        a['replicate']  = False
        a['overwrite']  = False

        a['template'] = {
                    0:odict([{'notvalue':'get'}, {'shape':[-1]}])}

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
    def description(self, key='imregrid', subkey=None):
        desc={'imregrid': 'regrid an image onto a template image',
               'imagename': 'Name of the source image',
               'template': 'A dictionary, refcode, or name of an image that provides the output shape and coordinate system',
               'output': 'Name for the regridded image',
               'asvelocity': 'Regrid spectral axis in velocity space rather than frequency space?',
               'axes': 'The pixel axes to regrid. -1 => all.',
               'shape': 'Shape of the output image. Only used if template is an image. If not specified (-1), the output image shape will be the same as the template image shape along the axes that are regridded and the same as input image shape along the axes which are not regridded.',
               'interpolation': 'The interpolation method.  One of "nearest", "linear", "cubic".',
               'decimate': 'Decimation factor for coordinate grid computation',
               'replicate': 'Replicate image rather than regrid?',
               'overwrite': 'Overwrite (unprompted) pre-existing output file?',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['template']  = 'get'
        a['output']  = ''
        a['asvelocity']  = True
        a['axes']  = [-1]
        a['shape']  = [-1]
        a['interpolation']  = 'linear'
        a['decimate']  = 10
        a['replicate']  = False
        a['overwrite']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['template']  != 'get':
            a['shape'] = [-1]

        if a.has_key(paramname) :
              return a[paramname]
imregrid_cli = imregrid_cli_()
