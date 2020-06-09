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
import task_listvis
def listvis(vis='', options='ap', datacolumn='data', field='', spw='*', selectdata=False, antenna='', timerange='', correlation='', scan='', feed='', array='', observation='', uvrange='', average='', showflags=False, pagerows=50, listfile=''):

        """List measurement set visibilities.

This task lists measurement set visibility data under a number of
input selection conditions.  The measurement set data columns that
can be listed are: the raw data, float_data, corrected data, model data,
and residual (corrected - model) data.

The output table format is dynamic.  Field, Spectral Window, and
Channel columns are not displayed if the column contents are uniform.
For example, if "spw = '1'" is specified, the spw column will not be
displayed.  When a column is not displayed, a message is sent to the
logger and terminal indicating that the column values are uniform and
listing the uniform value.

Table column descriptions:

COLUMN NAME       DESCRIPTION
-----------       -----------
Date/Time         Time stamp of data sample (YYMMDD/HH:MM:SS UT)
Intrf             Interferometer baseline (antenna names)
UVDist            uv-distance (units of wavelength)
Fld               Field ID (if more than 1)
SpW               Spectral Window ID (if more than 1)
Chn               Channel number (if more than 1)
(Correlated       Correlated polarizations (eg: RR, LL, XY)
  polarization)     Sub-columns are: Amp, Phs, Wt, F
Amp               Visibility amplitude
Phs               Visibility phase (deg)
Wt                Weight of visibility measurement
F                 Flag: 'F' = flagged datum; ' ' = unflagged
UVW               UVW coordinates (meters)


Input Parameters:
vis         Name of input visibility file
            default: none; example: vis='ngc5921.ms'

options     List options: default = 'ap'
            Not yet implemented for suboptions

datacolumn  Visibility file data column:
            default = 'data':  options are
            data, float_data, corrected, model, residual (corrected-model)

field       Select data based on field id(s) or name(s)
            default: ''==>all; example: field='1'
            field='0~2' field ids inclusive from 0 to 2
            field='3C*' all field names starting with 3C

spw         Select spectral window, channel to list
            default: '0:0' --> spw=0, chan=0
            spw='2:34' spectral window 2, channel 34

selectdata  Toggle the following 7 selection parameters.
            default: False; example: selectdata=True
            If false, the following parameters are reset
            to default values.

      antenna     Select calibration data based on antenna
                  default: ''-->all; examples:
                  antenna = '5,6'; antenna index 5 and 6 solutions
                  antenna = '05,06'; antenna names '05' and '06 solutions

      timerange   Select time range to list
                  default: ''-->all; examples:
                  timerange='10:37:50.1'; list data for this sampling interval
                  timerange='<10:37:25'; list data before 10:37:25

      correlation Select polarization correlations to list
                  default: ''-->all; examples:
                  correlation='RR LL'; list RR and LL correlations
                  correlation='XX XY'; list XX and XY correlations

      scan        Select scans to list
                  default: ''-->all; examples:
                  scan='2'; list scan 2
                  scan='>2'; list scan numbers greater than 2

      feed        (not yet implemented)

      array       (not yet implemented)

      observation Select by observation ID(s).
                  default: ''-->all;
                  example: observation='0' (select obsID 0)

      uvrange     Select baseline lengths to list.
                  default: ''--> all; examples:
                  uvrange='<5klambda'; less than 5 kilo-wavelengths
                  Caution: Input units default to meters.
                  Listed units are always wavelengths.

average     (not yet implemented)

showflags   (not yet implemented)

pagerows    rows per page of listing
            default: 50; 0 --> do not paginate

listfile    write output to disk; will not overwrite
            default: '' --> write to screen
            listfile = 'solutions.txt'

async       Run asynchronously
            default = False; do not run asychronously

   
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['options'] = options
        mytmp['datacolumn'] = datacolumn
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['selectdata'] = selectdata
        mytmp['antenna'] = antenna
        mytmp['timerange'] = timerange
        mytmp['correlation'] = correlation
        mytmp['scan'] = scan
        mytmp['feed'] = feed
        mytmp['array'] = array
        mytmp['observation'] = observation
        mytmp['uvrange'] = uvrange
        mytmp['average'] = average
        mytmp['showflags'] = showflags
        mytmp['pagerows'] = pagerows
        mytmp['listfile'] = listfile
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'listvis.xml')

        casalog.origin('listvis')
        if trec.has_key('listvis') and casac.utils().verify(mytmp, trec['listvis']) :
            result = task_listvis.listvis(vis, options, datacolumn, field, spw, selectdata, antenna, timerange, correlation, scan, feed, array, observation, uvrange, average, showflags, pagerows, listfile)

        else :
          result = False
        return result
