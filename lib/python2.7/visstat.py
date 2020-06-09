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
import task_visstat
def visstat(vis='', axis='amplitude', datacolumn='data', useflags=True, spw='', field='', selectdata=True, antenna='', uvrange='', timerange='', correlation='', scan='', array='', observation='', timeaverage=False, timebin='0s', timespan='', maxuvwdistance=0.0, disableparallel=False, ddistart=-1, taql='', monolithic_processing=False, intent='', reportingaxes='ddid'):

        """Displays statistical information from a MeasurementSet, or from a Multi-MS

      This task returns statistical information about data in a MeasurementSet
      or Multi-MS.

      The following statistics are computed: mean value, sum of values, sum of
      squared values, median, median absolute deviation, first and third
      quartiles, minimum, maximum, variance, standard deviation, and root mean
      square.

      Statistics may be computed on any of the following values: flag, antenna1,
      antenna2, feed1, feed2, field_id, array_id, data_desc_id, flag_row,
      interval, scan_number, time, weight_spectrum, amplitude, phase, real,
      imaginary, and uvrange (for the 'axis' parameter value, 'amp' is treated
      as an alias for amplitude, as are 'imag' for imaginary, and 'scan' for
      scan_number.)

      The 'reportingaxes' argument is used to partition the sample set along an
      axis. For example, setting its value to 'ddid' will result in the
      statistics of the chosen sample values partitioned by unique values of the
      data description id. Thus setting 'axis' to 'amp' and 'reportingaxes' to
      'ddid' will report statistics of visibility amplitudes for each unique
      value of data description id in the MeasurementSet.

      Optionally, the statistical information can be computed based only
      on a given subset of the MeasurementSet.

      Note: If the MS consists of inhomogeneous data, for example several
      spectral windows each having a different number of channels, it may be
      necessary to use selection parameters to select a homogeneous subset of
      the MS, e.g. spw='2'.

      Keyword arguments:

            vis  --- Name of input MeasurementSet or Multi-MS
                  default: '', example: vis='my.ms'

            axis -- Which data to analyze.

                  default: 'amplitude'
                  axis='phase'
                  axis='imag'
                  axis='scan_number'
                  axis='flag'

                  The phase of a complex number is in radians in the range [-pi; pi].


            datacolumn -- Which data column to use for complex data.
                  default: 'data'
                  datacolumn='data'
                  datacolumn='corrected'
                  datacolumn='model'
                  datacolumn='float_data'

            useflags -- Take MS flags into account?
                  default: True
                  useflags=False
                  useflags=True
                  If useflags=False, flagged values are included in the statistics.
                  If useflags=True, any flagged values are not used in the statistics.

            spw -- Select data based on spectral window and channels
                  default: '' (all); example: spw='1'
                  spw='<2' #spectral windows less than 2
                  spw='>1' #spectral windows greater than 1
                  spw='0:0~10' # first 10 channels from spw 0
                  spw='0:0~5;56~60' # multiple separated channel chunks.

            field -- Select data based on field id(s) or name(s)
                  default: '' (all); example: field='1'
                  field='0~2' # field ids inclusive from 0 to 2
                  field='3C*' # all field names starting with 3C

            selectdata -- Other data selection parameters
                  default: True
            antenna -- Select data based on baseline
                  default: '' (all); example: antenna='5&6' baseline 5-6
                  antenna='5&6;7&8' #baseline 5-6 and 7-8
                  antenna='5' # all baselines with antenna 5
                  antenna='5,6' # all baselines with antennas 5 and 6
            correlation -- Correlation types
                  default: '' (all);
                  example: correlation='RR LL'
            uvrange -- Select data within uvrange (default units meters)
                  default: '' (all); example:
                  uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                  uvrange='>4klambda';uvranges greater than 4 kilo-lambda
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
            array -- Selection based on the antenna array
                  observation -- Selection by observation ID(s).
                  default: '' (all); example: observation='1~3'




            --- Time averaging parameters ---
            timeaverage -- Average data in time. Flagged data will be included in the
            average calculation, unless the parameter useflags is set to True. In this
            case only partially flagged rows will be used in the average.
            default: False

            timebin -- Bin width for time averaging.
                  default: '0s'

            timespan -- Let the timebin span across scan, state or both.
                        State is equivalent to sub-scans. One scan may have several
                        state ids. For ALMA MSs, the sub-scans are limited to about
                        30s duration each. In these cases, the task will automatically
                        add state to the timespan parameter. To see the number of states
                        in an MS, use the msmd tool. See help msmd.

                  default: '' (separate time bins by both of the above)
                  options: 'scan', 'state', 'state,scan'

                  examples:
                        timespan = 'scan'; can be useful when the scan number
                        goes up with each integration as in many WSRT MSs.
                        timespan = ['scan', 'state']: disregard scan and state
                        numbers when time averaging.
                        timespan = 'state,scan'; same as above.

            maxuvwdistance -- Provide a maximum separation of start-to-end baselines
                              that can be included in an average. (int)
                  default: 0.0 (given in meters)







        
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['axis'] = axis
        mytmp['datacolumn'] = datacolumn
        mytmp['useflags'] = useflags
        mytmp['spw'] = spw
        mytmp['field'] = field
        mytmp['selectdata'] = selectdata
        mytmp['antenna'] = antenna
        mytmp['uvrange'] = uvrange
        mytmp['timerange'] = timerange
        mytmp['correlation'] = correlation
        mytmp['scan'] = scan
        mytmp['array'] = array
        mytmp['observation'] = observation
        mytmp['timeaverage'] = timeaverage
        mytmp['timebin'] = timebin
        mytmp['timespan'] = timespan
        mytmp['maxuvwdistance'] = maxuvwdistance
        mytmp['disableparallel'] = disableparallel
        mytmp['ddistart'] = ddistart
        mytmp['taql'] = taql
        mytmp['monolithic_processing'] = monolithic_processing
        mytmp['intent'] = intent
        mytmp['reportingaxes'] = reportingaxes
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'visstat.xml')

        casalog.origin('visstat')
        if trec.has_key('visstat') and casac.utils().verify(mytmp, trec['visstat']) :
            result = task_visstat.visstat(vis, axis, datacolumn, useflags, spw, field, selectdata, antenna, uvrange, timerange, correlation, scan, array, observation, timeaverage, timebin, timespan, maxuvwdistance, disableparallel, ddistart, taql, monolithic_processing, intent, reportingaxes)

        else :
          result = False
        return result
