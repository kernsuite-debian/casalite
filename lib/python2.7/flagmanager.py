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
import task_flagmanager
def flagmanager(vis='', mode='list', versionname='', oldname='', comment='', merge='replace'):

        """Enable list, save, restore, delete and rename flag version files.


        The flag version files are copies of the FLAG column of a
        Measurement Set. They can be restored to the data set to obtain
        a previous flag version.  On running importasdm, a flag
        version called 'Original' is produced by default.  It is recommended to
        save a flagversion at the beginning or after serious editing.    

        Keyword arguments:
        vis -- Name of input visibility file
                default: none. example: vis='ngc5921.ms'

        mode -- Flag version operation
                default: 'list': it will list in the logger the existing flag versions of the MS.
                                 This option will also return by default a dictionary containing the
                                 name of the MS, the name of the flag version and the comment. This 
                                 information is taken from the FLAG_VERSION_LIST file inside the
                                 .flagversions directory.

                'save': will save the FLAG column from vis to a specified flag file. If the name given
                        in versionname already exists, the task will give a warning and rename it 
                        to a name with a suffix '.old.timestamp'. The respective entry in FLAG_VERSION_LIST 
                        will also be updated.

                'restore': will place the specified flag file into vis

                'delete': will delete specified flag file

                'rename': will rename a specified flag file

        versionname -- Flag version name
                default: none; example: versionname='original_data'
                No imbedded blanks in the versionname

        comment -- Short description of a versionname, when mode is 'save' or 'rename'
                default: ''; example: comment='Clip above 1.85'
                comment = versionname

        oldname -- When mode='rename', the flag file to rename

        merge -- Merge operation
                Options: 'or','and', but not recommended for now.

 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['mode'] = mode
        mytmp['versionname'] = versionname
        mytmp['oldname'] = oldname
        mytmp['comment'] = comment
        mytmp['merge'] = merge
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'flagmanager.xml')

        casalog.origin('flagmanager')
        if trec.has_key('flagmanager') and casac.utils().verify(mytmp, trec['flagmanager']) :
            result = task_flagmanager.flagmanager(vis, mode, versionname, oldname, comment, merge)

        else :
          result = False
        return result
