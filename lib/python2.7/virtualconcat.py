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
import task_virtualconcat
def virtualconcat(vis=[''], concatvis='', freqtol='', dirtol='', respectname=True, visweightscale=[], keepcopy=False, copypointing=True):

        """Concatenate several visibility data sets into a multi-MS

The list of data sets given in the vis argument are moved into an output
multi-MS data set concatvis and virtually concatenated. 

NOTE: This task will modify the input datasets by moving them and reindexing them.
If you want to keep a copy of your original data, please set the parameter 
keepcopy to True.

There is no limit to the number of input data sets.

If none of the input data sets have any scratch columns (model and corrected
columns), none are created in the concatvis.  Otherwise these columns are
created on output and initialized to their default value (1 in model column,
data in corrected column) for those data with no input columns.

Spectral windows for each data set with the same chanelization, and within a
specified frequency tolerance of another data set will be combined into one
spectral window.

A field position in one data set that is within a specified direction tolerance
of another field position in any other data set will be combined into one
field.  The field names need not be the same---only their position is used.

Each appended dataset is assigned a new observation id if the corresponding
rows in the observation table are not the same.

Keyword arguments:
vis -- Name of input visibility files to be combined
        default: none; example: vis = ['src2.ms','ngc5921.ms','ngc315.ms']
concatvis -- Name of visibility file that will contain the concatenated data
        note: if this file exits on disk then the input files are 
              added to this file.  Otherwise the new file contains  
              the concatenated data.  Be careful here when concatenating to
              an existing file.
        default: none; example: concatvis='src2.ms'
                 example: concatvis='outvis.ms'

        other examples: 
           virtualconcat(vis=['src2.ms','ngc5921.ms'], concatvis='out.mms') 
               will concatenate 'ngc5921.ms' and 'src2.ms' into a file named 
               'out.mms'; the original 'ngc5921.ms' and 'src2.ms' are gone.
               'out.mms' is a multims. As most of the data is only moved, not 
               copied, this is faster and subsequent tasks can run in parallel
               on the subMSs of out.mms.
           virtualconcat(vis=['src2.ms','ngc5921.ms'], concatvis='out.mms', keepcopy=True) 
               will concatenate 'ngc5921.ms' and 'src2.ms' into a file named 
               'out.mms'; the original 'ngc5921.ms' and 'src2.ms' are as before
               but you consume more disk space and time for the copy.
               .

     Note: run flagmanager to save flags in the concatvis

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

respectname -- If true, fields with a different name are not merged even if their 
        direction agrees (within dirtol). 
        default: True

visweightscale -- The weights of the individual MSs will be scaled in the concatenated
        output MS by the factors in this list. Useful for handling heterogeneous arrays.
        Use plotms to inspect the "Wt" column as a reference for determining the scaling 
        factors. See the cookbook for more details.
        example: [1.,3.,3.] - scale the weights of the second and third MS by a factor 3.
        default: [] (empty list) - no scaling

keepcopy -- If true, a copy of the input MSs is kept in their original place.
        default: false

copypointing -- If true, the POINTING table information will be present in the output.
                If false, the result is an empty POINTING table.
         default: true


        """
        if type(vis)==str: vis=[vis]
        if type(visweightscale)==float: visweightscale=[visweightscale]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['concatvis'] = concatvis
        mytmp['freqtol'] = freqtol
        mytmp['dirtol'] = dirtol
        mytmp['respectname'] = respectname
        mytmp['visweightscale'] = visweightscale
        mytmp['keepcopy'] = keepcopy
        mytmp['copypointing'] = copypointing
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'virtualconcat.xml')

        casalog.origin('virtualconcat')
        if trec.has_key('virtualconcat') and casac.utils().verify(mytmp, trec['virtualconcat']) :
            result = task_virtualconcat.virtualconcat(vis, concatvis, freqtol, dirtol, respectname, visweightscale, keepcopy, copypointing)

        else :
          result = False
        return result
