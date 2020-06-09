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
import task_sdbaseline
def sdbaseline(infile='', datacolumn='data', antenna='', field='', spw='', timerange='', scan='', pol='', intent='', reindex=True, maskmode='list', thresh=5.0, avg_limit=4, minwidth=4, edge=[0, 0], blmode='fit', dosubtract=True, blformat='text', bloutput='', bltable='', blfunc='poly', order=5, npiece=2, applyfft=True, fftmethod='fft', fftthresh=3.0, addwn=[0], rejwn=[], clipthresh=3.0, clipniter=0, blparam='', verbose=False, showprogress=False, minnrow=1000, outfile='', overwrite=False):

        """Fit/subtract a spectral baseline 
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
        if type(edge)==int: edge=[edge]

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
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'sdbaseline.xml')

        casalog.origin('sdbaseline')
        if trec.has_key('sdbaseline') and casac.utils().verify(mytmp, trec['sdbaseline']) :
            result = task_sdbaseline.sdbaseline(infile, datacolumn, antenna, field, spw, timerange, scan, pol, intent, reindex, maskmode, thresh, avg_limit, minwidth, edge, blmode, dosubtract, blformat, bloutput, bltable, blfunc, order, npiece, applyfft, fftmethod, fftthresh, addwn, rejwn, clipthresh, clipniter, blparam, verbose, showprogress, minnrow, outfile, overwrite)

        else :
          result = False
        return result
