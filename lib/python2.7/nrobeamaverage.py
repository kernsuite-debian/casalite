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
import task_nrobeamaverage
def nrobeamaverage(infile='', datacolumn='float_data', field='', spw='', timerange='', scan='', beam='', timebin='0s', outfile=''):

        """Average SD data over beams and do time averaging  
-----------------
Keyword arguments
-----------------
infile -- name of input SD dataset
datacolumn -- name of data column to be used
        options: 'data', 'float_data', or 'corrected_data'
        default: 'float_data'
field -- select data by field IDs and names
        default: '' (use all fields)
        example: field='3C2*' (all names starting with 3C2)
                 field='0,4,5~7' (field IDs 0,4,5,6,7)
                 field='0,3C273' (field ID 0 or field named 3C273)
        this selection is in addition to the other selections to data
spw -- select data by IF IDs (spectral windows)
        default: '' (use all IFs)
        example: spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                 spw='<2';  spectral windows less than 2 (i.e. 0,1)
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
beam -- beam IDs to be averaged over
        default: '' (all beam IDs)
        example: beam='1,3' (beam IDs 1 and 3)
                 NOTE: beam IDs of averaged spectra in the output file will 
                       be the smallest one, e.g., in case of beam='1,3', 
                       the averaged output spectra will have beam ID 1.
                       Note also that beam IDs should be stored in the 
                       ANTENNA column of input MS.
timebin -- bin width for time averaging
           default: '' (only beam IDs changed, no time averaging)
outfile -- name of output file


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['datacolumn'] = datacolumn
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['timerange'] = timerange
        mytmp['scan'] = scan
        mytmp['beam'] = beam
        mytmp['timebin'] = timebin
        mytmp['outfile'] = outfile
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'nrobeamaverage.xml')

        casalog.origin('nrobeamaverage')
        if trec.has_key('nrobeamaverage') and casac.utils().verify(mytmp, trec['nrobeamaverage']) :
            result = task_nrobeamaverage.nrobeamaverage(infile, datacolumn, field, spw, timerange, scan, beam, timebin, outfile)

        else :
          result = False
        return result
