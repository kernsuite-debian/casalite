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
from task_visstat import visstat
class visstat_cli_:
    __name__ = "visstat"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (visstat_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'axis':None, 'datacolumn':None, 'useflags':None, 'spw':None, 'field':None, 'selectdata':None, 'antenna':None, 'uvrange':None, 'timerange':None, 'correlation':None, 'scan':None, 'array':None, 'observation':None, 'timeaverage':None, 'timebin':None, 'timespan':None, 'maxuvwdistance':None, 'disableparallel':None, 'ddistart':None, 'taql':None, 'monolithic_processing':None, 'intent':None, 'reportingaxes':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, axis=None, datacolumn=None, useflags=None, spw=None, field=None, selectdata=None, antenna=None, uvrange=None, timerange=None, correlation=None, scan=None, array=None, observation=None, timeaverage=None, timebin=None, timespan=None, maxuvwdistance=None, disableparallel=None, ddistart=None, taql=None, monolithic_processing=None, intent=None, reportingaxes=None, ):

        """Displays statistical information from a MeasurementSet, or from a Multi-MS
        Arguments :
                vis: Name of MeasurementSet or Multi-MS
                   Default Value: 

                axis: Values on which to compute statistics
                   Default Value: amplitude
                   Allowed Values:
                                flag
                                antenna1
                                antenna2
                                feed1
                                feed2
                                field_id
                                array_id
                                data_desc_id
                                flag_row
                                interval
                                scan
                                scan_number
                                time
                                weight_spectrum
                                amp
                                amplitude
                                phase
                                real
                                imag
                                imaginary
                                uvrange

                datacolumn: Which data column to use (data, corrected, model, float_data)
                   Default Value: data
                   Allowed Values:
                                data
                                corrected
                                model
                                float_data

                useflags: Take flagging into account?
                   Default Value: True

                spw: spectral-window/frequency/channel
                   Default Value: 

                field: Field names or field index numbers: \'\'==>all, field=\'0~2,3C286\'
                   Default Value: 

                selectdata: More data selection parameters (antenna, timerange etc)
                   Default Value: True

                antenna: antenna/baselines: \'\'==>all, antenna = \'3,VA04\'
                   Default Value: 

                uvrange: uv range: \'\'==>all; uvrange = \'0~100klambda\', default units=meters
                   Default Value: 

                timerange: time range: \'\'==>all, timerange=\'09:14:0~09:54:0\'
                   Default Value: 

                correlation: Select data based on correlation
                   Default Value: 

                scan: scan numbers: \'\'==>all
                   Default Value: 

                array: (sub)array numbers: \'\'==>all
                   Default Value: 

                observation: observation ID number(s): \'\' = all
                   Default Value: 

                timeaverage: Average data in time.
                   Default Value: False

                timebin: Bin width for time averaging.
                   Default Value: 0s

                timespan: Span the timebin across scan, state or both.
                   Default Value: 

                maxuvwdistance: Maximum separation of start-to-end baselines that can be included in an average. (meters)
                   Default Value: 0.0

                intent: Select data by scan intent.
                   Default Value: 

                reportingaxes: Which reporting axis to use (ddid, field, integration)
                   Default Value: ddid
                   Allowed Values:
                                ddid
                                field
                                integration

        Returns: record

        Example :


      This task returns statistical information about data in a MeasurementSet
      or Multi-MS.

      The following statistics are computed: mean value, sum of values, sum of
      squared values, median, median absolute deviation, first and third
      quartiles, minimum, maximum, variance, standard deviation, and root mean
      square.

      Statistics may be computed on any of the following values: flag, antenna1,
      antenna2, feed1, feed2, field_id, array_id, data_desc_id, flag_row,
      interval, scan_number, time, weight_spectrum, amplitude, phase, real,
      imaginary, and uvrange (for the 'axis' parameter value, 'amp' is treated
      as an alias for amplitude, as are 'imag' for imaginary, and 'scan' for
      scan_number.)

      The 'reportingaxes' argument is used to partition the sample set along an
      axis. For example, setting its value to 'ddid' will result in the
      statistics of the chosen sample values partitioned by unique values of the
      data description id. Thus setting 'axis' to 'amp' and 'reportingaxes' to
      'ddid' will report statistics of visibility amplitudes for each unique
      value of data description id in the MeasurementSet.

      Optionally, the statistical information can be computed based only
      on a given subset of the MeasurementSet.

      Note: If the MS consists of inhomogeneous data, for example several
      spectral windows each having a different number of channels, it may be
      necessary to use selection parameters to select a homogeneous subset of
      the MS, e.g. spw='2'.

      Keyword arguments:

            vis  --- Name of input MeasurementSet or Multi-MS
                  default: '', example: vis='my.ms'

            axis -- Which data to analyze.

                  default: 'amplitude'
                  axis='phase'
                  axis='imag'
                  axis='scan_number'
                  axis='flag'

                  The phase of a complex number is in radians in the range [-pi; pi].


            datacolumn -- Which data column to use for complex data.
                  default: 'data'
                  datacolumn='data'
                  datacolumn='corrected'
                  datacolumn='model'
                  datacolumn='float_data'

            useflags -- Take MS flags into account?
                  default: True
                  useflags=False
                  useflags=True
                  If useflags=False, flagged values are included in the statistics.
                  If useflags=True, any flagged values are not used in the statistics.

            spw -- Select data based on spectral window and channels
                  default: '' (all); example: spw='1'
                  spw='<2' #spectral windows less than 2
                  spw='>1' #spectral windows greater than 1
                  spw='0:0~10' # first 10 channels from spw 0
                  spw='0:0~5;56~60' # multiple separated channel chunks.

            field -- Select data based on field id(s) or name(s)
                  default: '' (all); example: field='1'
                  field='0~2' # field ids inclusive from 0 to 2
                  field='3C*' # all field names starting with 3C

            selectdata -- Other data selection parameters
                  default: True
            antenna -- Select data based on baseline
                  default: '' (all); example: antenna='5&6' baseline 5-6
                  antenna='5&6;7&8' #baseline 5-6 and 7-8
                  antenna='5' # all baselines with antenna 5
                  antenna='5,6' # all baselines with antennas 5 and 6
            correlation -- Correlation types
                  default: '' (all);
                  example: correlation='RR LL'
            uvrange -- Select data within uvrange (default units meters)
                  default: '' (all); example:
                  uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                  uvrange='>4klambda';uvranges greater than 4 kilo-lambda
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
            array -- Selection based on the antenna array
                  observation -- Selection by observation ID(s).
                  default: '' (all); example: observation='1~3'




            --- Time averaging parameters ---
            timeaverage -- Average data in time. Flagged data will be included in the
            average calculation, unless the parameter useflags is set to True. In this
            case only partially flagged rows will be used in the average.
            default: False

            timebin -- Bin width for time averaging.
                  default: '0s'

            timespan -- Let the timebin span across scan, state or both.
                        State is equivalent to sub-scans. One scan may have several
                        state ids. For ALMA MSs, the sub-scans are limited to about
                        30s duration each. In these cases, the task will automatically
                        add state to the timespan parameter. To see the number of states
                        in an MS, use the msmd tool. See help msmd.

                  default: '' (separate time bins by both of the above)
                  options: 'scan', 'state', 'state,scan'

                  examples:
                        timespan = 'scan'; can be useful when the scan number
                        goes up with each integration as in many WSRT MSs.
                        timespan = ['scan', 'state']: disregard scan and state
                        numbers when time averaging.
                        timespan = 'state,scan'; same as above.

            maxuvwdistance -- Provide a maximum separation of start-to-end baselines
                              that can be included in an average. (int)
                  default: 0.0 (given in meters)







        
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'visstat'
        self.__globals__['taskname'] = 'visstat'
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
            myparams['axis'] = axis = self.parameters['axis']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']
            myparams['useflags'] = useflags = self.parameters['useflags']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['field'] = field = self.parameters['field']
            myparams['selectdata'] = selectdata = self.parameters['selectdata']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['correlation'] = correlation = self.parameters['correlation']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['array'] = array = self.parameters['array']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['timeaverage'] = timeaverage = self.parameters['timeaverage']
            myparams['timebin'] = timebin = self.parameters['timebin']
            myparams['timespan'] = timespan = self.parameters['timespan']
            myparams['maxuvwdistance'] = maxuvwdistance = self.parameters['maxuvwdistance']
            myparams['disableparallel'] = disableparallel = self.parameters['disableparallel']
            myparams['ddistart'] = ddistart = self.parameters['ddistart']
            myparams['taql'] = taql = self.parameters['taql']
            myparams['monolithic_processing'] = monolithic_processing = self.parameters['monolithic_processing']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['reportingaxes'] = reportingaxes = self.parameters['reportingaxes']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['axis'] = axis
        mytmp['datacolumn'] = datacolumn
        mytmp['useflags'] = useflags
        mytmp['spw'] = spw
        mytmp['field'] = field
        mytmp['selectdata'] = selectdata
        mytmp['antenna'] = antenna
        mytmp['uvrange'] = uvrange
        mytmp['timerange'] = timerange
        mytmp['correlation'] = correlation
        mytmp['scan'] = scan
        mytmp['array'] = array
        mytmp['observation'] = observation
        mytmp['timeaverage'] = timeaverage
        mytmp['timebin'] = timebin
        mytmp['timespan'] = timespan
        mytmp['maxuvwdistance'] = maxuvwdistance
        mytmp['disableparallel'] = disableparallel
        mytmp['ddistart'] = ddistart
        mytmp['taql'] = taql
        mytmp['monolithic_processing'] = monolithic_processing
        mytmp['intent'] = intent
        mytmp['reportingaxes'] = reportingaxes
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'visstat.xml')

        casalog.origin('visstat')
        try :
          #if not trec.has_key('visstat') or not casac.casac.utils().verify(mytmp, trec['visstat']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['visstat'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('visstat', 'visstat.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'visstat'
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
          result = visstat(vis, axis, datacolumn, useflags, spw, field, selectdata, antenna, uvrange, timerange, correlation, scan, array, observation, timeaverage, timebin, timespan, maxuvwdistance, disableparallel, ddistart, taql, monolithic_processing, intent, reportingaxes)

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
             tname = 'visstat'
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
#        paramgui.runTask('visstat', myf['_ip'])
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
        a['axis']  = 'amplitude'
        a['useflags']  = True
        a['spw']  = ''
        a['field']  = ''
        a['selectdata']  = True
        a['timeaverage']  = False
        a['intent']  = ''
        a['reportingaxes']  = 'ddid'

        a['axis'] = {
                    0:odict([{'value':'amp'}, {'datacolumn':'data'}]), 
                    1:odict([{'value':'amplitude'}, {'datacolumn':'data'}]), 
                    2:odict([{'value':'phase'}, {'datacolumn':'data'}]), 
                    3:odict([{'value':'real'}, {'datacolumn':'data'}]), 
                    4:odict([{'value':'imag'}, {'datacolumn':'data'}]), 
                    5:odict([{'value':'imaginary'}, {'datacolumn':'data'}])}
        a['selectdata'] = {
                    0:odict([{'value':True}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'array':''}, {'observation':''}, {'uvrange':''}]), 
                    1:{'value':False}}
        a['timeaverage'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'timebin':'0s'}, {'timespan':''}, {'maxuvwdistance':0.0}])}

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
    def description(self, key='visstat', subkey=None):
        desc={'visstat': 'Displays statistical information from a MeasurementSet, or from a Multi-MS',
               'vis': 'Name of MeasurementSet or Multi-MS',
               'axis': 'Values on which to compute statistics',
               'datacolumn': 'Which data column to use (data, corrected, model, float_data)',
               'useflags': 'Take flagging into account?',
               'spw': 'spectral-window/frequency/channel',
               'field': 'Field names or field index numbers: \'\'==>all, field=\'0~2,3C286\'',
               'selectdata': 'More data selection parameters (antenna, timerange etc)',
               'antenna': 'antenna/baselines: \'\'==>all, antenna = \'3,VA04\'',
               'uvrange': 'uv range: \'\'==>all; uvrange = \'0~100klambda\', default units=meters',
               'timerange': 'time range: \'\'==>all, timerange=\'09:14:0~09:54:0\'',
               'correlation': 'Select data based on correlation',
               'scan': 'scan numbers: \'\'==>all',
               'array': '(sub)array numbers: \'\'==>all',
               'observation': 'observation ID number(s): \'\' = all',
               'timeaverage': 'Average data in time.',
               'timebin': 'Bin width for time averaging.',
               'timespan': 'Span the timebin across scan, state or both.',
               'maxuvwdistance': 'Maximum separation of start-to-end baselines that can be included in an average. (meters)',
               'disableparallel': 'Hidden parameter for internal use only. Do not change it!',
               'ddistart': 'Hidden parameter for internal use only. Do not change it!',
               'taql': 'Table query for nested selections',
               'monolithic_processing': 'Hidden parameter for internal use only. Do not change it!',
               'intent': 'Select data by scan intent.',
               'reportingaxes': 'Which reporting axis to use (ddid, field, integration)',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['axis']  = 'amplitude'
        a['datacolumn']  = 'data'
        a['useflags']  = True
        a['spw']  = ''
        a['field']  = ''
        a['selectdata']  = True
        a['antenna']  = ''
        a['uvrange']  = ''
        a['timerange']  = ''
        a['correlation']  = ''
        a['scan']  = ''
        a['array']  = ''
        a['observation']  = ''
        a['timeaverage']  = False
        a['timebin']  = '0s'
        a['timespan']  = ''
        a['maxuvwdistance']  = 0.0
        a['disableparallel']  = False
        a['ddistart']  = -1
        a['taql']  = ''
        a['monolithic_processing']  = False
        a['intent']  = ''
        a['reportingaxes']  = 'ddid'

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['axis']  == 'amp':
            a['datacolumn'] = 'data'

        if self.parameters['axis']  == 'amplitude':
            a['datacolumn'] = 'data'

        if self.parameters['axis']  == 'phase':
            a['datacolumn'] = 'data'

        if self.parameters['axis']  == 'real':
            a['datacolumn'] = 'data'

        if self.parameters['axis']  == 'imag':
            a['datacolumn'] = 'data'

        if self.parameters['axis']  == 'imaginary':
            a['datacolumn'] = 'data'

        if self.parameters['selectdata']  == True:
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['array'] = ''
            a['observation'] = ''
            a['uvrange'] = ''

        if self.parameters['timeaverage']  == True:
            a['timebin'] = '0s'
            a['timespan'] = ''
            a['maxuvwdistance'] = 0.0

        if a.has_key(paramname) :
              return a[paramname]
visstat_cli = visstat_cli_()
