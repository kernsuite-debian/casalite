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
from task_importatca import importatca
class importatca_cli_:
    __name__ = "importatca"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (importatca_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'files':None, 'vis':None, 'options':None, 'spw':None, 'nscans':None, 'lowfreq':None, 'highfreq':None, 'fields':None, 'edge':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, files=None, vis=None, options=None, spw=None, nscans=None, lowfreq=None, highfreq=None, fields=None, edge=None, ):

        """Import ATCA RPFITS file(s) to a measurement set

        Detailed Description:

Imports an arbitrary number of ATCA RPFITS format data sets into a
casa measurement set.  If more than one band is present, they will be
put in the same measurement set but in a separate spectral window.
The task will handle both old ATCA and new CABB (after April 2009)
archive data.

        Arguments :
                files: Name of input ATCA RPFits file(s)
                   Default Value: 

                vis: Name of output MeasurementSet
                     Default: none

                        Example: vis='mydata.ms'

                   Default Value: 

                options: Processing options
                     Default: none
                     Options: birdie, reweight, noxycorr, fastmosaic,
                     hires, noac (comma separated list)

                     * birdie: (pre-CABB data only) discard edge
                       channels and channels affected by internal RFI
                     * reweight: (pre-CABB data only) suppress ringing
                       of RFI spikes by reweighting of the lag
                       spectrum 
                     * noxycorr: do not apply the xy phase correction
                       as derived from the switched noise calibration,
                       by default this is applied during loading of
                       the data
                     * fastmosaic: use this option if you are loading
                       mosaic data with many pointings and only one or
                       two integrations per pointing; this option
                       changes the tiling of the data to avoid
                       excessive I/O
                     * hires: use this option if you have data in time
                       binning mode (as used for pulsars) but you want
                       to make it look like data with very short
                       integration time (no bins)
                     * noac: discard the auto-correlation data

                   Default Value: 

                spw: Select spectral window/channels
                     Default: '' (all spectral windows and channels)
           
                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                        spw='<2';  spectral windows less than 2 (i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
                        3 - chans 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
                        through 6 in each.
                        spw = '*:3~64'  channels 3 through 64 for all sp id's
                        spw = ' :3~64' will NOT work.

                   Default Value: -1

                nscans: Number of scans to skip followed by number of scans to
read
                     Default: [0, 0]

                   Default Value: 0,0

                lowfreq: Lowest reference frequency to select
                     Default: 0.1GHz

                   Default Value: 0.1

                highfreq: Highest reference frequency to select
                     Default: 999GHz

                   Default Value: 999

                fields: List of field names to select

                   Default Value: 

                edge: The edge parameter specifies how many edge channels to
discard as a percentage of the number of channels in each band.
                     Default: 8 (e.g., discard 82 channels from the
                     top and bottom of a 2048 channel spectrum)

                     For combined zooms, this specifies the percentage
                     for a single zoom window

                   Default Value: 8


        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTATCA IN CASA DOCS:
https://casa.nrao.edu/casadocs/ 
   
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'importatca'
        self.__globals__['taskname'] = 'importatca'
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

            myparams['files'] = files = self.parameters['files']
            myparams['vis'] = vis = self.parameters['vis']
            myparams['options'] = options = self.parameters['options']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['nscans'] = nscans = self.parameters['nscans']
            myparams['lowfreq'] = lowfreq = self.parameters['lowfreq']
            myparams['highfreq'] = highfreq = self.parameters['highfreq']
            myparams['fields'] = fields = self.parameters['fields']
            myparams['edge'] = edge = self.parameters['edge']

        if type(files)==str: files=[files]
        if type(spw)==int: spw=[spw]
        if type(nscans)==int: nscans=[nscans]
        if type(fields)==str: fields=[fields]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['files'] = files
        mytmp['vis'] = vis
        mytmp['options'] = options
        mytmp['spw'] = spw
        mytmp['nscans'] = nscans
        if type(lowfreq) == str :
           mytmp['lowfreq'] = casac.casac.qa.quantity(lowfreq)
        else :
           mytmp['lowfreq'] = lowfreq
        if type(highfreq) == str :
           mytmp['highfreq'] = casac.casac.qa.quantity(highfreq)
        else :
           mytmp['highfreq'] = highfreq
        mytmp['fields'] = fields
        mytmp['edge'] = edge
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'importatca.xml')

        casalog.origin('importatca')
        try :
          #if not trec.has_key('importatca') or not casac.casac.utils().verify(mytmp, trec['importatca']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['importatca'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('importatca', 'importatca.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'importatca'
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
          result = importatca(files, vis, options, spw, nscans, lowfreq, highfreq, fields, edge)

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
             tname = 'importatca'
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
#        paramgui.runTask('importatca', myf['_ip'])
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
        a['files']  = ['']
        a['vis']  = ''
        a['options']  = ''
        a['spw']  = [-1]
        a['nscans']  = [0,0]
        a['lowfreq']  = '0.1GHz'
        a['highfreq']  = '999GHz'
        a['fields']  = ['']
        a['edge']  = 8


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
    def description(self, key='importatca', subkey=None):
        desc={'importatca': 'Import ATCA RPFITS file(s) to a measurement set',
               'files': 'Name of input ATCA RPFits file(s)',
               'vis': 'Name of output MeasurementSet',
               'options': 'Processing options: birdie, reweight, noxycorr, fastmosaic, hires, noac (comma separated list)',
               'spw': 'Select spectral window/channels',
               'nscans': 'Number of scans to skip followed by number of scans to read',
               'lowfreq': 'Lowest reference frequency to select',
               'highfreq': 'Highest reference frequency to select',
               'fields': 'List of field names to select',
               'edge': 'Percentage of edge channels to flag. For combined zooms, this specifies the percentage for a single zoom window',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['files']  = ['']
        a['vis']  = ''
        a['options']  = ''
        a['spw']  = [-1]
        a['nscans']  = [0,0]
        a['lowfreq']  = '0.1GHz'
        a['highfreq']  = '999GHz'
        a['fields']  = ['']
        a['edge']  = 8

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
importatca_cli = importatca_cli_()
