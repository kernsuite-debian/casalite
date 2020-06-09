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
import task_immoments
def immoments(imagename='', moments=[0], axis='spectral', region='', box='', chans='', stokes='', mask='', includepix=-1, excludepix=-1, outfile='', stretch=False):

        """Compute moments from an image
        The spectral moment distributions at each pixel are
        determined.  See the cookbook and User Reference Manual for
        mathematical details.

        The main control of the calculation is given by parameter
        moments:
    
        moments=-1  - mean value of the spectrum
        moments=0   - integrated value of the spectrum
        moments=1   - intensity weighted coordinate;traditionally used to get 
                      'velocity fields'
        moments=2   - intensity weighted dispersion of the coordinate; traditionally
                      used to get "velocity dispersion"
        moments=3   - median of I
        moments=4   - median coordinate
        moments=5   - standard deviation about the mean of the spectrum
        moments=6   - root mean square of the spectrum
        moments=7   - absolute mean deviation of the spectrum
        moments=8   - maximum value of the spectrum
        moments=9   - coordinate of the maximum value of the spectrum
        moments=10  - minimum value of the spectrum
        moments=11  - coordinate of the minimum value of the spectrum

   Keyword arguments:
   imagename    Name of input image
                default: none; example: imagename="ngc5921_task.image"
   moments      List of moments you would like to compute
                default: 0 (integrated spectrum);example: moments=[0,1]
                see list above
   axis         The moment axis
                default: (spectral axis); example: axis=spec
                options: ra, dec, lattitude, longitude, spectral, stokes
   mask         Mask to use. Default is none.  
   stretch      Stretch the input mask if necessary and possible. See below.
   region       Region selection. Default
                is to use the full image.
    box         Rectangular region to select in direction plane. See
                Default is to use the entire direction plane.
                Example: box="10,10,50,50"
                box = "10,10,30,30,35,35,50,50" (two boxes)
    chans       Channels to use. Default is to use
                all channels.
                 
    stokes      Stokes planes to use. Default is to
                use all Stokes planes.
                Example: stokes="IQUV";  
                Example:stokes="I,Q"
    includepix  Range of pixel values to include
                default: [-1] (all pixels); example=[0.02,100.0]
    excludepix  Range of pixel values to exclude
                default: [-1] (don"t exclude pixels); example=[100.,200.]
    outfile     Output image file name (or root for multiple moments)
                default: "" (input+auto-determined suffix);example: outfile="source_moment"

    If stretch is true and if the number of mask dimensions is less than
    or equal to the number of image dimensions and some axes in the
    mask are degenerate while the corresponding axes in the image are not,
    the mask will be stetched in the degenerate axis dimensions. For example,
    if the input image has shape [100, 200, 10] and the input
    mask has shape [100, 200, 1] and stretch is true, the mask will be
    stretched along the third dimension to shape [100, 200, 10]. However if
    the mask is shape [100, 200, 2], stretching is not possible and an
    error will result.

        Example for finding the 1-momment, intensity-weighted
        coordinate, often used for finding velocity fields.
        immoments( axis="spec", imagename="myimage", moment=1, outfile="velocityfields" )

        Example finding the spectral mean, -1 moment, on a specified region
        of the image as defined by the box and stokes parameters
        taskname="immoments"
        default()
        imagename = "myimage"
        moment    =  -1

        axis      = "spec"
        stokes     = "I"
        box       = [55,12,97,32]
        go

        Example using a mask created with a second file to select the
        data used to calculate the 0-moments, integrated values.  In
        this case the mask is from the calibrated.im file and all values
        that have a value greater than 0.5 will be positive in the mask..
        immoments( "clean.image", axis="spec", mask="calibrated.im>0.5", outfile="mom_withmask.im" )
        
If an image has multiple (per-channel beams) and the moment axis is equal to the
spectral axis, each channel will be convolved with a beam that is equal to the beam
having the largest area in the beamset prior to moment determination.



        """
        if type(moments)==int: moments=[moments]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['moments'] = moments
        mytmp['axis'] = axis
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['includepix'] = includepix
        mytmp['excludepix'] = excludepix
        mytmp['outfile'] = outfile
        mytmp['stretch'] = stretch
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'immoments.xml')

        casalog.origin('immoments')
        if trec.has_key('immoments') and casac.utils().verify(mytmp, trec['immoments']) :
            result = task_immoments.immoments(imagename, moments, axis, region, box, chans, stokes, mask, includepix, excludepix, outfile, stretch)

        else :
          result = False
        return result
