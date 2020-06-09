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
from task_setjy import setjy
class setjy_cli_:
    __name__ = "setjy"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (setjy_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'field':None, 'spw':None, 'selectdata':None, 'timerange':None, 'scan':None, 'intent':None, 'observation':None, 'scalebychan':None, 'standard':None, 'model':None, 'modimage':None, 'listmodels':None, 'fluxdensity':None, 'spix':None, 'reffreq':None, 'polindex':None, 'polangle':None, 'rotmeas':None, 'fluxdict':None, 'useephemdir':None, 'interpolation':None, 'usescratch':None, 'ismms':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, field=None, spw=None, selectdata=None, timerange=None, scan=None, intent=None, observation=None, scalebychan=None, standard=None, model=None, modimage=None, listmodels=None, fluxdensity=None, spix=None, reffreq=None, polindex=None, polangle=None, rotmeas=None, fluxdict=None, useephemdir=None, interpolation=None, usescratch=None, ismms=None, ):

        """Fills the model column with the visibilities of a calibrator

        Detailed Description:

This task places the model visibility amp and phase associated with a
specified clean components image into the model column of the data
set.  The flux density (I,Q,U,V) for a point source calibrator can be
entered explicitly.

setjy need only be run on the calibrator sources with a known flux
density and/or model.

Models are available for 3C48, 3C138, and 3C286 between 1.4 and 43 GHz.  3C147 is available above 13 GHz.  These models are scaled to the precise frequency of the data.  Only I models are presently available.

For Solar System Objects, model determination was updated and it is
available via the 'Butler-JPL-Horizons 2012' standard. Currently they
are modeled as uniformtemperature disks based on their ephemeris at
the time of observation (note that this may oversimplify objects, in
particular asteroids). Specify the name of the object in the 'field'
parameter.

The location of the models is system dependent:  At the AOC, the
models are in the directory::/usr/lib/casapy/data/nrao/VLA/CalModels/
3C286_L.im (egs).

        Arguments :
                vis: Name of input visibility file
                     Default: none

                        Example: vis='ngc5921.ms'

                   Default Value: 

                field: Select field using field id(s) or field name(s)
                     Default: '' (all fields, but run setjy one field
                     at a time)
                     
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
 Field name(s)
                   Default Value: 

                spw: Select spectral window/channels
                     Default: '' (all spectral windows)

                     NOTE: setjy only selects by spectral window, and
                     ignores channel selections.  Fine-grained control
                     could be achieved using (and possibly
                     constructing) a cube for modimage.

                   Default Value: 

                selectdata: Other parameters for selecting part(s) of the MS to
operate on.
                     Default: False
                     Options: False|True

                     Currently all time-oriented and most likely only
                     of interest when using a Solar System object as a
                     calibrator.

                   Default Value: False

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

                scan: Scan number range
                     Subparameter of selectdata=True
                     Default: '' = all

                        Example:scan='1~5'

                     For multiple MS input, a list of scan strings can
                     be used:
                     scan=['0~100','10~200']
                     scan='0~100; scan ids 0-100 for all input MSes
                     Check 'go listobs' to insure the scan numbers are
                     in order.

                   Default Value: 

                intent: Select observing intent
                     Default: '' (all

                        Example: using wildcard characters,
                        intent="*CALIBRATE_AMPLI*" will match field(s)
                        contains CALIBRATE_AMPLI in a list of intents

                     WARNING: If a source with a specific field id has
                     scans that can be distinguishable with intent
                     selection, one should set
                     usescatch=True. Otherwise, any existing model of
                     the source may be cleared and overwritten even if
                     the part of the scans not selected by intent.

                   Default Value: 

                observation: Select by observation ID(s)
                     Subparameter of selectdata=True
                     Default: '' = all

                         Example: observation='0~2,4'

                   Default Value: 

                scalebychan: Scale the flux density on a per channel basis?
                     Default: True
                     Options: True|False

                     This determines whether the fluxdensity set in
                     the model is calculated on a per channel
                     basis. If False then it only one fluxdensity
                     value is calculated per spw.  (Either way, all
                     channels in spw are modified.)  It is effectively
                     True if fluxdensity[0] >  0.0. 

                   Default Value: True

                standard: Flux density standard, used if fluxdensity[0] less than 0.0
                     Default: 'Perley-Butler 2017'
                     Options: 'Baars', 'Perley 90', 'Perley-Taylor
                     95', 'Perley-Taylor 99', 'Perley-Butler 2010',
                     'Perley-Butler 2013', 'Perley-Butler 2017',
                     'Scaife-Heald 2012', 'Stevens-Reynolds 2016',
                     'Butler-JPL-Horizons 2010', 'Butler-JPL-Horizons
                     2012', 'manual' 'fluxscale'

                     All but the last four options are for
                     extragalactic calibrators. The two 'Butler-JPL'
                     standards are for Solar System objects. Note that
                     Scaife-Heald 2012 is for the low frequencies
                     (mostly valid for the frequency range,
                     30-300MHz). 

                     Flux density calculation with Solar System
                     objects depends on ephemerides. The setjy task
                     looks for the data in
                     os.getenv('CASAPATH').split()[0] +
                     '/data/ephemerides/JPL-Horizons'. If no ephemeris
                     for the right object at the right time is
                     present, the calculation will fail.  Ask the
                     helpdesk to make an ephemeris.

                     For more information on individual calibrators,
                     see CASA Docs (https://casa.nrao.edu/casadocs/)

                   Default Value: Perley-Butler 2017
                   Allowed Values:
                                Perley-Butler 2017
                                Perley-Butler 2013
                                Perley-Butler 2010
                                Perley-Taylor 99
                                Baars
                                Perley 90
                                Perley-Taylor 95
                                Butler-JPL-Horizons 2012
                                Butler-JPL-Horizons 2010
                                Scaife-Heald 2012
                                Stevens-Reynolds 2016
                                manual
                                fluxscale

                model: Model image (I only) for setting the model visibilities.
                     Subparameter of standard="Perley-Butler 2010",
                     "Perley-Butler 2013", and "Perley-Butler 2017"
                     Default: '' (do not use a model image)

                     The model can be a cube, and its channels do not
                     have to exactly match those of vis.  It is
                     recommended to use model for sources that are
                     resolved by the observation, but the
                     Butler-JPL-Horizons standard supplies a basic
                     model of what several Solar System objects look
                     like. Each field must be done separately when
                     using a model image. 

                     Both the amplitude and phase are calculated.  At
                     the AOC or CV, the models are located in
                     casa['dirs']['data'] + '/nrao/VLA/CalModels/',
                     e.g. /usr/lib/casapy/data/nrao/VLA/CalModels/3C286_L.im
                     lib64

                     If model does not start with '/', setjy will look
                     for a match in '.', './CalModels', and any
                     CalModels directories within the
                     casa['dirs']['data'] tree (excluding certain
                     branches).

                     Note that model should be deconvolved, i.e. a set
                     of clean components instead of an image that has
                     been convolved with a clean beam.

                   Default Value: 

                listmodels: List the available models for VLA calibrators or Tb
models for Solar System objects
                     Subparameter of standard="Perley-Butler 2010",
                     "Perley-Butler 2013", and "Perley-Butler 2017" 
                     Default: False
                     Options: False|True

                     If True, do nothing but list candidates for model
                     (for extragalactic calibrators) that are present
                     on the system. It looks for *.im* *.mod* in
                     . including its sub-directories but skipping any
                     directory name start with ".", CalModels, and
                     CalModels directories in the casa['dirs']['data']
                     tree. It does not check whether they are
                     appropriate for the MS! If
                     standard='Butler-JPL-Horizons 2012', Tb models
                     (frequency-dependend brightness temperature
                     models) for Solar System objects used in the
                     standard. For standard='Butler-JPL-Horizons
                     2010', the recognized Solar System objects are
                     listed.

                   Default Value: False

                fluxdensity: Specified flux density in Jy [I,Q,U,V]
                     Subparameter of standard="manual"
                     Default: -1 (uses [1,0,0,0] flux density for
                     unrecognized sources, and standard flux densities
                     for ones recognized by the default standard
                     Perley-Butler 2010).  

                     Only one flux density can be specified at a
                     time. The phases are set to zero.
                     setjy will try to use the standard if fluxdensity
                     is not positive.

                        Examples: 
                        fluxdensity=-1  will use the default standard
                        for recognized calibrators (like 3C286, 3C147
                        and 3C48) and insert 1.0  for selected fields
                        with unrecognized sources.
                        field = '1'; fluxdensity=[3.2,0,0,0] will put
                        in a flux density of I=3.2 for field='1'

                     At present (June 2000), this is the only method
                     to insert apolarized flux density model.

                        Example: fluxdensity=[2.63,0.21,-0.33,0.02]
                        will put in I,Q,U,V flux densities of
                        2.63,0.21,-0.33, and 0.02, respectively, in
                        the model column.

                   Default Value: -1

                spix: Spectral index for I flux density
                     Subparameter of standard="manual"
                     Default: [] =>0.0 (no effect)
                     Options: a float or a list of float values

                     S = fluxdensity *
                     (freq/reffreq)**(spix[0]+spix[1]*log(freq/reffreq)+..)

                     Only used if fluxdensity is being used.
                     IMPORTANT: If fluxdensity is positive, and spix
                     is nonzero, then reffreq must be set too!

                     It is applied in the same way to all
                     polarizations, and does not account for Faraday
                     rotation or depolarization.

                        Example: [-0.7, -0.15] for alpha and a curvature term

                   Default Value: 0.0

                reffreq: Reference frequency for spix
                     Subparameter of standard="manual"
                     Default: '1GHz' (this is only here to prevent
                     division by 0!)

                     Given with a unit with an optional frequency
                     frame (if the frame is not given, LSRK is
                     assumed). There should be no space between the
                     value and the unit  (e.g. '100.0GHz' or 'TOPO
                     100.0GHz' are correct but with  '100.0 GHz' you
                     will see a warning message that it will be
                     defaulted to LSRK). 

                        Example: '86.0GHz', 'TOPO 86.0GHz', '4.65e9Hz'

                     NOTE: If the flux density is being scaled by
                     spectral index, then reffreq must be set to
                     whatever reference frequency is correct for the
                     given fluxdensity and spix.  It cannot be
                     determined from vis.  On the other hand, if spix
                     is 0, then any positive frequency can be used
                     (and ignored).

                   Default Value: 1GHz

                polindex: Coefficients of the frequency-dependent linear
polarization index (polarization fraction) 
                     Subparameter of standard="manual"
                     Default: []

                     Expressed as pol. index = sqrt(Q^2+U^2)/I = c0 +
                     c1*((freq-reffreq)/reffreq) +
                     c2*((freq-reffreq)/reffreq)^2 + .. When Q and U
                     flux densities are given fluxdensity, c0 is
                     determined from these flux densities and the
                     entry for c0 in polindex is ignored. Or Q and U
                     flux densities in fluxdensity can be set to 0.0
                     and then polindex[0] and polangle[0] are used to
                     determine Q and U at reffreq.

                        Example: [0.2, -0.01] (= [c0,c1]) 

                   Default Value: 

                polangle: Coefficients of the frequency-dependent linear
polarization angle (in radians)
                     Subparameter of standard="manual"
                     Default: []

                     Expressed as pol. angle = 0.5*arctan(U/Q) = d0 +
                     d1*((freq-reffreq)/reffreq) +
                     d2*((freq-reffreq)/reffreq)^2 + .. When Q and U
                     flux densities are given in fluxdensity, d0 is
                     determined from these flux densities and the
                     entry for d0 in polangle is ignored. Or Q and U
                     flux densities in fluxdensity can be set to 0.0
                     and then polindex[0] and polangle[0] are used to
                     determine Q and U at reffreq. Here polangle
                     parameters are assumed to represent the intrinsic
                     polarization angle.

                        Example: [0.57, 0.2] (=[d0,d1])

                   Default Value: 

                rotmeas: Rotation measure (in rad/m^2)
                     Subparameter of standard="manual"
                     Default: 0.0

                     Note on the use of polindex, polangle and rotmeas
                     When the frequnecy-dependent polindex and
                     polangle are used, be sure to include all the
                     coefficients of both polindex and polangle to
                     describe frequency depencency. Otherwise
                     frequency-dependent Q and U flux densities are
                     not calculated correctly. If rotmeas is given,
                     the calculated Q and U flux densities are then
                     corrected for the Faraday rotation.

                   Default Value: 0.0

                fluxdict: Output dictionary from fluxscale
                     Subparameter of standard="fluxscale"

                     Using the flexibly results, the flux density,
                     spectral index, and reference frequency are
                     extracted and set to fluxdensity, spix, and
                     reffreq parameters, respectively. The field and
                     spw selections can be used to specify subset of
                     the fluxdict to be used to set the model. If they
                     are left as default (field="", spw="") all fields
                     and/or spws in the fluxdict (but those spws with
                     fluxd=-1 will be skipped) are used. 
 
                   Default Value: 

                useephemdir: Use directions in the ephemeris table for the solar
system object?
                     Subparameter of standard="Butler-JPL-Horizons
                     2012",
                     Default: False
                     Options: False|True

                   Default Value: False

                interpolation: Method to be used to interpolate in time for the time
variable sources (3C48,3C138,3C147).
                     Subparameter of standard="Perley-Butler 2013",
                     and "Perley-Butler 2017" 
                     Default: 'nearest'
                     Options: 'nearest|linear|cubic|spline'

                     This parameter is ignored for other non-variable
                     sources in the standard.

                   Default Value: nearest
                   Allowed Values:
                                nearest
                                linear
                                cubic
                                spline
                                

                usescratch: Will create if necessary and use the MODEL_DATA
                     Default: False
                     Options: False|True

                     * If False: 'virtual' model is created. The model
                       information is saved either in the SOURCE_MODEL
                       column in the SOURCE table (if one exists) or
                       in the keyword of the main table in the MS and
                       model visibilities are evaluated on the fly
                       when calculating  calibration or plotting in
                       plotms.
                     * If True: the model visibility will be evaluated
                       and saved on disk in the MODEL_DATA column.
                       This will increase your ms in size by a factor
                       of 1.5 (w.r.t. the case where  you only have
                       the DATA and the CORRECTED_DATA column). Use
                       True if you need to interact with the
                       MODEL_DATA in python, say. Also, use True if
                       you need finer than field and spw  selections
                       using scans/time (and when use with intent
                       selection, please see WARNING section in the
                       intent parameter description).

                     By running usescratch=T, it will remove the
                     existing virtual model from previous
                     runs. usescratch=F will not remove the existing
                     MODEL_DATA but in subsequent process the virtual
                     model with matching field and spw combination
                     will be used if it exists regardless of the
                     presence of the MODEL_DATA column.

                     NOTE: for usescratch=False, timerange, scan, and
                     observation are ignored (i.e. time-specific
                     virtual model is not possible.).

                   Default Value: False

        Returns: void

        Example :

FOR MORE INFORMATION, SEE THE TASK PAGES OF SETJY IN CASA DOCS:
https://casa.nrao.edu/casadocs/

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'setjy'
        self.__globals__['taskname'] = 'setjy'
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
            myparams['scan'] = scan = self.parameters['scan']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['scalebychan'] = scalebychan = self.parameters['scalebychan']
            myparams['standard'] = standard = self.parameters['standard']
            myparams['model'] = model = self.parameters['model']
            myparams['modimage'] = modimage = self.parameters['modimage']
            myparams['listmodels'] = listmodels = self.parameters['listmodels']
            myparams['fluxdensity'] = fluxdensity = self.parameters['fluxdensity']
            myparams['spix'] = spix = self.parameters['spix']
            myparams['reffreq'] = reffreq = self.parameters['reffreq']
            myparams['polindex'] = polindex = self.parameters['polindex']
            myparams['polangle'] = polangle = self.parameters['polangle']
            myparams['rotmeas'] = rotmeas = self.parameters['rotmeas']
            myparams['fluxdict'] = fluxdict = self.parameters['fluxdict']
            myparams['useephemdir'] = useephemdir = self.parameters['useephemdir']
            myparams['interpolation'] = interpolation = self.parameters['interpolation']
            myparams['usescratch'] = usescratch = self.parameters['usescratch']
            myparams['ismms'] = ismms = self.parameters['ismms']

        if type(polindex)==float: polindex=[polindex]
        if type(polangle)==float: polangle=[polangle]

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
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['observation'] = observation
        mytmp['scalebychan'] = scalebychan
        mytmp['standard'] = standard
        mytmp['model'] = model
        mytmp['modimage'] = modimage
        mytmp['listmodels'] = listmodels
        mytmp['fluxdensity'] = fluxdensity
        mytmp['spix'] = spix
        mytmp['reffreq'] = reffreq
        mytmp['polindex'] = polindex
        mytmp['polangle'] = polangle
        mytmp['rotmeas'] = rotmeas
        mytmp['fluxdict'] = fluxdict
        mytmp['useephemdir'] = useephemdir
        mytmp['interpolation'] = interpolation
        mytmp['usescratch'] = usescratch
        mytmp['ismms'] = ismms
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'setjy.xml')

        casalog.origin('setjy')
        try :
          #if not trec.has_key('setjy') or not casac.casac.utils().verify(mytmp, trec['setjy']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['setjy'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('setjy', 'setjy.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'setjy'
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
          result = setjy(vis, field, spw, selectdata, timerange, scan, intent, observation, scalebychan, standard, model, modimage, listmodels, fluxdensity, spix, reffreq, polindex, polangle, rotmeas, fluxdict, useephemdir, interpolation, usescratch, ismms)

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
             tname = 'setjy'
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
#        paramgui.runTask('setjy', myf['_ip'])
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
        a['selectdata']  = False
        a['scalebychan']  = True
        a['standard']  = 'Perley-Butler 2017'
        a['usescratch']  = False

        a['selectdata'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'timerange':''}, {'scan':''}, {'intent':''}, {'observation':''}])}
        a['standard'] = {
                    0:odict([{'value':'Perley-Butler 2017'}, {'model':''}, {'listmodels':False}, {'interpolation':'nearest'}]), 
                    1:odict([{'value':'Perley-Butler 2013'}, {'model':''}, {'listmodels':False}, {'interpolation':'nearest'}]), 
                    2:odict([{'value':'Perley-Butler 2010'}, {'model':''}, {'listmodels':False}]), 
                    3:{'value':'Perley-Taylor 99'}, 
                    4:{'value':'Baars'}, 
                    5:{'value':'Perley 90'}, 
                    6:{'value':'Perley-Taylor 95'}, 
                    7:{'value':'Scaife-Heald 2012'}, 
                    8:{'value':'Stevens-Reynolds 2016'}, 
                    9:odict([{'value':'Butler-JPL-Horizons 2012'}, {'listmodels':False}, {'useephemdir':False}]), 
                    10:{'value':'Butler-JPL-Horizons 2010'}, 
                    11:odict([{'value':'manual'}, {'fluxdensity':[1, 0, 0, 0]}, {'spix':[]}, {'reffreq':'1GHz'}, {'polindex':[]}, {'polangle':[]}, {'rotmeas':0.0}]), 
                    12:odict([{'value':'fluxscale'}, {'fluxdict':{}}])}

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
    def description(self, key='setjy', subkey=None):
        desc={'setjy': 'Fills the model column with the visibilities of a calibrator',
               'vis': 'Name of input visibility file',
               'field': 'Select field using field id(s) or field name(s)',
               'spw': 'Select spectral window/channels',
               'selectdata': 'Other data selection parameters',
               'timerange': 'Select data based on time range',
               'scan': 'Scan number range',
               'intent': 'Select observing intent',
               'observation': 'Select by observation ID(s)',
               'scalebychan': 'Scale the flux density on a per channel basis or else on a per spw basis',
               'standard': 'Flux density standard',
               'model': 'File location for field model',
               'modimage': 'File location for field model (deprecated)',
               'listmodels': 'List the available models for VLA calibrators or Tb models for Solar System objects',
               'fluxdensity': 'Specified flux density in Jy [I,Q,U,V]; (-1 will lookup values)',
               'spix': 'Spectral index (including higher terms) of I fluxdensity',
               'reffreq': 'Reference frequency for spix',
               'polindex': 'Coefficients of an expansion of frequency-dependent linear polarization fraction expression',
               'polangle': 'Coefficients of an expansion of frequency-dependent polarization angle expression (in radians)',
               'rotmeas': 'Rotation measure (in rad/m^2)',
               'fluxdict': 'Output dictionary from fluxscale',
               'useephemdir': 'Use directions in the ephemeris table',
               'interpolation': 'Method to be used to interpolate in time',
               'usescratch': 'Will create if necessary and use the MODEL_DATA ',
               'ismms': 'to be used internally for MMS',

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
        a['selectdata']  = False
        a['timerange']  = ''
        a['scan']  = ''
        a['intent']  = ''
        a['observation']  = ''
        a['scalebychan']  = True
        a['standard']  = 'Perley-Butler 2017'
        a['model']  = ''
        a['modimage']  = ''
        a['listmodels']  = False
        a['fluxdensity']  = -1
        a['spix']  = 0.0
        a['reffreq']  = '1GHz'
        a['polindex']  = []
        a['polangle']  = []
        a['rotmeas']  = 0.0
        a['fluxdict']  = {}
        a['useephemdir']  = False
        a['interpolation']  = 'nearest'
        a['usescratch']  = False
        a['ismms']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['selectdata']  == True:
            a['timerange'] = ''
            a['scan'] = ''
            a['intent'] = ''
            a['observation'] = ''

        if self.parameters['standard']  == 'Perley-Butler 2017':
            a['model'] = ''
            a['listmodels'] = False
            a['interpolation'] = 'nearest'

        if self.parameters['standard']  == 'Perley-Butler 2013':
            a['model'] = ''
            a['listmodels'] = False
            a['interpolation'] = 'nearest'

        if self.parameters['standard']  == 'Perley-Butler 2010':
            a['model'] = ''
            a['listmodels'] = False

        if self.parameters['standard']  == 'Butler-JPL-Horizons 2012':
            a['listmodels'] = False
            a['useephemdir'] = False

        if self.parameters['standard']  == 'manual':
            a['fluxdensity'] = [1, 0, 0, 0]
            a['spix'] = []
            a['reffreq'] = '1GHz'
            a['polindex'] = []
            a['polangle'] = []
            a['rotmeas'] = 0.0

        if self.parameters['standard']  == 'fluxscale':
            a['fluxdict'] = {}

        if a.has_key(paramname) :
              return a[paramname]
setjy_cli = setjy_cli_()
