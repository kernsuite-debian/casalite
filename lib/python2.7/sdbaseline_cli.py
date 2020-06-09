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
from task_sdbaseline import sdbaseline
class sdbaseline_cli_:
    __name__ = "sdbaseline"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (sdbaseline_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'infile':None, 'datacolumn':None, 'antenna':None, 'field':None, 'spw':None, 'timerange':None, 'scan':None, 'pol':None, 'intent':None, 'reindex':None, 'maskmode':None, 'thresh':None, 'avg_limit':None, 'minwidth':None, 'edge':None, 'blmode':None, 'dosubtract':None, 'blformat':None, 'bloutput':None, 'bltable':None, 'blfunc':None, 'order':None, 'npiece':None, 'applyfft':None, 'fftmethod':None, 'fftthresh':None, 'addwn':None, 'rejwn':None, 'clipthresh':None, 'clipniter':None, 'blparam':None, 'verbose':None, 'showprogress':None, 'minnrow':None, 'outfile':None, 'overwrite':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, infile=None, datacolumn=None, antenna=None, field=None, spw=None, timerange=None, scan=None, pol=None, intent=None, reindex=None, maskmode=None, thresh=None, avg_limit=None, minwidth=None, edge=None, blmode=None, dosubtract=None, blformat=None, bloutput=None, bltable=None, blfunc=None, order=None, npiece=None, applyfft=None, fftmethod=None, fftthresh=None, addwn=None, rejwn=None, clipthresh=None, clipniter=None, blparam=None, verbose=None, showprogress=None, minnrow=None, outfile=None, overwrite=None, ):

        """Fit/subtract a spectral baseline 

        Detailed Description:

Task sdbaseline fits and/or subtracts baseline from single-dish spectra.
Given baseline parameters (baseline type, order, etc.), sdbaseline 
computes the best-fit baseline for each spectrum by least-square fitting 
method and, if you want, subtracts it. The best-fit baseline parameters 
(including baseline type, coefficients of basis functions, etc.) and 
other values such as residual rms can be saved in various formats 
including ascii text (in human-readable format or CSV format) or baseline 
table (a CASA table).
Sdbaseline has another mode to 'apply' a baseline table to a MS data; 
for each spectrum in MS, the best-fit baseline is reproduced from the 
baseline parameters stored in the given baseline table and subtracted. 
Putting 'fit' and 'subtract' into separate processes can be useful for 
pipeline processing for huge dataset.
  
        Arguments :
                infile: name of input SD dataset
                   Default Value: 

                datacolumn: name of data column to be used ["data", "float_data", or "corrected"]
                   Default Value: data
                   Allowed Values:
                                data
                                float_data
                                corrected

                antenna: select data by antenna name or ID, e.g. "PM03"
                   Default Value: 

                field: select data by field IDs and names, e.g. "3C2*" (""=all)
                   Default Value: 

                spw: select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
                   Default Value: 

                timerange: select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
                   Default Value: 

                scan: select data by scan numbers, e.g. "21~23" (""=all)
                   Default Value: 

                pol: select data by polarization IDs, e.g. "XX,YY" (""=all)
                   Default Value: 

                intent: select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
                   Default Value: 

                reindex: Re-index indices in subtables based on data selection. Ignored when blmode='apply'.
                   Default Value: True

                maskmode: mode of setting additional channel masks. "list" and "auto" are available now.
                   Default Value: list
                   Allowed Values:
                                auto
                                list

                thresh: S/N threshold for linefinder
                   Default Value: 5.0

                avg_limit: channel averaging for broad lines
                   Default Value: 4

                minwidth: the minimum channel width to detect as a line
                   Default Value: 4

                edge: channels to drop at beginning and end of spectrum
                   Default Value: 00

                blmode: baselining mode ["fit" or "apply"]
                   Default Value: fit

                dosubtract: subtract baseline from input data [True, False] 
                   Default Value: True

                blformat: format(s) of file(s) in which best-fit parameters are written ["text", "csv", "table" or ""]
                   Default Value: text
                   Allowed Values:
                                table
                                text
                                csv
                                

                bloutput: name(s) of file(s) in which best-fit parameters are written
                   Default Value: 

                bltable: name of baseline table to apply
                   Default Value: 

                blfunc: baseline model function ["poly", "chebyshev", "cspline", "sinusoid", or "variable"(expert mode)]
                   Default Value: poly
                   Allowed Values:
                                poly
                                chebyshev
                                cspline
                                sinusoid
                                variable

                order: order of baseline model function
                   Default Value: 5

                npiece: number of element polynomials for cubic spline curve
                   Default Value: 2

                applyfft: automatically set wave numbers of sinusoids
                   Default Value: True

                fftmethod: method for automatically set wave numbers of sinusoids
                   Default Value: fft
                   Allowed Values:
                                fft

                fftthresh: threshold to select wave numbers of sinusoids
                   Default Value: 3.0

                addwn: additional wave numbers to use
                   Default Value: 0

                rejwn: wave numbers NOT to use
                   Default Value: 

                clipthresh: clipping threshold for iterative fitting
                   Default Value: 3.0

                clipniter: maximum iteration number for iterative fitting
                   Default Value: 0

                blparam: text file that stores per spectrum fit parameters
                   Default Value: 

                verbose: output fitting parameters to logger
                   Default Value: False

                showprogress: (NOT SUPPORTED YET) show progress status for large data
                   Default Value: False

                minnrow: (NOT SUPPORTED YET) minimum number of input spectra to show progress status
                   Default Value: 1000

                outfile: name of output file
                   Default Value: 

                overwrite: overwrite the output file if already exists
                   Default Value: False

        Returns: void

        Example :

-----------------
Keyword arguments
-----------------
infile -- name of input SD dataset
datacolumn -- name of data column to be used
        options: 'data', 'float_data', or 'corrected'
        default: 'data'
antenna -- select data by antenna name or ID
        default: '' (use all antennas)
        example: 'PM03'
field -- select data by field IDs and names
        default: '' (use all fields)
        example: field='3C2*' (all names starting with 3C2)
                 field='0,4,5~7' (field IDs 0,4,5,6,7)
                 field='0,3C273' (field ID 0 or field named 3C273)
        this selection is in addition to the other selections to data
spw -- select data by IF IDs (spectral windows)/channels
        default: '' (use all IFs and channels)
        example: spw='3,5,7' (IF IDs 3,5,7; all channels)
                 spw='<2' (IF IDs less than 2, i.e., 0,1; all channels)
                 spw='30~45GHz' (IF IDs with the center frequencies in range 30-45GHz; all channels)
                 spw='0:5~61' (IF ID 0; channels 5 to 61; all channels)
                 spw='3:10~20;50~60' (select multiple channel ranges within IF ID 3)
                 spw='3:10~20,4:0~30' (select different channel ranges for IF IDs 3 and 4)
                 spw='1~4;6:15~48' (for channels 15 through 48 for IF IDs 1,2,3,4 and 6)
        this selection is in addition to the other selections to data
timerange -- select data by time range
        default: '' (use all)
        example: timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                 Note: YYYY/MM/DD can be dropped as needed:
                 timerange='09:14:00~09:54:00' # this time range
                 timerange='09:44:00' # data within one integration of time
                 timerange='>10:24:00' # data after this time
                 timerange='09:44:00+00:13:00' #data 13 minutes after time
        this selection is in addition to the other selections to data
scan -- select data by scan numbers
        default: '' (use all scans)
        example: scan='21~23' (scan IDs 21,22,23)
        this selection is in addition to the other selections to data
pol -- select data by polarization IDs
        default: '' (use all polarizations)
        example: pol='XX,YY' (polarizations XX and YY)
        this selection is in addition to the other selections to data
intent -- select data by observational intent, also referred to as 'scan intent'
        default: '' (use all scan intents)
        example: intent='*ON_SOURCE*' (any valid scan-intent expression accepted by the MSSelection module can be specified)
        this selection is in addition to the other selections to data
reindex -- Re-index indices in subtables based on data selection.
           Ignored when blmode='apply'.
           If True, DATA_DESCRIPTION, FEED, SPECTRAL_WINDOW, STATE, and SOURCE
           subtables are filtered  based on data selection and re-indexed in output MS.
           default: True
maskmode -- mode of setting additional channel masks. When blmode='apply'
             and/or blfunc='variable', maskmode and its subparameters
             are ignored.
        options: 'list' and 'auto' ('interact' will be available later)
        default: 'list'
        example: maskmode='auto' runs linefinder to detect line regions 
                 to be excluded from fitting. this mode requires three 
                 expandable parameters: thresh, avg_limit, minwidth, and edge.
                 NOTE maskmode='auto' is EXPERIMENTAL.
                 USE WITH CARE! May need to tweak the expandable parameters.
                 maskmode='list' uses the given masklist only: no additional 
                 masks applied.
                 maskmode='interact' allows users to manually modify the 
                 mask regions by dragging mouse on the spectrum plotter GUI.
                 use LEFT or RIGHT button to add or delete regions, 
                 respectively.
    >>> maskmode expandable parameters
        thresh -- S/N threshold for linefinder. a single channel S/N ratio
                  above which the channel is considered to be a detection. 
                default: 5
        avg_limit -- channel averaging for broad lines. a number of
                     consecutive channels not greater than this parameter
                     can be averaged to search for broad lines.
                default: 4
        minwidth -- the minimum channel width to detect as a line.
                     a line with number of consecutive channels less
                     than this parameter will not be detected as a line.
                default: 4
        edge -- channels to drop at beginning and end of spectrum
                default: 0
                example: edge=[1000] drops 1000 channels at beginning AND end.
                         edge=[1000,500] drops 1000 from beginning and 500
                         from end.
        Note: For bad baselines threshold should be increased,
        and avg_limit decreased (r even switched off completely by
        setting this parameter to 1) to avoid detecting baseline
        undulations instead of real lines.
blmode -- baselining mode. 
        options: 'fit', 'apply'
        default: 'fit'
        example: blmode='fit' calculates the best-fit baseline based on 
                 given baseline type, then (if you set dosubtract=True) 
                 subtract it from each spectrum. The information about 
                 best-fit baselines (baseline type, order, coefficients, 
                 etc.) can be stored in various formats (cf. blformat).
                 blmode='apply' reads a baseline table as well as input 
                 MS, reproduces the best-fit baseline via info written 
                 in the baseline table, then subtracts it from each 
                 spectrum. 
    >>> blmode expandable parameters
        dosubtract -- execute baseline subtraction in addition to fitting.
                      Note that dosubtract=False will be ignored if 
                      bloutput is given, that is, baseline subtraction 
                      will be always executed for the input MS in case 
                      bloutput is not specified.
                options: (bool) True, False
                default: True
        blformat -- format(s) of file(s) in which best-fit parameters are 
                    written. 
                options: 'text', 'csv', 'table', and '' can be set for
                         a single output. In case you want to output 
                         fitting results in multiple formats, a list 
                         containing the above keywords is accepted as well.
                default: 'text'
                example: (1) blformat='text' outputs an ascii text file 
                         with the best-fit baseline parameters written 
                         in human-readable format. It may be good to read, 
                         but you should mind it might be huge.
                         (2) blformat='csv' outputs a CSV file. For example, 
                         output of csv with blfunc='poly' is as below:
                         #scan, beam, spw, pol, MJD[s], fitrange (i.e. inverse mask), blfunc, order, fitting coefficients, rms, number of clipped channels 
                         4,0,17,0,4915973292.23,[[252;3828]],poly,1,767.647,-0.00956208,26.3036,0
                         ... .
                         (3) blformat='table' outputs a baseline table 
                         which can be used to apply afterwards.
                         (4) blformat='' doesn't output any parameter file.
                         (5) blformat=['csv','table'] outputs both a CSV 
                         file and a baseline table. 
                         (6) If one or more ''s appear in blformat, they 
                         are all ignored. For example, if blformat=['',
                         'text',''] is given, only 'text' will be output. 
                         (7) Elements of blformat other than '' must not 
                         be duplicated. For example, blformat=['text','',
                         'text'] is not accepted.
        bloutput -- name(s) of file(s) in which best-fit parameters are 
                    written. If bloutput is a null string '', name(s) of 
                    baseline parameter file(s) will be set as follows: 
                    <outfile>_blparam.txt for blformat='text', 
                    <outfile>_blparam.csv for blformat='csv', and 
                    <outfile>_blparam.bltable for blformat='table'.
                    Otherwise, blformat and bloutput must have the same 
                    length, and one-to-one correspondence is assumed 
                    between them. If there are '' elements in bloutput, 
                    output file names will be set by following the above 
                    rules. If there are '' elements in blformat, the 
                    corresponding bloutput elements will be ignored. 
                    Also, non-'' bloutput elements correspoding to 
                    non-'' blformat elements must not be duplicated.
                default: ''
                example: (1) bloutput='' and blformat=['csv','table']: 
                         outputs a csv file '<outfile>_blparam.csv'
                         and a baseline table '<outfile>_blparam.bltable'.
                         (2) bloutput=['foo.csv',''] and blformat=['csv',
                         'table']: outputs a csv file 'foo.csv' and a 
                         baseline table '<outfile>_blparam.bltable'.
                         (3) bloutput=['foo.csv','bar.blt'] and blformat=
                         ['csv','']: outputs a csv file 'foo.csv' only.
                         (4) bloutput=['foo.csv','foo.csv','bar.blt'] and 
                         blformat=['csv','','table']: the second 'foo.csv' 
                         is ignored because it corresponds to the blformat 
                         element '', and thus outputs a csv file 'foo.csv' 
                         and a baseline table 'bar.blt'.
                         (5) bloutput=['foo.csv','foo.csv','bar.blt'] and 
                         blformat=['csv','text','table']: will be error 
                         since 'foo.csv' is duplicated.
                         (6) bloutput=['foo.csv','bar.blt'] and blformat=
                         ['csv','','table']: will be error since bloutput 
                         and blformat have different lengths.
        bltable -- name of baseline table to apply
                default: ''
blfunc -- baseline model function. In cases blmode='apply' or blparam is 
          set, blfunc and its subparameters are ignored.
        options: 'poly', 'chebyshev', 'cspline', 'sinusoid' or 'variable'
        default: 'poly'
        example: blfunc='poly' uses a single polynomial line of 
                 any order which should be given as an expandable 
                 parameter 'order' to fit baseline. 
                 blfunc='chebyshev' uses Chebyshev polynomials. 
                 blfunc='cspline' uses a cubic spline function, a piecewise 
                 cubic polynomial having C2-continuity (i.e., the second 
                 derivative is continuous at the joining points). 
                 blfunc='sinusoid' uses a combination of sinusoidal curves. 
        NOTE blfunc='variable' IS EXPERT MODE!!!
    >>> blfunc expandable parameters
        order -- order of baseline model function
                options: (int) (<0 turns off baseline fitting)
                default: 5
                example: typically in range 2-9 (higher values
                         seem to be needed for GBT)
        npiece -- number of the element polynomials of cubic spline curve
                options: (int) (<0 turns off baseline fitting)
                default: 2
        applyfft -- automatically choose an appropriate set of sinusoidal 
                    wave numbers via FFT for each spectrum data.
                options: (bool) True, False
                default: True
        fftmethod -- method to be used when applyfft=True. Now only 
                     'fft' is available and it is the default.
        fftthresh -- threshold on Fourier-domain spectrum data to pick up 
                     appropriate wave numbers to be used for sinusoidal 
                     fitting. both (float) and (str) accepted.
                     given a float value, the unit is set to sigma.
                     for string values, allowed formats include:
                     'xsigma' or 'x' (= above x-sigma level. e.g., '3sigma')
                     or 'topx' (= the x strongest ones, e.g. 'top5'). 
                default is 3.0 (i.e., above 3sigma level).
        addwn -- additional wave number(s) of sinusoids to be used 
                 for fitting. 
                 (list) and (int) are accepted to specify every
                 wave numbers. also (str) can be used in case
                 you need to specify wave numbers in a certain range.
                 default: [0] (i.e., constant is subtracted at least)
                 example: 0
                          [0,1,2]
                          '0,1,2'
                          'a-b' (= a, a+1, ..., b)
                          'a~b' (= a, a+1, ..., b)
                          '<a'  (= 0,1,...,a-2,a-1)
                          '>=a' (= a, a+1, ... up to the maximum wave
                                   number corresponding to the Nyquist
                                   frequency for the case of FFT)
        rejwn -- wave number(s) of sinusoid NOT to be used for fitting.
                 can be set just as addwn but has higher priority:
                 wave numbers which are specified both in addwn
                 and rejwn will NOT be used. 
                 note also that rejwn value takes precedence over those 
                 automatically selected by setting applyfft=True as well.
                 default: []
        clipthresh -- clipping threshold for iterative fitting
                 default: 3
        clipniter -- maximum iteration number for iterative fitting
                 default: 0 (no iteration, i.e., no clipping)
        blparam -- the name of text file that stores per spectrum fit
                   parameters. See below for details of format.
        verbose -- output fitting parameters to logger (ONLY available
           for blfunc='variable'. if False, the fitting parameters are
           not output to the CASA logger.
            options: (bool) True, False
            default: False
showprogress -- (NOT SUPPORTED YET) show progress status for large data
        options: (bool) False (this capability is currently unavailable.)
        default: False
    >>> showprogress expandable parameter
        minnrow -- (NOT SUPPORTED YET) minimum number of input spectra to show progress status
                 default: 1000
outfile -- name of output file
        default: '' (<infile>_bs)
overwrite -- overwrite the output file if already exists
        options: (bool) True, False
        default: False
        NOTE this parameter is ignored when outform='ASCII'


-----------
DESCRIPTION
-----------

Task sdbaseline performs baseline fitting/subtraction for single-dish spectra.
The fit parameters, terms and rms of baseline can be saved into an ascii file 
or baseline table. Subtracting baseline from data in input MS using existing 
baseline table is also possible.

-----------------------
BASELINE MODEL FUNCTION
-----------------------
The list of available model functions are shown above (see Keyword arguments
section). In general 'cspline' or 'chebyshev' are recommended since they are
more stable than others. 'poly' will work for lower order but will be unstable
for higher order fitting. 'sinusoid' is kind of special mode that will be
useful for the data that clearly shows standing wave in the spectral baseline.

----------------------------------
SIGMA CLIPPING (ITERATIVE FITTING)
----------------------------------
In general least square fitting is strongly affected by an extreme data
so that the resulting fit makes worse. Sigma clipping is an iterative
baseline fitting with data clipping based on a certain threshold. Threshold
is set as a certain factor times rms of the resulting (baseline subtracted)
spectra. If sigma clipping is on, baseline fit/removal is performed several
times. After each baseline subtraction, the data whose absolute value is
above threshold are detected and those data are excluded from the next round
of fitting. By using sigma clipping, extreme data are excluded from the
fit so that resulting fit is more robust.

The user is able to control a multiplication factor using parameter
clipthresh for clipping threshold based on rms. Actual threshold for sigma
clipping will be (clipthresh) x (rms of spectra). Also, the user can specify
number of maximum iteration to the parameter clipniter.

In general, sigma clipping will lower the performance since it increases
number of fits per spectra. However, it is strongly recommended to turn
on sigma clipping unless you are sure that the data is free from any kind
of extreme values that may affect the fit.


----------------------------------
PER SPECTRUM FIT PARAMETERS
----------------------------------
Per spectrum baseline fitting parameter is accepted in blfunc='variable'.
Note this is an expert mode. The fitting parameters should be defined in
a text file for each spectrum in the input MS. The text file should store
comma separated values in order of:
row ID, polarization, mask, clipniter, clipthresh, use_linefinder, 
thresh, left edge, right edge, avg_limit, blfunc, order, npiece, nwave.
Each row in the text file must contain the following keys and values:
* 'row': row number after selection,
* 'pol': polarization index in the row,
* 'clipniter': maximum iteration number for iterative fitting,
* 'blfunc': function name.
     available ones include, 'poly', 'chebyshev', 'cspline',and 'sinusoid'
* 'order': maximum order of polynomial. needed when blfunc='poly'
     or 'chebyshev', 
* 'npiece': number or piecewise polynomial. needed when blfunc='cspline',
and
* 'nwave': a list of sinusoidal wave numbers. needed when blfunc='sinusoid'.

example:
#row,pol,mask,clipniter,clipthresh,use_linefinder,thresh,Ledge,Redge,avg_limit,blfunc,order,npiece,nwave
1,1,0~4000;6000~8000,0,3.,false,0.,0,0,0,chebyshev,0,0,[]
1,0,,0,3.,false,0.,0,0,0,poly,1,0,[]
0,1,,0,3.,false,0.,0,0,0,chebyshev,2,0,[]
0,0,,0,3.,false,,,,,cspline,,1,[]

  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'sdbaseline'
        self.__globals__['taskname'] = 'sdbaseline'
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

            myparams['infile'] = infile = self.parameters['infile']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['pol'] = pol = self.parameters['pol']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['reindex'] = reindex = self.parameters['reindex']
            myparams['maskmode'] = maskmode = self.parameters['maskmode']
            myparams['thresh'] = thresh = self.parameters['thresh']
            myparams['avg_limit'] = avg_limit = self.parameters['avg_limit']
            myparams['minwidth'] = minwidth = self.parameters['minwidth']
            myparams['edge'] = edge = self.parameters['edge']
            myparams['blmode'] = blmode = self.parameters['blmode']
            myparams['dosubtract'] = dosubtract = self.parameters['dosubtract']
            myparams['blformat'] = blformat = self.parameters['blformat']
            myparams['bloutput'] = bloutput = self.parameters['bloutput']
            myparams['bltable'] = bltable = self.parameters['bltable']
            myparams['blfunc'] = blfunc = self.parameters['blfunc']
            myparams['order'] = order = self.parameters['order']
            myparams['npiece'] = npiece = self.parameters['npiece']
            myparams['applyfft'] = applyfft = self.parameters['applyfft']
            myparams['fftmethod'] = fftmethod = self.parameters['fftmethod']
            myparams['fftthresh'] = fftthresh = self.parameters['fftthresh']
            myparams['addwn'] = addwn = self.parameters['addwn']
            myparams['rejwn'] = rejwn = self.parameters['rejwn']
            myparams['clipthresh'] = clipthresh = self.parameters['clipthresh']
            myparams['clipniter'] = clipniter = self.parameters['clipniter']
            myparams['blparam'] = blparam = self.parameters['blparam']
            myparams['verbose'] = verbose = self.parameters['verbose']
            myparams['showprogress'] = showprogress = self.parameters['showprogress']
            myparams['minnrow'] = minnrow = self.parameters['minnrow']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']

        if type(edge)==int: edge=[edge]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['datacolumn'] = datacolumn
        mytmp['antenna'] = antenna
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['timerange'] = timerange
        mytmp['scan'] = scan
        mytmp['pol'] = pol
        mytmp['intent'] = intent
        mytmp['reindex'] = reindex
        mytmp['maskmode'] = maskmode
        mytmp['thresh'] = thresh
        mytmp['avg_limit'] = avg_limit
        mytmp['minwidth'] = minwidth
        mytmp['edge'] = edge
        mytmp['blmode'] = blmode
        mytmp['dosubtract'] = dosubtract
        mytmp['blformat'] = blformat
        mytmp['bloutput'] = bloutput
        mytmp['bltable'] = bltable
        mytmp['blfunc'] = blfunc
        mytmp['order'] = order
        mytmp['npiece'] = npiece
        mytmp['applyfft'] = applyfft
        mytmp['fftmethod'] = fftmethod
        mytmp['fftthresh'] = fftthresh
        mytmp['addwn'] = addwn
        mytmp['rejwn'] = rejwn
        mytmp['clipthresh'] = clipthresh
        mytmp['clipniter'] = clipniter
        mytmp['blparam'] = blparam
        mytmp['verbose'] = verbose
        mytmp['showprogress'] = showprogress
        mytmp['minnrow'] = minnrow
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'sdbaseline.xml')

        casalog.origin('sdbaseline')
        try :
          #if not trec.has_key('sdbaseline') or not casac.casac.utils().verify(mytmp, trec['sdbaseline']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['sdbaseline'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('sdbaseline', 'sdbaseline.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'sdbaseline'
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
          result = sdbaseline(infile, datacolumn, antenna, field, spw, timerange, scan, pol, intent, reindex, maskmode, thresh, avg_limit, minwidth, edge, blmode, dosubtract, blformat, bloutput, bltable, blfunc, order, npiece, applyfft, fftmethod, fftthresh, addwn, rejwn, clipthresh, clipniter, blparam, verbose, showprogress, minnrow, outfile, overwrite)

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
             tname = 'sdbaseline'
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
#        paramgui.runTask('sdbaseline', myf['_ip'])
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
        a['infile']  = ''
        a['datacolumn']  = 'data'
        a['antenna']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['timerange']  = ''
        a['scan']  = ''
        a['pol']  = ''
        a['intent']  = ''
        a['reindex']  = True
        a['maskmode']  = 'list'
        a['blmode']  = 'fit'
        a['blfunc']  = 'poly'
        a['showprogress']  = False
        a['outfile']  = ''
        a['overwrite']  = False

        a['maskmode'] = {
                    0:{'value':'list'}, 
                    1:odict([{'value':'auto'}, {'thresh':5.0}, {'avg_limit':4}, {'minwidth':4}, {'edge':[0, 0]}]), 
                    2:{'value':'interact'}}
        a['blmode'] = {
                    0:odict([{'value':'fit'}, {'dosubtract':True}, {'blformat':'text'}, {'bloutput':''}]), 
                    1:odict([{'value':'apply'}, {'bltable':''}])}
        a['blfunc'] = {
                    0:odict([{'value':'poly'}, {'order':5}, {'clipthresh':3.0}, {'clipniter':0}]), 
                    1:odict([{'value':'chebyshev'}, {'order':5}, {'clipthresh':3.0}, {'clipniter':0}]), 
                    2:odict([{'value':'cspline'}, {'npiece':2}, {'clipthresh':3.0}, {'clipniter':0}]), 
                    3:odict([{'value':'sinusoid'}, {'applyfft':True}, {'fftmethod':'fft'}, {'fftthresh':3.0}, {'addwn':[0]}, {'rejwn':[]}, {'clipthresh':3.0}, {'clipniter':0}]), 
                    4:odict([{'value':'variable'}, {'blparam':''}, {'verbose':False}])}
        a['showprogress'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'minnrow':1000}])}

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
    def description(self, key='sdbaseline', subkey=None):
        desc={'sdbaseline': 'Fit/subtract a spectral baseline ',
               'infile': 'name of input SD dataset',
               'datacolumn': 'name of data column to be used ["data", "float_data", or "corrected"]',
               'antenna': 'select data by antenna name or ID, e.g. "PM03"',
               'field': 'select data by field IDs and names, e.g. "3C2*" (""=all)',
               'spw': 'select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)',
               'timerange': 'select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)',
               'scan': 'select data by scan numbers, e.g. "21~23" (""=all)',
               'pol': 'select data by polarization IDs, e.g. "XX,YY" (""=all)',
               'intent': 'select data by observational intent, e.g. "*ON_SOURCE*" (""=all)',
               'reindex': 'Re-index indices in subtables based on data selection',
               'maskmode': 'mode of setting additional channel masks',
               'thresh': 'S/N threshold for linefinder',
               'avg_limit': 'channel averaging for broad lines',
               'minwidth': 'the minimum channel width to detect as a line',
               'edge': 'channels to drop at beginning and end of spectrum',
               'blmode': 'baselining mode ["fit" or "apply"]',
               'dosubtract': 'subtract baseline from input data [True, False] ',
               'blformat': 'format(s) of file(s) in which best-fit parameters are written',
               'bloutput': 'name(s) of file(s) in which best-fit parameters are written',
               'bltable': 'name of baseline table to apply',
               'blfunc': 'baseline model function',
               'order': 'order of baseline model function',
               'npiece': 'number of element polynomials for cubic spline curve',
               'applyfft': 'automatically set wave numbers of sinusoids',
               'fftmethod': 'method for automatically set wave numbers of sinusoids ["fft"]',
               'fftthresh': 'threshold to select wave numbers of sinusoids',
               'addwn': 'additional wave numbers to use',
               'rejwn': 'wave numbers NOT to use',
               'clipthresh': 'clipping threshold for iterative fitting',
               'clipniter': 'maximum iteration number for iterative fitting',
               'blparam': 'text file that stores per spectrum fit parameters',
               'verbose': 'output fitting parameters to logger [True, False]',
               'showprogress': '(NOT SUPPORTED YET) show progress status for large data [True, False] (NOT SUPPORTED YET)',
               'minnrow': '(NOT SUPPORTED YET) minimum number of input spectra to show progress status',
               'outfile': 'name of output file',
               'overwrite': 'overwrite the output file if already exists [True, False] ',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['infile']  = ''
        a['datacolumn']  = 'data'
        a['antenna']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['timerange']  = ''
        a['scan']  = ''
        a['pol']  = ''
        a['intent']  = ''
        a['reindex']  = True
        a['maskmode']  = 'list'
        a['thresh']  = 5.0
        a['avg_limit']  = 4
        a['minwidth']  = 4
        a['edge']  = [0, 0]
        a['blmode']  = 'fit'
        a['dosubtract']  = True
        a['blformat']  = 'text'
        a['bloutput']  = ''
        a['bltable']  = ''
        a['blfunc']  = 'poly'
        a['order']  = 5
        a['npiece']  = 2
        a['applyfft']  = True
        a['fftmethod']  = 'fft'
        a['fftthresh']  = 3.0
        a['addwn']  = [0]
        a['rejwn']  = []
        a['clipthresh']  = 3.0
        a['clipniter']  = 0
        a['blparam']  = ''
        a['verbose']  = False
        a['showprogress']  = False
        a['minnrow']  = 1000
        a['outfile']  = ''
        a['overwrite']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['maskmode']  == 'auto':
            a['thresh'] = 5.0
            a['avg_limit'] = 4
            a['minwidth'] = 4
            a['edge'] = [0, 0]

        if self.parameters['blmode']  == 'fit':
            a['dosubtract'] = True
            a['blformat'] = 'text'
            a['bloutput'] = ''

        if self.parameters['blmode']  == 'apply':
            a['bltable'] = ''

        if self.parameters['blfunc']  == 'poly':
            a['order'] = 5
            a['clipthresh'] = 3.0
            a['clipniter'] = 0

        if self.parameters['blfunc']  == 'chebyshev':
            a['order'] = 5
            a['clipthresh'] = 3.0
            a['clipniter'] = 0

        if self.parameters['blfunc']  == 'cspline':
            a['npiece'] = 2
            a['clipthresh'] = 3.0
            a['clipniter'] = 0

        if self.parameters['blfunc']  == 'sinusoid':
            a['applyfft'] = True
            a['fftmethod'] = 'fft'
            a['fftthresh'] = 3.0
            a['addwn'] = [0]
            a['rejwn'] = []
            a['clipthresh'] = 3.0
            a['clipniter'] = 0

        if self.parameters['blfunc']  == 'variable':
            a['blparam'] = ''
            a['verbose'] = False

        if self.parameters['showprogress']  == True:
            a['minnrow'] = 1000

        if a.has_key(paramname) :
              return a[paramname]
sdbaseline_cli = sdbaseline_cli_()
