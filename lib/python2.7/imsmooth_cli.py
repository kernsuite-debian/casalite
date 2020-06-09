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
from task_imsmooth import imsmooth
class imsmooth_cli_:
    __name__ = "imsmooth"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (imsmooth_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'kernel':None, 'major':None, 'minor':None, 'pa':None, 'targetres':None, 'kimage':None, 'scale':None, 'region':None, 'box':None, 'chans':None, 'stokes':None, 'mask':None, 'outfile':None, 'stretch':None, 'overwrite':None, 'beam':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, kernel=None, major=None, minor=None, pa=None, targetres=None, kimage=None, scale=None, region=None, box=None, chans=None, stokes=None, mask=None, outfile=None, stretch=None, overwrite=None, beam=None, ):

        """Smooth an image or portion of an image

        Detailed Description:


        Arguments :
                imagename: Name of the input image. Must be specified.
                   Default Value: 

                kernel: Type of kernel to use. Acceptable values are "b", "box", or "boxcar" for a boxcar kernel, "g", "gauss", or "gaussian" for a gaussian kernel, "c", "common", or "commonbeam" to use the common beam of an image with multiple beams as the gaussian to which to convolve all the planes, "i" or "image" to use an image as the kernel.
                   Default Value: gauss
                   Allowed Values:
                                g
                                gauss
                                gaussian
                                b
                                box
                                boxcar
                                commonbeam
                                common
                                c
                                image
                                i

                major: Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".
                   Default Value: 

                minor: Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".
                   Default Value: 

                pa: Position angle used only for gaussian kernel. Standard quantity representation.
                   Default Value: 

                targetres: If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).
                   Default Value: False

                kimage: Kernel image name. Only used if kernel="i" or "image".
                   Default Value: 

                scale: Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image".
                   Default Value: -1.0

                region: Region selection. Default is to use the full image.
                   Default Value: 

                box: Rectangular region to select in direction plane. Default is to use the entire direction plane.
                   Default Value: 

                chans: Channels to use. Default is to use all channels.
                   Default Value: 

                stokes: Stokes planes to use. Default is to use all Stokes planes.
                   Default Value: 

                mask: Mask to use. Default is none.
                   Default Value: 

                outfile: Output image name. Must be specified.
                   Default Value: 

                stretch: If true, stretch the mask if necessary and possible.
                   Default Value: False

                overwrite: If true, overwrite (unprompted) pre-existing output file.
                   Default Value: False

                beam: Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa.
                   Default Value: 

        Returns: any

        Example :

This task performs a Fourier-based convolution to 'smooth' the
direction plane of an image. Smoothing is typically performed in order to reduce the noise in
an image.

Keyword arguments:

imagename    Input image name. Must be specified.
outfile      Output smoothed image file name. Must be specified.
kernel       Type of kernel to use when smoothing ("g", "gauss", or "gaussian" for a gaussian
             kernel or "b", "box", or "boxcar" for a boxcar kernel), or if the
             image has multiple channels and kernel="commonbeam" (or "c", or "common"), convolve
             all channels to the smallest beam that encloses all beams in the input image, "i" or "image"
             to use an image as the kernel.
             For boxcar smoothing, the major axis is parallel to the y-axis of the image
             and the minor axis is parallel to the x-axis. For a Gaussian, the
             orientation is specified by a position angle. A value of 0 degrees means
             the major axis is parallel to the y-axis and an increasing value of the
             position angle results in a counter-clockwise rotation of the ellipse.
                default: 'gauss'
major        Major axis of kernel which must be specified for boxcar smoothing. For
             Gaussian smoothing, the kernel parameters can alternatively be specified
             in the beam parameter. Standard quantity representations are supported.
             Example "4arcsec".
minor        Minor axis of kernel which must be specified for boxcar smoothing. For
             Gaussian smoothing, the kernel parameters can alternatively be specified
             in the beam parameter. Standard quantity representations are supported.
             Example "3arcsec".
pa           Position angle to use for gaussian kernel, unused for boxcar. 
             The Gaussian kernel parameters can alternatively be specified
             in the beam parameter. Standard quantity representations are supported.
             Example "40deg".
beam         Record specifying Gaussian beam parameters. Do not specify any of
             major, minor, or pa if you choose to specify this parameter.
             Example: {"major": "5arcsec", "minor": "2arcsec", "pa": "20deg"}
targetres    Boolean used only for kernel='gauss'. If True, kernel parameters (major/minor/pa
             or beam) are the resolution of the output image. If false, a gaussian
             with these parameters is convolved with the input image to produce
             the output image.
kimage       The image to be used as the convolution kernel. Only used if kernel="image" or "i".
scale        Scale  factor to use if kernel="i" or "image".  -1.0 means auto-scale, which is the default.
mask         Mask to use. Default is none.
region       Region selection. Default is to use the full image.
box          Rectangular region to select in direction plane. 
             Default is to use the entire direction plane.
             Example: "5, 10, 100, 200".
chans        Channels to use. Default is to use all channels.
stokes       Stokes planes to use. Default is to use
             all Stokes planes.
             Example: 'I'

GAUSSIAN KERNEL

The direction pixels must be square. If they are not, use imregrid to regrid your image onto a grid
of square pixels.

Under the hood, ia.convolve2d() is called with scale=-1 (auto scaling). This means that, when the input image
has a restoring beam, pixel values in the output image are scaled in such a way as to conserve flux density.

Major and minor are the full width at half maximum  (FWHM) of the Gaussian. pa is the position angle
of the Gaussian. The beam parameter offers an alternate way of describing the convolving Gaussian.
If used, neither major, minor, nor pa can be specified. The beam parameter must have exactly three
fields: "major", "minor", and "pa" (or "positionangle"). This is the record format for the output
of ia.restoringbeam(). For example

beam = {"major": "5arcsec", "minor": "2arcsec", "pa": "20deg"}

If both beam and any of major, minor, and/or pa is specified for a Gaussian kernel,
an exception will be thrown.    

Alternatively, if the input image has multiple beams, setting kernel='commonbeam' will result in the
smallest beam that encloses all beams in the image to be used as the target resolution to which to
convolve all planes. 

In addition, the targetres parameter indicates if the specified Gaussian is to be the
resolution of the final image (True) or if it is to be used to convolve the input image.
If True, the input image must have a restoring beam. Use imhead() or ia.restoringbeam()
to check for its existence. If the image has multiple beams and targetres=True,
all planes in the image will be convolved so that the resulting resolution is that
specified by the kernel parameters. If the image has multiple beams and targetres=False,
each plane will be convolved with a Gaussian specified by beam (and hence, in
general, the output image will also have multiple beams that vary with spectral channel
and/or polarization).

If the units on the original image include Jy/beam, the units on the
output image will be rescaled by the ratio of the input and output
beams as well as rescaling by the area of convolution kernel.

If the units on the original image include K, then only the image
convolution kernel rescaling is done. 

BOXCAR KERNEL

major is length of the box along the y-axis and minor is length of the box along the x-axis.
pa is not used and beam should not be specified. The value of targetres is not used.

IN GENERAL

The major, minor, and pa parameters can be specified in one of three ways
   Quantity -- for example major=qa.quantity(1, 'arcsec')
               Note that you can use pixel units, such as 
               major=qa.quantity(1, 'pix')
   String -- for example minor='1pix' or major='0.5arcsec'
             (i.e. a string that the Quanta quantity function accepts).
   Numeric -- for example major=10.
              In this case, the units of major and minor are assumed to 
              be in arcsec and units of pa are assumed to be degrees. 

Note: Using pixel units allows you to convolve axes with different units.

IMAGE KERNEL
If kernel="i" or "image", the image specified by kimage is used to convolve the input image.
The coordinate system of the convolution image is ignored; only the pixel values are considered.

Fourier-based convolution is performed.

The provided kernel can have fewer
dimensions than the image being convolved.  In this case, it will be
padded with degenerate axes.  An error will result if the kernel has
more dimensions than the image.

The scaling of the output image is determined by the argument {\stfaf scale}.
If this is left unset, then the kernel is normalized to unit sum.
If {\stfaf scale} is not left unset, then the convolution kernel
will be scaled (multiplied) by this value.

Masked pixels will be assigned the value 0.0 before convolution.

The output mask is the combination (logical OR) of the default input
\pixelmask\ (if any) and the OTF mask.  Any other input \pixelmasks\
will not be copied.  The function
maskhandler
should be used if there is a need to copy other masks too.


EXAMPLES

# smoothing with a gaussian kernel 20arseconds by 10 arseconds
imsmooth( imagename='my.image', kernel='gauss', major='20arcsec', minor='10arcsec', pa="0deg")

# the same as before, just a different way of specifying the kernel parameters
mybeam = {'major': '20arcsec', 'minor': '10arcsec', 'pa': '0deg'}
imsmooth( imagename='my.image', kernel='gauss', beam=mybeam)

# Smoothing using pixel coordinates and a boxcar kernel.
imsmooth( imagename='new.image', major='20pix', minor='10pix', kernel='boxcar')


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'imsmooth'
        self.__globals__['taskname'] = 'imsmooth'
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
            myparams['kernel'] = kernel = self.parameters['kernel']
            myparams['major'] = major = self.parameters['major']
            myparams['minor'] = minor = self.parameters['minor']
            myparams['pa'] = pa = self.parameters['pa']
            myparams['targetres'] = targetres = self.parameters['targetres']
            myparams['kimage'] = kimage = self.parameters['kimage']
            myparams['scale'] = scale = self.parameters['scale']
            myparams['region'] = region = self.parameters['region']
            myparams['box'] = box = self.parameters['box']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['stretch'] = stretch = self.parameters['stretch']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['beam'] = beam = self.parameters['beam']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['kernel'] = kernel
        mytmp['major'] = major
        mytmp['minor'] = minor
        mytmp['pa'] = pa
        mytmp['targetres'] = targetres
        mytmp['kimage'] = kimage
        mytmp['scale'] = scale
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['outfile'] = outfile
        mytmp['stretch'] = stretch
        mytmp['overwrite'] = overwrite
        mytmp['beam'] = beam
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'imsmooth.xml')

        casalog.origin('imsmooth')
        try :
          #if not trec.has_key('imsmooth') or not casac.casac.utils().verify(mytmp, trec['imsmooth']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['imsmooth'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('imsmooth', 'imsmooth.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'imsmooth'
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
          result = imsmooth(imagename, kernel, major, minor, pa, targetres, kimage, scale, region, box, chans, stokes, mask, outfile, stretch, overwrite, beam)

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
             tname = 'imsmooth'
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
#        paramgui.runTask('imsmooth', myf['_ip'])
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
        a['kernel']  = 'gauss'
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['outfile']  = ''
        a['overwrite']  = False

        a['kernel'] = {
                    0:odict([{'value':'gauss'}, {'beam':''}, {'targetres':False}, {'major':''}, {'minor':''}, {'pa':''}]), 
                    1:odict([{'value':'gaussian'}, {'beam':''}, {'targetres':False}, {'major':''}, {'minor':''}, {'pa':''}]), 
                    2:odict([{'value':'g'}, {'beam':''}, {'targetres':False}, {'major':''}, {'minor':''}, {'pa':''}]), 
                    3:odict([{'value':'box'}, {'major':''}, {'minor':''}]), 
                    4:odict([{'value':'boxcar'}, {'major':''}, {'minor':''}]), 
                    5:odict([{'value':'b'}, {'major':''}, {'minor':''}]), 
                    6:odict([{'value':'image'}, {'kimage':''}, {'scale':-1.0}]), 
                    7:odict([{'value':'i'}, {'kimage':''}, {'scale':-1.0}])}
        a['mask'] = {
                    0:odict([{'notvalue':''}, {'stretch':False}])}

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
    def description(self, key='imsmooth', subkey=None):
        desc={'imsmooth': 'Smooth an image or portion of an image',
               'imagename': 'Name of the input image. Must be specified.',
               'kernel': 'Type of kernel to use. Acceptable values are "b", "box", or "boxcar" for a boxcar kernel, "g", "gauss", or "gaussian" for a gaussian kernel, "c", "common", or "commonbeam" to use the common beam of an image with multiple beams as the gaussian to which to convolve all the planes, "i" or "image" to use an image as the kernel.',
               'major': 'Major axis for the kernels. Standard quantity representation. Must be specified for kernel="boxcar".',
               'minor': 'Minor axis. Standard quantity representation. Must be specified for kernel="boxcar".',
               'pa': 'Position angle used only for gaussian kernel. Standard quantity representation.',
               'targetres': 'If gaussian kernel, specified parameters are to be resolution of output image (True) or parameters of gaussian to convolve with input image (False).',
               'kimage': 'Kernel image name. Only used if kernel="i" or "image".',
               'scale': 'Scale factor. -1.0 means auto-scale. Only used if kernel="i" or "image".',
               'region': 'Region selection. Default is to use the full image.',
               'box': 'Rectangular region to select in direction plane. Default is to use the entire direction plane.',
               'chans': 'Channels to use. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Default is to use all Stokes planes.',
               'mask': 'Mask to use. Default is none.',
               'outfile': 'Output image name. Must be specified.',
               'stretch': 'If true, stretch the mask if necessary and possible.',
               'overwrite': 'If true, overwrite (unprompted) pre-existing output file.',
               'beam': 'Alternate way of describing a Gaussian. If specified, must be a dictionary with keys "major", "minor", and "pa" (or "positionangle"). Do not specify beam if specifying major, minor, and pa.',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['kernel']  = 'gauss'
        a['major']  = ''
        a['minor']  = ''
        a['pa']  = ''
        a['targetres']  = False
        a['kimage']  = ''
        a['scale']  = -1.0
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['outfile']  = ''
        a['stretch']  = False
        a['overwrite']  = False
        a['beam']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['kernel']  == 'gauss':
            a['beam'] = ''
            a['targetres'] = False
            a['major'] = ''
            a['minor'] = ''
            a['pa'] = ''

        if self.parameters['kernel']  == 'gaussian':
            a['beam'] = ''
            a['targetres'] = False
            a['major'] = ''
            a['minor'] = ''
            a['pa'] = ''

        if self.parameters['kernel']  == 'g':
            a['beam'] = ''
            a['targetres'] = False
            a['major'] = ''
            a['minor'] = ''
            a['pa'] = ''

        if self.parameters['kernel']  == 'box':
            a['major'] = ''
            a['minor'] = ''

        if self.parameters['kernel']  == 'boxcar':
            a['major'] = ''
            a['minor'] = ''

        if self.parameters['kernel']  == 'b':
            a['major'] = ''
            a['minor'] = ''

        if self.parameters['kernel']  == 'image':
            a['kimage'] = ''
            a['scale'] = -1.0

        if self.parameters['kernel']  == 'i':
            a['kimage'] = ''
            a['scale'] = -1.0

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if a.has_key(paramname) :
              return a[paramname]
imsmooth_cli = imsmooth_cli_()
