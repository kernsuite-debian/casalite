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
import task_impv
def impv(imagename='', outfile='', mode='coords', start='', end='', center='', length='', pa='', width=1, unit='arcsec', overwrite=False, region="", chans='', stokes='', mask='', stretch=False):

        """Construct a position-velocity image by choosing two points in the direction plane.
PARAMETER SUMMARY
imagename        Name of the input (CASA, FITS, MIRIAD) image
outfile          Name of output CASA image. Must be specified.
mode             Indicates which sets of parameters to use for defining the slice. mode="coords" means use
                 start and end parameters. mode="length" means use center, length, and pa parameters to define
                 the slice.
start            The starting pixel in the direction plane (array of two values), such as [20, 5] or ["14h20m20.5s","-30d45m25.4s"].
                 Used iff mode="coords".
end              The ending pixel in the direction plane (array of two values), such as [200, 300].
                 Used iff mode="coords".
center           The center of the slice in the direction plane (array of two values), such as [20, 5] or ["14h20m20.5s","-30d45m25.4s"]. 
                 Used iff mode="length".
length           The length of the slice in the direction plane. May be specified as a single numerical value, in which
                 case it is interpreted as the number of pixels, or as a valid quantity which must be conformant with
                 the direction axes units (eg "40arcsec", {"value": 40, "unit": "arcsec"}).
                 Used iff mode="length".
pa               Position angle of the slice, measured from the direction of positive latitude of the positive longitude
                 (eg north through east in an equatorial coordinate system). Must be expressed as a valid angular
                 quantity (eg "40deg", {"value": 40, "unit": "deg"}).
                 Used iff mode="length".
width            Width of slice for averaging pixels perpendicular to the slice which must be an odd positive integer or
                 valid quantity. The averaging using this value occurs after the image has been rotated so the slice lies horizontally.
                 An integer value is interpreted as the number of pixels to average.
                 A value of 1 means no averaging. A value of 3 means average one pixel on each
                 side of the slice and the pixel on the slice. A value of 5 means average 2 pixels
                 on each side of the slice and the pixel on the slice, etc. If a quantity (eg. "4arcsec", qa.quantity("4arcsec"))
                 is specified, the equivalent number of pixels is calculated, and if necessary, rounded up
                 to the next odd integer.
unit             Allows the user to set the unit for the angular offset axis. Must be a unit of angular
                 measure.
overwrite        If output file is specified, this parameter controls if an already existing file by the
                 same name can be overwritten. If true, the user is not prompted, the file
                 if it exists is automatically overwritten.
region           Region specification. Default is to not use a region. If specified,
                 the entire direction plane must be specified. If specified do not specify chans or stokes.
chans            Optional contiguous frequency channel number specification. Default is all channels.
                 If specified, do not specify region.  
stokes           Contiguous stokes planes specification. If specified, do not specify region.
mask             Mask to use. Default is none.
stretch          Stretch the input mask if necessary and possible. Only used if a mask is specified.
                 

Create a position-velocity image. The way the slice is specified is controlled by the mode parameter. When
mode="coords", start end end are used to specified the points between which a slice is taken in the direction
coordinate. If mode="length"  center, pa (position angle), and length are used to specify the slice. The spectral
extent of the resulting image will be that provided by the region specification or the entire spectral range of
the input image if no region is specified. One may not specify a region in direction space; that is accomplished by
specifying the slice as described previously. The parameters start and end may be specified as two
element arrays of numerical values, in which case these values will be interpreted as pixel locations in the input
image. Alternatively, they may be expressed as arrays of two strings each representing the direction. These strings
can either represent quantities (eg ["40.5deg", "0.5rad") or be sexigesimal format (eg ["14h20m20.5s","-30d45m25.4s"],
["14:20:20.5s","-30.45.25.4"]). In addition, they may be expressed as a single string containing the longitude-like and
latitude-like values and optionally a reference frame value, eg "J2000 14:20:20.5s -30.45.25.4".The center parameter can
be specified in the same way. The length parameter may be specified as a single numerical value, in which case it is
interpreted as the length in pixels, or a valid quantity, in which case it must have units conformant with the
direction axes units. The pa (position angle) parameter must be specified as a valid quantity with angular units.
The position angle is interpreted in the usual astronomical sense; eg measured from north through east in an equatorial
coordinate system. The slice in this case starts at the specified position angle and ends on the opposite side of
the specified center. Thus pa="45deg" means start at a point at a pa of 45 degrees relative to the specified center and
end at a point at a pa of 215 degrees relative to the center. Either start/end or center/pa/length must be specified;
if a parameter from one of these sets is specified, a parameter from the other set may not be specified. In either
case, the end points of the segment must fail within the input image, and they both must be at least 2 pixels from the
edge of the input image to facilite rotation (see below).

One may specify a width, which represents the number of pixels centered along and perpendicular
to the direction slice that are used for averaging along the slice. The width may be specified as an integer, in which
case it must be positive and odd. Alternatively, it may be specified as a valid quantity string (eg, "4arcsec") or
quantity record (eg qa.quantity("4arcsec"). In this case, units must be conformant to the direction axes units (usually
angular units) and the specified quantity will be rounded up, if necessary, to the next highest equivalent odd integer number
of pixels. The default value of 1 represents no averaging.
A value of 3 means average one pixel on each side of the slice and the pixel on the slice. 
Note that this width is applied to pixels in the image after it has been rotated (see below for a description
of the algorithm used).
 
One may specify the unit for the angular offset axis.
        
Internally, the image is first rotated, padding if necessary to include relevant pixels that would otherwise
be excluded by the rotation operation, so that the slice is horizontal, with the starting pixel left of the
ending pixel. Then, the pixels within the specified width of the slice are averaged and the resulting image is
written and/or returned. The output image has a linear coordinate in place of the direction coordinate of the
input image, and the corresponding axis represents angular offset with the center pixel having a value of 0.
        
The equivalent coordinate system, with a (usually) rotated direction coordinate (eg, RA and Dec) is written
to the output image as a table record. It can be retrieved using the table tool as shown in the example below.
        
# create a pv image with the position axis running from ra, dec pixel positions of [45, 50] to [100, 120]
# in the input image
impv(imagename="my_spectral_cube.im", outfile="mypv.im", start=[45,50], end=[100,120])
# analyze the pv image, such as get statistics
pvstats = imstat("mypv.im")
#
# get the alternate coordinate system information
tb.open("mypv.im")
alternate_csys_record = tb.getkeyword("misc")["secondary_coordinates"]
tb.done()
    
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['mode'] = mode
        mytmp['start'] = start
        mytmp['end'] = end
        mytmp['center'] = center
        mytmp['length'] = length
        mytmp['pa'] = pa
        mytmp['width'] = width
        mytmp['unit'] = unit
        mytmp['overwrite'] = overwrite
        mytmp['region'] = region
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['stretch'] = stretch
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'impv.xml')

        casalog.origin('impv')
        if trec.has_key('impv') and casac.utils().verify(mytmp, trec['impv']) :
            result = task_impv.impv(imagename, outfile, mode, start, end, center, length, pa, width, unit, overwrite, region, chans, stokes, mask, stretch)

        else :
          result = False
        return result
