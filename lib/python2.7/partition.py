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
import task_partition
def partition(vis='', outputvis='', createmms=True, separationaxis='auto', numsubms='auto', flagbackup=True, datacolumn='all', field='', spw='', scan='', antenna='', correlation='', timerange='', intent='', array='', uvrange='', observation='', feed='', disableparallel=False, ddistart=-1, taql=''):

        """Task to produce Multi-MSs using parallelism


----- Detailed description of keyword arguments -----
    
    vis -- Name of input visibility file
        default: none; example: vis='ngc5921.ms'

    outputvis -- Name of output visibility file
        default: none; example: outputvis='ngc5921.mms'

    createmms -- Create a multi-MS as the output.
        default: True
        If False, it will work like the split task and create a
        normal MS, split according to the given data selection parameters.
        Note that, when this parameter is set to False, a cluster
        will not be used.

        separationaxis -- Axis to do parallelization across. 
            default: 'auto'
            Options: 'scan', 'spw', 'baseline', 'auto'

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

                Example: Launch CASA with 5 engines, where 4 of them will be used to create the MMS. The first
                    engine is used as the MPIClient.
      
                mpicasa -n 5 casa --nogui --log2term
                CASA> partition('uid__A1', outputvis='test.mms')

        flagbackup -- Make a backup of the FLAG column of the output MMS. When the
                      MMS is created, the .flagversions of the input MS are not transferred,
                      therefore it is necessary to re-create it for the new MMS. Note
                      that multiple backups from the input MS will not be preserved. This
                      will create a single backup of all the flags present in the input
                      MS at the time the MMS is created.
            default: True

    datacolumn -- Which data column to use when partitioning the MS.
        default='all'; example: datacolumn='data'
        Options: 'data', 'model', 'corrected', 'all',
                'float_data', 'lag_data', 'float_data,data', and
                'lag_data,data'.
            N.B.: 'all' = whichever of the above that are present.

---- Data selection parameters (see help par.selectdata for more detailed
    information)

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
           spw = '*:0;60~63'  channel 0 and channels 60 to 63 for all IFs 
                  ';' needed to separate different channel ranges in one spw
           spw='0:0~10;15~60'; spectral window 0 with channels 0-10,15-60
           spw='0:0~10,1:20~30,2:1;2;4'; spw 0, channels 0-10,
                    spw 1, channels 20-30, and spw 2, channels, 1, 2 and 4

    antenna -- Select data based on antenna/baseline
        default: '' (all)
            Non-negative integers are assumed to be antenna indices, and
            anything else is taken as an antenna name.

            Examples:
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

    timerange -- Select data based on time range:
        default = '' (all); examples,
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

    scan -- Scan number range
        default: ''=all

    observation -- Select by observation ID(s)
        default: ''=all


------ EXAMPLES ------

1) Create a Multi-MS of some spws, partitioned per spw. The MS contains 16 spws.
    partition('uid001.ms', outpuvis='source.mms', spw='1,3~10', separationaxis='spw')

2) Create a Multi-MS but select only the first channels of all spws. Do not back up the FLAG
column.
    partition('uid0001.ms', outputvis='fechans.mms', spw='*:1~10', flagbackup=False)

3) Create a Multi-MS using both separation axes.
    partition('uid0001.ms', outputvis='myuid.mms', createmms=True, separationaxis='auto')

4) Create a single-dish Multi-MS using the baseline axis only for the auto-correlations.
    partition('uid0001.ms', outputvis='myuid.mms', createmms=True, separationaxis='baseline', antenna='*&&&')



        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['outputvis'] = outputvis
        mytmp['createmms'] = createmms
        mytmp['separationaxis'] = separationaxis
        mytmp['numsubms'] = numsubms
        mytmp['flagbackup'] = flagbackup
        mytmp['datacolumn'] = datacolumn
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
        mytmp['disableparallel'] = disableparallel
        mytmp['ddistart'] = ddistart
        mytmp['taql'] = taql
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'partition.xml')

        casalog.origin('partition')
        if trec.has_key('partition') and casac.utils().verify(mytmp, trec['partition']) :
            result = task_partition.partition(vis, outputvis, createmms, separationaxis, numsubms, flagbackup, datacolumn, field, spw, scan, antenna, correlation, timerange, intent, array, uvrange, observation, feed, disableparallel, ddistart, taql)

        else :
          result = False
        return result
