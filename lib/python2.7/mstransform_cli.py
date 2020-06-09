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
from task_mstransform import mstransform
class mstransform_cli_:
    __name__ = "mstransform"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (mstransform_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'outputvis':None, 'createmms':None, 'separationaxis':None, 'numsubms':None, 'tileshape':None, 'field':None, 'spw':None, 'scan':None, 'antenna':None, 'correlation':None, 'timerange':None, 'intent':None, 'array':None, 'uvrange':None, 'observation':None, 'feed':None, 'datacolumn':None, 'realmodelcol':None, 'keepflags':None, 'usewtspectrum':None, 'combinespws':None, 'chanaverage':None, 'chanbin':None, 'hanning':None, 'regridms':None, 'mode':None, 'nchan':None, 'start':None, 'width':None, 'nspw':None, 'interpolation':None, 'phasecenter':None, 'restfreq':None, 'outframe':None, 'veltype':None, 'preaverage':None, 'timeaverage':None, 'timebin':None, 'timespan':None, 'maxuvwdistance':None, 'docallib':None, 'callib':None, 'douvcontsub':None, 'fitspw':None, 'fitorder':None, 'want_cont':None, 'denoising_lib':None, 'nthreads':None, 'niter':None, 'disableparallel':None, 'ddistart':None, 'taql':None, 'monolithic_processing':None, 'reindex':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, outputvis=None, createmms=None, separationaxis=None, numsubms=None, tileshape=None, field=None, spw=None, scan=None, antenna=None, correlation=None, timerange=None, intent=None, array=None, uvrange=None, observation=None, feed=None, datacolumn=None, realmodelcol=None, keepflags=None, usewtspectrum=None, combinespws=None, chanaverage=None, chanbin=None, hanning=None, regridms=None, mode=None, nchan=None, start=None, width=None, nspw=None, interpolation=None, phasecenter=None, restfreq=None, outframe=None, veltype=None, preaverage=None, timeaverage=None, timebin=None, timespan=None, maxuvwdistance=None, docallib=None, callib=None, douvcontsub=None, fitspw=None, fitorder=None, want_cont=None, denoising_lib=None, nthreads=None, niter=None, disableparallel=None, ddistart=None, taql=None, monolithic_processing=None, reindex=None, ):

        """Split the MS, combine/separate/regrid spws and do channel and time averaging

        Detailed Description:

    
    The task mstransform can do the same functionalities available
    in cvel, partition, hanningsmooth and split without the need to read and write
    the output to disk multiple times. The main features of this task
    are:
    
    * take an input MS or Multi-MS (MMS)
    * ability to create an output MS or MMS
    * spw combination and separation
    * channel averaging taking flags and weights into account
    * time averaging taking flags and weights into account
    * reference frame transformation
    * Hanning smoothing
    
    All these transformations will be applied on the fly without any writing to
    disk to optimize I/O. The user can ask to create a Multi-MS in parallel using CASA's 
    cluster infrastructure using the parameter createmms. See MPIInterface 
    for more information on the cluster infrastructure.

    This task is implemented in a modular way to preserve the functionalities
    available in the replaced tasks. One can choose which functionality to apply
    or apply all of them by setting the corresponding parameters to True. Note 
    that there is an order in which the transformations are applied to the data that 
    makes logical sense on the point of view of the data analysis. 

    This task can create a multi-MS as the output. General selection
    parameters are included, and one or all of the various data columns
    (DATA, LAG_DATA and/or FLOAT_DATA, and possibly MODEL_DATA and/or
    CORRECTED_DATA) can be selected. It can also be used to create a normal
    MS, split-based on the given data selection parameters.

    The mstransform task creates a Multi-MS in parallel, using the CASA MPI framework.
    The user should start CASA as follows in order to run it in parallel.
    
    1) Start CASA on a single node with 8 engines. The first engine will be used as the
       MPIClient, where the user will see the CASA prompt. All other engines will be used
       as MPIServers and will process the data in parallel.
           mpicasa -n 8 casa --nogui --log2term
           mstransform(.....)
        
    2) Running on a group of nodes in a cluster.
           mpicasa -hostfile user_hostfile casa ....
           mstransform(.....)
            
        where user_hostfile contains the names of the nodes and the number of engines to use 
        in each one of them. Example:
            pc001234a, slots=5
            pc001234b, slots=4
     
    If CASA is started without mpicasa, it is still possible to create an MMS, but
    the processing will be done in sequential.

    The resulting WEIGHT_SPECTRUM produced by mstransform is in the statistical
    sense correct for the simple cases of channel average and time average, but not for
    the general re-gridding case, in which the error propagation formulas applicable for 
    WEIGHT_SPECTRUM are yet to be defined. Currently, as in cvel and in the imager,
    WEIGHT_SPECTRUM is transformed in the same way as the other data columns.
    Notice that this is not formally correct from the statistical point of view, 
    but is a good approximation at this stage.
        
    NOTE: the input/output in mstransform have a one-to-one relation.
          input MS  --  output MS
          input MMS --  output MMS
    
       unless the user sets the parameter createmms to True to create the following:
          input MS  --  output MMS


        Arguments :
                vis: Name of input Measurement set or Multi-MS.
                   Default Value: 

                outputvis: Name of output Measurement Set or Multi-MS.
                   Default Value: 

                createmms: Create a multi-MS output from an input MS.
                   Default Value: False

                separationaxis: Axis to do parallelization across(scan,spw,auto,baseline).
                   Default Value: auto
                   Allowed Values:
                                auto
                                spw
                                scan
                                baseline

                numsubms: The number of Sub-MSs to create (auto or any number)
                   Default Value: auto

                tileshape: List with 1 or 3 elements giving the tile shape of the disk data columns.
                   Default Value: 0

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

                datacolumn: Which data column(s) to process.
                   Default Value: corrected
                   Allowed Values:
                                corrected
                                data
                                model
                                data,model,corrected
                                float_data
                                lag_data
                                float_data,data
                                lag_data,data
                                all

                realmodelcol: Make real a virtual MODEL column.
                   Default Value: False

                keepflags: Keep *completely flagged rows* or drop them from the output.
                   Default Value: True

                usewtspectrum: Force creation of the columns WEIGHT_SPECTRUM and SIGMA_SPECTRUM in the output MS, even if not present in the input MS.
                   Default Value: False

                combinespws: Combine the input spws into a new output spw. Only supported when the number of channels is the same for all the spws.
                   Default Value: False

                chanaverage: Average data in channels.
                   Default Value: False

                chanbin: Width (bin) of input channels to average to form an output channel.
                   Default Value: 1

                hanning: Hanning smooth data to remove Gibbs ringing.
                   Default Value: False

                regridms: Transform channel labels and visibilities to a different spectral reference frame. Notice that u,v,w data is not transformed. 
                   Default Value: False

                mode: Regridding mode (channel/velocity/frequency/channel_b).
                   Default Value: channel
                   Allowed Values:
                                channel
                                velocity
                                frequency
                                channel_b

                nchan: Number of channels in the output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.
                   Default Value: -1

                start: Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.
                   Default Value: 0

                width: Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.
                   Default Value: 1

                nspw: Number of output spws to create in output MS.
                   Default Value: 1

                interpolation: Spectral interpolation method.
                   Default Value: linear
                   Allowed Values:
                                nearest
                                linear
                                cubic
                                spline
                                fftshift

                phasecenter: Phase center direction to be used for the spectral coordinate transformation: direction measure or field index
                   Default Value: 

                restfreq: Rest frequency to use for output.
                   Default Value: 

                outframe: Output reference frame (''=keep input frame).
                   Default Value: 
                   Allowed Values:
                                topo
                                geo
                                lsrk
                                lsrd
                                bary
                                galacto
                                lgroup
                                cmb
                                source
                                

                veltype: Velocity definition.
                   Default Value: radio
                   Allowed Values:
                                optical
                                radio

                preaverage: Pre-average channels before regridding, when the ratio between the output and and input widths is greater than 2.
                   Default Value: False

                timeaverage: Average data in time.
                   Default Value: False

                timebin: Bin width for time averaging.
                   Default Value: 0s

                timespan: Span the timebin across scan, state or both.
                   Default Value: 

                maxuvwdistance: Maximum separation of start-to-end baselines that can be included in an average. (meters)
                   Default Value: 0.0

                docallib: Enable on-the-fly (OTF) calibration as in task applycal
                   Default Value: False

                callib: Path to calibration library file
                   Default Value: 

                douvcontsub: Enable continuum subtraction as in task uvcontsub
                   Default Value: False

                fitspw: Spectral window:channel selection for fitting the continuum
                   Default Value: 

                fitorder: Polynomial order for the fits
                   Default Value: 0

                want_cont: Produce continuum estimate instead of continuum subtracted data
                   Default Value: False

                denoising_lib: Use new denoising library (based on GSL) instead of casacore fitting routines
                   Default Value: True

                nthreads: Number of OMP threads to use (currently maximum limited by number of polarizations)
                   Default Value: 1

                niter: Number of iterations for re-weighted linear fit
                   Default Value: 1


        Example :
  

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
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'mstransform'
        self.__globals__['taskname'] = 'mstransform'
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
            myparams['tileshape'] = tileshape = self.parameters['tileshape']
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
            myparams['realmodelcol'] = realmodelcol = self.parameters['realmodelcol']
            myparams['keepflags'] = keepflags = self.parameters['keepflags']
            myparams['usewtspectrum'] = usewtspectrum = self.parameters['usewtspectrum']
            myparams['combinespws'] = combinespws = self.parameters['combinespws']
            myparams['chanaverage'] = chanaverage = self.parameters['chanaverage']
            myparams['chanbin'] = chanbin = self.parameters['chanbin']
            myparams['hanning'] = hanning = self.parameters['hanning']
            myparams['regridms'] = regridms = self.parameters['regridms']
            myparams['mode'] = mode = self.parameters['mode']
            myparams['nchan'] = nchan = self.parameters['nchan']
            myparams['start'] = start = self.parameters['start']
            myparams['width'] = width = self.parameters['width']
            myparams['nspw'] = nspw = self.parameters['nspw']
            myparams['interpolation'] = interpolation = self.parameters['interpolation']
            myparams['phasecenter'] = phasecenter = self.parameters['phasecenter']
            myparams['restfreq'] = restfreq = self.parameters['restfreq']
            myparams['outframe'] = outframe = self.parameters['outframe']
            myparams['veltype'] = veltype = self.parameters['veltype']
            myparams['preaverage'] = preaverage = self.parameters['preaverage']
            myparams['timeaverage'] = timeaverage = self.parameters['timeaverage']
            myparams['timebin'] = timebin = self.parameters['timebin']
            myparams['timespan'] = timespan = self.parameters['timespan']
            myparams['maxuvwdistance'] = maxuvwdistance = self.parameters['maxuvwdistance']
            myparams['docallib'] = docallib = self.parameters['docallib']
            myparams['callib'] = callib = self.parameters['callib']
            myparams['douvcontsub'] = douvcontsub = self.parameters['douvcontsub']
            myparams['fitspw'] = fitspw = self.parameters['fitspw']
            myparams['fitorder'] = fitorder = self.parameters['fitorder']
            myparams['want_cont'] = want_cont = self.parameters['want_cont']
            myparams['denoising_lib'] = denoising_lib = self.parameters['denoising_lib']
            myparams['nthreads'] = nthreads = self.parameters['nthreads']
            myparams['niter'] = niter = self.parameters['niter']
            myparams['disableparallel'] = disableparallel = self.parameters['disableparallel']
            myparams['ddistart'] = ddistart = self.parameters['ddistart']
            myparams['taql'] = taql = self.parameters['taql']
            myparams['monolithic_processing'] = monolithic_processing = self.parameters['monolithic_processing']
            myparams['reindex'] = reindex = self.parameters['reindex']

        if type(tileshape)==int: tileshape=[tileshape]

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
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'mstransform.xml')

        casalog.origin('mstransform')
        try :
          #if not trec.has_key('mstransform') or not casac.casac.utils().verify(mytmp, trec['mstransform']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['mstransform'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('mstransform', 'mstransform.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'mstransform'
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
          result = mstransform(vis, outputvis, createmms, separationaxis, numsubms, tileshape, field, spw, scan, antenna, correlation, timerange, intent, array, uvrange, observation, feed, datacolumn, realmodelcol, keepflags, usewtspectrum, combinespws, chanaverage, chanbin, hanning, regridms, mode, nchan, start, width, nspw, interpolation, phasecenter, restfreq, outframe, veltype, preaverage, timeaverage, timebin, timespan, maxuvwdistance, docallib, callib, douvcontsub, fitspw, fitorder, want_cont, denoising_lib, nthreads, niter, disableparallel, ddistart, taql, monolithic_processing, reindex)

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
             tname = 'mstransform'
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
#        paramgui.runTask('mstransform', myf['_ip'])
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
        a['createmms']  = False
        a['tileshape']  = [0]
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
        a['datacolumn']  = 'corrected'
        a['keepflags']  = True
        a['usewtspectrum']  = False
        a['combinespws']  = False
        a['chanaverage']  = False
        a['hanning']  = False
        a['regridms']  = False
        a['preaverage']  = False
        a['timeaverage']  = False
        a['docallib']  = False
        a['douvcontsub']  = False

        a['createmms'] = {
                    0:odict([{'value':False}, {'separationaxis':'auto'}, {'numsubms':'auto'}, {'disableparallel':False}, {'ddistart':-1}, {'taql':''}, {'reindex':True}]), 
                    1:odict([{'value':True}, {'separationaxis':'auto'}, {'numsubms':'auto'}, {'disableparallel':False}, {'ddistart':-1}, {'taql':''}, {'reindex':True}])}
        a['datacolumn'] = {
                    0:{'value':'corrected'}, 
                    1:odict([{'value':'model'}, {'realmodelcol':False}]), 
                    2:odict([{'value':'all'}, {'realmodelcol':False}]), 
                    3:odict([{'value':'data,model,corrected'}, {'realmodelcol':False}])}
        a['chanaverage'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'chanbin':1}])}
        a['regridms'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'mode':'channel'}, {'nchan':-1}, {'start':0}, {'width':1}, {'nspw':1}, {'interpolation':'linear'}, {'phasecenter':''}, {'restfreq':''}, {'outframe':''}, {'veltype':'radio'}, {'preaverage':False}])}
        a['timeaverage'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'timebin':'0s'}, {'timespan':''}, {'maxuvwdistance':0.0}])}
        a['docallib'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'callib':''}])}
        a['douvcontsub'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'fitspw':''}, {'fitorder':0}, {'want_cont':False}, {'denoising_lib':True}, {'nthreads':1}, {'niter':1}])}
        a['mode'] = {
                    0:odict([{'value':'channel'}, {'nchan':-1}, {'start':0}, {'width':1}, {'interpolation':'linear'}]), 
                    1:odict([{'value':'channel_b'}, {'nchan':-1}, {'start':0}, {'width':1}, {'interpolation':'linear'}]), 
                    2:odict([{'value':'velocity'}, {'nchan':-1}, {'start':''}, {'width':''}, {'interpolation':'linear'}]), 
                    3:odict([{'value':'frequency'}, {'nchan':-1}, {'start':''}, {'width':''}, {'interpolation':'linear'}])}

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
    def description(self, key='mstransform', subkey=None):
        desc={'mstransform': 'Split the MS, combine/separate/regrid spws and do channel and time averaging',
               'vis': 'Name of input Measurement set or Multi-MS.',
               'outputvis': 'Name of output Measurement Set or Multi-MS.',
               'createmms': 'Create a multi-MS output from an input MS.',
               'separationaxis': 'Axis to do parallelization across(scan,spw,auto,baseline).',
               'numsubms': 'The number of Sub-MSs to create (auto or any number)',
               'tileshape': 'List with 1 or 3 elements giving the tile shape of the disk data columns.',
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
               'datacolumn': 'Which data column(s) to process.',
               'realmodelcol': 'Make real a virtual MODEL column.',
               'keepflags': 'Keep *completely flagged rows* or drop them from the output.',
               'usewtspectrum': 'Force creation of the columns WEIGHT_SPECTRUM and SIGMA_SPECTRUM in the output MS, even if not present in the input MS.',
               'combinespws': 'Combine the input spws into a new output spw. Only supported when the number of channels is the same for all the spws.',
               'chanaverage': 'Average data in channels.',
               'chanbin': 'Width (bin) of input channels to average to form an output channel.',
               'hanning': 'Hanning smooth data to remove Gibbs ringing.',
               'regridms': 'Transform channel labels and visibilities to a different spectral reference frame. Notice that u,v,w data is not transformed. ',
               'mode': 'Regridding mode (channel/velocity/frequency/channel_b).',
               'nchan': 'Number of channels in the output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.',
               'start': 'Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.',
               'width': 'Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.',
               'nspw': 'Number of output spws to create in output MS.',
               'interpolation': 'Spectral interpolation method.',
               'phasecenter': 'Phase center direction to be used for the spectral coordinate transformation: direction measure or field index',
               'restfreq': 'Rest frequency to use for output.',
               'outframe': 'Output reference frame (''=keep input frame).',
               'veltype': 'Velocity definition.',
               'preaverage': 'Pre-average channels before regridding, when the ratio between the output and and input widths is greater than 2.',
               'timeaverage': 'Average data in time.',
               'timebin': 'Bin width for time averaging.',
               'timespan': 'Span the timebin across scan, state or both.',
               'maxuvwdistance': 'Maximum separation of start-to-end baselines that can be included in an average. (meters)',
               'docallib': 'Enable on-the-fly (OTF) calibration as in task applycal',
               'callib': 'Path to calibration library file',
               'douvcontsub': 'Enable continuum subtraction as in task uvcontsub',
               'fitspw': 'Spectral window:channel selection for fitting the continuum',
               'fitorder': 'Polynomial order for the fits',
               'want_cont': 'Produce continuum estimate instead of continuum subtracted data',
               'denoising_lib': 'Use new denoising library (based on GSL) instead of casacore fitting routines',
               'nthreads': 'Number of OMP threads to use (currently maximum limited by number of polarizations)',
               'niter': 'Number of iterations for re-weighted linear fit',
               'disableparallel': 'Hidden parameter for internal use only. Do not change it!',
               'ddistart': 'Hidden parameter for internal use only. Do not change it!',
               'taql': 'Table query for nested selections',
               'monolithic_processing': 'Hidden parameter for internal use only. Do not change it!',
               'reindex': 'Hidden parameter for use in the pipeline context only',

              }

#
# Set subfields defaults if needed
#
        if(subkey == 'channel'):
          desc['start'] = 'First input channel to use'
        if(subkey == 'channel_b'):
          desc['start'] = 'First input channel to use'
        if(subkey == 'velocity'):
          desc['start'] = 'Velocity of first channel: e.g \'0.0km/s\''
        if(subkey == 'velocity'):
          desc['width'] = 'Channel width of the output visibilities, in velocity units, e.g \'-1.0km/s\''
        if(subkey == 'frequency'):
          desc['start'] = 'Frequency of first channel: e.q. \'1.4GHz\''
        if(subkey == 'frequency'):
          desc['width'] = 'Channel width of the output visibilities, in frequency units, e.g \'1.0kHz\''

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['outputvis']  = ''
        a['createmms']  = False
        a['separationaxis']  = 'auto'
        a['numsubms']  = 'auto'
        a['tileshape']  = [0]
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
        a['datacolumn']  = 'corrected'
        a['realmodelcol']  = False
        a['keepflags']  = True
        a['usewtspectrum']  = False
        a['combinespws']  = False
        a['chanaverage']  = False
        a['chanbin']  = 1
        a['hanning']  = False
        a['regridms']  = False
        a['mode']  = 'channel'
        a['nchan']  = -1
        a['start']  = 0
        a['width']  = 1
        a['nspw']  = 1
        a['interpolation']  = 'linear'
        a['phasecenter']  = ''
        a['restfreq']  = ''
        a['outframe']  = ''
        a['veltype']  = 'radio'
        a['preaverage']  = False
        a['timeaverage']  = False
        a['timebin']  = '0s'
        a['timespan']  = ''
        a['maxuvwdistance']  = 0.0
        a['docallib']  = False
        a['callib']  = ''
        a['douvcontsub']  = False
        a['fitspw']  = ''
        a['fitorder']  = 0
        a['want_cont']  = False
        a['denoising_lib']  = True
        a['nthreads']  = 1
        a['niter']  = 1
        a['disableparallel']  = False
        a['ddistart']  = -1
        a['taql']  = ''
        a['monolithic_processing']  = False
        a['reindex']  = True

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['createmms']  == False:
            a['separationaxis'] = 'auto'
            a['numsubms'] = 'auto'
            a['disableparallel'] = False
            a['ddistart'] = -1
            a['taql'] = ''
            a['reindex'] = True

        if self.parameters['createmms']  == True:
            a['separationaxis'] = 'auto'
            a['numsubms'] = 'auto'
            a['disableparallel'] = False
            a['ddistart'] = -1
            a['taql'] = ''
            a['reindex'] = True

        if self.parameters['datacolumn']  == 'model':
            a['realmodelcol'] = False

        if self.parameters['datacolumn']  == 'all':
            a['realmodelcol'] = False

        if self.parameters['datacolumn']  == 'data,model,corrected':
            a['realmodelcol'] = False

        if self.parameters['chanaverage']  == True:
            a['chanbin'] = 1

        if self.parameters['regridms']  == True:
            a['mode'] = 'channel'
            a['nchan'] = -1
            a['start'] = 0
            a['width'] = 1
            a['nspw'] = 1
            a['interpolation'] = 'linear'
            a['phasecenter'] = ''
            a['restfreq'] = ''
            a['outframe'] = ''
            a['veltype'] = 'radio'
            a['preaverage'] = False

        if self.parameters['timeaverage']  == True:
            a['timebin'] = '0s'
            a['timespan'] = ''
            a['maxuvwdistance'] = 0.0

        if self.parameters['docallib']  == True:
            a['callib'] = ''

        if self.parameters['douvcontsub']  == True:
            a['fitspw'] = ''
            a['fitorder'] = 0
            a['want_cont'] = False
            a['denoising_lib'] = True
            a['nthreads'] = 1
            a['niter'] = 1

        if self.parameters['mode']  == 'channel':
            a['nchan'] = -1
            a['start'] = 0
            a['width'] = 1
            a['interpolation'] = 'linear'

        if self.parameters['mode']  == 'channel_b':
            a['nchan'] = -1
            a['start'] = 0
            a['width'] = 1
            a['interpolation'] = 'linear'

        if self.parameters['mode']  == 'velocity':
            a['nchan'] = -1
            a['start'] = ''
            a['width'] = ''
            a['interpolation'] = 'linear'

        if self.parameters['mode']  == 'frequency':
            a['nchan'] = -1
            a['start'] = ''
            a['width'] = ''
            a['interpolation'] = 'linear'

        if a.has_key(paramname) :
              return a[paramname]
mstransform_cli = mstransform_cli_()
