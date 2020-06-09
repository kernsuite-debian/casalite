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
import task_uvsub
def uvsub(vis='', reverse=False):

        """Subtract/add model from/to the corrected visibility data.
        Help for uvsub task

        This function subtracts model visibility data from corrected visibility
        data leaving the residuals in the corrected data column.  If the
        parameter 'reverse' is set true, the process is reversed.
        Please note the model visibility used is the one that has been saved in the MODEL_DATA of the MS and the 
        CORRECTED_DATA column is the one that is modified. If no CORRECTED_DATA column exists in the MS, one will be created and 
        a copy of the DATA column is saved in it  before the uvsub operation selected is performed. uvsub does not modify the DATA column.

        Keyword arguments:
        vis -- Name of input visibility file (MS)
                default: none; example: vis='ngc5921.ms'
        reverse -- Reverse the operation (add rather than subtract)
                default: False; example: reverse=true

        uvsub(vis='ngc5921.ms', reverse=False)

 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['reverse'] = reverse
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'uvsub.xml')

        casalog.origin('uvsub')
        if trec.has_key('uvsub') and casac.utils().verify(mytmp, trec['uvsub']) :
            result = task_uvsub.uvsub(vis, reverse)

        else :
          result = False
        return result
