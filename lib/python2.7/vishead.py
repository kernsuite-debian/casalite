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
import task_vishead
def vishead(vis='', mode='summary', listitems=['telescope', 'observer', 'project', 'field', 'freq_group_name', 'spw_name', 'schedule', 'schedule_type', 'release_date'], hdkey='', hdindex='', hdvalue=''):

        """List, summary, get, and put metadata in a measurement set


        """
        if type(listitems)==str: listitems=[listitems]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['mode'] = mode
        mytmp['listitems'] = listitems
        mytmp['hdkey'] = hdkey
        mytmp['hdindex'] = hdindex
        mytmp['hdvalue'] = hdvalue
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'vishead.xml')

        casalog.origin('vishead')
        if trec.has_key('vishead') and casac.utils().verify(mytmp, trec['vishead']) :
            result = task_vishead.vishead(vis, mode, listitems, hdkey, hdindex, hdvalue)

        else :
          result = False
        return result
