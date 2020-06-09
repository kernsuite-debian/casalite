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
import task_sdfit
def sdfit(infile='', datacolumn='data', antenna='', field='', spw='', timerange='', scan='', pol='', intent='', timebin='', timespan='', polaverage='', fitfunc='gaussian', fitmode='list', nfit=[0], thresh=5.0, avg_limit=4, minwidth=4, edge=[0, 0], outfile='', overwrite=False):

        """Fit a spectral line
-----------------
Keyword arguments
-----------------
infile -- name of input SD dataset
datacolumn -- name of data column to be used
        options: 'data', 'float_data', or 'corrected_data'
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
timebin -- bin width for time averaging. it must be a positive value.
        default: '' (no averaging over time)
        example: timebin='1s' (time averaging performed over 1 second bins)
    >>> timebin expandable parameters
        timespan -- span the timebin across 'scan', 'state', 'field', or a combination of them (e.g., 'scan,state')
                default: '' (average each scan, intent and field separately)
                example: 'scan' time averaging is done across scan ID boundaries
polaverage -- polarization averaging mode
        default: '' (no averaging over polarization)
        options: '', 'stokes', 'geometric'
fitfunc -- function for fitting
        options: 'gaussian', 'lorentzian'
        default: 'gaussian'
fitmode -- mode for fitting
        options: 'list' ('auto' and 'interact' will be available later)
        default: 'list'
        example: 'list' will use channel ranges specified in the parameter 
                        spw to fit for lines
                 'auto'  will use the linefinder to fit for lines
                        using the following parameters
                 'interact' allows adding and deleting mask 
                        regions by drawing rectangles on the plot 
                        with mouse. Draw a rectangle with LEFT-mouse 
                        to ADD the region to the mask and with RIGHT-mouse 
                        to DELETE the region. 
    >>> fitmode expandable parameters     
        nfit -- list of number of lines to fit in each region specified by the 
                parameter spw (only available in fitmode='list')
                default: [0] (no fitting)
                example: nfit=[1] for single line in single region,
                         nfit=[2] for two lines in single region,
                         nfit=[1,1] for single lines in each of two regions, etc.
        thresh -- S/N threshold for linefinder. a single channel S/N ratio
                  above which the channel is considered to be a detection.
                   (only available in fitmode='auto')
                default: 5
        avg_limit -- channel averaging for broad lines. a number of
                     consecutive channels not greater than this parameter
                     can be averaged to search for broad lines.
                    (only available in fitmode='auto')
                default: 4
        minwidth -- minimum number of consecutive channels required to
                    pass threshold
                    (only available in fitmode='auto')
                default: 4
        edge -- channels to drop at beginning and end of spectrum
                (only available in fitmode='auto')
                default: 0
                example: edge=[1000] drops 1000 channels at beginning AND end.
                         edge=[1000,500] drops 1000 from beginning and 500
                         from end

        Note: For bad baselines threshold should be increased,
        and avg_limit decreased (or even switched off completely by
        setting this parameter to 1) to avoid detecting baseline
        undulations instead of real lines.
outfile -- name of output file
        default: no output fit file
        example: 'mysd.fit'
overwrite -- overwrite the output file if already exists
        options: (bool) True, False
        default: False

-------
Returns
-------
a Python dictionary of line statistics
    keys: 'peak', 'cent', 'fwhm', 'nfit'
    example: each value except for 'nfit' is a list of lists with 
             a list of 2 entries [fitvalue,error] per component.
             e.g. xstat['peak']=[[234.9, 4.8],[234.2, 5.3]]
             for 2 components.

-----------
DESCRIPTION
-----------
Task sdfit is a basic line-fitter for single-dish spectra.
It assumes that the spectra have been calibrated in tsdcal
or sdreduce.

Note that multiple scans, IFs, and polarizations can in principle 
be handled, but we recommend that you use scan, field, spw, and pol
to give a single selection for each fit.

-------
POLARIZATION AVERAGE
-------
Two modes of polarization averaging are available. The default is 
'stokes' which is an average based on a formulation of Stokes 
parameter. In this mode, averaged data is calculated by 
(XX + YY) / 2 or (RR + LL) / 2. Other option is 'geometric', which 
is a conventional way of averaging in the field of single-dish 
data reduction. The averaged data is given by weighted average 
of XX and YY, or RR and LL. 

-------
FITMODE
-------
As described in the parameter description section, sdfit implements 
fitting modes 'list' and 'auto' so far. 
The 'list' mode allows users to set  initial guess manually. The only
controllable parameter for the guess is  range of the line region and
number of lines per region. In 'list' mode, users must give line 
region via spw parameter by using ms selection syntax while number of
lines per region can be specified via nfit parameter. For example,
 
    spw = '17:1500~2500'
    nfit = [1]

will set line region between channels 1500 and 2500 for spw 17, and
indicate that there is only one line in this region. Specifying single
region with multiple line is also possible but is not recommended.
In 'auto' mode, the line finder detects channel ranges of spectral lines
based on median absolute deviation (MAD) of the spectra using user defined
criteria, thres, avg_limit, minwidth, and edge. The number of channels
in both edges of spectra defined by edge parameter are ignored in line
detection. The median of lower 80% of MAD values in a spectrum is 
multiplied by thres parameter value to define a threshold of line 
detection. All channels with MAD above the threshold is detected as 
spectral line candidates and accepted as spectral lines only if the 
channel width of the line exceeds the value of minwidth parameter. The 
line detection is iteratively invoked for channel averaged spectra 
up to avg_limit.

  
        """
        if type(nfit)==int: nfit=[nfit]
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
        mytmp['timebin'] = timebin
        mytmp['timespan'] = timespan
        mytmp['polaverage'] = polaverage
        mytmp['fitfunc'] = fitfunc
        mytmp['fitmode'] = fitmode
        mytmp['nfit'] = nfit
        mytmp['thresh'] = thresh
        mytmp['avg_limit'] = avg_limit
        mytmp['minwidth'] = minwidth
        mytmp['edge'] = edge
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'sdfit.xml')

        casalog.origin('sdfit')
        if trec.has_key('sdfit') and casac.utils().verify(mytmp, trec['sdfit']) :
            result = task_sdfit.sdfit(infile, datacolumn, antenna, field, spw, timerange, scan, pol, intent, timebin, timespan, polaverage, fitfunc, fitmode, nfit, thresh, avg_limit, minwidth, edge, outfile, overwrite)

        else :
          result = False
        return result
