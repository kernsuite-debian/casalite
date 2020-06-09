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
from task_nrobeamaverage import nrobeamaverage
class nrobeamaverage_cli_:
    __name__ = "nrobeamaverage"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (nrobeamaverage_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'infile':None, 'datacolumn':None, 'field':None, 'spw':None, 'timerange':None, 'scan':None, 'beam':None, 'timebin':None, 'outfile':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, infile=None, datacolumn=None, field=None, spw=None, timerange=None, scan=None, beam=None, timebin=None, outfile=None, ):

        """Average SD data over beams and do time averaging

        Detailed Description:

    
    The task nrobeamaverage is for Nobeyama dataset of ON-ON observations.
    It averages on-source spectra having specified beam IDs over specified 
    time bins. 
    

        Arguments :
                infile: name of input SD dataset
                   Default Value: 

                datacolumn: name of data column to be used ["data", "float_data", or "corrected_data"]
                   Default Value: float_data

                field: select data by field IDs and names, e.g. "3C2*" (""=all)
                   Default Value: 

                spw: select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
                   Default Value: 

                timerange: select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
                   Default Value: 

                scan: select data by scan numbers, e.g. "21~23" (""=all)
                   Default Value: 

                beam: beam IDs to be averaged over, e.g. "1,3" (""=all)
                   Default Value: 

                timebin: bin width for time averaging.
                   Default Value: 0s

                outfile: name of output file
                   Default Value: 


        Example :
  
-----------------
Keyword arguments
-----------------
infile -- name of input SD dataset
datacolumn -- name of data column to be used
        options: 'data', 'float_data', or 'corrected_data'
        default: 'float_data'
field -- select data by field IDs and names
        default: '' (use all fields)
        example: field='3C2*' (all names starting with 3C2)
                 field='0,4,5~7' (field IDs 0,4,5,6,7)
                 field='0,3C273' (field ID 0 or field named 3C273)
        this selection is in addition to the other selections to data
spw -- select data by IF IDs (spectral windows)
        default: '' (use all IFs)
        example: spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                 spw='<2';  spectral windows less than 2 (i.e. 0,1)
        this selection is in addition to the other selections to data
timerange -- select data by time range
        default: '' (use all)
        example: timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                 Note: YYYY/MM/DD can be dropped as needed:
                 timerange='09:14:00~09:54:00' # this time range
                 timerange='09:44:00' # data within one integration of time
                 timerange='>10:24:00' # data after this time
                 timerange='09:44:00+00:13:00' #data 13 minutes after time
        this selection is in addition to the other selections to data
scan -- select data by scan numbers
        default: '' (use all scans)
        example: scan='21~23' (scan IDs 21,22,23)
        this selection is in addition to the other selections to data
beam -- beam IDs to be averaged over
        default: '' (all beam IDs)
        example: beam='1,3' (beam IDs 1 and 3)
                 NOTE: beam IDs of averaged spectra in the output file will 
                       be the smallest one, e.g., in case of beam='1,3', 
                       the averaged output spectra will have beam ID 1.
                       Note also that beam IDs should be stored in the 
                       ANTENNA column of input MS.
timebin -- bin width for time averaging
           default: '' (only beam IDs changed, no time averaging)
outfile -- name of output file


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'nrobeamaverage'
        self.__globals__['taskname'] = 'nrobeamaverage'
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

            myparams['infile'] = infile = self.parameters['infile']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['beam'] = beam = self.parameters['beam']
            myparams['timebin'] = timebin = self.parameters['timebin']
            myparams['outfile'] = outfile = self.parameters['outfile']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['datacolumn'] = datacolumn
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['timerange'] = timerange
        mytmp['scan'] = scan
        mytmp['beam'] = beam
        mytmp['timebin'] = timebin
        mytmp['outfile'] = outfile
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'nrobeamaverage.xml')

        casalog.origin('nrobeamaverage')
        try :
          #if not trec.has_key('nrobeamaverage') or not casac.casac.utils().verify(mytmp, trec['nrobeamaverage']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['nrobeamaverage'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('nrobeamaverage', 'nrobeamaverage.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'nrobeamaverage'
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
          result = nrobeamaverage(infile, datacolumn, field, spw, timerange, scan, beam, timebin, outfile)

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
             tname = 'nrobeamaverage'
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
#        paramgui.runTask('nrobeamaverage', myf['_ip'])
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
        a['infile']  = ''
        a['datacolumn']  = 'float_data'
        a['field']  = ''
        a['spw']  = ''
        a['timerange']  = ''
        a['scan']  = ''
        a['beam']  = ''
        a['timebin']  = '0s'
        a['outfile']  = ''


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
    def description(self, key='nrobeamaverage', subkey=None):
        desc={'nrobeamaverage': 'Average SD data over beams and do time averaging',
               'infile': 'name of input SD dataset',
               'datacolumn': 'name of data column to be used ["data", "float_data", or "corrected_data"]',
               'field': 'select data by field IDs and names, e.g. "3C2*" (""=all)',
               'spw': 'select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)',
               'timerange': 'select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)',
               'scan': 'select data by scan numbers, e.g. "21~23" (""=all)',
               'beam': 'beam IDs to be averaged over, e.g. "1,3" (""=all)',
               'timebin': 'bin width for time averaging.',
               'outfile': 'name of output file',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['infile']  = ''
        a['datacolumn']  = 'float_data'
        a['field']  = ''
        a['spw']  = ''
        a['timerange']  = ''
        a['scan']  = ''
        a['beam']  = ''
        a['timebin']  = '0s'
        a['outfile']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
nrobeamaverage_cli = nrobeamaverage_cli_()
