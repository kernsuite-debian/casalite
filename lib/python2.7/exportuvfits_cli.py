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
from task_exportuvfits import exportuvfits
class exportuvfits_cli_:
    __name__ = "exportuvfits"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (exportuvfits_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'fitsfile':None, 'datacolumn':None, 'field':None, 'spw':None, 'antenna':None, 'timerange':None, 'writesyscal':None, 'multisource':None, 'combinespw':None, 'writestation':None, 'padwithflags':None, 'overwrite':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, fitsfile=None, datacolumn=None, field=None, spw=None, antenna=None, timerange=None, writesyscal=None, multisource=None, combinespw=None, writestation=None, padwithflags=None, overwrite=None, ):

        """Convert a CASA visibility data set to a UVFITS file:

        Detailed Description:

 This task writes a UVFITS file, a general format data set used to
 transfer data between different software systems. It is written in
 floating point format.  Different programs have different
 restrictions on what forms of UVFITS files they will use, especially
 whether they will accept multiple sources and/or spectral windows in
 the same file.  See the spw, multisource, and combinespw descriptions
 below.

IMPORTANT NOTE: In general, some of the data averaging features of
this task have never worked properly. In general, users should run
mstransform to select and average data prior to running
exportuvfits. The associated input parameters are being slowly
deprecated and removed.

        Arguments :
                vis: Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'

                   Default Value: 

                fitsfile: Name of output UV FITS file
                     Default: none

                        Example: vis='ngc5921XC1.fits'

                   Default Value: 

                datacolumn: Visibility file data column
                     Default: corrected
                     Options: 'data'(raw)|'corrected'|'model'|'weight'

                        Example: datacolumn='model'

                   Default Value: corrected
                   Allowed Values:
                                data
                                corrected
                                model
                                weight

                field: Select field using field id(s) or field name(s)
                     Default: '' --> all fields
                     
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

                   Default Value: 

                spw: Select spectral window/channels

                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all
                        channels)
                        spw='<2';  spectral windows less than 2
                        (i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61,
                        INCLUSIVE
                        spw='*:5~61'; all spw with channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
                        3, channels 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
                        through 6 in each.
                        spw='0:0~10;15~60'; spectral window 0 with
                        channels 0-10,15-60. (NOTE ';' to separate
                        channel selections)
                        spw='0:0~10^2,1:20~30^5'; spw 0, channels
                        0,2,4,6,8,10, spw 1, channels 20,25,30 
                        type 'help par.selection' for more examples.

                   Default Value: 

                antenna: Select data based on antenna/baseline
                     Subparameter of selectdata=True
                     Default: '' (all)

                     If antenna string is a non-negative integer, it
                     is assumed an antenna index, otherwise, it is
                     assumed as an antenna name
  
                         Examples: 
                         antenna='5&6'; baseline between antenna
                         index 5 and index 6.
                         antenna='VA05&VA06'; baseline between VLA
                         antenna 5 and 6.
                         antenna='5&6;7&8'; baselines with
                         indices 5-6 and 7-8
                         antenna='5'; all baselines with antenna index
                         5
                         antenna='05'; all baselines with antenna
                         number 05 (VLA old name)
                         antenna='5,6,10'; all baselines with antennas
                         5,6,10 index numbers

                   Default Value: 

                timerange: Select data based on time range
                     Subparameter of selectdata=True
                     Default = '' (all)

                        Examples:
                        timerange =
                        'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                        (Note: if YYYY/MM/DD is missing date defaults
                        to first day in data set.)
                        timerange='09:14:0~09:54:0' picks 40 min on
                        first day 
                        timerange= '25:00:00~27:30:00' picks 1 hr to 3
                        hr 30min on NEXT day
                        timerange='09:44:00' pick data within one
                        integration of time
                        timerange='>10:24:00' data after this time

                   Default Value: 

                writesyscal: Write GC and TY tables. Not yet available.
                     Default: False

                   Default Value: False

                multisource: Write in multi-source format? 
                     Default: True

                     Set to False if only one source is selected. 

                     Note: diffmap does not work on multisource uvfits
                     files, so if planning on using diffmap on the
                     resulting uvfits file, select a single source and
                     set multisource = False. Otherwise use True. (If
                     multiple sources are selected, a multi-source
                     file will be written no matter what the setting
                     of this parameter).

                   Default Value: True

                combinespw: Export the spectral windows as IFs?
                     Default: True

                     If True, export the spectral windows as
                     IFs. All spectral windows must have same
                     shape. Otherwise multiple windows will use
                     multiple FREQIDs.

                   Default Value: True

                writestation: Write station name instead of antenna name
                     Default: True

                   Default Value: True

                padwithflags: Fill in missing data with flags to fit IFs
                     Subparameter of combinespw=True
                     Default: True
                     
                     If True, and combinespw is True, fill in missing
                     data as needed to fit the IF structure. This is
                     appropriate if the MS had a few
                     frequency-dependent flags applied, and was then
                     time-averaged by split, or when exporting for use
                     by difmap. If the spectral windows were observed
                     at different times, padwithflags=True will add a
                     large number of flags, making the output file
                     significantly longer. It does not yet support
                     spectral windows with different widths.

                   Default Value: False

                overwrite: Overwrite output file if it exists?
                     Default: False
                     Options: False|True

                   Default Value: False


        Example :


For more information, see the task pages of exportuvfits in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'exportuvfits'
        self.__globals__['taskname'] = 'exportuvfits'
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
            myparams['fitsfile'] = fitsfile = self.parameters['fitsfile']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['writesyscal'] = writesyscal = self.parameters['writesyscal']
            myparams['multisource'] = multisource = self.parameters['multisource']
            myparams['combinespw'] = combinespw = self.parameters['combinespw']
            myparams['writestation'] = writestation = self.parameters['writestation']
            myparams['padwithflags'] = padwithflags = self.parameters['padwithflags']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['fitsfile'] = fitsfile
        mytmp['datacolumn'] = datacolumn
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['antenna'] = antenna
        mytmp['timerange'] = timerange
        mytmp['writesyscal'] = writesyscal
        mytmp['multisource'] = multisource
        mytmp['combinespw'] = combinespw
        mytmp['writestation'] = writestation
        mytmp['padwithflags'] = padwithflags
        mytmp['overwrite'] = overwrite
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'exportuvfits.xml')

        casalog.origin('exportuvfits')
        try :
          #if not trec.has_key('exportuvfits') or not casac.casac.utils().verify(mytmp, trec['exportuvfits']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['exportuvfits'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('exportuvfits', 'exportuvfits.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'exportuvfits'
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
          result = exportuvfits(vis, fitsfile, datacolumn, field, spw, antenna, timerange, writesyscal, multisource, combinespw, writestation, padwithflags, overwrite)

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
             tname = 'exportuvfits'
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
#        paramgui.runTask('exportuvfits', myf['_ip'])
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
        a['fitsfile']  = ''
        a['datacolumn']  = 'corrected'
        a['field']  = ''
        a['spw']  = ''
        a['antenna']  = ''
        a['timerange']  = ''
        a['writesyscal']  = False
        a['multisource']  = True
        a['combinespw']  = True
        a['writestation']  = True
        a['overwrite']  = False

        a['combinespw'] = {
                    0:odict([{'value':True}, {'padwithflags':True}]), 
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
    def description(self, key='exportuvfits', subkey=None):
        desc={'exportuvfits': 'Convert a CASA visibility data set to a UVFITS file:',
               'vis': 'Name of input visibility file',
               'fitsfile': 'Name of output UV FITS file',
               'datacolumn': 'Visibility file data column',
               'field': 'Select field using field id(s) or field name(s)',
               'spw': 'Select spectral window/channels',
               'antenna': 'Select data based on antenna/baseline',
               'timerange': 'Select data based on time range',
               'writesyscal': 'Write GC and TY tables (not yet available)',
               'multisource': 'Write in multi-source format?',
               'combinespw': 'Export the spectral windows as IFs',
               'writestation': 'Write station name instead of antenna name',
               'padwithflags': 'Fill in missing data with flags to fit IFs',
               'overwrite': 'Overwrite output file if it exists?',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['fitsfile']  = ''
        a['datacolumn']  = 'corrected'
        a['field']  = ''
        a['spw']  = ''
        a['antenna']  = ''
        a['timerange']  = ''
        a['writesyscal']  = False
        a['multisource']  = True
        a['combinespw']  = True
        a['writestation']  = True
        a['padwithflags']  = False
        a['overwrite']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['combinespw']  == True:
            a['padwithflags'] = True

        if a.has_key(paramname) :
              return a[paramname]
exportuvfits_cli = exportuvfits_cli_()
