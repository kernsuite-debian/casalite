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
from task_imhead import imhead
class imhead_cli_:
    __name__ = "imhead"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (imhead_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'mode':None, 'hdkey':None, 'hdvalue':None, 'verbose':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, mode=None, hdkey=None, hdvalue=None, verbose=None, ):

        """List, get and put image header parameters

        Detailed Description:

List, get and put image header parameters.

This task allows the user to manipulate metadata associated with a
CASA image. Both float and complex valued images are fully supported.

For measurement sets, the task vishead should be used.

        Arguments :
                imagename: Input image cube.
                     Default: none

                        Example: imagename='ngc5921_task.image'

                   Default Value: 

                mode: Mode of operation.
                     Default: summary
                     Options: "add", "del", "get", "history", "list",
                     "put", or "summary".

                     * add: Add a new metadata value to the image. The
                       behavior of mode="add" depends on the
                       keyword. In general, the return value will be
                       True if the operation succeeds, or False if it
                       fails or is not supported. If unsuccessful or
                       not supported, a message is normally logged
                       which describes the failure. In most cases, you
                       probably want to use mode='put' rather than
                       mode='add'. We continue to support mode='add'
                       mainly for backward compatibility.
                     * del: Delete a key or reset its value to a
                       fidicual value if possible. Ignores all but
                       imagename, mode, and hdkey parameters. In
                       general, the return value will be True if the
                       operation succeeds, or False if it fails or is
                       not supported. If unsuccessful or not
                       supported, a warning message is normally logged
                       which describes the failure.
                     * get: Return the specified keyword
                       value. Ignores all but imagename, mode, and
                       hdkey parameters.
                     * history: Log image history. Ignores all but
                       imagename and mode parameters.
                     * list: Show supported keywords and their
                       values. Ignores all but imagename and mode
                       parameters.
                       put: Modify the specified value associated with
                       the keyword. True is returned if the metadatum
                       was successfully modified, False
                       otherwise. Normally, a diagnostic message is
                       logged if there is a failure. Only the
                       parameter specified is modified; eg, no
                       modification of reference direction occurs to
                       implicitly account for precession to a new
                       reference frame.
                     * summary: Log a summary of the image and return
                       a dictionary of various metadata
                       values. Ignores all but imagename and mode
                       parameters.

                     IMPORTANT: Lists of keywords for the various
                     modes of operation are given in the imhead task
                     pages of CASA Docs
                     (https://casa.nrao.edu/casadocs/). 

                     The behavior of mode='add|del|get depends on the
                     keyword. Modes "add", "del", and "put" will not
                     work if the image is read-only (eg a FITS
                     image). 

                     NOTE: Only limited checking is implemented to
                     ensure modifying a specific value will leave the
                     image metadata in a consistent state, so, if one
                     is not careful, one could end up with an image
                     that has an inconsistent set of metadata and is
                     therefore, nonsensical and useless That is,
                     PROCEED AT YOUR OWN RISK when using modes add,
                     del, or put.

                   Default Value: summary
                   Allowed Values:
                                list
                                history
                                get
                                put
                                add
                                del
                                summary

                hdkey: Keyword to use with get, put, add, or del.
                     Subparameter of mode=get|put|add|del

                     Only "get" will work if the image is read-only
                     (eg, a FITS image).

                        Example: hdkey='telescope'

                   Default Value: 

                hdvalue: Keyword value used for modes 'put' and 'add'. 
                     Subparameter of mode='put|add' ('del')

                     Also used for mode="del" when hdvalue="masks. 

                        Example: hdvalue='VLA'

                   Default Value: 

                verbose: Give a full listing of beams or just a short summary? Only used when the image has multiple beams and mode="summary".
                   Default Value: False

        Returns: variant

        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF IMHEAD IN CASA DOCS:
https://casa.nrao.edu/casadocs/    

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'imhead'
        self.__globals__['taskname'] = 'imhead'
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
            myparams['mode'] = mode = self.parameters['mode']
            myparams['hdkey'] = hdkey = self.parameters['hdkey']
            myparams['hdvalue'] = hdvalue = self.parameters['hdvalue']
            myparams['verbose'] = verbose = self.parameters['verbose']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['mode'] = mode
        mytmp['hdkey'] = hdkey
        mytmp['hdvalue'] = hdvalue
        mytmp['verbose'] = verbose
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'imhead.xml')

        casalog.origin('imhead')
        try :
          #if not trec.has_key('imhead') or not casac.casac.utils().verify(mytmp, trec['imhead']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['imhead'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('imhead', 'imhead.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'imhead'
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
          result = imhead(imagename, mode, hdkey, hdvalue, verbose)

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
             tname = 'imhead'
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
#        paramgui.runTask('imhead', myf['_ip'])
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
        a['mode']  = 'summary'

        a['mode'] = {
                    0:odict([{'value':'summary'}, {'verbose':False}]), 
                    1:{'value':'list'}, 
                    2:{'value':'history'}, 
                    3:odict([{'value':'put'}, {'hdkey':''}, {'hdvalue':''}]), 
                    4:odict([{'value':'add'}, {'hdkey':''}, {'hdvalue':''}]), 
                    5:odict([{'value':'get'}, {'hdkey':''}]), 
                    6:odict([{'value':'del'}, {'hdkey':''}])}

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
    def description(self, key='imhead', subkey=None):
        desc={'imhead': 'List, get and put image header parameters',
               'imagename': 'Name of the input spectral line image',
               'mode': '',
               'hdkey': 'The associated keyword for modes "add", "del", "get", or "put". Only "get" will work if the image is read-only (eg, a FITS image).',
               'hdvalue': 'Value of keyword for modes add or put.',
               'verbose': 'Give a full listing of beams or just a short summary? Only used when the image has multiple beams and mode="summary".',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['mode']  = 'summary'
        a['hdkey']  = ''
        a['hdvalue']  = ''
        a['verbose']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mode']  == 'summary':
            a['verbose'] = False

        if self.parameters['mode']  == 'put':
            a['hdkey'] = ''
            a['hdvalue'] = ''

        if self.parameters['mode']  == 'add':
            a['hdkey'] = ''
            a['hdvalue'] = ''

        if self.parameters['mode']  == 'get':
            a['hdkey'] = ''

        if self.parameters['mode']  == 'del':
            a['hdkey'] = ''

        if a.has_key(paramname) :
              return a[paramname]
imhead_cli = imhead_cli_()
