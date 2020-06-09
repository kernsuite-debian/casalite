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
from task_oldstatwt import oldstatwt
class oldstatwt_cli_:
    __name__ = "oldstatwt"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (oldstatwt_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'dorms':None, 'byantenna':None, 'sepacs':None, 'fitspw':None, 'fitcorr':None, 'combine':None, 'timebin':None, 'minsamp':None, 'field':None, 'spw':None, 'antenna':None, 'timerange':None, 'scan':None, 'intent':None, 'array':None, 'correlation':None, 'observation':None, 'datacolumn':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, dorms=None, byantenna=None, sepacs=None, fitspw=None, fitcorr=None, combine=None, timebin=None, minsamp=None, field=None, spw=None, antenna=None, timerange=None, scan=None, intent=None, array=None, correlation=None, observation=None, datacolumn=None, ):

        """ Reweight visibilities according to their scatter (Experimental)
        Arguments :
                vis: Name of measurement set
                   Default Value: 

                dorms: Use rms instead of stddev?
                   Default Value: False

                byantenna: Estimate the noise per antenna -not implemented (vs. per baseline)
                   Default Value: False

                sepacs: If solving by antenna, treat autocorrs separately (not implemented)
                   Default Value: True

                fitspw: The signal-free spectral window:channels to estimate the scatter from
                   Default Value: 

                fitcorr: The signal-free correlation(s) to estimate the scatter from (not implemented)
                   Default Value: 

                combine: Let estimates span changes in spw, corr, scan and/or state
                   Default Value: 

                timebin: Bin length for estimates (not implemented)
                   Default Value: 0s

                minsamp: Minimum number of unflagged visibilities for estimating the scatter
                   Default Value: 2

                field: Select field using ID(s) or name(s)
                   Default Value: 

                spw: Select spectral window/channels
                   Default Value: 

                antenna: Select data based on antenna/baseline
                   Default Value: 

                timerange: Select data by time range
                   Default Value: 

                scan: Select data by scan numbers
                   Default Value: 

                intent: Select data by scan intents
                   Default Value: 

                array: Select (sub)array(s) by array ID number
                   Default Value: 

                correlation: Select correlations to reweight (DEPRECATED in CASA v4.5)
                   Default Value: 

                observation: Select by observation ID(s)
                   Default Value: 

                datacolumn: Which data column to calculate the scatter from
                   Default Value: corrected
                   Allowed Values:
                                data
                                corrected
                                float_data
                                model


        Example :


    The WEIGHT and SIGMA columns of measurement sets are often set to arbitrary
    values (e.g. 1), or theoretically estimated from poorly known antenna and
    receiver properties.  Many tasks (e.g. clean) are insensitive to an overall
    scale error in WEIGHT, but are affected by errors in the relative weights
    between visibilities.  Other tasks, such as uvmodelfit, or anything which
    depends on theoretical estimates of the noise, require (reasonably) correct
    weights and sigmas.  oldstatwt empirically measures the visibility scatter
    (typically as a function of time, antenna, and/or baseline) and uses that
    to set WEIGHT and SIGMA. It is important that all necessary calibrations
    are applied to the data prior to running this task for correct determination of
    weights and sigmas.

    Note: Some of the parameters (byantenna, sepacs, fitcorr, and timebin)
          are not fully implemented for CASA 3.4.


        Keyword arguments:
        vis -- Name of the measurement set.
                default: none; example: vis='ngc5921.ms'

        dorms -- Estimate the scatter using rms instead of the standard
                 deviation?

                 Ideally the visibilities used to estimate the scatter, as
                 selected by fitspw and fitcorr, should be pure noise.  If you
                 know for certain that they are, then setting dorms to True
                 will give the best result.  Otherwise, use False (standard
                 sample standard deviation).  More robust scatter estimates
                 like the interquartile range or median absolute deviation from
                 the median are not offered because they require sorting by
                 value, which is not possible for complex numbers.
               default: False

        byantenna -- Assume that the noise is factorable by antenna (feed).
                     If false, treat it separately for each baseline
                     (recommended if there is strong signal).
               default: False (*** byantenna=True is not yet implemented)

        sepacs -- If solving by antenna, treat autocorrelations separately.
                  (Acknowledge that what autocorrelations "see" is very
                   different from what crosscorrelations see.)
               default: True (*** not yet implemented)


        --- Data Selection (see help par.selectdata for more detailed
            information)

        fitspw -- The (ideally) signal-free spectral window:channels to
                  estimate the scatter from.
               default: '' (All)

        fitcorr -- The (ideally) signal-free correlations to
                   estimate the scatter from.
               default: '' (All)
               *** not yet implemented

        combine -- Let samples span multiple spws, corrs, scans, and/or states.
                   combine = 'spw': Recommended when a line spans an entire spw
                                    - set fitspw to the neighboring spws and
                                    apply their weight to the line spw(s).
                                    However, the effect of the line signal per
                                    visibility may be relatively harmless
                                    compared to the noise difference between
                                    spws.
                   combine = 'scan': Can be useful when the scan number
                                     goes up with each integration,
                                     as in many WSRT MSes.
                   combine = ['scan', 'spw']: disregard scan and spw
                                              numbers when gathering samples.
                   combine = 'spw,scan': Same as above.
              default: '' (None)

        timebin -- Sample interval.
                   default: '0s' or '-1s' (1 integration at a time)
                   example: timebin='30s'
                            '10' means '10s'
                   *** not yet implemented

        minsamp -- Minimum number of unflagged visibilities for estimating the
                   scatter.  Selected visibilities for which the weight cannot
                   be estimated will be flagged.  Note that minsamp is
                   effectively at least 2 if dorms is False, and 1 if it is
                   True.

        field -- Select field using field id(s) or field name(s).
                  [run listobs to obtain the list id's or names]
               default: ''=all fields If field string is a non-negative
               integer, it is assumed to be a field index
               otherwise, it is assumed to be a field name
               field='0~2'; field ids 0,1,2
               field='0,4,5~7'; field ids 0,4,5,6,7
               field='3C286,3C295'; fields named 3C286 and 3C295
               field = '3,4C*'; field id 3, all names starting with 4C

        spw -- Select spectral window/channels for changing WEIGHT and SIGMA.
               default: ''=all spectral windows and channels
               spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
               spw='<2';  spectral windows less than 2 (i.e. 0,1)
               spw='0:5~61'; spw 0, channels 5 to 61
               spw='0,10,3:3~45'; spw 0,10 all channels, spw 3 - chans 3 to 45.
               spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
               spw = '*:3~64'  channels 3 through 64 for all sp id's
                       spw = ' :3~64' will NOT work.
               oldstatwt does not support multiple channel ranges per spectral
               window (';') because it is not clear whether to keep the ranges
               in the original spectral window or make a new spectral window
               for each additional range.

        antenna -- Select antennas/baselines for changing WEIGHT and SIGMA.
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
        scan -- Scan number range
            default: ''=all
        intent -- Select by scan intent (state).  Case sensitive.
            default: '' = all
            Examples:
            intent = 'CALIBRATE_ATMOSPHERE_REFERENCE'
            intent = 'calibrate_atmosphere_reference'.upper() # same as above
            # Select states that include one or both of CALIBRATE_WVR.REFERENCE
            # or OBSERVE_TARGET_ON_SOURCE.
            intent = 'CALIBRATE_WVR.REFERENCE, OBSERVE_TARGET_ON_SOURCE'
        array -- (Sub)array number range
            default: ''=all
        correlation -- Select correlations, e.g. 'rr, ll' or ['XY', 'YX'].
                       default '' (all).
                       NB: In CASA v4.5, non-trivial correlation selection has
                       been disabled since it was not working correctly, and
                       it is likely undesirable to set the weights in a
                       correlation-dependent way.

        observation -- Select by observation ID(s).
                       default: '' = all
       datacolumn -- Which data column to calculate the scatter from
                  default='corrected'; example: datacolumn='data'
                  Options: 'data', 'corrected', 'model', 'float_data'
                  note: 'corrected' will fall back to DATA if CORRECTED_DATA
                        is absent.


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'oldstatwt'
        self.__globals__['taskname'] = 'oldstatwt'
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
            myparams['dorms'] = dorms = self.parameters['dorms']
            myparams['byantenna'] = byantenna = self.parameters['byantenna']
            myparams['sepacs'] = sepacs = self.parameters['sepacs']
            myparams['fitspw'] = fitspw = self.parameters['fitspw']
            myparams['fitcorr'] = fitcorr = self.parameters['fitcorr']
            myparams['combine'] = combine = self.parameters['combine']
            myparams['timebin'] = timebin = self.parameters['timebin']
            myparams['minsamp'] = minsamp = self.parameters['minsamp']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['array'] = array = self.parameters['array']
            myparams['correlation'] = correlation = self.parameters['correlation']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['dorms'] = dorms
        mytmp['byantenna'] = byantenna
        mytmp['sepacs'] = sepacs
        mytmp['fitspw'] = fitspw
        mytmp['fitcorr'] = fitcorr
        mytmp['combine'] = combine
        mytmp['timebin'] = timebin
        mytmp['minsamp'] = minsamp
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['antenna'] = antenna
        mytmp['timerange'] = timerange
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['array'] = array
        mytmp['correlation'] = correlation
        mytmp['observation'] = observation
        mytmp['datacolumn'] = datacolumn
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'oldstatwt.xml')

        casalog.origin('oldstatwt')
        try :
          #if not trec.has_key('oldstatwt') or not casac.casac.utils().verify(mytmp, trec['oldstatwt']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['oldstatwt'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('oldstatwt', 'oldstatwt.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'oldstatwt'
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
          result = oldstatwt(vis, dorms, byantenna, sepacs, fitspw, fitcorr, combine, timebin, minsamp, field, spw, antenna, timerange, scan, intent, array, correlation, observation, datacolumn)

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
             tname = 'oldstatwt'
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
#        paramgui.runTask('oldstatwt', myf['_ip'])
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
        a['dorms']  = False
        a['byantenna']  = False
        a['fitspw']  = ''
        a['fitcorr']  = ''
        a['combine']  = ''
        a['timebin']  = '0s'
        a['minsamp']  = 2
        a['field']  = ''
        a['spw']  = ''
        a['antenna']  = ''
        a['timerange']  = ''
        a['scan']  = ''
        a['intent']  = ''
        a['array']  = ''
        a['correlation']  = ''
        a['observation']  = ''
        a['datacolumn']  = 'corrected'

        a['byantenna'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'sepacs':True}])}

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
    def description(self, key='oldstatwt', subkey=None):
        desc={'oldstatwt': ' Reweight visibilities according to their scatter (Experimental)',
               'vis': 'Name of measurement set',
               'dorms': 'Use rms instead of stddev?',
               'byantenna': 'Estimate the noise per antenna -not implemented (vs. per baseline)',
               'sepacs': 'If solving by antenna, treat autocorrs separately (not implemented)',
               'fitspw': 'The signal-free spectral window:channels to estimate the scatter from',
               'fitcorr': 'The signal-free correlation(s) to estimate the scatter from (not implemented)',
               'combine': 'Let estimates span changes in spw, corr, scan and/or state',
               'timebin': 'Bin length for estimates (not implemented)',
               'minsamp': 'Minimum number of unflagged visibilities for estimating the scatter',
               'field': 'Select field using ID(s) or name(s)',
               'spw': 'Select spectral window/channels',
               'antenna': 'Select data based on antenna/baseline',
               'timerange': 'Select data by time range',
               'scan': 'Select data by scan numbers',
               'intent': 'Select data by scan intents',
               'array': 'Select (sub)array(s) by array ID number',
               'correlation': 'Select correlations to reweight (DEPRECATED in CASA v4.5)',
               'observation': 'Select by observation ID(s)',
               'datacolumn': 'Which data column to calculate the scatter from',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['dorms']  = False
        a['byantenna']  = False
        a['sepacs']  = True
        a['fitspw']  = ''
        a['fitcorr']  = ''
        a['combine']  = ''
        a['timebin']  = '0s'
        a['minsamp']  = 2
        a['field']  = ''
        a['spw']  = ''
        a['antenna']  = ''
        a['timerange']  = ''
        a['scan']  = ''
        a['intent']  = ''
        a['array']  = ''
        a['correlation']  = ''
        a['observation']  = ''
        a['datacolumn']  = 'corrected'

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['byantenna']  == True:
            a['sepacs'] = True

        if a.has_key(paramname) :
              return a[paramname]
oldstatwt_cli = oldstatwt_cli_()
