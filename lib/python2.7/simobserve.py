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
import task_simobserve
def simobserve(project='sim', skymodel='', inbright='', indirection='', incell='', incenter='', inwidth='', complist='', compwidth='"8GHz"', comp_nchan=1, setpointings=True, ptgfile='$project.ptg.txt', integration='10s', direction=[''], mapsize=['', ''], maptype='hexagonal', pointingspacing='', caldirection='', calflux='1Jy', obsmode='int', refdate='2014/01/01', hourangle='transit', totaltime='7200s', antennalist='', sdantlist='aca.tp.cfg', sdant=0, outframe='LSRK', thermalnoise='tsys-atm', user_pwv=0.5, t_ground=270., t_sky=260., tau0=0.1, seed=11111, leakage=0.0, graphics='both', verbose=False, overwrite=True):

        """visibility simulation task
  

For more information, see the task pages of simobserve in CASA Docs:

https://casa.nrao.edu/casadocs/


        """
        if type(direction)==str: direction=[direction]
        if type(mapsize)==str: mapsize=[mapsize]

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
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'simobserve.xml')

        casalog.origin('simobserve')
        if trec.has_key('simobserve') and casac.utils().verify(mytmp, trec['simobserve']) :
            result = task_simobserve.simobserve(project, skymodel, inbright, indirection, incell, incenter, inwidth, complist, compwidth, comp_nchan, setpointings, ptgfile, integration, direction, mapsize, maptype, pointingspacing, caldirection, calflux, obsmode, refdate, hourangle, totaltime, antennalist, sdantlist, sdant, outframe, thermalnoise, user_pwv, t_ground, t_sky, tau0, seed, leakage, graphics, verbose, overwrite)

        else :
          result = False
        return result
