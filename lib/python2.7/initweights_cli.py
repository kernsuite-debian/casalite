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
from task_initweights import initweights
class initweights_cli_:
    __name__ = "initweights"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (initweights_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'wtmode':None, 'tsystable':None, 'gainfield':None, 'interp':None, 'spwmap':None, 'dowtsp':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, wtmode=None, tsystable=None, gainfield=None, interp=None, spwmap=None, dowtsp=None, ):

        """Initializes weight information in the MS
        Arguments :
                vis: Name of input visibility file (MS)
                   Default Value: 

                wtmode: Initialization mode
                   Default Value: nyq
                   Allowed Values:
                                nyq
                                sigma
                                weight
                                ones
                                delwtsp
                                delsigsp
                                tsys
                                tinttsys

                tsystable: Tsys calibration table to apply on the fly
                   Default Value: 

                gainfield: Select a subset of calibrators from Tsys table
                   Default Value: 

                interp: Interpolation type in time[,freq]. default==\'linear,linear\'
                   Default Value: 

                spwmap: Spectral windows combinations to form for gaintable(s)
                   Default Value: 

                dowtsp: Initialize the WEIGHT_SPECTRUM column
                   Default Value: False

        Returns: void

        Example :


      This task provides for initialization of the weight information
      in the MS.  For ALMA interferometry and EVLA data, it should not
      generally be necessary to use this task, as the weight information 
      should have been initialized properly at fill time (v4.2.2 and later).

      Several initialization modes are supported via the wtmode parameter.

      If wtmode='nyq' (the default), SIGMA and WEIGHT will be
      initialized according to bandwidth and integration time.  This
      is the theoretically correct mode for raw normalized visibilities.
      (e.g., ALMA).  For the EVLA, this is correct if switched-power
      and bandpass calibration will later be applied.  

      If wtmode='sigma', WEIGHT will be initialized according to the
      existing SIGMA column.  

      If wtmode='weight', WEIGHT_SPECTRUM will be initialized according
      to the existing WEIGHT column; dowtspec=T must be specified in
      this case.
 
      If wtmode='ones', SIGMA and WEIGHT will be initialized with 1.0,
      globally.  This is a traditional means of initializing weight
      information, and is adequate when the integration time and 
      bandwidth are uniform. It is not recommended for modern
      instruments (ALMA, EVLA), where variety in observational setups
      is common, and properly initialized and calibrated weights
      will be used for imaging sensitivity estimates.

      There are two EXPERIMENTAL modes, wtmode='tsys' and 'tinttsys'.
      In the modes, SIGMA and WEIGHT will be initialized according to
      Tsys, bandwidth, and integration time (used only in 'tinttsys'),
      i.e.,
          tsys    : weight=bw/Tsys^2
          tinttsys: weight=bw*t_int/Tsys^2
      These modes use Tsys values to calculate weight as is done in
      Tsys calibration. Tsys values are taken from a tsys calibration
      table given as tsystable. Selection of gain field (gainfield),
      interpolation method (interp), and spectral window mapping (spwmap)
      are supported, too.
      Available types of interpolation are,
          Time: 'nearest', 'linear', the variation of those with 'perobs',
                e.g., 'linearperobs' (enforce obsId boundaries in interpolation)
          Freq: 'nearest', 'linear', 'cubic', 'spline', and the variation
                of those with 'flag', e.g., 'linearflag' (with
                channelized flag).
      See the help of applycal for details of interpolations.
      Note if the weight in an MS is initialized with these modes and
      Tsys calibration table is applied with calwt=True after that, the
      weight would be contaminated by being devided by square of Tsys
      twice.
      !!! USERS ARE ADVICED TO USE THESE EXPERIMENTAL MODES WITH CARE !!!

      For the above wtmodes, if dowtsp=T (or if the WEIGHT_SPECTRUM
      column already exists), the WEIGHT_SPECTRUM column will be
      initialized (uniformly in channel in wtmode='nyq', 'sigma',
      'weight', and 'ones'), in a manner consistent with the
      disposition of the WEIGHT column.  If the WEIGHT_SPECTRUM 
      column does not exist, dowtsp=T will force its creation.
      Use of the WEIGHT_SPECTRUM column is only meaningful
      for ALMA data which will be calibrated with channelized
      Tsys information, or if the weights will become channelized
      after calibration, e.g., via averaging over time- and 
      channel-dependent flagging.  (A task for channel-dependent
      weight estimation from the data itself is also currently under
      development).
      In non-channelized modes (wtmode='nyq', 'sigma', 'weight', and
      'ones') or when dowtsp=F, SIGMA_SPECTRUM column will be removed
      from MS. On the other hand, SIGMA_SPECTRUM column is added and
      initialized in channelized modes (wtmode='tsys' and 'tinttsys')
      if dowtsp=T or WEIGHT_SPECTRUM already column exists.

      Two additional modes are available for managing the spectral
      weight info columns; these should be used with extreme care: If
      wtmode='delwtsp', the WEIGHT_SPECTRUM column will be deleted (if
      it exists).  If wtmode='delsigsp', the SIGMA_SPECTRUM column
      will be deleted (if it exists).  Note that creation of
      SIGMA_SPECTRUM is not supported via this method.

      Note that this task does not support any prior selection.  
      Intialization of the weight information must currently be done 
      globally or not at all.  This is to maintain consistency.

 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'initweights'
        self.__globals__['taskname'] = 'initweights'
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
            myparams['wtmode'] = wtmode = self.parameters['wtmode']
            myparams['tsystable'] = tsystable = self.parameters['tsystable']
            myparams['gainfield'] = gainfield = self.parameters['gainfield']
            myparams['interp'] = interp = self.parameters['interp']
            myparams['spwmap'] = spwmap = self.parameters['spwmap']
            myparams['dowtsp'] = dowtsp = self.parameters['dowtsp']

        if type(spwmap)==int: spwmap=[spwmap]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['wtmode'] = wtmode
        mytmp['tsystable'] = tsystable
        mytmp['gainfield'] = gainfield
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        mytmp['dowtsp'] = dowtsp
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'initweights.xml')

        casalog.origin('initweights')
        try :
          #if not trec.has_key('initweights') or not casac.casac.utils().verify(mytmp, trec['initweights']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['initweights'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('initweights', 'initweights.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'initweights'
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
          result = initweights(vis, wtmode, tsystable, gainfield, interp, spwmap, dowtsp)

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
             tname = 'initweights'
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
#        paramgui.runTask('initweights', myf['_ip'])
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
        a['wtmode']  = 'nyq'
        a['dowtsp']  = False

        a['wtmode'] = {
                    0:{'value':'nyq'}, 
                    1:{'value':'sigma'}, 
                    2:{'value':'weight'}, 
                    3:{'value':'ones'}, 
                    4:{'value':'delwtsp'}, 
                    5:{'value':'delsigsp'}, 
                    6:odict([{'value':'tsys'}, {'tsystable':''}, {'gainfield':''}, {'interp':''}, {'spwmap':[]}]), 
                    7:odict([{'value':'tinttsys'}, {'tsystable':''}, {'gainfield':''}, {'interp':''}, {'spwmap':[]}])}

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
    def description(self, key='initweights', subkey=None):
        desc={'initweights': 'Initializes weight information in the MS',
               'vis': 'Name of input visibility file (MS)',
               'wtmode': 'Initialization mode',
               'tsystable': 'Tsys calibration table to apply on the fly',
               'gainfield': 'Select a subset of calibrators from Tsys table',
               'interp': 'Interpolation type in time[,freq]. default==\'linear,linear\'',
               'spwmap': 'Spectral windows combinations to form for gaintable(s)',
               'dowtsp': 'Initialize the WEIGHT_SPECTRUM column',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['wtmode']  = 'nyq'
        a['tsystable']  = ''
        a['gainfield']  = ''
        a['interp']  = ''
        a['spwmap']  = []
        a['dowtsp']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['wtmode']  == 'tsys':
            a['tsystable'] = ''
            a['gainfield'] = ''
            a['interp'] = ''
            a['spwmap'] = []

        if self.parameters['wtmode']  == 'tinttsys':
            a['tsystable'] = ''
            a['gainfield'] = ''
            a['interp'] = ''
            a['spwmap'] = []

        if a.has_key(paramname) :
              return a[paramname]
initweights_cli = initweights_cli_()
