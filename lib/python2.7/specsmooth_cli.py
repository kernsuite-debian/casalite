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
from task_specsmooth import specsmooth
class specsmooth_cli_:
    __name__ = "specsmooth"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (specsmooth_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'outfile':None, 'box':None, 'chans':None, 'stokes':None, 'region':None, 'mask':None, 'overwrite':None, 'stretch':None, 'axis':None, 'function':None, 'width':None, 'dmethod':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, outfile=None, box=None, chans=None, stokes=None, region=None, mask=None, overwrite=None, stretch=None, axis=None, function=None, width=None, dmethod=None, ):

        """Smooth an image region in one dimension

        Detailed Description:


        Arguments :
                imagename: Name of the input image
                   Default Value: 

                outfile: Output image name.
                   Default Value: 

                box: Rectangular region to select in direction plane. Default is to use the entire direction plane.
                   Default Value: 

                chans: Channels to use. Channels must be contiguous. Default is to use all channels.
                   Default Value: 

                stokes: Stokes planes to use. Planes specified must be contiguous. Default is to use all Stokes planes.
                   Default Value: 

                region: Region selection. Default is to use the full image.
                   Default Value: 

                mask: Mask to use. Default is none..
                   Default Value: 

                overwrite: Overwrite the output if it exists?
                   Default Value: False

                stretch: Stretch the mask if necessary and possible? Default False
                   Default Value: False

                axis: The profile axis. Default: use the spectral axis if one exists, axis 0 otherwise (<0).
                   Default Value: -1

                function: Convolution function. hanning and boxcar are supported functions. Minimum match is supported.
                   Default Value: boxcar

                width: Width of boxcar, in pixels.
                   Default Value: 2

                dmethod: Decimation method. "" means no decimation, "copy" and "mean" are also supported (minimum match).
                   Default Value: copy

        Returns: record

        Example :

    
Smooth an image region in one dimension.

ARAMETER SUMMARY
imagename       Name of the input (CASA, FITS, MIRIAD) image
box             Rectangular region to select in direction plane. 
                Default is to use the entire direction plane. Only a single box may be specified.
chans           Channels to use. Channels must be contiguous.
                Default is to use all channels.
stokes          Stokes planes to use. Planes specified must be
                contiguous. Default is to use all Stokes planes.
region          Region selection. Default is to use the full image.
mask            Mask to use. Default is none.
overwrite       If the specified outfile already exists, overwrite it if True.
stretch         Stretch the input mask if necessary and possible? Only used if a mask is specified.
                
axis            Pixel axis along which to do the convolution <0 means use the spectral axis.
function        Convolution function to use. Supported values are "boxcar" and "hanning". Minimum
                match is supported.
width           Width of boxcar in pixels. Used only if function parameter minimally matches "boxcar".
dmethod         Plane decimation method. "" means no decimation should be performed. Other supported
                values are "copy" and "mean". Minimal match is supported. See below for details.

This application performs one dimensional convolution along a specified axis of an image
or selected region of an image. Hanning smoothing and boxcar smoothing are supported. 
Both float valued and complex valued images are supported. Masked pixel values are set to
zero prior to convolution. All nondefault pixel masks are ignored during
the calculation. The convolution is done in the image domain (i.e., not
with an FFT).

BOXCAR SMOOTHING

One dimensional boxcar convolution is defined by

z[i] = (y[i] + y[i+i] + ... + y[i+w])/w

where z[i] is the value at pixel i in the box car smoothed image, y[k]
is the pixel value of the input image at pixel k, and w is a postivie integer
representing the width of the boxcar in pixels.  The length of the axis along which the
convolution is to occur must be at least w pixels in the selected region,
unless decimation using the mean function is chosen in which case the axis
length must be at least 2*w (see below).

If dmethod="" (no decimation), the length of the output axis will be equal
to the length of the input axis - w + 1. The pixel mask, ORed with the OTF mask
if specified, is copied from the selected region of the input image to the
output image. Thus for example, if the selected region in the input image has
six planes along the convolution axis, if the specified boxcar width is 2,
and if the pixel values, which are all unmasked, on a slice along this axis
are [1, 2, 5, 10, 17, 26], then the corresponding output slice will be of
length five pixels and the output pixel values will be [1.5, 3.5, 7.5, 13.5, 21.5].

If dmethod="copy", the output image is the image calculated
if dmethod="", except that only every wth plane is kept. Both the pixel and mask
values of these planes are copied directly to the output image, without further
processing. Thus for example, if the selected region in the input image has six
planes along the convolution axis, the boxcar width is chosen to be 2, and if
the pixel values, which are all unmasked, on a slice along this axis are [1, 2,
5, 10, 17, 26], the corresponding output pixel values will be [1.5, 7.5, 21.5].

If dmethod="mean", first the image described in the dmethod=""
case is calculated. Then, the ith plane of the output image is calculated by
averaging the i*w to the (i+1)*w-1  planes of this intermediate image. Thus, for
example, if the selected region in the input image has six planes along the
convolution axis, the boxcar width is chosen to be 2, and if the pixel values,
which are all unmasked, on a slice along this axis are [1, 2, 5, 10, 17, 26],
then the corresponding output pixel values will be [2.5, 10.5]. Any pixels at the
end of the convolution axis of the intermediate image that do not fall into a complete bin of
width w are ignored. Masked values are taken into consideration when forming this
average, so if one of the values is masked, it is not used in the average. If at
least one of the values in the intermediate image bin is not masked, the
corresponding output pixel will not be masked.

HANNING SMOOTHING

Hanning convolution of one axis of an image is defined by

z[i] = 0.25*y[i-1] + 0.5*y[i] + 0.25*y[i+1]       (equation 1)

where z[i] is the value at pixel i in the hanning smoothed image, and
y[i-1], y[i], and y[i+1] are the values of the input image at pixels i-1,
i, and i+1 respectively. The length of the axis along which the convolution is
to occur must be at least three pixels in the selected region. 
    
If dmethod="" (no decimation of image planes), the length of the output axis will
be the same as that of the input axis. The output pixel values along the convolution
axis will be related to those of the input values according to equation 1, except
the first and last pixels. In that case, 
    
    z[0] = 0.5*(y[0] + y[1])
    
and,
    
    z[N-1] = 0.5*(y[N-2] + y[N-1])
    
where N is the number of pixels along the convolution aixs.
The pixel mask, ORed with the OTF mask if specified, is copied from the selected
region of the input image to the output image. Thus for example, if the selected
region in the input image has six planes along the convolution axis, and if the pixel
values, which are all unmasked, on a slice along this axis are [1, 2, 5, 10, 17, 26],
the corresponding output pixel values will be [1.5, 2.5, 5.5, 10.5, 17.5, 21.5].
    
If dmethod="copy", the output image is the image calculated if
dmethod="", except that only the odd-numbered planes are kept. Furthermore, if the
number of planes along the convolution axis in the selected region of the input image
is even, the last odd number plane is also discarded. Thus, if the selected region
has N pixels along the convolution axis in the input image, along the convolution
axis the output image will have (N-1)/2 planes if N is odd, or (N-2)/2 planes if N
is even. The pixel and mask values are copied directly, without further
processing. Thus for example, if the selected region in the input image has six planes
along the convolution axis, and if the pixel values, which are all unmasked, on a slice
along this axis are [1, 2, 5, 10, 17, 26], the corresponding output pixel values will be
[2.5, 10.5].

If dmethod="mean", first the image described in the dmethod="" case
is calculated. The first plane and last plane(s) of that image are then discarded as
described in the dmethod="copy" case. Then, the ith plane of the output
image is calculated by averaging the (2*i)th and (2*i + 1)th planes of the intermediate
image. Thus for example, if the selected region in the input image has six planes
along the convolution axis, and if the pixel values, which are all unmasked, on a slice
along this axis are [1, 2, 5, 10, 17, 26], the corresponding output pixel values will be
[4.0, 14.0]. Masked values are taken into consideration when forming this average, so if
one of the values is masked, it is not used in the average. If at least one of the values
in the input pair is not masked, the corresponding output pixel will not be masked.


EXAMPLES

# boxcar smooth the spectral axis by 3 pixels, say it's axis 2 and only
# write every other pixel
specsmooth(imagename="mynonsmoothed.im", outfile="myboxcarsmoothed.im",
axis=2, function="boxcar", dmethod="copy", width=3, overwrite=True)

# hanning smooth the spectral axis, say it's axis 2 and do not perform decimation
# of image planes
specsmooth(imagename="mynonsmoothed.im", outfile="myhanningsmoothed.im",
axis=2, dmethod=""," overwrite=True)

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'specsmooth'
        self.__globals__['taskname'] = 'specsmooth'
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
            myparams['box'] = box = self.parameters['box']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['region'] = region = self.parameters['region']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['stretch'] = stretch = self.parameters['stretch']
            myparams['axis'] = axis = self.parameters['axis']
            myparams['function'] = function = self.parameters['function']
            myparams['width'] = width = self.parameters['width']
            myparams['dmethod'] = dmethod = self.parameters['dmethod']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['region'] = region
        mytmp['mask'] = mask
        mytmp['overwrite'] = overwrite
        mytmp['stretch'] = stretch
        mytmp['axis'] = axis
        mytmp['function'] = function
        mytmp['width'] = width
        mytmp['dmethod'] = dmethod
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'specsmooth.xml')

        casalog.origin('specsmooth')
        try :
          #if not trec.has_key('specsmooth') or not casac.casac.utils().verify(mytmp, trec['specsmooth']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['specsmooth'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('specsmooth', 'specsmooth.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'specsmooth'
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
          result = specsmooth(imagename, outfile, box, chans, stokes, region, mask, overwrite, stretch, axis, function, width, dmethod)

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
             tname = 'specsmooth'
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
#        paramgui.runTask('specsmooth', myf['_ip'])
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
        a['outfile']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['region']  = ''
        a['mask']  = ''
        a['axis']  = -1
        a['function']  = 'boxcar'
        a['dmethod']  = 'copy'

        a['outfile'] = {
                    0:odict([{'notvalue':''}, {'overwrite':False}])}
        a['mask'] = {
                    0:odict([{'notvalue':''}, {'stretch':False}])}
        a['function'] = {
                    0:odict([{'notvalue':'hanning'}, {'width':2}])}

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
    def description(self, key='specsmooth', subkey=None):
        desc={'specsmooth': 'Smooth an image region in one dimension',
               'imagename': 'Name of the input image',
               'outfile': 'Output image name.',
               'box': 'Rectangular region to select in direction plane. Default is to use the entire direction plane.',
               'chans': 'Channels to use. Channels must be contiguous. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Planes specified must be contiguous. Default is to use all Stokes planes.',
               'region': 'Region selection. Default is to use the full image.',
               'mask': 'Mask to use. Default is none..',
               'overwrite': 'Overwrite the output if it exists?',
               'stretch': 'Stretch the mask if necessary and possible? Default False',
               'axis': 'The profile axis. Default: use the spectral axis if one exists, axis 0 otherwise (<0).',
               'function': 'Convolution function. hanning and boxcar are supported functions. Minimum match is supported.',
               'width': 'Width of boxcar, in pixels.',
               'dmethod': 'Decimation method. "" means no decimation, "copy" and "mean" are also supported (minimum match).',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['outfile']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['region']  = ''
        a['mask']  = ''
        a['overwrite']  = False
        a['stretch']  = False
        a['axis']  = -1
        a['function']  = 'boxcar'
        a['width']  = 2
        a['dmethod']  = 'copy'

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['outfile']  != '':
            a['overwrite'] = False

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if self.parameters['function']  != 'hanning':
            a['width'] = 2

        if a.has_key(paramname) :
              return a[paramname]
specsmooth_cli = specsmooth_cli_()
