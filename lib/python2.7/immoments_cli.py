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
from task_immoments import immoments
class immoments_cli_:
    __name__ = "immoments"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (immoments_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'moments':None, 'axis':None, 'region':None, 'box':None, 'chans':None, 'stokes':None, 'mask':None, 'includepix':None, 'excludepix':None, 'outfile':None, 'stretch':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, moments=None, axis=None, region=None, box=None, chans=None, stokes=None, mask=None, includepix=None, excludepix=None, outfile=None, stretch=None, ):

        """Compute moments from an image

        Detailed Description:


        Arguments :
                imagename: Name of the input image
                   Default Value: 

                moments: List of moments you would like to compute
                   Default Value: 0

                axis: The momement axis: ra, dec, lat, long, spectral, or stokes
                   Default Value: spectral

                region: Region selection. Default is to use the full image.
                   Default Value: 

                box: Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.
                   Default Value: 

                chans: Channels to use. Default is to use all channels.
                   Default Value: 

                stokes: Stokes planes to use. Default is to use all Stokes planes.
                   Default Value: 

                mask: Mask to use. Default is none.
                   Default Value: 

                includepix: Range of pixel values to include
                   Default Value: -1

                excludepix: Range of pixel values to exclude
                   Default Value: -1

                outfile: Output image file name (or root for multiple moments) 
                   Default Value: 

                stretch: Stretch the mask if necessary and possible? 
                   Default Value: False

        Returns: bool

        Example :

        The spectral moment distributions at each pixel are
        determined.  See the cookbook and User Reference Manual for
        mathematical details.

        The main control of the calculation is given by parameter
        moments:
    
        moments=-1  - mean value of the spectrum
        moments=0   - integrated value of the spectrum
        moments=1   - intensity weighted coordinate;traditionally used to get 
                      'velocity fields'
        moments=2   - intensity weighted dispersion of the coordinate; traditionally
                      used to get "velocity dispersion"
        moments=3   - median of I
        moments=4   - median coordinate
        moments=5   - standard deviation about the mean of the spectrum
        moments=6   - root mean square of the spectrum
        moments=7   - absolute mean deviation of the spectrum
        moments=8   - maximum value of the spectrum
        moments=9   - coordinate of the maximum value of the spectrum
        moments=10  - minimum value of the spectrum
        moments=11  - coordinate of the minimum value of the spectrum

   Keyword arguments:
   imagename    Name of input image
                default: none; example: imagename="ngc5921_task.image"
   moments      List of moments you would like to compute
                default: 0 (integrated spectrum);example: moments=[0,1]
                see list above
   axis         The moment axis
                default: (spectral axis); example: axis=spec
                options: ra, dec, lattitude, longitude, spectral, stokes
   mask         Mask to use. Default is none.  
   stretch      Stretch the input mask if necessary and possible. See below.
   region       Region selection. Default
                is to use the full image.
    box         Rectangular region to select in direction plane. See
                Default is to use the entire direction plane.
                Example: box="10,10,50,50"
                box = "10,10,30,30,35,35,50,50" (two boxes)
    chans       Channels to use. Default is to use
                all channels.
                 
    stokes      Stokes planes to use. Default is to
                use all Stokes planes.
                Example: stokes="IQUV";  
                Example:stokes="I,Q"
    includepix  Range of pixel values to include
                default: [-1] (all pixels); example=[0.02,100.0]
    excludepix  Range of pixel values to exclude
                default: [-1] (don"t exclude pixels); example=[100.,200.]
    outfile     Output image file name (or root for multiple moments)
                default: "" (input+auto-determined suffix);example: outfile="source_moment"

    If stretch is true and if the number of mask dimensions is less than
    or equal to the number of image dimensions and some axes in the
    mask are degenerate while the corresponding axes in the image are not,
    the mask will be stetched in the degenerate axis dimensions. For example,
    if the input image has shape [100, 200, 10] and the input
    mask has shape [100, 200, 1] and stretch is true, the mask will be
    stretched along the third dimension to shape [100, 200, 10]. However if
    the mask is shape [100, 200, 2], stretching is not possible and an
    error will result.

        Example for finding the 1-momment, intensity-weighted
        coordinate, often used for finding velocity fields.
        immoments( axis="spec", imagename="myimage", moment=1, outfile="velocityfields" )

        Example finding the spectral mean, -1 moment, on a specified region
        of the image as defined by the box and stokes parameters
        taskname="immoments"
        default()
        imagename = "myimage"
        moment    =  -1

        axis      = "spec"
        stokes     = "I"
        box       = [55,12,97,32]
        go

        Example using a mask created with a second file to select the
        data used to calculate the 0-moments, integrated values.  In
        this case the mask is from the calibrated.im file and all values
        that have a value greater than 0.5 will be positive in the mask..
        immoments( "clean.image", axis="spec", mask="calibrated.im>0.5", outfile="mom_withmask.im" )
        
If an image has multiple (per-channel beams) and the moment axis is equal to the
spectral axis, each channel will be convolved with a beam that is equal to the beam
having the largest area in the beamset prior to moment determination.



        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'immoments'
        self.__globals__['taskname'] = 'immoments'
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
            myparams['moments'] = moments = self.parameters['moments']
            myparams['axis'] = axis = self.parameters['axis']
            myparams['region'] = region = self.parameters['region']
            myparams['box'] = box = self.parameters['box']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['includepix'] = includepix = self.parameters['includepix']
            myparams['excludepix'] = excludepix = self.parameters['excludepix']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['stretch'] = stretch = self.parameters['stretch']

        if type(moments)==int: moments=[moments]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['moments'] = moments
        mytmp['axis'] = axis
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['includepix'] = includepix
        mytmp['excludepix'] = excludepix
        mytmp['outfile'] = outfile
        mytmp['stretch'] = stretch
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'immoments.xml')

        casalog.origin('immoments')
        try :
          #if not trec.has_key('immoments') or not casac.casac.utils().verify(mytmp, trec['immoments']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['immoments'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('immoments', 'immoments.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'immoments'
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
          result = immoments(imagename, moments, axis, region, box, chans, stokes, mask, includepix, excludepix, outfile, stretch)

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
             tname = 'immoments'
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
#        paramgui.runTask('immoments', myf['_ip'])
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
        a['moments']  = [0]
        a['axis']  = 'spectral'
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['includepix']  = -1
        a['excludepix']  = -1
        a['outfile']  = ''

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
    def description(self, key='immoments', subkey=None):
        desc={'immoments': 'Compute moments from an image',
               'imagename': 'Name of the input image',
               'moments': 'List of moments you would like to compute',
               'axis': 'The momement axis: ra, dec, lat, long, spectral, or stokes',
               'region': 'Region selection. Default is to use the full image.',
               'box': 'Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.',
               'chans': 'Channels to use. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Default is to use all Stokes planes.',
               'mask': 'Mask to use. Default is none.',
               'includepix': 'Range of pixel values to include',
               'excludepix': 'Range of pixel values to exclude',
               'outfile': 'Output image file name (or root for multiple moments) ',
               'stretch': 'Stretch the mask if necessary and possible? ',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['moments']  = [0]
        a['axis']  = 'spectral'
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['includepix']  = -1
        a['excludepix']  = -1
        a['outfile']  = ''
        a['stretch']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if a.has_key(paramname) :
              return a[paramname]
immoments_cli = immoments_cli_()
