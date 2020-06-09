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
from task_sdgaincal import sdgaincal
class sdgaincal_cli_:
    __name__ = "sdgaincal"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (sdgaincal_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'infile':None, 'calmode':None, 'radius':None, 'smooth':None, 'antenna':None, 'field':None, 'spw':None, 'scan':None, 'intent':None, 'applytable':None, 'interp':None, 'spwmap':None, 'outfile':None, 'overwrite':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, infile=None, calmode=None, radius=None, smooth=None, antenna=None, field=None, spw=None, scan=None, intent=None, applytable=None, interp=None, spwmap=None, outfile=None, overwrite=None, ):

        """ MS SD gain calibration task

        Detailed Description:


  
        Arguments :
                infile: name of input SD dataset (must be MS)
                   Default Value: 

                calmode: gain calibration mode
                   Default Value: doublecircle
                   Allowed Values:
                                doublecircle

                radius: radius of central region to be used for calibration
                   Default Value: 

                smooth: smooth data or not
                   Default Value: True

                antenna: select data by antenna name or ID, e.g. "PM03"
                   Default Value: 

                field: select data by field IDs and names, e.g. "3C2*" ("" = all)
                   Default Value: 

                spw: select data by spw IDs (spectral windows), e.g., "3,5,7" ("" = all)
                   Default Value: 

                scan: select data by scan numbers, e.g. "21~23" (""=all)
                   Default Value: 

                intent: select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE" (""=all)
                   Default Value: 

                applytable: (List of) sky and/or tsys tables for pre-application
                   Default Value: 

                interp: Interp type in time[,freq], per gaintable. default==linear,linear
                   Default Value: 

                spwmap: Spectral windows combinations to form for gaintables(s)
                   Default Value: 

                outfile: name of output caltable
                   Default Value: 

                overwrite: overwrite the output file if already exists
                   Default Value: False

        Returns: void

        Example :

Keyword arguments:
infile -- Name of input SD dataset
calmode -- Gain calibration mode. Currently, only 'doublecircle' is supported.
        options: 'doublecircle'
        default: 'doublecircle'
    >>> calmode expandable parameter
        radius -- Radius of the central region for double circle calibration.
                  Default ('') is a radius of the primary beam. If numeric value
                  is given, it is interpreted as a value in arcsec.
                default: ''
                options: '20arcsec', 20.0
        smooth -- Whether apply smoothing during gain calibration or not.
                options: (bool) True, False
                default: True
antenna -- select data by antenna name or ID
        default: '' (use all antennas)
        example: 'PM03'
field -- select data by field IDs and names
        default: '' (use all fields)
        example: field='3C2*' (all names starting with 3C2)
                 field='0,4,5~7' (field IDs 0,4,5,6,7)
                 field='0,3C273' (field ID 0 or field named 3C273)
        this selection is in addition to the other selections to data
spw -- select data by spw IDs (spectral windows)
        NOTE this task only supports spw ID selction and ignores channel
        selection.
        default: '' (use all spws and channels)
        example: spw='3,5,7' (spw IDs 3,5,7; all channels)
                 spw='<2' (spw IDs less than 2, i.e., 0,1; all channels)
                 spw='30~45GHz' (spw IDs with the center frequencies in range 30-45GHz; all channels)
        this selection is in addition to the other selections to data
        NOTE spw input must be '' (''= all) in calmode='tsys'.
scan -- select data by scan numbers
        default: '' (use all scans)
        example: scan='21~23' (scan IDs 21,22,23)
        this selection is in addition to the other selections to data
        NOTE scan input must be '' (''= all) in calmode='tsys'.
intent -- select data by observational intent, also referred to as 'scan intent'
        default: '' (use all scan intents)
        example: intent='*ON_SOURCE*' (any valid scan-intent expression accepted by the MSSelection module can be specified)
        this selection is in addition to the other selections to data
applytable -- List of sky/Tsys calibration tables you want to pre-apply.
                default: ''
    >>> applytable expandable parameter
       interp -- Interpolation type (in time[,freq]) to use for each gaintable.
                When frequency interpolation is relevant (bandpass solutions,
                frequency-dependent polcal solutions, ALMA Tsys)
                separate time-dependent and freq-dependent interp
                types with a comma (freq _after_ the comma).
                Specifications for frequency are ignored when the
                calibration table has no channel-dependence.
                Time-dependent interp options ending in 'PD' enable a
                "phase delay" correction per spw for non-channel-dependent
                calibration types.
                For multi-obsId datasets, 'perobs' can be appended to
                the time-dependent interpolation specification to
                enforce obsId boundaries when interpolating in time.
                Add 'flag' to the freq-dependent interpolation options
                to enforce channel-dependent flagging (rather than
                interpolation/extrapolation).
                default: '' --> 'linear,linear' for all gaintable(s)
                example: interp='nearest'   (in time, freq-dep will be
                                             linear, if relevant)
                         interp='linear,cubic'  (linear in time, cubic
                                                 in freq)
                         interp='linearperobs,splineflag' (linear in time
                                                          per obsId,
                                                          spline in
                                                          freq with
                                                          channelized
                                                          flagging)
                         interp=',spline'  (spline in freq; linear in
                                            time by default)
                         interp=['nearest,spline','linear']  (for multiple gaintables)
                Options: Time: 'nearest', 'linear', 'nearestPD', 'linearPD'
                         Freq: 'nearest', 'linear', 'cubic', 'spline',
                               'nearestflag', 'linearflag', 'cubicflag', 'splineflag',

       spwmap -- Spectral windows combinations to form for gaintable(s)
               default: [] (apply solutions from each spw to that spw only)
               Example:  spwmap=[0,0,1,1] means apply the caltable solutions
                         from spw = 0 to the spw 0,1 and spw 1 to spw 2,3.
                         spwmap=[[0,0,1,1],[0,1,0,1]]  (for multiple gaintables)

          Complicated example:

            gaintable=['tab1','tab2','tab3']
            gainfield='3C286'
            interp=['linear','nearest']
            spwmap=[[],[0,0,2]]

            This means: apply 3 cal tables, selecting only solutions for 3C286
            from tab1 (but all fields from tab2 and tab3, indicated by
            no gainfield entry for these files).  Linear interpolation
            (in time) will be used for 'tab1' and 'tab3' (default); 'tab2' will
            use nearest.  For the 'tab2', the calibration spws map
            will be mapped to the data spws according to 0->0, 0->1, 2->2.
            (I.e., for data spw=0 and 2, the spw mapping is one to one,
            but data spw 1 will be calibrated by solutions from spw 0.)

outfile -- Name of output caltable.
        default: '' (<infile>_<suffix> for calibration)
overwrite -- overwrite the output caltable if already exists
        options: (bool) True,False
        default: False


DESCRIPTION:
sdgaincal computes and removes a time-dependent gain variation in single-dish
data on a per-spectral-window and per-antenna basis. Presently the task
operates only on data taken with the ALMA fast-mapped, double-circle
observation modes [1]. This task exploits the fact that the double-circle mode
observes the same position in the center of the mapped field, approximately
circular every sub-cycle, and normalizes the gains throughout the entire
dataset, relative to the measured brightness at the center position.

Note that this gain calibration task is done independently of the atmosphere
(i.e. Tsys) and sky calibration steps. This can be applied through the sdcal
task. Alternatively, you can pass those caltables to applytable parameter to
apply them on-the-fly prior to gain calibration.

Presently, this task has only one calibration mode: calmode='doublecircle'.
In this mode, the size of the region that CASA regards as "the center" is
user-configurable via the expandable 'radius' (in arcsec) parameter (under
'calmode'). The default is to use the size of the primary beam. The data can
also be smoothed in the time domain, prior to computation of the gain variation.
Selection is by specral window/channels, field IDs, and antenna through the spw,
field, and antenna selection parameters. The default is to use all data for the
gain calibration. The caltable can be output with the 'outfile' parameter.

REFERENCE:
[1] Phillips et al, 2015. Fast Single-Dish Scans of the Sun Using ALMA
  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'sdgaincal'
        self.__globals__['taskname'] = 'sdgaincal'
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

            myparams['infile'] = infile = self.parameters['infile']
            myparams['calmode'] = calmode = self.parameters['calmode']
            myparams['radius'] = radius = self.parameters['radius']
            myparams['smooth'] = smooth = self.parameters['smooth']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['applytable'] = applytable = self.parameters['applytable']
            myparams['interp'] = interp = self.parameters['interp']
            myparams['spwmap'] = spwmap = self.parameters['spwmap']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']

        if type(spwmap)==int: spwmap=[spwmap]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['calmode'] = calmode
        mytmp['radius'] = radius
        mytmp['smooth'] = smooth
        mytmp['antenna'] = antenna
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['applytable'] = applytable
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'sdgaincal.xml')

        casalog.origin('sdgaincal')
        try :
          #if not trec.has_key('sdgaincal') or not casac.casac.utils().verify(mytmp, trec['sdgaincal']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['sdgaincal'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('sdgaincal', 'sdgaincal.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'sdgaincal'
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
          result = sdgaincal(infile, calmode, radius, smooth, antenna, field, spw, scan, intent, applytable, interp, spwmap, outfile, overwrite)

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
             tname = 'sdgaincal'
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
#        paramgui.runTask('sdgaincal', myf['_ip'])
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
        a['infile']  = ''
        a['calmode']  = 'doublecircle'
        a['antenna']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['scan']  = ''
        a['applytable']  = ''
        a['outfile']  = ''
        a['overwrite']  = False

        a['calmode'] = {
                    0:odict([{'value':'doublecircle'}, {'radius':''}, {'smooth':True}])}
        a['applytable'] = {
                    0:odict([{'notvalue':''}, {'interp':''}, {'spwmap':[-1]}])}

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
    def description(self, key='sdgaincal', subkey=None):
        desc={'sdgaincal': ' MS SD gain calibration task',
               'infile': 'name of input SD dataset (must be MS)',
               'calmode': 'gain calibration mode ("doublecircle")',
               'radius': 'radius of central region to be used for calibration',
               'smooth': 'smooth data or not',
               'antenna': 'select data by antenna name or ID, e.g. "PM03"',
               'field': 'select data by field IDs and names, e.g. "3C2*" ("" = all)',
               'spw': 'select data by spw IDs (spectral windows), e.g., "3,5,7" ("" = all)',
               'scan': 'select data by scan numbers, e.g. "21~23" (""=all)',
               'intent': 'select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE" (""=all)',
               'applytable': '(List of) sky and/or tsys tables for pre-application',
               'interp': 'Interp type in time[,freq], per gaintable. default==linear,linear',
               'spwmap': 'Spectral windows combinations to form for gaintables(s)',
               'outfile': 'name of output caltable',
               'overwrite': 'overwrite the output file if already exists [True, False]',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['infile']  = ''
        a['calmode']  = 'doublecircle'
        a['radius']  = ''
        a['smooth']  = True
        a['antenna']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['scan']  = ''
        a['intent']  = ''
        a['applytable']  = ''
        a['interp']  = ''
        a['spwmap']  = []
        a['outfile']  = ''
        a['overwrite']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['calmode']  == 'doublecircle':
            a['radius'] = ''
            a['smooth'] = True

        if self.parameters['applytable']  != '':
            a['interp'] = ''
            a['spwmap'] = [-1]

        if a.has_key(paramname) :
              return a[paramname]
sdgaincal_cli = sdgaincal_cli_()
