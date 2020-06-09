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
from task_polcal import polcal
class polcal_cli_:
    __name__ = "polcal"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (polcal_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'caltable':None, 'field':None, 'spw':None, 'intent':None, 'selectdata':None, 'timerange':None, 'uvrange':None, 'antenna':None, 'scan':None, 'observation':None, 'msselect':None, 'solint':None, 'combine':None, 'preavg':None, 'refant':None, 'minblperant':None, 'minsnr':None, 'poltype':None, 'smodel':None, 'append':None, 'docallib':None, 'callib':None, 'gaintable':None, 'gainfield':None, 'interp':None, 'spwmap':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, caltable=None, field=None, spw=None, intent=None, selectdata=None, timerange=None, uvrange=None, antenna=None, scan=None, observation=None, msselect=None, solint=None, combine=None, preavg=None, refant=None, minblperant=None, minsnr=None, poltype=None, smodel=None, append=None, docallib=None, callib=None, gaintable=None, gainfield=None, interp=None, spwmap=None, ):

        """Determine instrumental polarization calibrations

        Detailed Description:

The complex instrumental polarization factors (D-terms) for each antenna/spwid 
are determined from the data for the specified calibrator sources. Previous 
calibrations can be applied on the fly.

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

                uvrange: Select data within uvrange (default units meters)
                   Default Value: 

                antenna: Select data based on antenna/baseline
                   Default Value: 

                scan: Scan number range
                   Default Value: 

                observation: Select by observation ID(s)
                   Default Value: 

                msselect: Optional complex data selection (ignore for now)
                   Default Value: 

                solint: Solution interval
                   Default Value: inf

                combine: Data axes which to combine for solve (obs, scan, spw, and/or field)
                   Default Value: obs,scan

                preavg: Pre-averaging interval (sec)
                   Default Value: 300.0

                refant: Reference antenna name(s)
                   Default Value: 

                minblperant: Minimum baselines _per antenna_ required for solve
                   Default Value: 4

                minsnr: Reject solutions below this SNR
                   Default Value: 3.0

                poltype: Type of instrumental polarization solution (see help)
                   Default Value: D+QU
                   Allowed Values:
                                D
                                Df
                                D+X
                                Df+X
                                D+QU
                                Df+QU
                                Dgen
                                Dfgen
                                Dgen+X
                                Dfgen+X
                                Dgen+QU
                                Dfgen+QU
                                Dlls
                                Dflls
                                X
                                Xf
                                Xparang+QU
                                Xfparang+QU
                                PosAng
                                Xj

                smodel: Point source Stokes parameters for source model.
                   Default Value: 

                append: Append solutions to the (existing) table
                   Default Value: False

                docallib: Use callib or traditional cal apply parameters
                   Default Value: False

                callib: Cal Library filename
                   Default Value: 

                gaintable: Gain calibration table(s) to apply
                   Default Value: 

                gainfield: Select a subset of calibrators from gaintable(s)
                   Default Value: 

                interp: Interpolation mode (in time) to use for each gaintable
                   Default Value: 

                spwmap: Spectral windows combinations to form for gaintables(s)
                   Default Value: 


        Example :


      The instrumental polarization factors (D-terms), the calibrator polarization,
      and the R-L polarization angle can be determined using polcal.  The solutions
      can be obtained for each antenna/spwid and even individual channels, if desired.
      Previous calibrations of the total intensity data should be applied on the fly
      when running polcal, since polcal uses the 'data' column, not the 'corrected'
      column.

      After calibrating the gain, bandpass, and (if relevant, for channelized data)
      cross-hand delay, the simplest way to calibrate the polarization data is:

        a) Run polcal with poltype = 'D+QU' on the main 'calibrator' source.  The D terms
           and polarization (QU) of the calibrator will be determined.  Relatively good
           parallactic angle coverage is needed.

        b) If there is little parallactic angle coverage, place the known polarization of
           the main calibrator (or 0) using setjy with the appropriate fluxdensity.  Then
           run polcal with poltype = 'D'.  Run plotcal with xaxis = 'real'; yaxis ='imag'
           to view solutions.  It is best to use an unpolarized calibrator in this 
           instance; large systematic offsets from zero indicate significant source  
           polarization that will bias the polarization calibration.  A mechanism 
           to constrain this bias will be made available in the near future. 

        c) To determine R-L polarization angle, use setjy to put the fluxdensity of the
           polarization calibrator [I,Q,U,0.0] in the model column.  For resolved sources
           put in values associated with an appropriate u-v range.  Polarized models are
           not yet available for the major polarization standard sources, so very
           resolved polarized sources should not be used.

        d) Run polcal with poltype = 'X' and include polarization standard.  Make sure to
           include all previous calibrations, especially the D results.  Run plotxy with
           correlation = 'RL LR' and make sure polarization angles are as expected.

        e) Run applycal with all calibration table, include the D and X tables.  Make sure
           that parang = T

         NOTE: For very high dynamic range, use poltype='Df' or 'Df+QU' to determine 
               D terms for each channel.  Similarly, poltype='Xf' can
               be used to determine a channel-dependent R-L phase
               "bandpass".
         NOTE: Rather than use setjy in b and c above, the new smodel
               parameter may be used in polcal to specify a simple
               point source Stokes model.  

      Keyword arguments:
      vis -- Name of input visibility file
              default: none; example: vis='ngc5921.ms'
      caltable -- Name of output gain calibration table
              default: none; example: caltable='ngc5921.dcal'

      --- Data Selection (see help par.selectdata for more detailed information)

      field -- Select field using field id(s) or field name(s).
                 [run listobs to obtain the list id's or names]
              default: ''=all fields.
                  Most likely, the main calibrator source should be picked.
              If field string is a non-negative integer, it is assumed a field index
                otherwise, it is assumed a field name
              field='0~2'; field ids 0,1,2
              field='0,4,5~7'; field ids 0,4,5,6,7
              field='3C286,3C295'; field named 3C286 adn 3C295
              field = '3,4C*'; field id 3, all names starting with 4C
      spw -- Select spectral window/channels 
               type 'help par.selection' for more examples.
             spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
             spw='<2';  spectral windows less than 2 (i.e. 0,1)
             spw='0:5~61'; spw 0, channels 5 to 61, INCLUSIVE
             spw='*:5~61'; all spw with channels 5 to 62
             spw='0,10,3:3~45'; spw 0,10 all channels, spw 3, channels 3 to 45.
             spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
             spw='0:0~10;15~60'; spectral window 0 with channels 0-10,15-60
                       NOTE ';' to separate channel selections
             spw='0:0~10^2,1:20~30^5'; spw 0, channels 0,2,4,6,8,10,
                   spw 1, channels 20,25,30
      intent -- Select observing intent
                default: ''  (no selection by intent)
                intent='*BANDPASS*'  (selects data labelled with
                                      BANDPASS intent)
      selectdata -- Other data selection parameters
              default: True
      timerange  -- Select data based on time range:
              default = '' (all); examples,
              timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
              Note: if YYYY/MM/DD is missing dat defaults to first day in data set
              timerange='09:14:0~09:54:0' picks 40 min on first day
              timerange= '25:00:00~27:30:00' picks 1 hr to 3 hr 30min on next day
              timerange='09:44:00' data within one integration of time
              timerange='>10:24:00' data after this time
      uvrange -- Select data within uvrange (default units meters)
              default: '' (all); example:
              uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
              uvrange='>4klambda';uvranges greater than 4 kilo-lambda
      antenna -- Select data based on antenna/baseline
              default: '' (all)
              If antenna string is a non-negative integer, it is assumed an antenna index
                otherwise, it is assumed as an antenna name
              antenna='5&6'; baseline between antenna index 5 and index 6.
              antenna='VA05&VA06'; baseline between VLA antenna 5 and 6.
              antenna='5&6;7&8'; baseline 5-6 and 7-8
              antenna='5'; all baselines with antenna index 5
              antenna='05'; all baselines with antenna name 05, i.e. VLA ant 5
              antenna='5,6,10'; all baselines with antennas 5, 6 and 10
      scan -- Scan number range
      observation -- Observation ID(s).
                     default: '' = all
                     example: '0~2,4'
      msselect -- Optional complex data selection (ignore for now)

      --- Solution parameters
      poltype -- Type of instrumental polarization solution
              'D+QU' (or 'Df+QU')  solve also for apparent source polarization (channelized D)
                 Need relatively good parallactic angle coverage for this
              'D' (or 'Df') solve only for instrumental polarization (channelized).  The
                 I, Q, U flux density of the source can be placed in the model column using
                 setjy.  Use for poor parallactic angle coverage.
              'X' (or 'Xf') = solve only for position angle correction (channelized).  
                 The source must have its I, Q, U flux density in the model column 
                 or specified in smodel.  If the source is resolved, use a limited 
                 uvrange that is appropriate.
              'D+X' (or 'Df+X') = solve also for position angle offset (channelized D) as
                 well as the D-term.  Not normally done.
              default: 'D+QU'
              The solution used the traditional linear approximation.  Non-linearized options
                  will be avaible soon.
      smodel -- Point source Stokes parameters for source model (experimental)
              default: [] (use MODEL_DATA column)
              examples: [1,0,0,0] (I=1, unpolarized)
                        [5.2,0.2,0.3,0.0] (I=5.2, Q=0.2, U=0.3, V=0.0)
      solint --  Solution interval (units optional) 
              default: 'inf' (~infinite, up to boundaries controlled by combine); 
              Options: 'inf' (~infinite), 'int' (per integration), any float
                       or integer value with or without units
              examples: solint='1min'; solint='60s', solint=60 --> 1 minute
                        solint='0s'; solint=0; solint='int' --> per integration
                        solint-'-1s'; solint='inf' --> ~infinite, up to boundaries
                        enforced by combine
      combine -- Data axes to combine for solving
              default: 'obs,scan' --> solutions will break at field and spw
                      boundaries but may extend over multiple obs and scans
                      (per field and spw) up to solint.
              Options: '','obs','scan','spw',field', or any comma-separated 
                       combination in a single string
              example: combine='scan,spw' --> extend solutions over scan boundaries
                       (up to the solint), and combine spws for solving
      preavg -- Pre-averaging interval (sec)
              default=300
              Interval to apply parallactic angle.
      refant -- Reference antenna name
              default: '' => refant = '0'
              example: refant='13' (antenna with index 13)
                       refant='VA04' (VLA antenna #4)
                       refant='EA02,EA23,EA13' (EVLA antenna EA02, use
                                EA23 and EA13 as alternates if/when EA02
                                drops out)
              Use 'go listobs' for antenna listing.
              USE SAME REFERENCE ANTENNA AS USED FOR I CALIBRATION.
      minblperant -- Minimum number of baselines required per antenna for each solve
                   Antennas with fewer baaselines are excluded from solutions. Amplitude
                   solutions with fewer than 4 baselines, and phase solutions with fewer 
                   than 3 baselines are only trivially constrained, and are no better
                   than baseline-based solutions.
                   default: 4
                   example: minblperant=10  => Antennas participating on 10 or more 
                            baselines are included in the solve
      minsnr -- Reject solutions below this SNR
              default: 3.0
      append -- Append solutions to the (existing) table.  Appended solutions
                  must be derived from the same MS as the existing
                  caltable, and solution spws must have the same
                   meta-info (according to spw selection and solint)
                   or be non-overlapping.
              default: False; overwrite existing table or make new table

      --- Other calibrations to apply on the fly before determining polcal solution

      docallib -- Control means of specifying the caltables:
               default: False ==> Use gaintable,gainfield,interp,spwmap,calwt
                        If True, specify a file containing cal library in callib
      callib -- If docallib=True, specify a file containing cal
                  library directives

      gaintable -- Gain calibration table(s) to apply 
               default: '' (none);  BUT I CALIBRATION TABLES SHOULD GENERALLY BE INCLUDED
               examples: gaintable='ngc5921.gcal'
                         gaintable=['ngc5921.ampcal','ngc5921.phcal']
      gainfield -- Select a subset of calibrators from gaintable(s)
               default:'' ==> all sources in table;
               'nearest' ==> nearest (on sky) available field in table
               otherwise, same syntax as field
               example: gainfield='0~3'
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
      async --  Run asynchronously
               default = False; do not run asychronously

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'polcal'
        self.__globals__['taskname'] = 'polcal'
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
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['msselect'] = msselect = self.parameters['msselect']
            myparams['solint'] = solint = self.parameters['solint']
            myparams['combine'] = combine = self.parameters['combine']
            myparams['preavg'] = preavg = self.parameters['preavg']
            myparams['refant'] = refant = self.parameters['refant']
            myparams['minblperant'] = minblperant = self.parameters['minblperant']
            myparams['minsnr'] = minsnr = self.parameters['minsnr']
            myparams['poltype'] = poltype = self.parameters['poltype']
            myparams['smodel'] = smodel = self.parameters['smodel']
            myparams['append'] = append = self.parameters['append']
            myparams['docallib'] = docallib = self.parameters['docallib']
            myparams['callib'] = callib = self.parameters['callib']
            myparams['gaintable'] = gaintable = self.parameters['gaintable']
            myparams['gainfield'] = gainfield = self.parameters['gainfield']
            myparams['interp'] = interp = self.parameters['interp']
            myparams['spwmap'] = spwmap = self.parameters['spwmap']

        if type(smodel)==float: smodel=[smodel]
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
        mytmp['uvrange'] = uvrange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['observation'] = observation
        mytmp['msselect'] = msselect
        mytmp['solint'] = solint
        mytmp['combine'] = combine
        mytmp['preavg'] = preavg
        mytmp['refant'] = refant
        mytmp['minblperant'] = minblperant
        mytmp['minsnr'] = minsnr
        mytmp['poltype'] = poltype
        mytmp['smodel'] = smodel
        mytmp['append'] = append
        mytmp['docallib'] = docallib
        mytmp['callib'] = callib
        mytmp['gaintable'] = gaintable
        mytmp['gainfield'] = gainfield
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'polcal.xml')

        casalog.origin('polcal')
        try :
          #if not trec.has_key('polcal') or not casac.casac.utils().verify(mytmp, trec['polcal']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['polcal'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('polcal', 'polcal.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'polcal'
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
          result = polcal(vis, caltable, field, spw, intent, selectdata, timerange, uvrange, antenna, scan, observation, msselect, solint, combine, preavg, refant, minblperant, minsnr, poltype, smodel, append, docallib, callib, gaintable, gainfield, interp, spwmap)

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
             tname = 'polcal'
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
#        paramgui.runTask('polcal', myf['_ip'])
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
        a['combine']  = 'obs,scan'
        a['preavg']  = 300.0
        a['refant']  = ''
        a['minblperant']  = 4
        a['minsnr']  = 3.0
        a['poltype']  = 'D+QU'
        a['smodel']  = []
        a['append']  = False
        a['docallib']  = False

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
    def description(self, key='polcal', subkey=None):
        desc={'polcal': 'Determine instrumental polarization calibrations',
               'vis': 'Name of input visibility file',
               'caltable': 'Name of output gain calibration table',
               'field': 'Select field using field id(s) or field name(s)',
               'spw': 'Select spectral window/channels',
               'intent': 'Select observing intent',
               'selectdata': 'Other data selection parameters',
               'timerange': 'Select data based on time range',
               'uvrange': 'Select data within uvrange (default units meters)',
               'antenna': 'Select data based on antenna/baseline',
               'scan': 'Scan number range',
               'observation': 'Select by observation ID(s)',
               'msselect': 'Optional complex data selection (ignore for now)',
               'solint': 'Solution interval',
               'combine': 'Data axes which to combine for solve (obs, scan, spw, and/or field)',
               'preavg': 'Pre-averaging interval (sec)',
               'refant': 'Reference antenna name(s)',
               'minblperant': 'Minimum baselines _per antenna_ required for solve',
               'minsnr': 'Reject solutions below this SNR',
               'poltype': 'Type of instrumental polarization solution (see help)',
               'smodel': 'Point source Stokes parameters for source model.',
               'append': 'Append solutions to the (existing) table',
               'docallib': 'Use callib or traditional cal apply parameters',
               'callib': 'Cal Library filename',
               'gaintable': 'Gain calibration table(s) to apply',
               'gainfield': 'Select a subset of calibrators from gaintable(s)',
               'interp': 'Interpolation mode (in time) to use for each gaintable',
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
        a['uvrange']  = ''
        a['antenna']  = ''
        a['scan']  = ''
        a['observation']  = ''
        a['msselect']  = ''
        a['solint']  = 'inf'
        a['combine']  = 'obs,scan'
        a['preavg']  = 300.0
        a['refant']  = ''
        a['minblperant']  = 4
        a['minsnr']  = 3.0
        a['poltype']  = 'D+QU'
        a['smodel']  = []
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
polcal_cli = polcal_cli_()
