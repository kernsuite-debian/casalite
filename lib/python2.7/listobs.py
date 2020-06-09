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
import task_listobs
def listobs(vis='', selectdata=True, spw='', field='', antenna='', uvrange='', timerange='', correlation='', scan='', intent='', feed='', array='', observation='', verbose=True, listfile='', listunfl=False, cachesize=50, overwrite=False):

        """List the summary of a data set in the logger or in a file

       List the summary information of a data set in the logger or in a file, based on
       a data selection. Only rows can be selected and printed. No in-row selection is
       possible (channel or correlation). Refer to the task listvis to list visibilites.

       Lists the following properties of a measurement set:
       scan list, field list, spectral window list with
       correlators, antenna locations, ms table information.

       Keyword arguments:
       vis -- Name of input visibility file
               default: none. example: vis='ngc5921.ms'
       
       selectdata -- Select a subset of data for flagging
                    default: False
                    options: True,False
                    The summary listing will only apply to the specified selection.

              antenna -- Select data based on baseline
                    default: '' (all); example: antenna='5&6' baseline 5-6
                    antenna='5&6;7&8' #baseline 5-6 and 7-8
                    antenna='5' # all cross-correlation baselines between antenna 5 and all other available
                                  antennas
                    antenna='5,6' # all baselines with antennas 5 and 6
                    antenna='1&&1' # only the auto-correlation baselines for antenna 1
                    antenna='1&&*' # cross and auto-correlation baselines between antenna 1
                                             and all other available antennas
                    antenna='1~7&&&' # only the auto-correlation baselines for antennas in range 1~7
              spw -- Select data based on spectral window and channels
                    default: '' (all); example: spw='1'
                    spw='<2' #spectral windows less than 2
                    spw='>1' #spectral windows greater than 1
              correlation -- Correlation types
                    default: '' (all);
                    example: correlation='RR LL'
              field -- Select data based on field id(s) or name(s)
                    default: '' (all); example: field='1'
                    field='0~2' # field ids inclusive from 0 to 2
                    field='3C*' # all field names starting with 3C
              uvrange -- Select data within uvrange (default units meters)
                    default: '' (all); example:
                    uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lamgda
                    uvrange='>4klamda';uvranges greater than 4 kilo-lambda
                    uvrange='0~1000km'; uvrange in kilometers
              timerange  -- Select data based on time range:
                    default = '' (all); example,
                    timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                    Note: YYYY/MM/DD can be dropped as needed:
                    timerange='09:14:0~09:54:0' # this time range
                    timerange='09:44:00' # data within one integration of time
                    timerange='>10:24:00' # data after this time
                    timerange='09:44:00+00:13:00' #data 13 minutes after time
              scan -- Select data based on scan number
                    default: '' (all); example: scan='>3'
              intent -- Select data based on observation intent
                    default: '' (all); example: intent='*CAL*,*BAND*'
              feed -- Selection based on the feed - NOT IMPLEMENTED YET
              array -- Selection based on the antenna array
              observation -- Selection based on the observation ID
                    default: '' (all); example: observation='1' or observation=1


       verbose -- level of detail
             verbose=True: (default); scan and antenna lists
             verbose=False: less information
             
       listfile -- name of disk file to write output.
               default: None. Example: listfile='list.txt'
               
       listunfl -- List unflagged row counts? If true, it can have significant negative performance impact.
 
       cachesize -- maximum size of the memory cache in megabytes in which data structures can be
                    stored. For very large datasets this can be increased for possibly better performance.
                    THIS IS ONLY EXPERIEMENTAL FOR NOW, AND INCREASING THE VALUE OF THIS PARAMETER DOES NOT GUARANTEE INCREASED
                    SPEED. DEPENDING ON ITS (LACK OF) USEFULNESS, IT MAY BE REMOVED IN THE FUTURE.


      The 'Int (s)' column is the average of the MS's INTERVAL column
      for each scan, so in a time-averaged MS 'Int' = 9.83s more likely
      means 5 10s integrations and 1 9s integration (timebin) than 6
      9.83s integrations. 
      
    DESCRIPTION OF ALGORITHM TO CALCULATE THE NUMBER OF UNFLAGGED ROWS
    The number of unflagged rows are only computed if listunfl=True. Computing these quantity
    can have a negative performance impact, especially for large datasets.
    The number of unflagged rows (the nUnflRows columns in the scans and fields portions of the listing) is
    calculated by summing the fractional unflagged bandwidth for each row (and hence why the number of unflagged
    rows, in general, is not an integer). Thus a row which has half of its
    total bandwidth flagged contributes 0.5 rows to the unflagged row count. A row with 20 of 32 channels of
    homogeneous width contributes 20/32 = 0.625 rows to the unflagged row count. A row with a value of False
    in the FLAG_ROW column is not counted in the number of unflagged rows.
 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['selectdata'] = selectdata
        mytmp['spw'] = spw
        mytmp['field'] = field
        mytmp['antenna'] = antenna
        mytmp['uvrange'] = uvrange
        mytmp['timerange'] = timerange
        mytmp['correlation'] = correlation
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['feed'] = feed
        mytmp['array'] = array
        mytmp['observation'] = observation
        mytmp['verbose'] = verbose
        mytmp['listfile'] = listfile
        mytmp['listunfl'] = listunfl
        mytmp['cachesize'] = cachesize
        mytmp['overwrite'] = overwrite
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'listobs.xml')

        casalog.origin('listobs')
        if trec.has_key('listobs') and casac.utils().verify(mytmp, trec['listobs']) :
            result = task_listobs.listobs(vis, selectdata, spw, field, antenna, uvrange, timerange, correlation, scan, intent, feed, array, observation, verbose, listfile, listunfl, cachesize, overwrite)

        else :
          result = False
        return result
