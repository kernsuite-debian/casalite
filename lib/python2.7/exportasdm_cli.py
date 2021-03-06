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
from task_exportasdm import exportasdm
class exportasdm_cli_:
    __name__ = "exportasdm"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (exportasdm_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'asdm':None, 'datacolumn':None, 'archiveid':None, 'rangeid':None, 'subscanduration':None, 'sbduration':None, 'apcorrected':None, 'verbose':None, 'showversion':None, 'useversion':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, asdm=None, datacolumn=None, archiveid=None, rangeid=None, subscanduration=None, sbduration=None, apcorrected=None, verbose=None, showversion=None, useversion=None, ):

        """Convert a CASA visibility file (MS) into an ALMA or EVLA Science Data Model

        Detailed Description:

Convert a CASA visibility file (MS) into an ALMA or EVLA Science Data Model

        Arguments :
                vis: Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'

                   Default Value: 

                asdm: Name of output ASDM directory (on disk)
                     Default: none

                   Default Value: 

                datacolumn: Which data column(s) to use for processing
                     (case-insensitive).
                     Default: 'corrected'
                     Options: 'data', 'model', 'corrected',
                     'all','float_data', 'lag_data',
                     'float_data,data', 'lag_data,data'

                        Example: datacolumn='data'
    
                     NOTE: 'all' = whichever of the above that are
                     present. If the requested column does not exist,
                     the task will exit with an error.

                   Default Value: data
                   Allowed Values:
                                data
                                corrected
                                model

                archiveid: The X0 in uid://X0/X1/X2
                     Default: 'S0'

                   Default Value: S0

                rangeid: The X1 in uid://X0/X1/X2
                     Default: 'X1'

                   Default Value: X1

                subscanduration: Maximum duration of a subscan in the output ASDM
                     Default: 24h

                   Default Value: 24h

                sbduration: Maximum duration of a scheduling block (and therefore
exec block) in the output ASDM
                     Default: '2700s'

                     The sbduration parameter controls the number of
                     execution blocks (EBs) into which exportasdm
                     subdivides the visibilities from your input
                     MS. If the total observation time in the MS is
                     shorter than what is given in sbduration, a
                     single EB will be created.

                   Default Value: 2700s

                apcorrected: Data to be marked as having atmospheric phase correction
                     Default: False
                     Options: False|True

                   Default Value: False

                verbose: Produce log output?
                     Default: True
                     Options: True|False

                   Default Value: True

                showversion: Report the version of ASDM class set being used
                     Default: True
                     Options: True|False

                   Default Value: True

                useversion: Selects the version of MS2asdm to be used
                     Default: 'v3'

                   Default Value: v3
                   Allowed Values:
                                v3
                                

        Returns: bool

        Example :


For more information, see the task pages of exportasdm in CASA Docs:

https://casa.nrao.edu/casadocs/

  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'exportasdm'
        self.__globals__['taskname'] = 'exportasdm'
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
            myparams['asdm'] = asdm = self.parameters['asdm']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']
            myparams['archiveid'] = archiveid = self.parameters['archiveid']
            myparams['rangeid'] = rangeid = self.parameters['rangeid']
            myparams['subscanduration'] = subscanduration = self.parameters['subscanduration']
            myparams['sbduration'] = sbduration = self.parameters['sbduration']
            myparams['apcorrected'] = apcorrected = self.parameters['apcorrected']
            myparams['verbose'] = verbose = self.parameters['verbose']
            myparams['showversion'] = showversion = self.parameters['showversion']
            myparams['useversion'] = useversion = self.parameters['useversion']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['asdm'] = asdm
        mytmp['datacolumn'] = datacolumn
        mytmp['archiveid'] = archiveid
        mytmp['rangeid'] = rangeid
        mytmp['subscanduration'] = subscanduration
        mytmp['sbduration'] = sbduration
        mytmp['apcorrected'] = apcorrected
        mytmp['verbose'] = verbose
        mytmp['showversion'] = showversion
        mytmp['useversion'] = useversion
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'exportasdm.xml')

        casalog.origin('exportasdm')
        try :
          #if not trec.has_key('exportasdm') or not casac.casac.utils().verify(mytmp, trec['exportasdm']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['exportasdm'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('exportasdm', 'exportasdm.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'exportasdm'
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
          result = exportasdm(vis, asdm, datacolumn, archiveid, rangeid, subscanduration, sbduration, apcorrected, verbose, showversion, useversion)

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
             tname = 'exportasdm'
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
#        paramgui.runTask('exportasdm', myf['_ip'])
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
        a['asdm']  = ''
        a['datacolumn']  = 'data'
        a['archiveid']  = 'S0'
        a['rangeid']  = 'X1'
        a['subscanduration']  = '24h'
        a['sbduration']  = '2700s'
        a['apcorrected']  = False
        a['verbose']  = True
        a['showversion']  = True
        a['useversion']  = 'v3'


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
    def description(self, key='exportasdm', subkey=None):
        desc={'exportasdm': 'Convert a CASA visibility file (MS) into an ALMA or EVLA Science Data Model',
               'vis': 'Name of input visibility file',
               'asdm': '>Name of output ASDM directory (on disk)',
               'datacolumn': 'Which data column(s) to process.',
               'archiveid': 'The X0 in uid://X0/X1/X2',
               'rangeid': 'The X1 in uid://X0/X1/X2',
               'subscanduration': 'Maximum duration of a subscan in the output ASDM',
               'sbduration': 'Maximum duration of a scheduling block (and therefore exec block) in the output ASDM',
               'apcorrected': 'Data to be marked as having atmospheric phase correction',
               'verbose': 'Produce log output',
               'showversion': 'Report the version of ASDM class set being used',
               'useversion': 'Selects the version of MS2asdm to be used',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['asdm']  = ''
        a['datacolumn']  = 'data'
        a['archiveid']  = 'S0'
        a['rangeid']  = 'X1'
        a['subscanduration']  = '24h'
        a['sbduration']  = '2700s'
        a['apcorrected']  = False
        a['verbose']  = True
        a['showversion']  = True
        a['useversion']  = 'v3'

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
exportasdm_cli = exportasdm_cli_()
