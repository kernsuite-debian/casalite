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
from task_accum import accum
class accum_cli_:
    __name__ = "accum"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (accum_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'tablein':None, 'incrtable':None, 'caltable':None, 'field':None, 'calfield':None, 'interp':None, 'accumtime':None, 'spwmap':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, tablein=None, incrtable=None, caltable=None, field=None, calfield=None, interp=None, accumtime=None, spwmap=None, ):

        """Accumulate incremental calibration solutions into a calibration table

        Detailed Description:

Accum will interpolate and extrapolate a calibration table onto a new
table that has a regularly-space time grid.

The first run of accum defines the time grid and fills this table with
the results from the input table.

Subsequent use of accum will combine additional calibration tables
onto the same grid of the initial accum table to obtain an output
accum table.  See below for concrete examples.

Accum tables are similar to CL tables in AIPS. Incremental tables are
similar to SN tables in AIPS.

        Arguments :
                vis: Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'

                   Default Value: 

                tablein: Input cumulative calibration table
                     Default: '' (none)

                     On first execution of accum, tablein='' and
                     accumtime is used to generate tablein with the
                     specified time gridding.

                   Default Value: 

                incrtable: The calibration data to be interpolated onto the tablein
file.
                     Default: '' (must be specified)

                   Default Value: 

                caltable: The output cumulative calibration table
                     Default: '' (use tablein as the output file)

                   Default Value: 

                field: Select field using field id(s) or field name(s)
                     Default: '' --> all fields
                     
                     Use 'go listobs' to obtain the list id's or
                     names. If field string is a non-negative
                     integer, it is assumed a field index,
                     otherwise, it is assumed a field name.

                        Examples:
                        field='0~2'; field ids 0,1,2
                        field='0,4,5~7'; field ids 0,4,5,6,7
                        field='3C286,3C295'; field named 3C286 and
                        3C295
                        field = '3,4C*'; field id 3, all names
                        starting with 4C

                   Default Value: 

                calfield: Select field(s) from incrtable to process.
                     Default: '' (all fields)

                   Default Value: 

                interp: Interpolation type (in time[,freq]) to use for each
gaintable.
                     Default: '' ('linear,linear' for all gaintable(s))
                     Options: Time: 'nearest', 'linear'
                              Freq: 'nearest', 'linear', 'cubic',
                              'spline'

                   * When frequency interpolation is relevant (B, Df,
                     Xf), separate time-dependent and freq-dependent
                     interp types with a comma (freq _after_ the
                     comma). 
                   * Specifications for frequency are ignored when the
                     calibration table has no channel-dependence.
                   * Time-dependent interp options ending in 'PD'
                     enable a "phase delay" correction per spw for
                     non-channel-dependent calibration types.
                   * For multi-obsId datasets, 'perobs' can be
                     appended to the time-dependent interpolation
                     specification to enforce obsId boundaries when
                     interpolating in time.

                        Examples: 
                        interp='nearest' (in time, freq-dep will be
                        linear, if relevant)
                        interp='linear,cubic' (linear in time, cubic
                        in freq)
                        interp='linearperobs,spline' (linear in time
                        per obsId, spline in freq)
                        interp=',spline' (spline in freq; linear in
                        time by default)
                        interp=['nearest,spline','linear'] (for
                        multiple gaintables)

                   Default Value: linear

                accumtime: The time separation when making tablein.
                     Subparameter of tablein
                     Default: 1.0  (1 second)

                     Note: This time should not be less than the
                     visibility sampling time, but should be less than
                     about 30% of a typical scan length.

                   Default Value: 1.0

                spwmap: Spectral windows combinations to form for gaintable(s)
                     Default: [] (apply solutions from each spw to
                                  that spw only)

                        Examples: 
                        spwmap=[0,0,1,1] means apply the caltable
                        solutions from spw = 0 to the spw 0,1 
                        and spw 1 to spw 2,3.
                        spwmap=[[0,0,1,1],[0,1,0,1]] (for multiple
                        gaintables)

                   Default Value: -1

        Returns: void

        Example :


For more information, see the task pages of accum in CASA Docs:

https://casa.nrao.edu/casadocs/

 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'accum'
        self.__globals__['taskname'] = 'accum'
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
            myparams['tablein'] = tablein = self.parameters['tablein']
            myparams['incrtable'] = incrtable = self.parameters['incrtable']
            myparams['caltable'] = caltable = self.parameters['caltable']
            myparams['field'] = field = self.parameters['field']
            myparams['calfield'] = calfield = self.parameters['calfield']
            myparams['interp'] = interp = self.parameters['interp']
            myparams['accumtime'] = accumtime = self.parameters['accumtime']
            myparams['spwmap'] = spwmap = self.parameters['spwmap']

        if type(field)==str: field=[field]
        if type(calfield)==str: calfield=[calfield]
        if type(spwmap)==int: spwmap=[spwmap]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['tablein'] = tablein
        mytmp['incrtable'] = incrtable
        mytmp['caltable'] = caltable
        mytmp['field'] = field
        mytmp['calfield'] = calfield
        mytmp['interp'] = interp
        mytmp['accumtime'] = accumtime
        mytmp['spwmap'] = spwmap
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'accum.xml')

        casalog.origin('accum')
        try :
          #if not trec.has_key('accum') or not casac.casac.utils().verify(mytmp, trec['accum']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['accum'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('accum', 'accum.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'accum'
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
          result = accum(vis, tablein, incrtable, caltable, field, calfield, interp, accumtime, spwmap)

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
             tname = 'accum'
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
#        paramgui.runTask('accum', myf['_ip'])
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
        a['tablein']  = ''
        a['incrtable']  = ''
        a['caltable']  = ''
        a['field']  = ['']
        a['calfield']  = ['']
        a['interp']  = 'linear'
        a['spwmap']  = [-1]

        a['tablein'] = {
                    0:odict([{'value':''}, {'accumtime':1.0}])}

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
    def description(self, key='accum', subkey=None):
        desc={'accum': 'Accumulate incremental calibration solutions into a calibration table',
               'vis': 'Name of input visibility file',
               'tablein': 'Input cumulative calibration table; use \'\' on first run',
               'incrtable': 'Input incremental calibration table to add',
               'caltable': 'Output (cumulative) calibration table',
               'field': '',
               'calfield': 'List of field names to use from incrtable.',
               'interp': 'Interpolation mode to use for resampling incrtable solutions',
               'accumtime': 'Time-interval when create cumulative table',
               'spwmap': 'Spectral window combinations to apply',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['tablein']  = ''
        a['incrtable']  = ''
        a['caltable']  = ''
        a['field']  = ['']
        a['calfield']  = ['']
        a['interp']  = 'linear'
        a['accumtime']  = 1.0
        a['spwmap']  = [-1]

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['tablein']  == '':
            a['accumtime'] = 1.0

        if a.has_key(paramname) :
              return a[paramname]
accum_cli = accum_cli_()
