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
from task_imtrans import imtrans
class imtrans_cli_:
    __name__ = "imtrans"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (imtrans_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'outfile':None, 'order':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, outfile=None, order=None, ):

        """Reorder image axes
        Arguments :
                imagename: Name of the input image which must be specified.
                   Default Value: 

                outfile: Name of output CASA image.
                   Default Value: 

                order: New zero-based axes order.
                   Default Value: 

        Returns: bool

        Example :

PARAMETER SUMMARY
imagename        Name of the input image
outfile          Name of output CASA image. Must be specified.
order            Output axes mapping

This task reorders (transposes) the axes in the input image to the specified
order. The associated pixel values and coordinate system are transposed.

The order parameter describes the mapping of the input axes to the output axes.
It can be one of three types: a non-negative integer, a string, or a list of
strings. If a string or non-negative integer, it should contain
zero-based digits describing the new order of the input axes. It must
contain the same number of (unique) digits as the number of input axes. For example,
specifying order="1032" or order=1032 for a four axes image maps input axes
1, 0, 3, 2 to output axes 0, 1, 2, 3. In the case of order being a nonnegative integer
and the zeroth axis in the input being mapped to zeroth axis in the output, the zeroth
digit is implicitly understood to be 0 so that to transpose an image where one would
use a string order="0321", one could equivalently specify an int order=321.
IMPORTANT: When specifying a non-negative integer and mapping the zeroth axis of
the input to the zeroth axis of the output, do *not* explicitly specify the leading
0; eg, specify order=321 rather than order=0321. Python interprets an integer with
a leading 0 as an octal number.

Because of ambiguity for axes numbers greater than nine, using string or integer order
specifications cannot handle images containing more than 10 axes.
The order parameter can also be specified as a list of strings which uniquely match,
ignoring case, the first characters of the image axis names (ia.coordsys().names()).
So to reorder an image with right ascension, declination, and frequency axes, one could
specify order=["d", "f", "r"] or equivalently ["decl", "frequ", "right a"]. Note that
specifying "ra" for the right ascension axis will result in an error because "ra" does
not match the first two characters of "right ascension".
Axes can be simultaneously inverted in cases where order is a string or an array of
strings by specifying negative signs in front of the axis/axes to be inverted. So,
in a 4-D image, order="-10-3-2" maps input axes 1, 0, 3, 2 to output axes 0, 1, 2, 3 
and reverses the direction and values of input axes 1, 3, and 2.   
EXAMPLE: 
# Swap the stokes and spectral axes in an RA-Dec-Stokes-Frequency image
imagename = "myim.im"
outfile = "outim.im"
order = "0132"
imtrans()

# or

outfile = "myim_2.im"
order = 132
imtrans()

# or

outfile = "myim_3.im"
order = ["r", "d", "f", "s"]
imtrans()

# or

utfile = "myim_4.im"
order = ["rig", "declin", "frequ", "stok"]
imtrans()


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'imtrans'
        self.__globals__['taskname'] = 'imtrans'
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
            myparams['order'] = order = self.parameters['order']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['order'] = order
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'imtrans.xml')

        casalog.origin('imtrans')
        try :
          #if not trec.has_key('imtrans') or not casac.casac.utils().verify(mytmp, trec['imtrans']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['imtrans'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('imtrans', 'imtrans.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'imtrans'
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
          result = imtrans(imagename, outfile, order)

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
             tname = 'imtrans'
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
#        paramgui.runTask('imtrans', myf['_ip'])
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
        a['order']  = ''


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
    def description(self, key='imtrans', subkey=None):
        desc={'imtrans': 'Reorder image axes',
               'imagename': 'Name of the input image which must be specified.',
               'outfile': 'Name of output CASA image.',
               'order': 'New zero-based axes order.',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['outfile']  = ''
        a['order']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
imtrans_cli = imtrans_cli_()
