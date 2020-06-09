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
from task_hanningsmooth import hanningsmooth
class hanningsmooth_cli_:
    __name__ = "hanningsmooth"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (hanningsmooth_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'outputvis':None, 'keepmms':None, 'field':None, 'spw':None, 'scan':None, 'antenna':None, 'correlation':None, 'timerange':None, 'intent':None, 'array':None, 'uvrange':None, 'observation':None, 'feed':None, 'datacolumn':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, outputvis=None, keepmms=None, field=None, spw=None, scan=None, antenna=None, correlation=None, timerange=None, intent=None, array=None, uvrange=None, observation=None, feed=None, datacolumn=None, ):

        """Hanning smooth frequency channel data to remove Gibbs ringing

        Detailed Description:

The hanningsmooth task uses the MSTransform framework underneath but
keeps roughly the same interface as the old hanningsmooth task.

This function Hanning smooths the frequency channels with a weighted
running average. The weights are 0.5 for the central channel and 0.25
for each of the two adjacent channels. The first and last channels are
flagged. Inclusion of a flagged value in an average causes that data
value to be flagged. 

If the 'CORRECTED' data column is requested for an MS that does not
contain this column, it will use 'DATA' to calculate the smoothing and
save it to 'DATA' in the output MS.

WARNING: by default, all visibility columns will be smoothed. 

        Arguments :
                vis: Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'

                   Default Value: 

                outputvis: Name of output visibility file
                     Default: '' (same as vis)

                        Example: outputvis='ngc5921_out.ms'

                   Default Value: 

                keepmms: Create a Multi-MS as the output if the input is a
Multi-MS.

                     Default: True
                     Options: True|False

                     By default it will create a Multi-MS when the
                     input is a Multi-MS. The output Multi-MS will
                     have the same partition axis of the input
                     MMS. See CASA Docs for more information on
                     the MMS format.

                   Default Value: True

                field: Select field using field id(s) or field name(s)
                     Default: '' (all fields)
                     
                     Use 'go listobs' to obtain the list id's or
                     names. If field string is a non-negative integer,
                     it is assumed a field index,  otherwise, it is
                     assumed a field name.

                        Examples:
                        field='0~2'; field ids 0,1,2
                        field='0,4,5~7'; field ids 0,4,5,6,7
                        field='3C286,3C295'; field named 3C286 and
                        3C295
                        field = '3,4C*'; field id 3, all names
                        starting with 4C

                   Default Value: 

                spw: Select spectral window/channels
                     Default: ''=all spectral windows and channels
           
                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                        spw='<2';  spectral windows less than 2 (i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
                        3 - chans 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
                        through 6 in each.
                        spw = '*:3~64'  channels 3 through 64 for all sp id's
                        spw = ' :3~64' will NOT work.

                     NOTE: mstransform does not support multiple
                     channel ranges per spectral window (';').

                   Default Value: 

                scan: Scan number range
                     Subparameter of selectdata=True
                     Default: '' = all

                   Default Value: 

                antenna: Select data based on antenna/baseline
                     Subparameter of selectdata=True
                     Default: '' (all)

                     If antenna string is a non-negative integer, it
                     is assumed an antenna index, otherwise, it is
                     assumed as an antenna name
  
                         Examples: 
                         antenna='5&6'; baseline between antenna
                         index 5 and index 6.
                         antenna='VA05&VA06'; baseline between VLA
                         antenna 5 and 6.
                         antenna='5&6;7&8'; baselines with
                         indices 5-6 and 7-8
                         antenna='5'; all baselines with antenna index
                         5
                         antenna='05'; all baselines with antenna
                         number 05 (VLA old name)
                         antenna='5,6,10'; all baselines with antennas
                         5,6,10 index numbers
                          antenna='!ea03,ea12,ea17': all baselines
                          except those that include EVLA antennas
                          ea03, ea12, or ea17.

                   Default Value: 

                correlation: Select data based on correlation
                     Default: '' ==> all

                        Example: correlation="XX,YY".

                   Default Value: 

                timerange: Select data based on time range
                     Subparameter of selectdata=True
                     Default = '' (all)

                        Examples:
                        timerange =
                        'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                        (Note: if YYYY/MM/DD is missing date defaults
                        to first day in data set.)
                        timerange='09:14:0~09:54:0' picks 40 min on
                        first day 
                        timerange= '25:00:00~27:30:00' picks 1 hr to 3
                        hr 30min on NEXT day
                        timerange='09:44:00' pick data within one
                        integration of time
                        timerange='>10:24:00' data after this time

                   Default Value: 

                intent: Select observing intent
                     Default: '' (no selection by intent)

                        Example: intent='*BANDPASS*'  (selects data
                        labelled with BANDPASS intent)

                   Default Value: 

                array: (Sub)array number range
                     Default: '' (all)

                   Default Value: 

                uvrange: Select data by baseline length.
                     Default = '' (all)

                        Examples:
                        uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                        uvrange='>4klambda';uvranges greater than 4 kilo-lambda
                        uvrange='0~1000km'; uvrange in kilometers

                   Default Value: 

                observation: Select by observation ID(s)
                     Subparameter of selectdata=True
                     Default: '' = all

                         Example: observation='0~2,4'

                   Default Value: 

                feed: Selection based on the feed 
                     NOT IMPLEMENTED YET!
                     Default: '' = all

                   Default Value: 

                datacolumn: Which data column(s) to use for processing
                     (case-insensitive).
                     Default: 'all' (= whichever of the options that
                     are present)
                     Options: 'data', 'model', 'corrected',
                     'all','float_data', 'lag_data',
                     'float_data,data', 'lag_data,data'

                        Example: datacolumn='data'

                   Default Value: all
                   Allowed Values:
                                all
                                corrected
                                data
                                model
                                data,model,corrected
                                float_data
                                lag_data
                                float_data,data
                                lag_data,data


        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF HANNINGSMOOTH IN CASA DOCS:
https://casa.nrao.edu/casadocs/
 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'hanningsmooth'
        self.__globals__['taskname'] = 'hanningsmooth'
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
            myparams['keepmms'] = keepmms = self.parameters['keepmms']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['correlation'] = correlation = self.parameters['correlation']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['array'] = array = self.parameters['array']
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['feed'] = feed = self.parameters['feed']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['outputvis'] = outputvis
        mytmp['keepmms'] = keepmms
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['scan'] = scan
        mytmp['antenna'] = antenna
        mytmp['correlation'] = correlation
        mytmp['timerange'] = timerange
        mytmp['intent'] = intent
        mytmp['array'] = array
        mytmp['uvrange'] = uvrange
        mytmp['observation'] = observation
        mytmp['feed'] = feed
        mytmp['datacolumn'] = datacolumn
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'hanningsmooth.xml')

        casalog.origin('hanningsmooth')
        try :
          #if not trec.has_key('hanningsmooth') or not casac.casac.utils().verify(mytmp, trec['hanningsmooth']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['hanningsmooth'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('hanningsmooth', 'hanningsmooth.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'hanningsmooth'
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
          result = hanningsmooth(vis, outputvis, keepmms, field, spw, scan, antenna, correlation, timerange, intent, array, uvrange, observation, feed, datacolumn)

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
             tname = 'hanningsmooth'
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
#        paramgui.runTask('hanningsmooth', myf['_ip'])
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
        a['keepmms']  = True
        a['field']  = ''
        a['spw']  = ''
        a['scan']  = ''
        a['antenna']  = ''
        a['correlation']  = ''
        a['timerange']  = ''
        a['intent']  = ''
        a['array']  = ''
        a['uvrange']  = ''
        a['observation']  = ''
        a['feed']  = ''
        a['datacolumn']  = 'all'


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
    def description(self, key='hanningsmooth', subkey=None):
        desc={'hanningsmooth': 'Hanning smooth frequency channel data to remove Gibbs ringing',
               'vis': 'Name of input visibility file',
               'outputvis': 'Name of output visibility file',
               'keepmms': 'Create a Multi-MS as the output if the input is a Multi-MS.',
               'field': 'Select field using field id(s) or field name(s)',
               'spw': 'Select spectral window/channels',
               'scan': 'Scan number range',
               'antenna': 'Select data based on antenna/baseline',
               'correlation': 'Select data based on correlation',
               'timerange': 'Select data based on time range',
               'intent': 'Select observing intent',
               'array': 'Select (sub)array(s) by array ID number.',
               'uvrange': 'Select data by baseline length.',
               'observation': 'Select by observation ID(s)',
               'feed': 'Multi-feed numbers: Not yet implemented.',
               'datacolumn': 'Which data column(s) to use for processing',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['outputvis']  = ''
        a['keepmms']  = True
        a['field']  = ''
        a['spw']  = ''
        a['scan']  = ''
        a['antenna']  = ''
        a['correlation']  = ''
        a['timerange']  = ''
        a['intent']  = ''
        a['array']  = ''
        a['uvrange']  = ''
        a['observation']  = ''
        a['feed']  = ''
        a['datacolumn']  = 'all'

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
hanningsmooth_cli = hanningsmooth_cli_()
