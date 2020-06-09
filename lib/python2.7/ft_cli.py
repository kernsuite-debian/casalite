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
from task_ft import ft
class ft_cli_:
    __name__ = "ft"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (ft_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'field':None, 'spw':None, 'model':None, 'nterms':None, 'reffreq':None, 'complist':None, 'incremental':None, 'usescratch':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, field=None, spw=None, model=None, nterms=None, reffreq=None, complist=None, incremental=None, usescratch=None, ):

        """Insert a source model as a visibility set

        Detailed Description:

A source model (souce.model image) or components list is converted
into model visibilities that is inserted into the MODEL_DATA column or
alternatively is stored  in the header of the MS to be served on the
fly when requested. 

Setjy will automatically make this ft step on the sources currently
available, which are 3C48, 3C138, 3C147, 3C286 at 1.4, 5.0, 8.4, 15,
22, 43 GHz.  Their location is site dependent.  In Charlottesville and
Socorro, the models are in
/usr/lib(lib64)/casapy/data/nrao/VLA/CalModels.

        Arguments :
                vis: Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'

                   Default Value: 

                field: Select field using field id(s) or field name(s)
                     Default: '' (all fields)
                     
                     BUT, only one source can be specified in a
                     multi-source vis.


                        Examples: 
                        field = '1328+307'  specifies source
                        '1328+307'
                        field = '4' specified field with index 4

                   Default Value: 

                spw: Select spectral window/channels
                     Default: '' (all spectral windows and channels)
      
                   Default Value: 

                model: Name of input model image(s)
                     Default: '' (none)

                        Example:
                        model='/usr/lib/casapy/data/nrao/VLA/CalModels/3C286_X.im'

                     NOTE: The model visibilities are scaled from the
                     model frequency to the observed frequency of the
                     data.

                   Default Value: 

                nterms: Number of terms used to model the sky frequency
dependence
                     Default: 1 (one model image is required)

                        Example: nterms=3 - represents a 2nd order
                        Taylor-polynomial in frequency and should be
                        used in conjuction with coefficient model
                        images as
                        model=['xxx.model.tt0','xxx.model.tt1',
                        'xxx.model.tt2']

                   Default Value: 1

                reffreq: Reference-frequency about which this Taylor-expansion is
defined.
                     Default: '' (reads the reference frequency from
                     the model image)

                        Example: reffreq = '1.5GHz'

                   Default Value: 

                complist: Name of component list
                     Default: none

                        Example: complist='test.cl'

                     WARNING: component lists are difficult to make

                   Default Value: 

                incremental: Add model visibility to the existing model visibilties
stored in the MS
                     Default: False
                     Options: False|True

                   Default Value: False

                usescratch: Story visibilities in MODEL_DATA column?
                     Default: False
                     Options: False|True

                     If True, model visibilities will be stored in the
                     scratch column MODEL_DATA; if False, the model
                     visibilities will be generated  on the fly (this
                     mode may save some disk space equivalent to the
                     volume of the observed data).

                   Default Value: False

        Returns: void

        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF FT IN CASA DOCS:
https://casa.nrao.edu/casadocs/
 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'ft'
        self.__globals__['taskname'] = 'ft'
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
            myparams['spw'] = spw = self.parameters['spw']
            myparams['model'] = model = self.parameters['model']
            myparams['nterms'] = nterms = self.parameters['nterms']
            myparams['reffreq'] = reffreq = self.parameters['reffreq']
            myparams['complist'] = complist = self.parameters['complist']
            myparams['incremental'] = incremental = self.parameters['incremental']
            myparams['usescratch'] = usescratch = self.parameters['usescratch']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['model'] = model
        mytmp['nterms'] = nterms
        mytmp['reffreq'] = reffreq
        mytmp['complist'] = complist
        mytmp['incremental'] = incremental
        mytmp['usescratch'] = usescratch
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'ft.xml')

        casalog.origin('ft')
        try :
          #if not trec.has_key('ft') or not casac.casac.utils().verify(mytmp, trec['ft']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['ft'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('ft', 'ft.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'ft'
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
          result = ft(vis, field, spw, model, nterms, reffreq, complist, incremental, usescratch)

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
             tname = 'ft'
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
#        paramgui.runTask('ft', myf['_ip'])
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
        a['spw']  = ''
        a['model']  = ''
        a['nterms']  = 1
        a['complist']  = ''
        a['incremental']  = False
        a['usescratch']  = False

        a['nterms'] = {
                    0:odict([{'notvalue':1}, {'reffreq':''}])}

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
    def description(self, key='ft', subkey=None):
        desc={'ft': 'Insert a source model as a visibility set',
               'vis': 'Name of input visibility file',
               'field': 'Select field using field id(s) or field name(s)',
               'spw': 'Select spectral window/channels',
               'model': 'Name of input model image(s)',
               'nterms': 'Number of terms used to model the sky frequency dependence',
               'reffreq': 'Reference frequency (e.g. \'1.5e+9\' or \'1.5GHz\')',
               'complist': 'Name of component list',
               'incremental': 'Add to the existing model visibility?',
               'usescratch': 'If True, predicted  visibility  is stored in MODEL_DATA column',

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
        a['spw']  = ''
        a['model']  = ''
        a['nterms']  = 1
        a['reffreq']  = ''
        a['complist']  = ''
        a['incremental']  = False
        a['usescratch']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['nterms']  != 1:
            a['reffreq'] = ''

        if a.has_key(paramname) :
              return a[paramname]
ft_cli = ft_cli_()
