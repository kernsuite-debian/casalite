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
from task_listpartition import listpartition
class listpartition_cli_:
    __name__ = "listpartition"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (listpartition_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'createdict':None, 'listfile':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, createdict=None, listfile=None, ):

        """List the summary of a multi-MS data set in the logger or in a file

        Detailed Description:

       Lists the following properties of a multi-measurement set:
       sub-MS name, scan list, spw list, list of number of channels per spw, 
       number of rows for all scans.
       
        Arguments :
                vis: Name of Multi-MS or normal MS.
                   Default Value: 

                createdict: Create and return a dictionary with Sub-MS information
                   Default Value: False

                listfile: Name of ASCII file to save output: ''==>to terminal
                   Default Value: 

        Returns: void

        Example :


       A multi-measurement set (MMS) is an MS that has been split into sub-MSs.
       An MMS contains a reference MS in the top directory and the sub-MSs are 
       located in a directory called SUBMSS inside the MMS directory.
       Example of a MS that was partitioned in the 'scan' axis using the task partition: 

       > ls ngc5921.mms
         ANTENNA           FLAG_CMD     POLARIZATION  SPECTRAL_WINDOW  table.dat
         DATA_DESCRIPTION  HISTORY      PROCESSOR     STATE            table.info
         FEED              OBSERVATION  SORTED_TABLE  SUBMSS           WEATHER
         FIELD             POINTING     SOURCE        SYSCAL

       > ls ngc5921.mms/SUBMSS/
         ngc5921.0000.ms/  ngc5921.0002.ms/  ngc5921.0004.ms/  ngc5921.0006.ms/
         ngc5921.0001.ms/  ngc5921.0003.ms/  ngc5921.0005.ms/
              
       The task lists the following properties of a multi-MS or MS:
       sub-MS name, scan, spw list, list of number of channels per spw, 
       number of rows for each scan and the size in disk. Example of logger output:
       
        Sub-MS          Scan  Spw      Nchan    Nrows   Size  
        ngc5921.0000.ms  1    [0]      [63]     4509    11M
        ngc5921.0001.ms  2    [0]      [63]     1890    6.4M
        ngc5921.0002.ms  3    [0]      [63]     6048    13M
        ngc5921.0003.ms  4    [0]      [63]     756     4.9M
        ngc5921.0004.ms  5    [0]      [63]     1134    6.4M
        ngc5921.0005.ms  6    [0]      [63]     6804    15M
        ngc5921.0006.ms  7    [0]      [63]     1512    6.4M


------- Detailed description of keyword arguments -------
       vis -- Name of multi-MS or normal MS.
              default: ''. 
              example: vis='pScan.mms'

       createdict -- Create and return a dictionary containing scan summaries of each
                     sub-MS. 
              default: False
              
              If set to True, the returned dictionary will contain information from
              ms.getscansummary() and ms.getspectralwindowinfo(), with the addition of an 
              index as the top key and the sub-MS name.
              Example:
              
            {0: {'MS': 'ngc5921.0000.ms',
                 'scanId': {1: {'nchans': array([63], dtype=int32),
                                'nrows': 4509,
                                'spwIds': array([0], dtype=int32)}},
                 'size': '11M'},
             1: {'MS': 'ngc5921.0001.ms',
                 'scanId': {2: {'nchans': array([63], dtype=int32),
                                'nrows': 1890,
                                'spwIds': array([0], dtype=int32)}},
                 'size': '6.4M'}}
                    
       listfile -- Name of ASCII file to save output to. If empty, it will 
                   list on the logger/terminal.
              default: ''
              example: listfile='pscan.txt'

 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'listpartition'
        self.__globals__['taskname'] = 'listpartition'
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
            myparams['createdict'] = createdict = self.parameters['createdict']
            myparams['listfile'] = listfile = self.parameters['listfile']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['createdict'] = createdict
        mytmp['listfile'] = listfile
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'listpartition.xml')

        casalog.origin('listpartition')
        try :
          #if not trec.has_key('listpartition') or not casac.casac.utils().verify(mytmp, trec['listpartition']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['listpartition'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('listpartition', 'listpartition.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'listpartition'
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
          result = listpartition(vis, createdict, listfile)

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
             tname = 'listpartition'
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
#        paramgui.runTask('listpartition', myf['_ip'])
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
        a['vis']  = ''
        a['createdict']  = False
        a['listfile']  = ''


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
    def description(self, key='listpartition', subkey=None):
        desc={'listpartition': 'List the summary of a multi-MS data set in the logger or in a file',
               'vis': 'Name of Multi-MS or normal MS.',
               'createdict': 'Create and return a dictionary with Sub-MS information',
               'listfile': 'Name of ASCII file to save output: ''==>to terminal',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['createdict']  = False
        a['listfile']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
listpartition_cli = listpartition_cli_()
