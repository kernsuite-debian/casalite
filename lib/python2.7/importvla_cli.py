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
from task_importvla import importvla
class importvla_cli_:
    __name__ = "importvla"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (importvla_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'archivefiles':None, 'vis':None, 'bandname':None, 'frequencytol':None, 'project':None, 'starttime':None, 'stoptime':None, 'applytsys':None, 'autocorr':None, 'antnamescheme':None, 'keepblanks':None, 'evlabands':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, archivefiles=None, vis=None, bandname=None, frequencytol=None, project=None, starttime=None, stoptime=None, applytsys=None, autocorr=None, antnamescheme=None, keepblanks=None, evlabands=None, ):

        """Import VLA archive file(s) to a measurement set

        Detailed Description:

Imports an arbitrary number of VLA archive-format data sets into a
casa measurement set.  If more than one band is present, they will be
put in the same measurement set but in a separate spectral window.
The task will handle old style and new style VLA (after July 2007)
archive data and apply the tsys to the data and to the weights.

        Arguments :
                archivefiles: Name of input VLA archive file(s)
                     Default: none.  Must be supplied

                        Examples: 
                        archivefiles = 'AP314_A959519.xp1'
                        archivefiles=['AP314_A950519.xp1',
                        'AP314_A950519.xp2']

                   Default Value: 

                vis: Name of output visibility file
                     Default: none.  Must be supplied

                        Example: vis='NGC7538.ms'

                     NOTE: Will not over-write existing ms of same
                     name. A backup flag-file version 'Original' will
                     be made in vis.flagversions.  See help
                     flagmanager.
 
                   Default Value: 

                bandname: VLA frequency band name:
                     Default: '' (obtain all bands in the archive
                     file)
                     Options: '4'=48-96 MHz,'P'=298-345
                     MHz,'L'=1.15-1.75 GHz, 'C'=4.2-5.1
                     GHz,'X'=6.8-9.6 GHz,'U'=13.5-16.3 GHz,
                     'K'=20.8-25.8 GHz,'Q'=38-51 GHz

                        Example: bandname='K'

                   Default Value: 
                   Allowed Values:
                                4
                                P
                                L
                                S
                                C
                                X
                                U
                                K
                                Ka
                                Q
                                

                frequencytol: Tolerance in frequency shift in making spectral windows
                     Default: = 150000.0Hz'

                        Example: frequencytol = 1500000.0 (units = Hz)

                     For Doppler shifted data, less than 10000 Hz may
                     may produce too many unnecessary spectral
                     windows.

                   Default Value: 150000.0Hz

                project: Project name to import from archive files
                     Default: '' (all projects in file)

                        Example: project='AL519'             
                        Project = 'al519' or AL519 will work. 

                     WARNING: Do not include leading zeros; project =
                     'AL0519' will not work.

                   Default Value: 

                starttime: Time after which data will be considered for importing
                     Default: '' (all)

                     syntax: starttime = '2003/1/31/05:05:23'. Date
                     must be included!

                   Default Value: 

                stoptime: Time before which data will be considered for
importing
                     Default: '' (all)

                     syntax: starttime = '2003/1/31/08:05:23'. Date
                     must be included!

                   Default Value: 

                applytsys: Apply data scaling and weight scaling by nominal
sensitivity (~Tsys)
                     Default: True (strongly recommended)
                     Options: True|False

                   Default Value: True

                autocorr: Import autocorrelations to MS
                     Default: False (no autocorrelations)
                     Options: False|True

                   Default Value: False

                antnamescheme: 'old' or 'new' antenna names.
                     Default: 'new'
                     Options: new|old

                     * 'new' gives antnenna names 'VA04' or 'EA13 for
                       VLA telescopse 04 and 13 (EVLA)
                     * 'old' gives names '04' or '13'

                   Default Value: new
                   Allowed Values:
                                old
                                new

                keepblanks: Should sources with blank names be filled into the data
base?
                     Default: False (do not fill)
                     Options: False|True

                     These scans are tipping scans (as of June 1,
                     2009) and should not be filled in the visibility
                     data set.

                   Default Value: False

                evlabands: Use the EVLA's center frequency and bandwidths for
frequencies specified via wavelength or band.
                     Default: False
                     Options: False|True

                   Default Value: False


        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTVLA IN CASA DOCS:
https://casa.nrao.edu/casadocs/
   
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'importvla'
        self.__globals__['taskname'] = 'importvla'
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

            myparams['archivefiles'] = archivefiles = self.parameters['archivefiles']
            myparams['vis'] = vis = self.parameters['vis']
            myparams['bandname'] = bandname = self.parameters['bandname']
            myparams['frequencytol'] = frequencytol = self.parameters['frequencytol']
            myparams['project'] = project = self.parameters['project']
            myparams['starttime'] = starttime = self.parameters['starttime']
            myparams['stoptime'] = stoptime = self.parameters['stoptime']
            myparams['applytsys'] = applytsys = self.parameters['applytsys']
            myparams['autocorr'] = autocorr = self.parameters['autocorr']
            myparams['antnamescheme'] = antnamescheme = self.parameters['antnamescheme']
            myparams['keepblanks'] = keepblanks = self.parameters['keepblanks']
            myparams['evlabands'] = evlabands = self.parameters['evlabands']

        if type(archivefiles)==str: archivefiles=[archivefiles]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['archivefiles'] = archivefiles
        mytmp['vis'] = vis
        mytmp['bandname'] = bandname
        mytmp['frequencytol'] = frequencytol
        mytmp['project'] = project
        mytmp['starttime'] = starttime
        mytmp['stoptime'] = stoptime
        mytmp['applytsys'] = applytsys
        mytmp['autocorr'] = autocorr
        mytmp['antnamescheme'] = antnamescheme
        mytmp['keepblanks'] = keepblanks
        mytmp['evlabands'] = evlabands
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'importvla.xml')

        casalog.origin('importvla')
        try :
          #if not trec.has_key('importvla') or not casac.casac.utils().verify(mytmp, trec['importvla']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['importvla'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('importvla', 'importvla.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'importvla'
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
          result = importvla(archivefiles, vis, bandname, frequencytol, project, starttime, stoptime, applytsys, autocorr, antnamescheme, keepblanks, evlabands)

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
             tname = 'importvla'
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
#        paramgui.runTask('importvla', myf['_ip'])
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
        a['archivefiles']  = ['']
        a['vis']  = ''
        a['bandname']  = ''
        a['frequencytol']  = '150000.0Hz'
        a['project']  = ''
        a['starttime']  = ''
        a['stoptime']  = ''
        a['applytsys']  = True
        a['autocorr']  = False
        a['antnamescheme']  = 'new'
        a['keepblanks']  = False
        a['evlabands']  = False


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
    def description(self, key='importvla', subkey=None):
        desc={'importvla': 'Import VLA archive file(s) to a measurement set',
               'archivefiles': 'Name of input VLA archive file(s)',
               'vis': 'Name of output visibility file',
               'bandname': 'VLA frequency band name:\'\'=>obtain all bands in the archive file',
               'frequencytol': 'Frequency shift to define a unique spectra window (Hz)',
               'project': 'Project name: \'\' => all projects in files',
               'starttime': 'Start time to search for data',
               'stoptime': 'End time to search for data',
               'applytsys': 'Apply nominal sensitivity scaling to data and weights',
               'autocorr': 'Import autocorrelations to MS, if set to True',
               'antnamescheme': '\'old\' or \'new\'; \'VA04\' or \'04\' for VLA ant 4',
               'keepblanks': 'Fill scans with blank (empty) source names (e.g. tipping scans)',
               'evlabands': 'Use updated eVLA frequencies and bandwidths for bands and wavelengths',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['archivefiles']  = ['']
        a['vis']  = ''
        a['bandname']  = ''
        a['frequencytol']  = '150000.0Hz'
        a['project']  = ''
        a['starttime']  = ''
        a['stoptime']  = ''
        a['applytsys']  = True
        a['autocorr']  = False
        a['antnamescheme']  = 'new'
        a['keepblanks']  = False
        a['evlabands']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
importvla_cli = importvla_cli_()
