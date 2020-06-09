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
from task_listvis import listvis
class listvis_cli_:
    __name__ = "listvis"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (listvis_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'options':None, 'datacolumn':None, 'field':None, 'spw':None, 'selectdata':None, 'antenna':None, 'timerange':None, 'correlation':None, 'scan':None, 'feed':None, 'array':None, 'observation':None, 'uvrange':None, 'average':None, 'showflags':None, 'pagerows':None, 'listfile':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, options=None, datacolumn=None, field=None, spw=None, selectdata=None, antenna=None, timerange=None, correlation=None, scan=None, feed=None, array=None, observation=None, uvrange=None, average=None, showflags=None, pagerows=None, listfile=None, ):

        """List measurement set visibilities.

        Detailed Description:


This task lists measurement set visibility data under a number of
input selection conditions.  The measurement set data columns that
can be listed are: the raw data, float_data, corrected data, model data,
and residual (corrected - model) data.

The output table format is dynamic.  Field, Spectral Window, and
Channel columns are not displayed if the column contents are uniform.
For example, if "spw = '1'" is specified, the spw column will not be
displayed.  When a column is not displayed, a message is sent to the
logger and terminal indicating that the column values are uniform and
listing the uniform value.

Table column descriptions:

COLUMN NAME       DESCRIPTION
-----------       -----------
Date/Time         Time stamp of data sample (YYMMDD/HH:MM:SS UT)
Intrf             Interferometer baseline (antenna names)
UVDist            uv-distance (units of wavelength)
Fld               Field ID (if more than 1)
SpW               Spectral Window ID (if more than 1)
Chn               Channel number (if more than 1)
(Correlated       Correlated polarizations (eg: RR, LL, XY)
  polarization)     Sub-columns are: Amp, Phs, Wt, F
Amp               Visibility amplitude
Phs               Visibility phase (deg)
Wt                Weight of visibility measurement
F                 Flag: 'F' = flagged datum; ' ' = unflagged
UVW               UVW coordinates (meters)


Input Parameters:
vis         Name of input visibility file
            default: none; example: vis='ngc5921.ms'

options     List options: default = 'ap'
            Not yet implemented for suboptions

datacolumn  Visibility file data column:
            default = 'data':  options are
            data, float_data, corrected, model, residual (corrected-model)

field       Select data based on field id(s) or name(s)
            default: ''==&gt;all; example: field='1'
            field='0~2' field ids inclusive from 0 to 2
            field='3C*' all field names starting with 3C

spw         Select spectral window, channel to list
            default: '0:0' --&gt; spw=0, chan=0
            spw='2:34' spectral window 2, channel 34

selectdata  Toggle the following 7 selection parameters.
            default: False; example: selectdata=True
            If false, the following parameters are reset
            to default values.

      antenna     Select calibration data based on antenna
                  default: ''--&gt;all; examples:
                  antenna = '5,6'; antenna index 5 and 6 solutions
                  antenna = '05,06'; antenna names '05' and '06 solutions

      timerange   Select time range to list
                  default: ''--&gt;all; examples:
                  timerange='10:37:50.1'; list data for this sampling interval
                  timerange='&lt;10:37:25'; list data before 10:37:25

      correlation Select polarization correlations to list
                  default: ''--&gt;all; examples:
                  correlation='RR LL'; list RR and LL correlations
                  correlation='XX XY'; list XX and XY correlations

      scan        Select scans to list
                  default: ''--&gt;all; examples:
                  scan='2'; list scan 2
                  scan='&gt;2'; list scan numbers greater than 2

      feed        (not yet implemented)

      array       (not yet implemented)

      observation Select by observation ID.

      uvrange     Select baseline lengths to list.
                  default: ''--&gt; all; examples:
                  uvrange='&lt;5klambda'; less than 5 kilo-wavelengths
                  Caution: Input units default to meters.
                  Listed units are always wavelengths.

average     (not yet implemented)

showflags   (not yet implemented)

pagerows    rows per page of listing
            default: 50; 0 --&gt; do not paginate

listfile    write output to disk; will not overwrite
            default: '' --&gt; write to screen
            listfile = 'solutions.txt'

async       Run asynchronously
            default = False; do not run asychronously

  
        Arguments :
                vis: Name of input visibility file
                   Default Value: 

                options: List options: ap only 
                   Default Value: ap

                datacolumn: Column to list: data, float_data, corrected, model, residual
                   Default Value: data
                   Allowed Values:
                                data
                                float_data
                                corrected
                                model
                                residual

                field: Field names or index to be listed
                   Default Value: 

                spw: Spectral window channels 
                   Default Value: *

                selectdata: Other data selection parameters
                   Default Value: False

                antenna: Antenna/baselines
                   Default Value: 

                timerange: Time range
                   Default Value: 

                correlation: Correlations
                   Default Value: 

                scan: Scan numbers
                   Default Value: 

                feed: Multi-feed numbers (Not yet implemented)
                   Default Value: 

                array: Array numbers (Not yet implemented)
                   Default Value: 

                observation: Select by observation ID(s)
                   Default Value: 

                uvrange: uv range
                   Default Value: 

                average: Averaging mode 
                   Default Value: 
                   Allowed Values:
                                
                                none
                                time
                                chan
                                both

                showflags: Show flagged data (Not yet implemented)
                   Default Value: False

                pagerows: Rows per page
                   Default Value: 50

                listfile: Output file
                   Default Value: 

        Returns: void

        Example :


This task lists measurement set visibility data under a number of
input selection conditions.  The measurement set data columns that
can be listed are: the raw data, float_data, corrected data, model data,
and residual (corrected - model) data.

The output table format is dynamic.  Field, Spectral Window, and
Channel columns are not displayed if the column contents are uniform.
For example, if "spw = '1'" is specified, the spw column will not be
displayed.  When a column is not displayed, a message is sent to the
logger and terminal indicating that the column values are uniform and
listing the uniform value.

Table column descriptions:

COLUMN NAME       DESCRIPTION
-----------       -----------
Date/Time         Time stamp of data sample (YYMMDD/HH:MM:SS UT)
Intrf             Interferometer baseline (antenna names)
UVDist            uv-distance (units of wavelength)
Fld               Field ID (if more than 1)
SpW               Spectral Window ID (if more than 1)
Chn               Channel number (if more than 1)
(Correlated       Correlated polarizations (eg: RR, LL, XY)
  polarization)     Sub-columns are: Amp, Phs, Wt, F
Amp               Visibility amplitude
Phs               Visibility phase (deg)
Wt                Weight of visibility measurement
F                 Flag: 'F' = flagged datum; ' ' = unflagged
UVW               UVW coordinates (meters)


Input Parameters:
vis         Name of input visibility file
            default: none; example: vis='ngc5921.ms'

options     List options: default = 'ap'
            Not yet implemented for suboptions

datacolumn  Visibility file data column:
            default = 'data':  options are
            data, float_data, corrected, model, residual (corrected-model)

field       Select data based on field id(s) or name(s)
            default: ''==>all; example: field='1'
            field='0~2' field ids inclusive from 0 to 2
            field='3C*' all field names starting with 3C

spw         Select spectral window, channel to list
            default: '0:0' --> spw=0, chan=0
            spw='2:34' spectral window 2, channel 34

selectdata  Toggle the following 7 selection parameters.
            default: False; example: selectdata=True
            If false, the following parameters are reset
            to default values.

      antenna     Select calibration data based on antenna
                  default: ''-->all; examples:
                  antenna = '5,6'; antenna index 5 and 6 solutions
                  antenna = '05,06'; antenna names '05' and '06 solutions

      timerange   Select time range to list
                  default: ''-->all; examples:
                  timerange='10:37:50.1'; list data for this sampling interval
                  timerange='<10:37:25'; list data before 10:37:25

      correlation Select polarization correlations to list
                  default: ''-->all; examples:
                  correlation='RR LL'; list RR and LL correlations
                  correlation='XX XY'; list XX and XY correlations

      scan        Select scans to list
                  default: ''-->all; examples:
                  scan='2'; list scan 2
                  scan='>2'; list scan numbers greater than 2

      feed        (not yet implemented)

      array       (not yet implemented)

      observation Select by observation ID(s).
                  default: ''-->all;
                  example: observation='0' (select obsID 0)

      uvrange     Select baseline lengths to list.
                  default: ''--> all; examples:
                  uvrange='<5klambda'; less than 5 kilo-wavelengths
                  Caution: Input units default to meters.
                  Listed units are always wavelengths.

average     (not yet implemented)

showflags   (not yet implemented)

pagerows    rows per page of listing
            default: 50; 0 --> do not paginate

listfile    write output to disk; will not overwrite
            default: '' --> write to screen
            listfile = 'solutions.txt'

async       Run asynchronously
            default = False; do not run asychronously

   
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'listvis'
        self.__globals__['taskname'] = 'listvis'
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
            myparams['options'] = options = self.parameters['options']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['selectdata'] = selectdata = self.parameters['selectdata']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['correlation'] = correlation = self.parameters['correlation']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['feed'] = feed = self.parameters['feed']
            myparams['array'] = array = self.parameters['array']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['average'] = average = self.parameters['average']
            myparams['showflags'] = showflags = self.parameters['showflags']
            myparams['pagerows'] = pagerows = self.parameters['pagerows']
            myparams['listfile'] = listfile = self.parameters['listfile']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['options'] = options
        mytmp['datacolumn'] = datacolumn
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['selectdata'] = selectdata
        mytmp['antenna'] = antenna
        mytmp['timerange'] = timerange
        mytmp['correlation'] = correlation
        mytmp['scan'] = scan
        mytmp['feed'] = feed
        mytmp['array'] = array
        mytmp['observation'] = observation
        mytmp['uvrange'] = uvrange
        mytmp['average'] = average
        mytmp['showflags'] = showflags
        mytmp['pagerows'] = pagerows
        mytmp['listfile'] = listfile
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'listvis.xml')

        casalog.origin('listvis')
        try :
          #if not trec.has_key('listvis') or not casac.casac.utils().verify(mytmp, trec['listvis']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['listvis'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('listvis', 'listvis.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'listvis'
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
          result = listvis(vis, options, datacolumn, field, spw, selectdata, antenna, timerange, correlation, scan, feed, array, observation, uvrange, average, showflags, pagerows, listfile)

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
             tname = 'listvis'
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
#        paramgui.runTask('listvis', myf['_ip'])
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
        a['options']  = 'ap'
        a['datacolumn']  = 'data'
        a['field']  = ''
        a['spw']  = '*'
        a['selectdata']  = False
        a['observation']  = ''
        a['average']  = ''
        a['showflags']  = False
        a['pagerows']  = 50
        a['listfile']  = ''

        a['selectdata'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'feed':''}, {'array':''}, {'observation':''}, {'uvrange':''}])}

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
    def description(self, key='listvis', subkey=None):
        desc={'listvis': 'List measurement set visibilities.',
               'vis': 'Name of input visibility file',
               'options': 'List options: ap only ',
               'datacolumn': 'Column to list: data, float_data, corrected, model, residual',
               'field': 'Field names or index to be listed',
               'spw': 'Spectral window channels ',
               'selectdata': 'Other data selection parameters',
               'antenna': 'Antenna/baselines',
               'timerange': 'Time range',
               'correlation': 'Correlations',
               'scan': 'Scan numbers',
               'feed': 'Multi-feed numbers (Not yet implemented)',
               'array': 'Array numbers (Not yet implemented)',
               'observation': 'Select by observation ID(s)',
               'uvrange': 'uv range',
               'average': 'Averaging mode ',
               'showflags': 'Show flagged data (Not yet implemented)',
               'pagerows': 'Rows per page',
               'listfile': 'Output file',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['options']  = 'ap'
        a['datacolumn']  = 'data'
        a['field']  = ''
        a['spw']  = '*'
        a['selectdata']  = False
        a['antenna']  = ''
        a['timerange']  = ''
        a['correlation']  = ''
        a['scan']  = ''
        a['feed']  = ''
        a['array']  = ''
        a['observation']  = ''
        a['uvrange']  = ''
        a['average']  = ''
        a['showflags']  = False
        a['pagerows']  = 50
        a['listfile']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['selectdata']  == True:
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['feed'] = ''
            a['array'] = ''
            a['observation'] = ''
            a['uvrange'] = ''

        if a.has_key(paramname) :
              return a[paramname]
listvis_cli = listvis_cli_()
