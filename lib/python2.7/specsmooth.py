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
import task_specsmooth
def specsmooth(imagename='', outfile='', box='', chans='', stokes='', region='', mask='', overwrite=False, stretch=False, axis=-1, function='boxcar', width=2, dmethod='copy'):

        """Smooth an image region in one dimension
    
Smooth an image region in one dimension.

ARAMETER SUMMARY
imagename       Name of the input (CASA, FITS, MIRIAD) image
box             Rectangular region to select in direction plane. 
                Default is to use the entire direction plane. Only a single box may be specified.
chans           Channels to use. Channels must be contiguous.
                Default is to use all channels.
stokes          Stokes planes to use. Planes specified must be
                contiguous. Default is to use all Stokes planes.
region          Region selection. Default is to use the full image.
mask            Mask to use. Default is none.
overwrite       If the specified outfile already exists, overwrite it if True.
stretch         Stretch the input mask if necessary and possible? Only used if a mask is specified.
                
axis            Pixel axis along which to do the convolution <0 means use the spectral axis.
function        Convolution function to use. Supported values are "boxcar" and "hanning". Minimum
                match is supported.
width           Width of boxcar in pixels. Used only if function parameter minimally matches "boxcar".
dmethod         Plane decimation method. "" means no decimation should be performed. Other supported
                values are "copy" and "mean". Minimal match is supported. See below for details.

This application performs one dimensional convolution along a specified axis of an image
or selected region of an image. Hanning smoothing and boxcar smoothing are supported. 
Both float valued and complex valued images are supported. Masked pixel values are set to
zero prior to convolution. All nondefault pixel masks are ignored during
the calculation. The convolution is done in the image domain (i.e., not
with an FFT).

BOXCAR SMOOTHING

One dimensional boxcar convolution is defined by

z[i] = (y[i] + y[i+i] + ... + y[i+w])/w

where z[i] is the value at pixel i in the box car smoothed image, y[k]
is the pixel value of the input image at pixel k, and w is a postivie integer
representing the width of the boxcar in pixels.  The length of the axis along which the
convolution is to occur must be at least w pixels in the selected region,
unless decimation using the mean function is chosen in which case the axis
length must be at least 2*w (see below).

If dmethod="" (no decimation), the length of the output axis will be equal
to the length of the input axis - w + 1. The pixel mask, ORed with the OTF mask
if specified, is copied from the selected region of the input image to the
output image. Thus for example, if the selected region in the input image has
six planes along the convolution axis, if the specified boxcar width is 2,
and if the pixel values, which are all unmasked, on a slice along this axis
are [1, 2, 5, 10, 17, 26], then the corresponding output slice will be of
length five pixels and the output pixel values will be [1.5, 3.5, 7.5, 13.5, 21.5].

If dmethod="copy", the output image is the image calculated
if dmethod="", except that only every wth plane is kept. Both the pixel and mask
values of these planes are copied directly to the output image, without further
processing. Thus for example, if the selected region in the input image has six
planes along the convolution axis, the boxcar width is chosen to be 2, and if
the pixel values, which are all unmasked, on a slice along this axis are [1, 2,
5, 10, 17, 26], the corresponding output pixel values will be [1.5, 7.5, 21.5].

If dmethod="mean", first the image described in the dmethod=""
case is calculated. Then, the ith plane of the output image is calculated by
averaging the i*w to the (i+1)*w-1  planes of this intermediate image. Thus, for
example, if the selected region in the input image has six planes along the
convolution axis, the boxcar width is chosen to be 2, and if the pixel values,
which are all unmasked, on a slice along this axis are [1, 2, 5, 10, 17, 26],
then the corresponding output pixel values will be [2.5, 10.5]. Any pixels at the
end of the convolution axis of the intermediate image that do not fall into a complete bin of
width w are ignored. Masked values are taken into consideration when forming this
average, so if one of the values is masked, it is not used in the average. If at
least one of the values in the intermediate image bin is not masked, the
corresponding output pixel will not be masked.

HANNING SMOOTHING

Hanning convolution of one axis of an image is defined by

z[i] = 0.25*y[i-1] + 0.5*y[i] + 0.25*y[i+1]       (equation 1)

where z[i] is the value at pixel i in the hanning smoothed image, and
y[i-1], y[i], and y[i+1] are the values of the input image at pixels i-1,
i, and i+1 respectively. The length of the axis along which the convolution is
to occur must be at least three pixels in the selected region. 
    
If dmethod="" (no decimation of image planes), the length of the output axis will
be the same as that of the input axis. The output pixel values along the convolution
axis will be related to those of the input values according to equation 1, except
the first and last pixels. In that case, 
    
    z[0] = 0.5*(y[0] + y[1])
    
and,
    
    z[N-1] = 0.5*(y[N-2] + y[N-1])
    
where N is the number of pixels along the convolution aixs.
The pixel mask, ORed with the OTF mask if specified, is copied from the selected
region of the input image to the output image. Thus for example, if the selected
region in the input image has six planes along the convolution axis, and if the pixel
values, which are all unmasked, on a slice along this axis are [1, 2, 5, 10, 17, 26],
the corresponding output pixel values will be [1.5, 2.5, 5.5, 10.5, 17.5, 21.5].
    
If dmethod="copy", the output image is the image calculated if
dmethod="", except that only the odd-numbered planes are kept. Furthermore, if the
number of planes along the convolution axis in the selected region of the input image
is even, the last odd number plane is also discarded. Thus, if the selected region
has N pixels along the convolution axis in the input image, along the convolution
axis the output image will have (N-1)/2 planes if N is odd, or (N-2)/2 planes if N
is even. The pixel and mask values are copied directly, without further
processing. Thus for example, if the selected region in the input image has six planes
along the convolution axis, and if the pixel values, which are all unmasked, on a slice
along this axis are [1, 2, 5, 10, 17, 26], the corresponding output pixel values will be
[2.5, 10.5].

If dmethod="mean", first the image described in the dmethod="" case
is calculated. The first plane and last plane(s) of that image are then discarded as
described in the dmethod="copy" case. Then, the ith plane of the output
image is calculated by averaging the (2*i)th and (2*i + 1)th planes of the intermediate
image. Thus for example, if the selected region in the input image has six planes
along the convolution axis, and if the pixel values, which are all unmasked, on a slice
along this axis are [1, 2, 5, 10, 17, 26], the corresponding output pixel values will be
[4.0, 14.0]. Masked values are taken into consideration when forming this average, so if
one of the values is masked, it is not used in the average. If at least one of the values
in the input pair is not masked, the corresponding output pixel will not be masked.


EXAMPLES

# boxcar smooth the spectral axis by 3 pixels, say it's axis 2 and only
# write every other pixel
specsmooth(imagename="mynonsmoothed.im", outfile="myboxcarsmoothed.im",
axis=2, function="boxcar", dmethod="copy", width=3, overwrite=True)

# hanning smooth the spectral axis, say it's axis 2 and do not perform decimation
# of image planes
specsmooth(imagename="mynonsmoothed.im", outfile="myhanningsmoothed.im",
axis=2, dmethod=""," overwrite=True)

        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['region'] = region
        mytmp['mask'] = mask
        mytmp['overwrite'] = overwrite
        mytmp['stretch'] = stretch
        mytmp['axis'] = axis
        mytmp['function'] = function
        mytmp['width'] = width
        mytmp['dmethod'] = dmethod
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'specsmooth.xml')

        casalog.origin('specsmooth')
        if trec.has_key('specsmooth') and casac.utils().verify(mytmp, trec['specsmooth']) :
            result = task_specsmooth.specsmooth(imagename, outfile, box, chans, stokes, region, mask, overwrite, stretch, axis, function, width, dmethod)

        else :
          result = False
        return result
