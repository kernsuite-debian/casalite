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
from task_concat import concat
class concat_cli_:
    __name__ = "concat"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (concat_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'concatvis':None, 'freqtol':None, 'dirtol':None, 'respectname':None, 'timesort':None, 'copypointing':None, 'visweightscale':None, 'forcesingleephemfield':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, concatvis=None, freqtol=None, dirtol=None, respectname=None, timesort=None, copypointing=None, visweightscale=None, forcesingleephemfield=None, ):

        """Concatenate several visibility data sets.

        Detailed Description:

The list of data sets given in the vis argument are chronologically
concatenated into an output data set in concatvis, i.e. the data sets
in vis are first ordered by the time of their earliest integration and
then concatenated. If concatvis already exists (e.g., it is the same
as the first input data set), then the other input data sets will be
appended to the concatvis data set.There is no limit to the number of
input data sets.
   
If there are fields whose direction agrees within the direction will
be the one from the chronologically first input MS. Spectral windows
for each data set with the same chanelization, and within a specified
frequency tolerance of another data set will be combined into one
spectral window.

If none of the input data sets have any scratch columns (model and
corrected columns), none are created in the concatvis.  Otherwise
these columns are created on output and initialized to their default
value (1 in model column, data in corrected column) for those data
with no input columns.

Each appended dataset is assigned a new observation id (provided the
entries in the observation table are indeed different).

        Arguments :
                vis: Name of input visibility file
                     default: none

                        Example:
                        vis='['src2.ms','ngc5921.ms','ngc315.ms']

                   Default Value: 

                concatvis: Name of visibility file that will contain the
concatenated data
                     default: none

                        Example: concatvis='outvis.ms'

                     Note: if this file exits on disk then the input
                     files are added to this file.  Otherwise the new
                     file contains the concatenated data. Be careful
                     here when concatenating to an existing file.

                   Default Value: 

                freqtol: Frequency shift tolerance for considering data as the
same spwid. The number of channels must also be the same.
                    Default: '' == 1 Hz

                       Example: freqtol='10MHz' will not combine spwid
                       unless they are within 10 MHz.

                    Note: This option is useful to combine spectral
                    windows with very slight frequency differences
                    caused by Doppler tracking, for example.

                   Default Value: 

                dirtol: Direction shift tolerance for considering data as the
same field
                     Default: '' == 1 mas (milliarcsec)

                        Example: dirtol='1arcsec' will not combine
                        data for a field unless their phase center
                        differ by less than 1 arcsec.  

                     Note: If the field names are different in the
                     input data sets, the name in the output data set
                     will be the first relevant data set in the list.

                   Default Value: 

                respectname: If true, fields with a different name are not merged even
if their direction agrees (within dirtol)
                     Default: False

                   Default Value: False

                timesort: If true, sort by TIME in ascending order
                     Default: False (data in order as read in)

                        Example: timesort=True

                     Note: There is no constraint on data that is
                     simultaneously observed for more than one field;
                     for example multi-source correlation of VLBA
                     data.

                   Default Value: False

                copypointing: Make a proper copy of the POINTING subtable 
                     Default:True (can be time consuming!)

                     If False, the result is an empty POINTING table.

                   Default Value: True

                visweightscale: List of the weight scaling factors to be applied to the
individual MSs
                     Default: [] (empty list) - no scaling

                     The weights of the individual MSs will be scaled
                     in the concatenated output MS by the factors in
                     this list. SIGMA will be scaled by
                     1/sqrt(factor). Useful for handling heterogeneous
                     arrays. Use plotms to inspect the "Wt" column as
                     a reference for determining the scaling factors.
 
                        Example: [1.,3.,3.] - scale the weights of the
                        second and third MS by a factor 3 and the
                        SIGMA column of these MS by a factor
                        1/sqrt(3).

                   Default Value: 

                forcesingleephemfield: Make sure that there is only one joint ephemeris for every field in this list
                     Default: '' (standard treatment of all ephemeris
                     fields)

                     By default, concat will only merge two ephemeris
                     fields if the first ephemeris covers the time
                     range of the second. Otherwise, two separate
                     fields with separate ephemerides are placed in
                     the output MS.
                     In order to override this behaviour and make
                     concat merge the non-overlapping or only
                     partially overlapping input ephemerides, the name
                     or id of the field in question needs to be placed
                     into the list in parameter
                     'forcesingleephemfield'.

                     Example: ['Neptune'] - will make sure that there
                     is only one joint ephemeris for field Neptune in
                     the output MS

                   Default Value: 


        Example :


For more information, see the task pages of concat in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'concat'
        self.__globals__['taskname'] = 'concat'
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
            myparams['concatvis'] = concatvis = self.parameters['concatvis']
            myparams['freqtol'] = freqtol = self.parameters['freqtol']
            myparams['dirtol'] = dirtol = self.parameters['dirtol']
            myparams['respectname'] = respectname = self.parameters['respectname']
            myparams['timesort'] = timesort = self.parameters['timesort']
            myparams['copypointing'] = copypointing = self.parameters['copypointing']
            myparams['visweightscale'] = visweightscale = self.parameters['visweightscale']
            myparams['forcesingleephemfield'] = forcesingleephemfield = self.parameters['forcesingleephemfield']

        if type(vis)==str: vis=[vis]
        if type(visweightscale)==float: visweightscale=[visweightscale]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['concatvis'] = concatvis
        mytmp['freqtol'] = freqtol
        mytmp['dirtol'] = dirtol
        mytmp['respectname'] = respectname
        mytmp['timesort'] = timesort
        mytmp['copypointing'] = copypointing
        mytmp['visweightscale'] = visweightscale
        mytmp['forcesingleephemfield'] = forcesingleephemfield
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'concat.xml')

        casalog.origin('concat')
        try :
          #if not trec.has_key('concat') or not casac.casac.utils().verify(mytmp, trec['concat']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['concat'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('concat', 'concat.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'concat'
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
          result = concat(vis, concatvis, freqtol, dirtol, respectname, timesort, copypointing, visweightscale, forcesingleephemfield)

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
             tname = 'concat'
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
#        paramgui.runTask('concat', myf['_ip'])
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
        a['vis']  = ['']
        a['concatvis']  = ''
        a['freqtol']  = ''
        a['dirtol']  = ''
        a['respectname']  = False
        a['timesort']  = False
        a['copypointing']  = True
        a['visweightscale']  = []
        a['forcesingleephemfield']  = ''


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
    def description(self, key='concat', subkey=None):
        desc={'concat': 'Concatenate several visibility data sets.',
               'vis': 'Name of input visibility file',
               'concatvis': 'Name of output visibility file',
               'freqtol': 'Frequency shift tolerance for considering data as the same spwid',
               'dirtol': 'Direction shift tolerance for considering data as the same field',
               'respectname': 'If true, fields with a different name are not merged even if their direction agrees',
               'timesort': 'If true, sort by TIME in ascending order',
               'copypointing': 'Copy all rows of the POINTING table.',
               'visweightscale': 'List of the weight scaling factors to be applied to the individual MSs',
               'forcesingleephemfield': 'Make sure that there is only one joint ephemeris for every field in this list',

              }

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ['']
        a['concatvis']  = ''
        a['freqtol']  = ''
        a['dirtol']  = ''
        a['respectname']  = False
        a['timesort']  = False
        a['copypointing']  = True
        a['visweightscale']  = []
        a['forcesingleephemfield']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
concat_cli = concat_cli_()
