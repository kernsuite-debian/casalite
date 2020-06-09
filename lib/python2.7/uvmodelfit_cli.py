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
from task_uvmodelfit import uvmodelfit
class uvmodelfit_cli_:
    __name__ = "uvmodelfit"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (uvmodelfit_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'field':None, 'spw':None, 'selectdata':None, 'timerange':None, 'uvrange':None, 'antenna':None, 'scan':None, 'msselect':None, 'niter':None, 'comptype':None, 'sourcepar':None, 'varypar':None, 'outfile':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, field=None, spw=None, selectdata=None, timerange=None, uvrange=None, antenna=None, scan=None, msselect=None, niter=None, comptype=None, sourcepar=None, varypar=None, outfile=None, ):

        """Fit a single component source model to the uv data

        Detailed Description:

        Fit a single component source model to the uv data

        Arguments :
                vis: Name of input visibility file
                   Default Value: 

                field: Select field using field id(s) or field name(s)
                   Default Value: 

                spw: Select spectral window/channels
                   Default Value: 

                selectdata: Other data selection parameters
                   Default Value: True

                timerange: Select data based on time range
                   Default Value: 

                uvrange: Select data within uvrange (default units meters)
                   Default Value: 

                antenna: Select data based on antenna/baseline
                   Default Value: 

                scan: Scan number range
                   Default Value: 

                msselect: Optional complex data selection (ignore for now)
                   Default Value: 

                niter: Number of fitting iterations to execute
                   Default Value: 5

                comptype: component model type: P(oint), G(aussian), or D(isk)
                   Default Value: P
                   Allowed Values:
                                P
                                G
                                D

                sourcepar: Starting guess for component parameters (3 values for type P, 5 for G and D)
                   Default Value: 
                   1.0
                   0.0
                   0.0
  

                varypar: Control which parameters to let vary in the fit
                   Default Value: 

                outfile: Optional output component list table
                   Default Value: 


        Example :


        Fit a single component source model to the uv data.  Three models
        are available: P=point; G=Gaussian; D=Disk.  Fitting parameters can
        be held fixed.   The results are given in the log and placed in a
        components file.

        Keyword arguments:
        vis -- Name of input visibility file 
                default: none; example: vis='ngc5921.ms'
                
        --- Data Selection
        field -- Select data based on field id(s) or name(s)
                default: '' (all); example: field='1'
                field='0~2' # field ids inclusive from 0 to 2
                field='3C*' # all field names starting with 3C
        spw -- Select data based on spectral window
                default: '' (all); example: spw='1'
                spw='<2' #spectral windows less than 2
                spw='>1' #spectral windows greater than 1
        selectdata -- Select a subset of the visibility using MSSelection
                default: False; example: selectdata=True
        timerange  -- Select data based on time range:
                default = '' (all); example,
                timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                Note: YYYY/MM/DD can be dropped as needed:
                timerange='09:14:0~09:54:0' # this time range
                timerange='09:44:00' # data within one integration of time
                timerange='>10:24:00' # data after this time
                timerange='09:44:00+00:13:00' #data 13 minutes after time
        uvrange -- Select data within uvrange (default units kilo-lambda)
               default: '' (all); example:
               uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lamgda
               uvrange='>4klambda';uvranges greater than 4 kilo lambda
               uvrange='0~1000km'; uvrange in kilometers
        antenna -- Select data based on antenna/baseline
                default: '' (all); example: antenna='5&6' baseline 5-6
                antenna='5&6;7&8' #baseline 5-6 and 7-8
                antenna='5' # all baselines with antenna 5
                antenna='5,6' # all baselines with antennas 5 and 6
        scan -- Select data based on scan number - New, under developement
                default: '' (all); example: scan='>3'
        msselect -- Optional data selection (field,spw,time,etc)
                default:'' means select all; example:msselect='FIELD_ID==0', 
                msselect='FIELD_ID IN [0,1,2]' means select fields 0,1 and 2
                msselect='FIELD_ID <= 1 means select fields 0, 1
                msselect='FIELD_ID==0 && ANTENNA1 IN [0] && ANTENNA2 IN [2:26]'
                   means select field 0 and antennas 0 to 26, except antenna 1.
                Other msselect fields are: 'DATA_DESC_ID', 'SPECTRAL_WINDOW_ID',
                'POLARIZATION_ID', 'SCAN_NUMBER', 'TIME', 'UVW'
                See ccokbook for more details

        niter -- Number of fitting iterations to execute
                default: 5; example: niter=20
        comptype -- component model type
                default: 'P';
                Options: 'P' (point source), 'G' (elliptical gaussian),
                         'D' (elliptical disk)
        sourcepar -- Starting guess for component parameters
                default: [1,0,0];  (for comptype='P')
                IF comptype = 'P' then
                  sourcepar = [flux,xoff,yoff] where
                    flux = Jy, xoff = offset east (arcsec), yoff = offset north (arcsec).
                IF comptype = 'G' or 'D', then
                  sourcepar = [flux,xoff,yoff,majax,axrat,pos] where
                    majax = FWHM along the major axis (arcsec), axrat < 1 is
                    the ratio of minor to major axis, pos=angle in deg
        varypar -- Control which parameters to let vary in the fit
                default: [] (all vary);
                example: vary=[F,T,T]

        examples:

             fit a point:
                comptype = 'P'
                sourcepar = [0.4,0.2,-0.3];
                varypar = [T,T,T]

             fit a circular Gaussian:
                comptype = 'G'
                sourcepar = [1.4,0.3,-0.2,0.3, 1, 0]
                varypar    = [ T , T ,  T , T , F, F]
                    

        outfile -- Optional output component list table
                default: ''; example: outfile='componentlist.cl'


        How to get the output values:

            cl.open('componentlist.cl')
            fit = cl.getcompoent()             stores component information
            fit                                to see the whole mess
            flux = fit['flux']['value']        to store the I,Q,U,V, flux
            print flux

            ra = fit['shape']['direction']['m0']['value']
            dec =fit['shape']['direction']['m1']['value']
            print ra, dec

            bmaj = fit['shape']['majoraxis']['value']     to get major axis
            bmin = fit['shape']['minoraxis']['value']     to get minor axis
            


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'uvmodelfit'
        self.__globals__['taskname'] = 'uvmodelfit'
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
            myparams['selectdata'] = selectdata = self.parameters['selectdata']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['msselect'] = msselect = self.parameters['msselect']
            myparams['niter'] = niter = self.parameters['niter']
            myparams['comptype'] = comptype = self.parameters['comptype']
            myparams['sourcepar'] = sourcepar = self.parameters['sourcepar']
            myparams['varypar'] = varypar = self.parameters['varypar']
            myparams['outfile'] = outfile = self.parameters['outfile']

        if type(sourcepar)==float: sourcepar=[sourcepar]
        if type(varypar)==bool: varypar=[varypar]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['selectdata'] = selectdata
        mytmp['timerange'] = timerange
        mytmp['uvrange'] = uvrange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['msselect'] = msselect
        mytmp['niter'] = niter
        mytmp['comptype'] = comptype
        mytmp['sourcepar'] = sourcepar
        mytmp['varypar'] = varypar
        mytmp['outfile'] = outfile
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'uvmodelfit.xml')

        casalog.origin('uvmodelfit')
        try :
          #if not trec.has_key('uvmodelfit') or not casac.casac.utils().verify(mytmp, trec['uvmodelfit']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['uvmodelfit'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('uvmodelfit', 'uvmodelfit.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'uvmodelfit'
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
          result = uvmodelfit(vis, field, spw, selectdata, timerange, uvrange, antenna, scan, msselect, niter, comptype, sourcepar, varypar, outfile)

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
             tname = 'uvmodelfit'
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
#        paramgui.runTask('uvmodelfit', myf['_ip'])
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
        a['selectdata']  = True
        a['niter']  = 5
        a['comptype']  = 'P'
        a['sourcepar']  = [1.0, 0.0, 0.0]
        a['varypar']  = []
        a['outfile']  = ''

        a['selectdata'] = {
                    0:odict([{'value':True}, {'timerange':''}, {'uvrange':''}, {'antenna':''}, {'scan':''}, {'msselect':''}]), 
                    1:{'value':False}}

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
    def description(self, key='uvmodelfit', subkey=None):
        desc={'uvmodelfit': 'Fit a single component source model to the uv data',
               'vis': 'Name of input visibility file',
               'field': 'Select field using field id(s) or field name(s)',
               'spw': 'Select spectral window/channels',
               'selectdata': 'Other data selection parameters',
               'timerange': 'Select data based on time range',
               'uvrange': 'Select data within uvrange (default units meters)',
               'antenna': 'Select data based on antenna/baseline',
               'scan': 'Scan number range',
               'msselect': 'Optional complex data selection (ignore for now)',
               'niter': 'Number of fitting iterations to execute',
               'comptype': 'component model type: P(oint), G(aussian), or D(isk)',
               'sourcepar': 'Starting guess for component parameters (3 values for type P, 5 for G and D)',
               'varypar': 'Control which parameters to let vary in the fit',
               'outfile': 'Optional output component list table',

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
        a['selectdata']  = True
        a['timerange']  = ''
        a['uvrange']  = ''
        a['antenna']  = ''
        a['scan']  = ''
        a['msselect']  = ''
        a['niter']  = 5
        a['comptype']  = 'P'
        a['sourcepar']  = [1.0, 0.0, 0.0]
        a['varypar']  = []
        a['outfile']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['selectdata']  == True:
            a['timerange'] = ''
            a['uvrange'] = ''
            a['antenna'] = ''
            a['scan'] = ''
            a['msselect'] = ''

        if a.has_key(paramname) :
              return a[paramname]
uvmodelfit_cli = uvmodelfit_cli_()
