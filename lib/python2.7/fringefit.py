#
# This file was generated using xslt from its XML file
#
# Copyright 2009, Associated Universities Inc., Washington DC
#
import sys
import os
from  casac import *
import string
from taskinit import casalog
from taskinit import xmlpath
#from taskmanager import tm
import task_fringefit
def fringefit(vis='', caltable='', field='', spw='', intent='', selectdata=True, timerange='', antenna='', scan='', observation='', msselect='', solint='inf', combine='', refant='', minsnr=3.0, zerorates=False, globalsolve=True, niter=100, delaywindow=[], ratewindow=[], append=False, docallib=False, callib='', gaintable=[''], gainfield=[''], interp=[''], spwmap=[], parang=False):

        """Fringe fit delay and rates

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
        if type(delaywindow)==float: delaywindow=[delaywindow]
        if type(ratewindow)==float: ratewindow=[ratewindow]
        if type(gaintable)==str: gaintable=[gaintable]
        if type(gainfield)==str: gainfield=[gainfield]
        if type(interp)==str: interp=[interp]
        if type(spwmap)==int: spwmap=[spwmap]

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
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'fringefit.xml')

        casalog.origin('fringefit')
        if trec.has_key('fringefit') and casac.utils().verify(mytmp, trec['fringefit']) :
            result = task_fringefit.fringefit(vis, caltable, field, spw, intent, selectdata, timerange, antenna, scan, observation, msselect, solint, combine, refant, minsnr, zerorates, globalsolve, niter, delaywindow, ratewindow, append, docallib, callib, gaintable, gainfield, interp, spwmap, parang)

        else :
          result = False
        return result
