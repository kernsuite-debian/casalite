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
from task_uvcontsub import uvcontsub
class uvcontsub_cli_:
    __name__ = "uvcontsub"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (uvcontsub_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'field':None, 'fitspw':None, 'excludechans':None, 'combine':None, 'solint':None, 'fitorder':None, 'spw':None, 'want_cont':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, field=None, fitspw=None, excludechans=None, combine=None, solint=None, fitorder=None, spw=None, want_cont=None, ):

        """Continuum fitting and subtraction in the uv plane

        Detailed Description:



        Arguments :
                vis: Name of input MS.  Output goes to vis + ".contsub" (will be overwritten if already exists)
                   Default Value: 

                field: Select field(s) using id(s) or name(s)
                   Default Value: 

                fitspw: Spectral window:channel selection for fitting the continuum
                   Default Value: 

                excludechans: exclude Spectral window:channel selection in fitspw for fitting
                   Default Value: False

                combine: Data axes to combine for the continuum estimation (none, or spw and/or scan)
                   Default Value: 

                solint: Continuum fit timescale (int recommended!)
                   Default Value: int

                fitorder: Polynomial order for the fits
                   Default Value: 0

                spw: Spectral window selection for output
                   Default Value: 

                want_cont: Create vis + ".cont" to hold the continuum estimate.
                   Default Value: False


        Example :


        Continuum fitting and subtraction in the uv plane:
            
        This task estimates the continuum emission by fitting polynomials to
        the real and imaginary parts of the spectral windows and channels
        selected by fitspw.  This fit represents a model of the continuum in 
        all channels.

        The fitted continuum spectrum is subtracted from all channels 
        selected in spw, and the result (presumably only line emission)
        is stored in a new MS (vis + ".contsub"). If an MS  
        with the output name already exists, it will be overwritten.
        It will read from the CORRECTED_DATA column of vis if it is present,
        or DATA if it is not.  Whichever column is read is presumed to have
        already been calibrated.

        If want_cont is True, the continuum fit is placed in a second new MS
        (vis + '.cont', also overwritten if it already exists).  
        N.B. because the continuum model is necessarily a
        smoothed fit, images made with it are liable to have their field of
        view reduced in some strange way.  Images of the continuum should be
        made by simply excluding the line channels (and probably averaging the
        remaining ones) in clean.

        Keyword arguments:
        vis -- Name of input visibility file
                default: none; example: vis='ngc5921.ms'
        field -- Field selection for continuum estimation and subtraction.
                 The estimation and subtraction is done for each selected field
                 in turn.  (Run listobs to get lists of the ID and names.)
                default: field = '' means select all fields
                field = 1 # will get field_id=1 (if you give it an 
                        integer, it will retrieve the source with that index.
                field = '1328+307'  specifies source '1328+307'
                field = '13*' will retrieve '1328+307' and any other fields
                   beginning with '13'
        fitspw -- Selection of spectral windows and channels to use in the
                  fit for the continuum, using general spw:chan syntax.
                  The ranges of channels also can be specified by frequencies as in
                  the MS selection syntax (spw ids are required but '*' can be 
                  used, see the example below).
                  See the note under combine.
                default: '' (all)
                example: fitspw='0:5~30;40~55'
                                 --> select the ranges by channels in the spw id 0 
                         fitspw='0:5~30;40~55,1:10~25;45~58,2'
                                 --> select channel ranges 5-30 and 40-55 for the spw id 0, 
                                        10-25 and 45-58 for spwid 1, and use all channels for the spw id 2
                         fitspw='0:113.767~114.528GHz;114.744~115.447GHz'
                                 --> select the ranges by frequencies in the spw id 0 
                         fitspw='0:113.767~114.528GHz;114.744~115.447GHz,1:111.892~112.654GHz;112.868~113.025GHz'
                                 --> select the different ranges by frequencies for the spw ids 0 and 1 
                         fitspw='*:113.767~114.528GHz;114.744~115.447GHz'
                                 --> select the same frequency ranges for all the relevant spws 
         >>> expandable parameter for fitspw 
          excludechans - if True, it will exclude the spws:channels specified in fitspw
                         for the fit
                default: False (use fitspw for the fit) 
                example: fitspw='0:114.528GHz~114.744GHz'; excludechans=True
                         --> exclude the frequency range, 114.528GHz - 114.744GHz in the spw id 0
        combine -- Data axes to combine for the continuum estimate.
                It must include 'spw' if spw contains spws that are not in
                fitspw!
                default: '' --> solutions will break at scan, field, and spw
                      boundaries according to solint
              Options: '', 'spw'', 'scan', or 'spw, scan'
              example: combine='spw' --> form spw-merged continuum estimate
        solint -- Timescale for per-baseline fit (units optional)
                default (recommended): 'int' --> no time averaging, do a
                                       fit for each integration and let the
                                       noisy fits average out in the image.

                example: solint='10s'  --> average to 10s before fitting
                         10 or '10' --> '10s' (unitless: assumes seconds)
                options: 'int' --> per integration
                         'inf' --> per scan

                If solint is longer than 'int', the continuum estimate can be
                corrupted by time smearing!

        fitorder -- Polynomial order for the fits of the continuum w.r.t.
                    frequency.  fitorders > 1 are strongly discouraged
                    because high order polynomials have more flexibility, may
                    absorb line emission, and tend go wild at the edges of
                    fitspw, which is not what you want.

                default: 0 (constant); example: fitorder=1

        spw -- Optional per spectral window selection of channels to include
               in the output.  See the note under combine.

               The spectral windows will be renumbered to start from 0, as in
               split.
        want_cont -- Create vis + '.cont' to hold the continuum estimate.
                default: 'False'; example: want_cont=True
                The continuum estimate will be placed in vis + '.cont'
        async -- Run task in a separate process (return CASA prompt)
                default: False; example: async=True


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'uvcontsub'
        self.__globals__['taskname'] = 'uvcontsub'
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
            myparams['field'] = field = self.parameters['field']
            myparams['fitspw'] = fitspw = self.parameters['fitspw']
            myparams['excludechans'] = excludechans = self.parameters['excludechans']
            myparams['combine'] = combine = self.parameters['combine']
            myparams['solint'] = solint = self.parameters['solint']
            myparams['fitorder'] = fitorder = self.parameters['fitorder']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['want_cont'] = want_cont = self.parameters['want_cont']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['fitspw'] = fitspw
        mytmp['excludechans'] = excludechans
        mytmp['combine'] = combine
        mytmp['solint'] = solint
        mytmp['fitorder'] = fitorder
        mytmp['spw'] = spw
        mytmp['want_cont'] = want_cont
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'uvcontsub.xml')

        casalog.origin('uvcontsub')
        try :
          #if not trec.has_key('uvcontsub') or not casac.casac.utils().verify(mytmp, trec['uvcontsub']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['uvcontsub'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('uvcontsub', 'uvcontsub.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'uvcontsub'
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
          result = uvcontsub(vis, field, fitspw, excludechans, combine, solint, fitorder, spw, want_cont)

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
             tname = 'uvcontsub'
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
#        paramgui.runTask('uvcontsub', myf['_ip'])
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
        a['field']  = ''
        a['fitspw']  = ''
        a['combine']  = ''
        a['solint']  = 'int'
        a['fitorder']  = 0
        a['spw']  = ''
        a['want_cont']  = False

        a['fitspw'] = {
                    0:odict([{'notvalue':''}, {'excludechans':False}])}

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
    def description(self, key='uvcontsub', subkey=None):
        desc={'uvcontsub': 'Continuum fitting and subtraction in the uv plane',
               'vis': 'Name of input MS.  Output goes to vis + ".contsub" (will be overwritten if already exists)',
               'field': 'Select field(s) using id(s) or name(s)',
               'fitspw': 'Spectral window:channel selection for fitting the continuum',
               'excludechans': 'exclude Spectral window:channel selection in fitspw for fitting',
               'combine': 'Data axes to combine for the continuum estimation (none, or spw and/or scan)',
               'solint': 'Continuum fit timescale (int recommended!)',
               'fitorder': 'Polynomial order for the fits',
               'spw': 'Spectral window selection for output',
               'want_cont': 'Create vis + ".cont" to hold the continuum estimate.',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['field']  = ''
        a['fitspw']  = ''
        a['excludechans']  = False
        a['combine']  = ''
        a['solint']  = 'int'
        a['fitorder']  = 0
        a['spw']  = ''
        a['want_cont']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['fitspw']  != '':
            a['excludechans'] = False

        if a.has_key(paramname) :
              return a[paramname]
uvcontsub_cli = uvcontsub_cli_()
