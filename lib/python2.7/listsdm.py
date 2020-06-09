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
import task_listsdm
def listsdm(sdm=''):

        """Lists observation information present in an SDM directory.

        The listsdm task reads SDM XML tables, processes the
        observation information contained therein, and prints this
        information to the CASA log.  It will also return a dictionary
        keyed on scan number.  The dictionary contains the following
        information:

        'baseband'   list of baseband name(s)
        'chanwidth'  list of channel widths (Hz)
        'end'        observation end time (UTC)
        'field'      field ID
        'intent'     scan intent(s)
        'nchan'      list of number of channels
        'nsubs'      number of subscans
        'reffreq'    list of reference frequencies (Hz)
        'source'     source name
        'spws'       list of spectral windows
        'start'      observation start time (UTC)
        'timerange'  start time - end time range (UTC)

        Example:

        myscans = listsdm(sdm='AS1039_sb1382796_2_000.55368.51883247685')

        Prints information about the requested SDM to the CASA logger
        and returns a dictionary with scan information in 'myscans'.

        Keyword argument:

        sdm -- Name of input SDM directory.
               example: sdm='AG836_sb1377811_1.55345.300883159725'

  
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['sdm'] = sdm
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'listsdm.xml')

        casalog.origin('listsdm')
        if trec.has_key('listsdm') and casac.utils().verify(mytmp, trec['listsdm']) :
            result = task_listsdm.listsdm(sdm)

        else :
          result = False
        return result
