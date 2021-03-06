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
import task_mstransform
def mstransform(vis='', outputvis='', createmms=False, separationaxis='auto', numsubms='auto', tileshape=[0], field='', spw='', scan='', antenna='', correlation='', timerange='', intent='', array='', uvrange='', observation='', feed='', datacolumn='corrected', realmodelcol=False, keepflags=True, usewtspectrum=False, combinespws=False, chanaverage=False, chanbin=1, hanning=False, regridms=False, mode='channel', nchan=-1, start=0, width=1, nspw=1, interpolation='linear', phasecenter='', restfreq='', outframe='', veltype='radio', preaverage=False, timeaverage=False, timebin='0s', timespan='', maxuvwdistance=0.0, docallib=False, callib='', douvcontsub=False, fitspw='', fitorder=0, want_cont=False, denoising_lib=True, nthreads=1, niter=1, disableparallel=False, ddistart=-1, taql='', monolithic_processing=False, reindex=True):

        """Split the MS, combine/separate/regrid spws and do channel and time averaging  

    Detailed description of keyword arguments:

--- Input/Output parameters ---
    vis -- Name of input visibility file
        default: ''; example: vis='ngc5921.ms'

    outputvis -- Name of output visibility file or Multi-MS
        default: ''; example: outputvis='ngc5921.mms'

    createmms -- Create an output Multi-MS from an input MS.
        default: False

        This parameter only has effect if set to True, when it will try
        to create an output Multi-MS from an input MS. The one-to-one
        relation of input/output in mstransform is:
          input MS  --  output MS
          input MMS --  output MMS
    
        by setting createmms=True, the following is possible:
          input MS  --  output MMS
            
        NOTE: See information on processing input Multi-MS at the end of this help section.        

        separationaxis -- Axis to do parallelization across. 
            default: 'auto'
            options: 'scan', 'spw', 'auto', 'baseline'

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
                
    tileshape -- List with 1 or 3 elements describing the tile shape that will be used
                 to save the columns to disk. (list)
        default: [0]
        options: [0] or [1] or [int,int,int]. When list has only one element, it should
                 be either 0 or 1. When the list has three elements, they should be the
                 number of correlations, channels, rows.


--- Data selection parameters ---
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

               NOTE: mstransform does not support multiple channel ranges per
                     spectral window (';').

    scan -- Scan number range
        default: ''=all

    antenna -- Select data based on antenna/baseline
        default: '' (all)
            Non-negative integers are assumed to be antenna indices, and
            anything else is taken as an antenna name.

        examples:
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

    correlation -- Correlation types or expression.
        default: '' (all correlations)
        example: correlation='XX,YY' 

    timerange -- Select data based on time range:
        default: '' (all); examples,
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

    observation -- Select by observation ID(s)
        default: ''=all

    feed -- Selection based on the feed - NOT IMPLEMENTED YET
        default: ''=all


    datacolumn -- Which data column to use for processing (case-insensitive).
        default: 'corrected'; example: datacolumn='data'
        options: 'data', 'model', 'corrected', 'all','float_data', 'lag_data', 
                 'float_data,data', 'lag_data,data'.

            NOTE: 'all' = whichever of the above that are present. If the requested
                          column does not exist, the task will exit with an error.

            When datacolumn is set to either one of the values 'model','all',
            'data,model,corrected', a sub-parameter realmodelcol will be enabled.
            See description below.

        realmodelcol -- Make real a virtual MODEL column. If set to True, a real MODEL_DATA 
                        column will be added to the output MS based on the existing SOURCE_MODEL
                        column.
            default: False


    keepflags -- Keep completely flagged rows in the output or drop them. This has no
                 effect on partially flagged rows. All of the channels and correlations
                 of a row must be flagged for it to be droppable, and a row must be
                 well defined to be keepable. 
    
            IMPORTANT: Regardless of this parameter, flagged data is never included in
                       channel averaging. On the other hand, partially flagged rows will
                       always be included in time averaging. The average value of the
                       flagged data for averages containing ONLY flagged data in the relevant
                       output channel will be written to the output with the corresponding
                       flag set to True, while only unflagged data is used on averages where
                       there is some unflagged data with the flag set to False.
       
        default: True (keep completely flagged rows in the output)


    usewtspectrum -- Force creation of the columns WEIGHT_SPECTRUM and SIGMA_SPECTRUM in the
                     output MS. This flag can be used to force the creation of
                     WEIGHT_SPECTRUM and SIGMA_SPECTRUM when they are not present in the
                     input MS. When set to true, the output WEIGHT_SPECTRUM column will be
                     populated using the input WEIGHT column, such that each channel in the
                     WEIGHT_SPECTRUM column will get WEIGHT/nChannels. Note that if the
                     WEIGHT_SPECTRUM column is present in the input MS the columns will
                     always be created in the output MS, regardless of the value of this
                     parameter.

        default: False


--- SPW combination parameters ---
    combinespws -- Combine the input spws into a new output spw.
        default: False

            NOTE: This option is only supported when the number of channels is the same for
                  all the spws. Using this option with different numbers of channels for
                  different spws will result in an error.

            NOTE: If the SPWs have different polarization settings only the common
                  polarizations will be output. For instance, if SPW 1 has XX XY YX YY and
                  SPW 2 has XX YY, the output MS will have a single SPW with XX YY polarizations

            NOTE: Whenever the data to be combined has different EXPOSURE values 
                  in the spectral windows, mstransform will use the WEIGHT_SPECTRUM 
                  for the combination. If WEIGHT_SPECTRUM is not available, it will 
                  use the values from the WEIGHT column. Each output channel is calculated 
                  using the following equation:

          outputChannel_j = SUM(inputChannel_i*contributionFraction_i*inputWeightSpectrum_i) 
                           ------------------------------------------------------------------
                                 SUM(contributionFraction_i*inputWeightSpectrum_i)


--- Channel averaging parameters ---
    chanaverage -- Average data across channels. Partially flagged data is not be included in the average
                   unless all data contributing to a given output channel is flagged. In this case, 
                   mstransform calculates the average of all flagged data, and writes it to the output MS
                   with the corresponding flag set to true. If present, WEIGHT_SPECTRUM/SIGMA_SPECTRUM
                   are used together with the channelized flags (FLAG), to compute a weighted average 
                   (using WEIGHT_SPECTRUM for CORRECTED_DATA and SIGMA_SPECTRUM for DATA).    
        default: False

        chanbin -- Bin width for channel average in number of input channels.
                   If a list is given, each bin applies to one of the selected SPWs.
                   
            default: 1 => no channel averaging.
            options: (int) or [int]
            example: chanbin=[2,3] => average 2 channels of 1st selected
                     spectral window and 3 in the second one.
    
            NOTE: WEIGHT_SPECTRUM/SIGMA_SPECTRUM will be used (if present) in
                  addition to the flags to compute a weighted average. The calculations
                  is done as follows:
    
             1) When WEIGHT_SPECTRUM/SIGMA_SPECTRUM are not present:
                    Avg = SUM(Chan_i*Flag_i)/SUM(Flag_i) 
    
             2) When WEIGHT_SPECTRUM/SIGMA_SPECTRUM are present:
                    Avg = SUM(Chan_i*Flag_i*WeightSpectrum_i)/SUM(Flag_i*WeightSpectrum_i)

           If combinespws=True, then chanbin can only be a (int). This is because the
           channel average then refers to the already combined MS after spw combination,
           which has a single spw.


--- Hanning smoothing parameters --- 
    hanning -- Hanning smooth frequency channel data to remove Gibbs ringing.
        default: False

--- Regrid parameters ---
    regridms -- Transform channel labels and visibilities to a different spectral reference frame. 
                Notice that u,v,w data is not transformed. 
        default: False

        mode -- Regridding mode.
            default: 'channel'; produces equidistant grid based on first selected channel.
            options: 'velocity', 'frequency', 'channel_b'.

            When set to velocity or frequency, it means that the channels must be specified
            in the respective units. When set to channel_b it means an alternative 'channel' 
            mode that does not force an equidistant grid. It is faster.

        nchan -- Number of channels in the output spw (int).
            default: -1

        start -- First channel to use in the output spw (depends on the mode)
            default: 0 --> when mode='channel'

            When mode='channel', 'start' means the first channel in the input spw
            to use when creating the output spw. When mode='frequency' or mode='velocity',
            'start' means the frequency or velocity, respectively, of the first output
            channel. If this information is not available, leave it blank and mstransform
            will calculate it.

        width -- Width of input channels that are used to create an output channel. 
            default: 1

            Note that mstransform will only shift spws with channel widths of the same 
            sign in a single operation. If you are regridding spws with mixed positive 
            and negative channel widths, you should run this task separated for each 
            group of spws. You can verify the channel widths for your MS using 
            listobs for example, and looking at the SPW table, column ChanWid.
            
        nspw -- Number of output spws to create in the output MS/MMS (int). 
            default: 1  --> it means, do not separate the spws.

            One can regrid the MS or not and further separate the
            output into a given number of spws. Internally, the framework
            will combine the selected spws before separating them so that
            channel gaps and overlaps are taken into account. This parameter
            will create a regular grid of spws in the output MS. If nchan
            is set, it will refer to the number of output channels in each
            of the separated spws.

        interpolation -- Spectral interpolation method.
            default: 'linear'
            options: 'nearest', 'cubic', 'spline', 'fftshift'

        phasecenter -- Direction measure  or fieldid. To be used in mosaics to indicate
               the center direction to be used in the spectral coordinate transformation.
            default: '' (first selected field)
            options: FIELD_ID (int) or center coordinate measure (str).
            example: phasecenter=6 or phasecenter='J2000 19h30m00 -40d00m00'

        restfreq -- Specify rest frequency to use for output.
            default: ''; occasionally it is necessary to set this.
            example1 for some VLA spectral line data.
            example2 for NH_3 (1,1) put restfreq='23.694496GHz'.

        outframe -- Output reference frame (case-insensitive).
            default: ''; it will keep the input reference frame.
            options: 'LSRK', 'LSRD', 'BARY', 'GALACTO', 'LGROUP', 'CMB', 'GEO', 'TOPO'.

        veltype -- Definition of velocity (as used in mode).
            default: 'radio'

        preaverage -- Pre-average channels before regridding. This is done when the ratio
                      between the output and and input widths is greater than 2. This has
                      been disabled since CASA 5.0
            default: False


--- Time averaging parameters ---
    timeaverage -- Average data across time. Partially flagged data is not be included in the average
                   unless all data contributing to a given output channel is flagged. In this case, 
                   mstransform calculates the average of all flagged data, and writes it to the output MS
                   with the corresponding flag set to true. If keepflags=False, the fully flagged data
                   is not be written to the output MS. If present, WEIGHT_SPECTRUM/SIGMA_SPECTRUM
                   are used together with the channelized flags (FLAG), to compute a weighted average 
                   (using WEIGHT_SPECTRUM for CORRECTED_DATA and SIGMA_SPECTRUM for DATA). Otherwise 
                   WEIGHT/SIGMA are used instead to average together data from different integrations.    

        default: False

        timebin -- Bin width for time average in seconds.
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

--- On-the-fly calibration parameters ---            
    docallib -- Enable on-the-fly (OTF) calibration as in task applycal
        default: False
        
        callib -- Path to calibration library file, which is a ascii file containing
                  the parameters to correct the data as task in task applycal, namely
                  gaintable/gainfield/interp/spwmap/calwt. In a Cal Library file, each 
                  row expresses the calibration apply instructions for a particular 
                  caltable and (optionally) a specific selection of data in the MS to 
                  which it is to be applied.
                  
            default: '' (there is no default callib file)    
            
            examples: 
            
            caltable='cal.G' tinterp='linear' calwt=True
            
            -> Arrange a caltable called cal.G to be applied (with no detailed selection) 
            to all MS data with linear interpolation in time, and with the weights also 
            calibrated.
            
            caltable='cal.G' tinterp='linear' fldmap='nearest' spwmap=[0,1,1,3] calwt=True
            caltable='cal.B' finterp='linear' fldmap='3' spwmap=[0,0,0,0] calwt=False    
            
            -> In this case, solutions from cal.G will be selected based on directional 
            proximity ('nearest') for each MS field via the fldmap parameter, and spw 2 
            will be calibrated by spw 1 solutions. For cal.B, solutions from field id 3 
            will be used exclusively, with spw 0 calibrating all MS spws.
            


        
    ------ Multi-MS Processing and Heuristics ---------
    
    ** Input Multi-MS (MMS) **

    Task mstransform will process an input MMS in parallel whenever possible. Each sub-MS of
    the MMS will be processed in a separate engine and the results will be post-processed at the
    end to create an output MMS. The output MMS will have the same separationaxis of the input
    MMS, which will be written to the table.info file inside the MMS directory.

    Naturally, some transformations available in mstransform require more care when the user
    first partition the MS. If one wants to do a combination of spws by setting the parameter
    combinespws = True in mstransform, the input MMS needs to contain all the
    selected spws in each of the sub-MSs or the processing will fail. For this, one may set the initial
    separationaxis to scan or use the default auto with a proper numsubms set so that each sub- MS in 
    the MMS is self-contained with all the necessary spws for the combination.

    The task will check if the sub-MSs contain all the selected spws when combinespws=True
    and if not, it will issue a warning and process the input MMS as a monolithic MS. In this
    case, the separation axis of the output MMS will be set to scan, regardless of what the input
    axis was. 

    A similar case happens when the separation axis of the input MMS is per scan and the user
    asks to do time averaging with time spanning across scans. If the individual sub-MSs are not
    self-contained of the necessary scans and the duration of the scans is shorter than the given
    timebin, the spanning will not be possible. In this case, the task will process the input MMS as
    a monolithic MS and will set the axis of the output MMS to spw. 

    It is important that the user sets the separation axis correctly when first partitioning the MS.
    See the table below for when it is possible to process the input MMS in parallel or not, using
    mstransform.
        
    input MMS axis   combinespws=True   nspw > 1   timeaverage=True, timespan='scan'
    -------------------------------------------------------------------------------
    scan                  YES            YES             NO        
    spw                   NO             NO              YES     
    auto                  MAYBE          MAYBE           MAYBE             
                
    
------ EXAMPLES ------

More documentation on mstransform can be found here:
http://www.eso.org/~scastro/ALMA/casa/MST/MSTransformDocs/MSTransformDocs.html

1) Split out a single channel.
    mstransform(vis='ctb80-vsm.ms', outputvis='mychn.ms', datacolumn='data', spw='0:25')

2) Only combine the selected spws into a single output spw.
    mstransform(vis='Four_ants.ms', outputvis='myspw.ms', combinespws=True, spw='0~3')

3) Combine two spws and regrid one field, using two input channels to make one output.
    mstransform(vis='jupiter6cm.demo.ms',outputvis='test1.ms',datacolumn='DATA',field='11',
                spw='0,1', combinespws=True, regridms=True, nchan=1, width=2)

4) Combine 24 spws and regrid in frequency mode to create 21 output channels. Change the 
   phase center.
    mstransform(vis='g19_d2usb_targets_line.ms', outputvis='test2.ms', datacolumn='DATA',
                combinespws=True, regridms=True, mode='frequency', nchan=21, start='229587.0MHz',
                width='1600kHz', phasecenter="J2000 18h25m56.09 -12d04m28.20")

5) Only apply Hanning smoothing to MS.
    mstransform(vis='g19_d2usb_targets_line.ms', outputvis='test3.ms', datacolumn='DATA',
                hanning=True)
 
6) Change the reference frame and apply Hanning smoothing after combining all spws.
    mstransform(vis='g19_d2usb_targets_line.ms', outputvis='test4.ms', datacolumn='DATA',
                combinespws=True, regridms=True, mode="channel", outframe="BARY",
                phasecenter="J2000 18h25m56.09 -12d04m28.20", hanning = True)

7) Apply time averaging using a bin of 30 seconds on the default CORRECTED column.
    mstransform(vis='g19_d2usb_targets_line.ms', outputvis='test5.ms', timeaverage=True,
                timebin='30s')
                
8) Apply OTF calibration to ng5921 using a calibration library
    mstransform(vis='ngc5921.ms', outputvis='ngc5921_calibrated.ms',docallib=True,
                callib='unittest/mstransform/ngc5921_regression/ngc5921_callib.txt')                



        """
        if type(tileshape)==int: tileshape=[tileshape]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['outputvis'] = outputvis
        mytmp['createmms'] = createmms
        mytmp['separationaxis'] = separationaxis
        mytmp['numsubms'] = numsubms
        mytmp['tileshape'] = tileshape
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
        mytmp['realmodelcol'] = realmodelcol
        mytmp['keepflags'] = keepflags
        mytmp['usewtspectrum'] = usewtspectrum
        mytmp['combinespws'] = combinespws
        mytmp['chanaverage'] = chanaverage
        mytmp['chanbin'] = chanbin
        mytmp['hanning'] = hanning
        mytmp['regridms'] = regridms
        mytmp['mode'] = mode
        mytmp['nchan'] = nchan
        mytmp['start'] = start
        mytmp['width'] = width
        mytmp['nspw'] = nspw
        mytmp['interpolation'] = interpolation
        mytmp['phasecenter'] = phasecenter
        mytmp['restfreq'] = restfreq
        mytmp['outframe'] = outframe
        mytmp['veltype'] = veltype
        mytmp['preaverage'] = preaverage
        mytmp['timeaverage'] = timeaverage
        mytmp['timebin'] = timebin
        mytmp['timespan'] = timespan
        mytmp['maxuvwdistance'] = maxuvwdistance
        mytmp['docallib'] = docallib
        mytmp['callib'] = callib
        mytmp['douvcontsub'] = douvcontsub
        mytmp['fitspw'] = fitspw
        mytmp['fitorder'] = fitorder
        mytmp['want_cont'] = want_cont
        mytmp['denoising_lib'] = denoising_lib
        mytmp['nthreads'] = nthreads
        mytmp['niter'] = niter
        mytmp['disableparallel'] = disableparallel
        mytmp['ddistart'] = ddistart
        mytmp['taql'] = taql
        mytmp['monolithic_processing'] = monolithic_processing
        mytmp['reindex'] = reindex
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'mstransform.xml')

        casalog.origin('mstransform')
        if trec.has_key('mstransform') and casac.utils().verify(mytmp, trec['mstransform']) :
            result = task_mstransform.mstransform(vis, outputvis, createmms, separationaxis, numsubms, tileshape, field, spw, scan, antenna, correlation, timerange, intent, array, uvrange, observation, feed, datacolumn, realmodelcol, keepflags, usewtspectrum, combinespws, chanaverage, chanbin, hanning, regridms, mode, nchan, start, width, nspw, interpolation, phasecenter, restfreq, outframe, veltype, preaverage, timeaverage, timebin, timespan, maxuvwdistance, docallib, callib, douvcontsub, fitspw, fitorder, want_cont, denoising_lib, nthreads, niter, disableparallel, ddistart, taql, monolithic_processing, reindex)

        else :
          result = False
        return result
