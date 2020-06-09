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
from task_listobs import listobs
class listobs_cli_:
    __name__ = "listobs"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (listobs_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'selectdata':None, 'spw':None, 'field':None, 'antenna':None, 'uvrange':None, 'timerange':None, 'correlation':None, 'scan':None, 'intent':None, 'feed':None, 'array':None, 'observation':None, 'verbose':None, 'listfile':None, 'listunfl':None, 'cachesize':None, 'overwrite':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, selectdata=None, spw=None, field=None, antenna=None, uvrange=None, timerange=None, correlation=None, scan=None, intent=None, feed=None, array=None, observation=None, verbose=None, listfile=None, listunfl=None, cachesize=None, overwrite=None, ):

        """List the summary of a data set in the logger or in a file

        Detailed Description:

       List the summary information of a data set in the logger or in a file, based on
       a data selection. Only rows can be selected and printed. No in-row selection is
       possible (channel or correlation).

       Lists the following properties of a measurement set:
       scan list, field list, spectral window list with
       correlators, antenna locations, ms table information.
    
        Arguments :
                vis: Name of input visibility file (MS)
                   Default Value: 

                selectdata: Data selection parameters
                   Default Value: True

                spw: Selection based on spectral-window/frequency/channel.
                   Default Value: 

                field: Selection based on field names or field index numbers. Default is all.
                   Default Value: 

                antenna: Selection based on antenna/baselines. Default is all.
                   Default Value: 

                uvrange: Selection based on uv range. Default: entire range. Default units: meters.
                   Default Value: 

                timerange: Selection based on time range. Default is entire range.
                   Default Value: 

                correlation: Selection based on correlation. Default is all.
                   Default Value: 

                scan: Selection based on scan numbers. Default is all.
                   Default Value: 

                intent: Selection based on observation intent. Default is all.
                   Default Value: 

                feed: Selection based on multi-feed numbers: Not yet implemented
                   Default Value: 

                array: Selection based on (sub)array numbers. Default is all.
                   Default Value: 

                observation: Selection based on observation ID. Default is all.
                   Default Value: 

                verbose: Controls level of information detail reported. True reports more than False.
                   Default Value: True

                listfile: Name of disk file to write output. Default is none (output is written to logger only).
                   Default Value: 

                listunfl: List unflagged row counts? If true, it can have significant negative performance impact.
                   Default Value: False

                cachesize: EXPERIMENTAL. Maximum size in megabytes of cache in which data structures can be held.
                   Default Value: 50

                overwrite: If True, tacitly overwrite listfile if it exists.
                   Default Value: False

        Returns: void

        Example :


       List the summary information of a data set in the logger or in a file, based on
       a data selection. Only rows can be selected and printed. No in-row selection is
       possible (channel or correlation). Refer to the task listvis to list visibilites.

       Lists the following properties of a measurement set:
       scan list, field list, spectral window list with
       correlators, antenna locations, ms table information.

       Keyword arguments:
       vis -- Name of input visibility file
               default: none. example: vis='ngc5921.ms'
       
       selectdata -- Select a subset of data for flagging
                    default: False
                    options: True,False
                    The summary listing will only apply to the specified selection.

              antenna -- Select data based on baseline
                    default: '' (all); example: antenna='5&6' baseline 5-6
                    antenna='5&6;7&8' #baseline 5-6 and 7-8
                    antenna='5' # all cross-correlation baselines between antenna 5 and all other available
                                  antennas
                    antenna='5,6' # all baselines with antennas 5 and 6
                    antenna='1&&1' # only the auto-correlation baselines for antenna 1
                    antenna='1&&*' # cross and auto-correlation baselines between antenna 1
                                             and all other available antennas
                    antenna='1~7&&&' # only the auto-correlation baselines for antennas in range 1~7
              spw -- Select data based on spectral window and channels
                    default: '' (all); example: spw='1'
                    spw='<2' #spectral windows less than 2
                    spw='>1' #spectral windows greater than 1
              correlation -- Correlation types
                    default: '' (all);
                    example: correlation='RR LL'
              field -- Select data based on field id(s) or name(s)
                    default: '' (all); example: field='1'
                    field='0~2' # field ids inclusive from 0 to 2
                    field='3C*' # all field names starting with 3C
              uvrange -- Select data within uvrange (default units meters)
                    default: '' (all); example:
                    uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lamgda
                    uvrange='>4klamda';uvranges greater than 4 kilo-lambda
                    uvrange='0~1000km'; uvrange in kilometers
              timerange  -- Select data based on time range:
                    default = '' (all); example,
                    timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                    Note: YYYY/MM/DD can be dropped as needed:
                    timerange='09:14:0~09:54:0' # this time range
                    timerange='09:44:00' # data within one integration of time
                    timerange='>10:24:00' # data after this time
                    timerange='09:44:00+00:13:00' #data 13 minutes after time
              scan -- Select data based on scan number
                    default: '' (all); example: scan='>3'
              intent -- Select data based on observation intent
                    default: '' (all); example: intent='*CAL*,*BAND*'
              feed -- Selection based on the feed - NOT IMPLEMENTED YET
              array -- Selection based on the antenna array
              observation -- Selection based on the observation ID
                    default: '' (all); example: observation='1' or observation=1


       verbose -- level of detail
             verbose=True: (default); scan and antenna lists
             verbose=False: less information
             
       listfile -- name of disk file to write output.
               default: None. Example: listfile='list.txt'
               
       listunfl -- List unflagged row counts? If true, it can have significant negative performance impact.
 
       cachesize -- maximum size of the memory cache in megabytes in which data structures can be
                    stored. For very large datasets this can be increased for possibly better performance.
                    THIS IS ONLY EXPERIEMENTAL FOR NOW, AND INCREASING THE VALUE OF THIS PARAMETER DOES NOT GUARANTEE INCREASED
                    SPEED. DEPENDING ON ITS (LACK OF) USEFULNESS, IT MAY BE REMOVED IN THE FUTURE.


      The 'Int (s)' column is the average of the MS's INTERVAL column
      for each scan, so in a time-averaged MS 'Int' = 9.83s more likely
      means 5 10s integrations and 1 9s integration (timebin) than 6
      9.83s integrations. 
      
    DESCRIPTION OF ALGORITHM TO CALCULATE THE NUMBER OF UNFLAGGED ROWS
    The number of unflagged rows are only computed if listunfl=True. Computing these quantity
    can have a negative performance impact, especially for large datasets.
    The number of unflagged rows (the nUnflRows columns in the scans and fields portions of the listing) is
    calculated by summing the fractional unflagged bandwidth for each row (and hence why the number of unflagged
    rows, in general, is not an integer). Thus a row which has half of its
    total bandwidth flagged contributes 0.5 rows to the unflagged row count. A row with 20 of 32 channels of
    homogeneous width contributes 20/32 = 0.625 rows to the unflagged row count. A row with a value of False
    in the FLAG_ROW column is not counted in the number of unflagged rows.
 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'listobs'
        self.__globals__['taskname'] = 'listobs'
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
            myparams['selectdata'] = selectdata = self.parameters['selectdata']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['field'] = field = self.parameters['field']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['correlation'] = correlation = self.parameters['correlation']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['feed'] = feed = self.parameters['feed']
            myparams['array'] = array = self.parameters['array']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['verbose'] = verbose = self.parameters['verbose']
            myparams['listfile'] = listfile = self.parameters['listfile']
            myparams['listunfl'] = listunfl = self.parameters['listunfl']
            myparams['cachesize'] = cachesize = self.parameters['cachesize']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['selectdata'] = selectdata
        mytmp['spw'] = spw
        mytmp['field'] = field
        mytmp['antenna'] = antenna
        mytmp['uvrange'] = uvrange
        mytmp['timerange'] = timerange
        mytmp['correlation'] = correlation
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['feed'] = feed
        mytmp['array'] = array
        mytmp['observation'] = observation
        mytmp['verbose'] = verbose
        mytmp['listfile'] = listfile
        mytmp['listunfl'] = listunfl
        mytmp['cachesize'] = cachesize
        mytmp['overwrite'] = overwrite
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'listobs.xml')

        casalog.origin('listobs')
        try :
          #if not trec.has_key('listobs') or not casac.casac.utils().verify(mytmp, trec['listobs']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['listobs'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('listobs', 'listobs.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'listobs'
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
          result = listobs(vis, selectdata, spw, field, antenna, uvrange, timerange, correlation, scan, intent, feed, array, observation, verbose, listfile, listunfl, cachesize, overwrite)

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
             tname = 'listobs'
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
#        paramgui.runTask('listobs', myf['_ip'])
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
        a['selectdata']  = True
        a['verbose']  = True
        a['listfile']  = ''
        a['listunfl']  = False
        a['cachesize']  = 50

        a['selectdata'] = {
                    0:odict([{'value':True}, {'field':''}, {'spw':''}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'intent':''}, {'feed':''}, {'array':''}, {'uvrange':''}, {'observation':''}]), 
                    1:{'value':False}}
        a['listfile'] = {
                    0:odict([{'notvalue':''}, {'overwrite':False}])}

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
    def description(self, key='listobs', subkey=None):
        desc={'listobs': 'List the summary of a data set in the logger or in a file',
               'vis': 'Name of input visibility file (MS)',
               'selectdata': 'Data selection parameters',
               'spw': 'Selection based on spectral-window/frequency/channel.',
               'field': 'Selection based on field names or field index numbers. Default is all.',
               'antenna': 'Selection based on antenna/baselines. Default is all.',
               'uvrange': 'Selection based on uv range. Default: entire range. Default units: meters.',
               'timerange': 'Selection based on time range. Default is entire range.',
               'correlation': 'Selection based on correlation. Default is all.',
               'scan': 'Selection based on scan numbers. Default is all.',
               'intent': 'Selection based on observation intent. Default is all.',
               'feed': 'Selection based on multi-feed numbers: Not yet implemented',
               'array': 'Selection based on (sub)array numbers. Default is all.',
               'observation': 'Selection based on observation ID. Default is all.',
               'verbose': 'Controls level of information detail reported. True reports more than False.',
               'listfile': 'Name of disk file to write output. Default is none (output is written to logger only).',
               'listunfl': 'List unflagged row counts? If true, it can have significant negative performance impact.',
               'cachesize': 'EXPERIMENTAL. Maximum size in megabytes of cache in which data structures can be held.',
               'overwrite': 'If True, tacitly overwrite listfile if it exists.',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['selectdata']  = True
        a['spw']  = ''
        a['field']  = ''
        a['antenna']  = ''
        a['uvrange']  = ''
        a['timerange']  = ''
        a['correlation']  = ''
        a['scan']  = ''
        a['intent']  = ''
        a['feed']  = ''
        a['array']  = ''
        a['observation']  = ''
        a['verbose']  = True
        a['listfile']  = ''
        a['listunfl']  = False
        a['cachesize']  = 50
        a['overwrite']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['selectdata']  == True:
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['feed'] = ''
            a['array'] = ''
            a['uvrange'] = ''
            a['observation'] = ''

        if self.parameters['listfile']  != '':
            a['overwrite'] = False

        if a.has_key(paramname) :
              return a[paramname]
listobs_cli = listobs_cli_()
