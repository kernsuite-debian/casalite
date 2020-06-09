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
from task_imrebin import imrebin
class imrebin_cli_:
    __name__ = "imrebin"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (imrebin_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'outfile':None, 'factor':None, 'region':None, 'box':None, 'chans':None, 'stokes':None, 'mask':None, 'dropdeg':None, 'overwrite':None, 'stretch':None, 'crop':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, outfile=None, factor=None, region=None, box=None, chans=None, stokes=None, mask=None, dropdeg=None, overwrite=None, stretch=None, crop=None, ):

        """Rebin an image by the specified integer factors
        Arguments :
                imagename: Name of the input image
                   Default Value: 

                outfile: Output image name.
                   Default Value: 

                factor: Binning factors for each axis. Use imhead or ia.summary to determine axis ordering.
                   Default Value: 

                region: Region selection. Default is to use the full image.
                   Default Value: 

                box: Rectangular region to select in direction plane. Default is to use the entire direction plane.
                   Default Value: 

                chans: Channels to use. Default is to use all channels.
                   Default Value: 

                stokes: Stokes planes to use. Default is to use all Stokes planes. Stokes planes cannot be rebinned.
                   Default Value: 

                mask: Mask to use. Default is none.
                   Default Value: 

                dropdeg: Drop degenerate axes?
                   Default Value: False

                overwrite: Overwrite the output if it exists? Default False
                   Default Value: False

                stretch: Stretch the mask if necessary and possible? 
                   Default Value: False

                crop: Remove pixels from the end of an axis to be rebinned if there are not enough to form an integral bin?
                   Default Value: True

        Returns: bool

        Example :

PARAMETER SUMMARY
imagename        Name of the input (CASA, FITS, MIRIAD) image
outfile          Name of output CASA image. Must be specified.
factor           Array of binning factors for each axis, eg [2,3]. Use imhead or ia.summary()
                 to determine order of axes in your image.
region           Region selection. Default is to use the
                 full image.
box              Rectangular region to select in direction plane.  for
                 details. Default is to use the entire direction plane.
chans            Channels to use. Default is to use all channels.
stokes           Stokes planes to use. Default is to use all
                 Stokes planes. Stokes planes cannot be rebiined.
mask             Mask to use. Default is none.
dropdeg          Drop degenerate axes?
overwrite        Should the image of the same name as specified in outfile be overwritten?
                 If true, the file if it exists is automatically overwritten.
stretch          Stretch the input mask if necessary and possible. 
crop             Only considered if the length of the input axis is not an integral multiple of
                 the associated binning factor. If True, pixels at the end of the axis that do not
                 form a complete bin are not included in the binning. If False, the remaining extra
                 pixels are averaged to form the final bin along the axis.

DESCRIPTION

This application rebins the specified image by the specified integer binning
factors for each axis. It supports both float valued and complex valued images.
The corresponding output pixel value is the average of the
input pixel values. The output pixel will be masked False if there
were no good input pixels.  A polarization axis cannot be rebinned.

The binning factors array must contain at least one element and no more
elements than the number of input image axes. If the number of elements
specified is less than the number of image axes, then the remaining axes
not specified are not rebinned. All specified values must be positive. A
value of one indicates that no rebinning of the associated axis will occur.
Should this array contain any float values, they will be rounded to the next
lowest integer. Note that in many images with both frequency and polarization
axes, the polarization axis preceeds the frequency axis. If you wish to rebin
the frequency axis, it is recommended that you inspect your image with imhead
or ia.summary() to determine the axis ordering.

Binning starts from the origin pixel of the bounding box of the selected region or
the origin pixel of the input image if no region is specified. The value of crop
is used to determine how to handle cases where there are pixels
at the end of the axis that do not form a complete bin. If crop=True,
extra pixels at the end of the axis are discarded. If crop=False, the remaining
pixels are averaged into the final bin along that axis. Should the length
of the axis to be rebinned be an integral multiple of the associated binning
factor, the value of crop is irrelevant. 

A value of dropdeg=True will result in the output image not containing
axes that are degenerate in the specified region or in the input image if no
region is specified. Note that, however, the binning
factors array must still account for degenerate axes, and the binning
factor associated with a degenerate axis must always be 1.

EXAMPLE

# rebin the first two axes (normally the direction axes)
imrebin(imagename="my.im", outfile="rebinned.im", factor=[2,3])

# rebin the frequency axis, which is the fourth axis in this image
imrebin(imagename="my2.im", outfile="rebinned2.im", factor=[1,1,1,4])

    
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'imrebin'
        self.__globals__['taskname'] = 'imrebin'
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
            myparams['factor'] = factor = self.parameters['factor']
            myparams['region'] = region = self.parameters['region']
            myparams['box'] = box = self.parameters['box']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['dropdeg'] = dropdeg = self.parameters['dropdeg']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['stretch'] = stretch = self.parameters['stretch']
            myparams['crop'] = crop = self.parameters['crop']

        if type(factor)==int: factor=[factor]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['factor'] = factor
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['dropdeg'] = dropdeg
        mytmp['overwrite'] = overwrite
        mytmp['stretch'] = stretch
        mytmp['crop'] = crop
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'imrebin.xml')

        casalog.origin('imrebin')
        try :
          #if not trec.has_key('imrebin') or not casac.casac.utils().verify(mytmp, trec['imrebin']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['imrebin'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('imrebin', 'imrebin.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'imrebin'
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
          result = imrebin(imagename, outfile, factor, region, box, chans, stokes, mask, dropdeg, overwrite, stretch, crop)

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
             tname = 'imrebin'
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
#        paramgui.runTask('imrebin', myf['_ip'])
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
        a['factor']  = []
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['dropdeg']  = False
        a['overwrite']  = False
        a['crop']  = True

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
    def description(self, key='imrebin', subkey=None):
        desc={'imrebin': 'Rebin an image by the specified integer factors',
               'imagename': 'Name of the input image',
               'outfile': 'Output image name.',
               'factor': 'Binning factors for each axis. Use imhead or ia.summary to determine axis ordering.',
               'region': 'Region selection. Default is to use the full image.',
               'box': 'Rectangular region to select in direction plane. Default is to use the entire direction plane.',
               'chans': 'Channels to use. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Default is to use all Stokes planes. Stokes planes cannot be rebinned.',
               'mask': 'Mask to use. Default is none.',
               'dropdeg': 'Drop degenerate axes?',
               'overwrite': 'Overwrite the output if it exists? Default False',
               'stretch': 'Stretch the mask if necessary and possible? ',
               'crop': 'Remove pixels from the end of an axis to be rebinned if there are not enough to form an integral bin?',

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
        a['factor']  = []
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['dropdeg']  = False
        a['overwrite']  = False
        a['stretch']  = False
        a['crop']  = True

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if a.has_key(paramname) :
              return a[paramname]
imrebin_cli = imrebin_cli_()
