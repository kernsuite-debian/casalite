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
import task_listpartition
def listpartition(vis='', createdict=False, listfile=''):

        """List the summary of a multi-MS data set in the logger or in a file

       A multi-measurement set (MMS) is an MS that has been split into sub-MSs.
       An MMS contains a reference MS in the top directory and the sub-MSs are 
       located in a directory called SUBMSS inside the MMS directory.
       Example of a MS that was partitioned in the 'scan' axis using the task partition: 

       > ls ngc5921.mms
         ANTENNA           FLAG_CMD     POLARIZATION  SPECTRAL_WINDOW  table.dat
         DATA_DESCRIPTION  HISTORY      PROCESSOR     STATE            table.info
         FEED              OBSERVATION  SORTED_TABLE  SUBMSS           WEATHER
         FIELD             POINTING     SOURCE        SYSCAL

       > ls ngc5921.mms/SUBMSS/
         ngc5921.0000.ms/  ngc5921.0002.ms/  ngc5921.0004.ms/  ngc5921.0006.ms/
         ngc5921.0001.ms/  ngc5921.0003.ms/  ngc5921.0005.ms/
              
       The task lists the following properties of a multi-MS or MS:
       sub-MS name, scan, spw list, list of number of channels per spw, 
       number of rows for each scan and the size in disk. Example of logger output:
       
        Sub-MS          Scan  Spw      Nchan    Nrows   Size  
        ngc5921.0000.ms  1    [0]      [63]     4509    11M
        ngc5921.0001.ms  2    [0]      [63]     1890    6.4M
        ngc5921.0002.ms  3    [0]      [63]     6048    13M
        ngc5921.0003.ms  4    [0]      [63]     756     4.9M
        ngc5921.0004.ms  5    [0]      [63]     1134    6.4M
        ngc5921.0005.ms  6    [0]      [63]     6804    15M
        ngc5921.0006.ms  7    [0]      [63]     1512    6.4M


------- Detailed description of keyword arguments -------
       vis -- Name of multi-MS or normal MS.
              default: ''. 
              example: vis='pScan.mms'

       createdict -- Create and return a dictionary containing scan summaries of each
                     sub-MS. 
              default: False
              
              If set to True, the returned dictionary will contain information from
              ms.getscansummary() and ms.getspectralwindowinfo(), with the addition of an 
              index as the top key and the sub-MS name.
              Example:
              
            {0: {'MS': 'ngc5921.0000.ms',
                 'scanId': {1: {'nchans': array([63], dtype=int32),
                                'nrows': 4509,
                                'spwIds': array([0], dtype=int32)}},
                 'size': '11M'},
             1: {'MS': 'ngc5921.0001.ms',
                 'scanId': {2: {'nchans': array([63], dtype=int32),
                                'nrows': 1890,
                                'spwIds': array([0], dtype=int32)}},
                 'size': '6.4M'}}
                    
       listfile -- Name of ASCII file to save output to. If empty, it will 
                   list on the logger/terminal.
              default: ''
              example: listfile='pscan.txt'

 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['createdict'] = createdict
        mytmp['listfile'] = listfile
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'listpartition.xml')

        casalog.origin('listpartition')
        if trec.has_key('listpartition') and casac.utils().verify(mytmp, trec['listpartition']) :
            result = task_listpartition.listpartition(vis, createdict, listfile)

        else :
          result = False
        return result
