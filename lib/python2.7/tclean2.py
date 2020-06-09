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
import task_tclean2
def tclean2(vis='', selectdata=True, field='', spw='', timerange='', uvrange='', antenna='', scan='', observation='', intent='', datacolumn='corrected', imagename='', imsize=[100], cell=["1arcsec"], phasecenter='', stokes='I', projection='SIN', startmodel='', specmode='mfs', reffreq='', nchan=-1, start='', width='', outframe='LSRK', veltype='radio', restfreq=[], interpolation='linear', gridder='standard', facets=1, chanchunks=1, wprojplanes=1, aterm=True, psterm=False, wbawp=True, conjbeams=True, cfcache='', computepastep=360.0, rotatepastep=360.0, pblimit=0.2, normtype='flatnoise', deconvolver='hogbom', scales=[], nterms=2, scalebias=0.6, restoringbeam=[], outlierfile='', weighting='natural', robust=0.5, npixels=0, uvtaper=[''], niter=0, gain=0.1, threshold=0.0, cycleniter=-1, cyclefactor=1.0, minpsffraction=0.05, maxpsffraction=0.8, interactive=False, usemask='user', mask='', pbmask=0.0, maskthreshold='', maskresolution='', restart=True, savemodel='none', makeimages='auto', calcres=True, calcpsf=True, restoremodel='auto', writepb='auto', ranks=[]):

        """Radio Interferometric Image Reconstruction

                This is the first release of our refactored imager code. Although most features have
                been used and validated, there are many details that have not been thoroughly tested.
                Feedback will be much appreciated.


                Usage Examples :
                -----------------------

                (A) A suite of test programs that demo all usable modes of tclean on small test datasets
                https://svn.cv.nrao.edu/svn/casa/branches/release-4_5/gcwrap/python/scripts/tests/test_refimager.py
                (B) A set of demo examples for ALMA imaging
                https://casaguides.nrao.edu/index.php/TCLEAN_and_ALMA



    
        """
        if type(uvtaper)==str: uvtaper=[uvtaper]
        if type(ranks)==int: ranks=[ranks]

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
        mytmp['gridder'] = gridder
        mytmp['facets'] = facets
        mytmp['chanchunks'] = chanchunks
        mytmp['wprojplanes'] = wprojplanes
        mytmp['aterm'] = aterm
        mytmp['psterm'] = psterm
        mytmp['wbawp'] = wbawp
        mytmp['conjbeams'] = conjbeams
        mytmp['cfcache'] = cfcache
        mytmp['computepastep'] = computepastep
        mytmp['rotatepastep'] = rotatepastep
        mytmp['pblimit'] = pblimit
        mytmp['normtype'] = normtype
        mytmp['deconvolver'] = deconvolver
        mytmp['scales'] = scales
        mytmp['nterms'] = nterms
        mytmp['scalebias'] = scalebias
        mytmp['restoringbeam'] = restoringbeam
        mytmp['outlierfile'] = outlierfile
        mytmp['weighting'] = weighting
        mytmp['robust'] = robust
        mytmp['npixels'] = npixels
        mytmp['uvtaper'] = uvtaper
        mytmp['niter'] = niter
        mytmp['gain'] = gain
        mytmp['threshold'] = threshold
        mytmp['cycleniter'] = cycleniter
        mytmp['cyclefactor'] = cyclefactor
        mytmp['minpsffraction'] = minpsffraction
        mytmp['maxpsffraction'] = maxpsffraction
        mytmp['interactive'] = interactive
        mytmp['usemask'] = usemask
        mytmp['mask'] = mask
        mytmp['pbmask'] = pbmask
        mytmp['maskthreshold'] = maskthreshold
        mytmp['maskresolution'] = maskresolution
        mytmp['restart'] = restart
        mytmp['savemodel'] = savemodel
        mytmp['makeimages'] = makeimages
        mytmp['calcres'] = calcres
        mytmp['calcpsf'] = calcpsf
        mytmp['restoremodel'] = restoremodel
        mytmp['writepb'] = writepb
        mytmp['ranks'] = ranks
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'tclean2.xml')

        casalog.origin('tclean2')
        if trec.has_key('tclean2') and casac.utils().verify(mytmp, trec['tclean2']) :
            result = task_tclean2.tclean2(vis, selectdata, field, spw, timerange, uvrange, antenna, scan, observation, intent, datacolumn, imagename, imsize, cell, phasecenter, stokes, projection, startmodel, specmode, reffreq, nchan, start, width, outframe, veltype, restfreq, interpolation, gridder, facets, chanchunks, wprojplanes, aterm, psterm, wbawp, conjbeams, cfcache, computepastep, rotatepastep, pblimit, normtype, deconvolver, scales, nterms, scalebias, restoringbeam, outlierfile, weighting, robust, npixels, uvtaper, niter, gain, threshold, cycleniter, cyclefactor, minpsffraction, maxpsffraction, interactive, usemask, mask, pbmask, maskthreshold, maskresolution, restart, savemodel, makeimages, calcres, calcpsf, restoremodel, writepb, ranks)

        else :
          result = False
        return result
