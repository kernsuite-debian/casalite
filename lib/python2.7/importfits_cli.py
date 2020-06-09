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
from task_importfits import importfits
class importfits_cli_:
    __name__ = "importfits"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (importfits_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'fitsimage':None, 'imagename':None, 'whichrep':None, 'whichhdu':None, 'zeroblanks':None, 'overwrite':None, 'defaultaxes':None, 'defaultaxesvalues':None, 'beam':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, fitsimage=None, imagename=None, whichrep=None, whichhdu=None, zeroblanks=None, overwrite=None, defaultaxes=None, defaultaxesvalues=None, beam=None, ):

        """Convert an image FITS file into a CASA image

        Detailed Description:

Convert an image FITS file into a CASA image

        Arguments :
                fitsimage: Name of input image FITS file
                     Default: none

                        Example: fitsimage='3C273XC1.fits'

                   Default Value: 

                imagename: Name of output CASA image
                     Default: none

                        Example: fitsimage='3C273XC1.image'

                   Default Value: 

                whichrep: If fits image has multiple coordinate reps, choose one.
                     Default: 0 (means first)

                        Example: whichrep=1

                   Default Value: 0

                whichhdu: If fits file contains multiple images, choose one
                     Default: -1 (use the first valid one)

                     NOTE: 0 = first HDU, -1 = first valid image

                        Example: whichhdu=1

                   Default Value: -1

                zeroblanks: Set blanked pixels to zero (not NaN)
                     Default: True
                     Options: True|False

                   Default Value: True

                overwrite: Overwrite output file if it exists?
                     Default: False
                     Options: False|True

                   Default Value: False

                defaultaxes: Add the default 4D coordinate axes where they are
missing
                     Default: False
                     Options: False|True

                     IMPORTANT: value True requires setting defaultaxesvalues

                   Default Value: False

                defaultaxesvalues: List of values to assign to added degenerate axes when
defaultaxes==True (ra,dec,freq,stokes)
                     Default: []

                     For existing axes, empty strings can be given as
                     values. For the directions and spectral values,
                     any valid angle/frequency expressions can be
                     given.

                        Example: defaultaxesvalues=['19h30m00',
                        '-02d30m00', '88.5GHz', 'Q'] 

                   Default Value: []

                beam: List of values to be used to define the synthesized beam
[BMAJ,BMIN,BPA] (as in the FITS keywords)
                     Default: [] (i.e.take from FITS file)

                        Example: beam=['0.35arcsec', '0.24arcsec',
                        '25deg']

                   Default Value: []


        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTFITS IN CASA DOCS:
https://casa.nrao.edu/casadocs/
 
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'importfits'
        self.__globals__['taskname'] = 'importfits'
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

            myparams['fitsimage'] = fitsimage = self.parameters['fitsimage']
            myparams['imagename'] = imagename = self.parameters['imagename']
            myparams['whichrep'] = whichrep = self.parameters['whichrep']
            myparams['whichhdu'] = whichhdu = self.parameters['whichhdu']
            myparams['zeroblanks'] = zeroblanks = self.parameters['zeroblanks']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['defaultaxes'] = defaultaxes = self.parameters['defaultaxes']
            myparams['defaultaxesvalues'] = defaultaxesvalues = self.parameters['defaultaxesvalues']
            myparams['beam'] = beam = self.parameters['beam']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['fitsimage'] = fitsimage
        mytmp['imagename'] = imagename
        mytmp['whichrep'] = whichrep
        mytmp['whichhdu'] = whichhdu
        mytmp['zeroblanks'] = zeroblanks
        mytmp['overwrite'] = overwrite
        mytmp['defaultaxes'] = defaultaxes
        mytmp['defaultaxesvalues'] = defaultaxesvalues
        mytmp['beam'] = beam
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'importfits.xml')

        casalog.origin('importfits')
        try :
          #if not trec.has_key('importfits') or not casac.casac.utils().verify(mytmp, trec['importfits']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['importfits'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('importfits', 'importfits.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'importfits'
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
          result = importfits(fitsimage, imagename, whichrep, whichhdu, zeroblanks, overwrite, defaultaxes, defaultaxesvalues, beam)

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
             tname = 'importfits'
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
#        paramgui.runTask('importfits', myf['_ip'])
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
        a['fitsimage']  = ''
        a['imagename']  = ''
        a['whichrep']  = 0
        a['whichhdu']  = -1
        a['zeroblanks']  = True
        a['overwrite']  = False
        a['defaultaxes']  = False
        a['defaultaxesvalues']  = []
        a['beam']  = []


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
    def description(self, key='importfits', subkey=None):
        desc={'importfits': 'Convert an image FITS file into a CASA image',
               'fitsimage': 'Name of input image FITS file',
               'imagename': 'Name of output CASA image',
               'whichrep': 'If fits image has multiple coordinate reps, choose one.',
               'whichhdu': 'If fits file contains multiple images, choose one (0 = first HDU, -1 = first valid image).',
               'zeroblanks': 'Set blanked pixels to zero (not NaN)',
               'overwrite': 'Overwrite output file if it exists?',
               'defaultaxes': 'Add the default 4D coordinate axes where they are missing; value True requires setting defaultaxesvalues',
               'defaultaxesvalues': 'List of values to assign to added degenerate axes when defaultaxes==True (ra,dec,freq,stokes)',
               'beam': 'List of values to be used to define the synthesized beam [BMAJ,BMIN,BPA] (as in the FITS keywords)',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['fitsimage']  = ''
        a['imagename']  = ''
        a['whichrep']  = 0
        a['whichhdu']  = -1
        a['zeroblanks']  = True
        a['overwrite']  = False
        a['defaultaxes']  = False
        a['defaultaxesvalues']  = []
        a['beam']  = []

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
importfits_cli = importfits_cli_()
