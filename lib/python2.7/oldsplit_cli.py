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
from task_oldsplit import oldsplit
class oldsplit_cli_:
    __name__ = "oldsplit"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (oldsplit_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'outputvis':None, 'datacolumn':None, 'field':None, 'spw':None, 'width':None, 'antenna':None, 'timebin':None, 'timerange':None, 'array':None, 'uvrange':None, 'scan':None, 'intent':None, 'correlation':None, 'observation':None, 'combine':None, 'keepflags':None, 'keepmms':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, outputvis=None, datacolumn=None, field=None, spw=None, width=None, antenna=None, timebin=None, timerange=None, array=None, uvrange=None, scan=None, intent=None, correlation=None, observation=None, combine=None, keepflags=None, keepmms=None, ):

        """Create a visibility subset from an existing visibility set

        Detailed Description:


    T H I S   T A S K   I S    D E P R E C A T E D
    I T   W I L L   B E   R E M O V E D   S O O N

Oldsplit is the general purpose program to make a new data set that is a
subset or averaged form of an existing data set. Oldsplit is often used after the initial calibration of the data to make a
smaller measurement set with only the data that will be used in
further flagging, imaging and/or self-calibration. Oldsplit includes
general selection parameters and can average over frequency (channels) and time (integrations).


        Arguments :
                vis: Name of input MeasurementSet
               Default: none;
                 Example: vis='ngc5921.ms'

                   Default Value: 

                outputvis: Name of output measurement set
               Default: none;
                 Example: outputvis='ngc5921_src.ms'

                   Default Value: 

                datacolumn: Data column(s) to Oldsplit out
                Default='corrected';
                Options: 'data', 'model', 'corrected', 'all',
                'float_data', 'lag_data', 'float_data,data', and
                'lag_data,data'.
                  Example: datacolumn='data'

                  Note: 'all' = whichever of the above that are
                  present. Otherwise the selected column will go to
                  DATA (or FLOAT_DATA) in the output. Splitting with
                  the default datacolumn='corrected' before clean is
                  normally required for self-calibration!

                   Default Value: corrected
                   Allowed Values:
                                data
                                corrected
                                model
                                data,model,corrected
                                float_data
                                lag_data
                                float_data,data
                                lag_data,data
                                all

                field: Select field using ID(s) or name(s)
                (Run listobs to obtain list of field IDs and names)
                Default: ''=all fields.
                If field string is a non-negative integer, it is
                assumed to be a field index otherwise, it is assumed
                to be a field name.

                  Examples:
                  field='0~2'; field ids 0,1,2
                  field='0,4,5~7'; field ids 0,4,5,6,7
                  field='3C286,3C295'; fields named 3C286 and 3C295
                  field = '3,4C*'; field id 3, all names starting with
                  4C

                   Default Value: 

                spw: Select spectral window/channels
                Default: ''=all spectral windows and channels

                  Examples:
                  spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                  spw='<2';  spectral windows less than 2 (i.e. 0,1)
                  spw='0:5~61'; spw 0, channels 5 to 61
                  spw='0,10,3:3~45'; spw 0,10 all channels, spw 3 - chans 3 to 45.
                  spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
                  spw = '*:3~64'  channels 3 through 64 for all sp id's
                  spw = ' :3~64' will NOT work.

                    Note: Oldsplit does not support multiple channel
                    ranges per spectral window (';') because it is not
                    clear whether to keep the ranges in the original
                    spectral window or make a new spectral window for
                    each additional range.

                   Default Value: 

                width: Number of channels to average to form one output channel
               Default: '1' => no channel averaging
                 Example: width=[2,3] => average 2 channels of 1s
                 spectral window selected and 3 in the second one.

                   Default Value: 1

                antenna: Select data based on antenna/baseline
               Default: '' (all)
               Non-negative integers are assumed to be antenna
               indices, and anything else is taken as an antenna name.

                 Examples:
                 antenna='5&6': baseline between antenna index 5 and index 6.
                 antenna='VA05&VA06': baseline between VLA antenna 5 and 6.
                 antenna='5&6;7&8': baselines 5-6 and 7-8
                 antenna='5': all baselines with antenna 5
                 antenna='5,6,10': all baselines including antennas 5, 6, or 10
                 antenna='5,6,10&': all baselines
                 with *only* antennas 5, 6, or 10.
                 (cross-correlations only.  Use
                 && to include
                 autocorrelations, and &&&
                 to get only autocorrelations.)
                 antenna='!ea03,ea12,ea17': all
                 baselines except those that include EVLA antennas
                 ea03, ea12, or ea17.

                   Default Value: 

                timebin: Interval for time averaging
               Default: '0s' or '-1s' (no averaging)
                 Example: timebin='30s'
                 '10' means '10s'

                   Default Value: 0s

                timerange: Select data by time range
               timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
               Note: if YYYY/MM/DD is missing date, timerange defaults
               to the first day in the dataset.

               Default = '' (all); examples,

                 Examples:
                 timerange='09:14:0~09:54:0' picks 40 min on first day
                 timerange='25:00:00~27:30:00' picks 1
                 hr to 3 hr 30min on next day
                 timerange='09:44:00' data within one integration of time
                 timerange='>10:24:00' data after this time

                   Default Value: 

                array: Select (sub)array(s) by array ID number
               Default: ''=all

                   Default Value: 

                uvrange: Select data by baseline length (default units meters)
               Default: ''=all

                  Examples:
                  uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                  uvrange='>4klambda';uvranges greater than 4 kilo-lambda
                  uvrange='0~1000km'; uvrange in kilometers

                   Default Value: 

                scan: Select data by scan numbers
               Default: ''=all

                   Default Value: 

                intent: Select data by scan intents
               Default: '' = all

                 Examples:
                 intent = 'CALIBRATE_ATMOSPHERE_REFERENCE'
                 intent = 'calibrate_atmosphere_reference'.upper() # same as above
                 # Select states that include one or
                 both of CALIBRATE_WVR.REFERENCE or OBSERVE_TARGET_ON_SOURCE.
                 intent = 'CALIBRATE_WVR.REFERENCE, OBSERVE_TARGET_ON_SOURCE'

                   Default Value: 

                correlation: Select correlations
               Default: '' = all

                 Examples:
                 correlation = 'rr, ll'
                 correlation = ['XY', 'YX'].

                   Default Value: 

                observation: Select by observation ID(s)
               Default: '' = all

                   Default Value: 

                combine: Let time bins span changes in scan and/or state
               Default = '' (separate time bins by both of the above)

                  Examples:
                  combine = 'scan': Can be useful when the scan number
                  goes up with each integration, as in many WSRT MSs.
                  combine = ['scan', 'state']: disregard
                  scan and state numbers when time averaging.
                  combine = 'state,scan': Same as above.

                   Default Value: 

                keepflags: If practical, keep *completely flagged rows* instead of
dropping them.
               This has absolutely no effect on averaging
               calculations, or partially flagged rows.  All of the
               channels and correlations of a row must be flagged for
               it to be droppable, and a row must be well defined to
               be keepable.  The latter condition means that this
               option has no effect on time averaging - in that case
               fully flagged rows are automatically
               omitted. Regardless of this parameter, flagged data is
               never included in averaging calculations.

               The only time keepflags matters is if
               1. the input MS has some completely flagged rows
               and
               2. time averaging is not being done.

               Then, if keepflags is False, the completely flagged
               rows will be omitted from the output MS.  Otherwise,
               they will be included (subject to the selection
               parameters).

                   Default Value: True

                keepmms: If the input is a multi-MS, make the output one,
too. (experimental)
               Default: False => the output will be a normal MS
               without partitioning.

                   Default Value: False


        Example :


For more information, see the oldsplit task-list pages in the CASA
documentation "CASA Docs":

https://casa.nrao.edu/casadocs/


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'oldsplit'
        self.__globals__['taskname'] = 'oldsplit'
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
            myparams['outputvis'] = outputvis = self.parameters['outputvis']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['width'] = width = self.parameters['width']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['timebin'] = timebin = self.parameters['timebin']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['array'] = array = self.parameters['array']
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['correlation'] = correlation = self.parameters['correlation']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['combine'] = combine = self.parameters['combine']
            myparams['keepflags'] = keepflags = self.parameters['keepflags']
            myparams['keepmms'] = keepmms = self.parameters['keepmms']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['outputvis'] = outputvis
        mytmp['datacolumn'] = datacolumn
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['width'] = width
        mytmp['antenna'] = antenna
        mytmp['timebin'] = timebin
        mytmp['timerange'] = timerange
        mytmp['array'] = array
        mytmp['uvrange'] = uvrange
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['correlation'] = correlation
        mytmp['observation'] = observation
        mytmp['combine'] = combine
        mytmp['keepflags'] = keepflags
        mytmp['keepmms'] = keepmms
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'oldsplit.xml')

        casalog.origin('oldsplit')
        try :
          #if not trec.has_key('oldsplit') or not casac.casac.utils().verify(mytmp, trec['oldsplit']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['oldsplit'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('oldsplit', 'oldsplit.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'oldsplit'
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
          result = oldsplit(vis, outputvis, datacolumn, field, spw, width, antenna, timebin, timerange, array, uvrange, scan, intent, correlation, observation, combine, keepflags, keepmms)

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
             tname = 'oldsplit'
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
#        paramgui.runTask('oldsplit', myf['_ip'])
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
        a['outputvis']  = ''
        a['datacolumn']  = 'corrected'
        a['field']  = ''
        a['spw']  = ''
        a['width']  = 1
        a['antenna']  = ''
        a['timebin']  = '0s'
        a['timerange']  = ''
        a['array']  = ''
        a['uvrange']  = ''
        a['scan']  = ''
        a['intent']  = ''
        a['correlation']  = ''
        a['observation']  = ''
        a['keepflags']  = True
        a['keepmms']  = False

        a['timebin'] = {
                    0:odict([{'notvalue':'0s'}, {'combine':''}])}

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
    def description(self, key='oldsplit', subkey=None):
        desc={'oldsplit': 'Create a visibility subset from an existing visibility set',
               'vis': 'Name of input measurement set',
               'outputvis': 'Name of output measurement set',
               'datacolumn': 'Data column(s) to Oldsplit out',
               'field': 'Select field using ID(s) or name(s)',
               'spw': 'Select spectral window/channels',
               'width': 'Number of channels to average to form one output channel',
               'antenna': 'Select data based on antenna/baseline',
               'timebin': 'Interval for time averaging',
               'timerange': 'Select data by time range',
               'array': 'Select (sub)array(s) by array ID number',
               'uvrange': 'Select data by baseline length (default units meters)',
               'scan': 'Select data by scan numbers',
               'intent': 'Select data by scan intents',
               'correlation': 'Select correlations',
               'observation': 'Select by observation ID(s)',
               'combine': 'Let time bins span changes in scan and/or stat',
               'keepflags': 'If practical, keep *completely flagged rows* instead of dropping them.',
               'keepmms': 'If the input is a multi-MS, make the output one,too.',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['outputvis']  = ''
        a['datacolumn']  = 'corrected'
        a['field']  = ''
        a['spw']  = ''
        a['width']  = 1
        a['antenna']  = ''
        a['timebin']  = '0s'
        a['timerange']  = ''
        a['array']  = ''
        a['uvrange']  = ''
        a['scan']  = ''
        a['intent']  = ''
        a['correlation']  = ''
        a['observation']  = ''
        a['combine']  = ''
        a['keepflags']  = True
        a['keepmms']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['timebin']  != '0s':
            a['combine'] = ''

        if a.has_key(paramname) :
              return a[paramname]
oldsplit_cli = oldsplit_cli_()
