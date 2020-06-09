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
from task_simobserve import simobserve
class simobserve_cli_:
    __name__ = "simobserve"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (simobserve_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'project':None, 'skymodel':None, 'inbright':None, 'indirection':None, 'incell':None, 'incenter':None, 'inwidth':None, 'complist':None, 'compwidth':None, 'comp_nchan':None, 'setpointings':None, 'ptgfile':None, 'integration':None, 'direction':None, 'mapsize':None, 'maptype':None, 'pointingspacing':None, 'caldirection':None, 'calflux':None, 'obsmode':None, 'refdate':None, 'hourangle':None, 'totaltime':None, 'antennalist':None, 'sdantlist':None, 'sdant':None, 'outframe':None, 'thermalnoise':None, 'user_pwv':None, 't_ground':None, 't_sky':None, 'tau0':None, 'seed':None, 'leakage':None, 'graphics':None, 'verbose':None, 'overwrite':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, project=None, skymodel=None, inbright=None, indirection=None, incell=None, incenter=None, inwidth=None, complist=None, compwidth=None, comp_nchan=None, setpointings=None, ptgfile=None, integration=None, direction=None, mapsize=None, maptype=None, pointingspacing=None, caldirection=None, calflux=None, obsmode=None, refdate=None, hourangle=None, totaltime=None, antennalist=None, sdantlist=None, sdant=None, outframe=None, thermalnoise=None, user_pwv=None, t_ground=None, t_sky=None, tau0=None, seed=None, leakage=None, graphics=None, verbose=None, overwrite=None, ):

        """visibility simulation task

        Detailed Description:

This task simulates interferometric or total power measurment sets. It
is currently optimized for JVLA and ALMA, although many observatories
are included, and adding your own is simply a matter of providing an
antenna location file (see below).
    
simobserve is meant to work in conjunction with the simanalyze
task. Calling simobserve one more times will produce simulated
measurement set(s), which are then gridded, inverted and deconvolved
into output simulated images using simanalyze.
    
ALMA users are encouraged to use the simalma task, which provides
additional information on the multiple simobserve and simanalyze calls
required to simulate an ALMA observation which may consist of 12m
interferometric, 7m interferometric, and 12m total power data.
    
More information and examples are availible at 
http://casaguides.nrao.edu/index.php?title=Simulating_Observations_in_CASA
Please contact the Helpdesk with any questions (see
https://casa.nrao.edu/help_desk_all.shtml)

        Arguments :
                project: root prefix for output file names
                   Default Value: sim

                skymodel: Model image to observe

                   * simobserve uses a CASA or fits image. If you
                     merely have a grid of numbers, you will need to
                     write them out as fits or write a CASA script to
                     read them in and use the ia tool to create an
                     image and insert the data.

                   * simobserve does NOT require a coordinate system
                     in the header. If the coordinate information is
                     incomplete, missing, or you would like to
                     override it, set the appropriate "in"
                     parameters. NOTE that setting those parameters
                     simply changes the header values, ignoring any
                     values already in the image. No regridding is
                     performed. 

                   * You can also manipulate an image header manually
                     with the "imhead" task. 

                   * If you have a proper Coordinate System,
                     simobserve will do its best to generate
                     visibilities from that. 

                   Default Value: 

                inbright: Peak brightness to scale the image to, in Jy/pixel
                     Subparameter of skymodel
                     Default: '' (i.e., unchanged)

                        Example: inbright='1.2Jy/pixel'

                     Note: "unchanged" will take the numerical values
                     in your image and assume they are in Jy/pixel,
                     even if it says some other unit in the header. 

                   Default Value: 

                indirection: Central direction to place the sky model image
                     Subparameter of skymodel
                     Default: '' (use whatever is in the image
                     already)

                        Example: indirection='J2000 19h00m00
                        -40d00m00'

                   Default Value: 

                incell: set new cell/pixel size
                     Subparameter of skymodel
                     Default: '' (use whatever is in the image
                     already)

                        Example: incell='0.1arcsec'

                   Default Value: 

                incenter: Frequency to use for the center channel (or only channel,
if the skymodel is 2D)
                     Subparameter of skymodel
                     Default: '' (use whatever is in the image
                     already)

                        Example: incenter='89GHz'

                   Default Value: 

                inwidth: Set new channel width 
                     Subparameter of skymodel
                     Default: '' (use whatever is in the image
                     already)
                     
                     Should be a string representing a quantity with
                     units e.g. inwidth='10MHz'

                     NOTES: 
                   * Only works reliably with frequencies, not
                     velocities 
                   * It is not possible to change the number of
                     spectral planes of the sky model, only to relabel
                     them with different frequencies That kind of
                     regridding can be accomplished with the CASA
                     toolkit.

                   Default Value: 

                complist: Component list model of the sky, added to or instead of skymodel. See https://casaguides.nrao.edu/index.php/Simulation_Guide_Component_Lists_(CASA_5.4)

                   Default Value: 

                compwidth: Bandwidth of components
                     Subparameter of complist

                     If simulating from components only, this defines
                     the bandwidth of the MS and output images

                        Example: compwidth='8GHz'

                   Default Value: "8GHz"

                comp_nchan: Channelization of components
                     Subparameter of complist

                     If simulating from components only, this defines
                     the number of channels of the MeasurementSet

                        Example: comp_nchan=256

                   Default Value: 1

                setpointings: If true, calculate a map of pointings and write ptgfile. If false, read pointings from ptgfile.
                     Default: True

                     If graphics are on, display the pointings shown
                     on the model image

                   Default Value: True

                ptgfile: A text file specifying directions
                     Subparameter of setpointings=False
                     
                     The text file should have the following format,
                     with optional integration times:
                     Epoch     RA          DEC      TIME(optional)
                     J2000 23h59m28.10 -019d52m12.35 10.0

                     If the time column is not present in the file, it
                     will use "integration" for all pointings.

                     NOTE: at this time the file should contain only
                     science pointings: simobserve will observe these,
                     then optionally the calibrator, then the list of
                     science pointings again, etc, until totaltime is
                     used up.
 
                   Default Value: $project.ptg.txt

                integration: Time interval for each integration
                     Subparameter of setpointings=False

                        Example: integration='10s'

                     NOTE: to simulate a "scan" longer than one
                     integration, use  setpointings to generate a
                     pointing file, and then edit the file to increase
                     the time at each point to be larger than the
                     parameter integration time.

                   Default Value: 10s

                direction: Mosaic center direction.
                     Subparameter of setpointings=True

                        Example: "J2000 19h00m00 -40d00m00" or "" to
                        center on model

                     If unset, will use the center of the skymodel
                     image.
                   * can optionally be a list of pointings, otherwise
                   * simobserve will cover a region of size mapsize
                     according to maptype

                   Default Value: 

                mapsize: Angular size of of mosaic map to simulate.
                     Subparameter of setpointings=True

                     Set to "" to cover model

                   Default Value: 
  
  
      

                maptype: How to calculate the pointings for the mosaic
observation?
                     Subparameter of setpointings=True
                     Options: hexagonal, square (raster), ALMA, etc

                     "ALMA" for the same hex algorithm as the ALMA
                     Cycle 1 OT or "ALMA2012" for the algorithm used
                     in the Cycle 0 OT

                   Default Value: hexagonal
                   Allowed Values:
                                hexagonal
                                square
                                hex
                                ALMA
                                ALMA2012
                                alma
                                ALMA-OT

                pointingspacing: Spacing in between pointings. 
                     Subparameter of setpointings=True

                        Examples: 
                        pointingspacing="0.25PB" 
                        pointingspacing="" for ALMA default
                        INT=lambda/D/sqrt(3), SD=lambda/D/3 

                   Default Value: 

                caldirection: pt source calibrator [experimental]
                   Default Value: 

                calflux: pt source calibrator flux [experimental]
                   Default Value: 1Jy

                obsmode: Observation mode to simulate
                     Options: int(interferometer)|sd(singledish)|""(none)

                     Observation mode to calculate visibilities from a
                     skymodel image (which may have been modified
                     above), an optional component list, and a
                     pointing file (which also may have been generated
                     above).

                     This parameter takes two possible values:
                     - interferometer (or int)
                     - singledish (or sd)
                   * If graphics are on, this observe step will
                     display the array (similar to plotants), the uv
                     coverage, the synthesized (dirty) beam, and
                     ephemeris information 
                   * If simulating from a component list, you should
                     specify "compwidth", the desired bandwidth; and 
		     specify "comp_nchan", the desired channelization
		     if more than one output channel is desired

                   Default Value: int
                   Allowed Values:
                                
                                int
                                sd

                refdate: Date of simulated observation
                     Subparameter of obsmode='int|sd'
                     Not critical unless concatting simulations

                        Example: refdate="2014/05/21"

                   Default Value: 2014/01/01

                hourangle: Hour angle of observation center.
                     Subparameter of obsmode='int|sd'

                         Examples:
                         hourangle="-3:00:00", "5h", or "transit"
 
                   Default Value: transit

                totaltime: Total time of observation or number of repetitions
                     Subparameter of obsmode='int|sd'

                         Example:
                         totaltime='7200s'
                         If a number without units, interpreted as the
                         number of times to repeat the mosaic.

                   Default Value: 7200s

                antennalist: Ascii file containing antenna positions.
                     Subparameter of obsmode='int|""'

                     Each row has x y z coordinates and antenna
                     diameter; header lines are required to specify
                     # observatory=ALMA
                     # coordsys=UTM
                     # datum=WGS84
                     # zone=19

                   * Standard arrays are found in your CASA data
                     repository,
                   * If "", simobserve will not not produce an
                     interferometric MS 
                   * A string of the form "alma;0.5arcsec" will be
                   parsed into a full 12m ALMA configuration.  

                   Default Value: 

                sdantlist: single dish antenna position file
                     Subparameter of obsmode='sd|""'

                   Default Value: aca.tp.cfg

                sdant: Index of the antenna in the list to use for total power.  
                     Subparameter of obsmode='sd|""'
                     Default: first antenna on the list. 

                   Default Value: 0

                outframe: spectral frame of MS to create
                     Subparameter of obsmode='sd|""'

                   Default Value: LSRK

                thermalnoise: add thermal noise.
                     Options: tsys-atm, tsys-manual, ""

                     This parameter accepts two settings:
                     - tsys-atm: J. Pardo's ATM library will be used
                     to construct an atmospheric profile for the ALMA
                     site: altitude 5000m, ground pressure 650mbar,
                     relhum=20%, a water layer of user_pwv at altitude
                     of 2km, the sky brightness temperature returned
                     by ATM, and internally tabulated receiver
                     temperatures.
                     - tsys-manual: instead of using the ATM model,
                     specify the zenith  sky brightness and opacity
                     manually.  Noise is added and then the visibility
                     flux scale is referenced above the atmosphere.

                     If left unset (empty string) no thermalnoise
                     corruption is performed.
 
                     In either mode, noise is calculated using an
                     antenna spillover efficiency of 0.96, taper of
                     0.86, surface accuracy of 25 and 300 microns for
                     ALMA and EVLA respectively (using the Ruze
                     formula for surface efficiency), correlator
                     efficiencies of 0.95 and 0.91 for ALMA and EVLA,
                     receiver temperatures 
                     for ALMA of 17, 30, 37, 51, 65,
                     83,147,196,175,230 K interpolated between 35,
                     75,110,145,185,230,345,409,675,867 GHz, 
                     for EVLA of 500, 70,  60,  55,  100, 130, 350 K
                     interpolated between
                     0.33,1.47,4.89,8.44,22.5,33.5,43.3 GHz, 
                     for SMA of 67,  116, 134, 500 K interpolated
                     between 212.,310.,383.,660. GHz.

                     Note: These are only approximate numbers and do
                     not take into account performance at edges of
                     receiver bands, neither are they guaranteed to
                     reflect the most recent measurements.  Caveat
                     emptor. Use the sm tool to add noise if you want
                     more precise control, and use the ALMA exposure
                     time calculator for sensitivity numbers in
                     proposals.

                   Default Value: tsys-atm
                   Allowed Values:
                                
                                tsys-atm
                                tsys-manual

                user_pwv: Precipitable water vapor if constructing an atmospheric
model (in mm)
                      Subparameter of thermalnoise='tsys-atm'

                   Default Value: 0.5
                   Allowed Values:
                                0

                t_ground: Ground/spillover temperature in K
                      Subparameter of
                      thermalnoise='tsys-atm|tsys-manual'

                   Default Value: 270.
                   Allowed Values:
                                0

                t_sky: Atmospheric temperature in K
                      Subparameter of thermalnoise='tsys-manual'

                   Default Value: 260.
                   Allowed Values:
                                0

                tau0: Zenith opacity at observing frequency
                      Subparameter of thermalnoise='tsys-manual'

                      https://casaguides.nrao.edu/index.php/Corrupt
                      for more information on noise, in particular how
                      to add a phase screen using the toolkit

                   Default Value: 0.1
                   Allowed Values:
                                0

                seed: Random number seed
                      Subparameter of
                      thermalnoise='tsys-atm|tsys-manual'

                   Default Value: 11111

                leakage: add cross polarization corruption of this fractional
magnitude (interferometer only)

                   Default Value: 0.0
                   Allowed Values:
                                0

                graphics: View plots on the screen, saved to file, both, or neither
                     Options: screen|file|both|none

                   Default Value: both
                   Allowed Values:
                                screen
                                file
                                both
                                none
                                

                verbose: Print extra information to the logger and terminal
                     Default: False
                     Options: True|False

                   Default Value: False

                overwrite: Overwrite files starting with $project
                     Default: False
                     Options: True|False

                   Default Value: True

        Returns: bool

        Example :

  

For more information, see the task pages of simobserve in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'simobserve'
        self.__globals__['taskname'] = 'simobserve'
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

            myparams['project'] = project = self.parameters['project']
            myparams['skymodel'] = skymodel = self.parameters['skymodel']
            myparams['inbright'] = inbright = self.parameters['inbright']
            myparams['indirection'] = indirection = self.parameters['indirection']
            myparams['incell'] = incell = self.parameters['incell']
            myparams['incenter'] = incenter = self.parameters['incenter']
            myparams['inwidth'] = inwidth = self.parameters['inwidth']
            myparams['complist'] = complist = self.parameters['complist']
            myparams['compwidth'] = compwidth = self.parameters['compwidth']
            myparams['comp_nchan'] = comp_nchan = self.parameters['comp_nchan']
            myparams['setpointings'] = setpointings = self.parameters['setpointings']
            myparams['ptgfile'] = ptgfile = self.parameters['ptgfile']
            myparams['integration'] = integration = self.parameters['integration']
            myparams['direction'] = direction = self.parameters['direction']
            myparams['mapsize'] = mapsize = self.parameters['mapsize']
            myparams['maptype'] = maptype = self.parameters['maptype']
            myparams['pointingspacing'] = pointingspacing = self.parameters['pointingspacing']
            myparams['caldirection'] = caldirection = self.parameters['caldirection']
            myparams['calflux'] = calflux = self.parameters['calflux']
            myparams['obsmode'] = obsmode = self.parameters['obsmode']
            myparams['refdate'] = refdate = self.parameters['refdate']
            myparams['hourangle'] = hourangle = self.parameters['hourangle']
            myparams['totaltime'] = totaltime = self.parameters['totaltime']
            myparams['antennalist'] = antennalist = self.parameters['antennalist']
            myparams['sdantlist'] = sdantlist = self.parameters['sdantlist']
            myparams['sdant'] = sdant = self.parameters['sdant']
            myparams['outframe'] = outframe = self.parameters['outframe']
            myparams['thermalnoise'] = thermalnoise = self.parameters['thermalnoise']
            myparams['user_pwv'] = user_pwv = self.parameters['user_pwv']
            myparams['t_ground'] = t_ground = self.parameters['t_ground']
            myparams['t_sky'] = t_sky = self.parameters['t_sky']
            myparams['tau0'] = tau0 = self.parameters['tau0']
            myparams['seed'] = seed = self.parameters['seed']
            myparams['leakage'] = leakage = self.parameters['leakage']
            myparams['graphics'] = graphics = self.parameters['graphics']
            myparams['verbose'] = verbose = self.parameters['verbose']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']

        if type(direction)==str: direction=[direction]
        if type(mapsize)==str: mapsize=[mapsize]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['project'] = project
        mytmp['skymodel'] = skymodel
        mytmp['inbright'] = inbright
        mytmp['indirection'] = indirection
        mytmp['incell'] = incell
        mytmp['incenter'] = incenter
        mytmp['inwidth'] = inwidth
        mytmp['complist'] = complist
        mytmp['compwidth'] = compwidth
        mytmp['comp_nchan'] = comp_nchan
        mytmp['setpointings'] = setpointings
        mytmp['ptgfile'] = ptgfile
        mytmp['integration'] = integration
        mytmp['direction'] = direction
        mytmp['mapsize'] = mapsize
        mytmp['maptype'] = maptype
        mytmp['pointingspacing'] = pointingspacing
        mytmp['caldirection'] = caldirection
        mytmp['calflux'] = calflux
        mytmp['obsmode'] = obsmode
        mytmp['refdate'] = refdate
        mytmp['hourangle'] = hourangle
        mytmp['totaltime'] = totaltime
        mytmp['antennalist'] = antennalist
        mytmp['sdantlist'] = sdantlist
        mytmp['sdant'] = sdant
        mytmp['outframe'] = outframe
        mytmp['thermalnoise'] = thermalnoise
        mytmp['user_pwv'] = user_pwv
        mytmp['t_ground'] = t_ground
        mytmp['t_sky'] = t_sky
        mytmp['tau0'] = tau0
        mytmp['seed'] = seed
        mytmp['leakage'] = leakage
        mytmp['graphics'] = graphics
        mytmp['verbose'] = verbose
        mytmp['overwrite'] = overwrite
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'simobserve.xml')

        casalog.origin('simobserve')
        try :
          #if not trec.has_key('simobserve') or not casac.casac.utils().verify(mytmp, trec['simobserve']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['simobserve'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('simobserve', 'simobserve.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'simobserve'
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
          result = simobserve(project, skymodel, inbright, indirection, incell, incenter, inwidth, complist, compwidth, comp_nchan, setpointings, ptgfile, integration, direction, mapsize, maptype, pointingspacing, caldirection, calflux, obsmode, refdate, hourangle, totaltime, antennalist, sdantlist, sdant, outframe, thermalnoise, user_pwv, t_ground, t_sky, tau0, seed, leakage, graphics, verbose, overwrite)

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
             tname = 'simobserve'
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
#        paramgui.runTask('simobserve', myf['_ip'])
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
        a['project']  = 'sim'
        a['skymodel']  = ''
        a['complist']  = ''
        a['setpointings']  = True
        a['obsmode']  = 'int'
        a['outframe']  = 'LSRK'
        a['thermalnoise']  = 'tsys-atm'
        a['leakage']  = 0.0
        a['graphics']  = 'both'
        a['verbose']  = False
        a['overwrite']  = True

        a['skymodel'] = {
                    0:odict([{'notvalue':''}, {'inbright':''}, {'indirection':''}, {'incell':''}, {'incenter':''}, {'inwidth':''}])}
        a['complist'] = {
                    0:odict([{'notvalue':''}, {'compwidth':'8GHz'}, {'comp_nchan':1}])}
        a['setpointings'] = {
                    0:odict([{'value':True}, {'integration':'10s'}, {'direction':''}, {'mapsize':['', '']}, {'maptype':'ALMA'}, {'pointingspacing':''}]), 
                    1:odict([{'value':False}, {'ptgfile':'$project.ptg.txt'}, {'integration':'10s'}])}
        a['obsmode'] = {
                    0:odict([{'value':'int'}, {'antennalist':'alma.out10.cfg'}, {'refdate':'2014/05/21'}, {'hourangle':'transit'}, {'totaltime':"7200s"}, {'caldirection':''}, {'calflux':'1Jy'}]), 
                    1:odict([{'value':'sd'}, {'sdantlist':'aca.tp.cfg'}, {'sdant':0}, {'refdate':'2014/05/21'}, {'hourangle':'transit'}, {'totaltime':"7200s"}]), 
                    2:odict([{'value':''}, {'antennalist':''}, {'sdantlist':''}, {'sdant':0}])}
        a['thermalnoise'] = {
                    0:odict([{'value':'tsys-atm'}, {'user_pwv':0.5}, {'t_ground':269.}, {'seed':11111}]), 
                    1:{'value':''}, 
                    2:{'value':'False'}, 
                    3:{'value':'F'}, 
                    4:odict([{'value':'tsys-manual'}, {'t_ground':269.}, {'t_sky':263.}, {'tau0':0.1}, {'seed':11111}]), 
                    5:{'value':''}, 
                    6:{'value':'False'}, 
                    7:{'value':'F'}}

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
    def description(self, key='simobserve', subkey=None):
        desc={'simobserve': 'visibility simulation task',
               'project': 'Root prefix for output file names',
               'skymodel': 'model image to observe',
               'inbright': 'Peak brightness to scale the image to in Jy/pixel',
               'indirection': 'Set new direction, e.g. J2000 19h00m00 -40d00m00',
               'incell': 'Set new cell/pixel size, e.g. 0.1arcsec',
               'incenter': 'Set new frequency of center channel e.g. 89GHz (required even for 2D model)',
               'inwidth': 'Set new channel width, e.g. "10MHz" (required even for 2D model)',
               'complist': 'Componentlist to observe',
               'compwidth': 'Bandwidth of components',
               'comp_nchan': 'Channelization of components',
               'setpointings': 'Calculate a map of pointings?',
               'ptgfile': 'List of pointing positions',
               'integration': 'Integration (sampling) time',
               'direction': 'Mosaic center direction, e.g J2000 19h00m00 -40d00m00',
               'mapsize': 'Angular size of mosaic map to simulate.',
               'maptype': 'how to calculate the pointings for the mosaic observation: hexagonal, square (raster), ALMA, etc.',
               'pointingspacing': 'Spacing in between pointings e.g. 0.25PB. ALMA default: INT=lambda/D/sqrt(3), SD=lambda/D/3 ',
               'caldirection': 'pt source calibrator [experimental]',
               'calflux': 'pt source calibrator flux [experimental]',
               'obsmode': 'Observation mode to simulate [int(interferometer)|sd(singledish)|(none)]',
               'refdate': 'Date of observation. Not critical unless concatting simulations',
               'hourangle': 'Hour angle of observation center, e.g. -3:00:00, 5h',
               'totaltime': 'Total time of observation or number of repetitions',
               'antennalist': 'Interferometer antenna position file',
               'sdantlist': 'Single dish antenna position file',
               'sdant': 'Single dish antenna index in file',
               'outframe': 'Spectral frame of MS to create',
               'thermalnoise': 'add thermal noise: [tsys-atm|tsys-manual|(none)]',
               'user_pwv': 'Precipitable Water Vapor in mm',
               't_ground': 'Ground/spillover ambient temperature in K',
               't_sky': 'Atmospheric temperatur in K',
               'tau0': 'Zenith opacity',
               'seed': 'Random number seed',
               'leakage': 'Cross polarization (interferometer only)',
               'graphics': 'Display graphics at each stage to [screen|file|both|none]',
               'verbose': 'Print extra information to the logger and terminal',
               'overwrite': 'Overwrite existing files in the project subdirectory',

              }

#
# Set subfields defaults if needed
#
        if(subkey == 'True'):
          desc['direction'] = 'center of map or "" to center on the model'
        if(subkey == 'False'):
          desc['integration'] = 'integration time (see below)'
        if(subkey == ''):
          desc['antennalist'] = 'antenna info can be used to calculate the primary beam'
        if(subkey == ''):
          desc['sdantlist'] = 'antenna info can be used to calculate the primary beam'

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['project']  = 'sim'
        a['skymodel']  = ''
        a['inbright']  = ''
        a['indirection']  = ''
        a['incell']  = ''
        a['incenter']  = ''
        a['inwidth']  = ''
        a['complist']  = ''
        a['compwidth']  = '"8GHz"'
        a['comp_nchan']  = 1
        a['setpointings']  = True
        a['ptgfile']  = '$project.ptg.txt'
        a['integration']  = '10s'
        a['direction']  = ['']
        a['mapsize']  = ['', '']
        a['maptype']  = 'hexagonal'
        a['pointingspacing']  = ''
        a['caldirection']  = ''
        a['calflux']  = '1Jy'
        a['obsmode']  = 'int'
        a['refdate']  = '2014/01/01'
        a['hourangle']  = 'transit'
        a['totaltime']  = '7200s'
        a['antennalist']  = ''
        a['sdantlist']  = 'aca.tp.cfg'
        a['sdant']  = 0
        a['outframe']  = 'LSRK'
        a['thermalnoise']  = 'tsys-atm'
        a['user_pwv']  = 0.5
        a['t_ground']  = 270.
        a['t_sky']  = 260.
        a['tau0']  = 0.1
        a['seed']  = 11111
        a['leakage']  = 0.0
        a['graphics']  = 'both'
        a['verbose']  = False
        a['overwrite']  = True

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['skymodel']  != '':
            a['inbright'] = ''
            a['indirection'] = ''
            a['incell'] = ''
            a['incenter'] = ''
            a['inwidth'] = ''

        if self.parameters['complist']  != '':
            a['compwidth'] = '8GHz'
            a['comp_nchan'] = 1

        if self.parameters['setpointings']  == True:
            a['integration'] = '10s'
            a['direction'] = ''
            a['mapsize'] = ['', '']
            a['maptype'] = 'ALMA'
            a['pointingspacing'] = ''

        if self.parameters['setpointings']  == False:
            a['ptgfile'] = '$project.ptg.txt'
            a['integration'] = '10s'

        if self.parameters['obsmode']  == 'int':
            a['antennalist'] = 'alma.out10.cfg'
            a['refdate'] = '2014/05/21'
            a['hourangle'] = 'transit'
            a['totaltime'] = "7200s"
            a['caldirection'] = ''
            a['calflux'] = '1Jy'

        if self.parameters['obsmode']  == 'sd':
            a['sdantlist'] = 'aca.tp.cfg'
            a['sdant'] = 0
            a['refdate'] = '2014/05/21'
            a['hourangle'] = 'transit'
            a['totaltime'] = "7200s"

        if self.parameters['obsmode']  == '':
            a['antennalist'] = ''
            a['sdantlist'] = ''
            a['sdant'] = 0

        if self.parameters['thermalnoise']  == 'tsys-atm':
            a['user_pwv'] = 0.5
            a['t_ground'] = 269.
            a['seed'] = 11111

        if self.parameters['thermalnoise']  == 'tsys-manual':
            a['t_ground'] = 269.
            a['t_sky'] = 263.
            a['tau0'] = 0.1
            a['seed'] = 11111

        if a.has_key(paramname) :
              return a[paramname]
simobserve_cli = simobserve_cli_()
