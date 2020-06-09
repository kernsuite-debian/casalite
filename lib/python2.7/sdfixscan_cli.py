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
from task_sdfixscan import sdfixscan
class sdfixscan_cli_:
    __name__ = "sdfixscan"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (sdfixscan_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'infiles':None, 'mode':None, 'numpoly':None, 'beamsize':None, 'smoothsize':None, 'direction':None, 'maskwidth':None, 'tmax':None, 'tmin':None, 'outfile':None, 'overwrite':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, infiles=None, mode=None, numpoly=None, beamsize=None, smoothsize=None, direction=None, maskwidth=None, tmax=None, tmin=None, outfile=None, overwrite=None, ):

        """Task for single-dish image processing

        Detailed Description:

Task sdfixscan is used to remove a scanning noise that appears 
as a striped noise pattern along the scan direction in a raster 
scan data. 

By default, the scanning noise is removed by using the 
FFT-based 'Basket-Weaving' method (Emerson \&amp; Grave 1988) that
requires multiple images that observed exactly the same area with
different scanning direction. If only one image is available, the
'Pressed-out' method (Sofue \&amp; Reich 1979) can be used to remove
the scanning effect.
  
        Arguments :
                infiles: list of name of input SD images (FITS or CASA image)
                   Default Value: ''

                mode: image processing mode
                   Default Value: fft_mask
                   Allowed Values:
                                fft_mask
                                model

                numpoly: order of polynomial fit for Pressed-out method
                   Default Value: 2

                beamsize: beam size for Pressed-out method
                   Default Value: 0.0

                smoothsize: size of smoothing beam for Pressed-out method
                   Default Value: 2.0

                direction: scan direction (p.a.) counterclockwise from the horizontal axis in unit of degree
                   Default Value: 

                maskwidth: mask width for Basket-Weaving (on percentage)
                   Default Value: 1.0

                tmax: maximum threshold value for processing
                   Default Value: 0.0

                tmin: minimum threshold value for processing
                   Default Value: 0.0

                outfile: name of output file
                   Default Value: 

                overwrite: overwrite the output file if already exists
                   Default Value: False

        Returns: void

        Example :

-----------------    
Keyword arguments
-----------------
infiles -- name or list of names of input SD (FITS or CASA) image(s)
mode -- image processing mode
        options: 'fft_mask' (FFT-based Basket-Weaving),
                 'model' (Pressed-out method)
        default: 'fft_mask'
    >>>mode expandable parameter
        direction -- scan direction (p.a.) counterclockwise from the 
                     horizontal axis in unit of degree.
                default: []
                example: direction=[0.0, 90.0] means that the first image
                         has scan direction along longitude axis while the
                         second image is along latitude axis.
        maskwidth -- mask width for Basket-Weaving on percentage
                default: 1.0 (1.0% of map size)
        numpoly -- order of polynomial fit in Presssed-out method
                default: 2
        beamsize -- beam size for Pressed-out method 
                default: 0.0
                example: beamsize=10.0 is interpreted as '10arcsec'.
                         beamsize='1arcmin' specifies beam size as
                         quantity.
        smoothsize -- smoothing beam size in Pressed-out method.
                      if numeric value is given, it is interpreted in unit
                      of beam size specified by the parameter beamsize
                default: 2.0 
                example: smoothsize=2.0 means that smoothing beam size is
                         2.0 * beamsize.
                         smoothsize='1arcmin' sets smoothsize directly.
tmax -- maximum threshold value for processing
        default: 0.0 (no threshold in maximum)
        example: 10.0 (mask data larger value than 10.0)
tmin -- minimum threshold value for processing
        default: 0.0 (no threshold in minimum)
        example: -10.0 (mask data smaller value than -10.0)
outfile -- name of output file. output file is in CASA image format.
        default: '' (use default name 'sdfixscan.out.im')
        example: 'output.im'
overwrite -- overwrite the output file if already exists
        options: (bool) True, False
        default: False

-----------
DESCRIPTION
-----------
Task sdfixscan is used to remove a scanning noise that appears 
as a striped noise pattern along the scan direction in a raster 
scan data. 

By default, the scanning noise is removed by using the FFT-based 
'Basket-Weaving' method (Emerson \& Grave 1988) that requires 
multiple images that observed exactly the same area with different 
scanning direction. If only one image is available, the 'Pressed-out' 
method (Sofue \& Reich 1979) can be used to remove the scanning 
effect.

For 'Basket-Weaving', scanning directions must have at least two 
different values. Normally, the scanning direction should be 
specified for each input image. Otherwise, specified scanning 
directions will be used iteratively. The maskwidth is a width of 
masking region in the Fourier plane. It is specified as a fraction 
(percentage) of the image size. 

For 'Pressed-out', the scanning direction must be unique. There are 
two ways to specify a size of smoothing beam used for process. One 
is to specify smoothing size directly. To do this, smoothsize should 
be specified as string that consists of a numerical value and an unit 
(e.g. '10.0arcsec'). A value of beamsize will be ignored in this case. 
Another way to specify smoothing size is to set an observed beam size 
and indicate smoothing size as a scale factor of the observed beam 
size. In this case, the beamsize is interpreted as the observed beam 
size, and the smoothsize is the scale factor. If the beamsize is 
provided as float value, its unit is assumed to 'arcsec'. It is also 
possible to set the beamsize as string consisting of the numerical 
value and the unit. The smoothsize must be float value.

The infiles only allows an image data (CASA or FITS), and does not 
work with MS or Scantable. The direction is an angle with respect to 
the horizontal direction, and its unit is degree. Any value may be 
interpreted properly, but the value ranging from 0.0 to 180.0 will 
be secure. The tmax and the tmin is used to specify a threshold that 
defines a range of spectral values used for processing. The data point 
that has the value larger than tmax or smaller than tmin will be 
excluded from the processing. The default (0.0) is no threshold. 
The outfile specifies an output CASA image name. If the outfile is 
empty, the default name ('sdfixscan.out.im') will be used. 
  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'sdfixscan'
        self.__globals__['taskname'] = 'sdfixscan'
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

            myparams['infiles'] = infiles = self.parameters['infiles']
            myparams['mode'] = mode = self.parameters['mode']
            myparams['numpoly'] = numpoly = self.parameters['numpoly']
            myparams['beamsize'] = beamsize = self.parameters['beamsize']
            myparams['smoothsize'] = smoothsize = self.parameters['smoothsize']
            myparams['direction'] = direction = self.parameters['direction']
            myparams['maskwidth'] = maskwidth = self.parameters['maskwidth']
            myparams['tmax'] = tmax = self.parameters['tmax']
            myparams['tmin'] = tmin = self.parameters['tmin']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infiles'] = infiles
        mytmp['mode'] = mode
        mytmp['numpoly'] = numpoly
        mytmp['beamsize'] = beamsize
        mytmp['smoothsize'] = smoothsize
        mytmp['direction'] = direction
        mytmp['maskwidth'] = maskwidth
        mytmp['tmax'] = tmax
        mytmp['tmin'] = tmin
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'sdfixscan.xml')

        casalog.origin('sdfixscan')
        try :
          #if not trec.has_key('sdfixscan') or not casac.casac.utils().verify(mytmp, trec['sdfixscan']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['sdfixscan'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('sdfixscan', 'sdfixscan.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'sdfixscan'
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
          result = sdfixscan(infiles, mode, numpoly, beamsize, smoothsize, direction, maskwidth, tmax, tmin, outfile, overwrite)

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
             tname = 'sdfixscan'
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
#        paramgui.runTask('sdfixscan', myf['_ip'])
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
        a['infiles']  = ['']
        a['mode']  = 'fft_mask'
        a['tmax']  = 0.0
        a['tmin']  = 0.0
        a['outfile']  = ''
        a['overwrite']  = False

        a['mode'] = {
                    0:odict([{'value':'fft_mask'}, {'direction':[]}, {'maskwidth':1.0}]), 
                    1:odict([{'value':'model'}, {'numpoly':2}, {'beamsize':0.0}, {'smoothsize':2.0}, {'direction':0.0}])}

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
    def description(self, key='sdfixscan', subkey=None):
        desc={'sdfixscan': 'Task for single-dish image processing',
               'infiles': 'list of name of input SD images (FITS or CASA image)',
               'mode': 'image processing mode ["fft_mask", "model"]',
               'numpoly': 'order of polynomial fit for Pressed-out method',
               'beamsize': 'beam size for Pressed-out method',
               'smoothsize': 'size of smoothing beam for Pressed-out method',
               'direction': 'scan direction (p.a.) counterclockwise from the horizontal axis in unit of degree',
               'maskwidth': 'mask width for Basket-Weaving (on percentage)',
               'tmax': 'maximum threshold value for processing',
               'tmin': 'minimum threshold value for processing',
               'outfile': 'name of output file',
               'overwrite': 'overwrite the output file if already exists [True, False]',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['infiles']  = ['']
        a['mode']  = 'fft_mask'
        a['numpoly']  = 2
        a['beamsize']  = 0.0
        a['smoothsize']  = 2.0
        a['direction']  = []
        a['maskwidth']  = 1.0
        a['tmax']  = 0.0
        a['tmin']  = 0.0
        a['outfile']  = ''
        a['overwrite']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mode']  == 'fft_mask':
            a['direction'] = []
            a['maskwidth'] = 1.0

        if self.parameters['mode']  == 'model':
            a['numpoly'] = 2
            a['beamsize'] = 0.0
            a['smoothsize'] = 2.0
            a['direction'] = 0.0

        if a.has_key(paramname) :
              return a[paramname]
sdfixscan_cli = sdfixscan_cli_()
