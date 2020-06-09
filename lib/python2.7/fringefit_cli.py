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
from task_fringefit import fringefit
class fringefit_cli_:
    __name__ = "fringefit"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (fringefit_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'caltable':None, 'field':None, 'spw':None, 'intent':None, 'selectdata':None, 'timerange':None, 'antenna':None, 'scan':None, 'observation':None, 'msselect':None, 'solint':None, 'combine':None, 'refant':None, 'minsnr':None, 'zerorates':None, 'globalsolve':None, 'niter':None, 'delaywindow':None, 'ratewindow':None, 'append':None, 'docallib':None, 'callib':None, 'gaintable':None, 'gainfield':None, 'interp':None, 'spwmap':None, 'parang':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, caltable=None, field=None, spw=None, intent=None, selectdata=None, timerange=None, antenna=None, scan=None, observation=None, msselect=None, solint=None, combine=None, refant=None, minsnr=None, zerorates=None, globalsolve=None, niter=None, delaywindow=None, ratewindow=None, append=None, docallib=None, callib=None, gaintable=None, gainfield=None, interp=None, spwmap=None, parang=None, ):

        """Fringe fit delay and rates

        Detailed Description:

Phase offsets, groups delays and delay rates are calculated with
respect to a specified referance antenna by a two-dimensional FFT and
subsequent least-squares optimisation.

Previous calibrations should be applied on the fly.


        Arguments :
                vis: Name of input visibility file
                   Default Value: 

                caltable: Name of output gain calibration table
                   Default Value: 

                field: Select field using field id(s) or field name(s)
                   Default Value: 

                spw: Select spectral window/channels
                   Default Value: 

                intent: Select observing intent
                   Default Value: 

                selectdata: Other data selection parameters
                   Default Value: True

                timerange: Select data based on time range
                   Default Value: 

                antenna: Select data based on antenna/baseline
                   Default Value: 

                scan: Scan number range
                   Default Value: 

                observation: Select by observation ID(s)
                   Default Value: 

                msselect: Optional complex data selection (ignore for now)
                   Default Value: 

                solint: Solution interval: egs. \'inf\', \'60s\' (see help)
                   Default Value: inf

                combine: Data axes which to combine for solve (obs, scan, spw, and/or field)
                   Default Value: 

                refant: Reference antenna name(s)
                   Default Value: 

                minsnr: Reject solutions below this signal-to-noise ratio (at the FFT stage)
                   Default Value: 3.0

                zerorates: Zero delay-rates in solution table
                   Default Value: False

                globalsolve: Refine estimates of delay and rate with global least-squares solver
                   Default Value: True

                niter: Maximum number of iterations for least-squares solver
                   Default Value: 100

                delaywindow: Constrain FFT delay search to a window; a two-element list, units of nanoseconds
                   Default Value: 

                ratewindow: Constrain FFT rate search to a window; a two-element list, units of seconds per second
                   Default Value: 

                append: Append solutions to the (existing) table
                   Default Value: False

                docallib: Use callib or traditional cal apply parameters
                   Default Value: False

                callib: Cal Library filename
                   Default Value: 

                gaintable: Gain calibration table(s) to apply on the fly
                   Default Value: 

                gainfield: Select a subset of calibrators from gaintable(s)
                   Default Value: 

                interp: Temporal interpolation for each gaintable (''=linear)
                   Default Value: 

                spwmap: Spectral windows combinations to form for gaintables(s)
                   Default Value: 

                parang: Apply parallactic angle correction on the fly
                   Default Value: False


        Example :


      Previous calibrations (egs, bandpass, opacity, parallactic angle) can
      be applied on the fly.  At present with dual-polarized data, both
      polarizations must be unflagged for any solution to be obtained.

      Keyword arguments:
      vis -- Name of input visibility file
              default: none; example: vis='ngc5921.ms'
      caltable -- Name of output fringefit calibration table
              default: none; example: caltable='ngc5921.fringe'

      --- Data Selection (see help par.selectdata for more detailed information)

      field -- Select field using field id(s) or field name(s).
                 ['go listobs' to obtain the list id's or names]
              default: ''=all fields
              If field string is a non-negative integer, it is assumed a
                field index,  otherwise, it is assumed a field name
              field='0~2'; field ids 0,1,2
              field='0,4,5~7'; field ids 0,4,5,6,7
              field='3C286,3C295'; field named 3C286 and 3C295
              field = '3,4C*'; field id 3, all names starting with 4C
          DON'T FORGET TO INCLUDE THE FLUX DENSITY CALIBRATOR IF YOU HAVE ONE
      spw -- Select spectral window/channels 
               type 'help par.selection' for more examples.
             spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
             spw='<2';  spectral windows less than 2 (i.e. 0,1)
             spw='0:5~61'; spw 0, channels 5 to 61, INCLUSIVE
             spw='*:5~61'; all spw with channels 5 to 61
             spw='0,10,3:3~45'; spw 0,10 all channels, spw 3, channels 3 to 45.
             spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
             spw='0:0~10;15~60'; spectral window 0 with channels 0-10,15-60
                       NOTE ';' to separate channel selections
             spw='0:0~10^2,1:20~30^5'; spw 0, channels 0,2,4,6,8,10,
                   spw 1, channels 20,25,30
      intent -- Select observing intent
                default: ''  (no selection by intent)
                intent='*FRINGEFIT*'  (selects data labelled with
                                      FRINGEFIT intent)
      selectdata -- Other data selection parameters
              default: True 

              Must set selectdata=True to use the following selections:

      timerange  -- Select data based on time range:
              default = '' (all); examples,
              timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
              Note: if YYYY/MM/DD is missing date defaults to first day in data set
              timerange='09:14:0~09:54:0' picks 40 min on first day
              timerange= '25:00:00~27:30:00' picks 1 hr to 3 hr 30min on NEXT day
              timerange='09:44:00' pick data within one integration of time
              timerange='>10:24:00' data after this time
      uvrange -- Select data within uvrange (default units meters)
              default: '' (all); example:
              uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
              uvrange='>4klambda';uvranges greater than 4 kilo lambda
      antenna -- Select data based on antenna/baseline
              default: '' (all)
              If antenna string is a non-negative integer, it is assumed an
                antenna index, otherwise, it is assumed as an antenna name
              antenna='5&6'; baseline between antenna index 5 and index 6.
              antenna='VA05&VA06'; baseline between VLA antenna 5 and 6.
              antenna='5&6;7&8'; baselines with indices 5-6 and 7-8
              antenna='5'; all baselines with antenna index 5
              antenna='05'; all baselines with antenna number 05 (VLA old name)
              antenna='5,6,10'; all baselines with antennas 5,6,10 index numbers
      scan -- Scan number range.
              Check 'go listobs' to insure the scan numbers are in order.
      observation -- Observation ID(s).
                     default: '' = all
                     example: '0~2,4'
      msselect -- Optional complex data selection (ignore for now)

      solint --  Solution interval (units optional) 
              default: 'inf' (~infinite, up to boundaries controlled by combine); 
              Options: 'inf' (~infinite), 
                       'int' (per integration)
                       any float or integer value with or without units
              examples: solint='1min'; solint='60s'; solint=60 --> 1 minute
                        solint='0s'; solint=0; solint='int' --> per integration
                        solint-'-1s'; solint='inf' --> ~infinite, up to boundaries
                        interacts with combine
      combine -- Data axes to combine for solving
              default: '' --> solutions will break at obs, scan, field, and spw
                      boundaries
              Options: '','obs','scan','spw',field', or any comma-separated 
                       combination in a single string
              For gaintype='K', if combine includes 'spw', multi-band
               delays will be determined; otherwise, (per-spw)
               single-band delays will be determined.
              example: combine='scan,spw'  --> extend solutions over scan boundaries
                       (up to the solint), and combine spws for solving
      refant -- Reference antenna name(s); a prioritized list may be
                specified for solving and for applying solutions. For
                solving, the first reference antenna associated with
                unflagged data is used for the solution.
              default: '' => no refant applied
              example: refant='4' (antenna with index 4)
                       refant='VA04' (VLA antenna #4)
                       refant='EA02,EA23,EA13' (EVLA antenna EA02, use
                                EA23 and EA13 as alternates if/when EA02
                                drops out)
              Use taskname=listobs for antenna listing
      minsnr -- Reject solutions below this SNR
              default: 3.0 
      solnorm -- Normalize average solution amps to 1.0 after solution (G, T only)
              default: False (no normalization)
      append -- Append solutions to the (existing) table.  Appended solutions
                 must be derived from the same MS as the existing
                 caltable, and solution spws must have the same
                 meta-info (according to spw selection and solint)
                 or be non-overlapping.
              default: False; overwrite existing table or make new table
      zerorates -- Write a solution table with delay-rates zeroed, for
      the case of "manual phase calibration".
                default: False

      globalsolve -- Refine fringefit solutions with global least-squares solver.
                default: False


                delaywindow -- Constrain FFT delay search to a window
      ratewindow -- Constrain FFT rate search to a window

      --- Other calibrations to apply on the fly before determining
      fringe fit solution

      docallib -- Control means of specifying the caltables:
               default: False ==> Use gaintable,gainfield,interp,spwmap,calwt
                        If True, specify a file containing cal library in callib
      callib -- If docallib=True, specify a file containing cal
                  library directives

      gaintable -- Gain calibration table(s) to apply 
               default: '' (none);
               examples: gaintable='ngc5921.gcal'
                         gaintable=['ngc5921.ampcal','ngc5921.phcal']
      gainfield -- Select a subset of calibrators from gaintable(s) to apply
               default:'' ==> all sources in table;
               'nearest' ==> nearest (on sky) available field in table
               otherwise, same syntax as field
               example: gainfield='0~2,5' means use fields 0,1,2,5 from gaintable
                        gainfield=['0~3','4~6'] means use field 0 through 3
                          from first gain file, field 4 through 6 for second.
      interp -- Interpolation type (in time[,freq]) to use for each gaintable.
                When frequency interpolation is relevant (B, Df, Xf),
                separate time-dependent and freq-dependent interp
                types with a comma (freq _after_ the comma).                
                Specifications for frequency are ignored when the
                calibration table has no channel-dependence.
                Time-dependent interp options ending in 'PD' enable a
                "phase delay" correction per spw for non-channel-dependent
                calibration types.
                For multi-obsId datasets, 'perobs' can be appended to
                the time-dependent interpolation specification to
                enforce obsId boundaries when interpolating in time.
                default: '' --> 'linear,linear' for all gaintable(s)
                example: interp='nearest'   (in time, freq-dep will be
                                             linear, if relevant)
                         interp='linear,cubic'  (linear in time, cubic
                                                 in freq)
                         interp='linearperobs,spline' (linear in time
                                                       per obsId,
                                                       spline in freq)
                         interp=',spline'  (spline in freq; linear in
                                            time by default)
                         interp=['nearest,spline','linear']  (for multiple gaintables)
                Options: Time: 'nearest', 'linear'
                         Freq: 'nearest', 'linear', 'cubic', 'spline'
      spwmap -- Spectral windows combinations to form for gaintable(s)
                default: [] (apply solutions from each spw to that spw only)
                Example:  spwmap=[0,0,1,1] means apply the caltable solutions
                          from spw = 0 to the spw 0,1 and spw 1 to spw 2,3.
                          spwmap=[[0,0,1,1],[0,1,0,1]]
      parang -- If True, apply the parallactic angle correction (required
               for polarization calibration)
               default: False
      async --  Run asynchronously
              default = False; do not run asychronously

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'fringefit'
        self.__globals__['taskname'] = 'fringefit'
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
            myparams['refant'] = refant = self.parameters['refant']
            myparams['minsnr'] = minsnr = self.parameters['minsnr']
            myparams['zerorates'] = zerorates = self.parameters['zerorates']
            myparams['globalsolve'] = globalsolve = self.parameters['globalsolve']
            myparams['niter'] = niter = self.parameters['niter']
            myparams['delaywindow'] = delaywindow = self.parameters['delaywindow']
            myparams['ratewindow'] = ratewindow = self.parameters['ratewindow']
            myparams['append'] = append = self.parameters['append']
            myparams['docallib'] = docallib = self.parameters['docallib']
            myparams['callib'] = callib = self.parameters['callib']
            myparams['gaintable'] = gaintable = self.parameters['gaintable']
            myparams['gainfield'] = gainfield = self.parameters['gainfield']
            myparams['interp'] = interp = self.parameters['interp']
            myparams['spwmap'] = spwmap = self.parameters['spwmap']
            myparams['parang'] = parang = self.parameters['parang']

        if type(delaywindow)==float: delaywindow=[delaywindow]
        if type(ratewindow)==float: ratewindow=[ratewindow]
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
        mytmp['refant'] = refant
        mytmp['minsnr'] = minsnr
        mytmp['zerorates'] = zerorates
        mytmp['globalsolve'] = globalsolve
        mytmp['niter'] = niter
        mytmp['delaywindow'] = delaywindow
        mytmp['ratewindow'] = ratewindow
        mytmp['append'] = append
        mytmp['docallib'] = docallib
        mytmp['callib'] = callib
        mytmp['gaintable'] = gaintable
        mytmp['gainfield'] = gainfield
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        mytmp['parang'] = parang
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'fringefit.xml')

        casalog.origin('fringefit')
        try :
          #if not trec.has_key('fringefit') or not casac.casac.utils().verify(mytmp, trec['fringefit']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['fringefit'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('fringefit', 'fringefit.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'fringefit'
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
          result = fringefit(vis, caltable, field, spw, intent, selectdata, timerange, antenna, scan, observation, msselect, solint, combine, refant, minsnr, zerorates, globalsolve, niter, delaywindow, ratewindow, append, docallib, callib, gaintable, gainfield, interp, spwmap, parang)

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
             tname = 'fringefit'
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
#        paramgui.runTask('fringefit', myf['_ip'])
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
        a['refant']  = ''
        a['minsnr']  = 3.0
        a['zerorates']  = False
        a['globalsolve']  = True
        a['niter']  = 100
        a['delaywindow']  = []
        a['ratewindow']  = []
        a['append']  = False
        a['docallib']  = False
        a['parang']  = False

        a['selectdata'] = {
                    0:odict([{'value':True}, {'timerange':''}, {'uvrange':''}, {'antenna':''}, {'scan':''}, {'observation':''}, {'msselect':''}]), 
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
    def description(self, key='fringefit', subkey=None):
        desc={'fringefit': 'Fringe fit delay and rates',
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
               'refant': 'Reference antenna name(s)',
               'minsnr': 'Reject solutions below this signal-to-noise ratio (at the FFT stage)',
               'zerorates': 'Zero delay-rates in solution table',
               'globalsolve': 'Refine estimates of delay and rate with global least-squares solver',
               'niter': 'Maximum number of iterations for least-squares solver',
               'delaywindow': 'Constrain FFT delay search to a window; a two-element list, units of nanoseconds',
               'ratewindow': 'Constrain FFT rate search to a window; a two-element list, units of seconds per second',
               'append': 'Append solutions to the (existing) table',
               'docallib': 'Use callib or traditional cal apply parameters',
               'callib': 'Cal Library filename',
               'gaintable': 'Gain calibration table(s) to apply on the fly',
               'gainfield': 'Select a subset of calibrators from gaintable(s)',
               'interp': 'Temporal interpolation for each gaintable (''=linear)',
               'spwmap': 'Spectral windows combinations to form for gaintables(s)',
               'parang': 'Apply parallactic angle correction on the fly',

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
        a['refant']  = ''
        a['minsnr']  = 3.0
        a['zerorates']  = False
        a['globalsolve']  = True
        a['niter']  = 100
        a['delaywindow']  = []
        a['ratewindow']  = []
        a['append']  = False
        a['docallib']  = False
        a['callib']  = ''
        a['gaintable']  = ['']
        a['gainfield']  = ['']
        a['interp']  = ['']
        a['spwmap']  = []
        a['parang']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['selectdata']  == True:
            a['timerange'] = ''
            a['uvrange'] = ''
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
fringefit_cli = fringefit_cli_()
