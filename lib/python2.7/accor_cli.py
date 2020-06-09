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
from task_accor import accor
class accor_cli_:
    __name__ = "accor"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (accor_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'caltable':None, 'field':None, 'spw':None, 'intent':None, 'selectdata':None, 'timerange':None, 'antenna':None, 'scan':None, 'observation':None, 'msselect':None, 'solint':None, 'combine':None, 'append':None, 'docallib':None, 'callib':None, 'gaintable':None, 'gainfield':None, 'interp':None, 'spwmap':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, caltable=None, field=None, spw=None, intent=None, selectdata=None, timerange=None, antenna=None, scan=None, observation=None, msselect=None, solint=None, combine=None, append=None, docallib=None, callib=None, gaintable=None, gainfield=None, interp=None, spwmap=None, ):

        """Normalize visibilities based on auto-correlations

        Detailed Description:

Determines the amplitude corrections neede due to errors in sampler
thresholds using measurements of auto-correlation spectra. This
correction is typically requiered for data correlated with the DiFX
correlator (such as VLBA data).  Other correlators (such as the SFXC
correlator used to correlate EVN data at JIVE) already apply this
correction at the correlator.  In this case, running this task is not
necessary.

        Arguments :
                vis: Name of input visibility file
                     default: none
                        
                        example: vis='ngc5921.ms'

                   Default Value: 

                caltable: Name of output gain calibration table
                     default: none
                        
                        example: caltable='ngc5921.gcal'

                   Default Value: 

                field: Select field using field id(s) or field name(s)
                     default: '' --> all fields
                     
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

                     Note: do not forget to include the flux density
                     calibrator if you have one!

                   Default Value: 

                spw: Select spectral window/channels

                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all
                        channels)
                        spw='<2';  spectral windows less than 2
                        (i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61,
                        INCLUSIVE
                        spw='*:5~61'; all spw with channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
                        3, channels 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
                        through 6 in each.
                        spw='0:0~10;15~60'; spectral window 0 with
                        channels 0-10,15-60. (NOTE ';' to separate
                        channel selections)
                        spw='0:0~10^2,1:20~30^5'; spw 0, channels
                        0,2,4,6,8,10, spw 1, channels 20,25,30 
                        type 'help par.selection' for more examples.

                   Default Value: 

                intent: Select observing intent
                     default: '' (no selection by intent)

                        Example: intent='*BANDPASS*'  (selects data
                        labelled with BANDPASS intent)

                   Default Value: 

                selectdata: Other data selection parameters
                     default: True (Must set selectdata=True to select
                     other selection parameters.)

                   Default Value: True

                timerange: Select data based on time range
                     Subparameter of selectdata=True
                     default = '' (all)

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

                antenna: Select data based on antenna/baseline
                     Subparameter of selectdata=True
                     default: '' (all)

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

                     Note: just for antenna selection, an integer (or
                     integer list) is converted to a string and
                     matched against the antenna 'name' first. Only if
                     that fails, the integer is matched with the
                     antenna ID. The latter is the case for most
                     observatories, where the antenna name is not
                     strictly an integer.
 
                   Default Value: 

                scan: Scan number range
                     Subparameter of selectdata=True
                     default: '' = all

                     Check 'go listobs' to insure the scan numbers are
                     in order.

                   Default Value: 

                observation: Select by observation ID(s)
                     Subparameter of selectdata=True
                     default: '' = all

                         Example: observation='0~2,4'

                   Default Value: 

                msselect: Optional complex data selection (ignore for now)

                   Default Value: 

                solint: Solution interval (units optional)
                     default: 'inf' (~infinite, up to boundaries
                     controlled by combine)
                     Options: 'inf' (~infinite), 'int' (per
                     integration), any float or integer value with or
                     without units

                        Examples: solint='1min'; solint='60s';
                        solint=60 --> 1 minute
                        solint='0s'; solint=0; solint='int' --> per
                        integration
                        solint-'-1s'; solint='inf' --> ~infinite, up
                        to boundaries -interacts with combine

                   Default Value: inf

                combine: Data axes which to combine for solve
                     default: '' (solutions will break at obs, scan,
                     field, and spw)
                     Options: '','obs','scan','spw',field', or any
                     comma-separated combination in a single string

                     For gaintype='K', if combine includes 'spw',
                     multi-band delays will be determined; otherwise,
                     (per-spw) single-band delays will be determined.

                        Example: combine='scan,spw' (extend solutions
                        over scan boundaries)

                   Default Value: 

                append: Append solutions to the (existing) table
                     default: False (overwrite existing table or make
                     new table)

                     Appended solutions must be derived from the same
                     MS as the existing caltable, and solution spws
                     must have the same meta-info (according to spw
                     selection and solint) or be non-overlapping.

                   Default Value: False

                docallib: Control means of specifying the caltables
                     default: False --> Use gaintable, gainfield,
                     interp, spwmap, calwt. 

                     If True, specify a file containing cal library in
                     callib

                   Default Value: False

                callib: Cal Library filename
                     Subparameter of callib=True

                     If docallib=True, specify a file containing cal
                     library directives

                   Default Value: 

                gaintable: Gain calibration table(s) to apply on the fly
                     Subparameter of callib=False
                     default: '' (none)

                        Examples: gaintable='ngc5921.gcal'
                        gaintable=['ngc5921.ampcal','ngc5921.phcal']

                   Default Value: 

                gainfield: Select a subset of calibrators from gaintable(s)
                     Subparameter of callib=False
                     default:'' --> all sources in table
                     
                     gaintable='nearest' --> nearest (on sky)
                     available field in table. Otherwise, same syntax
                     as field

                        Examples: 
                        gainfield='0~2,5' means use fields 0,1,2,5
                        from gaintable
                        gainfield=['0~3','4~6'] means use field 0
                        through 3 from first gain file, field 4
                        through 6 for second.

                   Default Value: 

                interp: Interpolation parmameters (in time[,freq]) for each gaintable, as a list of strings.
                     Default: '' --> 'linear,linear' for all gaintable(s)
                     Options: Time: 'nearest', 'linear'
                              Freq: 'nearest', 'linear', 'cubic',
                              'spline'
                   Specify a list of strings, aligned with the list of caltable specified
                   in gaintable, that contain the required interpolation parameters
                   for each caltable.
                   * When frequency interpolation is relevant (B, Df,
                     Xf), separate time-dependent and freq-dependent
                     interp types with a comma (freq_after_ the
                     comma). 
                   * Specifications for frequency are ignored when the
                     calibration table has no channel-dependence. 
                   * Time-dependent interp options ending in 'PD'
                     enable a "phase delay" correction per spw for
                     non-channel-dependent calibration types.
                   * For multi-obsId datasets, 'perobs' can be
                     appended to the time-dependent interpolation
                     specification to enforce obsId boundaries when
                     interpolating in time. 
                   * Freq-dependent interp options can have 'flag' appended
                     to enforce channel-dependent flagging, and/or 'rel' 
                     appended to invoke relative frequency interpolation

                        Examples: 
                        interp='nearest' (in time, freq-dep will be
                        linear, if relevant)
                        interp='linear,cubic'  (linear in time, cubic
                        in freq)
                        interp='linearperobs,splineflag' (linear in
                        time per obsId, spline in freq with
                        channelized flagging)
                        interp='nearest,linearflagrel' (nearest in
                        time, linear in freq with with channelized 
                        flagging and relative-frequency interpolation)
                        interp=',spline'  (spline in freq; linear in
                        time by default)
                        interp=['nearest,spline','linear']  (for
                        multiple gaintables)

                   Default Value: 

                spwmap: Spectral windows combinations to form for gaintables(s)
                     Subparameter of callib=False
                     default: [] (apply solutions from each spw to
                     that spw only)

                        Examples:
                        spwmap=[0,0,1,1] means apply the caltable
                        solutions from spw = 0 to the spw 0,1 and spw
                        1 to spw 2,3.
                        spwmap=[[0,0,1,1],[0,1,0,1]]

                   Default Value: 


        Example :

For more information, see the task pages of accor in CASA Docs:

https://casa.nrao.edu/casadocs/

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'accor'
        self.__globals__['taskname'] = 'accor'
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
            myparams['caltable'] = caltable = self.parameters['caltable']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['selectdata'] = selectdata = self.parameters['selectdata']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['msselect'] = msselect = self.parameters['msselect']
            myparams['solint'] = solint = self.parameters['solint']
            myparams['combine'] = combine = self.parameters['combine']
            myparams['append'] = append = self.parameters['append']
            myparams['docallib'] = docallib = self.parameters['docallib']
            myparams['callib'] = callib = self.parameters['callib']
            myparams['gaintable'] = gaintable = self.parameters['gaintable']
            myparams['gainfield'] = gainfield = self.parameters['gainfield']
            myparams['interp'] = interp = self.parameters['interp']
            myparams['spwmap'] = spwmap = self.parameters['spwmap']

        if type(gaintable)==str: gaintable=[gaintable]
        if type(gainfield)==str: gainfield=[gainfield]
        if type(interp)==str: interp=[interp]
        if type(spwmap)==int: spwmap=[spwmap]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['caltable'] = caltable
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['intent'] = intent
        mytmp['selectdata'] = selectdata
        mytmp['timerange'] = timerange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['observation'] = observation
        mytmp['msselect'] = msselect
        mytmp['solint'] = solint
        mytmp['combine'] = combine
        mytmp['append'] = append
        mytmp['docallib'] = docallib
        mytmp['callib'] = callib
        mytmp['gaintable'] = gaintable
        mytmp['gainfield'] = gainfield
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'accor.xml')

        casalog.origin('accor')
        try :
          #if not trec.has_key('accor') or not casac.casac.utils().verify(mytmp, trec['accor']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['accor'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('accor', 'accor.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'accor'
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
          result = accor(vis, caltable, field, spw, intent, selectdata, timerange, antenna, scan, observation, msselect, solint, combine, append, docallib, callib, gaintable, gainfield, interp, spwmap)

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
             tname = 'accor'
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
#        paramgui.runTask('accor', myf['_ip'])
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
        a['caltable']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['intent']  = ''
        a['selectdata']  = True
        a['solint']  = 'inf'
        a['combine']  = ''
        a['append']  = False
        a['docallib']  = False

        a['selectdata'] = {
                    0:odict([{'value':True}, {'timerange':''}, {'antenna':''}, {'scan':''}, {'observation':''}, {'msselect':''}]), 
                    1:{'value':False}}
        a['docallib'] = {
                    0:odict([{'value':False}, {'gaintable':[]}, {'gainfield':[]}, {'interp':[]}, {'spwmap':[]}]), 
                    1:odict([{'value':True}, {'callib':''}])}

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
    def description(self, key='accor', subkey=None):
        desc={'accor': 'Normalize visibilities based on auto-correlations',
               'vis': 'Name of input visibility file',
               'caltable': 'Name of output gain calibration table',
               'field': 'Select field using field id(s) or field name(s)',
               'spw': 'Select spectral window/channels',
               'intent': 'Select observing intent',
               'selectdata': 'Other data selection parameters',
               'timerange': 'Select data based on time range',
               'antenna': 'Select data based on antenna/baseline',
               'scan': 'Scan number range',
               'observation': 'Select by observation ID(s)',
               'msselect': 'Optional complex data selection (ignore for now)',
               'solint': 'Solution interval: egs. \'inf\', \'60s\' (see help)',
               'combine': 'Data axes which to combine for solve (obs, scan, spw, and/or field)',
               'append': 'Append solutions to the (existing) table',
               'docallib': 'Use callib or traditional cal apply parameters',
               'callib': 'Cal Library filename',
               'gaintable': 'Gain calibration table(s) to apply on the fly',
               'gainfield': 'Select a subset of calibrators from gaintable(s)',
               'interp': 'Interpolation parameters for each gaintable, as a list',
               'spwmap': 'Spectral windows combinations to form for gaintables(s)',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['caltable']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['intent']  = ''
        a['selectdata']  = True
        a['timerange']  = ''
        a['antenna']  = ''
        a['scan']  = ''
        a['observation']  = ''
        a['msselect']  = ''
        a['solint']  = 'inf'
        a['combine']  = ''
        a['append']  = False
        a['docallib']  = False
        a['callib']  = ''
        a['gaintable']  = ['']
        a['gainfield']  = ['']
        a['interp']  = ['']
        a['spwmap']  = []

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['selectdata']  == True:
            a['timerange'] = ''
            a['antenna'] = ''
            a['scan'] = ''
            a['observation'] = ''
            a['msselect'] = ''

        if self.parameters['docallib']  == False:
            a['gaintable'] = []
            a['gainfield'] = []
            a['interp'] = []
            a['spwmap'] = []

        if self.parameters['docallib']  == True:
            a['callib'] = ''

        if a.has_key(paramname) :
              return a[paramname]
accor_cli = accor_cli_()
