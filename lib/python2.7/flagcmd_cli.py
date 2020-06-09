#
# This file was generated using xslt from its XML file
#
# Copyright 2014, Associated Universities Inc., Washington DC
#
import sys
import os
import datetime
#from casac import *
import casac
import string
import time
import inspect
import numpy
from casa_stack_manip import stack_frame_find
from odict import odict
from types import *
from task_flagcmd import flagcmd
class flagcmd_cli_:
    __name__ = "flagcmd"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (flagcmd_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'inpmode':None, 'inpfile':None, 'tablerows':None, 'reason':None, 'useapplied':None, 'tbuff':None, 'ants':None, 'action':None, 'flagbackup':None, 'clearall':None, 'rowlist':None, 'plotfile':None, 'savepars':None, 'outfile':None, 'overwrite':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, inpmode=None, inpfile=None, tablerows=None, reason=None, useapplied=None, tbuff=None, ants=None, action=None, flagbackup=None, clearall=None, rowlist=None, plotfile=None, savepars=None, outfile=None, overwrite=None, ):

        """Flagging task based on batches of flag-commands

        Detailed Description:

    The flagcmd task will flag the visibility data or calibration
    table based on several batch-operations using flag commands. 

    Flag commands follow the mode and parameter names from the
    flagdata task.

    The flagcmd task will flag data based on the commands input on
    inpmode:
        table = input from FLAG_CMD table in MS
        list  = input from text file or list of strings from inpfile
        xml   = input from Flag.xml in the MS given by vis

    Batch operations include : apply/unapply/list/plot/clear/extract

    IMPORTANT: If you use other ways to flag such as interactive
    flagging in plotms, the FLAG_CMD will NOT be updated! 
               
    NOTE on flagging calibration tables.
    -----------------------------------    
    We recommend using the flagdata task for flagging cal tabels. When
    using flagcmd to flag cal tables, only the 'apply' and 'list'
    actions are supported. Because cal tables do not have a FLAG_CMD
    sub-table, the default inpmode='table' can only be used if an MS
    is given in the 'inpfile' parameter so that flags from the MS are
    applied to the cal table. Otherwise, the flag commands must be
    given using inpmode='list', either from a file(s) or from a list
    of strings. Data selection for calibration tables is limited to
    field, scan, antenna, time, spw and observation.

        
        Arguments :
                vis: Name of input visibility file or calibration table.
                     default: '' (none) 

                        example: vis='uid___A002_X2a5c2f_X54.ms'

                   Default Value: 

                inpmode: Input mode for flag commands(table/list/xml)
                     options: 'table','list','xml'
                     default: 'table' (the input commands from
                     FLAG_CMD table of the MS)

                     inpmode='xml' inputs online flags from Flag.xml
                     file in the MS. This mode has become largely
                     obsolete with the deprecation of the importevla
                     task (see the flagcmd task pages in CASA Docs for
                     more information). This mode will not work for
                     ALMA MS or cal tables.

                     NOTE: You can only apply the flags from a list or
                     xml; you will not be able to unapply
                     them. Transfer the flag commands to the FLAG_CMD
                     table if you want to unapply the flags (see
                     'inpfile' description below).

                   Default Value: table
                   Allowed Values:
                                table
                                list
                                xml

                inpfile: Source of flag commands. Subparameter of
inpmode='table/list'.
                     Path to MS containing FLAG_CMD (table), or name
                     of an ASCII file, list of files or a list of
                     Python strings to apply to MS or cal table
                     (list). 
                     options: [] with flag commands or [] with
                     filenames or '' with a filename. (String values
                     must contain quotes around them or the parser
                     will not work.)
                     default: '' (read from FLAG_CMD table in the MS
                     specified via 'vis')

                     Main use is to read flags from internal FLAG_CMD,
                     but one use case is to read the flag commands
                     from an MS given in inpfile and apply them to
                     another MS or cal table given in vis.

                   Default Value: 

                tablerows: List of rows of the FLAG_CMD table to read. Subparameter
of inpmode='table/list'.
                     default: [] (read all rows)

                        example: [0,1,2,10]

                     NOTE: currently only takes integer lists, not
                     parseable strings with ranges.  Use the Python
                     range function to generate ranges, e.g. tablerows
                     = range(0,30) + range(50,55) instead of
                     '0~29,50~54' for now.

                   Default Value: 

                reason: Select flag commands based on REASON(s). Subparameter of
inpmode.
                     default: 'any' (all flags regardless of reason)

                        Examples: 
                        reason='FOCUS_ERROR'
                        reason=['FOCUS_ERROR','SUBREFLECTOR_ERROR']

                     If inpfile is a list of files, the reasons given
                     in this parameter will apply to all the files.

                     NOTE: what is within the string is literally
                     matched, e.g. reason='' matches only blank
                     reasons, and reason
                     ='FOCUS_ERROR,SUBREFLECTOR_ERROR' matches this
                     compound reason string only

                   Default Value: any

                useapplied: Select commands whose rows have APPLIED column set to
True. Subparameter of inpmode='table'.
                     options: True,False
                     default: False   

                     If useapplied=True it will read in both applied
                     and unapplied flags.

                     IMPORTANT: The APPLIED column is set to True
                     after a flag command is applied to the MS. In
                     order to re-apply the same flag command, this
                     parameter should be set to True. 

                   Default Value: False

                tbuff: Time buffer (sec) to pad flags. Subparameter of
inpmode='xml'.
                     default: 0.0

                   Default Value: 0.0

                ants: Allowed flag antenna names to select by. Subparameter of
inpmode='xml'.

                   Default Value: 

                action: Action to perform in MS and/or in inpfile
                     options: apply/unapply/list/plot/clear/extract
                     default: 'apply'
                   
                        Examples:
                        -- action='apply': This operation will apply
                        the commands chosen by inpmode. If
                        inpmode='table' and inpfile='' then the
                        APPLIED column in FLAG_CMD will be set to
                        True.
                        -- action='unapply': unapply flags in MS. (Not
                        available for cal tables). This operation will
                        unapply the commands chosen by inpmode='table'
                        ONLY. After unapplying the commands, the task
                        will update the APPLIED column to False.
                        -- action='list': list and/or save flag
                        commands. This operation will list the
                        commands chosen by inpmode on the screen and
                        save them to the MS or to a file without
                        applying. It will save the commands to outfile
                        if the parameter savepars is set to True. If
                        outfile is None, it will save the commands to
                        the MS given in 'vis'.
                        -- action='plot': plot flags (ant
                        vs. time). (Not available for cal
                        tables). This operation will plot the flags
                        chosen by inpmode to a matplotlib gui or to a
                        file.  These will be sorted by antenna
                        vs. time.  Most useful for showing the online
                        flags.
                        -- action='clear': clear flags from FLAG_CMD
                        in the MS. (Not available for cal tables) This
                        operation will delete the selected flag rows
                        from the internal FLAG_CMD table of the MS.
                        -- action='extract': extract internal flag
                        dictionary. (Not available for cal tables)
                        This option will return the internal flagging
                        dictionary to python. There is no extant
                        description of the format of this dictionary,
                        as it is an internal device used by the
                        flagcmd task. This action is provided for the
                        convenience of advanced users.

                    WARNING: choosing this action='clear' will
                    disregard anything you set in inpmode and will
                    always work on the FLAG_CMD table in vis. This can
                    be used to totally delete rows from the FLAG_CMD
                    table, when setting clearall=True.

                   Default Value: apply
                   Allowed Values:
                                apply
                                unapply
                                list
                                plot
                                clear
                                extract

                flagbackup: Automatically backup the FLAG column before
execution. Subparameter of action='apply/unapply'.
                     options: True,False
                     default: True

                   Default Value: True

                clearall: Delete all rows from FLAG_CMD. Subparameter of
action='clear'.
                     default: False (will not clear)

                   Default Value: False

                rowlist: FLAG_CMD rows to clear. Subparameter of action='clear'.
                     default: [] (all flags in table)
               
                        example: [0,1,2,10]

                     WARNING: this can be dangerous, and you must set
                     clearall=True  to use this!!! This will delete
                     the specified rows from the internal FLAG_CMD
                     table for vis regardless of what mode is set to
                     (useful for when you import from xml or file),
                     and decide to redo it). This action will NOT
                     unapply the commands.

                     NOTE: currently only takes integer lists, not
                     parseable strings with ranges.  Use the Python
                     range function to generate ranges, e.g. rowlist =
                     range(0,30) + range(50,55) instead of
                     '0~29,50~54' for now.

                   Default Value: 

                plotfile: Name of output file to save plot
                     default: '' (plot to matplotlib window)

                     WARNING: will only reliably plot individual flags
                     per antenna and timerange (e.g. direct from xml)   

                   Default Value: 

                savepars: Save the flag commands to the FLAG_CMD table of the MS or
to an output text file.
                     options: True/False     
                     default: False

                   Default Value: False

                outfile: Name of output file to save commands. Subparameter of
savepars=True.
                     default: ' '; it will save the commands in the
                     FLAG_CMD table of the MS.

                        example: outfile='flags.txt' will save the
                        parameters in a text file.

                   Default Value: 

                overwrite: Overwrite an existing file given in 'outfile' to save the
flag commands. Subparameter of savepars=True.
                     options: True/False
                     default: True; it will remove the existing file
                     given in 'outfile' and save the current flag
                     commands to a new file with the same name. When
                     set to False, the task will exit with an error
                     message if the file exist.

                   Default Value: True

        Returns: void

        Example :


For more information, see the task pages of flagcmd in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'flagcmd'
        self.__globals__['taskname'] = 'flagcmd'
        ###
        self.__globals__['update_params'](func=self.__globals__['taskname'],printtext=False,ipython_globals=self.__globals__)
        ###
        ###
        #Handle globals or user over-ride of arguments
        #
        if type(self.__call__.func_defaults) is NoneType:
            function_signature_defaults={}
        else:
            function_signature_defaults=dict(zip(self.__call__.func_code.co_varnames[1:],self.__call__.func_defaults))
        useLocalDefaults = False

        for item in function_signature_defaults.iteritems():
                key,val = item
                keyVal = eval(key)
                if (keyVal == None):
                        #user hasn't set it - use global/default
                        pass
                else:
                        #user has set it - use over-ride
                        if (key != 'self') :
                           useLocalDefaults = True

        myparams = {}
        if useLocalDefaults :
           for item in function_signature_defaults.iteritems():
               key,val = item
               keyVal = eval(key)
               exec('myparams[key] = keyVal')
               self.parameters[key] = keyVal
               if (keyVal == None):
                   exec('myparams[key] = '+ key + ' = self.itsdefault(key)')
                   keyVal = eval(key)
                   if(type(keyVal) == dict) :
                      if len(keyVal) > 0 :
                         exec('myparams[key] = ' + key + ' = keyVal[len(keyVal)-1][\'value\']')
                      else :
                         exec('myparams[key] = ' + key + ' = {}')

        else :
            print ''

            myparams['vis'] = vis = self.parameters['vis']
            myparams['inpmode'] = inpmode = self.parameters['inpmode']
            myparams['inpfile'] = inpfile = self.parameters['inpfile']
            myparams['tablerows'] = tablerows = self.parameters['tablerows']
            myparams['reason'] = reason = self.parameters['reason']
            myparams['useapplied'] = useapplied = self.parameters['useapplied']
            myparams['tbuff'] = tbuff = self.parameters['tbuff']
            myparams['ants'] = ants = self.parameters['ants']
            myparams['action'] = action = self.parameters['action']
            myparams['flagbackup'] = flagbackup = self.parameters['flagbackup']
            myparams['clearall'] = clearall = self.parameters['clearall']
            myparams['rowlist'] = rowlist = self.parameters['rowlist']
            myparams['plotfile'] = plotfile = self.parameters['plotfile']
            myparams['savepars'] = savepars = self.parameters['savepars']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']

        if type(tablerows)==int: tablerows=[tablerows]
        if type(rowlist)==int: rowlist=[rowlist]

        result = None

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
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'flagcmd.xml')

        casalog.origin('flagcmd')
        try :
          #if not trec.has_key('flagcmd') or not casac.casac.utils().verify(mytmp, trec['flagcmd']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['flagcmd'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('flagcmd', 'flagcmd.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'flagcmd'
          spaces = ' '*(18-len(tname))
          casalog.post('\n##########################################'+
                       '\n##### Begin Task: ' + tname + spaces + ' #####')
          # Don't do telemetry from MPI servers (CASR-329)
          if do_full_logging and casa['state']['telemetry-enabled']:
              #casalog.poststat('Begin Task: ' + tname)
              task_starttime = str(datetime.datetime.now())
          if type(self.__call__.func_defaults) is NoneType:
              casalog.post(scriptstr[0]+'\n', 'INFO')
          else:
              casalog.post(scriptstr[1][1:]+'\n', 'INFO')

          # Effective call to the task as defined in gcwrap/python/scripts/task_*
          result = flagcmd(vis, inpmode, inpfile, tablerows, reason, useapplied, tbuff, ants, action, flagbackup, clearall, rowlist, plotfile, savepars, outfile, overwrite)

          if do_full_logging and casa['state']['telemetry-enabled']:
              task_endtime = str(datetime.datetime.now())
              casalog.poststat( 'Task ' + tname + ' complete. Start time: ' + task_starttime + ' End time: ' + task_endtime )
          casalog.post('##### End Task: ' + tname + '  ' + spaces + ' #####'+
                       '\n##########################################')

        except Exception, instance:
          if(self.__globals__.has_key('__rethrow_casa_exceptions') and self.__globals__['__rethrow_casa_exceptions']) :
             raise
          else :
             #print '**** Error **** ',instance
             tname = 'flagcmd'
             casalog.post('An error occurred running task '+tname+'.', 'ERROR')
             pass
        casalog.origin('')

        return result
#
#
#
#    def paramgui(self, useGlobals=True, ipython_globals=None):
#        """
#        Opens a parameter GUI for this task.  If useGlobals is true, then any relevant global parameter settings are used.
#        """
#        import paramgui
#        if not hasattr(self, "__globals__") or self.__globals__ == None :
#           self.__globals__=stack_frame_find( )
#
#        if useGlobals:
#            if ipython_globals == None:
#                myf=self.__globals__
#            else:
#                myf=ipython_globals
#
#            paramgui.setGlobals(myf)
#        else:
#            paramgui.setGlobals({})
#
#        paramgui.runTask('flagcmd', myf['_ip'])
#        paramgui.setGlobals({})
#
#
#
#
    def defaults(self, param=None, ipython_globals=None, paramvalue=None, subparam=None):
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        if ipython_globals == None:
            myf=self.__globals__
        else:
            myf=ipython_globals

        a = odict()
        a['vis']  = ''
        a['inpmode']  = 'table'
        a['action']  = 'apply'
        a['savepars']  = False

        a['inpmode'] = {
                    0:odict([{'value':'table'}, {'inpfile':''}, {'tablerows':[]}, {'reason':'any'}, {'useapplied':False}]), 
                    1:odict([{'value':'list'}, {'inpfile':''}, {'reason':'any'}]), 
                    2:odict([{'value':'xml'}, {'tbuff':0.0}, {'ants':''}, {'reason':'any'}])}
        a['action'] = {
                    0:odict([{'value':'apply'}, {'flagbackup':True}]), 
                    1:odict([{'value':'unapply'}, {'flagbackup':True}]), 
                    2:{'value':'list'}, 
                    3:odict([{'value':'plot'}, {'plotfile':''}]), 
                    4:odict([{'value':'clear'}, {'clearall':False}, {'rowlist':[]}])}
        a['savepars'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'outfile':''}, {'overwrite':True}])}

### This function sets the default values but also will return the list of
### parameters or the default value of a given parameter
        if(param == None):
                myf['__set_default_parameters'](a)
        elif(param == 'paramkeys'):
                return a.keys()
        else:
            if(paramvalue==None and subparam==None):
               if(a.has_key(param)):
                  return a[param]
               else:
                  return self.itsdefault(param)
            else:
               retval=a[param]
               if(type(a[param])==dict):
                  for k in range(len(a[param])):
                     valornotval='value'
                     if(a[param][k].has_key('notvalue')):
                        valornotval='notvalue'
                     if((a[param][k][valornotval])==paramvalue):
                        retval=a[param][k].copy()
                        retval.pop(valornotval)
                        if(subparam != None):
                           if(retval.has_key(subparam)):
                              retval=retval[subparam]
                           else:
                              retval=self.itsdefault(subparam)
                     else:
                        retval=self.itsdefault(subparam)
               return retval


#
#
    def check_params(self, param=None, value=None, ipython_globals=None):
      if ipython_globals == None:
          myf=self.__globals__
      else:
          myf=ipython_globals
#      print 'param:', param, 'value:', value
      try :
         if str(type(value)) != "<type 'instance'>" :
            value0 = value
            value = myf['cu'].expandparam(param, value)
            matchtype = False
            if(type(value) == numpy.ndarray):
               if(type(value) == type(value0)):
                  myf[param] = value.tolist()
               else:
                  #print 'value:', value, 'value0:', value0
                  #print 'type(value):', type(value), 'type(value0):', type(value0)
                  myf[param] = value0
                  if type(value0) != list :
                     matchtype = True
            else :
               myf[param] = value
            value = myf['cu'].verifyparam({param:value})
            if matchtype:
               value = False
      except Exception, instance:
         #ignore the exception and just return it unchecked
         myf[param] = value
      return value
#
#
    def description(self, key='flagcmd', subkey=None):
        desc={'flagcmd': 'Flagging task based on batches of flag-commands',
               'vis': 'Name of MS file or calibration table to flag',
               'inpmode': 'Input mode for flag commands(table/list/xml)',
               'inpfile': 'Source of flag commands',
               'tablerows': 'Rows of inpfile to read',
               'reason': 'Select by REASON types',
               'useapplied': 'Select commands whose rows have APPLIED column set to True',
               'tbuff': 'Time buffer (sec) to pad flags',
               'ants': 'Allowed flag antenna names to select by',
               'action': 'Action to perform in MS and/or in inpfile (apply/unapply/list/plot/clear/extract)',
               'flagbackup': 'Automatically backup the FLAG column before execution',
               'clearall': 'Delete all rows from FLAG_CMD',
               'rowlist': 'FLAG_CMD rows to clear',
               'plotfile': 'Name of output file to save plot',
               'savepars': 'Save flag commands to the MS or file',
               'outfile': 'Name of output file to save commands',
               'overwrite': 'Overwrite an existing file to save the flag commands',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['inpmode']  = 'table'
        a['inpfile']  = ''
        a['tablerows']  = []
        a['reason']  = 'any'
        a['useapplied']  = False
        a['tbuff']  = 0.0
        a['ants']  = ''
        a['action']  = 'apply'
        a['flagbackup']  = True
        a['clearall']  = False
        a['rowlist']  = []
        a['plotfile']  = ''
        a['savepars']  = False
        a['outfile']  = ''
        a['overwrite']  = True

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['inpmode']  == 'table':
            a['inpfile'] = ''
            a['tablerows'] = []
            a['reason'] = 'any'
            a['useapplied'] = False

        if self.parameters['inpmode']  == 'list':
            a['inpfile'] = ''
            a['reason'] = 'any'

        if self.parameters['inpmode']  == 'xml':
            a['tbuff'] = 0.0
            a['ants'] = ''
            a['reason'] = 'any'

        if self.parameters['action']  == 'apply':
            a['flagbackup'] = True

        if self.parameters['action']  == 'unapply':
            a['flagbackup'] = True

        if self.parameters['action']  == 'plot':
            a['plotfile'] = ''

        if self.parameters['action']  == 'clear':
            a['clearall'] = False
            a['rowlist'] = []

        if self.parameters['savepars']  == True:
            a['outfile'] = ''
            a['overwrite'] = True

        if a.has_key(paramname) :
              return a[paramname]
flagcmd_cli = flagcmd_cli_()
