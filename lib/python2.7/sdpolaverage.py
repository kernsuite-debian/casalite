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
import task_sdpolaverage
def sdpolaverage(infile='', datacolumn='data', antenna='', field='', spw='', timerange='', scan='', intent='', polaverage='', outfile=''):

        """Average SD spectra over polarisation  
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
        example: spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                 spw='<2';  spectral windows less than 2 (i.e. 0,1)
                 spw='0:5~61'; spw 0, channels 5 to 61
                 spw='0,10,3:3~45'; spw 0,10 all channels, spw 3 - chans 3 to 45.
                 spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
                 spw = '*:3~64'  channels 3 through 64 for all sp id's
                 spw = ' :3~64' will NOT work.

                 NOTE: sdpolaverage does not support multiple channel ranges 
                       per spectral window (';') just like mstransform doesn't.
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
intent -- select data by observational intent, also referred to as 'scan intent'
        default: '' (use all scan intents)
        example: intent='*ON_SOURCE*' (any valid scan-intent expression accepted by the MSSelection module can be specified)
        this selection is in addition to the other selections to data
polaverage -- polarization averaging mode
        default: '' (no averaging over polarization)
        options: '', 'stokes', 'geometric'
outfile -- name of output file


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
        mytmp['intent'] = intent
        mytmp['polaverage'] = polaverage
        mytmp['outfile'] = outfile
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'sdpolaverage.xml')

        casalog.origin('sdpolaverage')
        if trec.has_key('sdpolaverage') and casac.utils().verify(mytmp, trec['sdpolaverage']) :
            result = task_sdpolaverage.sdpolaverage(infile, datacolumn, antenna, field, spw, timerange, scan, intent, polaverage, outfile)

        else :
          result = False
        return result
