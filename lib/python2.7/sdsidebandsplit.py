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
import task_sdsidebandsplit
def sdsidebandsplit(imagename=[''], outfile='', overwrite=False, signalshift=[], imageshift=[], getbothside=False, refchan=0.0, refval='', otherside=False, threshold=0.2):

        """[EXPERIMENTAL] invoke sideband separation using FFT
Solve signal sideband

    sdsidebandsplit(imagename=['shift_0ch.image', 'shift_132ch.image', 'shift_neg81ch.image'],
                  outfile='separated.image', signalshift=[0.0, +132.0, -81.0],
                  imageshift=[0.0, -132.0, +81.0])

The output image is 'separated.image.signalband'.

Solve both signal and image sidebands (need to set frequency of image sideband explicitly)

    sdsidebandsplit(imagename=['shift_0ch.image', 'shift_132ch.image', 'shift_neg81ch.image'],
                  outfile='separated.image', signalshift=[0.0, +132.0, -81.0],
                  imageshift=[0.0, -132.0, +81.0],
                  getbothside=True, refchan=0.0, refval='805.8869GHz')

The output images are 'separated.image.signalband' and 'separated.image.imageband'
for signal and image sideband, respectively.

Obtain signal sideband image by solving image sideband

    sdsidebandsplit(imagename=['shift_0ch.image', 'shift_132ch.image', 'shift_neg81ch.image'],
                  outfile='separated.image', signalshift=[0.0, +132.0, -81.0],
                  imageshift=[0.0, -132.0, +81.0], otherside=True)

Solution of image sidband is obtained and subtracted from the original (double sideband) spectra
to derive spectra of signal sideband.

  
        """
        if type(imagename)==str: imagename=[imagename]
        if type(signalshift)==float: signalshift=[signalshift]
        if type(imageshift)==float: imageshift=[imageshift]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        mytmp['signalshift'] = signalshift
        mytmp['imageshift'] = imageshift
        mytmp['getbothside'] = getbothside
        mytmp['refchan'] = refchan
        mytmp['refval'] = refval
        mytmp['otherside'] = otherside
        mytmp['threshold'] = threshold
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'sdsidebandsplit.xml')

        casalog.origin('sdsidebandsplit')
        if trec.has_key('sdsidebandsplit') and casac.utils().verify(mytmp, trec['sdsidebandsplit']) :
            result = task_sdsidebandsplit.sdsidebandsplit(imagename, outfile, overwrite, signalshift, imageshift, getbothside, refchan, refval, otherside, threshold)

        else :
          result = False
        return result
