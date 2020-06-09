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
import task_tclean
def tclean(vis='', selectdata=True, field='', spw='', timerange='', uvrange='', antenna='', scan='', observation='', intent='', datacolumn='corrected', imagename='', imsize=[100], cell=["1arcsec"], phasecenter='', stokes='I', projection='SIN', startmodel='', specmode='mfs', reffreq='', nchan=-1, start='', width='', outframe='LSRK', veltype='radio', restfreq=[], interpolation='linear', perchanweightdensity=True, gridder='standard', facets=1, psfphasecenter='', chanchunks=1, wprojplanes=1, vptable='', mosweight=True, aterm=True, psterm=False, wbawp=True, conjbeams=False, cfcache='', usepointing=False, computepastep=360.0, rotatepastep=360.0, pointingoffsetsigdev=0.0, pblimit=0.2, normtype='flatnoise', deconvolver='hogbom', scales=[], nterms=2, smallscalebias=0.0, restoration=True, restoringbeam=[], pbcor=False, outlierfile='', weighting='natural', robust=0.5, noise='1.0Jy', npixels=0, uvtaper=[''], niter=0, gain=0.1, threshold=0.0, nsigma=0.0, cycleniter=-1, cyclefactor=1.0, minpsffraction=0.05, maxpsffraction=0.8, interactive=False, usemask='user', mask='', pbmask=0.0, sidelobethreshold=3.0, noisethreshold=5.0, lownoisethreshold=1.5, negativethreshold=0.0, smoothfactor=1.0, minbeamfrac=0.3, cutthreshold=0.01, growiterations=75, dogrowprune=True, minpercentchange=-1.0, verbose=False, fastnoise=True, restart=True, savemodel='none', calcres=True, calcpsf=True, parallel=False):

        """Radio Interferometric Image Reconstruction

    Please refer to the CASAdocs pages for the task tclean for examples.

  
        """
        if type(uvtaper)==str: uvtaper=[uvtaper]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['selectdata'] = selectdata
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['timerange'] = timerange
        mytmp['uvrange'] = uvrange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['observation'] = observation
        mytmp['intent'] = intent
        mytmp['datacolumn'] = datacolumn
        mytmp['imagename'] = imagename
        mytmp['imsize'] = imsize
        mytmp['cell'] = cell
        mytmp['phasecenter'] = phasecenter
        mytmp['stokes'] = stokes
        mytmp['projection'] = projection
        mytmp['startmodel'] = startmodel
        mytmp['specmode'] = specmode
        mytmp['reffreq'] = reffreq
        mytmp['nchan'] = nchan
        mytmp['start'] = start
        mytmp['width'] = width
        mytmp['outframe'] = outframe
        mytmp['veltype'] = veltype
        mytmp['restfreq'] = restfreq
        mytmp['interpolation'] = interpolation
        mytmp['perchanweightdensity'] = perchanweightdensity
        mytmp['gridder'] = gridder
        mytmp['facets'] = facets
        mytmp['psfphasecenter'] = psfphasecenter
        mytmp['chanchunks'] = chanchunks
        mytmp['wprojplanes'] = wprojplanes
        mytmp['vptable'] = vptable
        mytmp['mosweight'] = mosweight
        mytmp['aterm'] = aterm
        mytmp['psterm'] = psterm
        mytmp['wbawp'] = wbawp
        mytmp['conjbeams'] = conjbeams
        mytmp['cfcache'] = cfcache
        mytmp['usepointing'] = usepointing
        mytmp['computepastep'] = computepastep
        mytmp['rotatepastep'] = rotatepastep
        mytmp['pointingoffsetsigdev'] = pointingoffsetsigdev
        mytmp['pblimit'] = pblimit
        mytmp['normtype'] = normtype
        mytmp['deconvolver'] = deconvolver
        mytmp['scales'] = scales
        mytmp['nterms'] = nterms
        mytmp['smallscalebias'] = smallscalebias
        mytmp['restoration'] = restoration
        mytmp['restoringbeam'] = restoringbeam
        mytmp['pbcor'] = pbcor
        mytmp['outlierfile'] = outlierfile
        mytmp['weighting'] = weighting
        mytmp['robust'] = robust
        mytmp['noise'] = noise
        mytmp['npixels'] = npixels
        mytmp['uvtaper'] = uvtaper
        mytmp['niter'] = niter
        mytmp['gain'] = gain
        mytmp['threshold'] = threshold
        mytmp['nsigma'] = nsigma
        mytmp['cycleniter'] = cycleniter
        mytmp['cyclefactor'] = cyclefactor
        mytmp['minpsffraction'] = minpsffraction
        mytmp['maxpsffraction'] = maxpsffraction
        mytmp['interactive'] = interactive
        mytmp['usemask'] = usemask
        mytmp['mask'] = mask
        mytmp['pbmask'] = pbmask
        mytmp['sidelobethreshold'] = sidelobethreshold
        mytmp['noisethreshold'] = noisethreshold
        mytmp['lownoisethreshold'] = lownoisethreshold
        mytmp['negativethreshold'] = negativethreshold
        mytmp['smoothfactor'] = smoothfactor
        mytmp['minbeamfrac'] = minbeamfrac
        mytmp['cutthreshold'] = cutthreshold
        mytmp['growiterations'] = growiterations
        mytmp['dogrowprune'] = dogrowprune
        mytmp['minpercentchange'] = minpercentchange
        mytmp['verbose'] = verbose
        mytmp['fastnoise'] = fastnoise
        mytmp['restart'] = restart
        mytmp['savemodel'] = savemodel
        mytmp['calcres'] = calcres
        mytmp['calcpsf'] = calcpsf
        mytmp['parallel'] = parallel
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'tclean.xml')

        casalog.origin('tclean')
        if trec.has_key('tclean') and casac.utils().verify(mytmp, trec['tclean']) :
            result = task_tclean.tclean(vis, selectdata, field, spw, timerange, uvrange, antenna, scan, observation, intent, datacolumn, imagename, imsize, cell, phasecenter, stokes, projection, startmodel, specmode, reffreq, nchan, start, width, outframe, veltype, restfreq, interpolation, perchanweightdensity, gridder, facets, psfphasecenter, chanchunks, wprojplanes, vptable, mosweight, aterm, psterm, wbawp, conjbeams, cfcache, usepointing, computepastep, rotatepastep, pointingoffsetsigdev, pblimit, normtype, deconvolver, scales, nterms, smallscalebias, restoration, restoringbeam, pbcor, outlierfile, weighting, robust, noise, npixels, uvtaper, niter, gain, threshold, nsigma, cycleniter, cyclefactor, minpsffraction, maxpsffraction, interactive, usemask, mask, pbmask, sidelobethreshold, noisethreshold, lownoisethreshold, negativethreshold, smoothfactor, minbeamfrac, cutthreshold, growiterations, dogrowprune, minpercentchange, verbose, fastnoise, restart, savemodel, calcres, calcpsf, parallel)

        else :
          result = False
        return result
