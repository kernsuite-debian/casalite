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
from task_fixvis import fixvis
class fixvis_cli_:
    __name__ = "fixvis"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (fixvis_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'outputvis':None, 'field':None, 'refcode':None, 'reuse':None, 'phasecenter':None, 'distances':None, 'datacolumn':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, outputvis=None, field=None, refcode=None, reuse=None, phasecenter=None, distances=None, datacolumn=None, ):

        """Recalculates (u, v, w) and/or changes Phase Center 

        Detailed Description:

       Recalculates (u, v, w) and/or changes Phase Center.

       If the phase center is changed, the corresponding modifications
       are applied to the visibility columns given by the parameter
       "datacolumn" which is by default set to "all" (DATA, CORRECTED,
       and MODEL).

        Arguments :
                vis: Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'

                   Default Value: 

                outputvis: Name of output visibility file
                     Default: '' (same as vis)

                        Example: outputvis='ngc5921_out.ms'

                   Default Value: 

                field: Select field using field id(s) or field name(s)
                     Default: '' (all fields)
                     
                     Use 'go listobs' to obtain the list id's or
                     names. If field string is a non-negative integer,
                     it is assumed a field index,  otherwise, it is
                     assumed a field name.

                        Examples:
                        field='0~2'; field ids 0,1,2
                        field='0,4,5~7'; field ids 0,4,5,6,7
                        field='3C286,3C295'; field named 3C286 and
                        3C295
                        field = '3,4C*'; field id 3, all names
                        starting with 4C

                   Default Value: ""

                refcode: Reference frame to convert UVW coordinates to
                     Default: '' (refcode of PHASE_DIR in the FIELD
                     table)

                        Example: refcode='B1950'

                   Default Value: 

                reuse: Base UVW calculation on the old values?
                     Default: True
                     Options: True|False

                     Note: ignored if parameter 'phasecenter' is set

                   Default Value: True

                phasecenter: If set to a valid direction: change the phase center for
the given field to this value
                     If given without the equinox, e.g. '0h01m00s
                     +00d12m00s', the parameter is interpreted as a
                     pair of offsets in RA and DEC to the present
                     phasecenter.

                        Example: phasecenter='J2000 9h25m00s
                        -05d12m00s'

                     Note: The RA offset can be given in units of time
                     or angle. If given as a time (i.e. as a single
                     number with a time unit as in, e.g., 12s or in
                     the XXhXXmXXs or XX:XX:XX.XXX formats), it is
                     applied as is. If given as an angle (e.g.,
                     0.01deg), it is divided by the cos(DEC) before it
                     is applied.

                   Default Value: 

                distances: (experimental) List of the distances (as quanta) of the
fields selected by field.
                     Default: [] (the distances of all fields are
                     assumed to be infinity.)

                     If not a list but just a single value is given,
                     this is applied to all fields.

                        Examples: 
                        distances=['2E6km', '3E6km']   
                        distances='15au'

                   Default Value: ""

                datacolumn: when applying a phase center shift, modify visibilities
only in this/these column(s)
                     Default: 'all' (DATA, CORRECTED, and MODEL)

                        Example: datacolumn='DATA,CORRECTED' (will not
                        modify MODEL)

                   Default Value: all


        Example :


For more information, see the task pages of fixvis in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'fixvis'
        self.__globals__['taskname'] = 'fixvis'
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
            myparams['outputvis'] = outputvis = self.parameters['outputvis']
            myparams['field'] = field = self.parameters['field']
            myparams['refcode'] = refcode = self.parameters['refcode']
            myparams['reuse'] = reuse = self.parameters['reuse']
            myparams['phasecenter'] = phasecenter = self.parameters['phasecenter']
            myparams['distances'] = distances = self.parameters['distances']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['outputvis'] = outputvis
        mytmp['field'] = field
        mytmp['refcode'] = refcode
        mytmp['reuse'] = reuse
        mytmp['phasecenter'] = phasecenter
        mytmp['distances'] = distances
        mytmp['datacolumn'] = datacolumn
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'fixvis.xml')

        casalog.origin('fixvis')
        try :
          #if not trec.has_key('fixvis') or not casac.casac.utils().verify(mytmp, trec['fixvis']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['fixvis'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('fixvis', 'fixvis.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'fixvis'
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
          result = fixvis(vis, outputvis, field, refcode, reuse, phasecenter, distances, datacolumn)

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
             tname = 'fixvis'
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
#        paramgui.runTask('fixvis', myf['_ip'])
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
        a['outputvis']  = ''
        a['field']  = ""
        a['refcode']  = ''
        a['reuse']  = True
        a['phasecenter']  = ''
        a['distances']  = ""
        a['datacolumn']  = 'all'


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
    def description(self, key='fixvis', subkey=None):
        desc={'fixvis': 'Recalculates (u, v, w) and/or changes Phase Center ',
               'vis': 'Name of input visibility file',
               'outputvis': 'Name of output visibility file',
               'field': 'Select field using field id(s) or field name(s)',
               'refcode': 'reference frame to convert UVW coordinates to',
               'reuse': 'base UVW calculation on the old values?',
               'phasecenter': 'use this direction as phase center',
               'distances': '(experimental) List of the distances (as quanta) of the fields selected by field.',
               'datacolumn': 'when applying a phase center shift, modify visibilities only in this/these column(s)',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['outputvis']  = ''
        a['field']  = ""
        a['refcode']  = ''
        a['reuse']  = True
        a['phasecenter']  = ''
        a['distances']  = ""
        a['datacolumn']  = 'all'

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
fixvis_cli = fixvis_cli_()
