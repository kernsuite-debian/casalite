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
from task_partition import partition
class partition_cli_:
    __name__ = "partition"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (partition_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'outputvis':None, 'createmms':None, 'separationaxis':None, 'numsubms':None, 'flagbackup':None, 'datacolumn':None, 'field':None, 'spw':None, 'scan':None, 'antenna':None, 'correlation':None, 'timerange':None, 'intent':None, 'array':None, 'uvrange':None, 'observation':None, 'feed':None, 'disableparallel':None, 'ddistart':None, 'taql':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, outputvis=None, createmms=None, separationaxis=None, numsubms=None, flagbackup=None, datacolumn=None, field=None, spw=None, scan=None, antenna=None, correlation=None, timerange=None, intent=None, array=None, uvrange=None, observation=None, feed=None, disableparallel=None, ddistart=None, taql=None, ):

        """Task to produce Multi-MSs using parallelism

        Detailed Description:

    Partition is a task to create a Multi-MS out of an MS. General selection
    parameters are included, and one or all of the various data columns
    (DATA, LAG_DATA and/or FLOAT_DATA, and possibly MODEL_DATA and/or
    CORRECTED_DATA) can be selected.
    
    The partition task creates a Multi-MS in parallel, using the CASA MPI framework.
    The user should start CASA as follows in order to run it in parallel.
    
    1) Start CASA on a single node with 8 engines. The first engine will be used as the
       MPIClient, where the user will see the CASA prompt. All other engines will be used
       as MPIServers and will process the data in parallel.
           mpicasa -n 8 casa --nogui --log2term
           partition(.....)
        
    2) Running on a group of nodes in a cluster.
           mpicasa -hostfile user_hostfile casa ....
           partition(.....)
            
        where user_hostfile contains the names of the nodes and the number of engines to use 
        in each one of them. Example:
            pc001234a, slots=5
            pc001234b, slots=4
     
    If CASA is started without mpicasa, it is still possible to create an MMS, but
    the processing will be done in sequential.

    A multi-MS is structured to have a reference MS on the top directory and a
    sub-directory called SUBMSS, which contain each partitioned sub-MS. The
    reference MS contains links to the sub-tables of the first sub-MS. The other
    sub-MSs contain a copy of the sub-tables each. A multi-MS looks like this in disk.

    ls ngc5921.mms
    ANTENNA           FLAG_CMD     POLARIZATION  SPECTRAL_WINDOW  table.dat
    DATA_DESCRIPTION  HISTORY      PROCESSOR     STATE            table.info
    FEED              OBSERVATION  SORTED_TABLE  SUBMSS           WEATHER
    FIELD             POINTING     SOURCE        SYSCAL

    ls ngc5921.mms/SUBMSS/
    ngc5921.0000.ms/  ngc5921.0002.ms/  ngc5921.0004.ms/  ngc5921.0006.ms/
    ngc5921.0001.ms/  ngc5921.0003.ms/  ngc5921.0005.ms/

    Inside casapy, one can use the task listpartition to list the information
    from a multi-MS.
    
    When partition processes an MMS in parallel, each sub-MS is processed independently in an engine.
    The log messages of the engines are identified by the string MPIServer-#, where # gives the number
    of the engine running that process. When the task runs sequentially, it shows the MPIClient text
    in the origin of the log messages or does not show anything.
      

        Arguments :
                vis: Name of input measurement set
                   Default Value: 

                outputvis: Name of output measurement set
                   Default Value: 

                createmms: Should this create a multi-MS output
                   Default Value: True

                separationaxis: Axis to do parallelization across(scan, spw, baseline, auto)
                   Default Value: auto
                   Allowed Values:
                                auto
                                scan
                                spw
                                baseline

                numsubms: The number of SubMSs to create (auto or any number)
                   Default Value: auto

                flagbackup: Create a backup of the FLAG column in the MMS.
                   Default Value: True

                datacolumn: Which data column(s) to process.
                   Default Value: all
                   Allowed Values:
                                all
                                data
                                corrected
                                model
                                data,model,corrected
                                float_data
                                lag_data
                                float_data,data
                                lag_data,data

                field: Select field using ID(s) or name(s).
                   Default Value: 

                spw: Select spectral window/channels.
                   Default Value: 

                scan: Select data by scan numbers.
                   Default Value: 

                antenna: Select data based on antenna/baseline.
                   Default Value: 

                correlation: Correlation: '' ==> all, correlation="XX,YY".
                   Default Value: 

                timerange: Select data by time range.
                   Default Value: 

                intent: Select data by scan intent.
                   Default Value: 

                array: Select (sub)array(s) by array ID number.
                   Default Value: 

                uvrange: Select data by baseline length.
                   Default Value: 

                observation: Select by observation ID(s).
                   Default Value: 

                feed: Multi-feed numbers: Not yet implemented.
                   Default Value: 


        Example :



----- Detailed description of keyword arguments -----
    
    vis -- Name of input visibility file
        default: none; example: vis='ngc5921.ms'

    outputvis -- Name of output visibility file
        default: none; example: outputvis='ngc5921.mms'

    createmms -- Create a multi-MS as the output.
        default: True
        If False, it will work like the split task and create a
        normal MS, split according to the given data selection parameters.
        Note that, when this parameter is set to False, a cluster
        will not be used.

        separationaxis -- Axis to do parallelization across. 
            default: 'auto'
            Options: 'scan', 'spw', 'baseline', 'auto'

            * The 'auto' option will partition per scan/spw to obtain optimal load balancing with the
             following criteria:
    
               1 - Maximize the scan/spw/field distribution across sub-MSs
               2 - Generate sub-MSs with similar size

            * The 'scan' or 'spw' axes will partition the MS into scan or spw. The individual sub-MSs may
            not be balanced with respect to the number of rows.

            * The 'baseline' axis is mostly useful for Single-Dish data. This axis will partition the MS
              based on the available baselines. If the user wants only auto-correlations, use the
              antenna selection such as antenna='*&&&' together with this separation axis. Note that in
              if numsubms='auto', partition will try to create as many subMSs as the number of available
              servers in the cluster. If the user wants to have one subMS for each baseline, set the numsubms
              parameter to a number higher than the number of baselines to achieve this.        
               
        numsubms -- The number of sub-MSs to create.
            default: 'auto'
            Options: any integer number (example: numsubms=4)
    
               The default 'auto' is to partition using the number of available servers in the cluster.
               If the task is unable to determine the number of running servers, or the user did not start CASA
               using mpicasa, numsubms will use 8 as the default.

                Example: Launch CASA with 5 engines, where 4 of them will be used to create the MMS. The first
                    engine is used as the MPIClient.
      
                mpicasa -n 5 casa --nogui --log2term
                CASA> partition('uid__A1', outputvis='test.mms')

        flagbackup -- Make a backup of the FLAG column of the output MMS. When the
                      MMS is created, the .flagversions of the input MS are not transferred,
                      therefore it is necessary to re-create it for the new MMS. Note
                      that multiple backups from the input MS will not be preserved. This
                      will create a single backup of all the flags present in the input
                      MS at the time the MMS is created.
            default: True

    datacolumn -- Which data column to use when partitioning the MS.
        default='all'; example: datacolumn='data'
        Options: 'data', 'model', 'corrected', 'all',
                'float_data', 'lag_data', 'float_data,data', and
                'lag_data,data'.
            N.B.: 'all' = whichever of the above that are present.

---- Data selection parameters (see help par.selectdata for more detailed
    information)

    field -- Select field using field id(s) or field name(s).
             [run listobs to obtain the list iof d's or names]
        default: ''=all fields If field string is a non-negative
           integer, it is assumed to be a field index
           otherwise, it is assumed to be a field name
           field='0~2'; field ids 0,1,2
           field='0,4,5~7'; field ids 0,4,5,6,7
           field='3C286,3C295'; fields named 3C286 and 3C295
           field = '3,4C*'; field id 3, all names starting with 4C

    spw -- Select spectral window/channels
        default: ''=all spectral windows and channels
           spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
           spw='<2';  spectral windows less than 2 (i.e. 0,1)
           spw='0:5~61'; spw 0, channels 5 to 61
           spw='0,10,3:3~45'; spw 0,10 all channels, spw 3 - chans 3 to 45.
           spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
           spw = '*:3~64'  channels 3 through 64 for all sp id's
                   spw = ' :3~64' will NOT work.
           spw = '*:0;60~63'  channel 0 and channels 60 to 63 for all IFs 
                  ';' needed to separate different channel ranges in one spw
           spw='0:0~10;15~60'; spectral window 0 with channels 0-10,15-60
           spw='0:0~10,1:20~30,2:1;2;4'; spw 0, channels 0-10,
                    spw 1, channels 20-30, and spw 2, channels, 1, 2 and 4

    antenna -- Select data based on antenna/baseline
        default: '' (all)
            Non-negative integers are assumed to be antenna indices, and
            anything else is taken as an antenna name.

            Examples:
            antenna='5&6': baseline between antenna index 5 and index 6.
            antenna='VA05&VA06': baseline between VLA antenna 5 and 6.
            antenna='5&6;7&8': baselines 5-6 and 7-8
            antenna='5': all baselines with antenna 5
            antenna='5,6,10': all baselines including antennas 5, 6, or 10
            antenna='5,6,10&': all baselines with *only* antennas 5, 6, or
                                   10.  (cross-correlations only.  Use &&
                                   to include autocorrelations, and &&&
                                   to get only autocorrelations.)
            antenna='!ea03,ea12,ea17': all baselines except those that
                                       include EVLA antennas ea03, ea12, or
                                       ea17.

    timerange -- Select data based on time range:
        default = '' (all); examples,
           timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
           Note: if YYYY/MM/DD is missing date, timerange defaults to the
           first day in the dataset
           timerange='09:14:0~09:54:0' picks 40 min on first day
           timerange='25:00:00~27:30:00' picks 1 hr to 3 hr 30min
           on next day
           timerange='09:44:00' data within one integration of time
           timerange='>10:24:00' data after this time

    array -- (Sub)array number range
        default: ''=all

    uvrange -- Select data within uvrange (default units meters)
        default: ''=all; example:
            uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
            uvrange='>4klambda';uvranges greater than 4 kilo-lambda
            uvrange='0~1000km'; uvrange in kilometers

    scan -- Scan number range
        default: ''=all

    observation -- Select by observation ID(s)
        default: ''=all


------ EXAMPLES ------

1) Create a Multi-MS of some spws, partitioned per spw. The MS contains 16 spws.
    partition('uid001.ms', outpuvis='source.mms', spw='1,3~10', separationaxis='spw')

2) Create a Multi-MS but select only the first channels of all spws. Do not back up the FLAG
column.
    partition('uid0001.ms', outputvis='fechans.mms', spw='*:1~10', flagbackup=False)

3) Create a Multi-MS using both separation axes.
    partition('uid0001.ms', outputvis='myuid.mms', createmms=True, separationaxis='auto')

4) Create a single-dish Multi-MS using the baseline axis only for the auto-correlations.
    partition('uid0001.ms', outputvis='myuid.mms', createmms=True, separationaxis='baseline', antenna='*&&&')



        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'partition'
        self.__globals__['taskname'] = 'partition'
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
            myparams['createmms'] = createmms = self.parameters['createmms']
            myparams['separationaxis'] = separationaxis = self.parameters['separationaxis']
            myparams['numsubms'] = numsubms = self.parameters['numsubms']
            myparams['flagbackup'] = flagbackup = self.parameters['flagbackup']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']
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
            myparams['disableparallel'] = disableparallel = self.parameters['disableparallel']
            myparams['ddistart'] = ddistart = self.parameters['ddistart']
            myparams['taql'] = taql = self.parameters['taql']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['outputvis'] = outputvis
        mytmp['createmms'] = createmms
        mytmp['separationaxis'] = separationaxis
        mytmp['numsubms'] = numsubms
        mytmp['flagbackup'] = flagbackup
        mytmp['datacolumn'] = datacolumn
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
        mytmp['disableparallel'] = disableparallel
        mytmp['ddistart'] = ddistart
        mytmp['taql'] = taql
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'partition.xml')

        casalog.origin('partition')
        try :
          #if not trec.has_key('partition') or not casac.casac.utils().verify(mytmp, trec['partition']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['partition'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('partition', 'partition.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'partition'
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
          result = partition(vis, outputvis, createmms, separationaxis, numsubms, flagbackup, datacolumn, field, spw, scan, antenna, correlation, timerange, intent, array, uvrange, observation, feed, disableparallel, ddistart, taql)

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
             tname = 'partition'
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
#        paramgui.runTask('partition', myf['_ip'])
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
        a['createmms']  = True
        a['datacolumn']  = 'all'
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

        a['createmms'] = {
                    0:odict([{'value':True}, {'separationaxis':'auto'}, {'numsubms':'auto'}, {'flagbackup':True}, {'disableparallel':False}, {'ddistart':-1}, {'taql':''}]), 
                    1:odict([{'value':False}, {'separationaxis':'auto'}, {'numsubms':'auto'}, {'flagbackup':True}, {'disableparallel':False}, {'ddistart':-1}, {'taql':''}])}

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
    def description(self, key='partition', subkey=None):
        desc={'partition': 'Task to produce Multi-MSs using parallelism',
               'vis': 'Name of input measurement set',
               'outputvis': 'Name of output measurement set',
               'createmms': 'Should this create a multi-MS output',
               'separationaxis': 'Axis to do parallelization across(scan, spw, baseline, auto)',
               'numsubms': 'The number of SubMSs to create (auto or any number)',
               'flagbackup': 'Create a backup of the FLAG column in the MMS.',
               'datacolumn': 'Which data column(s) to process.',
               'field': 'Select field using ID(s) or name(s).',
               'spw': 'Select spectral window/channels.',
               'scan': 'Select data by scan numbers.',
               'antenna': 'Select data based on antenna/baseline.',
               'correlation': 'Correlation: '' ==> all, correlation="XX,YY".',
               'timerange': 'Select data by time range.',
               'intent': 'Select data by scan intent.',
               'array': 'Select (sub)array(s) by array ID number.',
               'uvrange': 'Select data by baseline length.',
               'observation': 'Select by observation ID(s).',
               'feed': 'Multi-feed numbers: Not yet implemented.',
               'disableparallel': 'Create a multi-MS in parallel.',
               'ddistart': 'Do not change this parameter. For internal use only.',
               'taql': 'Table query for nested selections',

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
        a['createmms']  = True
        a['separationaxis']  = 'auto'
        a['numsubms']  = 'auto'
        a['flagbackup']  = True
        a['datacolumn']  = 'all'
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
        a['disableparallel']  = False
        a['ddistart']  = -1
        a['taql']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['createmms']  == True:
            a['separationaxis'] = 'auto'
            a['numsubms'] = 'auto'
            a['flagbackup'] = True
            a['disableparallel'] = False
            a['ddistart'] = -1
            a['taql'] = ''

        if self.parameters['createmms']  == False:
            a['separationaxis'] = 'auto'
            a['numsubms'] = 'auto'
            a['flagbackup'] = True
            a['disableparallel'] = False
            a['ddistart'] = -1
            a['taql'] = ''

        if a.has_key(paramname) :
              return a[paramname]
partition_cli = partition_cli_()
