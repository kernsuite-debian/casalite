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
from task_imval import imval
class imval_cli_:
    __name__ = "imval"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (imval_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'region':None, 'box':None, 'chans':None, 'stokes':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, region=None, box=None, chans=None, stokes=None, ):

        """Get the data value(s) and/or mask value in an image.
        Arguments :
                imagename: Name of the input image
                   Default Value: 

                region: Region selection. Empty string (default) means use rules for box/chans/stokes specification.
                   Default Value: 

                box: Rectangular region(s) to select in direction plane. Empty string (default) means use the reference pixel.
                   Default Value: 

                chans: Channels to use. Default is to use all channels.
                   Default Value: 

                stokes: Stokes planes to use. Planes specified must be contiguous. Default is to use all Stokes planes.
                   Default Value: 

        Returns: void

        Example :

     The data point(s) to be retrieved are those found in the specified
     region, which may be:
        1. A region file or text string, with the following caveat:
           * If the specified region is complex (eg, a union or intersection of multiple regions,
             only the first simple region in this set is used.
           * If the region is not rectangular, then the rectangular region that circumscribes the
             specified region (ie the bounding box) is used to retrieve values, since the returned
             arrays must be rectangular. The resulting mask values in this case are the result of
             anding the image mask values with the specified region mask values, eg
             if a pixel falls outside the specified region but within the bounding box, its returned
             mask value will be false even if its image mask value is true.
        2. A region specified by a set of rectangular
           pixel coordinates, the channel ranges and/or the Stokes.

     For directed output, run as 
                    myoutput = imval()
   

        Keyword arguments:
        imagename -- Name of input image
                Default: none; Example: imagename='ngc5921_task.im'
        region -- Region selection. Empty string (default) means use rules for box/chans/stokes specification.
                Example: region='myimage.im.rgn'
                         region='region1'
        box --  Rectangular region to select in direction plane. Empty string (default) means use the reference pixel.
                Default: '' (referencepixel values for the Directional coord); 
                Example: box='10,10,50,50'
                         box = '10,10,30,30,35,35,50,50' (two boxes)
        chans -- Channels to use. Default is to use all channels.
        stokes -- Stokes planes to use. Planes specified must be contiguous. Default is to use all Stokes planes.
                 Example: stokes='IQUV';  
                      stokes='I,Q'

      General procedure:

         1.  Specify inputs, then

         2.  myoutput = imval()
               or specify inputs directly in calling sequence to task
             myoutput = imsval(imagename='image.im', etc)

         3.  myoutput['KEYS'] will contain the result associated with any
               of the keys given below
        
        KEYS CURRENTLY AVAILABLE
        blc          - absolute PIXEL coordinate of the bottom left corner of 
                       the bounding box surrounding the selected region
        trc          - the absolute PIXEL coordinate of the top right corner 
                       of the bounding box surrOunding the selected region
        axes         - List the data stored in each axis of the data block.
        unit         - unit of the returned data values.
        data         - data value(s) found in the given region
        mask         - mask value(s) found in the given region. See important
                       note above regarding returned mask values for
                       non-rectangular regions.

        NOTE: The data returned is in the same order as it is internally
        stored, typically RA, DEC, spectral, stokes. Also both the data
        and mask values are returned as Python Numpy arrays, for more
        information on how to manipulate them see
             http://numpy.scipy.org/#array_interface


        Additional Examples
        # The value and mask value at a single point (5,17,2,Q)
        imval( 'myImage', box='5,5,17,17', chans=2, stokes='Q' )

        # Select and report on two box regions
        # box 1, bottom-left coord is 2,3 and top-right coord is 14,15
        # box 2, bottom-left coord is 30,31 and top-right coord is 42,43
        # Note that only the boxes for the 
        imval( 'myImage', box='2,3,14,15;30,31,42,43' )

        # Select the same two box regions but only channels 4 and 5
        imval( 'myImage', box='2,3,14,15;30,31,42,43', chan='4~5' )

        # Select all channels greater the 20 as well as channel 0.
        # Then the mean and standard deviation are printed
        # Note that the data returned is a Python numpy array which
        # has built in operations such as min, max, and means as
        # demonstrated here.
        results = imval( 'myImage', chans='>20;0' )
        imval_data=results['data']
        mask=results['mask']
        # holds the absolute coordinates of the associated pixels in imval_data
        coords = results['coords']
        print "Data max: ", imval_data.max(), "  mean is ", imval_data.mean()
        swapped_data=imval_data.swapaxes(0,2)
        swapped_mask=mask.swapaxes(0,2)
        print "Data values for 21st channel: \n", swapped_data[0]
        print "Mask values for 21st channel: \n", swapped_mask[0]

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'imval'
        self.__globals__['taskname'] = 'imval'
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
            myparams['region'] = region = self.parameters['region']
            myparams['box'] = box = self.parameters['box']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'imval.xml')

        casalog.origin('imval')
        try :
          #if not trec.has_key('imval') or not casac.casac.utils().verify(mytmp, trec['imval']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['imval'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('imval', 'imval.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'imval'
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
          result = imval(imagename, region, box, chans, stokes)

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
             tname = 'imval'
             casalog.post('An error occurred running task '+tname+'.', 'ERROR')
             pass
        casalog.origin('')

        for arg in result :
           if not result.has_key(arg) :
                 throw('Missing output value '+arg)

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
#        paramgui.runTask('imval', myf['_ip'])
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
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''


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
    def description(self, key='imval', subkey=None):
        desc={'imval': 'Get the data value(s) and/or mask value in an image.',
               'imagename': 'Name of the input image',
               'region': 'Region selection. Empty string (default) means use rules for box/chans/stokes specification.',
               'box': 'Rectangular region(s) to select in direction plane. Empty string (default) means use the reference pixel.',
               'chans': 'Channels to use. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Planes specified must be contiguous. Default is to use all Stokes planes.',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
imval_cli = imval_cli_()
