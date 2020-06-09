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
from task_msuvbin import msuvbin
class msuvbin_cli_:
    __name__ = "msuvbin"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (msuvbin_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'field':None, 'spw':None, 'taql':None, 'outvis':None, 'phasecenter':None, 'nx':None, 'ny':None, 'cell':None, 'ncorr':None, 'nchan':None, 'fstart':None, 'fstep':None, 'wproject':None, 'memfrac':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, field=None, spw=None, taql=None, outvis=None, phasecenter=None, nx=None, ny=None, cell=None, ncorr=None, nchan=None, fstart=None, fstep=None, wproject=None, memfrac=None, ):

        """grid the visibility data onto a defined uniform grid (in the form of an ms); multiple MS\'s can be done onto the same grid

        Detailed Description:

          msuvbin is a uv gridding task. The use is for large volumes
          of data (from multiple epochs) that needs to be imaged into
          one image.  One way of proceeding is to image the epochs and
          average them after wards. Rather than doing this averaging
          the visibilities on a common uv grid has several convenience
          advantages like easily doing the proper weighted averaging and imaging.
          If an output grid already exists and a second ms is gridded on the grid
          then the output grid parameters is ignored but the existant grid is used.

  
        Arguments :
                vis: Name of input visibility file (MS)
                   Default Value: 

                field: Field selection of input ms
                   Default Value: 

                spw: Spw selection
                   Default Value: 

                taql: TaQl string for data selection
                   Default Value: 

                outvis: name of output uvgrid
                   Default Value: 

                phasecenter: phase center of uv grid
                   Default Value: 

                nx: Number of pixels of grid along the x-axis
                   Default Value: 1000

                ny: Number of pixels of grid along the y-axis
                   Default Value: 1000

                cell: pixel cell size defined in sky dimension
                   Default Value: 1arcsec

                ncorr: number of correlations to store in grid
                   Default Value: 1
                   Allowed Values:
                                1
                                2
                                4

                nchan: Number of spectral channels in grid
                   Default Value: 1

                fstart: Frequency of first spectral channel
                   Default Value: 1GHz

                fstep: spectral channel width
                   Default Value: 1kHz

                wproject: Do wprojection correction while gridding
                   Default Value: False

                memfrac: Limit how much of memory to use
                   Default Value: 0.5
                   Allowed Values:
                                0.01
                                0.99

        Returns: void

        Example :





       Keyword arguments:
       vis -- Name of input visibility file
              default: none; example: vis='ngc5921.ms'
       field -- Field name list
               default: '' ==> all
               field = '1328+307'  specifies source '1328+307'
               field = '4' specified field with index 4
       spw -- Spw selection
               default: spw = '' (all spw)
               spw='2'
       taql  --TaQl expression for data selection (see http://www.astron.nl/casacore/trunk/casacore/doc/notes/199.html)
               default taql=''
               Example select all data where U > 1 m in the ms
               taql='UVW[0] > 1'
       outvis -- name of output grid
               default: ''  The user has to give something here
       phasecenter -- phasecenter of the grid
               default= ''
                phasecenter='J2000 18h03m04 -20d00m45.1'
      nx  -- number of pixels along the x axis of the grid
               default: 1000
               nx=1200
      ny  -- number of pixels along the y axis of the grid
               default: 1000
               ny=1200
       cell -- cellsize of the grid (given in sky units)
               default: '1arcsec'
               cell='0.1arcsec'
        ncorr -- number of correlation/polarization plane in uv grid (allowed 1, 2, 4)
               default: 1
               ncorr=4
        nchan -- number of spectral channel
               default: 1
               nchan=2000
        fstart -- frequency of the first channel
               default: '1GHz';  User has to give something useful here
        fstep -- spectral channel width
               default: '1kHz'
        wproject -- do wprojection correction while gridding
                default: False
                wproject=True
        memfrac -- control how much of computer's memory is available for  gridding
                default=0.5
                memfrac=0.9

 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'msuvbin'
        self.__globals__['taskname'] = 'msuvbin'
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
            myparams['taql'] = taql = self.parameters['taql']
            myparams['outvis'] = outvis = self.parameters['outvis']
            myparams['phasecenter'] = phasecenter = self.parameters['phasecenter']
            myparams['nx'] = nx = self.parameters['nx']
            myparams['ny'] = ny = self.parameters['ny']
            myparams['cell'] = cell = self.parameters['cell']
            myparams['ncorr'] = ncorr = self.parameters['ncorr']
            myparams['nchan'] = nchan = self.parameters['nchan']
            myparams['fstart'] = fstart = self.parameters['fstart']
            myparams['fstep'] = fstep = self.parameters['fstep']
            myparams['wproject'] = wproject = self.parameters['wproject']
            myparams['memfrac'] = memfrac = self.parameters['memfrac']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['taql'] = taql
        mytmp['outvis'] = outvis
        mytmp['phasecenter'] = phasecenter
        mytmp['nx'] = nx
        mytmp['ny'] = ny
        mytmp['cell'] = cell
        mytmp['ncorr'] = ncorr
        mytmp['nchan'] = nchan
        mytmp['fstart'] = fstart
        mytmp['fstep'] = fstep
        mytmp['wproject'] = wproject
        mytmp['memfrac'] = memfrac
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'msuvbin.xml')

        casalog.origin('msuvbin')
        try :
          #if not trec.has_key('msuvbin') or not casac.casac.utils().verify(mytmp, trec['msuvbin']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['msuvbin'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('msuvbin', 'msuvbin.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'msuvbin'
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
          result = msuvbin(vis, field, spw, taql, outvis, phasecenter, nx, ny, cell, ncorr, nchan, fstart, fstep, wproject, memfrac)

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
             tname = 'msuvbin'
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
#        paramgui.runTask('msuvbin', myf['_ip'])
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
        a['taql']  = ''
        a['outvis']  = ''
        a['phasecenter']  = ''
        a['nx']  = 1000
        a['ny']  = 1000
        a['cell']  = '1arcsec'
        a['ncorr']  = 1
        a['nchan']  = 1
        a['fstart']  = '1GHz'
        a['fstep']  = '1kHz'
        a['wproject']  = False
        a['memfrac']  = 0.5


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
    def description(self, key='msuvbin', subkey=None):
        desc={'msuvbin': 'grid the visibility data onto a defined uniform grid (in the form of an ms); multiple MS\'s can be done onto the same grid',
               'vis': 'Name of input visibility file (MS)',
               'field': 'Field selection of input ms',
               'spw': 'Spw selection',
               'taql': 'TaQl string for data selection',
               'outvis': 'name of output uvgrid',
               'phasecenter': 'phase center of uv grid',
               'nx': 'Number of pixels of grid along the x-axis',
               'ny': 'Number of pixels of grid along the y-axis',
               'cell': 'pixel cell size defined in sky dimension',
               'ncorr': 'number of correlations to store in grid',
               'nchan': 'Number of spectral channels in grid',
               'fstart': 'Frequency of first spectral channel',
               'fstep': 'spectral channel width',
               'wproject': 'Do wprojection correction while gridding',
               'memfrac': 'Limit how much of memory to use',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['taql']  = ''
        a['outvis']  = ''
        a['phasecenter']  = ''
        a['nx']  = 1000
        a['ny']  = 1000
        a['cell']  = '1arcsec'
        a['ncorr']  = 1
        a['nchan']  = 1
        a['fstart']  = '1GHz'
        a['fstep']  = '1kHz'
        a['wproject']  = False
        a['memfrac']  = 0.5

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
msuvbin_cli = msuvbin_cli_()
