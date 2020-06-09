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
import task_imsmooth
def imsmooth(imagename='', kernel='gauss', major='', minor='', pa='', targetres=False, kimage='', scale=-1.0, region='', box='', chans='', stokes='', mask='', outfile='', stretch=False, overwrite=False, beam=''):

        """Smooth an image or portion of an image
This task performs a Fourier-based convolution to 'smooth' the
direction plane of an image. Smoothing is typically performed in order to reduce the noise in
an image.

Keyword arguments:

imagename    Input image name. Must be specified.
outfile      Output smoothed image file name. Must be specified.
kernel       Type of kernel to use when smoothing ("g", "gauss", or "gaussian" for a gaussian
             kernel or "b", "box", or "boxcar" for a boxcar kernel), or if the
             image has multiple channels and kernel="commonbeam" (or "c", or "common"), convolve
             all channels to the smallest beam that encloses all beams in the input image, "i" or "image"
             to use an image as the kernel.
             For boxcar smoothing, the major axis is parallel to the y-axis of the image
             and the minor axis is parallel to the x-axis. For a Gaussian, the
             orientation is specified by a position angle. A value of 0 degrees means
             the major axis is parallel to the y-axis and an increasing value of the
             position angle results in a counter-clockwise rotation of the ellipse.
                default: 'gauss'
major        Major axis of kernel which must be specified for boxcar smoothing. For
             Gaussian smoothing, the kernel parameters can alternatively be specified
             in the beam parameter. Standard quantity representations are supported.
             Example "4arcsec".
minor        Minor axis of kernel which must be specified for boxcar smoothing. For
             Gaussian smoothing, the kernel parameters can alternatively be specified
             in the beam parameter. Standard quantity representations are supported.
             Example "3arcsec".
pa           Position angle to use for gaussian kernel, unused for boxcar. 
             The Gaussian kernel parameters can alternatively be specified
             in the beam parameter. Standard quantity representations are supported.
             Example "40deg".
beam         Record specifying Gaussian beam parameters. Do not specify any of
             major, minor, or pa if you choose to specify this parameter.
             Example: {"major": "5arcsec", "minor": "2arcsec", "pa": "20deg"}
targetres    Boolean used only for kernel='gauss'. If True, kernel parameters (major/minor/pa
             or beam) are the resolution of the output image. If false, a gaussian
             with these parameters is convolved with the input image to produce
             the output image.
kimage       The image to be used as the convolution kernel. Only used if kernel="image" or "i".
scale        Scale  factor to use if kernel="i" or "image".  -1.0 means auto-scale, which is the default.
mask         Mask to use. Default is none.
region       Region selection. Default is to use the full image.
box          Rectangular region to select in direction plane. 
             Default is to use the entire direction plane.
             Example: "5, 10, 100, 200".
chans        Channels to use. Default is to use all channels.
stokes       Stokes planes to use. Default is to use
             all Stokes planes.
             Example: 'I'

GAUSSIAN KERNEL

The direction pixels must be square. If they are not, use imregrid to regrid your image onto a grid
of square pixels.

Under the hood, ia.convolve2d() is called with scale=-1 (auto scaling). This means that, when the input image
has a restoring beam, pixel values in the output image are scaled in such a way as to conserve flux density.

Major and minor are the full width at half maximum  (FWHM) of the Gaussian. pa is the position angle
of the Gaussian. The beam parameter offers an alternate way of describing the convolving Gaussian.
If used, neither major, minor, nor pa can be specified. The beam parameter must have exactly three
fields: "major", "minor", and "pa" (or "positionangle"). This is the record format for the output
of ia.restoringbeam(). For example

beam = {"major": "5arcsec", "minor": "2arcsec", "pa": "20deg"}

If both beam and any of major, minor, and/or pa is specified for a Gaussian kernel,
an exception will be thrown.    

Alternatively, if the input image has multiple beams, setting kernel='commonbeam' will result in the
smallest beam that encloses all beams in the image to be used as the target resolution to which to
convolve all planes. 

In addition, the targetres parameter indicates if the specified Gaussian is to be the
resolution of the final image (True) or if it is to be used to convolve the input image.
If True, the input image must have a restoring beam. Use imhead() or ia.restoringbeam()
to check for its existence. If the image has multiple beams and targetres=True,
all planes in the image will be convolved so that the resulting resolution is that
specified by the kernel parameters. If the image has multiple beams and targetres=False,
each plane will be convolved with a Gaussian specified by beam (and hence, in
general, the output image will also have multiple beams that vary with spectral channel
and/or polarization).

If the units on the original image include Jy/beam, the units on the
output image will be rescaled by the ratio of the input and output
beams as well as rescaling by the area of convolution kernel.

If the units on the original image include K, then only the image
convolution kernel rescaling is done. 

BOXCAR KERNEL

major is length of the box along the y-axis and minor is length of the box along the x-axis.
pa is not used and beam should not be specified. The value of targetres is not used.

IN GENERAL

The major, minor, and pa parameters can be specified in one of three ways
   Quantity -- for example major=qa.quantity(1, 'arcsec')
               Note that you can use pixel units, such as 
               major=qa.quantity(1, 'pix')
   String -- for example minor='1pix' or major='0.5arcsec'
             (i.e. a string that the Quanta quantity function accepts).
   Numeric -- for example major=10.
              In this case, the units of major and minor are assumed to 
              be in arcsec and units of pa are assumed to be degrees. 

Note: Using pixel units allows you to convolve axes with different units.

IMAGE KERNEL
If kernel="i" or "image", the image specified by kimage is used to convolve the input image.
The coordinate system of the convolution image is ignored; only the pixel values are considered.

Fourier-based convolution is performed.

The provided kernel can have fewer
dimensions than the image being convolved.  In this case, it will be
padded with degenerate axes.  An error will result if the kernel has
more dimensions than the image.

The scaling of the output image is determined by the argument {\stfaf scale}.
If this is left unset, then the kernel is normalized to unit sum.
If {\stfaf scale} is not left unset, then the convolution kernel
will be scaled (multiplied) by this value.

Masked pixels will be assigned the value 0.0 before convolution.

The output mask is the combination (logical OR) of the default input
\pixelmask\ (if any) and the OTF mask.  Any other input \pixelmasks\
will not be copied.  The function
maskhandler
should be used if there is a need to copy other masks too.


EXAMPLES

# smoothing with a gaussian kernel 20arseconds by 10 arseconds
imsmooth( imagename='my.image', kernel='gauss', major='20arcsec', minor='10arcsec', pa="0deg")

# the same as before, just a different way of specifying the kernel parameters
mybeam = {'major': '20arcsec', 'minor': '10arcsec', 'pa': '0deg'}
imsmooth( imagename='my.image', kernel='gauss', beam=mybeam)

# Smoothing using pixel coordinates and a boxcar kernel.
imsmooth( imagename='new.image', major='20pix', minor='10pix', kernel='boxcar')


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['kernel'] = kernel
        mytmp['major'] = major
        mytmp['minor'] = minor
        mytmp['pa'] = pa
        mytmp['targetres'] = targetres
        mytmp['kimage'] = kimage
        mytmp['scale'] = scale
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['outfile'] = outfile
        mytmp['stretch'] = stretch
        mytmp['overwrite'] = overwrite
        mytmp['beam'] = beam
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'imsmooth.xml')

        casalog.origin('imsmooth')
        if trec.has_key('imsmooth') and casac.utils().verify(mytmp, trec['imsmooth']) :
            result = task_imsmooth.imsmooth(imagename, kernel, major, minor, pa, targetres, kimage, scale, region, box, chans, stokes, mask, outfile, stretch, overwrite, beam)

        else :
          result = False
        return result
