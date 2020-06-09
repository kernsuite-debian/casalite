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
import task_imsubimage
def imsubimage(imagename='', outfile='', box='', region='', chans='', stokes='', mask='', dropdeg=False, overwrite=False, verbose=True, stretch=False, keepaxes=[]):

        """Create a (sub)image from a region of the image
PARAMETER SUMMARY
imagename        Name of the input image
outfile          Name of output file. Must be specified.
box              Rectangular region to select in direction plane. 
                 for details. Default is to use the entire direction plane.
region           Region selection. Default is to use
                 the full image.
chans            Channels to use. Default is to use
                 all channels.
stokes           Stokes planes to use. Default is to
                 use all Stokes planes.
mask             Mask to use. Default ("") is none.
dropdeg          If True, all degenerate axes in the input image will be excluded in the output image.
overwrite        If True, a pre-existing file of the same name as outfile will be overwritten.
verbose          Post additional informative messages to the logger.
stretch          Stretch the input mask if necessary and possible. Only used if a mask is specified.
                 
keepaxes         If dropdeg=True, these are the degenerate axes to keep. Nondegenerate axes are
                 implicitly always kept.
       

OVERVIEW

This task copies all or part of the image to a new image specified by outfile.
Both float and complex valued images are supported.

Sometimes it is useful to drop axes of length one (degenerate axes).
Set {\stfaf dropdeg} equal to True if you want to do this.

The output mask is the combination (logical OR) of the default input
\pixelmask\ (if any) and the OTF mask.  Any other input \pixelmasks\
will not be copied.  Use function maskhandler if you
need to copy other masks too.

If the mask has fewer dimensions than the image and if the shape
of the dimensions the mask and image have in common are the same,
the mask will automatically have the missing dimensions added so
it conforms to the image.

If stretch is true and if the number of mask dimensions is less than
or equal to the number of image dimensions and some axes in the
mask are degenerate while the corresponding axes in the image are not,
the mask will be stetched in the degenerate dimensions. For example,
if the input image has shape [100, 200, 10] and the input
mask has shape [100, 200, 1] and stretch is true, the mask will be
stretched along the third dimension to shape [100, 200, 10]. However if
the mask is shape [100, 200, 2], stretching is not possible and an
error will result.

EXAMPLES

# make a subimage containing only channels 4 to 6 of the original image,
imsubimage(imagename="my.im", outfile="first.im", chans="4~6")

# Same as above command, just specifying chans in an alternate, more verbose
# way
imsubimage(imagename="my.im", outfile="second.im", chans="range=[4pix,6pix]")

# Same as the above command, but even more verbose way of specifying the spectral
# selection. Assumes the direction axes are axes numbers 0 and 1.
ia.open("my.im")
shape = ia.shape()
axes = ia.coordsys().names()
ia.done()
xmax = shape[axes.index("Right Ascension")] - 1
ymax = shape[axes.index("Declination")] - 1
reg = "box[[0pix,0pix],[" + str(xmax) + "pix, " + str(ymax) + "pix]] range=[4pix,6pix]"
imsubimage(imagename="my.im", outfile="third.im", region=reg)

# As an example of the usage of the keepaxes parameter, consider an image
# that has axes RA, Dec, Stokes, and Freq. The Stokes and Freq axes are both
# degenerate while the RA and Dec axes are not, and it is desired to make a
# subimage in which the Stokes axis is discarded. The following command will
# accomplish that.
imsubimage(imagename="my.im", outfile="discarded_stokes.im", dropdeg=True, keepaxes=[3])


        """
        if type(keepaxes)==int: keepaxes=[keepaxes]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['box'] = box
        mytmp['region'] = region
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['dropdeg'] = dropdeg
        mytmp['overwrite'] = overwrite
        mytmp['verbose'] = verbose
        mytmp['stretch'] = stretch
        mytmp['keepaxes'] = keepaxes
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'imsubimage.xml')

        casalog.origin('imsubimage')
        if trec.has_key('imsubimage') and casac.utils().verify(mytmp, trec['imsubimage']) :
            result = task_imsubimage.imsubimage(imagename, outfile, box, region, chans, stokes, mask, dropdeg, overwrite, verbose, stretch, keepaxes)

        else :
          result = False
        return result
