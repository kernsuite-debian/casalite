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
from task_testconcat import testconcat
class testconcat_cli_:
    __name__ = "testconcat"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (testconcat_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'testconcatvis':None, 'freqtol':None, 'dirtol':None, 'copypointing':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, testconcatvis=None, freqtol=None, dirtol=None, copypointing=None, ):

        """Concatenate the subtables of several visibility data sets, not the MAIN bulk data.
        Arguments :
                vis: Name(s) of input visibility files to be test-concatenated
                   Default Value: 

                testconcatvis: Name of output MS containing the merged subtables
                   Default Value: 

                freqtol: Frequency shift tolerance for considering data as the same spwid
                   Default Value: 

                dirtol: Direction shift tolerance for considering data as the same field
                   Default Value: 

                copypointing: Copy all rows of the POINTING table.
                   Default Value: True


        Example :


The list of data sets given in the vis argument are concatenated into an output
data set in testconcatvis without the bulk data of the MAIN table.  
This is useful for obtaining the information in the merged subtables without
actually performing a time-consuming concatenation of the MAIN tables on disk.


Keyword arguments:
vis -- Name of input visibility files for which the subtables are to be combined
        default: none; example: vis = 'mydata.ms',
             vis=['src2.ms','ngc5921.ms','ngc315.ms']
testconcatvis -- Name of MS that will contain the concatenated subtables
        default: none; example: testconcatvis='test.ms'

freqtol -- Frequency shift tolerance for considering data to be in the same
           spwid.  The number of channels must also be the same.
        default: ''  do not combine unless frequencies are equal
        example: freqtol='10MHz' will not combine spwid unless they are
           within 10 MHz.
        Note: This option is useful to conbine spectral windows with very slight
           frequency differences caused by Doppler tracking, for example.

dirtol -- Direction shift tolerance for considering data as the same field
        default: '' means always combine.
        example: dirtol='1.arcsec' will not combine data for a field unless
           their phase center differ by less than 1 arcsec.  If the field names
           are different in the input data sets, the name in the output data
           set will be the first relevant data set in the list.

copypointing -- Make a proper copy of the POINTING subtable (can be time consuming).
                If False, the result is an empty POINTING table.
         default: True


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'testconcat'
        self.__globals__['taskname'] = 'testconcat'
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

            myparams['vis'] = vis = self.parameters['vis']
            myparams['testconcatvis'] = testconcatvis = self.parameters['testconcatvis']
            myparams['freqtol'] = freqtol = self.parameters['freqtol']
            myparams['dirtol'] = dirtol = self.parameters['dirtol']
            myparams['copypointing'] = copypointing = self.parameters['copypointing']

        if type(vis)==str: vis=[vis]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['testconcatvis'] = testconcatvis
        mytmp['freqtol'] = freqtol
        mytmp['dirtol'] = dirtol
        mytmp['copypointing'] = copypointing
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'testconcat.xml')

        casalog.origin('testconcat')
        try :
          #if not trec.has_key('testconcat') or not casac.casac.utils().verify(mytmp, trec['testconcat']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['testconcat'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('testconcat', 'testconcat.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'testconcat'
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
          result = testconcat(vis, testconcatvis, freqtol, dirtol, copypointing)

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
             tname = 'testconcat'
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
#        paramgui.runTask('testconcat', myf['_ip'])
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
        a['vis']  = ['']
        a['testconcatvis']  = ''
        a['freqtol']  = ''
        a['dirtol']  = ''
        a['copypointing']  = True


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
    def description(self, key='testconcat', subkey=None):
        desc={'testconcat': 'Concatenate the subtables of several visibility data sets, not the MAIN bulk data.',
               'vis': 'Name(s) of input visibility files to be test-concatenated',
               'testconcatvis': 'Name of output MS containing the merged subtables',
               'freqtol': 'Frequency shift tolerance for considering data as the same spwid',
               'dirtol': 'Direction shift tolerance for considering data as the same field',
               'copypointing': 'Copy all rows of the POINTING table.',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ['']
        a['testconcatvis']  = ''
        a['freqtol']  = ''
        a['dirtol']  = ''
        a['copypointing']  = True

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
testconcat_cli = testconcat_cli_()
