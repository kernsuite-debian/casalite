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
import task_sdsmooth
def sdsmooth(infile='', datacolumn='data', antenna='', field='', spw='', timerange='', scan='', pol='', intent='', reindex=True, kernel='gaussian', kwidth=5, outfile='', overwrite=False):

        """Smooth spectral data 
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
spw -- select data by spectral window IDs/channels
        default: '' (use all spws and channels)
        example: spw='3,5,7' (spw IDs 3,5,7; all channels)
                 spw='<2' (spw IDs less than 2, i.e., 0,1; all channels)
                 spw='30~45GHz' (spw IDs with the center frequencies in range 30-45GHz; all channels)
                 spw='0:5~61' (spw ID 0; channels 5 to 61; all channels)
                 spw='3:10~20;50~60' (select multiple channel ranges within spw ID 3)
                 spw='3:10~20,4:0~30' (select different channel ranges for spw IDs 3 and 4)
                 spw='1~4;6:15~48' (for channels 15 through 48 for spw IDs 1,2,3,4 and 6)
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
        example: pol='0,1' (polarization IDs 0,1)
        this selection is in addition to the other selections to data
intent -- select data by observational intent, also referred to as 'scan intent'
        default: '' (use all scan intents)
        example: intent='*ON_SOURCE*' (any valid scan-intent expression accepted by the MSSelection module can be specified)
        this selection is in addition to the other selections to data
reindex -- Re-index indices in subtables based on data selection.
           If True, DATA_DESCRIPTION, FEED, SPECTRAL_WINDOW, STATE, and SOURCE
           subtables are filtered based on data selection and re-indexed in output MS.
           default: True
kernel -- type of spectral smoothing kernel
        options: 'gaussian', 'boxcar'
        default: 'gaussian' (no smoothing)

    >>>kernel expandable parameter
        kwidth -- width of spectral smoothing kernel
                options: (int) in channels 
                default: 5
outfile -- name of output file
        default: '' (<infile>_bs)
overwrite -- overwrite the output file if already exists
        options: (bool) True, False
        default: False
        NOTE this parameter is ignored when outform='ASCII'


-----------
DESCRIPTION
-----------
Task sdsmooth performs smoothing along spectral axis using user-specified 
smoothing kernel. Currently gaussian and boxcar kernels are supported.


  
        """

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
        mytmp['kernel'] = kernel
        mytmp['kwidth'] = kwidth
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'sdsmooth.xml')

        casalog.origin('sdsmooth')
        if trec.has_key('sdsmooth') and casac.utils().verify(mytmp, trec['sdsmooth']) :
            result = task_sdsmooth.sdsmooth(infile, datacolumn, antenna, field, spw, timerange, scan, pol, intent, reindex, kernel, kwidth, outfile, overwrite)

        else :
          result = False
        return result
