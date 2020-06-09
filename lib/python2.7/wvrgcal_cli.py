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
from task_wvrgcal import wvrgcal
class wvrgcal_cli_:
    __name__ = "wvrgcal"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (wvrgcal_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'caltable':None, 'toffset':None, 'segsource':None, 'sourceflag':None, 'tie':None, 'nsol':None, 'disperse':None, 'wvrflag':None, 'statfield':None, 'statsource':None, 'smooth':None, 'scale':None, 'spw':None, 'wvrspw':None, 'reversespw':None, 'cont':None, 'maxdistm':None, 'minnumants':None, 'mingoodfrac':None, 'usefieldtab':None, 'refant':None, 'offsetstable':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, caltable=None, toffset=None, segsource=None, sourceflag=None, tie=None, nsol=None, disperse=None, wvrflag=None, statfield=None, statsource=None, smooth=None, scale=None, spw=None, wvrspw=None, reversespw=None, cont=None, maxdistm=None, minnumants=None, mingoodfrac=None, usefieldtab=None, refant=None, offsetstable=None, ):

        """Generate a gain table based on Water Vapour Radiometer data

        Detailed Description:


Information about the observation and the performance of WVRGCAL is written to the CASA logger
and also returned in a dictionary; see the CASA cookbook for a more detailed description of these parameters.
The dictionary element 'success' is True if no errors occured.

Of particular note is the discrepancy parameter (Disc): high values (&gt; a few hundred microns) 
may indicate some levels of cloud contamination and the effect of applying the WVRGCAL correction 
should be checked; values &gt; 1000 um in all antennas have currently been found to indicate that 
WVRGCAL correction should not be used.

      
  vis -- Name of input visibility file
              default: none; example: vis='ngc5921.ms'

  caltable -- Name of output gain calibration table
              default: none; example: caltable='ngc5921.wvr'

  toffset -- Time offset (sec) between interferometric and WVR data
             default: 0 (ALMA default for cycle 1, for cycle 0, i.e. up to Jan 2013 it was -1)

  segsource -- Do a new coefficient calculation for each source
               default: True

  tie -- Prioritise tieing the phase of these sources as well as possible
         (requires segsource=True)
         default: [] example: ['3C273,NGC253', 'IC433,3C279']

  sourceflag -- Flag the WVR data for these source(s) as bad and do not produce corrections for it
               (requires segsource=True)
               default: [] (none) example: ['3C273']

  nsol -- Number of solutions for phase correction coefficients during this observation.
          By default only one set of coefficients is generated for the entire observation. 
          If more sets are requested, then they will be evenly distributed in time throughout 
          the observation. Values &gt; 1 require segsource=False.
          default: 1

  disperse -- Apply correction for dispersion
             default: False

  wvrflag -- Regard the WVR data for these antenna(s) as bad and use interpolated values instead
             default: [] (none) example: ['DV03','DA05','PM02']           

  statfield -- Compute the statistics (Phase RMS, Disc) on this field only
               default: '' (all) 

  statsource -- Compute the statistics (Phase RMS, Disc) on this source only
                default: '' (all)             

  smooth -- Smooth the calibration solution on the given timescale 
            default: '' (no smoothing), example: '3s' smooth on a timescale of 3 seconds

  scale -- Scale the entire phase correction by this factor
           default: 1. (no scaling)

  spw -- List of the spectral window IDs for which solutions should be saved into the caltable
           default: [] (all spectral windows), example [17,19,21,23]

  wvrspw -- List of the spectral window IDs from which the WVR data should be taken
           default: [] (all WVR spectral windows), example [0]

  reversespw -- Reverse the sign of the correction for the listed SPWs
                (only neede for early ALMA data before Cycle 0)
                default: '' (none), example: reversespw='0~2,4'; spectral windows 0,1,2,4

  cont -- Estimate the continuum (e.g., due to clouds)
          default: False

  maxdistm -- maximum distance (m) an antenna may have to be considered for being part
              of the antenna set (minnumants to 3 antennas) for the interpolation of a solution 
              for a flagged antenna
              default: 500.

  minnumants -- minimum number of near antennas required for interpolation
                default: 2

  mingoodfrac -- If the fraction of unflagged data for an antenna is below this value (0. to 1.), 
                 the antenna is flagged.
                 default: 0.8

  usefieldtab -- derive the antenna AZ/EL values from the FIELD rather than the POINTING table
                 default: False

  refant -- use the WVR data from this antenna for calculating the dT/dL parameters (can give ranked list)
                default: '' (use the first good or interpolatable antenna), 
                examples: 'DA45' - use DA45 
                          ['DA45','DV51'] - use DA45 and if that is not good, use DV51 instead

  offsetstable -- (experimental) subtract the temperature offsets in this table from the WVR measurements before
             using them to calculate the phase corrections
                default: '' (do not apply any offsets)
                examples: 'uid___A002_Xabd867_X2277.cloud_offsets' use the given table

  
        Arguments :
                vis: Name of input visibility file
                   Default Value: 

                caltable: Name of output gain calibration table
                   Default Value: 

                toffset: Time offset (sec) between interferometric and WVR data
                   Default Value: 0

                segsource: Do a new coefficient calculation for each source
                   Default Value: True

                sourceflag: Regard the WVR data for these source(s) as bad and do not produce corrections for it (requires segsource=True)
                   Default Value: 

                tie: Prioritise tieing the phase of these sources as well as possible (requires segsource=True)
                   Default Value: 

                nsol: Number of solutions for phase correction coefficients (nsol>1 requires segsource=False)
                   Default Value: 1

                disperse: Apply correction for dispersion
                   Default Value: False

                wvrflag: Regard the WVR data for these antenna(s) as bad and replace its data with interpolated values from neighbouring antennas
                   Default Value: 

                statfield: Compute the statistics (Phase RMS, Disc) on this field only
                   Default Value: 

                statsource: Compute the statistics (Phase RMS, Disc) on this source only
                   Default Value: 

                smooth: Smooth calibration solution on the given timescale
                   Default Value: 

                scale: Scale the entire phase correction by this factor
                   Default Value: 1.

                spw: List of the spectral window IDs for which solutions should be saved into the caltable
                   Default Value: 

                wvrspw: List of the spectral window IDs from which the WVR data should be taken
                   Default Value: 

                reversespw: Reverse the sign of the correction for the listed SPWs (only needed for early ALMA data before Cycle 0)
                   Default Value: 

                cont: Estimate the continuum (e.g., due to clouds) (experimental)
                   Default Value: False

                maxdistm: maximum distance (m) of an antenna used for interpolation for a flagged antenna
                   Default Value: 500.

                minnumants: minimum number of near antennas (up to 3) required for interpolation
                   Default Value: 2
                   Allowed Values:
                                1
                                2
                                3

                mingoodfrac: If the fraction of unflagged data for an antenna is below this value (0. to 1.), the antenna is flagged.
                   Default Value: 0.8

                usefieldtab: derive the antenna AZ/EL values from the FIELD rather than the POINTING table
                   Default Value: False

                refant: use the WVR data from this antenna for calculating the dT/dL parameters (can give ranked list)
                   Default Value: 

                offsetstable: (experimental) subtract the temperature offsets in this table from the WVR measurements before calculating the phase corrections
                   Default Value: 

        Returns: variant

        Example :


   wvrgcal(vis='uid___A002_X1d54a1_X5.ms', caltable='cal-wvr-uid___A002_X1d54a1_X5.W',
           toffset=-1, segsource=True, tie=['Titan,1037-295,NGC3256'], statsource='1037-295')

  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'wvrgcal'
        self.__globals__['taskname'] = 'wvrgcal'
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
            myparams['toffset'] = toffset = self.parameters['toffset']
            myparams['segsource'] = segsource = self.parameters['segsource']
            myparams['sourceflag'] = sourceflag = self.parameters['sourceflag']
            myparams['tie'] = tie = self.parameters['tie']
            myparams['nsol'] = nsol = self.parameters['nsol']
            myparams['disperse'] = disperse = self.parameters['disperse']
            myparams['wvrflag'] = wvrflag = self.parameters['wvrflag']
            myparams['statfield'] = statfield = self.parameters['statfield']
            myparams['statsource'] = statsource = self.parameters['statsource']
            myparams['smooth'] = smooth = self.parameters['smooth']
            myparams['scale'] = scale = self.parameters['scale']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['wvrspw'] = wvrspw = self.parameters['wvrspw']
            myparams['reversespw'] = reversespw = self.parameters['reversespw']
            myparams['cont'] = cont = self.parameters['cont']
            myparams['maxdistm'] = maxdistm = self.parameters['maxdistm']
            myparams['minnumants'] = minnumants = self.parameters['minnumants']
            myparams['mingoodfrac'] = mingoodfrac = self.parameters['mingoodfrac']
            myparams['usefieldtab'] = usefieldtab = self.parameters['usefieldtab']
            myparams['refant'] = refant = self.parameters['refant']
            myparams['offsetstable'] = offsetstable = self.parameters['offsetstable']

        if type(sourceflag)==str: sourceflag=[sourceflag]
        if type(tie)==str: tie=[tie]
        if type(wvrflag)==str: wvrflag=[wvrflag]
        if type(spw)==int: spw=[spw]
        if type(wvrspw)==int: wvrspw=[wvrspw]
        if type(refant)==str: refant=[refant]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['caltable'] = caltable
        mytmp['toffset'] = toffset
        mytmp['segsource'] = segsource
        mytmp['sourceflag'] = sourceflag
        mytmp['tie'] = tie
        mytmp['nsol'] = nsol
        mytmp['disperse'] = disperse
        mytmp['wvrflag'] = wvrflag
        mytmp['statfield'] = statfield
        mytmp['statsource'] = statsource
        mytmp['smooth'] = smooth
        mytmp['scale'] = scale
        mytmp['spw'] = spw
        mytmp['wvrspw'] = wvrspw
        mytmp['reversespw'] = reversespw
        mytmp['cont'] = cont
        mytmp['maxdistm'] = maxdistm
        mytmp['minnumants'] = minnumants
        mytmp['mingoodfrac'] = mingoodfrac
        mytmp['usefieldtab'] = usefieldtab
        mytmp['refant'] = refant
        mytmp['offsetstable'] = offsetstable
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'wvrgcal.xml')

        casalog.origin('wvrgcal')
        try :
          #if not trec.has_key('wvrgcal') or not casac.casac.utils().verify(mytmp, trec['wvrgcal']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['wvrgcal'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('wvrgcal', 'wvrgcal.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'wvrgcal'
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
          result = wvrgcal(vis, caltable, toffset, segsource, sourceflag, tie, nsol, disperse, wvrflag, statfield, statsource, smooth, scale, spw, wvrspw, reversespw, cont, maxdistm, minnumants, mingoodfrac, usefieldtab, refant, offsetstable)

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
             tname = 'wvrgcal'
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
#        paramgui.runTask('wvrgcal', myf['_ip'])
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
        a['toffset']  = 0
        a['segsource']  = True
        a['disperse']  = False
        a['wvrflag']  = ['']
        a['statfield']  = ''
        a['statsource']  = ''
        a['smooth']  = ''
        a['scale']  = 1.
        a['spw']  = []
        a['wvrspw']  = []
        a['reversespw']  = ''
        a['cont']  = False
        a['maxdistm']  = 500.
        a['minnumants']  = 2
        a['mingoodfrac']  = 0.8
        a['usefieldtab']  = False
        a['refant']  = ['']
        a['offsetstable']  = ''

        a['segsource'] = {
                    0:odict([{'value':True}, {'tie':[]}, {'sourceflag':[]}]), 
                    1:odict([{'value':False}, {'nsol':1}])}

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
    def description(self, key='wvrgcal', subkey=None):
        desc={'wvrgcal': 'Generate a gain table based on Water Vapour Radiometer data',
               'vis': 'Name of input visibility file',
               'caltable': 'Name of output gain calibration table',
               'toffset': 'Time offset (sec) between interferometric and WVR data',
               'segsource': 'Do a new coefficient calculation for each source',
               'sourceflag': 'Regard the WVR data for these source(s) as bad and do not produce corrections for it (requires segsource=True)',
               'tie': 'Prioritise tieing the phase of these sources as well as possible (requires segsource=True)',
               'nsol': 'Number of solutions for phase correction coefficients (nsol>1 requires segsource=False)',
               'disperse': 'Apply correction for dispersion',
               'wvrflag': 'Regard the WVR data for these antenna(s) as bad and replace its data with interpolated values from neighbouring antennas',
               'statfield': 'Compute the statistics (Phase RMS, Disc) on this field only',
               'statsource': 'Compute the statistics (Phase RMS, Disc) on this source only',
               'smooth': 'Smooth calibration solution on the given timescale',
               'scale': 'Scale the entire phase correction by this factor',
               'spw': 'List of the spectral window IDs for which solutions should be saved into the caltable',
               'wvrspw': 'List of the spectral window IDs from which the WVR data should be taken',
               'reversespw': 'Reverse the sign of the correction for the listed SPWs (only needed for early ALMA data before Cycle 0)',
               'cont': 'Estimate the continuum (e.g., due to clouds) (experimental)',
               'maxdistm': 'maximum distance (m) of an antenna used for interpolation for a flagged antenna',
               'minnumants': 'minimum number of near antennas (up to 3) required for interpolation',
               'mingoodfrac': 'If the fraction of unflagged data for an antenna is below this value (0. to 1.), the antenna is flagged.',
               'usefieldtab': 'derive the antenna AZ/EL values from the FIELD rather than the POINTING table',
               'refant': 'use the WVR data from this antenna for calculating the dT/dL parameters (can give ranked list)',
               'offsetstable': '(experimental) subtract the temperature offsets in this table from the WVR measurements before calculating the phase corrections',

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
        a['toffset']  = 0
        a['segsource']  = True
        a['sourceflag']  = ['']
        a['tie']  = ['']
        a['nsol']  = 1
        a['disperse']  = False
        a['wvrflag']  = ['']
        a['statfield']  = ''
        a['statsource']  = ''
        a['smooth']  = ''
        a['scale']  = 1.
        a['spw']  = []
        a['wvrspw']  = []
        a['reversespw']  = ''
        a['cont']  = False
        a['maxdistm']  = 500.
        a['minnumants']  = 2
        a['mingoodfrac']  = 0.8
        a['usefieldtab']  = False
        a['refant']  = ['']
        a['offsetstable']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['segsource']  == True:
            a['tie'] = []
            a['sourceflag'] = []

        if self.parameters['segsource']  == False:
            a['nsol'] = 1

        if a.has_key(paramname) :
              return a[paramname]
wvrgcal_cli = wvrgcal_cli_()
