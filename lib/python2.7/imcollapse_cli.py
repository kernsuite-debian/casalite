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
from task_imcollapse import imcollapse
class imcollapse_cli_:
    __name__ = "imcollapse"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (imcollapse_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'function':None, 'axes':None, 'outfile':None, 'box':None, 'region':None, 'chans':None, 'stokes':None, 'mask':None, 'overwrite':None, 'stretch':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, function=None, axes=None, outfile=None, box=None, region=None, chans=None, stokes=None, mask=None, overwrite=None, stretch=None, ):

        """Collapse image along one axis, aggregating pixel values along that axis.

        Detailed Description:

This task collapses an image along a specified axis or set of axes of
N pixels to a single pixel on each specified axis. Both float valued
and complex valued images are supported. It computes the specified
aggregate function for pixel values along the specified axes and
places those values in the single remaining plane of those axes in the
output image. 

The reference pixel of the collapsed axis is set to 0 and its
reference value is set to the mean of the the first and last values of
that axis in the specified region of the input image. Convolution to a
common beam is not performed automatically as part of the
preprocessing before the collapse operation occurs. Therefore, if the
input image has per-plane beams, then the user should consider first
smoothing the data to have the same resolution, and use the resulting
image as the input for imcollapse.

        Arguments :
                imagename: Name of the input image
                     Default: none

                        Example: imagename='ngc5921.im' 

                   Default Value: 

                function: Function used to compute aggregation of pixel values
along the collapsed axis.
                     Default: none
                     Options: flux, madm, max, mean, median, min,
                     npts, rms, stddev, sum, variance, xmadm

                     Minimum match is supported for the function
                     parameter (eg, function="r" will compute the rms
                     of the pixel values).

                     If one specifies function='flux', the following
                     constraints must be true:
                     1. The image must have a direction coordinate,
                     2. The image must have at least one beam,
                     3. The specified axes must be exactly the
                     direction coordinate axes,
                     4. Only one of the non-directional axes may be
                     non-degenerate,
                     5. The iamge brightness unit must be conformant
                     with x*yJy/beam, where x is an optional unit
                     (such as km/s for moments images) and y is an
                     optional SI prefix.

                   Default Value: 

                axes: Zero-based axis number(s) or minimal match strings to
collapse.
                     Default: [0]
                     Axes can be specified as a single integer or
                     array of integers indicating the zero-based axes
                     along which to collapse the image. Axes may also
                     be specified as a single or array of strings
                     which minimally and uniquely match (ignoring
                     case) world axes names in the image (eg "dec" or
                     ["ri, "d"] for collapsing along the declination
                     axis or along the right ascension and declination
                     axes, respectively).

                   Default Value: [0]

                outfile: Name of output CASA image. Must be specified.
                     Default: none

                        Example: outfile='collapsed.im'

                   Default Value: 

                box: Rectangular region to select in direction plane. 
                     Default: '' (use the entire direction plane)

                        Example: box="100,100,200,200"

                   Default Value: 

                region: Region selection.
                     Default: '' (use the full image)

                   Default Value: 

                chans: Channels to use. 
                     Default: '' (use all channels)

                   Default Value: 

                stokes: Stokes planes to use.
                     Default: '' (use all stokes planes)

                   Default Value: 

                mask: Mask to use.
                     Default: none

                   Default Value: 

                overwrite: Overwrite output image if it exists?
                     Default: False
                     Options: False|True

                   Default Value: False

                stretch: Stretch the mask if necessary and possible? 
                     Default: False
                     Options: False|True

                     Stretch the input mask if necessary and
                     possible. Only used if a mask is specified.

                   Default Value: False

        Returns: bool

        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF IMCOLLAPSE IN CASA DOCS:
https://casa.nrao.edu/casadocs/

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'imcollapse'
        self.__globals__['taskname'] = 'imcollapse'
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
            myparams['function'] = function = self.parameters['function']
            myparams['axes'] = axes = self.parameters['axes']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['box'] = box = self.parameters['box']
            myparams['region'] = region = self.parameters['region']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['stretch'] = stretch = self.parameters['stretch']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['function'] = function
        mytmp['axes'] = axes
        mytmp['outfile'] = outfile
        mytmp['box'] = box
        mytmp['region'] = region
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['overwrite'] = overwrite
        mytmp['stretch'] = stretch
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'imcollapse.xml')

        casalog.origin('imcollapse')
        try :
          #if not trec.has_key('imcollapse') or not casac.casac.utils().verify(mytmp, trec['imcollapse']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['imcollapse'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('imcollapse', 'imcollapse.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'imcollapse'
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
          result = imcollapse(imagename, function, axes, outfile, box, region, chans, stokes, mask, overwrite, stretch)

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
             tname = 'imcollapse'
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
#        paramgui.runTask('imcollapse', myf['_ip'])
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
        a['function']  = ''
        a['axes']  = [0]
        a['outfile']  = ''
        a['box']  = ''
        a['region']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['stretch']  = False

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
    def description(self, key='imcollapse', subkey=None):
        desc={'imcollapse': 'Collapse image along one axis, aggregating pixel values along that axis.',
               'imagename': 'Name of the input image',
               'function': 'Aggregate function to apply. This can be set one of flux, madm, max, mean, median, min, npts, rms, stddev, sum, variance, xmadm. Must be specified.',
               'axes': 'Zero-based axis number(s) or minimal match strings to collapse.',
               'outfile': 'Name of output CASA image. Must be specified.',
               'box': 'Rectangular region to select in direction plane. Default is to use the entire direction plane.',
               'region': 'Region selection. Default is to use the full image.',
               'chans': 'Channels to use. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Default is to use all Stokes planes.',
               'mask': 'Mask to use. Default is none.',
               'overwrite': 'Overwrite output image if it exists?',
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
        a['function']  = ''
        a['axes']  = [0]
        a['outfile']  = ''
        a['box']  = ''
        a['region']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['overwrite']  = False
        a['stretch']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['outfile']  != '':
            a['overwrite'] = False

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if a.has_key(paramname) :
              return a[paramname]
imcollapse_cli = imcollapse_cli_()
