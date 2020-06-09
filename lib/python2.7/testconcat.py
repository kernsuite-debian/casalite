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
import task_testconcat
def testconcat(vis=[''], testconcatvis='', freqtol='', dirtol='', copypointing=True):

        """Concatenate the subtables of several visibility data sets, not the MAIN bulk data.

The list of data sets given in the vis argument are concatenated into an output
data set in testconcatvis without the bulk data of the MAIN table.  
This is useful for obtaining the information in the merged subtables without
actually performing a time-consuming concatenation of the MAIN tables on disk.


Keyword arguments:
vis -- Name of input visibility files for which the subtables are to be combined
        default: none; example: vis = 'mydata.ms',
             vis=['src2.ms','ngc5921.ms','ngc315.ms']
testconcatvis -- Name of MS that will contain the concatenated subtables
        default: none; example: testconcatvis='test.ms'

freqtol -- Frequency shift tolerance for considering data to be in the same
           spwid.  The number of channels must also be the same.
        default: ''  do not combine unless frequencies are equal
        example: freqtol='10MHz' will not combine spwid unless they are
           within 10 MHz.
        Note: This option is useful to conbine spectral windows with very slight
           frequency differences caused by Doppler tracking, for example.

dirtol -- Direction shift tolerance for considering data as the same field
        default: '' means always combine.
        example: dirtol='1.arcsec' will not combine data for a field unless
           their phase center differ by less than 1 arcsec.  If the field names
           are different in the input data sets, the name in the output data
           set will be the first relevant data set in the list.

copypointing -- Make a proper copy of the POINTING subtable (can be time consuming).
                If False, the result is an empty POINTING table.
         default: True


        """
        if type(vis)==str: vis=[vis]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['testconcatvis'] = testconcatvis
        mytmp['freqtol'] = freqtol
        mytmp['dirtol'] = dirtol
        mytmp['copypointing'] = copypointing
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'testconcat.xml')

        casalog.origin('testconcat')
        if trec.has_key('testconcat') and casac.utils().verify(mytmp, trec['testconcat']) :
            result = task_testconcat.testconcat(vis, testconcatvis, freqtol, dirtol, copypointing)

        else :
          result = False
        return result
