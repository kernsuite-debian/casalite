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
from task_apparentsens import apparentsens
class apparentsens_cli_:
    __name__ = "apparentsens"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (apparentsens_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'field':None, 'spw':None, 'intent':None, 'selectdata':None, 'timerange':None, 'uvrange':None, 'antenna':None, 'scan':None, 'observation':None, 'imsize':None, 'cell':None, 'stokes':None, 'specmode':None, 'weighting':None, 'robust':None, 'npixels':None, 'uvtaper':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, field=None, spw=None, intent=None, selectdata=None, timerange=None, uvrange=None, antenna=None, scan=None, observation=None, imsize=None, cell=None, stokes=None, specmode=None, weighting=None, robust=None, npixels=None, uvtaper=None, ):

        """Imaging sensitivity estimataion

        Detailed Description:
Estimates the expected imaging sensitivity as a function of the
               visibility weights and imaging parameters.


        Arguments :
                vis: Name(s) of input visibility file(s)
               default: none;
               example: vis='ngc5921.ms'
                        vis=['ngc5921a.ms','ngc5921b.ms']; multiple MSes

                   Default Value: 

                field: Select fields to image or mosaic.  Use field id(s) or name(s).
                  ['go listobs' to obtain the list id's or names]
               default: ''= all fields
                 If field string is a non-negative integer, it is assumed to
                 be a field index otherwise, it is assumed to be a
                 field name
                 field='0~2'; field ids 0,1,2
                 field='0,4,5~7'; field ids 0,4,5,6,7
                 field='3C286,3C295'; field named 3C286 and 3C295
                 field = '3,4C*'; field id 3, all names starting with 4C
                 For multiple MS input, a list of field strings can be used:
                 field = ['0~2','0~4']; field ids 0-2 for the first MS and 0-4
                         for the second
                 field = '0~2'; field ids 0-2 for all input MSes


                   Default Value: 

                spw: Select spectral window/channels
               NOTE: channels de-selected here will contain all zeros if
                         selected by the parameter mode subparameters.
               default: ''=all spectral windows and channels
                 spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                 spw='0:5~61'; spw 0, channels 5 to 61
                 spw='<2';   spectral windows less than 2 (i.e. 0,1)
                 spw='0,10,3:3~45'; spw 0,10 all channels, spw 3,
                                    channels 3 to 45.
                 spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
                 For multiple MS input, a list of spw strings can be used:
                 spw=['0','0~3']; spw ids 0 for the first MS and 0-3 for the second
                 spw='0~3' spw ids 0-3 for all input MS
                 spw='3:10~20;50~60' for multiple channel ranges within spw id 3
                 spw='3:10~20;50~60,4:0~30' for different channel ranges for spw ids 3 and 4
                 spw='0:0~10,1:20~30,2:1;2;3'; spw 0, channels 0-10,
                      spw 1, channels 20-30, and spw 2, channels, 1,2 and 3
                 spw='1~4;6:15~48' for channels 15 through 48 for spw ids 1,2,3,4 and 6


                   Default Value: 

                intent: Scan Intent(s)

                   default: '' (all)
                   example: intent='TARGET_SOURCE'
                   example: intent='TARGET_SOURCE1,TARGET_SOURCE2'
                   example: intent='TARGET_POINTING*'

                   Default Value: 

                timerange: Range of time to select from data

                   default: '' (all); examples,
                   timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                   Note: if YYYY/MM/DD is missing date defaults to first
                         day in data set
                   timerange='09:14:0~09:54:0' picks 40 min on first day
                   timerange='25:00:00~27:30:00' picks 1 hr to 3 hr
                             30min on NEXT day
                   timerange='09:44:00' pick data within one integration
                             of time
                   timerange='> 10:24:00' data after this time
                   For multiple MS input, a list of timerange strings can be
                   used:
                   timerange=['09:14:0~09:54:0','> 10:24:00']
                   timerange='09:14:0~09:54:0''; apply the same timerange for
                                                 all input MSes


                   Default Value: 

                uvrange: Select data within uvrange (default unit is meters)
                   default: '' (all); example:
                   uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                   uvrange='> 4klambda';uvranges greater than 4 kilo lambda
                   For multiple MS input, a list of uvrange strings can be
                   used:
                   uvrange=['0~1000klambda','100~1000klamda']
                   uvrange='0~1000klambda'; apply 0-1000 kilo-lambda for all
                                            input MSes
 
                   Default Value: 

                antenna: Select data based on antenna/baseline

                   default: '' (all)
                   If antenna string is a non-negative integer, it is
                   assumed to be an antenna index, otherwise, it is
                   considered an antenna name.
                   antenna='5\&6'; baseline between antenna index 5 and
                                 index 6.
                   antenna='VA05\&VA06'; baseline between VLA antenna 5
                                       and 6.
                   antenna='5\&6;7\&8'; baselines 5-6 and 7-8
                   antenna='5'; all baselines with antenna index 5
                   antenna='05'; all baselines with antenna number 05
                                (VLA old name)
                   antenna='5,6,9'; all baselines with antennas 5,6,9
                                   index number
                   For multiple MS input, a list of antenna strings can be
                   used:
                   antenna=['5','5\&6'];
                   antenna='5'; antenna index 5 for all input MSes
                   antenna='!DV14'; use all antennas except DV14


                   Default Value: 

                scan: Scan number range

                   default: '' (all)
                   example: scan='1~5'
                   For multiple MS input, a list of scan strings can be used:
                   scan=['0~100','10~200']
                   scan='0~100; scan ids 0-100 for all input MSes


                   Default Value: 

                observation: Observation ID range
                   default: '' (all)
                   example: observation='1~5'

                   Default Value: 

                imsize: Number of pixels
         example :  imsize = [350,250]
                           imsize = 500 is equivalent to [500,500]
         To take proper advantage of internal optimized FFT routines, the
         number of pixels must be even and factorizable by 2,3,5,7 only.

                   Default Value: 100

                cell: Cell size
               example: cell=['0.5arcsec,'0.5arcsec'] or
               cell=['1arcmin', '1arcmin']
               cell = '1arcsec' is equivalent to ['1arcsec','1arcsec']

                   Default Value: "1arcsec"

                stokes: Stokes Planes to make (I only, for now)
               default='I'; example: stokes='IQUV';
                 Options: 'I','Q','U','V','IV','QU','IQ','UV','IQUV','RR','LL','XX','YY','RRLL','XXYY','pseudoI'

                             Note : Due to current internal code constraints, if any correlation pair
                                        is flagged, by default, no data for that row in the MS will be used.
                                        So, in an MS with XX,YY, if only YY is flagged, neither a
                                        Stokes I image nor an XX image can be made from those data points.
                                        In such a situation, please split out only the unflagged correlation into
                                        a separate MS.

                             Note : The 'pseudoI' option is a partial solution, allowing Stokes I imaging
                                    when either of the parallel-hand correlations are unflagged.

                             The remaining constraints shall be removed (where logical) in a future release.


                   Default Value: I
                   Allowed Values:
                                I
                                Q
                                U
                                V
                                IV
                                QU
                                IQ
                                UV
                                IQUV
                                RR
                                LL
                                XX
                                YY
                                RRLL
                                XXYY
                                pseudoI

                specmode: Spectral definition mode (mfs only, for now)

                       mode='mfs' : Continuum imaging with only one output image channel.
                                             (mode='cont' can also be used here)

                       mode='cube' : Spectral line imaging with one or more channels
                                               Parameters start, width,and nchan define the spectral
                                               coordinate system and can be specified either in terms
                                               of channel numbers, frequency or velocity in whatever
                                               spectral frame is specified in 'outframe'.
                                               All internal and output images are made with outframe as the
                                               base spectral frame. However imaging code internally uses the fixed
                                               spectral frame, LSRK for automatic internal software
                                               Doppler tracking so that a spectral line observed over an
                                               extended time range will line up appropriately.
                                               Therefore the output images have additional spectral frame conversion
                                               layer in LSRK on the top the base frame.


                                               (Note : Even if the input parameters are specified in a frame
                                                           other than LSRK, the viewer still displays spectral
                                                           axis in LSRK by default because of the conversion frame
                                                           layer mentioned above. The viewer can be used to relabel
                                                           the spectral axis in any desired frame - via the spectral
                                                           reference option under axis label properties in the
                                                           data display options window.)


                                               

                        mode='cubedata' : Spectral line imaging with one or more channels
                                                        There is no internal software Doppler tracking so
                                                        a spectral line observed over an extended time range
                                                        may be smeared out in frequency. There is strictly
                                                        no valid spectral frame with which to label the output
                                                        images, but they will list the frame defined in the MS.



                   Default Value: mfs
                   Allowed Values:
                                mfs
                                cont
                                cube
                                cubedata

                weighting: Weighting scheme (natural,uniform,briggs,superuniform,radial)

                       During gridding of the dirty or residual image, each visibility value is
                       multiplied by a weight before it is accumulated on the uv-grid.
                       The PSF's uv-grid is generated by gridding only the weights (weightgrid).

                       weighting='natural' : Gridding weights are identical to the data weights
                                                         from the MS. For visibilities with similar data weights,
                                                         the weightgrid will follow the sample density
                                                         pattern on the uv-plane. This weighting scheme
                                                         provides the maximum imaging sensitivity at the
                                                         expense of a possibly fat PSF with high sidelobes.
                                                         It is most appropriate for detection experiments
                                                         where sensitivity is most important.

                       weighting='uniform' : Gridding weights per visibility data point are the
                                                          original data weights divided by the total weight of
                                                          all data points that map to the same uv grid cell :
                                                          ' data_weight / total_wt_per_cell '.

                                                          The weightgrid is as close to flat as possible resulting
                                                          in a PSF with a narrow main lobe and suppressed
                                                          sidelobes. However, since heavily sampled areas of
                                                          the uv-plane get down-weighted, the imaging
                                                          sensitivity is not as high as with natural weighting.
                                                          It is most appropriate for imaging experiments where
                                                          a well behaved PSF can help the reconstruction.

                       weighting='briggs' :  Gridding weights per visibility data point are given by
                                                         'data_weight / ( A / total_wt_per_cell + B ) ' where
                                                         A and B vary according to the 'robust' parameter.

                                                         robust = -2.0 maps to A=1,B=0 or uniform weighting.
                                                         robust = +2.0 maps to natural weighting.
                                                         (robust=0.5 is equivalent to robust=0.0 in AIPS IMAGR.)

                                                         Robust/Briggs weighting generates a PSF that can
                                                         vary smoothly between 'natural' and 'uniform' and
                                                         allow customized trade-offs between PSF shape and
                                                         imaging sensitivity.

                       weighting='superuniform' : This is similar to uniform weighting except that
                                                                    the total_wt_per_cell is replaced by the
                                                                    total_wt_within_NxN_cells around the uv cell of
                                                                    interest.  ( N = subparameter 'npixels' )

                                                                   This method tends to give a PSF with inner
                                                                   sidelobes that are suppressed as in uniform
                                                                   weighting but with far-out sidelobes closer to
                                                                   natural weighting. The peak sensitivity is also
                                                                   closer to natural weighting.

                       weighting='radial' : Gridding weights are given by ' data_weight * uvdistance '

                                                      This method approximately minimizes rms sidelobes
                                                      for an east-west synthesis array.

               For more details on weighting please see Chapter3
               of Dan Briggs' thesis (http://www.aoc.nrao.edu/dissertations/dbriggs)


                   Default Value: natural
                   Allowed Values:
                                natural
                                uniform
                                briggs
                                radial
                                superuniform

                robust: Robustness parameter for Briggs weighting.

                            robust = -2.0 maps to uniform weighting.
                            robust = +2.0 maps to natural weighting.
                            (robust=0.5 is equivalent to robust=0.0 in AIPS IMAGR.)


                   Default Value: 0.5
                   Allowed Values:
                                -2.0
                                2.0

                npixels: Number of pixels to determine uv-cell size for super-uniform weighting
                      (0 defaults to -/+ 3 pixels)

                     npixels -- uv-box used for weight calculation
                                    a box going from -npixel/2 to +npixel/2 on each side
                                   around a point is used to calculate weight density.

                     npixels=2 goes from -1 to +1 and covers 3 pixels on a side.

                     npixels=0 implies a single pixel, which does not make sense for
                                     superuniform weighting. Therefore, if npixels=0 it will
                                     be forced to 6 (or a box of -3pixels to +3pixels) to cover
                                     7 pixels on a side.


                   Default Value: 0

                uvtaper: uv-taper on outer baselines in uv-plane

                   Apply a Gaussian taper in addition to the weighting scheme specified
                   via the 'weighting' parameter. Higher spatial frequencies are weighted
                   down relative to lower spatial frequencies to suppress artifacts
                   arising from poorly sampled areas of the uv-plane. It is equivalent to
                   smoothing the PSF obtained by other weighting schemes and can be
                   specified either as a Gaussian in uv-space (eg. units of lambda)
                   or as a Gaussian in the image domain (eg. angular units like arcsec).

                   uvtaper = [bmaj, bmin, bpa]

                   NOTE: the on-sky FWHM in arcsec is roughly  the uv taper/200 (klambda).
                   default: uvtaper=[]; no Gaussian taper applied
                   example: uvtaper=['5klambda']  circular taper
                                FWHM=5 kilo-lambda
                            uvtaper=['5klambda','3klambda','45.0deg']
                            uvtaper=['10arcsec'] on-sky FWHM 10 arcseconds
                            uvtaper=['300.0'] default units are lambda
                                in aperture plane


                   Default Value: 
              
            

        Returns: record

        Example :


     TBD.

  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'apparentsens'
        self.__globals__['taskname'] = 'apparentsens'
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
            myparams['intent'] = intent = self.parameters['intent']
            myparams['selectdata'] = selectdata = self.parameters['selectdata']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['imsize'] = imsize = self.parameters['imsize']
            myparams['cell'] = cell = self.parameters['cell']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['specmode'] = specmode = self.parameters['specmode']
            myparams['weighting'] = weighting = self.parameters['weighting']
            myparams['robust'] = robust = self.parameters['robust']
            myparams['npixels'] = npixels = self.parameters['npixels']
            myparams['uvtaper'] = uvtaper = self.parameters['uvtaper']

        if type(uvtaper)==str: uvtaper=[uvtaper]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['intent'] = intent
        mytmp['selectdata'] = selectdata
        mytmp['timerange'] = timerange
        mytmp['uvrange'] = uvrange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['observation'] = observation
        mytmp['imsize'] = imsize
        mytmp['cell'] = cell
        mytmp['stokes'] = stokes
        mytmp['specmode'] = specmode
        mytmp['weighting'] = weighting
        mytmp['robust'] = robust
        mytmp['npixels'] = npixels
        mytmp['uvtaper'] = uvtaper
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'apparentsens.xml')

        casalog.origin('apparentsens')
        try :
          #if not trec.has_key('apparentsens') or not casac.casac.utils().verify(mytmp, trec['apparentsens']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['apparentsens'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('apparentsens', 'apparentsens.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'apparentsens'
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
          result = apparentsens(vis, field, spw, intent, selectdata, timerange, uvrange, antenna, scan, observation, imsize, cell, stokes, specmode, weighting, robust, npixels, uvtaper)

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
             tname = 'apparentsens'
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
#        paramgui.runTask('apparentsens', myf['_ip'])
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
        a['selectdata']  = True
        a['imsize']  = [100]
        a['cell']  = ["1arcsec"]
        a['stokes']  = 'I'
        a['specmode']  = 'mfs'
        a['weighting']  = 'natural'

        a['selectdata'] = {
                    0:odict([{'value':True}, {'field':""}, {'spw':""}, {'timerange':""}, {'uvrange':""}, {'antenna':""}, {'scan':""}, {'observation':""}, {'intent':""}])}
        a['weighting'] = {
                    0:odict([{'value':'natural'}, {'uvtaper':[]}]), 
                    1:{'value':'uniform'}, 
                    2:odict([{'value':'briggs'}, {'robust':0.5}, {'npixels':0}, {'uvtaper':[]}])}

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
    def description(self, key='apparentsens', subkey=None):
        desc={'apparentsens': 'Imaging sensitivity estimataion',
               'vis': 'Name of input visibility file(s)',
               'field': 'field(s) to select',
               'spw': 'spw(s)/channels to select',
               'intent': 'Scan Intent(s)',
               'selectdata': 'Enable data selection parameters',
               'timerange': 'Range of time to select from data',
               'uvrange': 'Select data within uvrange',
               'antenna': 'Select data based on antenna/baseline',
               'scan': 'Scan number range',
               'observation': 'Observation ID range',
               'imsize': 'Number of pixels',
               'cell': 'Cell size',
               'stokes': 'Stokes Planes to make (I only, for now)',
               'specmode': 'Spectral definition mode (mfs only, for now)',
               'weighting': 'Weighting scheme (natural,uniform,briggs)',
               'robust': 'Robustness parameter',
               'npixels': 'Number of pixels to determine uv-cell size (0 : -/+ 3 pixels)',
               'uvtaper': 'uv-taper on outer baselines in uv-plane',

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
        a['intent']  = ''
        a['selectdata']  = True
        a['timerange']  = ''
        a['uvrange']  = ''
        a['antenna']  = ''
        a['scan']  = ''
        a['observation']  = ''
        a['imsize']  = [100]
        a['cell']  = ["1arcsec"]
        a['stokes']  = 'I'
        a['specmode']  = 'mfs'
        a['weighting']  = 'natural'
        a['robust']  = 0.5
        a['npixels']  = 0
        a['uvtaper']  = ['']

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['selectdata']  == True:
            a['field'] = ""
            a['spw'] = ""
            a['timerange'] = ""
            a['uvrange'] = ""
            a['antenna'] = ""
            a['scan'] = ""
            a['observation'] = ""
            a['intent'] = ""

        if self.parameters['weighting']  == 'natural':
            a['uvtaper'] = []

        if self.parameters['weighting']  == 'briggs':
            a['robust'] = 0.5
            a['npixels'] = 0
            a['uvtaper'] = []

        if a.has_key(paramname) :
              return a[paramname]
apparentsens_cli = apparentsens_cli_()
