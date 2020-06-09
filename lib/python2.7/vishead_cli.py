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
from task_vishead import vishead
class vishead_cli_:
    __name__ = "vishead"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (vishead_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'mode':None, 'listitems':None, 'hdkey':None, 'hdindex':None, 'hdvalue':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, mode=None, listitems=None, hdkey=None, hdindex=None, hdvalue=None, ):

        """List, summary, get, and put metadata in a measurement set

        Detailed Description:


        This task allows the user to manipulate some meta-data keywords in a
        measurement set.  The mode='list' shows those keywords that are
        presently implemented, with their values.  The contents associated
        with the keywords can be obtained with mode='get' and changed with mode='put'. 

        The modes that are available are:

           list    --- List all keywords that are recognized, and list the
                       value(s) for each.  Only these keywords can be obtained
                       (get) or changed (put) 
           summary --- Provides a summary that is equivalent to running listobs(verbose=False)
           get     --- Get the specified keyword value(s) from the ms
           put     --- Put the specified keyword value(s) into the ms

        Keywords currently implemented are:

           cal_grp              
           field                 Field names
           fld_code              Field Observing codes
           freq_group_name       
           log                   
           observer              Observer name
           project               Project name
           ptcs                  Phase tracking centers for each field
           release_date          
           schedule
           schedule_type
           spw_name              Spectral parameters?
           source_name           Source Names (=Field Names?)
           telescope             Telescope Name

        Note that the default list of keywords is a subset of the former list. To get
        all the keywords set listitemts=[]. See task parameter listitems for more details.



        Arguments :
                vis: Name of input visibility file
                   Default Value: 

                mode: Mode of operation for vishead
                   Default Value: summary
                   Allowed Values:
                                list
                                summary
                                get
                                put
                                

                listitems: Keyword items to list. This parameter is only relevant in list mode. Note that the default list is a subset of the possible keywords. To get all the keywords set listitems=[]
                   Default Value: 
                   telescope
                   observer
                   project
                   field
                   freq_group_name
                   spw_name
                   schedule
                   schedule_type
                   release_date
         

                hdkey: Keyword to get/put
                   Default Value: 

                hdindex: Index (counting from 0) if keyword is an array (used in get/put mode only). The empty string means all elements
                   Default Value: 

                hdvalue: Value of the keywords to be put in the MS (used in put mode only)
                   Default Value: 


        Example :



        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'vishead'
        self.__globals__['taskname'] = 'vishead'
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
            myparams['listitems'] = listitems = self.parameters['listitems']
            myparams['hdkey'] = hdkey = self.parameters['hdkey']
            myparams['hdindex'] = hdindex = self.parameters['hdindex']
            myparams['hdvalue'] = hdvalue = self.parameters['hdvalue']

        if type(listitems)==str: listitems=[listitems]

        result = None

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
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'vishead.xml')

        casalog.origin('vishead')
        try :
          #if not trec.has_key('vishead') or not casac.casac.utils().verify(mytmp, trec['vishead']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['vishead'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('vishead', 'vishead.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'vishead'
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
          result = vishead(vis, mode, listitems, hdkey, hdindex, hdvalue)

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
             tname = 'vishead'
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
#        paramgui.runTask('vishead', myf['_ip'])
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
        a['mode']  = 'summary'

        a['mode'] = {
                    0:odict([{'value':'list'}, {'listitems':['telescope', 'observer', 'project', 'field', 'freq_group_name', 'spw_name', 'schedule', 'schedule_type', 'release_date']}]), 
                    1:{'value':'summary'}, 
                    2:odict([{'value':'get'}, {'hdkey':''}, {'hdindex':''}]), 
                    3:odict([{'value':'put'}, {'hdkey':''}, {'hdindex':''}, {'hdvalue':''}])}

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
    def description(self, key='vishead', subkey=None):
        desc={'vishead': 'List, summary, get, and put metadata in a measurement set',
               'vis': 'Name of input visibility file',
               'mode': 'Mode of operation for vishead',
               'listitems': 'Keyword items to list. This parameter is only relevant in list mode. Note that the default list is a subset of the possible keywords. To get all the keywords set listitems=[]',
               'hdkey': 'Keyword to get/put',
               'hdindex': 'Index (counting from 0) if keyword is an array (used in get/put mode only). The empty string means all elements',
               'hdvalue': 'Value of the keywords to be put in the MS (used in put mode only)',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['mode']  = 'summary'
        a['listitems']  = ['telescope', 'observer', 'project', 'field', 'freq_group_name', 'spw_name', 'schedule', 'schedule_type', 'release_date']
        a['hdkey']  = ''
        a['hdindex']  = ''
        a['hdvalue']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mode']  == 'list':
            a['listitems'] = ['telescope', 'observer', 'project', 'field', 'freq_group_name', 'spw_name', 'schedule', 'schedule_type', 'release_date']

        if self.parameters['mode']  == 'get':
            a['hdkey'] = ''
            a['hdindex'] = ''

        if self.parameters['mode']  == 'put':
            a['hdkey'] = ''
            a['hdindex'] = ''
            a['hdvalue'] = ''

        if a.has_key(paramname) :
              return a[paramname]
vishead_cli = vishead_cli_()
