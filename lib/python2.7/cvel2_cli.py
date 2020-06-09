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
from task_cvel2 import cvel2
class cvel2_cli_:
    __name__ = "cvel2"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (cvel2_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'outputvis':None, 'keepmms':None, 'passall':None, 'field':None, 'spw':None, 'scan':None, 'antenna':None, 'correlation':None, 'timerange':None, 'intent':None, 'array':None, 'uvrange':None, 'observation':None, 'feed':None, 'datacolumn':None, 'mode':None, 'nchan':None, 'start':None, 'width':None, 'interpolation':None, 'phasecenter':None, 'restfreq':None, 'outframe':None, 'veltype':None, 'hanning':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, outputvis=None, keepmms=None, passall=None, field=None, spw=None, scan=None, antenna=None, correlation=None, timerange=None, intent=None, array=None, uvrange=None, observation=None, feed=None, datacolumn=None, mode=None, nchan=None, start=None, width=None, interpolation=None, phasecenter=None, restfreq=None, outframe=None, veltype=None, hanning=None, ):

        """Regrid an MS or MMS to a new spectral window, channel structure or frame

        Detailed Description:

The intent of cvel2 is to transform channel labels and the
visibilities to a spectral reference frame which is appropriate for
the science analysis, e.g. from TOPO to LSRK to correct for Doppler
shifts throughout the time of the observation. Naturally, this will
change the shape of the spectral feature to some extent. According to
the Nyquist theorem you should oversample a spectrum with twice the
numbers of channels to retain the shape. Based on some tests, however,
we recommend to observe with at least 3-4 times the number of channels
for each significant spectral feature (like 3-4 times the
linewidth). This will minimize regridding artifacts in cvel2.

If cvel2 has already established the grid that is desired for the
imaging, tclean should be run with exactly the same frequency/velocity
parameters as used in cvel2 in order to avoid additional regridding in
clean.

Hanning smoothing is optionally offered in cvel2, but tests have shown
that already the regridding process itself, if it involved a
transformation from TOPO to a non-terrestrial reference frame, implies
some smoothing (due to channel interpolation) such that Hanning
smoothing may not be necessary.
   
This version of cvel2 also supports Multi-MS input, in which case it
will create an output Multi-MS too.

    NOTE:
    The parameter passall is not supported in cvel2. The user may
    achieve the same results of passall=True by splitting out the data
    that will not be regridded with cvel2 and concatenate regridded
    and non-regridded sets at the end. In the case of Multi-MS input,
    the user should use virtualconcat to achieve a concatenated MMS.    

        Arguments :
                vis: Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'

                   Default Value: 

                outputvis: Name of output visibility file or Multi-MS
                     Default: none

                        Example: vis='ngc5921_out.ms'

                   Default Value: 

                keepmms: If the input is a Multi-MS the output will also be a
Multi-MS.
                     Default: True

                     By default it will create a Multi-MS when the
                     input is a Multi-MS. The output Multi-MS will
                     have the same partition axis of the input
                     MMS. See 'help partition' for more information on
                     the MMS format.

                     NOTE: It is not possible to combine the spws if
                     the input MMS was partitioned with
                     separationaxis='spw'. In this case, the task will
                     abort with an error.

                   Default Value: True

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

                   Default Value: 

                spw: Select spectral window/channels
                     Default: ''=all spectral windows and channels
           
                        Examples:
                        spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                        spw='<2';  spectral windows less than 2 (i.e. 0,1)
                        spw='0:5~61'; spw 0, channels 5 to 61
                        spw='0,10,3:3~45'; spw 0,10 all channels, spw
                        3 - chans 3 to 45.
                        spw='0~2:2~6'; spw 0,1,2 with channels 2
                        through 6 in each.
                        spw = '*:3~64'  channels 3 through 64 for all sp id's
                        spw = ' :3~64' will NOT work.

                     NOTE: mstransform does not support multiple
                     channel ranges per spectral window.

                   Default Value: 

                scan: Scan number range
                     Subparameter of selectdata=True
                     default: '' = all

                   Default Value: 

                antenna: Select data based on antenna/baseline
                     Subparameter of selectdata=True
                     default: '' (all)

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
                         antenna='!ea03,ea12,ea17': all baselines
                         except those that include EVLA antennas ea03,
                         ea12, or ea17.

                   Default Value: 

                correlation: Select data based on correlation
                     Default: '' (all)

                        Example: correlation='XX,YY'.

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

                intent: Select observing intent
                     Default: '' (no selection by intent)

                        Example: intent='*BANDPASS*'  (selects data
                        labelled with BANDPASS intent)

                   Default Value: 

                array: Select (sub)array(s) by array ID number.
                     Default = '' (all)

                   Default Value: 

                uvrange: Select data by baseline length.
                   Default Value: 

                observation: Select by observation ID(s)
                     Subparameter of selectdata=True
                     Default: '' = all

                         Example: observation='0~2,4'

                   Default Value: 

                feed: Multi-feed numbers: Not yet implemented.
                   Default Value: 

                datacolumn: Which data column(s) to process.
                   Default Value: all
                   Allowed Values:
                                all
                                data
                                corrected
                                model
                                data,model,corrected
                                float_data
                                lag_data
                                float_data,data
                                lag_data,data

                mode: Regridding mode (channel/velocity/frequency/channel_b).
                     Default: 'channel'
                     Options: 'channel', 'velocity', 'frequency',
                     'channel_b'

                   * mode = 'channel'; Use with nchan, start, width to
                     specify output spw. Produces equidistant grid
                     based on first selected channel.
                   * mode = 'velocity', means channels are specified
                     in velocity.
                   * mode = 'frequency', means channels are specified
                     in frequency.
                   * mode = 'channel_b', alternative 'channel'
                     mode. Does not force an equidistant grid. Faster.

                        Examples: 
                        spw = '0,1'; mode = 'channel' will produce a
                        single spw containing all channels in spw 0
                        and 1
                        spw='0:5~28^2'; mode = 'channel' will produce
                        a single spw made with channels
                        (5,7,9,...,25,27)
                        spw = '0'; mode = 'channel': nchan=3; start=5;
                        width=4 will produce an spw with 3 output
                        channels
                        - new channel 1 contains data from channels
                        (5+6+7+8)
                        - new channel 2 contains data from channels
                        (9+10+11+12)
                        - new channel 3 contains data from channels
                        (13+14+15+16)
                        spw = '0:0~63^3'; mode='channel'; nchan=21;
                        start = 0; width = 1 will produce an spw with
                        21 channels
                        - new channel 1 contains data from channel 0
                        - new channel 2 contains data from channel 2
                        - new channel 21 contains data from channel 61
                        spw = '0:0~40^2'; mode = 'channel'; nchan = 3;
                        start = 5; width = 4 will produce an spw with
                        three output channels
                        - new channel 1 contains channels (5,7)
                        - new channel 2 contains channels (13,15)
                        - new channel 3 contains channels (21,23)

                   Default Value: channel
                   Allowed Values:
                                channel
                                velocity
                                frequency
                                channel_b

                nchan: Number of channels in the output spw (-1=all). 
                     Subparameter of
                     mode='channel|velocity|frequency|channel_b'                
                     Default: -1 = all channels

                     Used for regridding, together with 'start' and
                     'width'.

                        Example: nchan=3

                   Default Value: -1

                start: Start or end input channel (zero-based), depending on the sign of the width parameter 
                     Subparameter of
                     mode='channel|velocity|frequency|channel_b'                

                     Used for regridding, together with 'width' and
                     'nchan'. It can be in different units, depending
                     on the regridding mode: 
                     - first input channel (mode='channel'), 
                     - first velocity (mode='velocity'), or 
                     - first frequency (mode='frequency'). 

                        Example values: '5', '0.0km/s', '1.4GHz', for
                        channel, velocity, and frequency modes,
                        respectively.

                   Default Value: 0

                width: Channel width of the output visibilities. 
                     Subparameter of
                     mode='channel|velocity|frequency|channel_b'                

                     Used for regridding, together with 'start', and
                     'nchan'. It can be in different units, depending
                     on the regridding mode: number of input channels
                     (mode='channel'), velocity (mode='velocity'), or
                     frequency (mode='frequency'. 

                        Example values: '2', '1.0km/s', '1.0kHz', for
                        channel, velocity, and frequency modes,
                        respectively.

                     Note: the sign indicates whether the start
                     parameter is lower(+) or upper(-) end of the
                     range.

                   Default Value: 1

                interpolation: Spectral interpolation method
                     Subparameter of
                     mode='channel|velocity|frequency|channel_b'
                     Default = 'linear'
                     Options: linear, nearest, cubic, spline, fftshift

                   Default Value: linear
                   Allowed Values:
                                nearest
                                linear
                                cubic
                                spline
                                fftshift

                phasecenter: Phase center direction to be used for the spectral
coordinate transformation.
                     Default: '' (first selected field)
                     Options: FIELD_ID (int) or center coordinate measure (str).

                     Phase direction measure  or fieldid. To be used
                     in mosaics to indicate the center direction to be
                     used in the spectral coordinate transformation.

                        Examples: 
                        phasecenter=6
                        phasecenter='J2000 19h30m00 -40d00m00'

                   Default Value: 

                restfreq: Rest frequency to use for output visibilities.
                     Default='' 

                     Occasionally it is necessary to set this (for
                     example some VLA spectral line data).  For
                     example for NH_3 (1,1) put
                     restfreq='23.694496GHz'

                   Default Value: 

                outframe: Output reference frame (not case-sensitive).
                     Default: '' (keep original reference frame)
                     Options: LSRK, LSRD, BARY, GALACTO, LGROUP, CMB,
                     GEO, TOPO, or SOURCE 

                     SOURCE is meant for solar system work and
                     corresponds to GEO + radial velocity correction
                     for ephemeris objects.

                        Example: outframe='BARY'     

                   Default Value: 
                   Allowed Values:
                                topo
                                geo
                                lsrk
                                lsrd
                                bary
                                galacto
                                lgroup
                                cmb
                                source
                                

                veltype: Definition of velocity (in mode)
                     Default = 'radio'

                   Default Value: radio
                   Allowed Values:
                                optical
                                radio

                hanning: Hanning smooth data to remove Gibbs ringing.
                     Default: False
                     Options: False|True

                   Default Value: False

        Returns: void

        Example :


For more information, see the task pages of cvel2 in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'cvel2'
        self.__globals__['taskname'] = 'cvel2'
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
            myparams['keepmms'] = keepmms = self.parameters['keepmms']
            myparams['passall'] = passall = self.parameters['passall']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['correlation'] = correlation = self.parameters['correlation']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['array'] = array = self.parameters['array']
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['feed'] = feed = self.parameters['feed']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']
            myparams['mode'] = mode = self.parameters['mode']
            myparams['nchan'] = nchan = self.parameters['nchan']
            myparams['start'] = start = self.parameters['start']
            myparams['width'] = width = self.parameters['width']
            myparams['interpolation'] = interpolation = self.parameters['interpolation']
            myparams['phasecenter'] = phasecenter = self.parameters['phasecenter']
            myparams['restfreq'] = restfreq = self.parameters['restfreq']
            myparams['outframe'] = outframe = self.parameters['outframe']
            myparams['veltype'] = veltype = self.parameters['veltype']
            myparams['hanning'] = hanning = self.parameters['hanning']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['outputvis'] = outputvis
        mytmp['keepmms'] = keepmms
        mytmp['passall'] = passall
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['scan'] = scan
        mytmp['antenna'] = antenna
        mytmp['correlation'] = correlation
        mytmp['timerange'] = timerange
        mytmp['intent'] = intent
        mytmp['array'] = array
        mytmp['uvrange'] = uvrange
        mytmp['observation'] = observation
        mytmp['feed'] = feed
        mytmp['datacolumn'] = datacolumn
        mytmp['mode'] = mode
        mytmp['nchan'] = nchan
        mytmp['start'] = start
        mytmp['width'] = width
        mytmp['interpolation'] = interpolation
        mytmp['phasecenter'] = phasecenter
        mytmp['restfreq'] = restfreq
        mytmp['outframe'] = outframe
        mytmp['veltype'] = veltype
        mytmp['hanning'] = hanning
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'cvel2.xml')

        casalog.origin('cvel2')
        try :
          #if not trec.has_key('cvel2') or not casac.casac.utils().verify(mytmp, trec['cvel2']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['cvel2'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('cvel2', 'cvel2.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'cvel2'
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
          result = cvel2(vis, outputvis, keepmms, passall, field, spw, scan, antenna, correlation, timerange, intent, array, uvrange, observation, feed, datacolumn, mode, nchan, start, width, interpolation, phasecenter, restfreq, outframe, veltype, hanning)

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
             tname = 'cvel2'
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
#        paramgui.runTask('cvel2', myf['_ip'])
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
        a['keepmms']  = True
        a['field']  = ''
        a['spw']  = ''
        a['scan']  = ''
        a['antenna']  = ''
        a['correlation']  = ''
        a['timerange']  = ''
        a['intent']  = ''
        a['array']  = ''
        a['uvrange']  = ''
        a['observation']  = ''
        a['feed']  = ''
        a['datacolumn']  = 'all'
        a['mode']  = 'channel'
        a['phasecenter']  = ''
        a['restfreq']  = ''
        a['outframe']  = ''
        a['veltype']  = 'radio'
        a['hanning']  = False

        a['mode'] = {
                    0:odict([{'value':'channel'}, {'nchan':-1}, {'start':0}, {'width':1}, {'interpolation':'linear'}]), 
                    1:odict([{'value':'channel_b'}, {'nchan':-1}, {'start':0}, {'width':1}, {'interpolation':'linear'}]), 
                    2:odict([{'value':'velocity'}, {'nchan':-1}, {'start':''}, {'width':''}, {'interpolation':'linear'}]), 
                    3:odict([{'value':'frequency'}, {'nchan':-1}, {'start':''}, {'width':''}, {'interpolation':'linear'}])}

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
    def description(self, key='cvel2', subkey=None):
        desc={'cvel2': 'Regrid an MS or MMS to a new spectral window, channel structure or frame',
               'vis': 'Name of input visibility file',
               'outputvis': 'Name of output visibility file',
               'keepmms': 'Create a Multi-MS as the output if the input is a Multi-MS',
               'passall': 'Hidden parameter',
               'field': 'Select field using field id(s) or field name(s)',
               'spw': 'Select spectral window/channels',
               'scan': 'Scan number range',
               'antenna': 'Select data based on antenna/baseline',
               'correlation': 'Select data based on correlation',
               'timerange': 'Select data based on time range',
               'intent': 'Select observing intent',
               'array': 'Select (sub)array(s) by array ID number.',
               'uvrange': 'Select data by baseline length.',
               'observation': 'Select by observation ID(s)',
               'feed': 'Multi-feed numbers: Not yet implemented.',
               'datacolumn': 'Data column(s) to process.',
               'mode': 'Regridding mode (channel/velocity/frequency/channel_b).',
               'nchan': 'Number of channels in the output spw',
               'start': 'First input channel to use',
               'width': 'Channel width of the output visibilities.',
               'interpolation': 'Spectral interpolation method',
               'phasecenter': 'Phase center direction to be used for the spectral coordinate transformation: direction measure or field index',
               'restfreq': 'Rest frequency to use for output.',
               'outframe': 'Output reference frame.',
               'veltype': 'Velocity definition.',
               'hanning': 'Hanning smooth data to remove Gibbs ringing.',

              }

#
# Set subfields defaults if needed
#
        if(subkey == 'channel'):
          desc['start'] = 'First input channel to use'
        if(subkey == 'channel_b'):
          desc['start'] = 'First input channel to use'
        if(subkey == 'velocity'):
          desc['start'] = 'Velocity of first channel: e.g \'0.0km/s\''
        if(subkey == 'velocity'):
          desc['width'] = 'Channel width of the output visibilities, in velocity units, e.g \'-1.0km/s\''
        if(subkey == 'frequency'):
          desc['start'] = 'Frequency of first channel: e.q. \'1.4GHz\''
        if(subkey == 'frequency'):
          desc['width'] = 'Channel width of the output visibilities, in frequency units, e.g \'1.0kHz\''

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['outputvis']  = ''
        a['keepmms']  = True
        a['passall']  = False
        a['field']  = ''
        a['spw']  = ''
        a['scan']  = ''
        a['antenna']  = ''
        a['correlation']  = ''
        a['timerange']  = ''
        a['intent']  = ''
        a['array']  = ''
        a['uvrange']  = ''
        a['observation']  = ''
        a['feed']  = ''
        a['datacolumn']  = 'all'
        a['mode']  = 'channel'
        a['nchan']  = -1
        a['start']  = 0
        a['width']  = 1
        a['interpolation']  = 'linear'
        a['phasecenter']  = ''
        a['restfreq']  = ''
        a['outframe']  = ''
        a['veltype']  = 'radio'
        a['hanning']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mode']  == 'channel':
            a['nchan'] = -1
            a['start'] = 0
            a['width'] = 1
            a['interpolation'] = 'linear'

        if self.parameters['mode']  == 'channel_b':
            a['nchan'] = -1
            a['start'] = 0
            a['width'] = 1
            a['interpolation'] = 'linear'

        if self.parameters['mode']  == 'velocity':
            a['nchan'] = -1
            a['start'] = ''
            a['width'] = ''
            a['interpolation'] = 'linear'

        if self.parameters['mode']  == 'frequency':
            a['nchan'] = -1
            a['start'] = ''
            a['width'] = ''
            a['interpolation'] = 'linear'

        if a.has_key(paramname) :
              return a[paramname]
cvel2_cli = cvel2_cli_()
