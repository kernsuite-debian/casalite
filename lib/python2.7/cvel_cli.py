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
from task_cvel import cvel
class cvel_cli_:
    __name__ = "cvel"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (cvel_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'outputvis':None, 'passall':None, 'field':None, 'spw':None, 'selectdata':None, 'antenna':None, 'timerange':None, 'scan':None, 'array':None, 'mode':None, 'nchan':None, 'start':None, 'width':None, 'interpolation':None, 'phasecenter':None, 'restfreq':None, 'outframe':None, 'veltype':None, 'hanning':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, outputvis=None, passall=None, field=None, spw=None, selectdata=None, antenna=None, timerange=None, scan=None, array=None, mode=None, nchan=None, start=None, width=None, interpolation=None, phasecenter=None, restfreq=None, outframe=None, veltype=None, hanning=None, ):

        """regrid an MS to a new spectral window / channel structure or frame

        Detailed Description:

The intent of cvel is to transform channel labels and the 
visibilities to a spectral reference frame which is appropriate
for the science analysis, e.g. from TOPO to LSRK to correct for 
Doppler shifts throughout the time of the observation. Naturally, 
this will change the shape of the spectral feature to some extent. 
According to the Nyquist theorem you should oversample a spectrum 
with twice the numbers of channels to retain the shape. Based on 
some tests, however, we recommend to observe with at least 
3-4 times the number of channels for each significant spectral 
feature (like 3-4 times the linewidth). This will minimize 
regridding artifacts in cvel.

If cvel has already established the grid that is desired for the
imaging, clean should be run with exactly the same frequency/velocity 
parameters as used in cvel in order to avoid additional regridding in 
clean.

Hanning smoothing is optionally offered in cvel, but tests have 
shown that already the regridding process itself, if it involved 
a transformation from TOPO to a non-terrestrial reference frame, 
implies some smoothing (due to channel interpolation) such that 
Hanning smoothing may not be necessary.

        Arguments :
                vis: Name of input measurement set
                   Default Value: 

                outputvis: Name of output measurement set
                   Default Value: 

                passall: Pass through (write to output MS) non-selected data with no change
                   Default Value: False

                field: Select field using field id(s) or field name(s)
                   Default Value: 

                spw: Select spectral window/channels
                   Default Value: 

                selectdata: Other data selection parameters
                   Default Value: True

                antenna: Select data based on antenna/baseline
                   Default Value: 

                timerange: Range of time to select from data
                   Default Value: 

                scan: scan number range
                   Default Value: 

                array: (sub)array indices
                   Default Value: 

                mode:  Regridding mode 
                   Default Value: channel
                   Allowed Values:
                                channel
                                velocity
                                frequency
                                channel_b

                nchan: Number of channels in output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.
                   Default Value: -1

                start: Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.
                   Default Value: 0

                width: Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.
                   Default Value: 1

                interpolation: Spectral interpolation method
                   Default Value: linear
                   Allowed Values:
                                nearest
                                linear
                                cubic
                                spline
                                fftshift

                phasecenter: Phase center direction to be used for the spectral coordinate transformation: direction measure or field index
                   Default Value: 

                restfreq: rest frequency (see help)
                   Default Value: 

                outframe: Output frame (not case-sensitive, \'\'=keep input frame)
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
                                

                veltype: velocity definition
                   Default Value: radio
                   Allowed Values:
                                optical
                                radio

                hanning:  If true, Hanning smooth data before regridding to remove Gibbs ringing.
                   Default Value: False

        Returns: void

        Example :


       vis -- Name of input visibility file
               default: none; example: vis='ngc5921.ms'    

       outputvis -- Name of output measurement set (required)
               default: none; example: vis='ngc5921-regridded.ms'    
               
       passall --  if False, data not meeting the selection is omitted/deleted 
               or flagged (if in-row); if True, data not meeting the selection 
               on field and spw is passed through without modification
               default: False; example: 
               field='NGC5921'
               passall=False : only data from NGC5921 is included in output MS, 
                         no data from other fields (e.g. 1331+305) is included
               passall=True : data from NGC5921 is transformed by cvel, all other 
                         fields are passed through unchanged 

       field -- Select fields in mosaic.  Use field id(s) or field name(s).
                  ['go listobs' to obtain the list id's or names]
              default: ''= all fields
              If field string is a non-negative integer, it is assumed to
                  be a field index otherwise, it is assumed to be a 
                  field name
              field='0~2'; field ids 0,1,2
              field='0,4,5~7'; field ids 0,4,5,6,7
              field='3C286,3C295'; field named 3C286 and 3C295
              field = '3,4C*'; field id 3, all names starting with 4C

       spw --Select spectral window/channels
              NOTE: This selects the data passed as the INPUT to mode
              default: ''=all spectral windows and channels
                spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                spw='0:5~61'; spw 0, channels 5 to 61
                spw='<2';   spectral windows less than 2 (i.e. 0,1)
                spw='0,10,3:3~45'; spw 0,10 all channels, spw 3, 
                                   channels 3 to 45.
                spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
                spw='0:0~10;15~60'; spectral window 0 with channels 
                                    0-10,15-60
                spw='0:0~10,1:20~30,2:1;2;3'; spw 0, channels 0-10,
                      spw 1, channels 20-30, and spw 2, channels, 1,2 and 3

       selectdata -- Other data selection parameters
              default: True

  >>> selectdata=True expandable parameters

              antenna -- Select data based on antenna/baseline
                  default: '' (all)
                  If antenna string is a non-negative integer, it is 
                    assumed to be an antenna index, otherwise, it is
                    considered an antenna name.
                  antenna='5&6'; baseline between antenna index 5 and 
                                 index 6.
                  antenna='VA05&VA06'; baseline between VLA antenna 5 
                                       and 6.
                  antenna='5&6;7&8'; baselines 5-6 and 7-8
                  antenna='5'; all baselines with antenna index 5
                  antenna='05'; all baselines with antenna number 05 
                                (VLA old name)
                  antenna='5,6,9'; all baselines with antennas 5,6,9 
                                   index numbers

              timerange  -- Select data based on time range:
                 default = '' (all); examples,
                  timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                  Note: if YYYY/MM/DD is missing date defaults to first 
                        day in data set
                  timerange='09:14:0~09:54:0' picks 40 min on first day
                  timerange= '25:00:00~27:30:00' picks 1 hr to 3 hr 
                             30min on NEXT day
                  timerange='09:44:00' pick data within one integration 
                             of time
                  timerange='>10:24:00' data after this time

              scan -- Scan number range.
                  default: '' (all)
                  example: scan='1~5'
                  Check 'go listobs' to insure the scan numbers are in 
                        order.

              array -- Select data by (sub)array indices
                  default: '' (all); example:
                  array='0~2'; arrays 0 to 2 

      mode -- Frequency Specification:
               NOTE: See examples below:
               default: 'channel'
                 mode = 'channel'; Use with nchan, start, width to specify
                         output spw. Produces equidistant grid based on first
                         selected channel. See examples below.
                 mode = 'velocity', means channels are specified in 
                      velocity.
                 mode = 'frequency', means channels are specified in 
                      frequency.
                 mode = 'channel_b', alternative 'channel' mode.
                         Does not force an equidistant grid. Faster.

  >>> mode expandable parameters 
               Start, width are given in units of channels, frequency 
                  or velocity as indicated by mode 
               nchan -- Number of channels in output spw
                 default: -1 = all channels; example: nchan=3
               start -- Start or end input channel (zero-based) depending on the sign of the width parameter
                 default=0; example: start=5
               width -- Output channel width in units of the input
                     channel width (sign indicates whether the start parameter is lower(+) or upper(-) end of the range)
                 default=1; example: width=4
               interpolation -- Interpolation method (linear, nearest, cubic, spline, fftshift)
                 default = 'linear'
           examples:
               spw = '0,1'; mode = 'channel'
                  will produce a single spw containing all channels in spw 
                       0 and 1
               spw='0:5~28^2'; mode = 'channel'
                  will produce a single spw made with channels 
                       (5,7,9,...,25,27)
               spw = '0'; mode = 'channel': nchan=3; start=5; width=4
                  will produce an spw with 3 output channels
                  new channel 1 contains data from channels (5+6+7+8)
                  new channel 2 contains data from channels (9+10+11+12)
                  new channel 3 contains data from channels (13+14+15+16)
               spw = '0:0~63^3'; mode='channel'; nchan=21; start = 0; 
                   width = 1
                  will produce an spw with 21 channels
                  new channel 1 contains data from channel 0
                  new channel 2 contains data from channel 2
                  new channel 21 contains data from channel 61
               spw = '0:0~40^2'; mode = 'channel'; nchan = 3; start = 
                   5; width = 4
                  will produce an spw with three output channels
                  new channel 1 contains channels (5,7)
                  new channel 2 contains channels (13,15)
                  new channel 3 contains channels (21,23)

      phasecenter -- Direction measure  or fieldid. To be used in mosaics to indicate
               the center direction to be used in the spectral coordinate transformation.
               default: '' => first field selected ; example: phasecenter=6
               or phasecenter='J2000 19h30m00 -40d00m00'

      restfreq -- Specify rest frequency to use for output visibilities
               default='' Occasionally it is necessary to set this (for
               example some VLA spectral line data).  For example for
               NH_3 (1,1) put restfreq='23.694496GHz'

      outframe -- output reference frame (not case-sensitive)
               possible values: LSRK, LSRD, BARY, GALACTO, LGROUP, CMB, GEO, TOPO, or SOURCE
               (SOURCE is meant for solar system work and corresponds to GEO + radial velocity
               correction for ephemeris objects).
               default='' (keep original reference frame) ; example: outframe='BARY'     

      veltype -- definition of velocity (in mode)
               default = 'radio'

      hanning -- if true, Hanning smooth frequency channel data to remove Gibbs ringing

==================================================================

The intent of cvel is to transform channel labels and the 
visibilities to a spectral reference frame which is appropriate
for the science analysis, e.g. from TOPO to LSRK to correct for 
Doppler shifts throughout the time of the observation. Naturally, 
this will change the shape of the spectral feature to some extent. 
According to the Nyquist theorem you should oversample a spectrum 
with twice the numbers of channels to retain the shape. Based on 
some tests, however, we recommend to observe with at least 
3-4 times the number of channels for each significant spectral 
feature (like 3-4 times the linewidth). This will minimize 
regridding artifacts in cvel.

If cvel has already established the grid that is desired for the
imaging, clean should be run with exactly the same frequency/velocity 
parameters as used in cvel in order to avoid additional regridding in 
clean.

Hanning smoothing is optionally offered in cvel, but tests have 
shown that already the regridding process itself, if it involved 
a transformation from TOPO to a non-terrestrial reference frame, 
implies some smoothing (due to channel interpolation) such that 
Hanning smoothing may not be necessary.

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'cvel'
        self.__globals__['taskname'] = 'cvel'
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
            myparams['passall'] = passall = self.parameters['passall']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['selectdata'] = selectdata = self.parameters['selectdata']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['array'] = array = self.parameters['array']
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
        mytmp['passall'] = passall
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['selectdata'] = selectdata
        mytmp['antenna'] = antenna
        mytmp['timerange'] = timerange
        mytmp['scan'] = scan
        mytmp['array'] = array
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
        trec = casac.casac.utils().torecord(pathname+'cvel.xml')

        casalog.origin('cvel')
        try :
          #if not trec.has_key('cvel') or not casac.casac.utils().verify(mytmp, trec['cvel']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['cvel'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('cvel', 'cvel.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'cvel'
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
          result = cvel(vis, outputvis, passall, field, spw, selectdata, antenna, timerange, scan, array, mode, nchan, start, width, interpolation, phasecenter, restfreq, outframe, veltype, hanning)

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
             tname = 'cvel'
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
#        paramgui.runTask('cvel', myf['_ip'])
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
        a['passall']  = False
        a['field']  = ''
        a['spw']  = ''
        a['selectdata']  = True
        a['mode']  = 'channel'
        a['phasecenter']  = ''
        a['restfreq']  = ''
        a['outframe']  = ''
        a['veltype']  = 'radio'
        a['hanning']  = False

        a['selectdata'] = {
                    0:odict([{'value':True}, {'timerange':''}, {'array':''}, {'antenna':''}, {'scan':''}]), 
                    1:{'value':False}}
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
    def description(self, key='cvel', subkey=None):
        desc={'cvel': 'regrid an MS to a new spectral window / channel structure or frame',
               'vis': 'Name of input measurement set',
               'outputvis': 'Name of output measurement set',
               'passall': 'Pass through (write to output MS) non-selected data with no change',
               'field': 'Select field using field id(s) or field name(s)',
               'spw': 'Select spectral window/channels',
               'selectdata': 'Other data selection parameters',
               'antenna': 'Select data based on antenna/baseline',
               'timerange': 'Range of time to select from data',
               'scan': 'scan number range',
               'array': '(sub)array indices',
               'mode': ' Regridding mode ',
               'nchan': 'Number of channels in output spw (-1=all). Used for regridding, together with \'start\' and \'width\'.',
               'start': 'Start of the output visibilities. Used for regridding, together with \'width\' and \'nchan\'. It can be in different units, depending on the regridding mode: first input channel (mode=\'channel\'), first velocity (mode=\'velocity\'), or first frequency (mode=\'frequency\'). Example values: \'5\', \'0.0km/s\', \'1.4GHz\', for channel, velocity, and frequency modes, respectively.',
               'width': 'Channel width of the output visibilities. Used for regridding, together with \'start\', and \'nchan\'. It can be in different units, depending on the regridding mode: number of input channels (mode=\'channel\'), velocity (mode=\'velocity\'), or frequency (mode=\'frequency\'. Example values: \'2\', \'1.0km/s\', \'1.0kHz\', for channel, velocity, and frequency modes, respectively.',
               'interpolation': 'Spectral interpolation method',
               'phasecenter': 'Phase center direction to be used for the spectral coordinate transformation: direction measure or field index',
               'restfreq': 'rest frequency (see help)',
               'outframe': 'Output frame (not case-sensitive, \'\'=keep input frame)',
               'veltype': 'velocity definition',
               'hanning': ' If true, Hanning smooth data before regridding to remove Gibbs ringing.',

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
        a['passall']  = False
        a['field']  = ''
        a['spw']  = ''
        a['selectdata']  = True
        a['antenna']  = ''
        a['timerange']  = ''
        a['scan']  = ''
        a['array']  = ''
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

        if self.parameters['selectdata']  == True:
            a['timerange'] = ''
            a['array'] = ''
            a['antenna'] = ''
            a['scan'] = ''

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
cvel_cli = cvel_cli_()
