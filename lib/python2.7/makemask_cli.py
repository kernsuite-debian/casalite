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
from task_makemask import makemask
class makemask_cli_:
    __name__ = "makemask"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (makemask_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'mode':None, 'inpimage':None, 'inpmask':None, 'output':None, 'overwrite':None, 'inpfreqs':None, 'outfreqs':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, mode=None, inpimage=None, inpmask=None, output=None, overwrite=None, inpfreqs=None, outfreqs=None, ):

        """Makes and manipulates image masks

        Detailed Description:
Construct masks based on various criteria, convert between mask-types, and generate a mask for clean
        Arguments :
                mode: Mask method (list, copy,expand,delete,setdefaultmask)
                   Default Value: list
                   Allowed Values:
                                list
                                copy
                                expand
                                delete
                                setdefaultmask

                inpimage: Name of input image.
                   Default Value: 

                inpmask: mask(s) to be processed: image masks,T/F internal masks(Need to include parent image names),regions(for copy mode)
                   Default Value: 

                output: Name of output mask (imagename or imagename:internal_maskname)
                   Default Value: 

                overwrite: overwrite output if exists?
                   Default Value: False

                inpfreqs: List of chans/freqs (in inpmask) to read masks from 
                   Default Value: 

                outfreqs: List of chans/freqs (in output) on which to expand the mask
                   Default Value: 

        Returns: void

        Example :


Modes :
-------------

list : list internal masks in inpimage to the log
copy :  Copy/merge masks and regrid if necessary to a new or existing mask
expand : Expand a mask from one range of freqs to another range
delete : delete an internal mask from an image (if the deleted mask was a default mask,
         the task chooses the first one in the remaining internal mask list (as appears
         in the log when do listing with mode='list')
setdefaultmask : set a specified internal mask as a default internal mask




In all cases (for output mask is expected), if the output image has a different coordinate system from the
result of input and processing, the mask will be re-gridded to the output
coordinate system.


Parameter Descriptions and rules:
------------------------------
inpimage : Name of input image to use as a reference for the output coordinates (if output does not exist).
           Also used as a reference image when regions are specified in inpmask for copy mode
           If output is a new image specified with an internal T/F mask, the pixel values in the input image
           are copied to the output image and the regions specified in inpmask are merged (if mutliple regions
           specified) and treated as a valid region therefore will be UNMASKED in output.
           default: none (must specify for list, copy, expand modes)

Expandable parameters for mode='copy','expand','delete' and 'setdefaultmask':
inpmask : Name(s) of input mask(s)
          default: none
         To specify an image (zero/non-zero) mask, just give a image name (e.g. myimage1.im)
         To specify an internal (T/F) mask, you must give a parent image name and the internal mask name
         separated by a colon. (e.g. myimage1.im:mask0). The internal mask names can be found by running
         the makemask task in mode='list'.

         (expand mode)
         'myimage:mask0' : use(true/false) internal mask
         'myimage'  : use the inpimage values to make a mask (zero/non-zero).
                      Non-zero values are normalized to one in the process.
         (copy mode)
         Specify the image mask(s), T/F mask(s), and region(s) to be merged in a list of strings.
         The regions can be specified directly in the CASA region format or in the text file(s) contains
         the regions.

         (delete and setdefaultmask mode)
         Specify the internal mask with the format, image:mask


output : Name of output image.
         default: none
         *The resultant mask is written as an image (zero/one) mask if the output is a plain image name
         *The resultant mask is written as an internal (T/F) mask if the output name is the form of 'imagename:maskname'
          The created mask is set as a default internal mask.
         *To re-grid a mask to a different coordinate system,
          give an image with the target coordinate system in inpimage. Or make a copy an image
          with the target coordinate system and specified the name of the copy in output.


    - If output is specified as a plain image, if it exists, it will regrid the mask to
      the new coordinate system  and modify output (if overwrite=True).
    - If output is specified as an image with an internal mask, if the internal mask exists,
      it will regrid the mask to the new coordinate system  and modify the internal mask only (if overwrite=True).
    - If output does not exist, it will only copy inpimage.
    - If output == inpimage, do not regrid. Only modify in-place.

    *** Please note that the term 'mask' is used in the image analysis and clean tasks in opposite
        sense. In the image analysis, the masked region in general a region to be excluded while
        clean's input mask defines the region to be used as a clean box/region.
        In the makemask task, since the most common use case of output image mask is to use as
        an input mask in clean, when it converts an internal mask to the image mask,
        the 'masked' region (where the pixels are masked and have the Boolean values 'False')
        of the internal mask is translated to the pixels with value of 0 in output image mask.

overwrite : overwrite the mask specified in output? (see also the output rules above)
            default: False
            * Note that for a cube mask, overwrite=True generally overwrites in the specified channel planes only and
            so any pre-existed masks in other channels  will be remain untouched.

Additional expandable parameters for mode='expand':
  inpfreqs : input channel/frequency/velocity range
             Specify channels in a list of integers. for frequency/velocity,
             a range is specified in a string with '~', e.g. '1.5MHz~1.6MHz', '-8km/s~-14km/s'
             (for the cube with ascending frequencies)
             default: []  - all channels
             * Note that the range in frequency or velocity needs to be specified as the same order
             as in the template cube specified in inpimage. E.g., if a template cube has descending
             frequencies, then the range will be, for example,'1.6MHz~1.5MHz' or '-14km/s~-8km/s'

  outfreqs : output channel/frequency/velocity range
             Specify same way as inpfreqs
             default: []  - all channels


Usage examples :
---------------------------
(1) (list mode):
     makemask(mode='list', inpimage='mymask.im')
     it prints out a list of the internal mask(s) exist in mymask.im to the log

(2) (copy mode):
     Regrid a Boolean mask from one coordinate system to another and save as Boolean mask
     in the output image.

     makemask(mode='copy', inpimage='oldmask.im', inpmask='oldmask.im:mask0', output='newmask.im:mask0')

(3) (copy mode):
     Same as (1), but save as integer mask in the output image.

     makemask(mode='copy', inpimage='oldmask.im', inpmask='oldmask.im:mask0', output='newmask.im')

     * mask0 is translated so that pixels in oldmask.im that appears as 'masked' in the viewer or
       has the pixel mask value = 'False' when extracted in imval, are to have pixel value of 1 in
       the output image, newmask.im.

(4) (copy mode):
     Convert a Boolean(true/false) mask to an integer(one/zero) mask in the same image

     makemask(mode='copy', inpimage='oldmask.im', inpmask='oldmask.im:mask0', output='', overwrite=True)


(5) (copy mode):
     Convert an integer(one/zero) mask to a Boolean(true/false) mask in the same image

     makemask(mode='copy', inpimage='oldmask.im', inpmask='oldmask.im', output='oldmask.im:mask0')

(6) (copy mode):
     Copy a CRTF mask defined in mybox.txt to a Boolean(true/false) mask in a new image

     makemask(mode='copy', inpimage='image1.im', inpmask='mybox.txt', output='image2.im:mask0')

     The pixel values of image1.im will be copied to image2.im and the region outside mybox.txt
     will be masked.

(7) (copy mode):
     Apply a region defined in a CRTF file to mask part of an image

     makemask(mode='copy', inpimage='image1.im', inpmask='myregion.crtf', output='image1.im:mask0')

     The region is copied as a T/F mask (mask0) inside the image, image1.im. The region outside myregion.crtf
     will be masked.


(8) (copy mode):

     Merge a (one/zero) mask and  T/F masks, using the input coordinate-sys of inpimage and
     saving in a new output file. Remember, if the image specified in output already exist and
     has a different coordinate system from inpimage, the mask will be regridded to it.
     All masks to be merged are specified in a list in inpmask.
     The name of internal masks must be given in the format, 'parent_image_name:internal_mask_name',
     as shown the example below.

     In the example below, image1.im (the 1/0 mask), the internal masks, mask0 from image1.im
     and mask1 from image2.im, and a region (on image1.im as defined in inpimage)  are combined.
     The output, newmask.im is a new mask name which has not
     yet exist so image specified in inpimage, image1.im's coordinates are used as a target
     image coordinates. If image1.im and image2.im has different coordinates, image2.im:mask1 is
     regridded before it is combined to the other two masks.

     makemask(mode='copy',
              inpimage='image1.im', 
              inpmask=['image1.im', image1.im:mask0','image2.mask:mask1', 'circle[[15pix , 15pix] ,8pix ]'],
              output='newmask.im);

(9) (expand mode):
     Expand a (one/zero) mask from continuum imaging to use as an input mask image for
     spectral line imaging. Use an existing spectral line clean image as a template by
     specified in inpimage.
     The inpfreqs is left out as it uses a default (=[], means all channels).

     makemask(mode='expand', inpimage='spec.clean.image', inpmask='cont.clean.mask'
              outfreqs=[4,5,6,7], output='spec.clean.mask')

(10) (expand mode):
     Expand a Boolean mask from one range of channels to another range
     in the same image.

     makemask(mode='expand', inpimage='oldmask.im', inpmask='oldmask.im:mask0', inpfreqs=[5,6], outfreqs=[4,5,6,7],
              output='oldmask.im:mask0', overwrite=True)


(11) (expand mode):
     Expand a Boolean mask from a range of channels in the input image to another range
     of channels in a different image with a different spectral-coordinate system.
     Save the mask as ones/zeros so that it can be used as an input mask in the clean task.
     As the inpimage is used as a template for the CoordinateSystem of the output cube, it is
     a prerequisite to have the cube image (a dirty image, etc). In this particular example,
     it is assumed that bigmask.im is a working copy made from the cube image of a previous clean
     execution. It is used as an input template and the resultant mask is overwritten to the same image.

     Specify the infreqs and outfreqs in frequency (assuming here bigmask.im has frequencies in ascending order)
     makemask(mode='expand', inpimage='bigmask.im', inpmask='smallmask.im:mask0',
              inpfreqs='1.5MHz~1.6MHz', outfreqs='1.2MHz~1.8MHz', output='bigmask.im', overwrite=True)

     or to specify the ranges in velocities,
     makemask(mode='expand', inpimage='bigmask.im', inpmask='smallmask.im:mask0',
              inpfreqs=4.0km/s~0.5km/s', outfreqs='6.5km/s~-2.4km/s', output='bigmask.im', overwrite=True)


(12) (delete mode)
      Delete an internal mask from an image.

      makemask(mode='delete', inpmask='newmask.im:mask0')

(13) (setdefaultmask mode)
      Set an internal mask as a default internal mask.

      makemask(mode='setdefaultmask', inpmask='newmask.im:mask1')





  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'makemask'
        self.__globals__['taskname'] = 'makemask'
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

            myparams['mode'] = mode = self.parameters['mode']
            myparams['inpimage'] = inpimage = self.parameters['inpimage']
            myparams['inpmask'] = inpmask = self.parameters['inpmask']
            myparams['output'] = output = self.parameters['output']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['inpfreqs'] = inpfreqs = self.parameters['inpfreqs']
            myparams['outfreqs'] = outfreqs = self.parameters['outfreqs']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['mode'] = mode
        mytmp['inpimage'] = inpimage
        mytmp['inpmask'] = inpmask
        mytmp['output'] = output
        mytmp['overwrite'] = overwrite
        mytmp['inpfreqs'] = inpfreqs
        mytmp['outfreqs'] = outfreqs
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'makemask.xml')

        casalog.origin('makemask')
        try :
          #if not trec.has_key('makemask') or not casac.casac.utils().verify(mytmp, trec['makemask']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['makemask'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('makemask', 'makemask.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'makemask'
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
          result = makemask(mode, inpimage, inpmask, output, overwrite, inpfreqs, outfreqs)

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
             tname = 'makemask'
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
#        paramgui.runTask('makemask', myf['_ip'])
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
        a['mode']  = 'list'

        a['mode'] = {
                    0:odict([{'value':'list'}, {'inpimage':''}]), 
                    1:odict([{'value':'copy'}, {'inpimage':''}, {'inpmask':''}, {'output':''}, {'overwrite':False}]), 
                    2:odict([{'value':'expand'}, {'inpimage':''}, {'inpmask':''}, {'inpfreqs':[]}, {'outfreqs':[]}, {'output':''}, {'overwrite':False}]), 
                    3:odict([{'value':'delete'}, {'inpmask':''}]), 
                    4:odict([{'value':'setdefaultmask'}, {'inpmask':''}])}

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
    def description(self, key='makemask', subkey=None):
        desc={'makemask': 'Makes and manipulates image masks',
               'mode': 'Mask method (list, copy,expand,delete,setdefaultmask)',
               'inpimage': 'Name of input image.',
               'inpmask': 'mask(s) to be processed: image masks,T/F internal masks(Need to include parent image names),regions(for copy mode)',
               'output': 'Name of output mask (imagename or imagename:internal_maskname)',
               'overwrite': 'overwrite output if exists?',
               'inpfreqs': 'List of chans/freqs (in inpmask) to read masks from ',
               'outfreqs': 'List of chans/freqs (in output) on which to expand the mask',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['mode']  = 'list'
        a['inpimage']  = ''
        a['inpmask']  = ''
        a['output']  = ''
        a['overwrite']  = False
        a['inpfreqs']  = []
        a['outfreqs']  = []

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mode']  == 'list':
            a['inpimage'] = ''

        if self.parameters['mode']  == 'copy':
            a['inpimage'] = ''
            a['inpmask'] = ''
            a['output'] = ''
            a['overwrite'] = False

        if self.parameters['mode']  == 'expand':
            a['inpimage'] = ''
            a['inpmask'] = ''
            a['inpfreqs'] = []
            a['outfreqs'] = []
            a['output'] = ''
            a['overwrite'] = False

        if self.parameters['mode']  == 'delete':
            a['inpmask'] = ''

        if self.parameters['mode']  == 'setdefaultmask':
            a['inpmask'] = ''

        if a.has_key(paramname) :
              return a[paramname]
makemask_cli = makemask_cli_()
