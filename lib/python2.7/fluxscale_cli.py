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
from task_fluxscale import fluxscale
class fluxscale_cli_:
    __name__ = "fluxscale"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (fluxscale_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'caltable':None, 'fluxtable':None, 'reference':None, 'transfer':None, 'listfile':None, 'append':None, 'refspwmap':None, 'gainthreshold':None, 'antenna':None, 'timerange':None, 'scan':None, 'incremental':None, 'fitorder':None, 'display':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, caltable=None, fluxtable=None, reference=None, transfer=None, listfile=None, append=None, refspwmap=None, gainthreshold=None, antenna=None, timerange=None, scan=None, incremental=None, fitorder=None, display=None, ):

        """Bootstrap the flux density scale from standard calibrators

        Detailed Description:

Bootstrap the flux density scale from standard calibrators.
    
        Arguments :
                vis: Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'

                   Default Value: 

                caltable: Name of input calibration table
                     Default: none

                        Example: caltable='ngc5921.gcal'. This cal
                        table was obtained from task gaincal.=

                   Default Value: 

                fluxtable: Name of output, flux-scaled calibration table (required)
                     Default: none

                        Example: fluxtable='ngc5921.gcal2'

                     The gains in this table have been adjusted by the
                     derived flux density each calibrator.  The
                     MODEL_DATA column has NOT been updated for the
                     flux density of the calibrator.  Use setjy to do
                     this if it is a point source.

                   Default Value: 

                reference: Reference field name(s) (transfer flux scale FROM)
                     Default: none

                        Example: reference='1328+307'

                     The names of the fields with a known flux
                     densities or visibilities that have been placed
                     in the MODEL column by setjy or ft for a model
                     not in the CASA system. The syntax is similar to
                     field.  Hence field index or names can be used.

                   Default Value: 

                transfer: Transfer field name(s) (transfer flux scale TO)
                     Default: '' (all sources in caltable that are not
                     specified as reference sources.  Do not include
                     unknown target sources)

                     The names of the fields with unknown flux
                     densities. These should be point-like calibrator
                     sources The syntax is similar to field.  Hence
                     source index or names can be used.

                        Examples: transfer='1445+099, 3C84'; transfer
                        = '0,4'

                     NOTE: All fields in reference and transfer must
                     have solutions in the caltable.

                   Default Value: 

                listfile: Name of listfile that contains the fit information.
                     Default: '' (no fit listfile will be created)

                     The list file contains the flux density, flux
                     density error, S/N, and number of solutions (all
                     antennas and feeds) for each spectral window.  
                     NOTE: The nominal spectral window frequencies
                     will be included in the future.

                   Default Value: 

                append: Append fluxscaled solutions to the fluxtable?
                     Default: False (the fluxtable must not exist)
                     Options: False|True

                   Default Value: False

                refspwmap: Vector of spectral windows enabling scaling across
spectral windows
                     Default: [-1] (none)

                        Example with 4 spectral windows:
                        If the reference fields were observed only in
                        spw=1 and 3, and the transfer fields were
                        observed in all 4 spws (0,1,2,3), specify
                        refspwmap=[1,1,3,3]. This will ensure that
                        transfer fields observed in spws 0,1,2,3 will
                        be referenced to reference field solutions
                        only in spw 1 or 3.

                   Default Value: -1

                gainthreshold: Threshold in the input gain solutions to be used in % deviation from median values.
                     Default: -1 (no threshold)

                        Example: gainthreshold=0.15 (only used the
                        gain solutions within 15% (inclusive) of the
                        median gain value (per field and per spw). 

                   Default Value: -1.0

                antenna: Select data based on antenna/baseline
                     Subparameter of antenna
                     Default: '' (all)

                     If antenna string is a non-negative integer, it
                     is assumed an antenna index, otherwise, it is
                     assumed as an antenna name
  
                         Examples: 
                         antenna='5&6'; baseline between antenna
                         index 5 and index 6.
                         antenna='VA05&VA06'; baseline between VLA
                         antenna 5 and 6.
                         antenna='5&6;7&8'; baselines with
                         indices 5-6 and 7-8
                         antenna='5'; all baselines with antenna index
                         5
                         antenna='05'; all baselines with antenna
                         number 05 (VLA old name)
                         antenna='5,6,10'; all baselines with antennas
                         5,6,10 index numbers

                   Default Value: 

                timerange: Select data based on time range
                     Subparameter of antenna
                     Default = '' (all)

                        Examples:
                        timerange =
                        'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                        (Note: if YYYY/MM/DD is missing date defaults
                        to first day in data set.)
                        timerange='09:14:0~09:54:0' picks 40 min on
                        first day 
                        timerange= '25:00:00~27:30:00' picks 1 hr to 3
                        hr 30min on NEXT day
                        timerange='09:44:00' pick data within one
                        integration of time
                        timerange='>10:24:00' data after this time

                   Default Value: 

                scan: Scan number range
                     Subparameter of antenna
                     Default: '' = all

                   Default Value: 

                incremental: Create an incremental caltable containing only gain
correction factors ( flux density= 1/(gain correction factor)**2)?
                     Default: False
                     Options: False|True

                        Example: incremental=True (output a caltable
                        containing flux scale factors.)

                     NOTE: If you use the incremental option, note
                     that BOTH this incremental fluxscale table AND an
                     amplitude vs. time table should be supplied in
                     applycal.

                   Default Value: False

                fitorder: Polynomial order of the spectral fitting for valid flux
densities
                     Default: 1

                     It falls back to a lower fitorder if there are
                     not enough solutions to fit with the requested
                     fitorder.

                   Default Value: 1

                display: Display statistics and/or spectral fitting results.
                     Default: False
                     Options: False|True

                     Currently only a histogram of the correction
                     factors to derive the final flux density for each
                     spectral window will be plotted.

                   Default Value: False

        Returns: void

        Example :

For more information, see the task pages of fluxscale in CASA Docs:

https://casa.nrao.edu/casadocs/
 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'fluxscale'
        self.__globals__['taskname'] = 'fluxscale'
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
            myparams['caltable'] = caltable = self.parameters['caltable']
            myparams['fluxtable'] = fluxtable = self.parameters['fluxtable']
            myparams['reference'] = reference = self.parameters['reference']
            myparams['transfer'] = transfer = self.parameters['transfer']
            myparams['listfile'] = listfile = self.parameters['listfile']
            myparams['append'] = append = self.parameters['append']
            myparams['refspwmap'] = refspwmap = self.parameters['refspwmap']
            myparams['gainthreshold'] = gainthreshold = self.parameters['gainthreshold']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['incremental'] = incremental = self.parameters['incremental']
            myparams['fitorder'] = fitorder = self.parameters['fitorder']
            myparams['display'] = display = self.parameters['display']

        if type(reference)==str: reference=[reference]
        if type(transfer)==str: transfer=[transfer]
        if type(refspwmap)==int: refspwmap=[refspwmap]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['caltable'] = caltable
        mytmp['fluxtable'] = fluxtable
        mytmp['reference'] = reference
        mytmp['transfer'] = transfer
        mytmp['listfile'] = listfile
        mytmp['append'] = append
        mytmp['refspwmap'] = refspwmap
        mytmp['gainthreshold'] = gainthreshold
        mytmp['antenna'] = antenna
        mytmp['timerange'] = timerange
        mytmp['scan'] = scan
        mytmp['incremental'] = incremental
        mytmp['fitorder'] = fitorder
        mytmp['display'] = display
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'fluxscale.xml')

        casalog.origin('fluxscale')
        try :
          #if not trec.has_key('fluxscale') or not casac.casac.utils().verify(mytmp, trec['fluxscale']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['fluxscale'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('fluxscale', 'fluxscale.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'fluxscale'
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
          result = fluxscale(vis, caltable, fluxtable, reference, transfer, listfile, append, refspwmap, gainthreshold, antenna, timerange, scan, incremental, fitorder, display)

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
             tname = 'fluxscale'
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
#        paramgui.runTask('fluxscale', myf['_ip'])
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
        a['caltable']  = ''
        a['fluxtable']  = ''
        a['reference']  = ['']
        a['transfer']  = ['']
        a['listfile']  = ''
        a['append']  = False
        a['refspwmap']  = [-1]
        a['gainthreshold']  = -1.0
        a['antenna']  = ''
        a['incremental']  = False
        a['fitorder']  = 1
        a['display']  = False

        a['antenna'] = {
                    0:odict([{'notvalue':''}, {'timerange':''}, {'scan':''}])}

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
    def description(self, key='fluxscale', subkey=None):
        desc={'fluxscale': 'Bootstrap the flux density scale from standard calibrators',
               'vis': 'Name of input visibility file',
               'caltable': 'Name of input calibration table',
               'fluxtable': 'Name of output, flux-scaled calibration table (required)',
               'reference': 'Reference field name(s) (transfer flux scale FROM)',
               'transfer': 'Transfer field name(s) (transfer flux scale TO), \'\' -> all',
               'listfile': 'Name of listfile that contains the fit information.  Default is '' (no file).',
               'append': 'Append solutions?',
               'refspwmap': 'Scale across spectral window boundaries',
               'gainthreshold': 'Threshold (% deviation from the median) on gain amplitudes to be used in the flux scale calculation',
               'antenna': 'Select data based on antenna/baseline',
               'timerange': 'Select data based on time range',
               'scan': 'Scan number range',
               'incremental': 'Incremental caltable',
               'fitorder': 'Order of spectral fitting',
               'display': 'Display some statistics of flux scaling',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['caltable']  = ''
        a['fluxtable']  = ''
        a['reference']  = ['']
        a['transfer']  = ['']
        a['listfile']  = ''
        a['append']  = False
        a['refspwmap']  = [-1]
        a['gainthreshold']  = -1.0
        a['antenna']  = ''
        a['timerange']  = ''
        a['scan']  = ''
        a['incremental']  = False
        a['fitorder']  = 1
        a['display']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['antenna']  != '':
            a['timerange'] = ''
            a['scan'] = ''

        if a.has_key(paramname) :
              return a[paramname]
fluxscale_cli = fluxscale_cli_()
