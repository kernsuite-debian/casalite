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
import task_imrebin
def imrebin(imagename='', outfile='', factor=[], region='', box='', chans='', stokes='', mask='', dropdeg=False, overwrite=False, stretch=False, crop=True):

        """Rebin an image by the specified integer factors
PARAMETER SUMMARY
imagename        Name of the input (CASA, FITS, MIRIAD) image
outfile          Name of output CASA image. Must be specified.
factor           Array of binning factors for each axis, eg [2,3]. Use imhead or ia.summary()
                 to determine order of axes in your image.
region           Region selection. Default is to use the
                 full image.
box              Rectangular region to select in direction plane.  for
                 details. Default is to use the entire direction plane.
chans            Channels to use. Default is to use all channels.
stokes           Stokes planes to use. Default is to use all
                 Stokes planes. Stokes planes cannot be rebiined.
mask             Mask to use. Default is none.
dropdeg          Drop degenerate axes?
overwrite        Should the image of the same name as specified in outfile be overwritten?
                 If true, the file if it exists is automatically overwritten.
stretch          Stretch the input mask if necessary and possible. 
crop             Only considered if the length of the input axis is not an integral multiple of
                 the associated binning factor. If True, pixels at the end of the axis that do not
                 form a complete bin are not included in the binning. If False, the remaining extra
                 pixels are averaged to form the final bin along the axis.

DESCRIPTION

This application rebins the specified image by the specified integer binning
factors for each axis. It supports both float valued and complex valued images.
The corresponding output pixel value is the average of the
input pixel values. The output pixel will be masked False if there
were no good input pixels.  A polarization axis cannot be rebinned.

The binning factors array must contain at least one element and no more
elements than the number of input image axes. If the number of elements
specified is less than the number of image axes, then the remaining axes
not specified are not rebinned. All specified values must be positive. A
value of one indicates that no rebinning of the associated axis will occur.
Should this array contain any float values, they will be rounded to the next
lowest integer. Note that in many images with both frequency and polarization
axes, the polarization axis preceeds the frequency axis. If you wish to rebin
the frequency axis, it is recommended that you inspect your image with imhead
or ia.summary() to determine the axis ordering.

Binning starts from the origin pixel of the bounding box of the selected region or
the origin pixel of the input image if no region is specified. The value of crop
is used to determine how to handle cases where there are pixels
at the end of the axis that do not form a complete bin. If crop=True,
extra pixels at the end of the axis are discarded. If crop=False, the remaining
pixels are averaged into the final bin along that axis. Should the length
of the axis to be rebinned be an integral multiple of the associated binning
factor, the value of crop is irrelevant. 

A value of dropdeg=True will result in the output image not containing
axes that are degenerate in the specified region or in the input image if no
region is specified. Note that, however, the binning
factors array must still account for degenerate axes, and the binning
factor associated with a degenerate axis must always be 1.

EXAMPLE

# rebin the first two axes (normally the direction axes)
imrebin(imagename="my.im", outfile="rebinned.im", factor=[2,3])

# rebin the frequency axis, which is the fourth axis in this image
imrebin(imagename="my2.im", outfile="rebinned2.im", factor=[1,1,1,4])

    
        """
        if type(factor)==int: factor=[factor]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['factor'] = factor
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['dropdeg'] = dropdeg
        mytmp['overwrite'] = overwrite
        mytmp['stretch'] = stretch
        mytmp['crop'] = crop
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'imrebin.xml')

        casalog.origin('imrebin')
        if trec.has_key('imrebin') and casac.utils().verify(mytmp, trec['imrebin']) :
            result = task_imrebin.imrebin(imagename, outfile, factor, region, box, chans, stokes, mask, dropdeg, overwrite, stretch, crop)

        else :
          result = False
        return result
