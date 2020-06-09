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
from task_slsearch import slsearch
class slsearch_cli_:
    __name__ = "slsearch"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (slsearch_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'tablename':None, 'outfile':None, 'freqrange':None, 'species':None, 'reconly':None, 'chemnames':None, 'qns':None, 'intensity':None, 'smu2':None, 'loga':None, 'el':None, 'eu':None, 'rrlinclude':None, 'rrlonly':None, 'verbose':None, 'logfile':None, 'append':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, tablename=None, outfile=None, freqrange=None, species=None, reconly=None, chemnames=None, qns=None, intensity=None, smu2=None, loga=None, el=None, eu=None, rrlinclude=None, rrlonly=None, verbose=None, logfile=None, append=None, ):

        """Search a spectral line table.
        Arguments :
                tablename: Input spectral line table name to search. If not specified, use the default table in the system.
                   Default Value: 

                outfile: Results table name. Blank means do not write the table to disk.
                   Default Value: 

                freqrange: Frequency range in GHz.
                   Default Value: 
              84
              90
            

                species: Species to search for.
                   Default Value: 

                reconly: List only NRAO recommended frequencies.
                   Default Value: False

                chemnames: Chemical names to search for.
                   Default Value: 

                qns: Resolved quantum numbers to search for.
                   Default Value: 

                intensity: CDMS/JPL intensity range. -1 -> do not use an intensity range.
                   Default Value: -1

                smu2: Quantum mechanical line strength. -1 -> do not use a smu2 range.
                   Default Value: -1

                loga: log(A) (Einstein coefficient) range. -1 -> do not use a loga range.
                   Default Value: -1

                el: Lower energy state range in Kelvin. -1 -> do not use an el range.
                   Default Value: -1

                eu: Upper energy state range in Kelvin. -1 -> do not use an eu range.
                   Default Value: -1

                rrlinclude: Include RRLs in the result set?
                   Default Value: True

                rrlonly: Include only RRLs in the result set?
                   Default Value: False

                verbose: List result set to logger (and optionally logfile)?
                   Default Value: False

                logfile: List result set to this logfile (only used if verbose=True).
                   Default Value: ""

                append: If true, append to logfile if it already exists, if false overwrite logfile it it exists. Only used if verbose=True and logfile not blank.
                   Default Value: False

        Returns: bool

        Example :


PARAMETER SUMMARY

tablename      Input spectral line table name to search. If not specified, use the default table in the system.
outfile        Results table name. Blank means do not write the table to disk.
freqrange      Frequency range in GHz.
species        Species to search for.
reconly        List only NRAO recommended frequencies.
chemnames      Chemical names to search for.
qns            Resolved quantum numbers to search for.
intensity      CDMS/JPL intensity range. -1 -> do not use an intensity range.
smu2           S*mu*mu range in Debye**2. -1 -> do not use an S*mu*mu range.
loga           log(A) (Einstein coefficient) range. -1 -> do not use a loga range.
el             Lower energy state range in Kelvin. -1 -> do not use an el range.
eu             Upper energy state range in Kelvin. -1 -> do not use an eu range.
rrlinclude     Include RRLs in the result set?
rrlonly        Include only RRLs in the result set?
verbose        List result set to logger (and optionally logfile)?
logfile        List result set to this logfile (only used if verbose=True).
append         If true, append to logfile if it already exists, if false overwrite logfile it it exists. Only used if verbose=True and logfile not blank.

    Search the specfied spectral line table. The results table can be written to disk by specifying its name in the outfile parameter.
    If outfile is not specified (ie outfile=""), no table is created. Because Splatalogue does not have values for intensity, smu2,
    loga, eu, and el for radio recombination lines (rrls), one must specify to include RRLs in the specified frequency range in the
    output. In this case, RRLs will be included ignoring any filters on intensity, smu2, loga, eu, and el. One can also specify to
    list only RRLs. One can specify to list the search results to the logger via the verbose parameter. If verbose is False, no
    logger output is listed. If verbose=True, one can also specify that the results be listed to a logfile and if this file already
    exists, one can specify that the results be appended to it or to overwrite it with the results.
    
    # put search results in a table but do not list to the logger
    slsearch("myspectrallines.tbl", verbose=False)


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'slsearch'
        self.__globals__['taskname'] = 'slsearch'
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

            myparams['tablename'] = tablename = self.parameters['tablename']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['freqrange'] = freqrange = self.parameters['freqrange']
            myparams['species'] = species = self.parameters['species']
            myparams['reconly'] = reconly = self.parameters['reconly']
            myparams['chemnames'] = chemnames = self.parameters['chemnames']
            myparams['qns'] = qns = self.parameters['qns']
            myparams['intensity'] = intensity = self.parameters['intensity']
            myparams['smu2'] = smu2 = self.parameters['smu2']
            myparams['loga'] = loga = self.parameters['loga']
            myparams['el'] = el = self.parameters['el']
            myparams['eu'] = eu = self.parameters['eu']
            myparams['rrlinclude'] = rrlinclude = self.parameters['rrlinclude']
            myparams['rrlonly'] = rrlonly = self.parameters['rrlonly']
            myparams['verbose'] = verbose = self.parameters['verbose']
            myparams['logfile'] = logfile = self.parameters['logfile']
            myparams['append'] = append = self.parameters['append']

        if type(freqrange)==float: freqrange=[freqrange]
        if type(species)==str: species=[species]
        if type(chemnames)==str: chemnames=[chemnames]
        if type(qns)==str: qns=[qns]
        if type(intensity)==float: intensity=[intensity]
        if type(smu2)==float: smu2=[smu2]
        if type(loga)==float: loga=[loga]
        if type(el)==float: el=[el]
        if type(eu)==float: eu=[eu]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['tablename'] = tablename
        mytmp['outfile'] = outfile
        mytmp['freqrange'] = freqrange
        mytmp['species'] = species
        mytmp['reconly'] = reconly
        mytmp['chemnames'] = chemnames
        mytmp['qns'] = qns
        mytmp['intensity'] = intensity
        mytmp['smu2'] = smu2
        mytmp['loga'] = loga
        mytmp['el'] = el
        mytmp['eu'] = eu
        mytmp['rrlinclude'] = rrlinclude
        mytmp['rrlonly'] = rrlonly
        mytmp['verbose'] = verbose
        mytmp['logfile'] = logfile
        mytmp['append'] = append
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'slsearch.xml')

        casalog.origin('slsearch')
        try :
          #if not trec.has_key('slsearch') or not casac.casac.utils().verify(mytmp, trec['slsearch']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['slsearch'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('slsearch', 'slsearch.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'slsearch'
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
          result = slsearch(tablename, outfile, freqrange, species, reconly, chemnames, qns, intensity, smu2, loga, el, eu, rrlinclude, rrlonly, verbose, logfile, append)

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
             tname = 'slsearch'
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
#        paramgui.runTask('slsearch', myf['_ip'])
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
        a['tablename']  = ''
        a['outfile']  = ''
        a['freqrange']  = [84, 90]
        a['species']  = ['']
        a['reconly']  = False
        a['chemnames']  = ['']
        a['qns']  = ['']
        a['rrlinclude']  = True
        a['rrlonly']  = False
        a['verbose']  = False

        a['verbose'] = {
                    0:odict([{'value':True}, {'logfile':""}, {'append':True}])}
        a['rrlonly'] = {
                    0:odict([{'value':False}, {'intensity':-1}, {'smu2':-1}, {'loga':-1}, {'eu':-1}, {'el':-1}])}

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
    def description(self, key='slsearch', subkey=None):
        desc={'slsearch': 'Search a spectral line table.',
               'tablename': 'Input spectral line table name to search. If not specified, use the default table in the system.',
               'outfile': 'Results table name. Blank means do not write the table to disk.',
               'freqrange': 'Frequency range in GHz.',
               'species': 'Species to search for.',
               'reconly': 'List only NRAO recommended frequencies.',
               'chemnames': 'Chemical names to search for.',
               'qns': 'Resolved quantum numbers to search for.',
               'intensity': 'CDMS/JPL intensity range. -1 -> do not use an intensity range.',
               'smu2': 'Quantum mechanical line strength. -1 -> do not use a smu2 range.',
               'loga': 'log(A) (Einstein coefficient) range. -1 -> do not use a loga range.',
               'el': 'Lower energy state range in Kelvin. -1 -> do not use an el range.',
               'eu': 'Upper energy state range in Kelvin. -1 -> do not use an eu range.',
               'rrlinclude': 'Include RRLs in the result set?',
               'rrlonly': 'Include only RRLs in the result set?',
               'verbose': 'List result set to logger (and optionally logfile)?',
               'logfile': 'List result set to this logfile (only used if verbose=True).',
               'append': 'If true, append to logfile if it already exists, if false overwrite logfile it it exists. Only used if verbose=True and logfile not blank.',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['tablename']  = ''
        a['outfile']  = ''
        a['freqrange']  = [84, 90]
        a['species']  = ['']
        a['reconly']  = False
        a['chemnames']  = ['']
        a['qns']  = ['']
        a['intensity']  = [-1]
        a['smu2']  = [-1]
        a['loga']  = [-1]
        a['el']  = [-1]
        a['eu']  = [-1]
        a['rrlinclude']  = True
        a['rrlonly']  = False
        a['verbose']  = False
        a['logfile']  = '""'
        a['append']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['verbose']  == True:
            a['logfile'] = ""
            a['append'] = True

        if self.parameters['rrlonly']  == False:
            a['intensity'] = -1
            a['smu2'] = -1
            a['loga'] = -1
            a['eu'] = -1
            a['el'] = -1

        if a.has_key(paramname) :
              return a[paramname]
slsearch_cli = slsearch_cli_()
