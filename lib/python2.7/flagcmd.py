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
import task_flagcmd
def flagcmd(vis='', inpmode='table', inpfile='', tablerows=[], reason='any', useapplied=False, tbuff=0.0, ants='', action='apply', flagbackup=True, clearall=False, rowlist=[], plotfile='', savepars=False, outfile='', overwrite=True):

        """Flagging task based on batches of flag-commands

For more information, see the task pages of flagcmd in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if type(tablerows)==int: tablerows=[tablerows]
        if type(rowlist)==int: rowlist=[rowlist]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['inpmode'] = inpmode
        mytmp['inpfile'] = inpfile
        mytmp['tablerows'] = tablerows
        mytmp['reason'] = reason
        mytmp['useapplied'] = useapplied
        mytmp['tbuff'] = tbuff
        mytmp['ants'] = ants
        mytmp['action'] = action
        mytmp['flagbackup'] = flagbackup
        mytmp['clearall'] = clearall
        mytmp['rowlist'] = rowlist
        mytmp['plotfile'] = plotfile
        mytmp['savepars'] = savepars
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'flagcmd.xml')

        casalog.origin('flagcmd')
        if trec.has_key('flagcmd') and casac.utils().verify(mytmp, trec['flagcmd']) :
            result = task_flagcmd.flagcmd(vis, inpmode, inpfile, tablerows, reason, useapplied, tbuff, ants, action, flagbackup, clearall, rowlist, plotfile, savepars, outfile, overwrite)

        else :
          result = False
        return result
