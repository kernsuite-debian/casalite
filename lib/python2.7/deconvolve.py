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
import task_deconvolve
def deconvolve(imagename='', model='', psf=[''], alg='clark', niter=10, gain=0.1, threshold='0.0mJy', mask='', scales=[0, 3, 10], sigma='0.0mJy', targetflux='1.0Jy', prior=''):

        """Image based deconvolver

        Several algorithms are available to deconvolve an image with a
        known psf (dirty beam), or a Gaussian beam.  The algorithms
        available are clark and hogbom clean, a multiscale clean and a
        mem clean.  For more deconvolution control, use clean.

        Keyword arguments:
        imagename -- Name of input image to be deconvolved
        model     -- Name of output image containing the clean components
        psf       -- Name of psf image (dirty beam) to use
                     example: psf='casaxmlf.image' .
                     If the psf has 3 parameter, then a Gaussian
                     psf is assumed with the values representing
                     the major , minor and position angle  values
                     e.g  psf=['3arcsec', '2.5arcsec', '10deg']
        alg       -- algorithm to use: default = 'clark'
                       options: clark, hogbom, multiscale or mem.
        niter     -- Maximum number of iterations
        gain      -- CLEAN gain parameter; fraction to remove from peak
        threshold -- Halt deconvolution if the maximum residual image is
                     below this threshold.
                     default = '0.0Jy'
        mask      -- mask image (same shape as image and psf) to limit region
                     where deconvoltion is to occur

        ------parameters useful for multiscale only
        scales     -- in pixel numbers; the size of component to deconvolve.
                      default value [0,3,10]
                      recommended sizes are 0 (point), 3 (points per clean beam), and
                      10 (about a factor of three lower resolution)
        ------parameters useful for mem only
        sigma      -- Estimated noise for image
        targetflux -- Target total flux in image 
        prior      -- Prior image to guide mem


  
        """
        if type(psf)==str: psf=[psf]
        if type(scales)==int: scales=[scales]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['model'] = model
        mytmp['psf'] = psf
        mytmp['alg'] = alg
        mytmp['niter'] = niter
        mytmp['gain'] = gain
        if type(threshold) == str :
           mytmp['threshold'] = casac.quanta().quantity(threshold)
        else :
           mytmp['threshold'] = threshold
        mytmp['mask'] = mask
        mytmp['scales'] = scales
        if type(sigma) == str :
           mytmp['sigma'] = casac.quanta().quantity(sigma)
        else :
           mytmp['sigma'] = sigma
        if type(targetflux) == str :
           mytmp['targetflux'] = casac.quanta().quantity(targetflux)
        else :
           mytmp['targetflux'] = targetflux
        mytmp['prior'] = prior
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'deconvolve.xml')

        casalog.origin('deconvolve')
        if trec.has_key('deconvolve') and casac.utils().verify(mytmp, trec['deconvolve']) :
            result = task_deconvolve.deconvolve(imagename, model, psf, alg, niter, gain, threshold, mask, scales, sigma, targetflux, prior)

        else :
          result = False
        return result
