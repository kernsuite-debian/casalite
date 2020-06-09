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
from task_specflux import specflux
class specflux_cli_:
    __name__ = "specflux"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (specflux_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'region':None, 'box':None, 'chans':None, 'stokes':None, 'mask':None, 'stretch':None, 'function':None, 'unit':None, 'major':None, 'minor':None, 'logfile':None, 'overwrite':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, region=None, box=None, chans=None, stokes=None, mask=None, stretch=None, function=None, unit=None, major=None, minor=None, logfile=None, overwrite=None, ):

        """Report spectral profile and calculate spectral flux over a user specified region
        Arguments :
                imagename: Name of the input image
                   Default Value: 

                region: Region selection. Default is to use the full image.
                   Default Value: 

                box: Rectangular region to select in direction plane. Default is to use the entire direction plane.
                   Default Value: 

                chans: Channels to use. Default is to use all channels.
                   Default Value: 

                stokes: Stokes planes to use. Default is to use all Stokes planes.
                   Default Value: 

                mask: Mask to use. Default is none.
                   Default Value: 

                stretch: Stretch the mask if necessary and possible? 
                   Default Value: False

                function: Aggregate function to use for computing per channel values. Supported values are "flux density", "mean", "median", "sum". Minimal match supported.
                   Default Value: flux density

                unit: Unit to use for the spectral flux calculation. Must be conformant with a typical spectral axis unit.
                   Default Value: km/s

                major: Major axis of overriding restoring beam. If specified, must be a valid quantity.
                   Default Value: 

                minor: Minor axis of overriding restoring beam. If specified, must be a valid quantity
                   Default Value: 

                logfile: File which to write details. Default is to not write to a file.
                   Default Value: 

                overwrite: Overwrite exisitng ouput file if it exists?
                   Default Value: False

        Returns: record

        Example :

PARAMETER SUMMARY
imagename        Name of the input (CASA, FITS, MIRIAD) image
region           Region selection. Default is to use
                 the full image.
box              Rectangular region to select in direction plane.
                 for details. Default is to use the entire direction plane.
chans            Channels to use. Default is to use
                 all channels.
stokes           Stokes planes to use. Default is to use
                 all Stokes planes.
mask             Mask to use. Default is none.
stretch          Stretch the input mask if necessary and possible. Only used if a mask is specified.

function         Aggregate function to use for computing per channel values. Supported values are
                 "flux density", "mean", "median", "sum". Minimal match supported.
unit             Unit to use for the spectral flux calculation. Must be conformant with a typical
                 spectral axis unit (ie something conformant with a velocity, frequency, or length).
                 Velocity units may only be used if the spectral coordinate has a rest frequency and
                 if it is > 0.
major            Major axis of overriding restoring beam. If specified, must be a valid quantity
                 If specified, minor must also be specified. The overriding beam is used for computing
                 flux and flux density values. Ignored if the image brightness units do not contain
                 "/beam". Example "4arcsec".
minor            Minor axis of overriding restoring beam. If specified, must be a valid quantity.
                 If specified, major must also be specified. See help on parameter major for details.
                 Example: "3arcsec".
logfile          Name of file to which to write tabular output. Default is to not write to a file.
overwrite        Controls if an already existing log file by the
                 same name can be overwritten. If true, the user is not prompted, the file
                 if it exists is automatically overwritten.

This application retrieves details of an image spectrum which has been integrated over a specified
region (or the entire image if no region has been specified).

One may specify which function to use to aggregate pixel values using the function parameter. Supported
values are "flux density", "mean", "median", and "sum". Minimal match is supported.

The spectral flux is reported in units flux density consistent with the image brightness unit times the
specified spectral unit (eg, Jy*km/s, K*arcsec2*km/s). If the units are K*arcsec2..., multiply the
reported value by 2.3504430539098e-8*d*d, where d is the distance in pc, to convert to units of K*pc2...
If provided, major and minor will be used to compute the beam size, and hence the per channel flux
densities (if function="flux density"), overriding the input image beam information, if present.

# write spectrum to file that has been integrated over
# rectangular region, using only pixels with non-negative values.
# if the log file already exists, overwrite it with the new data.
specflux(imagename="my.im", box="10,10,45,50", mask="my.im>=0", unit="km/s", logfile="my.log", overwrite=True)

# Extract the spectral profile using "sum" as the aggregate function from a cube over a given region:
specflux(imagename="myimage.image", box="10,10,45,50", mask="my.im>=0", function="sum", unit="km/s", logfile="profile.log", overwrite=True)

# Calculate the integrated line flux over a given region and channel range
# (this value will be reported as "Total Flux" in the output of specflux)
specflux(imagename="myimage.image", region="myregion.crtf", chans="14~25", unit="km/s", logfile="integrated_line_flux.log", overwrite=True)


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'specflux'
        self.__globals__['taskname'] = 'specflux'
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
            myparams['region'] = region = self.parameters['region']
            myparams['box'] = box = self.parameters['box']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['stretch'] = stretch = self.parameters['stretch']
            myparams['function'] = function = self.parameters['function']
            myparams['unit'] = unit = self.parameters['unit']
            myparams['major'] = major = self.parameters['major']
            myparams['minor'] = minor = self.parameters['minor']
            myparams['logfile'] = logfile = self.parameters['logfile']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['stretch'] = stretch
        mytmp['function'] = function
        mytmp['unit'] = unit
        mytmp['major'] = major
        mytmp['minor'] = minor
        mytmp['logfile'] = logfile
        mytmp['overwrite'] = overwrite
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'specflux.xml')

        casalog.origin('specflux')
        try :
          #if not trec.has_key('specflux') or not casac.casac.utils().verify(mytmp, trec['specflux']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['specflux'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('specflux', 'specflux.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'specflux'
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
          result = specflux(imagename, region, box, chans, stokes, mask, stretch, function, unit, major, minor, logfile, overwrite)

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
             tname = 'specflux'
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
#        paramgui.runTask('specflux', myf['_ip'])
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
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['function']  = 'flux density'
        a['unit']  = 'km/s'
        a['major']  = ''
        a['minor']  = ''
        a['logfile']  = ''

        a['logfile'] = {
                    0:odict([{'notvalue':''}, {'overwrite':False}])}
        a['mask'] = {
                    0:odict([{'notvalue':''}, {'stretch':False}])}

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
    def description(self, key='specflux', subkey=None):
        desc={'specflux': 'Report spectral profile and calculate spectral flux over a user specified region',
               'imagename': 'Name of the input image',
               'region': 'Region selection. Default is to use the full image.',
               'box': 'Rectangular region to select in direction plane. Default is to use the entire direction plane.',
               'chans': 'Channels to use. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Default is to use all Stokes planes.',
               'mask': 'Mask to use. Default is none.',
               'stretch': 'Stretch the mask if necessary and possible? ',
               'function': 'Aggregate function to use for computing per channel values. Supported values are "flux density", "mean", "median", "sum". Minimal match supported.',
               'unit': 'Unit to use for the spectral flux calculation. Must be conformant with a typical spectral axis unit.',
               'major': 'Major axis of overriding restoring beam. If specified, must be a valid quantity.',
               'minor': 'Minor axis of overriding restoring beam. If specified, must be a valid quantity',
               'logfile': 'File which to write details. Default is to not write to a file.',
               'overwrite': 'Overwrite exisitng ouput file if it exists?',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['stretch']  = False
        a['function']  = 'flux density'
        a['unit']  = 'km/s'
        a['major']  = ''
        a['minor']  = ''
        a['logfile']  = ''
        a['overwrite']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['logfile']  != '':
            a['overwrite'] = False

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if a.has_key(paramname) :
              return a[paramname]
specflux_cli = specflux_cli_()
