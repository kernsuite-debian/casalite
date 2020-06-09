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
from task_simalma import simalma
class simalma_cli_:
    __name__ = "simalma"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (simalma_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'project':None, 'dryrun':None, 'skymodel':None, 'inbright':None, 'indirection':None, 'incell':None, 'incenter':None, 'inwidth':None, 'complist':None, 'compwidth':None, 'setpointings':None, 'ptgfile':None, 'integration':None, 'direction':None, 'mapsize':None, 'antennalist':None, 'hourangle':None, 'totaltime':None, 'tpnant':None, 'tptime':None, 'pwv':None, 'image':None, 'imsize':None, 'imdirection':None, 'cell':None, 'niter':None, 'threshold':None, 'graphics':None, 'verbose':None, 'overwrite':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, project=None, dryrun=None, skymodel=None, inbright=None, indirection=None, incell=None, incenter=None, inwidth=None, complist=None, compwidth=None, setpointings=None, ptgfile=None, integration=None, direction=None, mapsize=None, antennalist=None, hourangle=None, totaltime=None, tpnant=None, tptime=None, pwv=None, image=None, imsize=None, imdirection=None, cell=None, niter=None, threshold=None, graphics=None, verbose=None, overwrite=None, ):

        """Simulation task for ALMA 

        Detailed Description:

This task simulates ALMA observation including 12-m, ACA 7-m and total
power arrays, and images and analyzes simulated data.

This task makes multiple calls to simobserve (to calculate
visibilities and total power spectra), followed by gridding of total
power spectra (if total power is requested), concatenation of the
simulated visibilities, calls to the simanalyze task for visibility
inversion and deconvolution and calculation of difference and fidelity
images, and feathering of single dish and interferometric data.

These steps may not all be familiar to new users, so the simalma task
runs by default in a "dryrun" mode, in which it assesses the user's
input parameters and sky model, and prints an informational report
including the required calls to other CASA tasks, both to the screen
and to a text file in the project directory (defined below).

The user can modify their parameters based on the information, then
either run with dryrun=False to actually call the other tasks to
create the simulated data, or run the other tasks individually one at
a time to better understand and control the process.

NOTE The ALMA project is refining the optimal method of combining the
three types of data.  If that best practice is changed after this
release of CASA, the user can control the process by modifying the
calls to the other CASA tasks.

        Arguments :
                project: root prefix for output file names
                   Default Value: sim

                dryrun: dryrun=True will only produce the informative report, not run simobserve/analyze
                   Default Value: True

                skymodel: model image to observe
                   Default Value: 

                inbright: scale surface brightness of brightest pixel e.g. "1.2Jy/pixel"
                   Default Value: 

                indirection: set new direction e.g. "J2000 19h00m00 -40d00m00"
                   Default Value: 

                incell: set new cell/pixel size e.g. "0.1arcsec"
                   Default Value: 

                incenter: set new frequency of center channel e.g. "89GHz" (required even for 2D model)
                   Default Value: 

                inwidth: set new channel width e.g. "10MHz" (required even for 2D model)
                   Default Value: 

                complist: componentlist to observe
                   Default Value: 

                compwidth: bandwidth of components
                   Default Value: "8GHz"

                setpointings: 
                   Default Value: True

                ptgfile: list of pointing positions
                   Default Value: $project.ptg.txt

                integration: integration (sampling) time
                   Default Value: 10s

                direction: "J2000 19h00m00 -40d00m00" or "" to center on model
                   Default Value: 

                mapsize: angular size of map or "" to cover model
                   Default Value: 
  
  
      

                antennalist: antenna position files of ALMA 12m and 7m arrays
                   Default Value: 
        alma.cycle1.1.cfg
        aca.cycle1.cfg
      

                hourangle: hour angle of observation center e.g. -3:00:00, or "transit"
                   Default Value: transit

                totaltime: total time of observation; vector corresponding to antennalist
                   Default Value: 
        20min
        1h
      

                tpnant: Number of total power antennas to use (0-4)
                   Default Value: 0
                   Allowed Values:
                                0
                                4

                tptime: total observation time for total power
                   Default Value: 0s

                pwv: Precipitable Water Vapor in mm. 0 for noise-free simulation
                   Default Value: 0.5
                   Allowed Values:
                                0

                image: image simulated data
                   Default Value: True

                imsize: output image size in pixels (x,y) or 0 to match model
                   Default Value: 128128

                imdirection: set output image direction, (otherwise center on the model)
                   Default Value: 

                cell: cell size with units or "" to equal model
                   Default Value: 

                niter: maximum number of iterations (0 for dirty image)
                   Default Value: 0

                threshold: flux level (+units) to stop cleaning
                   Default Value: 0.1mJy

                graphics: display graphics at each stage to [screen|file|both|none]
                   Default Value: both
                   Allowed Values:
                                screen
                                file
                                both
                                none
                                

                verbose: 
                   Default Value: False

                overwrite: overwrite files starting with $project
                   Default Value: False

        Returns: bool

        Example :

    -------------------------------
    Parameters:

    project -- root filename for all output files.  A subdirectory will be
         created, and all created files will be placed in that subdirectory
         including the informational report.

    -------------------------------
    skymodel -- input image (used as a model of the sky)
       * simalma requires a CASA or fits image. If you merely have a grid of
         numbers, you will need to write them out as fits or write a
         CASA script to read them in and use the ia tool to create an image
         and insert the data.

       * simalma does NOT require a coordinate system in the header. If the
         coordinate information is incomplete, missing, or you would like to
         override it, set the appropriate "in" parameters. NOTE that setting
         those parameters simply changes the header values, ignoring
         any values already in the image. No regridding is performed.

       * If you have a proper Coordinate System, simalma will do its best to
         generate visibilities from that, and then create a synthesis image
         according to the specified user parameters.

       * You can manipulate an image header manually with the "imhead" task.

    inbright -- peak brightness to scale the image to in Jy/pixel,
         or "" for unchanged
       * NOTE: "unchanged" will take the numerical values in your image
         and assume they are in Jy/pixel, even if it says some other unit
         in the header.

    indirection -- central direction to place the sky model image,
         or "" to use whatever is in the image already

    incell -- spatial pixel size to scale the skymodel image,
         or "" to use whatever is in the image already.

    incenter -- frequency to use for the center channel (or only channel,
         if the skymodel is 2D)  e.g. "89GHz",
         or "" to use what is in the header.

    inwidth -- width of channels to use, or "" to use what is in the image
         should be a string representing a quantity with units e.g. "10MHz"
       * NOTE: only works reliably with frequencies, not velocities
       * NOTE: it is not possible to change the number of spectral planes
         of the sky model, only to relabel them with different frequencies
         That kind of regridding can be accomplished with the CASA toolkit.

    -------------------------------
    complist -- component list model of the sky, added to or instead of skymodel
         see http://casaguides.nrao.edu/index.php?title=Simulation_Guide_Component_Lists_%28CASA_4.1%29

    compwidth -- bandwidth of components; if simulating from components only,
         this defines the bandwidth of the MS and output images

    -------------------------------
    setpointings -- if true, calculate a map of pointings and write ptgfile.
       * if graphics are on, display the pointings shown on the model image
       * observations with the ALMA 12m and ACA 7m arrays will observe a
         region of size "mapsize" using the same hexagonal algorithm as
         the ALMA OT, with Nyquist sampling.
       * The total power array maps a slightly (+1 primary beam) larger area
         than the 12m array does, to improve later image combination.
         It samples the region with lattice grids of spacing 0.33 lambda/D.
       * if setpointings=false, read pointings from ptgfile.

    ptgfile -- a text file specifying directions in the same
         format as the example, and optional integration times, e.g.
         #Epoch     RA          DEC      TIME(optional)
         J2000 23h59m28.10 -019d52m12.35 10.0
       * if the time column is not present in the file, it will use
         "integration" for all pointings.
       * NOTE: at this time the file should contain only science pointings:
         simalma will observe these until totaltime is used up.

    integration --- Time interval for each integration e.g '10s'
       * NOTE: to simulate a "scan" longer than one integration, use
         setpointings to generate a pointing file, and then edit the
         file to increase the time at each point to be larger than
         the parameter integration time.

    direction -- mosaic center direction e.g 'J2000 19h00m00 -40d00m00'
         if unset, will use the center of the skymodel image.
       * can optionally be a list of pointings, otherwise
       * simobserve will cover a region of size mapsize according to maptype

    mapsize -- angular size of mosaic map to simulate.
       * set to "" to cover the model image

    -------------------------------
    antennalist -- vector of ascii files containing antenna positions,
         one for each configuration of 7m or 12m dishes.
       * NOTE: In this task, it should be an ALMA configuration.
       * standard arrays are found in your CASA data repository,
         os.getenv("CASAPATH").split()[0]+"/data/alma/simmos/"
       * a string of the form "alma;0.5arcsec" will be parsed into a
         12m ALMA configuration - see casaguides.nrao.edu
       * examples: ['alma.cycle2.5.cfg','aca.cycle2.i.cfg']
              ['alma.cycle1;0.3arcsec','alma.cycle1.1.cfg','aca.i.cfg']

    hourangle -- hour angle of observation e.g. '-3h'

    totaltime --- total time of observations. This should either be a scalar
         time quantity expressed as a string e.g. '1h', '3600sec', '10min',
         or a vector of such quantities, corresponding to the elements of
         the antennalist vector, e.g. ['5min','20min','3h'].  If you
         specify a scalar, that will be used for the highest resolution
         12m configuration in antennalist, and any lower resolution 12m
         configurations, any 7m configurations, and any TP configurations
         will have observing times relative to totaltime of 0.5, 2,and 4,
         respectively.
    -------------------------------

    tpnant -- the number of total power antennas to use in simulation.

    tptime -- if tpnant>0, the user must specify the observing time for
         total power as a CASA quantity e.g. '4h'.
       * NOTE: this is not broken up among multiple days -
         a 20h track will include observations below the horizon,
         which is probably not what is desired.

    -------------------------------
    pwv -- precipitable water vapor if constructing an atmospheric model.
         Set 0 for noise-free simulation. When pwv>0, thermal noise is
         applied to the simulated data.
       * J. Pardo's ATM library will be used to construct anatmospheric
         profile for the ALMA site:
         altitude 5000m, ground pressure 650mbar, relhum=20%,
         a water layer of pwv at altitude of 2km,
         the sky brightness temperature returned by ATM, and internally
         tabulated receiver temperatures.
       See the documentation of simobserve for more details.

    -------------------------------
    image -- option to invert and deconvolve the simulated measurement set(s)
       * NOTE: interactive clean or more parameters than the subset visible
         here are available by simply running the clean task directly.
       * if graphics turned on, display the clean image and residual image
       * uses Cotton-Schwab clean for single fields and Mosaic gridding
         for multiple fields (with Clark PSF calculation in minor cycles).

    imsize -- image size in spatial pixels (x,y)
       0 or -1 will use the model image size; example: imsize=[500,500]

    imdirection -- phase center for synthesized image.  default is to
       center on the sky model.

    cell -- cell size e.g '10arcsec'.  "" defaults to the skymodel cell

    niter -- number of clean/deconvolution iterations, 0 for no cleaning

    threshold -- flux level to stop cleaning
    -------------------------------
    graphics -- view plots on the screen, saved to file, both, or neither
    verbose -- print extra information to the logger and terminal
    overwrite -- overwrite existing files in the project subdirectory
    -------------------------------

    Please see the documents of simobserve and simanalyze for
    the list of outputs produced.
  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'simalma'
        self.__globals__['taskname'] = 'simalma'
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
            myparams['dryrun'] = dryrun = self.parameters['dryrun']
            myparams['skymodel'] = skymodel = self.parameters['skymodel']
            myparams['inbright'] = inbright = self.parameters['inbright']
            myparams['indirection'] = indirection = self.parameters['indirection']
            myparams['incell'] = incell = self.parameters['incell']
            myparams['incenter'] = incenter = self.parameters['incenter']
            myparams['inwidth'] = inwidth = self.parameters['inwidth']
            myparams['complist'] = complist = self.parameters['complist']
            myparams['compwidth'] = compwidth = self.parameters['compwidth']
            myparams['setpointings'] = setpointings = self.parameters['setpointings']
            myparams['ptgfile'] = ptgfile = self.parameters['ptgfile']
            myparams['integration'] = integration = self.parameters['integration']
            myparams['direction'] = direction = self.parameters['direction']
            myparams['mapsize'] = mapsize = self.parameters['mapsize']
            myparams['antennalist'] = antennalist = self.parameters['antennalist']
            myparams['hourangle'] = hourangle = self.parameters['hourangle']
            myparams['totaltime'] = totaltime = self.parameters['totaltime']
            myparams['tpnant'] = tpnant = self.parameters['tpnant']
            myparams['tptime'] = tptime = self.parameters['tptime']
            myparams['pwv'] = pwv = self.parameters['pwv']
            myparams['image'] = image = self.parameters['image']
            myparams['imsize'] = imsize = self.parameters['imsize']
            myparams['imdirection'] = imdirection = self.parameters['imdirection']
            myparams['cell'] = cell = self.parameters['cell']
            myparams['niter'] = niter = self.parameters['niter']
            myparams['threshold'] = threshold = self.parameters['threshold']
            myparams['graphics'] = graphics = self.parameters['graphics']
            myparams['verbose'] = verbose = self.parameters['verbose']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']

        if type(direction)==str: direction=[direction]
        if type(mapsize)==str: mapsize=[mapsize]
        if type(antennalist)==str: antennalist=[antennalist]
        if type(totaltime)==str: totaltime=[totaltime]
        if type(imsize)==int: imsize=[imsize]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['project'] = project
        mytmp['dryrun'] = dryrun
        mytmp['skymodel'] = skymodel
        mytmp['inbright'] = inbright
        mytmp['indirection'] = indirection
        mytmp['incell'] = incell
        mytmp['incenter'] = incenter
        mytmp['inwidth'] = inwidth
        mytmp['complist'] = complist
        mytmp['compwidth'] = compwidth
        mytmp['setpointings'] = setpointings
        mytmp['ptgfile'] = ptgfile
        mytmp['integration'] = integration
        mytmp['direction'] = direction
        mytmp['mapsize'] = mapsize
        mytmp['antennalist'] = antennalist
        mytmp['hourangle'] = hourangle
        mytmp['totaltime'] = totaltime
        mytmp['tpnant'] = tpnant
        mytmp['tptime'] = tptime
        mytmp['pwv'] = pwv
        mytmp['image'] = image
        mytmp['imsize'] = imsize
        mytmp['imdirection'] = imdirection
        mytmp['cell'] = cell
        mytmp['niter'] = niter
        mytmp['threshold'] = threshold
        mytmp['graphics'] = graphics
        mytmp['verbose'] = verbose
        mytmp['overwrite'] = overwrite
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'simalma.xml')

        casalog.origin('simalma')
        try :
          #if not trec.has_key('simalma') or not casac.casac.utils().verify(mytmp, trec['simalma']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['simalma'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('simalma', 'simalma.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'simalma'
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
          result = simalma(project, dryrun, skymodel, inbright, indirection, incell, incenter, inwidth, complist, compwidth, setpointings, ptgfile, integration, direction, mapsize, antennalist, hourangle, totaltime, tpnant, tptime, pwv, image, imsize, imdirection, cell, niter, threshold, graphics, verbose, overwrite)

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
             tname = 'simalma'
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
#        paramgui.runTask('simalma', myf['_ip'])
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
        a['dryrun']  = True
        a['skymodel']  = ''
        a['complist']  = ''
        a['setpointings']  = True
        a['antennalist']  = ['alma.cycle1.1.cfg', 'aca.cycle1.cfg']
        a['hourangle']  = 'transit'
        a['totaltime']  = ['20min', '1h']
        a['tpnant']  = 0
        a['pwv']  = 0.5
        a['image']  = True
        a['graphics']  = 'both'
        a['verbose']  = False
        a['overwrite']  = False

        a['skymodel'] = {
                    0:odict([{'notvalue':''}, {'inbright':''}, {'indirection':''}, {'incell':''}, {'incenter':''}, {'inwidth':''}])}
        a['complist'] = {
                    0:odict([{'notvalue':''}, {'compwidth':'8GHz'}])}
        a['setpointings'] = {
                    0:odict([{'value':True}, {'integration':'10s'}, {'direction':''}, {'mapsize':['', '']}]), 
                    1:odict([{'value':False}, {'ptgfile':'$project.ptg.txt'}, {'integration':'10s'}])}
        a['tpnant'] = {
                    0:odict([{'notvalue':0}, {'tptime':'0s'}])}
        a['image'] = {
                    0:odict([{'value':True}, {'imsize':0}, {'imdirection':''}, {'cell':''}, {'niter':0}, {'threshold':'0.1mJy'}]), 
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
    def description(self, key='simalma', subkey=None):
        desc={'simalma': 'Simulation task for ALMA ',
               'project': 'root prefix for output file names',
               'dryrun': 'dryrun=True will only produce the informative report, not run simobserve/analyze',
               'skymodel': 'model image to observe',
               'inbright': 'scale surface brightness of brightest pixel e.g. "1.2Jy/pixel"',
               'indirection': 'set new direction e.g. "J2000 19h00m00 -40d00m00"',
               'incell': 'set new cell/pixel size e.g. "0.1arcsec"',
               'incenter': 'set new frequency of center channel e.g. "89GHz" (required even for 2D model)',
               'inwidth': 'set new channel width e.g. "10MHz" (required even for 2D model)',
               'complist': 'componentlist to observe',
               'compwidth': 'bandwidth of components',
               'setpointings': '',
               'ptgfile': 'list of pointing positions',
               'integration': 'integration (sampling) time',
               'direction': '"J2000 19h00m00 -40d00m00" or "" to center on model',
               'mapsize': 'angular size of map or "" to cover model',
               'antennalist': 'antenna position files of ALMA 12m and 7m arrays',
               'hourangle': 'hour angle of observation center e.g. -3:00:00, or "transit"',
               'totaltime': 'total time of observation; vector corresponding to antennalist',
               'tpnant': 'Number of total power antennas to use (0-4)',
               'tptime': 'total observation time for total power',
               'pwv': 'Precipitable Water Vapor in mm. 0 for noise-free simulation',
               'image': 'image simulated data',
               'imsize': 'output image size in pixels (x,y) or 0 to match model',
               'imdirection': 'set output image direction, (otherwise center on the model)',
               'cell': 'cell size with units or "" to equal model',
               'niter': 'maximum number of iterations (0 for dirty image)',
               'threshold': 'flux level (+units) to stop cleaning',
               'graphics': 'display graphics at each stage to [screen|file|both|none]',
               'verbose': '',
               'overwrite': 'overwrite files starting with $project',

              }

#
# Set subfields defaults if needed
#
        if(subkey == 'True'):
          desc['direction'] = 'center of map or "" to center on the model'
        if(subkey == 'False'):
          desc['integration'] = 'integration time (see below)'

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['project']  = 'sim'
        a['dryrun']  = True
        a['skymodel']  = ''
        a['inbright']  = ''
        a['indirection']  = ''
        a['incell']  = ''
        a['incenter']  = ''
        a['inwidth']  = ''
        a['complist']  = ''
        a['compwidth']  = '"8GHz"'
        a['setpointings']  = True
        a['ptgfile']  = '$project.ptg.txt'
        a['integration']  = '10s'
        a['direction']  = ['']
        a['mapsize']  = ['', '']
        a['antennalist']  = ['alma.cycle1.1.cfg', 'aca.cycle1.cfg']
        a['hourangle']  = 'transit'
        a['totaltime']  = ['20min', '1h']
        a['tpnant']  = 0
        a['tptime']  = '0s'
        a['pwv']  = 0.5
        a['image']  = True
        a['imsize']  = [128, 128]
        a['imdirection']  = ''
        a['cell']  = ''
        a['niter']  = 0
        a['threshold']  = '0.1mJy'
        a['graphics']  = 'both'
        a['verbose']  = False
        a['overwrite']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['skymodel']  != '':
            a['inbright'] = ''
            a['indirection'] = ''
            a['incell'] = ''
            a['incenter'] = ''
            a['inwidth'] = ''

        if self.parameters['complist']  != '':
            a['compwidth'] = '8GHz'

        if self.parameters['setpointings']  == True:
            a['integration'] = '10s'
            a['direction'] = ''
            a['mapsize'] = ['', '']

        if self.parameters['setpointings']  == False:
            a['ptgfile'] = '$project.ptg.txt'
            a['integration'] = '10s'

        if self.parameters['tpnant']  != 0:
            a['tptime'] = '0s'

        if self.parameters['image']  == True:
            a['imsize'] = 0
            a['imdirection'] = ''
            a['cell'] = ''
            a['niter'] = 0
            a['threshold'] = '0.1mJy'

        if a.has_key(paramname) :
              return a[paramname]
simalma_cli = simalma_cli_()
