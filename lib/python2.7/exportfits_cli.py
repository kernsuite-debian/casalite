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
from task_exportfits import exportfits
class exportfits_cli_:
    __name__ = "exportfits"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (exportfits_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'fitsimage':None, 'velocity':None, 'optical':None, 'bitpix':None, 'minpix':None, 'maxpix':None, 'overwrite':None, 'dropstokes':None, 'stokeslast':None, 'history':None, 'dropdeg':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, fitsimage=None, velocity=None, optical=None, bitpix=None, minpix=None, maxpix=None, overwrite=None, dropstokes=None, stokeslast=None, history=None, dropdeg=None, ):

        """Convert a CASA image to a FITS file

        Detailed Description:

CASA-produced images can be exported as FITS files for transporting to
other software packages or publication.  
No subimaging of the fits image can be made with this task.
The spectral reference frame can be changed prior to export using the
task imreframe.

        Arguments :
                imagename: Name of input CASA image
                     Default: none

                        Example: fitsimage='3C273XC1.image'

                   Default Value: 

                fitsimage: Name of output image FITS file
                     Default: none

                        Example: fitsimage='3C273XC1.fits'

                   Default Value: 

                velocity: Use velocity (rather than frequency) as spectral axis
                     Default: False
                     Options: False|True

                   Default Value: False

                optical: Use the optical (rather than radio) velocity convention
                     Default: False
                     Options: False|True

                   Default Value: False

                bitpix: Bits per pixel
                     Default: -32

                        Example: bitpix=16

                   Default Value: -32
                   Allowed Values:
                                -32
                                16

                minpix: Minimum pixel value (if minpix > maxpix, value is automatically determined)
                   Default Value: 0

                maxpix: Maximum pixel value (if minpix > maxpix, value is
automatically determined)
                     Default: -1

                   Default Value: -1

                overwrite: Overwrite output file if it exists?
                     Default: False
                     Options: False|True

                   Default Value: False

                dropstokes: Drop the Stokes axis?
                   Default Value: False

                stokeslast: Put Stokes axis last in header?
                     Default: True
                     Options: True|False

                   Default Value: True

                history: Write history to the FITS image?
                     Default: True
                     Options: True|False

                   Default Value: True

                dropdeg: Drop all degenerate axes (e.g. Stokes and/or Frequency)?
                     Default: False
                     Options: False|True

                   Default Value: False


        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF EXPORTFITS IN CASA DOCS:
https://casa.nrao.edu/casadocs/

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'exportfits'
        self.__globals__['taskname'] = 'exportfits'
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

            myparams['imagename'] = imagename = self.parameters['imagename']
            myparams['fitsimage'] = fitsimage = self.parameters['fitsimage']
            myparams['velocity'] = velocity = self.parameters['velocity']
            myparams['optical'] = optical = self.parameters['optical']
            myparams['bitpix'] = bitpix = self.parameters['bitpix']
            myparams['minpix'] = minpix = self.parameters['minpix']
            myparams['maxpix'] = maxpix = self.parameters['maxpix']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['dropstokes'] = dropstokes = self.parameters['dropstokes']
            myparams['stokeslast'] = stokeslast = self.parameters['stokeslast']
            myparams['history'] = history = self.parameters['history']
            myparams['dropdeg'] = dropdeg = self.parameters['dropdeg']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['fitsimage'] = fitsimage
        mytmp['velocity'] = velocity
        mytmp['optical'] = optical
        mytmp['bitpix'] = bitpix
        mytmp['minpix'] = minpix
        mytmp['maxpix'] = maxpix
        mytmp['overwrite'] = overwrite
        mytmp['dropstokes'] = dropstokes
        mytmp['stokeslast'] = stokeslast
        mytmp['history'] = history
        mytmp['dropdeg'] = dropdeg
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'exportfits.xml')

        casalog.origin('exportfits')
        try :
          #if not trec.has_key('exportfits') or not casac.casac.utils().verify(mytmp, trec['exportfits']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['exportfits'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('exportfits', 'exportfits.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'exportfits'
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
          result = exportfits(imagename, fitsimage, velocity, optical, bitpix, minpix, maxpix, overwrite, dropstokes, stokeslast, history, dropdeg)

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
             tname = 'exportfits'
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
#        paramgui.runTask('exportfits', myf['_ip'])
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
        a['imagename']  = ''
        a['fitsimage']  = ''
        a['velocity']  = False
        a['optical']  = False
        a['bitpix']  = -32
        a['minpix']  = 0
        a['maxpix']  = -1
        a['overwrite']  = False
        a['dropstokes']  = False
        a['stokeslast']  = True
        a['history']  = True
        a['dropdeg']  = False


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
    def description(self, key='exportfits', subkey=None):
        desc={'exportfits': 'Convert a CASA image to a FITS file',
               'imagename': 'Name of input CASA image',
               'fitsimage': 'Name of output image FITS file',
               'velocity': 'Use velocity (rather than frequency) as spectral axis',
               'optical': 'Use the optical (rather than radio) velocity convention',
               'bitpix': 'Bits per pixel',
               'minpix': 'Minimum pixel value (if minpix > maxpix, value is automatically determined)',
               'maxpix': 'Maximum pixel value (if minpix > maxpix, value is automatically determined)',
               'overwrite': 'Overwrite output file if it exists?',
               'dropstokes': 'Drop the Stokes axis?',
               'stokeslast': 'Put Stokes axis last in header?',
               'history': 'Write history to the FITS image?',
               'dropdeg': 'Drop all degenerate axes (e.g. Stokes and/or Frequency)?',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['fitsimage']  = ''
        a['velocity']  = False
        a['optical']  = False
        a['bitpix']  = -32
        a['minpix']  = 0
        a['maxpix']  = -1
        a['overwrite']  = False
        a['dropstokes']  = False
        a['stokeslast']  = True
        a['history']  = True
        a['dropdeg']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
exportfits_cli = exportfits_cli_()
