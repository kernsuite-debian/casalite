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
from task_importfitsidi import importfitsidi
class importfitsidi_cli_:
    __name__ = "importfitsidi"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (importfitsidi_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'fitsidifile':None, 'vis':None, 'constobsid':None, 'scanreindexgap_s':None, 'specframe':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, fitsidifile=None, vis=None, constobsid=None, scanreindexgap_s=None, specframe=None, ):

        """Convert a FITS-IDI file to a CASA visibility data set

        Detailed Description:

Convert a FITS-IDI file to a CASA visiblity data set.
If several files are given, they will be concatenated into one MS.

        Arguments :
                fitsidifile: Name(s) of input FITS-IDI file(s)
                     Default: none (must be supplied)

                        Examples: 
                        fitsidifile='3C273XC1.IDI'
                        fitsidifile=['3C273XC1.IDI1','3C273XC1.IDI2']

                   Default Value: 

                vis: Name of output visibility file
                     Default: none

                        Example: outputvis='3C273XC1.ms'

                   Default Value: 

                constobsid: If True, give constant obs ID==0 to the data from all
input fitsidi files (False = separate obs id for each file)
                     Default: False (new obs id for each input file)
                     Options: False|True



                   Default Value: False

                scanreindexgap_s: Min time gap (seconds) between integrations to start a
new scan
                     Default: 0. (no reindexing)

                     If > 0., a new scan is started whenever the gap
                     between two integrations is > the given value
                     (seconds) or when a new field starts or when the
                     ARRAY_ID changes.

                   Default Value: 0.

                specframe: This frame will be used to set the spectral reference
frame for all spectral windows in the output MS
                     Default: GEO (geocentric)
                     Options: GEO|TOPO|LSRK|BARY

                     NOTE: if specframe is set to TOPO, the reference
                     location will be taken from the Observatories
                     table in the CASA data repository for the given
                     name of the observatory. You can edit that table
                     and add new rows.

                   Default Value: GEO


        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTFITSIDI IN CASA DOCS:
https://casa.nrao.edu/casadocs/
 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'importfitsidi'
        self.__globals__['taskname'] = 'importfitsidi'
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

            myparams['fitsidifile'] = fitsidifile = self.parameters['fitsidifile']
            myparams['vis'] = vis = self.parameters['vis']
            myparams['constobsid'] = constobsid = self.parameters['constobsid']
            myparams['scanreindexgap_s'] = scanreindexgap_s = self.parameters['scanreindexgap_s']
            myparams['specframe'] = specframe = self.parameters['specframe']

        if type(fitsidifile)==str: fitsidifile=[fitsidifile]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['fitsidifile'] = fitsidifile
        mytmp['vis'] = vis
        mytmp['constobsid'] = constobsid
        mytmp['scanreindexgap_s'] = scanreindexgap_s
        mytmp['specframe'] = specframe
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'importfitsidi.xml')

        casalog.origin('importfitsidi')
        try :
          #if not trec.has_key('importfitsidi') or not casac.casac.utils().verify(mytmp, trec['importfitsidi']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['importfitsidi'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('importfitsidi', 'importfitsidi.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'importfitsidi'
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
          result = importfitsidi(fitsidifile, vis, constobsid, scanreindexgap_s, specframe)

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
             tname = 'importfitsidi'
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
#        paramgui.runTask('importfitsidi', myf['_ip'])
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
        a['fitsidifile']  = ['']
        a['vis']  = ''
        a['constobsid']  = False
        a['scanreindexgap_s']  = 0.
        a['specframe']  = 'GEO'


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
    def description(self, key='importfitsidi', subkey=None):
        desc={'importfitsidi': 'Convert a FITS-IDI file to a CASA visibility data set',
               'fitsidifile': 'Name(s) of input FITS-IDI file(s)',
               'vis': 'Name of output visibility file',
               'constobsid': 'If True, give constant obs ID==0 to the data from all input fitsidi files (False = separate obs id for each file)',
               'scanreindexgap_s': 'Min time gap (seconds) between integrations to start a new scan',
               'specframe': 'Spectral reference frame for all spectral windows in the output MS',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['fitsidifile']  = ['']
        a['vis']  = ''
        a['constobsid']  = False
        a['scanreindexgap_s']  = 0.
        a['specframe']  = 'GEO'

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
importfitsidi_cli = importfitsidi_cli_()
