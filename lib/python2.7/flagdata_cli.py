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
from task_flagdata import flagdata
class flagdata_cli_:
    __name__ = "flagdata"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (flagdata_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'mode':None, 'autocorr':None, 'inpfile':None, 'reason':None, 'tbuff':None, 'spw':None, 'field':None, 'antenna':None, 'uvrange':None, 'timerange':None, 'correlation':None, 'scan':None, 'intent':None, 'array':None, 'observation':None, 'feed':None, 'clipminmax':None, 'datacolumn':None, 'clipoutside':None, 'channelavg':None, 'chanbin':None, 'timeavg':None, 'timebin':None, 'clipzeros':None, 'quackinterval':None, 'quackmode':None, 'quackincrement':None, 'tolerance':None, 'addantenna':None, 'lowerlimit':None, 'upperlimit':None, 'ntime':None, 'combinescans':None, 'timecutoff':None, 'freqcutoff':None, 'timefit':None, 'freqfit':None, 'maxnpieces':None, 'flagdimension':None, 'usewindowstats':None, 'halfwin':None, 'extendflags':None, 'winsize':None, 'timedev':None, 'freqdev':None, 'timedevscale':None, 'freqdevscale':None, 'spectralmax':None, 'spectralmin':None, 'antint_ref_antenna':None, 'minchanfrac':None, 'verbose':None, 'extendpols':None, 'growtime':None, 'growfreq':None, 'growaround':None, 'flagneartime':None, 'flagnearfreq':None, 'minrel':None, 'maxrel':None, 'minabs':None, 'maxabs':None, 'spwchan':None, 'spwcorr':None, 'basecnt':None, 'fieldcnt':None, 'name':None, 'action':None, 'display':None, 'flagbackup':None, 'savepars':None, 'cmdreason':None, 'outfile':None, 'overwrite':None, 'writeflags':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, mode=None, autocorr=None, inpfile=None, reason=None, tbuff=None, spw=None, field=None, antenna=None, uvrange=None, timerange=None, correlation=None, scan=None, intent=None, array=None, observation=None, feed=None, clipminmax=None, datacolumn=None, clipoutside=None, channelavg=None, chanbin=None, timeavg=None, timebin=None, clipzeros=None, quackinterval=None, quackmode=None, quackincrement=None, tolerance=None, addantenna=None, lowerlimit=None, upperlimit=None, ntime=None, combinescans=None, timecutoff=None, freqcutoff=None, timefit=None, freqfit=None, maxnpieces=None, flagdimension=None, usewindowstats=None, halfwin=None, extendflags=None, winsize=None, timedev=None, freqdev=None, timedevscale=None, freqdevscale=None, spectralmax=None, spectralmin=None, antint_ref_antenna=None, minchanfrac=None, verbose=None, extendpols=None, growtime=None, growfreq=None, growaround=None, flagneartime=None, flagnearfreq=None, minrel=None, maxrel=None, minabs=None, maxabs=None, spwchan=None, spwcorr=None, basecnt=None, fieldcnt=None, name=None, action=None, display=None, flagbackup=None, savepars=None, cmdreason=None, outfile=None, overwrite=None, writeflags=None, ):

        """All-purpose flagging task based on data-selections and flagging modes/algorithms.

        Detailed Description:
        
This task can flag a Measurement Set or a calibration table. It has
two main types of operation. One type will read the parameters from
the interface and flag using any of the various available modes. The
other type will read the commands from a text file, a list of files or
a Python list of strings, containing a list of flag commands.
        
It is also possible to only save the parameters set in the interface
without flagging. The parameters can be saved in the FLAG_CMD
sub-table or in a text file. Note that when saving to an external
file, the parameters will be appended to the given file.

The current flags can be automatically backed up before applying new
flags if the parameter flagbackup is set. Previous flag versions can
be recovered using the flagmanager task.      
      
Flagdata can also flag many types of calibration tables. For detailed
information, see the task pages of flagdata in CASA Docs
(https://casa.nrao.edu/casadocs/)

        Arguments :
                vis: Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'

                   Default Value: 

                mode: Flagging mode
                     Default: 'manual'
                     Options: 'list', 'manual', 'clip', 'quack',
                     'shadow', 'elevation', 'tfcrop', 'rflag',
                     'antint', 'extend', 'unflag', 'summary'


                     * 'list': Flag according to the data selection
                       and flag commands specified in the input
                       list. The input list may come from a text file,
                       a list of text files or from a Python list of
                       strings. Each input line may contain data
                       selection parameters and any parameter
                       specific to the mode given in the line. Default
                       values will be used for the parameters that are
                       not present in the line. Each line will be
                       taken as a command to the task. If data is
                       pre-selected using any of the selection
                       parameters, then flagging will apply only to
                       that subset of the MS.
                                    
                       For optimization and whenever possible, the
                       task will create a union of the data selection
                       parameters present in the list and select only
                       that portion of the MS.

                       NOTE1: the flag commands will be applied only
                       when action='apply'. If action='calculate' the
                       flags will be calculated, but not applied. This
                       is useful if display is set to something other
                       than 'none'. If action='' or 'none', the flag
                       commands will not be applied either. An empty
                       action is useful only to save the parameters of
                       the list to a file or to the FLAG_CMD
                       sub-table.

                       NOTE2: In list mode the parameter
                       quackincrement=True is not supported as part of
                       any quack flag command, unless it is the first
                       command of the list. See more about this in the
                       quack mode section of this help.


                     * 'manual': Flag according to the data selection
                       specified. This is the default mode 


                     * 'clip': Clip data according to values of the
                       following subparameters. The polarization
                       expression is given by the correlation
                       parameter. For calibration tables, the
                       solutions are also given by the correlation
                       parameter.


                     * 'quack': Option to remove specified part of
                       scan beginning/end.


                     * 'shadow': Option to flag data of shadowed
                       antennas. This mode is not available for cal
                       tables.
                 
                       All antennas in the antenna-subtable of the MS
                       (and the corresponding diameters) will be
                       considered for shadow-flag calculations. For a
                       given timestep, an antenna is flagged if any of
                       its baselines (projected onto the uv-plane) is
                       shorter than  radius_1 + radius_2 -
                       tolerance. The value of 'w' is used to
                       determine which antenna is behind the
                       other. The phase-reference center is used for
                       antenna-pointing direction. 


                     * 'elevation': Option to flag based on antenna
                       elevation. This mode is not available for cal
                       tables.


                     * 'tfcrop': Flag using the TFCrop autoflag
                       algorithm.
 
                       For each field, spw, timerange (specified by
                       ntime), and baseline, 
                       (1) Average visibility amplitudes along time
                       dimension to form an average spectrum
                       (2) Calculate a robust piece-wise polynomial
                       fit for the band-shape at the base of RFI
                       spikes. Calculate 'stddev' of (data - fit).
                       (3) Flag points deviating from the fit by more
                       than N-stddev
                       (4) Repeat (1-3) along the other dimension.

                       This algorithm is designed to operate on
                       un-calibrated data (step (2)), as well as
                       calibrated data. It is recommended to extend
                       the flags after running this algorithm. See the
                       sub-parameter extendflags below.


                     * 'rflag': Detect outliers based on the RFlag
                       algorithm (ref. E.Greisen, AIPS, 2011). The
                       polarization expression is given by the
                       correlation parameter.

                       Iterate through the data in chunks of time.
                       For each chunk, calculate local statistics, and
                       apply flags based on user supplied (or
                       auto-calculated) thresholds.

                       Step 1 : Time analysis (for each channel)
                         -- calculate local rms of real and imag
                         visibilities, within a sliding time window
                         -- calculate the median rms across time
                         windows, deviations of local rms from this
                         median, and the median deviation 
                         -- flag if local rms is larger than
                         timedevscale x (medianRMS + medianDev)

                       Step 2 : Spectral analysis (for each time)
                         -- calculate avg of real and imag
                         visibilities and their rms across channels
                         -- calculate the deviation of each channel
                         from this avg, and the median-deviation
                         -- flag if deviation is larger than
                         freqdevscale x medianDev

                       It is recommended to extend the flags after
                       running this algorithm. See the sub-parameter
                       extendflags below.

                       Note that by default the flag implementation in
                       CASA is able to calculate the thresholds and
                       apply them on-the-fly (OTF). There is a
                       significant performancegain with this approach,
                       as the visibilities don't have to be read
                       twice,and therefore is highly
                       recommended. Otherwise it is possible
                       toreproduce the AIPS usage pattern by doing a
                       first run with 'calculate' mode and a second
                       run with 'apply' mode. The advantage of this
                       approach is that the thresholdsare calculated
                       using the data from all scans, instead of
                       calculating them for one scan only.

                       For more information and examples of 'rflag',
                       see the task pages of rflag in CASA Docs
                       (https://casa.nrao.edu/casadocs/)
                       

                     * 'antint': Flag integrations if all baselines to
                       a specified antenna are flagged

                       This mode flag all integrations in which a
                       specified antenna is flagged. This mode
                       operates for an spectral window. It flags any
                       integration in which all baselines to a
                       specified antenna are flagged, but only if this
                       condition is satisfied in a fraction of
                       channels within the spectral window of interest
                       greater than a nominated fraction. For
                       simplicity, it assumes that all polarization
                       products must be unflagged for a baseline to be
                       deemed unflagged. The antint mode implements
                       the flagging approach introduced in
                       'antintflag'
                       (https://doi.org/10.5281/zenodo.163546)

                       The motivating application for introducing this
                       mode is removal of data that will otherwise
                       lead to changes in reference antenna during
                       gain calibration, which will in turn lead to
                       corrupted polarization.


                     * 'extend': Extend and/or grow flags beyond what
                       the basic algorithms detect. This mode will
                       extend the accumulated flags available in the
                       MS, regardless of which algorithm created them.

                       It is recommended that any autoflag (tfcrop,
                       rflag) algorithm be followed up by a flag
                       extension.
                         
                       Extensions will apply only within the selected
                       data, according to the settings of
                       extendpols,growtime,growfreq,growaround,
                       flagneartime,flagnearfreq.
                        
                       Note : Runtime summary counts in the logger can
                       sometimes report larger flag percentages than
                       what is actually flagged. This is because
                       extensions onto already-flagged data-points are
                       counted as new flags. An accurate flag count
                       can be obtained via the summary mode.


                     * 'unflag': Unflag according to the data
                       selection specified.


                     * 'summary': List the number of rows and flagged
                       data points for the MS's meta-data. The
                       resulting summary will be returned as a Python
                       dictionary.
                     

                   Default Value: manual
                   Allowed Values:
                                list
                                manual
                                manualflag
                                clip
                                shadow
                                quack
                                elevation
                                tfcrop
                                rflag
                                antint
                                extend
                                summary
                                unflag

                autocorr: Flag only the auto-correlations?
                     Subparameter of mode='manual'
                     Default: False
                     Options: False|True

                     NOTE: this parameter is only active when set to
                     True. If set to False it does NOT mean "do not
                     flag auto-correlations". When set to True, it
                     will only flag data from a processor of type
                     CORRELATOR. 

                   Default Value: False

                inpfile: Input ASCII file, list of files or Python list of strings
with flag commands.
                     Subparameter of mode='list'
                     Default: ''
                     Options: [] with flag commands or 
                              [] with filenames or 
                              '' with a filename.

                     The parser will be strict and accept only valid
                     flagdata parameters in the list. The parser
                     evaluates the commands in the list and considers
                     only existing Python types.It will check each
                     parameter name and type and exit with an error if
                     any of them is wrong. 

                     NOTE: There should be no whitespace between
                     KEY=VALUE since the parser first breaks command
                     lines on whitespace, then on "=". Use only one
                     whitespace to separate the parameters (no
                     commas).

                   Default Value: 

                reason: Select flag commands based on REASON(s)
                     Subparameter of mode='list'
                     Default: 'any' (all flags regardless of reason)
                     Can be a string, or list of strings

                        Examples: 
                        reason='FOCUS_ERROR'
                        reason=['FOCUS_ERROR','SUBREFLECTOR_ERROR']

                     If inpfile is a list of files, the reasons given
                     in this parameter will apply to all the files.

                     NOTE: what is within the string is literally
                     matched, e.g. reason='' matches only blank
                     reasons, and reason =
                     'FOCUS_ERROR,SUBREFLECTOR_ERROR' matches this
                     compound reason string only.

                   Default Value: any

                tbuff: A time buffer or list of time buffers to pad the
timerange parameters in flag commands.
                     Subparameter of mode='list'
                     Default: 0.0 (it will not apply any time padding)

                     When a list of 2 time buffers is given, it will
                     subtract the first value from the lower time and
                     the second value will be added to the upper time
                     in the range. The 2 time buffer values can be
                     different, allowing to have an irregular time
                     buffer padding to time ranges. If the list
                     contains only one time buffer, it will use it to
                     subtract from t0 and add to t1. If more than one
                     list of input files is given, tbuff will apply to
                     all of the flag commands that have timerange
                     parameters in the files. Each tbuff value should
                     be a Float number given in seconds.

                        Examples:
                        tbuff=[0.5, 0.8]                   
                        inpfile=['online.txt','userflags.txt']

                        The timeranges in the online.txt file are
                        first converted to seconds. Then, 0.5 is
                        subtracted from t0 and 0.8 is added to t1,
                        where t0 and t1 are the two intervals given in
                        timerange. Similarly, tbuff will be applied to
                        any timerange in userflags.txt. 

                     IMPORTANT: This parameter assumes that timerange
                     = t0 ~ t1, therefore it will not work if only t0
                     or t1 is given.

                     NOTE: The most common use-case for tbuff is to
                     apply the online flags that are created by
                     importasdm when savecmds=True. The value of a
                     regular time buffer should be
                     tbuff=0.5*max(integration time).

                   Default Value: 0.0

                spw: Select spectral window/channels
                     Default: '' (all spectral windows and channels)

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

                     NOTE: For modes clip, tfcrop and rflag,
                     channel-ranges can be excluded from flagging by
                     leaving them out of the selection range. This is
                     a way to protect known spectral-lines from being
                     flagged by the autoflag algorithms. For example,
                     if spectral-lines fall in channels 6~9, set the
                     selection range to spw='0:0~5;10~63'.

                   Default Value: 

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

                     NOTE: for some antenna-based calibration tables,
                     selecting baselines with the & syntax do not
                     apply.

                   Default Value: 

                uvrange: Select data by baseline length.
                     Default = '' (all)

                        Examples:
                        uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                        uvrange='>4klambda';uvranges greater than 4 kilo-lambda
                        uvrange='0~1000km'; uvrange in kilometers

                     NOTE: uvrange selection is not supported for cal tables.  

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

                correlation: Select data based on correlation
                     Default: '' ==> all
                     Options: Any of 'ABS', 'ARG', 'REAL', 'IMAG',
                     'NORM' followed by any of 'ALL', 'I', 'XX', 'YY',
                     'RR', 'LL', 'WVR' ('WVR' = water vapour
                     radiometer of ALMA data).

                        Example: correlation="XX,YY".

                     For modes clip, tfcrop or rflag, the default
                     means ABS_ALL. If the input is cal table that
                     does not contain a complex data column, the
                     default will fall back to REAL_ALL.
                     For calibration tables, the solutions are:
                     'Sol1', 'Sol2', Sol3, Sol4.

                     NOTE: correlation selection is not supported for
                     modes other than clip, tfcrop or rflag in cal
                     tables.   

                   Default Value: 

                scan: Scan number range
                     Subparameter of selectdata=True
                     Default: '' = all

                   Default Value: 

                intent: Select observing intent
                     Default: '' (no selection by intent)

                        Example: intent='*BANDPASS*'  (selects data
                        labelled with BANDPASS intent)

                     NOTE: intent selection is not supported for cal
                     tables.

                   Default Value: 

                array: Selection based on the antenna array
                     Default: '' (all)

                     NOTE: array selection is not supported for cal
                     tables.

                   Default Value: 

                observation: Select by observation ID(s)
                     Subparameter of selectdata=True
                     Default: '' = all

                         Example: observation='0~2,4'

                   Default Value: 

                feed: Selection based on the feed: Not yet implemented

                   Default Value: 

                clipminmax: Range to use for clipping
                     Subparameter of mode='clip'
                     Default: [] (it will flag only NaN and Infs)

                     It will always flag the NaN/Inf data, even when a range is specified. 

                        Example: [0.0,1.5]

                   Default Value: 

                datacolumn: Data column to image (data or observed, corrected)
                     Subparameter of mode='clip|tfcrop|rflag'
                     Default:'corrected'
                     Options: data, corrected, model, weight, etc.
                     
                     If 'corrected' does not exist, it will use 'data'
                     instead

                   Default Value: DATA

                clipoutside: Clip outside the range?
                     Subparameter of mode='clip'
                     Default: True
                     Options: True|False

                   Default Value: True

                channelavg: Pre-average data across channels before analyzing
visibilities for flagging
                     Subparameter of mode='clip|tfcrop|rflag'
                     Default: False
                     Options: False|True

                     Pre-average data across channels before analyzing
                     visibilities for flagging. Partially flagged data
                     is  not be included in the average unless all
                     data contributing to a given output channel is
                     flagged. If present, WEIGHT_SPECTRUM /
                     SIGMA_SPECTRUM are used to compute a weighted
                     average (WEIGHT_SPECTRUM for CORRECTED_DATA and
                     SIGMA_SPECTRUM for DATA).

                     NOTE 1: Pre-average across channels is not
                     supported in list mode.

                     NOTE 2: Pre-average across channels is not
                     supported for calibration tables 

                   Default Value: False

                chanbin: Bin width for channel average in number of input channels
                     Subparameter of mode='clip|tfcrop|rflag'
                     Default: 1

                     Bin width for channel average in number of input
                     channels. If a list is given, each bin applies to
                     one of the selected SPWs. When chanbin is set to
                     1 all input channels are used considered for the
                     average to produce a single output channel, this
                     behaviour aims to be preserve backwards
                     compatibility with the previous pre-averaging
                     feature of clip mode.

                   Default Value: 1

                timeavg: Pre-average data across time before analyzing
visibilities for flagging.
                     Subparameter of mode='clip|tfcrop|rflag'
                     Default: False
                     Options: False|True

                     Pre-average data across time before analyzing
                     visibilities for flagging. Partially flagged data
                     is  not be included in the average unless all
                     data contributing to a given output channel is
                     flagged. If present, WEIGHT_SPECTRUM /
                     SIGMA_SPECTRUM are used to compute a weighted
                     average (WEIGHT_SPECTRUM for  CORRECTED_DATA and
                     SIGMA_SPECTRUM for DATA). Otherwise WEIGHT/SIGMA
                     are used to average together data from different
                     integrations.

                     NOTE 1: Pre-average across time is not
                     supported in list mode.

                     NOTE 2: Pre-average across time is not
                     supported for calibration tables 

                   Default Value: False

                timebin: Bin width for time average in seconds
                     Subparameter of mode='clip|tfcrop|rflag'
                     Default: '0s'

                   Default Value: 0s

                clipzeros: Clip zero-value data
                     Subparameter of mode='clip'
                     Default: False
                     Options: False|True

                   Default Value: False

                quackinterval: Time in seconds from scan beginning or end to flag.
                     Subparameter of mode='quack'
                     Default: 0.0

                     Note: Make time slightly smaller than the desired
                     time.

                   Default Value: 1.0

                quackmode: Quack mode. beg: first n seconds of scan; endb: last n
seconds of scan; end: all but first n seconds of scan; tail: all but
last n seconds of scan.
                     Subparameter of mode='quack'
                     Default: 'beg'
                     Options: 
                   * 'beg': flag an interval at the beginning of scan
                   * 'endb': flag an interval at the end of scan 
                   * 'tail': flag all but an interval at the beginning
                             of scan
                   * 'end': flag all but an interval at end of scan

                     Visual representation of quack mode flagging one
                     scan with 1s duration. The following diagram
                     shows what is flagged for each quack mode when
                     quackinterval is set to 0.25s. The flagged part
                     is represented by crosses (+++++++++)

                                 scan with 1s duration
                     --------------------------------------------
                     beg
                     +++++++++++---------------------------------
                                                      endb
                     ---------------------------------+++++++++++
                                tail
                     -----------+++++++++++++++++++++++++++++++++
                     end
                     +++++++++++++++++++++++++++++++++-----------

                   Default Value: beg

                quackincrement: Increment quack flagging in time taking into account
flagged data or not.
                     Subparameter of mode='quack'
                     Default: False
                     Options: False|True

                     False: the quack interval is counted from the
                     scan boundaries, as determined by the quackmode
                     parameter, regardless of if data has been flagged
                     or not.
                     True: the quack interval is counted from the
                     first unflagged data in the scan.

                     NOTE: on adding quack to a command in 'list'
                     mode: quackincrement = True works based on the
                     state of prior flagging, and unless it is the
                     first item in the list the agent doing the
                     quacking in list mode doesn't know about the
                     state of prior flags. In this case, the command
                     with quackincrement=True will be ignored and the
                     task will issue a WARNING.

                   Default Value: False

                tolerance: Amount of shadowing allowed (or tolerated), in meters. 
                     Subparameter of mode='shadow'
                     Default: 0.0

                     A positive number allows antennas to overlap in
                     projection. A negative number forces antennas
                     apart in projection. Zero implies a distance of
                     radius_1+radius_2 between antenna centers.

                   Default Value: 0.0

                addantenna: File name or dictionary with additional antenna names,
positions and diameters
                     Subparameter of mode='shadow'
                     Default: ''

                     It can be either a file name with additional
                     antenna names, positions and diameters, or a
                     Python dictionary with the same information. You
                     can use the flaghelper functions to create the
                     dictionary from a file. 

                     To create a dictionary inside casapy.
                     > import flaghelper as fh
                     > antdic = fh.readAntennaList(antfile)
                   
                     Where antfile is a text file in disk that
                     contains information such as:
                     name=VLA01
                     diameter=25.0
                     position=[-1601144.96146691, -5041998.01971858,
                     3554864.76811967]
                     name=VLA02
                     diameter=25.0
                     position=[-1601105.7664601889,
                     -5042022.3917835914, 3554847.245159178]

                   Default Value: 

                lowerlimit: Lower limiting elevation (in degrees)
                     Subparameter of mode='elevation'
                     Default: 0.0

                     Lower limiting elevation in degrees. Data coming
                     from a baseline where one or both antennas were
                     pointing at a strictly lower elevation (as
                     function of time), will be flagged.

                   Default Value: 0.0

                upperlimit: Upper limiting elevation (in degrees)
                     Subparameter of mode='elevation'
                     Default: 90.0

                     Upper limiting elevation in degrees. Data coming
                     from a baseline where one or both antennas were
                     pointing at a strictly higher elevation (as
                     function of time), will be flagged.

                   Default Value: 90.0

                ntime: Timerange (in seconds or minutes) over which to buffer
data before running the algorithm. 
                     Subparameter of mode='tfcrop|rflag|extend'
                     Default: 'scan'
                     Options: 'scan' or any other float value or
                     string containing the units.

                     The dataset will be iterated through in
                     time-chunks defined here.

                        Example: ntime='1.5min'; 1.2 (taken in
                        seconds)

                     WARNING: if ntime='scan' and combinescans=True,
                     all the scans will be loaded at once, thus
                     requesting a lot of memory depending on the
                     available spws.

                   Default Value: scan

                combinescans: Accumulate data across scans depending on the value of
ntime.
                     Subparameter of mode='tfcrop|rflag|extend'
                     Default: False
                     Options: False|True

                     This parameter should be set to True only when
                     ntime is specified as a time-interval (not
                     'scan'). When set to True, it will remove SCAN
                     from the sorting columns, therefore it will only
                     accumulate across scans if ntime is not set to
                     'scan'.

                   Default Value: False

                timecutoff: Flagging thresholds in units of deviation from the fit
                     Subparameter of mode='tfcrop'
                     Default: 4.0

                     Flag all data-points further than N-stddev from
                     the fit. This threshold catches time-varying RFI
                     spikes (narrow and broad-band), but will not
                     catch RFI that is persistent in time.

                     Flagging is done in upto 5 iterations. The stddev
                     calculation is adaptive and converges to a value
                     that reflects only the data and no RFI. At each
                     iteration, the same relative threshold is applied
                     to detect flags. (Step (3) of the algorithm).

                   Default Value: 4.0

                freqcutoff: Flag threshold in frequency.
                     Subparameter of mode='tfcrop'
                     Default: 3.0

                     Flag all data-points further than N-stddev from
                     the fit. Same as timecutoff, but along the
                     frequency-dimension. This threshold catches
                     narrow-band RFI that may or may not be persistent
                     in time. 

                   Default Value: 3.0

                timefit: Fitting function for the time direction (poly/line)
                     Subparameter of mode='tfcrop'
                     Default: 'line'
                     Options: line|poly

                     'line': fit is a robust straight-line fit across
                     the entire timerange (defined by 'ntime').
                     'poly': fit is a robust piece-wise polynomial fit
                     across the timerange.

                     NOTE: A robust fit is computed in upto 5
                     iterations. At each iteration, the stddev between
                     the data and the fit is computed, values beyond
                     N-stddev are flagged, and the fit and stddev are
                     re-calculated with the remaining points. This
                     stddev calculation is adaptive, and converges to
                     a value that reflects only the data and no RFI.
                     It also provides a varying set of flagging
                     thresholds, that allows deep flagging only when
                     the fit best represents the true data.

                     Choose 'poly' only if the visibilities are
                     expected to vary significantly over the timerange
                     selected by 'ntime', or if there is a lot of
                     strong but intermittent RFI.

                   Default Value: line

                freqfit: Fitting function for the frequency direction (poly/line)
                     Subparameter of mode='tfcrop'
                     Default: 'poly'
                     Options: line|poly

                     Same as for the 'timefit' parameter.

                     Choose 'line' only if you are operating on
                     bandpass-corrected data, or residuals,and expect
                     that the bandshape is linear. The 'poly' option
                     works better on uncalibrated bandpasses with
                     narrow-band RFI spikes.

                   Default Value: poly

                maxnpieces: Number of pieces in the polynomial-fits (for "freqfit" or
"timefit" = "poly")
                     Subparameter of mode='tfcrop'
                     Default: 7
                     Options: 1-9

                     This parameter is used only if 'timefit' or
                     'freqfit' are chosen as 'poly'. If there is
                     significant broad-band RFI, reduce this
                     number. Using too many pieces could result in the
                     RFI being fitted in the 'clean' bandpass. In
                     later stages of the fit, a third-order polynomial
                     is fit per piece, so for best results, please
                     ensure that nchan/maxnpieces is at-least 10.

                   Default Value: 7

                flagdimension: Choose the directions along which to perform flagging
                     Subparameter of mode='tfcrop'
                     Default: 'freqtime' (first flag along frequency,
                     and then along time) 
                     Options: 'time', 'freq', 'timefreq', 'freqtime'

                     For most cases, 'freqtime' or 'timefreq' are
                     appropriate, and differences between these
                     choices are apparant only if RFI in one dimension
                     is significantly stronger than the other. The
                     goal is to flag the dominant RFI first.
                     If there are very few (less than 5) channels of
                     data, then choose 'time'. Similarly for 'freq'.

                   Default Value: freqtime

                usewindowstats: Use sliding-window statistics to find additional flags.
                     Subparameter of mode='tfcrop'
                     Default: 'none' 
                     Options: 'none', 'sum', 'std', 'both'   

                     NOTE: This is experimental!
                     The 'sum' option chooses to flag a point, if the
                     mean-value in a window centered on that point
                     deviates from the fit by more than N-stddev/2.0. 

                     NOTE: stddev is calculated between the data and
                     fit as explained in Step (2). This option is an
                     attempt to catch broad-band or time-persistent
                     RFI  that the above polynomial fits will
                     mistakenly fit as the clean band. It is an
                     approximation to the sumThreshold method found to
                     be effective by Offringa et.al (2010) for LOFAR
                     data. The 'std' option chooses to flag a point,
                     if the 'local' stddev calculated in a window
                     centered on that point is larger than
                     N-stddev/2.0. This option is an attempt to catch
                     noisy RFI that is not excluded in the polynomial
                     fits, and which increases the global stddev, and
                     results in fewer flags (based on the N-stddev
                     threshold).

                   Default Value: none

                halfwin: Half-width of sliding window to use with "usewindowstats"
(1,2,3).
                     Subparameter of mode='tfcrop'
                     Default: 1  (a 3-point window size)
                     Options: 1, 2, 3

                     NOTE: This is experimental!

                   Default Value: 1

                extendflags: Extend flags along time, frequency and correlation.
                     Subparameter of mode='tfcrop|rflag'
                     Default: True
                     Options: True|False

                     NOTE: It is usually helpful to extend the flags
                     along time, frequency, and correlation using this
                     parameter, which will run the "extend" mode after
                     "tfcrop" and extend the flags if more than 50% of
                     the timeranges are already flagged, and if more
                     than 80% of the channels are already flagged. It
                     will also extend the flags to the other
                     polarizations. The user may also set extendflags
                     to False and run the "extend" mode in a second
                     step within the same flagging run:

                        Example: cmd=["mode='tfcrop' freqcutoff=3.0
                        usewindowstats='sum' extendflags=False",
                        "mode='extend' extendpols=True growtime=50.0
                        growaround=True"]
                        flagdata(vis, mode='list', inpfile=cmd)   

                   Default Value: True

                winsize: Number of timesteps in the sliding time window ( fparm(1)
in AIPS )
                     Subparameter of mode='rflag'
                     Default: 3

                   Default Value: 3

                timedev: Time-series noise estimate ( noise in AIPS )
                     Subparameter of mode='rflag'
                     Default: []

                        Examples: 
                        timedev = 0.5 : Use this noise-estimate to
                        calculate flags. Do not recalculate.
                        timedev = [ [1,9,0.2], [1,10,0.5] ] :  Use
                        noise-estimate of 0.2 for field 1, spw 9, and
                        noise-estimate of 0.5 for field 1, spw 10.
                        timedev = [] : Auto-calculate noise
                        estimates. 
                        'tdevfile.txt' : Auto-calculate noise
                        estimates and write them into a file with the
                        name given (any string will be interpreted as
                        a file name which will be checked for
                        existence).

                   Default Value: 

                freqdev: Spectral noise estimate ( scutoff in AIPS )
                     Subparameter of mode='rflag'
                     Default: []

                     This step depends on having a relatively-flat
                     bandshape. Same parameter-options as 'timedev'.

                   Default Value: 

                timedevscale: Threshold scaling for timedev( fparm(9) in AIPS ).
                     For Step 1 (time analysis), flag a point if local
                     rms around it is larger than 'timedevscale' x
                     'timedev' (fparm(0) in AIPS)
                     Subparameter of mode='rflag'
                     Default: 5.0

                     This scale parameter is only applied when
                     flagging (action='apply') and displaying reports
                     (display option). It is not used when the
                     thresholds are simply calculated and saved into
                     files (action='calculate', as in the two-passes
                     usage pattern of AIPS)

                   Default Value: 5.0

                freqdevscale: Threshold scaling for freqdev (fparm(10) in AIPS ). 
                     For Step 2 (spectral analysis), flag a point if
                     local rms around it is larger than 'freqdevscale'
                     x 'freqdev' (fparm(10) in AIPS)
                     Subparameter of mode='rflag'
                     Default: 5.0

                     Similarly as with timedevscale, freqdevscale is
                     used when applying flags and displaying
                     reports. It is not used when the thresholds are
                     simply calculated and saved into files
                     (action='calculate', as in the two-passes usage
                     pattern of AIPS)

                   Default Value: 5.0

                spectralmax: Flag whole spectrum if 'freqdev' is greater than
spectralmax ( fparm(6) in AIPS )
                     Subparameter of mode='rflag'
                     Default: 1E6

                   Default Value: 1E6

                spectralmin: Flag whole spectrum if 'freqdev' is less than spectralmin
( fparm(5) in AIPS )
                     Subparameter of mode='rflag'
                     Default: 0.0

                   Default Value: 0.0

                antint_ref_antenna: Antenna of interest. Baselines with this antenna will be
checked for flagged channels.
                     Subparameter of mode='antint'

                     Note that this is not the same as the general
                     'antenna' parameter of flagdata. The parameter
                     antint_ref_antenna is mandatory with the 'antint'
                     mode and chooses the antenna for which the
                     fraction of channels flagged will be checked.

                   Default Value: 

                minchanfrac: Minimum fraction of flagged channels required for a
baseline to be deemed as flagged
                     Subparameter of mode='antint'
                     Takes values between 0-1 (float).

                     In this mode flagdata does the following for
                     every point in time. It checks the fraction of
                     channels flagged for any of the polarization
                     products and for every baseline to the antenna of
                     interest. If the fraction is higher than this
                     'minchanfrac' threshold then the data are flagged
                     for this pont in time (this includes all the rows
                     selected with the flagdata command that have that
                     timestamp).
                     This parameter will be ignored if spw specifies a
                     channel.

                   Default Value: 0.6

                verbose: Print timestamps of flagged integrations to the log
                     Subparameter of mode='antint'

                        Examples: 
                        flagdata(vis, ..., spw='9',
                        antint_ref_antenna='ea01')
                        flagdata(vis, ..., spw='9',
                        antint_ref_antenna='ea01', minchanfrac=0.3,
                        verbose=True) ==> reduce the fraction of
                        channels that are required to be flagged, and
                        print information for every integration that
                        is flagged.

                   Default Value: False

                extendpols: Extend flags to all selected correlations
                     Subparameter of mode='extend'
                     Default: True
                     Options: True|False

                        For example, to extend flags from RR to only
                        RL and LR, a data-selection of
                        correlation='RR,LR,RL' is required along with
                        extendpols=True. 

                   Default Value: True

                growtime: For any channel, flag the entire timerange in the current
2D chunk (set by 'ntime') if more than X% of the timerange is already
flagged.
                     Subparameter of mode='extend'
                     Default: 50.0
                     Options:  0.0 - 100.0

                     This option catches the low-intensity parts of
                     time-persistent RFI.

                   Default Value: 50.0

                growfreq: For any timestep, flag all channels in the current 2D
chunk (set by  data-selection) if more than X% of the channels are
already flagged.
                     Subparameter of mode='extend'
                     Default: 50.0
                     Options:  0.0 - 100.0

                     This option catches broad-band RFI that is
                     partially identified by earlier steps.

                   Default Value: 50.0

                growaround: Flag a point based on the number of flagged points around it.
                     Subparameter of mode='extend'
                     Default: False
                     Options: False|True

                     For every un-flagged point on the 2D time/freq
                     plane, if more than four surrounding points are
                     already flagged, flag that point. This option
                     catches some wings of strong RFI spikes.

                   Default Value: False

                flagneartime: Flag points before and after every flagged one, in the
time-direction.
                     Subparameter of mode='extend'
                     Default: False
                     Options: False|True

                     NOTE: This can result in excessive flagging.

                   Default Value: False

                flagnearfreq: Flag points before and after every flagged one, in the
frequency-direction
                     Subparameter of mode='extend'
                     Default: False
                     Options: False|True

                     NOTE:  This can result in excessive flagging

                   Default Value: False

                minrel: Minimum number of flags (relative) to include in
histogram
                     Subparameter of mode='summary'
                     Default: 0.0

                   Default Value: 0.0

                maxrel: Maximum number of flags (relative) to include in
histogram
                     Subparameter of mode='summary'
                     Default: 1.0

                   Default Value: 1.0

                minabs: Minimum number of flags (absolute, inclusive) to include
in histogram
                     Subparameter of mode='summary'
                     Default: 0

                   Default Value: 0

                maxabs: Maximum number of flags (absolute, inclusive) to include
in histogram
                     Subparameter of mode='summary'
                     Default: -1

                     To indicate infinity, use any negative number.

                   Default Value: -1

                spwchan: List the number of flags per spw and per channel.
                     Subparameter of mode='summary'
                     Default: False
                     Options: False|True

                   Default Value: False

                spwcorr: List the number of flags per spw and per correlation.
                     Subparameter of mode='summary'
                     Default: False
                     Options: False|True

                   Default Value: False

                basecnt: List the number of flags per baseline
                     Subparameter of mode='summary'
                     Default: False
                     Options: False|True

                   Default Value: False

                fieldcnt: Produce a separated breakdown per field
                     Subparameter of mode='summary'
                     Default: False
                     Options: False|True

                   Default Value: False

                name: Name for this summary, to be used as a key in the
returned Python dictionary
                     Subparameter of mode='summary'
                     Default: 'Summary'

                     It is possible to call the summary mode multiple
                     times in list mode. When calling the summary mode
                     as a command in a list, one can give different
                     names to each one of them so that they can be
                     easily pulled out of the summary's dictionary.

                    In summary mode, the task returns a dictionary of flagging statistics.
        
                    Example 1:
                    s = flagdata(..., mode='summary')
                    Then s will be a dictionary which contains
                    s['total']   : total number of data
                    s['flagged'] : amount of flagged data

                    Example 2: 
                    Two summary commands in list mode, intercalating a
                    manual flagging command.
                    s = flagdata(..., mode='list',
                    inpfile=["mode='summary' name='InitFlags'",
                    "mode='manual' autocorr=True", "mode='summary'
                    name='Autocorr'"])

                    The dictionary returned in 's' will contain two
                    dictionaries, one for each of the two summary
                    modes. 
                    s['report0']['name'] : 'InitFlags'
                    s['report1']['name'] : 'Autocorr'

                   Default Value: Summary

                action: Action to perform in MS/cal table or in the input list of
parameters.
                     Default: 'apply'
                     Options:  'none', 'apply','calculate'

                     * 'apply': Apply the flags to the MS.
                     * 'calculate': Only calculate the flags but do
                       not write them to the MS. This is useful if
                       used together with the display to analyse the
                       results before writing to the MS.
                     * '': When set to empty, the underlying tool will
                       not be executed and no flags will be
                       produced. No data selection will be done
                       either. This is useful when used together with
                       the parameter savepars to only save the current
                       parameters (or list of parameters) to the
                       FLAG_CMD sub-table or to an external file.

                   Default Value: apply
                   Allowed Values:
                                apply
                                calculate
                                none
                                

                display: Display data and/or end-of-MS reports at runtime.
                     Subparameter of action='apply|calculate'
                     Default: 'none'
                     Options: 'none', 'data', 'report', 'both'

                     * 'none': will not display anything.
                     * 'data': display data and flags per-chunk at
                       run-time, within an interactive GUI.
                       This option opens a GUI to show the 2D
                       time-freq planes of the data with old and new
                       flags, for all correlations per baseline.
                       -- The GUI allows stepping through all
                       baselines (prev/next) in the current chunk (set
                       by 'ntime'), and stepping to the next-chunk.
                       -- The 'flagdata' task can be quit from the
                       GUI, in case it becomes obvious that the
                       current set of parameters is just wrong.
                       -- There is an option to stop the display but
                       continue flagging.
                     * 'report': displays end-of-MS reports on the
                       screen.
                     * 'both': displays data per chunk and end-of-MS
                       reports on the screen

                   Default Value: 

                flagbackup: Automatically backup flags before the run?
                     Default: True
                     Options: True|False

                     Flagversion names are chosen automatically, and
                     are based on the mode being used.

                   Default Value: True

                savepars: Save the current parameters to the FLAG_CMD table of the
MS or to an output text file?
                     Default: False
                     Options: False|True

                     Note that when display is set to anything other
                     than 'none', savepars will be disabled. This is
                     done because in an interactive mode, the user may
                     skip data which may invalidate the initial input
                     parameters and there is no way to save the
                     interactive commands. When the input is a
                     calibration table it is only possible to save the
                     parameters to a file.

                   Default Value: False

                cmdreason: A string containing a reason to save to the FLAG_CMD
table or to an output text file given by the outfile sub-parameter.
                     Subparameter of savepars=True
                     Default: '' (no reason will be added to output)

                     If the input  contains any reason, they will be
                     replaced with this one. At the moment it is not
                     possible to add more than one reason. 

                        Example: cmdreason='CLIP_ZEROS'

                   Default Value: 

                outfile: Name of output file to save current parameters. If empty,
save to FLAG_CMD
                     Subparameter of savepars=True
                     Default: '' (save the parameters to the FLAG_CMD
                     table of the MS)

                        Example: outfile='flags.txt' will save the
                        parameters in a text file.

                   Default Value: 

                overwrite: Overwrite the existing file given in 'outfile'
                     Default: True
                     Options: True|False

                     The default True will remove the existing file
                     given in 'outfile' and save the current flag
                     commands to a new file with the same name. When
                     set to False, the task will exit with an error
                     message if the file exist.

                   Default Value: True

        Returns: void

        Example :


FOR MORE INFORMATION, SEE THE TASK PAGES OF FLAGDATA IN CASA DOCS:
https://casa.nrao.edu/casadocs/


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'flagdata'
        self.__globals__['taskname'] = 'flagdata'
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
            myparams['mode'] = mode = self.parameters['mode']
            myparams['autocorr'] = autocorr = self.parameters['autocorr']
            myparams['inpfile'] = inpfile = self.parameters['inpfile']
            myparams['reason'] = reason = self.parameters['reason']
            myparams['tbuff'] = tbuff = self.parameters['tbuff']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['field'] = field = self.parameters['field']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['correlation'] = correlation = self.parameters['correlation']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['array'] = array = self.parameters['array']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['feed'] = feed = self.parameters['feed']
            myparams['clipminmax'] = clipminmax = self.parameters['clipminmax']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']
            myparams['clipoutside'] = clipoutside = self.parameters['clipoutside']
            myparams['channelavg'] = channelavg = self.parameters['channelavg']
            myparams['chanbin'] = chanbin = self.parameters['chanbin']
            myparams['timeavg'] = timeavg = self.parameters['timeavg']
            myparams['timebin'] = timebin = self.parameters['timebin']
            myparams['clipzeros'] = clipzeros = self.parameters['clipzeros']
            myparams['quackinterval'] = quackinterval = self.parameters['quackinterval']
            myparams['quackmode'] = quackmode = self.parameters['quackmode']
            myparams['quackincrement'] = quackincrement = self.parameters['quackincrement']
            myparams['tolerance'] = tolerance = self.parameters['tolerance']
            myparams['addantenna'] = addantenna = self.parameters['addantenna']
            myparams['lowerlimit'] = lowerlimit = self.parameters['lowerlimit']
            myparams['upperlimit'] = upperlimit = self.parameters['upperlimit']
            myparams['ntime'] = ntime = self.parameters['ntime']
            myparams['combinescans'] = combinescans = self.parameters['combinescans']
            myparams['timecutoff'] = timecutoff = self.parameters['timecutoff']
            myparams['freqcutoff'] = freqcutoff = self.parameters['freqcutoff']
            myparams['timefit'] = timefit = self.parameters['timefit']
            myparams['freqfit'] = freqfit = self.parameters['freqfit']
            myparams['maxnpieces'] = maxnpieces = self.parameters['maxnpieces']
            myparams['flagdimension'] = flagdimension = self.parameters['flagdimension']
            myparams['usewindowstats'] = usewindowstats = self.parameters['usewindowstats']
            myparams['halfwin'] = halfwin = self.parameters['halfwin']
            myparams['extendflags'] = extendflags = self.parameters['extendflags']
            myparams['winsize'] = winsize = self.parameters['winsize']
            myparams['timedev'] = timedev = self.parameters['timedev']
            myparams['freqdev'] = freqdev = self.parameters['freqdev']
            myparams['timedevscale'] = timedevscale = self.parameters['timedevscale']
            myparams['freqdevscale'] = freqdevscale = self.parameters['freqdevscale']
            myparams['spectralmax'] = spectralmax = self.parameters['spectralmax']
            myparams['spectralmin'] = spectralmin = self.parameters['spectralmin']
            myparams['antint_ref_antenna'] = antint_ref_antenna = self.parameters['antint_ref_antenna']
            myparams['minchanfrac'] = minchanfrac = self.parameters['minchanfrac']
            myparams['verbose'] = verbose = self.parameters['verbose']
            myparams['extendpols'] = extendpols = self.parameters['extendpols']
            myparams['growtime'] = growtime = self.parameters['growtime']
            myparams['growfreq'] = growfreq = self.parameters['growfreq']
            myparams['growaround'] = growaround = self.parameters['growaround']
            myparams['flagneartime'] = flagneartime = self.parameters['flagneartime']
            myparams['flagnearfreq'] = flagnearfreq = self.parameters['flagnearfreq']
            myparams['minrel'] = minrel = self.parameters['minrel']
            myparams['maxrel'] = maxrel = self.parameters['maxrel']
            myparams['minabs'] = minabs = self.parameters['minabs']
            myparams['maxabs'] = maxabs = self.parameters['maxabs']
            myparams['spwchan'] = spwchan = self.parameters['spwchan']
            myparams['spwcorr'] = spwcorr = self.parameters['spwcorr']
            myparams['basecnt'] = basecnt = self.parameters['basecnt']
            myparams['fieldcnt'] = fieldcnt = self.parameters['fieldcnt']
            myparams['name'] = name = self.parameters['name']
            myparams['action'] = action = self.parameters['action']
            myparams['display'] = display = self.parameters['display']
            myparams['flagbackup'] = flagbackup = self.parameters['flagbackup']
            myparams['savepars'] = savepars = self.parameters['savepars']
            myparams['cmdreason'] = cmdreason = self.parameters['cmdreason']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['writeflags'] = writeflags = self.parameters['writeflags']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['mode'] = mode
        mytmp['autocorr'] = autocorr
        mytmp['inpfile'] = inpfile
        mytmp['reason'] = reason
        mytmp['tbuff'] = tbuff
        mytmp['spw'] = spw
        mytmp['field'] = field
        mytmp['antenna'] = antenna
        mytmp['uvrange'] = uvrange
        mytmp['timerange'] = timerange
        mytmp['correlation'] = correlation
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['array'] = array
        mytmp['observation'] = observation
        mytmp['feed'] = feed
        mytmp['clipminmax'] = clipminmax
        mytmp['datacolumn'] = datacolumn
        mytmp['clipoutside'] = clipoutside
        mytmp['channelavg'] = channelavg
        mytmp['chanbin'] = chanbin
        mytmp['timeavg'] = timeavg
        mytmp['timebin'] = timebin
        mytmp['clipzeros'] = clipzeros
        mytmp['quackinterval'] = quackinterval
        mytmp['quackmode'] = quackmode
        mytmp['quackincrement'] = quackincrement
        mytmp['tolerance'] = tolerance
        mytmp['addantenna'] = addantenna
        mytmp['lowerlimit'] = lowerlimit
        mytmp['upperlimit'] = upperlimit
        mytmp['ntime'] = ntime
        mytmp['combinescans'] = combinescans
        mytmp['timecutoff'] = timecutoff
        mytmp['freqcutoff'] = freqcutoff
        mytmp['timefit'] = timefit
        mytmp['freqfit'] = freqfit
        mytmp['maxnpieces'] = maxnpieces
        mytmp['flagdimension'] = flagdimension
        mytmp['usewindowstats'] = usewindowstats
        mytmp['halfwin'] = halfwin
        mytmp['extendflags'] = extendflags
        mytmp['winsize'] = winsize
        mytmp['timedev'] = timedev
        mytmp['freqdev'] = freqdev
        mytmp['timedevscale'] = timedevscale
        mytmp['freqdevscale'] = freqdevscale
        mytmp['spectralmax'] = spectralmax
        mytmp['spectralmin'] = spectralmin
        mytmp['antint_ref_antenna'] = antint_ref_antenna
        mytmp['minchanfrac'] = minchanfrac
        mytmp['verbose'] = verbose
        mytmp['extendpols'] = extendpols
        mytmp['growtime'] = growtime
        mytmp['growfreq'] = growfreq
        mytmp['growaround'] = growaround
        mytmp['flagneartime'] = flagneartime
        mytmp['flagnearfreq'] = flagnearfreq
        mytmp['minrel'] = minrel
        mytmp['maxrel'] = maxrel
        mytmp['minabs'] = minabs
        mytmp['maxabs'] = maxabs
        mytmp['spwchan'] = spwchan
        mytmp['spwcorr'] = spwcorr
        mytmp['basecnt'] = basecnt
        mytmp['fieldcnt'] = fieldcnt
        mytmp['name'] = name
        mytmp['action'] = action
        mytmp['display'] = display
        mytmp['flagbackup'] = flagbackup
        mytmp['savepars'] = savepars
        mytmp['cmdreason'] = cmdreason
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        mytmp['writeflags'] = writeflags
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'flagdata.xml')

        casalog.origin('flagdata')
        try :
          #if not trec.has_key('flagdata') or not casac.casac.utils().verify(mytmp, trec['flagdata']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['flagdata'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('flagdata', 'flagdata.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'flagdata'
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
          result = flagdata(vis, mode, autocorr, inpfile, reason, tbuff, spw, field, antenna, uvrange, timerange, correlation, scan, intent, array, observation, feed, clipminmax, datacolumn, clipoutside, channelavg, chanbin, timeavg, timebin, clipzeros, quackinterval, quackmode, quackincrement, tolerance, addantenna, lowerlimit, upperlimit, ntime, combinescans, timecutoff, freqcutoff, timefit, freqfit, maxnpieces, flagdimension, usewindowstats, halfwin, extendflags, winsize, timedev, freqdev, timedevscale, freqdevscale, spectralmax, spectralmin, antint_ref_antenna, minchanfrac, verbose, extendpols, growtime, growfreq, growaround, flagneartime, flagnearfreq, minrel, maxrel, minabs, maxabs, spwchan, spwcorr, basecnt, fieldcnt, name, action, display, flagbackup, savepars, cmdreason, outfile, overwrite, writeflags)

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
             tname = 'flagdata'
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
#        paramgui.runTask('flagdata', myf['_ip'])
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
        a['mode']  = 'manual'
        a['action']  = 'apply'
        a['savepars']  = False

        a['mode'] = {
                    0:odict([{'value':'manual'}, {'field':''}, {'spw':''}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'intent':''}, {'array':''}, {'uvrange':''}, {'observation':''}, {'feed':''}, {'autocorr':False}]), 
                    1:odict([{'value':'manualflag'}, {'field':''}, {'spw':''}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'intent':''}, {'array':''}, {'uvrange':''}, {'observation':''}, {'feed':''}, {'autocorr':False}]), 
                    2:odict([{'value':'list'}, {'inpfile':''}, {'reason':'any'}, {'tbuff':0.0}]), 
                    3:odict([{'value':'clip'}, {'field':''}, {'spw':''}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'intent':''}, {'array':''}, {'uvrange':''}, {'observation':''}, {'feed':''}, {'datacolumn':'DATA'}, {'clipminmax':[]}, {'clipoutside':True}, {'channelavg':False}, {'chanbin':1}, {'timeavg':False}, {'timebin':''}, {'clipzeros':False}]), 
                    4:odict([{'value':'quack'}, {'field':''}, {'spw':''}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'intent':''}, {'array':''}, {'uvrange':''}, {'observation':''}, {'feed':''}, {'quackinterval':0.0}, {'quackmode':'beg'}, {'quackincrement':False}]), 
                    5:odict([{'value':'shadow'}, {'field':''}, {'spw':''}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'intent':''}, {'array':''}, {'uvrange':''}, {'observation':''}, {'feed':''}, {'tolerance':0.0}, {'addantenna':''}]), 
                    6:odict([{'value':'elevation'}, {'field':''}, {'spw':''}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'intent':''}, {'array':''}, {'uvrange':''}, {'observation':''}, {'feed':''}, {'lowerlimit':0.0}, {'upperlimit':90.0}]), 
                    7:odict([{'value':'tfcrop'}, {'field':''}, {'spw':''}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'intent':''}, {'array':''}, {'uvrange':''}, {'observation':''}, {'feed':''}, {'ntime':'scan'}, {'combinescans':False}, {'datacolumn':'DATA'}, {'timecutoff':4.0}, {'freqcutoff':3.0}, {'timefit':'line'}, {'freqfit':'poly'}, {'maxnpieces':7}, {'flagdimension':'freqtime'}, {'usewindowstats':'none'}, {'halfwin':1}, {'extendflags':True}, {'channelavg':False}, {'chanbin':1}, {'timeavg':False}, {'timebin':''}]), 
                    8:odict([{'value':'rflag'}, {'field':''}, {'spw':''}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'intent':''}, {'array':''}, {'uvrange':''}, {'observation':''}, {'feed':''}, {'ntime':'scan'}, {'combinescans':False}, {'datacolumn':'DATA'}, {'winsize':3}, {'timedev':''}, {'freqdev':''}, {'timedevscale':5.0}, {'freqdevscale':5.0}, {'spectralmax':1E6}, {'spectralmin':0.0}, {'extendflags':True}, {'channelavg':False}, {'chanbin':1}, {'timeavg':False}, {'timebin':''}]), 
                    9:odict([{'value':'antint'}, {'field':''}, {'spw':''}, {'antenna':''}, {'datacolumn':'DATA'}, {'antint_ref_antenna':''}, {'minchanfrac':.6}, {'verbose':False}]), 
                    10:odict([{'value':'extend'}, {'field':''}, {'spw':''}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'intent':''}, {'array':''}, {'uvrange':''}, {'observation':''}, {'feed':''}, {'ntime':'scan'}, {'combinescans':False}, {'extendpols':True}, {'growtime':50.0}, {'growfreq':50.0}, {'growaround':False}, {'flagneartime':False}, {'flagnearfreq':False}]), 
                    11:odict([{'value':'unflag'}, {'field':''}, {'spw':''}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'intent':''}, {'array':''}, {'uvrange':''}, {'observation':''}, {'feed':''}]), 
                    12:odict([{'value':'summary'}, {'field':''}, {'spw':''}, {'antenna':''}, {'timerange':''}, {'correlation':''}, {'scan':''}, {'intent':''}, {'array':''}, {'uvrange':''}, {'observation':''}, {'feed':''}, {'minrel':0.0}, {'maxrel':1.0}, {'minabs':0}, {'maxabs':-1}, {'spwchan':False}, {'spwcorr':False}, {'basecnt':False}, {'fieldcnt':False}, {'name':'Summary'}])}
        a['action'] = {
                    0:odict([{'value':'apply'}, {'display':''}, {'flagbackup':True}]), 
                    1:odict([{'value':'calculate'}, {'display':''}]), 
                    2:{'value':''}, 
                    3:{'value':'none'}}
        a['savepars'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'cmdreason':''}, {'outfile':''}, {'overwrite':True}])}

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
    def description(self, key='flagdata', subkey=None):
        desc={'flagdata': 'All-purpose flagging task based on data-selections and flagging modes/algorithms.',
               'vis': 'Name of input visibility file',
               'mode': 'Flagging mode (list/manual/clip/quack/shadow/elevation/tfcrop/rflag/antint/extent/unflag/summary)',
               'autocorr': 'Flag only the auto-correlations?',
               'inpfile': 'Input ASCII file, list of files or Python list of strings with flag commands.',
               'reason': 'Select by REASON types',
               'tbuff': 'List of time buffers (sec) to pad timerange in flag commands',
               'spw': 'Select spectral window/channels',
               'field': 'Select field using field id(s) or field name(s)',
               'antenna': 'Select data based on antenna/baseline',
               'uvrange': 'Select data by baseline length.',
               'timerange': 'Select data based on time range',
               'correlation': 'Select data based on correlation',
               'scan': 'Scan number range',
               'intent': 'Select observing intent',
               'array': '(Sub)array numbers',
               'observation': 'Select by observation ID(s)',
               'feed': 'Multi-feed numbers: Not yet implemented',
               'clipminmax': 'Range to use for clipping',
               'datacolumn': 'Data column on which to operate',
               'clipoutside': 'Clip outside the range, or within it',
               'channelavg': 'Pre-average data across channels before analyzing visibilities for flagging',
               'chanbin': 'Bin width for channel average in number of input channels',
               'timeavg': 'Pre-average data across time before analyzing visibilities for flagging.',
               'timebin': 'Bin width for time average in seconds',
               'clipzeros': 'Clip zero-value data',
               'quackinterval': 'Quack n seconds from scan beginning or end',
               'quackmode': 'Quack mode. beg: first n seconds of scan; endb: last n seconds of scan; end: all but first n seconds of scan; tail: all but last n seconds of scan.',
               'quackincrement': 'Increment quack flagging in time taking into account flagged data or not.',
               'tolerance': 'Amount of shadow allowed (in meters)',
               'addantenna': 'File name or dictionary with additional antenna names, positions and diameters',
               'lowerlimit': 'Lower limiting elevation (in degrees)',
               'upperlimit': 'Upper limiting elevation (in degrees)',
               'ntime': 'Time-range to use for each chunk (in seconds or minutes)',
               'combinescans': 'Accumulate data across scans depending on the value of ntime.',
               'timecutoff': 'Flagging thresholds in units of deviation from the fit',
               'freqcutoff': ' Flagging thresholds in units of deviation from the fit',
               'timefit': 'Fitting function for the time direction (poly/line)',
               'freqfit': 'Fitting function for the frequency direction (poly/line)',
               'maxnpieces': 'Number of pieces in the polynomial-fits (for freqfit or timefit poly)',
               'flagdimension': 'Dimensions along which to calculate fits (freq, time, freqtime, timefreq)',
               'usewindowstats': 'Calculate additional flags using sliding window statistics (none, sum, std, both)',
               'halfwin': 'Half-width of sliding window to use with usewindowstats (1,2,3).',
               'extendflags': 'Extend flags along time, frequency and correlation.',
               'winsize': 'Number of timesteps in the sliding time window',
               'timedev': 'Time-series noise estimate',
               'freqdev': 'Spectral noise estimate',
               'timedevscale': 'Threshold scaling for timedev',
               'freqdevscale': 'Threshold scaling for freqdev.',
               'spectralmax': 'Flag whole spectrum if freqdev is greater than spectralmax',
               'spectralmin': 'Flag whole spectrum if freqdev is less than spectralmin',
               'antint_ref_antenna': 'Antenna of interest. Baselines with this antenna will be checked for flagged channels.',
               'minchanfrac': 'Minimum fraction of flagged channels required for a baseline to be deemed as flagged',
               'verbose': 'Print timestamps of flagged integrations to the log',
               'extendpols': 'If any correlation is flagged, flag all correlations',
               'growtime': 'Flag all ntime integrations if more than X percent of the timerange is flagged (0-100)',
               'growfreq': 'Flag all selected channels if more than X percent of the frequency range is flagged (0-100)',
               'growaround': 'Flag data based on surrounding flags',
               'flagneartime': 'Flag one timestep before and after a flagged one (True/False)',
               'flagnearfreq': 'Flag one channel before and after a flagged one (True/False)',
               'minrel': 'Minimum number of flags (relative)',
               'maxrel': 'Maximum number of flags (relative)',
               'minabs': 'Minimum number of flags (absolute)',
               'maxabs': 'Maximum number of flags (absolute). Use a negative value to indicate infinity.',
               'spwchan': 'Print summary of channels per spw',
               'spwcorr': 'Print summary of correlation per spw',
               'basecnt': 'Print summary counts per baseline',
               'fieldcnt': 'Produce a separated breakdown for each field',
               'name': 'Name of this summary report (key in summary dictionary)',
               'action': 'Action to perform in MS and/or in inpfile (none/apply/calculate)',
               'display': 'Display data and/or end-of-MS reports at runtime (data/report/both).',
               'flagbackup': 'Back up the state of flags before the run',
               'savepars': 'Save the current parameters to the FLAG_CMD table or to a file',
               'cmdreason': 'Reason to save to output file or to FLAG_CMD table.',
               'outfile': 'Name of output file to save current parameters. If empty, save to FLAG_CMD',
               'overwrite': 'Overwrite an existing file to save the flag commands',
               'writeflags': 'Internal hidden parameter. Do not modify.',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['mode']  = 'manual'
        a['autocorr']  = False
        a['inpfile']  = ''
        a['reason']  = 'any'
        a['tbuff']  = 0.0
        a['spw']  = ''
        a['field']  = ''
        a['antenna']  = ''
        a['uvrange']  = ''
        a['timerange']  = ''
        a['correlation']  = ''
        a['scan']  = ''
        a['intent']  = ''
        a['array']  = ''
        a['observation']  = ''
        a['feed']  = ''
        a['clipminmax']  = []
        a['datacolumn']  = 'DATA'
        a['clipoutside']  = True
        a['channelavg']  = False
        a['chanbin']  = 1
        a['timeavg']  = False
        a['timebin']  = '0s'
        a['clipzeros']  = False
        a['quackinterval']  = 1.0
        a['quackmode']  = 'beg'
        a['quackincrement']  = False
        a['tolerance']  = 0.0
        a['addantenna']  = ''
        a['lowerlimit']  = 0.0
        a['upperlimit']  = 90.0
        a['ntime']  = 'scan'
        a['combinescans']  = False
        a['timecutoff']  = 4.0
        a['freqcutoff']  = 3.0
        a['timefit']  = 'line'
        a['freqfit']  = 'poly'
        a['maxnpieces']  = 7
        a['flagdimension']  = 'freqtime'
        a['usewindowstats']  = 'none'
        a['halfwin']  = 1
        a['extendflags']  = True
        a['winsize']  = 3
        a['timedev']  = ''
        a['freqdev']  = ''
        a['timedevscale']  = 5.0
        a['freqdevscale']  = 5.0
        a['spectralmax']  = 1E6
        a['spectralmin']  = 0.0
        a['antint_ref_antenna']  = ''
        a['minchanfrac']  = 0.6
        a['verbose']  = False
        a['extendpols']  = True
        a['growtime']  = 50.0
        a['growfreq']  = 50.0
        a['growaround']  = False
        a['flagneartime']  = False
        a['flagnearfreq']  = False
        a['minrel']  = 0.0
        a['maxrel']  = 1.0
        a['minabs']  = 0
        a['maxabs']  = -1
        a['spwchan']  = False
        a['spwcorr']  = False
        a['basecnt']  = False
        a['fieldcnt']  = False
        a['name']  = 'Summary'
        a['action']  = 'apply'
        a['display']  = ''
        a['flagbackup']  = True
        a['savepars']  = False
        a['cmdreason']  = ''
        a['outfile']  = ''
        a['overwrite']  = True
        a['writeflags']  = True

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mode']  == 'manual':
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['array'] = ''
            a['uvrange'] = ''
            a['observation'] = ''
            a['feed'] = ''
            a['autocorr'] = False

        if self.parameters['mode']  == 'manualflag':
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['array'] = ''
            a['uvrange'] = ''
            a['observation'] = ''
            a['feed'] = ''
            a['autocorr'] = False

        if self.parameters['mode']  == 'list':
            a['inpfile'] = ''
            a['reason'] = 'any'
            a['tbuff'] = 0.0

        if self.parameters['mode']  == 'clip':
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['array'] = ''
            a['uvrange'] = ''
            a['observation'] = ''
            a['feed'] = ''
            a['datacolumn'] = 'DATA'
            a['clipminmax'] = []
            a['clipoutside'] = True
            a['channelavg'] = False
            a['chanbin'] = 1
            a['timeavg'] = False
            a['timebin'] = ''
            a['clipzeros'] = False

        if self.parameters['mode']  == 'quack':
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['array'] = ''
            a['uvrange'] = ''
            a['observation'] = ''
            a['feed'] = ''
            a['quackinterval'] = 0.0
            a['quackmode'] = 'beg'
            a['quackincrement'] = False

        if self.parameters['mode']  == 'shadow':
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['array'] = ''
            a['uvrange'] = ''
            a['observation'] = ''
            a['feed'] = ''
            a['tolerance'] = 0.0
            a['addantenna'] = ''

        if self.parameters['mode']  == 'elevation':
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['array'] = ''
            a['uvrange'] = ''
            a['observation'] = ''
            a['feed'] = ''
            a['lowerlimit'] = 0.0
            a['upperlimit'] = 90.0

        if self.parameters['mode']  == 'tfcrop':
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['array'] = ''
            a['uvrange'] = ''
            a['observation'] = ''
            a['feed'] = ''
            a['ntime'] = 'scan'
            a['combinescans'] = False
            a['datacolumn'] = 'DATA'
            a['timecutoff'] = 4.0
            a['freqcutoff'] = 3.0
            a['timefit'] = 'line'
            a['freqfit'] = 'poly'
            a['maxnpieces'] = 7
            a['flagdimension'] = 'freqtime'
            a['usewindowstats'] = 'none'
            a['halfwin'] = 1
            a['extendflags'] = True
            a['channelavg'] = False
            a['chanbin'] = 1
            a['timeavg'] = False
            a['timebin'] = ''

        if self.parameters['mode']  == 'rflag':
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['array'] = ''
            a['uvrange'] = ''
            a['observation'] = ''
            a['feed'] = ''
            a['ntime'] = 'scan'
            a['combinescans'] = False
            a['datacolumn'] = 'DATA'
            a['winsize'] = 3
            a['timedev'] = ''
            a['freqdev'] = ''
            a['timedevscale'] = 5.0
            a['freqdevscale'] = 5.0
            a['spectralmax'] = 1E6
            a['spectralmin'] = 0.0
            a['extendflags'] = True
            a['channelavg'] = False
            a['chanbin'] = 1
            a['timeavg'] = False
            a['timebin'] = ''

        if self.parameters['mode']  == 'antint':
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['datacolumn'] = 'DATA'
            a['antint_ref_antenna'] = ''
            a['minchanfrac'] = .6
            a['verbose'] = False

        if self.parameters['mode']  == 'extend':
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['array'] = ''
            a['uvrange'] = ''
            a['observation'] = ''
            a['feed'] = ''
            a['ntime'] = 'scan'
            a['combinescans'] = False
            a['extendpols'] = True
            a['growtime'] = 50.0
            a['growfreq'] = 50.0
            a['growaround'] = False
            a['flagneartime'] = False
            a['flagnearfreq'] = False

        if self.parameters['mode']  == 'unflag':
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['array'] = ''
            a['uvrange'] = ''
            a['observation'] = ''
            a['feed'] = ''

        if self.parameters['mode']  == 'summary':
            a['field'] = ''
            a['spw'] = ''
            a['antenna'] = ''
            a['timerange'] = ''
            a['correlation'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['array'] = ''
            a['uvrange'] = ''
            a['observation'] = ''
            a['feed'] = ''
            a['minrel'] = 0.0
            a['maxrel'] = 1.0
            a['minabs'] = 0
            a['maxabs'] = -1
            a['spwchan'] = False
            a['spwcorr'] = False
            a['basecnt'] = False
            a['fieldcnt'] = False
            a['name'] = 'Summary'

        if self.parameters['action']  == 'apply':
            a['display'] = ''
            a['flagbackup'] = True

        if self.parameters['action']  == 'calculate':
            a['display'] = ''

        if self.parameters['savepars']  == True:
            a['cmdreason'] = ''
            a['outfile'] = ''
            a['overwrite'] = True

        if a.has_key(paramname) :
              return a[paramname]
flagdata_cli = flagdata_cli_()