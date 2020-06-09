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
from task_browsetable import browsetable
class browsetable_cli_:
    __name__ = "browsetable"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (browsetable_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'tablename':None, 'mightedit':None, 'sortlist':None, 'taql':None, 'skipcols':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, tablename=None, mightedit=None, sortlist=None, taql=None, skipcols=None, ):

        """Browse a table (MS, calibration table, image)

        Detailed Description:

This task brings up a browser that can open and display any CASA
table. The tablename can be specified at startup, or any table can be
loaded after the browser comes up.
  
        Arguments :
                tablename: Name of table file (vis, calibration table, image)
                     Default: none
                     
                        Example: tablename='ngc5921.ms'

                   Default Value: 

                mightedit: Disable the filtering options (below) and allow editing
the table.
                     Default: False
                     Options: False|True

                     Warning: the GUI seems to ignore whether the
                     table tool is opened read-only - just be careful,
                     esp. if filtering.

                   Default Value: False

                sortlist: List of columns to sort by
                     Default: none

                   Default Value: 

                taql: TaQL query string for prefiltering the table.
                     Default: none

                        Example: taql="ANTENNA2 < 6

                   Default Value: 

                skipcols: Columns to NOT display.
                     Default: none

                        Example: skipcols='feed1, feed2'

                   Default Value: 

        Returns: void

        Example :


For more information, see the task pages of browsetable in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'browsetable'
        self.__globals__['taskname'] = 'browsetable'
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

            myparams['tablename'] = tablename = self.parameters['tablename']
            myparams['mightedit'] = mightedit = self.parameters['mightedit']
            myparams['sortlist'] = sortlist = self.parameters['sortlist']
            myparams['taql'] = taql = self.parameters['taql']
            myparams['skipcols'] = skipcols = self.parameters['skipcols']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['tablename'] = tablename
        mytmp['mightedit'] = mightedit
        mytmp['sortlist'] = sortlist
        mytmp['taql'] = taql
        mytmp['skipcols'] = skipcols
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'browsetable.xml')

        casalog.origin('browsetable')
        try :
          #if not trec.has_key('browsetable') or not casac.casac.utils().verify(mytmp, trec['browsetable']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['browsetable'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('browsetable', 'browsetable.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'browsetable'
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
          result = browsetable(tablename, mightedit, sortlist, taql, skipcols)

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
             tname = 'browsetable'
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
#        paramgui.runTask('browsetable', myf['_ip'])
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
        a['tablename']  = ''

        a['tablename'] = {
                    0:odict([{'notvalue':''}, {'mightedit':False}, {'sortlist':''}, {'taql':''}, {'skipcols':''}])}

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
    def description(self, key='browsetable', subkey=None):
        desc={'browsetable': 'Browse a table (MS, calibration table, image)',
               'tablename': 'Name of input table',
               'mightedit': 'Warning: the GUI seems to ignore whether the table tool is opened read-only. Just be careful, esp. if filtering.',
               'sortlist': 'Columns to sort by (ascending)',
               'taql': 'TaQL query string for prefiltering the table.',
               'skipcols': 'Columns to omit',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['tablename']  = ''
        a['mightedit']  = False
        a['sortlist']  = ''
        a['taql']  = ''
        a['skipcols']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['tablename']  != '':
            a['mightedit'] = False
            a['sortlist'] = ''
            a['taql'] = ''
            a['skipcols'] = ''

        if a.has_key(paramname) :
              return a[paramname]
browsetable_cli = browsetable_cli_()
