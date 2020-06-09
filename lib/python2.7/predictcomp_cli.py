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
from task_predictcomp import predictcomp
class predictcomp_cli_:
    __name__ = "predictcomp"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (predictcomp_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'objname':None, 'standard':None, 'epoch':None, 'minfreq':None, 'maxfreq':None, 'nfreqs':None, 'prefix':None, 'antennalist':None, 'showplot':None, 'savefig':None, 'symb':None, 'include0amp':None, 'include0bl':None, 'blunit':None, 'showbl0flux':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, objname=None, standard=None, epoch=None, minfreq=None, maxfreq=None, nfreqs=None, prefix=None, antennalist=None, showplot=None, savefig=None, symb=None, include0amp=None, include0bl=None, blunit=None, showbl0flux=None, ):

        """Make a component list for a known calibrator

        Detailed Description:

          Writes a component list named clist to disk and returns a dict of
          {'clist': clist,
           'objname': objname,
           'standard': standard,
           'epoch': epoch,
           'freqs': pl.array of frequencies, in GHz,
           'antennalist': a simdata type configuration file,
           'amps':  pl.array of predicted visibility amplitudes, in Jy,
           'savedfig': False or, if made, the filename of a plot.}
          or False on error.
  
        Arguments :
                objname: Object name
                   Default Value: 

                standard: Flux density standard
                   Default Value: Butler-JPL-Horizons 2010
                   Allowed Values:
                                Perley-Butler 2017
                                Perley-Butler 2013
                                Perley-Butler 2010
                                Perley-Taylor 99
                                Baars
                                Perley 90
                                Perley-Taylor 95
                                Butler-JPL-Horizons 2010
                                Butler-JPL-Horizons 2012

                epoch: Epoch
                   Default Value: 

                minfreq: Minimum frequency
                   Default Value: 

                maxfreq: Maximum frequency
                   Default Value: 

                nfreqs: Number of frequencies
                   Default Value: 2

                prefix: Prefix for the component list directory name.
                   Default Value: 

                antennalist: Plot for this configuration
                   Default Value: 

                showplot: Plot S vs |u| to the screen?
                   Default Value: False

                savefig: Save a plot of S vs |u| to this filename
                   Default Value: 

                symb: A matplotlib plot symbol code
                   Default Value: .

                include0amp: Force the amplitude axis to start at 0?
                   Default Value: False

                include0bl: Force the baseline axis to start at 0?
                   Default Value: False

                blunit: unit of the baseline axis
                   Default Value: 
                   Allowed Values:
                                
                                klambda

                showbl0flux: Print the zero baseline flux ?
                   Default Value: False

        Returns: record

        Example :


    Writes a component list to disk and returns a dict of
    {'clist': filename of the component list,
     'objname': objname,
     'angdiam': angular diameter in radians (if used in clist),
     'standard': standard,
     'epoch': epoch,
     'freqs': pl.array of frequencies, in GHz,
     'antennalist': pl.array of baseline lengths, in m,
     'amps':  pl.array of predicted visibility amplitudes, in Jy,
     'savedfig': False or, if made, the filename of a plot.}
    or False on error.

    objname: An object supported by standard.
    standard: A standard for calculating flux densities, as in setjy.
              Default: 'Butler-JPL-Horizons 2010'
    epoch: The epoch to use for the calculations.   Irrelevant for
           extrasolar standards. (Uses UTC)
           Examples: '2011-12-31/5:34:12', '2011-12-31-5:34:12'
    minfreq: The minimum frequency to use.
             Example: '342.0GHz'
    maxfreq: The maximum frequency to use.
             Default: minfreq
             Example: '346.0GHz'
             Example: '', anything <= 0, or None: use minfreq.
    nfreqs:  The number of frequencies to use.
             Default: 1 if minfreq == maxfreq,
                      2 otherwise.
    prefix: The component list will be saved to
               prefix + 'spw0_<objname>_<minfreq><epoch>.cl'
            Default: '' 
            Example: "Bands3to7_"
                     (which could produce 'Bands3to7_Uranus_spw0_100GHz55877d.cl',
                      depending on the other parameters)
    antennalist: 'Observe' and plot the visibility amplitudes for this
                 antenna configuration.  The file should be in a format usable
                 by simdata.  The search path is:
                     .:casa['dirs']['data'] + '/alma/simmos/'
             Default: '' (None, just make clist.)
             Example: 'alma.cycle0.extended.cfg'

    Subparameters of antennalist:
    showplot: Whether or not to show a plot of S vs. |u| on screen.
              Subparameter of antennalist.
              Default: Necessarily False if antennalist is not specified.
                       True otherwise.
    savefig: Filename for saving a plot of S vs. |u|.
             Subparameter of antennalist.
             Default: '' 
             Examples: ''           (do not save the plot)
                       'myplot.png' (save to myplot.png)
    symb: One of matplotlib's codes for plot symbols: .:,o^v<>s+xDd234hH|_
          Default: '.'
    include0amp: Force the amplitude axis to start at 0?
                 Default: False
    include0bl: Force the baseline axis to start at 0?
                Default: False
    blunit: unit of the baseline axis ('' or 'klambda')
            Default:''=use a unit in the data
    showbl0flux: Print the zero baseline flux? 
                 Default: False 

     

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'predictcomp'
        self.__globals__['taskname'] = 'predictcomp'
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

            myparams['objname'] = objname = self.parameters['objname']
            myparams['standard'] = standard = self.parameters['standard']
            myparams['epoch'] = epoch = self.parameters['epoch']
            myparams['minfreq'] = minfreq = self.parameters['minfreq']
            myparams['maxfreq'] = maxfreq = self.parameters['maxfreq']
            myparams['nfreqs'] = nfreqs = self.parameters['nfreqs']
            myparams['prefix'] = prefix = self.parameters['prefix']
            myparams['antennalist'] = antennalist = self.parameters['antennalist']
            myparams['showplot'] = showplot = self.parameters['showplot']
            myparams['savefig'] = savefig = self.parameters['savefig']
            myparams['symb'] = symb = self.parameters['symb']
            myparams['include0amp'] = include0amp = self.parameters['include0amp']
            myparams['include0bl'] = include0bl = self.parameters['include0bl']
            myparams['blunit'] = blunit = self.parameters['blunit']
            myparams['showbl0flux'] = showbl0flux = self.parameters['showbl0flux']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['objname'] = objname
        mytmp['standard'] = standard
        mytmp['epoch'] = epoch
        mytmp['minfreq'] = minfreq
        mytmp['maxfreq'] = maxfreq
        mytmp['nfreqs'] = nfreqs
        mytmp['prefix'] = prefix
        mytmp['antennalist'] = antennalist
        mytmp['showplot'] = showplot
        mytmp['savefig'] = savefig
        mytmp['symb'] = symb
        mytmp['include0amp'] = include0amp
        mytmp['include0bl'] = include0bl
        mytmp['blunit'] = blunit
        mytmp['showbl0flux'] = showbl0flux
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'predictcomp.xml')

        casalog.origin('predictcomp')
        try :
          #if not trec.has_key('predictcomp') or not casac.casac.utils().verify(mytmp, trec['predictcomp']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['predictcomp'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('predictcomp', 'predictcomp.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'predictcomp'
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
          result = predictcomp(objname, standard, epoch, minfreq, maxfreq, nfreqs, prefix, antennalist, showplot, savefig, symb, include0amp, include0bl, blunit, showbl0flux)

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
             tname = 'predictcomp'
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
#        paramgui.runTask('predictcomp', myf['_ip'])
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
        a['objname']  = ''
        a['standard']  = 'Butler-JPL-Horizons 2010'
        a['epoch']  = ''
        a['minfreq']  = ''
        a['maxfreq']  = ''
        a['nfreqs']  = 2
        a['prefix']  = ''
        a['antennalist']  = ''
        a['symb']  = '.'

        a['antennalist'] = {
                    0:odict([{'notvalue':''}, {'showplot':True}, {'savefig':''}, {'symb':'.'}, {'include0amp':False}, {'include0bl':False}, {'blunit':''}, {'showbl0flux':False}])}

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
    def description(self, key='predictcomp', subkey=None):
        desc={'predictcomp': 'Make a component list for a known calibrator',
               'objname': 'Object name',
               'standard': 'Flux density standard',
               'epoch': 'Epoch',
               'minfreq': 'Minimum frequency',
               'maxfreq': 'Maximum frequency',
               'nfreqs': 'Number of frequencies',
               'prefix': 'Prefix for the component list directory name.',
               'antennalist': 'Plot for this configuration',
               'showplot': 'Plot S vs |u| to the screen?',
               'savefig': 'Save a plot of S vs |u| to this filename',
               'symb': 'A matplotlib plot symbol code',
               'include0amp': 'Force the amplitude axis to start at 0?',
               'include0bl': 'Force the baseline axis to start at 0?',
               'blunit': 'unit of the baseline axis',
               'showbl0flux': 'Print the zero baseline flux ?',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['objname']  = ''
        a['standard']  = 'Butler-JPL-Horizons 2010'
        a['epoch']  = ''
        a['minfreq']  = ''
        a['maxfreq']  = ''
        a['nfreqs']  = 2
        a['prefix']  = ''
        a['antennalist']  = ''
        a['showplot']  = False
        a['savefig']  = ''
        a['symb']  = '.'
        a['include0amp']  = False
        a['include0bl']  = False
        a['blunit']  = ''
        a['showbl0flux']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['antennalist']  != '':
            a['showplot'] = True
            a['savefig'] = ''
            a['symb'] = '.'
            a['include0amp'] = False
            a['include0bl'] = False
            a['blunit'] = ''
            a['showbl0flux'] = False

        if a.has_key(paramname) :
              return a[paramname]
predictcomp_cli = predictcomp_cli_()
