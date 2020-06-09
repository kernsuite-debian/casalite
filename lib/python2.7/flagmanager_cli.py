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
from task_flagmanager import flagmanager
class flagmanager_cli_:
    __name__ = "flagmanager"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (flagmanager_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'mode':None, 'versionname':None, 'oldname':None, 'comment':None, 'merge':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, mode=None, versionname=None, oldname=None, comment=None, merge=None, ):

        """Enable list, save, restore, delete and rename flag version files.

        Detailed Description:

        These flag version files are copies of the flag column for a
        measurement set.  They can be restored to the data set to get
        back to a previous flag version.  On running importvla, a flag
        version call 'Original' is automatically produced.
        
        Arguments :
                vis: Name of input visibility file (MS)
                   Default Value: 

                mode: Operation: list, save, restore, delete, rename
                   Default Value: list
                   Allowed Values:
                                list
                                save
                                restore
                                delete
                                rename

                versionname: Flag version name
                   Default Value: 

                oldname: Flag version to rename
                   Default Value: 

                comment: Short description of a versionname
                   Default Value: 

                merge: Merge option: replace will save or over-write the flags
                   Default Value: replace

        Returns: void

        Example :



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
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'flagmanager'
        self.__globals__['taskname'] = 'flagmanager'
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
            myparams['mode'] = mode = self.parameters['mode']
            myparams['versionname'] = versionname = self.parameters['versionname']
            myparams['oldname'] = oldname = self.parameters['oldname']
            myparams['comment'] = comment = self.parameters['comment']
            myparams['merge'] = merge = self.parameters['merge']


        result = None

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
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'flagmanager.xml')

        casalog.origin('flagmanager')
        try :
          #if not trec.has_key('flagmanager') or not casac.casac.utils().verify(mytmp, trec['flagmanager']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['flagmanager'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('flagmanager', 'flagmanager.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'flagmanager'
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
          result = flagmanager(vis, mode, versionname, oldname, comment, merge)

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
             tname = 'flagmanager'
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
#        paramgui.runTask('flagmanager', myf['_ip'])
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
        a['mode']  = 'list'

        a['mode'] = {
                    0:{'value':'list'}, 
                    1:odict([{'value':'save'}, {'versionname':''}, {'comment':''}, {'merge':'replace'}]), 
                    2:odict([{'value':'restore'}, {'versionname':''}, {'merge':'replace'}]), 
                    3:odict([{'value':'delete'}, {'versionname':''}]), 
                    4:odict([{'value':'rename'}, {'oldname':''}, {'versionname':''}, {'comment':''}])}

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
    def description(self, key='flagmanager', subkey=None):
        desc={'flagmanager': 'Enable list, save, restore, delete and rename flag version files.',
               'vis': 'Name of input visibility file (MS)',
               'mode': 'Operation: list, save, restore, delete, rename',
               'versionname': 'Flag version name',
               'oldname': 'Flag version to rename',
               'comment': 'Short description of a versionname',
               'merge': 'Merge option: replace will save or over-write the flags',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['mode']  = 'list'
        a['versionname']  = ''
        a['oldname']  = ''
        a['comment']  = ''
        a['merge']  = 'replace'

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mode']  == 'save':
            a['versionname'] = ''
            a['comment'] = ''
            a['merge'] = 'replace'

        if self.parameters['mode']  == 'restore':
            a['versionname'] = ''
            a['merge'] = 'replace'

        if self.parameters['mode']  == 'delete':
            a['versionname'] = ''

        if self.parameters['mode']  == 'rename':
            a['oldname'] = ''
            a['versionname'] = ''
            a['comment'] = ''

        if a.has_key(paramname) :
              return a[paramname]
flagmanager_cli = flagmanager_cli_()
