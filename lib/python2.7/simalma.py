#
# This file was generated using xslt from its XML file
#
# Copyright 2009, Associated Universities Inc., Washington DC
#
import sys
import os
from  casac import *
import string
from taskinit import casalog
from taskinit import xmlpath
#from taskmanager import tm
import task_simalma
def simalma(project='sim', dryrun=True, skymodel='', inbright='', indirection='', incell='', incenter='', inwidth='', complist='', compwidth='"8GHz"', setpointings=True, ptgfile='$project.ptg.txt', integration='10s', direction=[''], mapsize=['', ''], antennalist=['alma.cycle1.1.cfg', 'aca.cycle1.cfg'], hourangle='transit', totaltime=['20min', '1h'], tpnant=0, tptime='0s', pwv=0.5, image=True, imsize=[128, 128], imdirection='', cell='', niter=0, threshold='0.1mJy', graphics='both', verbose=False, overwrite=False):

        """Simulation task for ALMA 
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
        if type(direction)==str: direction=[direction]
        if type(mapsize)==str: mapsize=[mapsize]
        if type(antennalist)==str: antennalist=[antennalist]
        if type(totaltime)==str: totaltime=[totaltime]
        if type(imsize)==int: imsize=[imsize]

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
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'simalma.xml')

        casalog.origin('simalma')
        if trec.has_key('simalma') and casac.utils().verify(mytmp, trec['simalma']) :
            result = task_simalma.simalma(project, dryrun, skymodel, inbright, indirection, incell, incenter, inwidth, complist, compwidth, setpointings, ptgfile, integration, direction, mapsize, antennalist, hourangle, totaltime, tpnant, tptime, pwv, image, imsize, imdirection, cell, niter, threshold, graphics, verbose, overwrite)

        else :
          result = False
        return result
