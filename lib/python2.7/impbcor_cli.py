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
from task_impbcor import impbcor
class impbcor_cli_:
    __name__ = "impbcor"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (impbcor_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'pbimage':None, 'outfile':None, 'overwrite':None, 'box':None, 'region':None, 'chans':None, 'stokes':None, 'mask':None, 'mode':None, 'cutoff':None, 'stretch':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, pbimage=None, outfile=None, overwrite=None, box=None, region=None, chans=None, stokes=None, mask=None, mode=None, cutoff=None, stretch=None, ):

        """Construct a primary beam corrected image from an image and a primary beam pattern.

        Detailed Description:

Correct an image for primary beam attenuation using an image of the
primary beam pattern. The primary beam pattern can be provided as an
image, in which case 1. it must have the same shape as the input image
and its coordinate system must be the same, or 2. it must be a 2-D
image in which case its coordinate system must consist of a (2-D)
direction coordinate which is the same as the direction coordinate in
the input image and its direction plane must be the same shape as that
of the input image. Alternatively, pbimage can be an array of pixel
values in which case the same dimensionality and shape constraints
apply.

One can choose between dividing the image by the primary beam pattern
(mode="divide") or multiplying the image by the primary beam pattern
(mode="multiply"). One can also choose to specify a cutoff limit for
the primary beam pattern. For mode="divide", for all pixels below this
cutoff in the primary beam pattern, the output image will be
masked. In the case of mode="multiply", all pixels in the output will
be masked corresponding to pixels with values greater than the cutoff
in the primary beam pattern. A negative value for cutoff means that no
cutoff will be applied, which is the default.

        Arguments :
                imagename: Name of the input (CASA, FITS, MIRIAD) image

                   Default Value: 

                pbimage: Name of the image (CASA, FITS, MIRIAD) of the primary
beam pattern or an array of pixel values.
                     Default: ''

                   Default Value: ""

                outfile: Name of output CASA image. 
                     Default: none. Must be specified.

                   Default Value: 

                overwrite: If output file is specified, controls if an already
existing file by the same name can be overwritten. 
                     Default: True
                     Options: True|False

                     If true, the user is not prompted, the file if it
                     exists is automatically overwritten.

                   Default Value: False

                box: Rectangular region to select in direction plane.
                     Default: '' (use the entire direction plane)

                   Default Value: 

                region: Region selection. 
                     Default: '' (use the full image)

                   Default Value: 

                chans: Channels to use. 
                     Default: '' (use all channels)

                   Default Value: 

                stokes: Stokes planes to use.
                     Default: '' (use all Stokes planes)

                   Default Value: 

                mask: Mask to use.
                     Default: none

                   Default Value: 

                mode: Divide or multiply the image by the primary beam image. 
                     Default: 'divide'

                     Minimal match supported.

                   Default Value: divide

                cutoff: Primary beam cutoff.
                     Default: -1.0 (no cutoff)

                     If mode is "d", all values less than this will be
                     masked. If "m", all values greater will be
                     masked. Less than 0, no cutoff (default)

                   Default Value: -1.0

                stretch: Stretch the mask if necessary and possible? 
                     Default: False
                     Options: False|True

                   Default Value: False

        Returns: bool

        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPBCOR IN CASA DOCS:
https://casa.nrao.edu/casadocs/
    
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'impbcor'
        self.__globals__['taskname'] = 'impbcor'
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
            myparams['pbimage'] = pbimage = self.parameters['pbimage']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['box'] = box = self.parameters['box']
            myparams['region'] = region = self.parameters['region']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['mode'] = mode = self.parameters['mode']
            myparams['cutoff'] = cutoff = self.parameters['cutoff']
            myparams['stretch'] = stretch = self.parameters['stretch']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['pbimage'] = pbimage
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        mytmp['box'] = box
        mytmp['region'] = region
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['mode'] = mode
        mytmp['cutoff'] = cutoff
        mytmp['stretch'] = stretch
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'impbcor.xml')

        casalog.origin('impbcor')
        try :
          #if not trec.has_key('impbcor') or not casac.casac.utils().verify(mytmp, trec['impbcor']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['impbcor'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('impbcor', 'impbcor.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'impbcor'
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
          result = impbcor(imagename, pbimage, outfile, overwrite, box, region, chans, stokes, mask, mode, cutoff, stretch)

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
             tname = 'impbcor'
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
#        paramgui.runTask('impbcor', myf['_ip'])
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
        a['pbimage']  = ""
        a['outfile']  = ''
        a['box']  = ''
        a['region']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['mode']  = 'divide'
        a['cutoff']  = -1.0

        a['outfile'] = {
                    0:odict([{'notvalue':''}, {'overwrite':False}])}
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
    def description(self, key='impbcor', subkey=None):
        desc={'impbcor': 'Construct a primary beam corrected image from an image and a primary beam pattern.',
               'imagename': 'Name of the input image',
               'pbimage': 'Name of the primary beam image which must exist or array of values for the pb response.',
               'outfile': 'Output image name. If empty, no image is written.',
               'overwrite': 'Overwrite the output if it exists?',
               'box': 'Rectangular region to select in direction plane. Default is to use the entire direction plane.',
               'region': 'Region selection.',
               'chans': 'Channels to use.',
               'stokes': 'Stokes planes to use.',
               'mask': 'Mask to use.',
               'mode': 'Divide or multiply the image by the primary beam image. Minimal match supported.',
               'cutoff': 'PB cutoff. If mode is "d", all values less than this will be masked. If "m", all values greater will be masked. Less than 0, no cutoff.',
               'stretch': 'Stretch the mask if necessary and possible?',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['pbimage']  = ""
        a['outfile']  = ''
        a['overwrite']  = False
        a['box']  = ''
        a['region']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['mode']  = 'divide'
        a['cutoff']  = -1.0
        a['stretch']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['outfile']  != '':
            a['overwrite'] = False

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if a.has_key(paramname) :
              return a[paramname]
impbcor_cli = impbcor_cli_()
