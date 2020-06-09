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
from task_gencal import gencal
class gencal_cli_:
    __name__ = "gencal"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (gencal_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'caltable':None, 'caltype':None, 'infile':None, 'spw':None, 'antenna':None, 'pol':None, 'parameter':None, 'uniform':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, caltable=None, caltype=None, infile=None, spw=None, antenna=None, pol=None, parameter=None, uniform=None, ):

        """Specify Calibration Values of Various Types

        Detailed Description:

The gencal task provides a means of specifying antenna-based
calibration values manually.  The values are put in designated tables
and applied to the data using applycal. Several specialized
calibrations are also generated with gencal.

Current antenna-based gencal options (caltype) are:
* 'amp'= amplitude correction
* 'ph' = phase correction
* 'sbd'= single-band delay (phase-frequency slope for each spw)
* 'mbd'= multi-band delay (phase-frequency slope over all spw)
* 'antpos' = ITRF antenna position corrections
* 'antposvla' = VLA-centric antenna position corrections 
* 'tsys' = Tsys from the SYSCAL table (ALMA)
* 'swpow' = EVLA switched-power gains (experimental)
* 'evlagain' (='swpow') (this syntax will deprecate)
* 'rq' = EVLA requantizer gains _only_
* 'swp/rq' = EVLA switched-power gains divided by requantizer gain
* 'opac' = Tropospheric opacity
* 'gc' = Gain curve (zenith-angle-dependent gain) (VLA only)
* 'eff' = Antenna efficiency (sqrt(K/Jy)) (VLA only)
* 'gceff' = Gain curve and efficiency (VLA only)
* 'tecim' = Time-dep TEC image specified in infile
   
        Arguments :
                vis: Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'

                   Default Value: 

                caltable: Name of input calibration table
                     Default: none

                     If a calibration table does not exist, it will be
                     created. Specifying an existing table will result
                     in the parameters being applied
                     cumulatively. Only a single time-stamp for all
                     calibrations are supported, currently.  Do not
                     use a caltable created by gaincal, bandpass,
                     etc. 

                        Example: caltable='test.G'

                   Default Value: 

                caltype: The calibration parameter type being specified
                     Default: none
                     Options: 'amp', 'ph', 'sbd', 'mbd', 'antpos',
                     'antposvla', 'tsys', 'evlagain', 'opac', 'gc',
                     'gceff', 'eff', 'tecim'

                     * 'amp' = gain (G) amplitude (1 real parameter
                       per pol, antenna, spw)
                     * 'ph'  = gain (G) phase (deg) (1 real parameter
                       per pol, antenna, spw)
                     * 'sbd' = single-band delays (nsec) (1 real
                       parameter per pol, antenna, spw)
                     * 'mbd' = multi-band delay (nsec) (1 real
                       parameter per pol, antenna, spw)
                     * 'antpos' = antenna position corrections (m) (3
                       real ITRF offset parameters per antenna; spw,
                       pol selection will be ignored)
                       With antenna='', this triggers an automated
                       lookup of antenna positions for EVLA and ALMA.
                     * 'antposvla' = antenna position corrections (m)
                       specified in the old VLA-centric coordinate
                       system
                     * 'tsys' = Tsys from the SYSCAL table (ALMA)
                     * 'evlagain' = EVLA switched-power gains
                       (experimental)
                     * 'opac' = Tropospheric opacity (1 real parameter
                       per antenna, spw)
                     * 'gc' = Antenna zenith-angle dependent gain
                       curve (auto-lookup)
                     * 'gceff' = Gain curve and efficiency
                       (auto-lookup)
                     * 'eff' = Antenna efficiency (auto-lookup)

                        Example: caltype='ph'

                   Default Value: 
                   Allowed Values:
                                amp
                                ph
                                sbd
                                mbd
                                antpos
                                antposvla
                                tsys
                                evlagain
                                swpow
                                rq
                                swp/rq
                                opac
                                gc
                                gceff
                                eff
                                tecim

                infile: Input ancilliary file
                    Subparameter of caltype='gc|gceff|tecim'
                    Default: none

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

                   Default Value: 

                antenna: Select data based on antenna/baseline
                     Subparameter of selectdata=True
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

                pol: Polarization selection for specified parameters
                     Default: pol='' (specified parameters apply to
                     all polarizations)

                        Example: pol='R' (specified parameters to
                        apply to R only)

                   Default Value: 

                parameter: The calibration values

                     The calibration parameters, specified as a list,
                     to store in the caltable for the spw, antenna,
                     and pol selection.  The required length of the
                     list is determined by the caltype and the spw,
                     antenna, pol selection.  One "set" of parameters
                     (e.g., one value for 'amp', 'ph', etc., three
                     values for 'antpos') specified the same value for
                     all indicated spw, antenna, and pol.
                     OR, 
                     When specifying a long list of calibration
                     parameter values, these should be ordered first
                     (fastest) by pol (if pol!=''), then by antenna
                     (if antenna!=''), and finally (sloweset) by spw
                     (if spw!='').  Unspecified selection axes must
                     not be enumerated in the parameter list

                   Default Value: 

                uniform: Assume uniform calibration values across the array
                    Subparameter of caltype='tsys'
                     Default: True
                     Options: True|False

                   Default Value: True

        Returns: void

        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF GENCAL IN CASA DOCS:
https://casa.nrao.edu/casadocs/
 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'gencal'
        self.__globals__['taskname'] = 'gencal'
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
            myparams['caltype'] = caltype = self.parameters['caltype']
            myparams['infile'] = infile = self.parameters['infile']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['pol'] = pol = self.parameters['pol']
            myparams['parameter'] = parameter = self.parameters['parameter']
            myparams['uniform'] = uniform = self.parameters['uniform']

        if type(parameter)==float: parameter=[parameter]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['caltable'] = caltable
        mytmp['caltype'] = caltype
        mytmp['infile'] = infile
        mytmp['spw'] = spw
        mytmp['antenna'] = antenna
        mytmp['pol'] = pol
        mytmp['parameter'] = parameter
        mytmp['uniform'] = uniform
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'gencal.xml')

        casalog.origin('gencal')
        try :
          #if not trec.has_key('gencal') or not casac.casac.utils().verify(mytmp, trec['gencal']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['gencal'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('gencal', 'gencal.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'gencal'
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
          result = gencal(vis, caltable, caltype, infile, spw, antenna, pol, parameter, uniform)

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
             tname = 'gencal'
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
#        paramgui.runTask('gencal', myf['_ip'])
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
        a['caltype']  = ''
        a['spw']  = ''
        a['antenna']  = ''
        a['pol']  = ''
        a['parameter']  = []

        a['caltype'] = {
                    0:odict([{'value':'tecim'}, {'infile':''}]), 
                    1:odict([{'value':'gc'}, {'infile':''}]), 
                    2:odict([{'value':'gceff'}, {'infile':''}]), 
                    3:odict([{'value':'tsys'}, {'uniform':True}])}

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
    def description(self, key='gencal', subkey=None):
        desc={'gencal': 'Specify Calibration Values of Various Types',
               'vis': 'Name of input visibility file',
               'caltable': 'Name of input calibration table',
               'caltype': 'The calibration type: (amp, ph, sbd, mbd, antpos, antposvla, tsys, evlagain, opac, gc, gceff, eff, tecim)',
               'infile': 'Input ancilliary file',
               'spw': 'Select spectral window/channels',
               'antenna': 'Select data based on antenna/baseline',
               'pol': 'Calibration polarizations(s) selection',
               'parameter': 'The calibration values',
               'uniform': 'Assume uniform calibration values across the array',

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
        a['caltype']  = ''
        a['infile']  = ''
        a['spw']  = ''
        a['antenna']  = ''
        a['pol']  = ''
        a['parameter']  = []
        a['uniform']  = True

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['caltype']  == 'tecim':
            a['infile'] = ''

        if self.parameters['caltype']  == 'gc':
            a['infile'] = ''

        if self.parameters['caltype']  == 'gceff':
            a['infile'] = ''

        if self.parameters['caltype']  == 'tsys':
            a['uniform'] = True

        if a.has_key(paramname) :
              return a[paramname]
gencal_cli = gencal_cli_()
