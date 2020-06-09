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
import task_specflux
def specflux(imagename='', region='', box='', chans='', stokes='', mask='', stretch=False, function='flux density', unit='km/s', major='', minor='', logfile='', overwrite=False):

        """Report spectral profile and calculate spectral flux over a user specified region
PARAMETER SUMMARY
imagename        Name of the input (CASA, FITS, MIRIAD) image
region           Region selection. Default is to use
                 the full image.
box              Rectangular region to select in direction plane.
                 for details. Default is to use the entire direction plane.
chans            Channels to use. Default is to use
                 all channels.
stokes           Stokes planes to use. Default is to use
                 all Stokes planes.
mask             Mask to use. Default is none.
stretch          Stretch the input mask if necessary and possible. Only used if a mask is specified.

function         Aggregate function to use for computing per channel values. Supported values are
                 "flux density", "mean", "median", "sum". Minimal match supported.
unit             Unit to use for the spectral flux calculation. Must be conformant with a typical
                 spectral axis unit (ie something conformant with a velocity, frequency, or length).
                 Velocity units may only be used if the spectral coordinate has a rest frequency and
                 if it is > 0.
major            Major axis of overriding restoring beam. If specified, must be a valid quantity
                 If specified, minor must also be specified. The overriding beam is used for computing
                 flux and flux density values. Ignored if the image brightness units do not contain
                 "/beam". Example "4arcsec".
minor            Minor axis of overriding restoring beam. If specified, must be a valid quantity.
                 If specified, major must also be specified. See help on parameter major for details.
                 Example: "3arcsec".
logfile          Name of file to which to write tabular output. Default is to not write to a file.
overwrite        Controls if an already existing log file by the
                 same name can be overwritten. If true, the user is not prompted, the file
                 if it exists is automatically overwritten.

This application retrieves details of an image spectrum which has been integrated over a specified
region (or the entire image if no region has been specified).

One may specify which function to use to aggregate pixel values using the function parameter. Supported
values are "flux density", "mean", "median", and "sum". Minimal match is supported.

The spectral flux is reported in units flux density consistent with the image brightness unit times the
specified spectral unit (eg, Jy*km/s, K*arcsec2*km/s). If the units are K*arcsec2..., multiply the
reported value by 2.3504430539098e-8*d*d, where d is the distance in pc, to convert to units of K*pc2...
If provided, major and minor will be used to compute the beam size, and hence the per channel flux
densities (if function="flux density"), overriding the input image beam information, if present.

# write spectrum to file that has been integrated over
# rectangular region, using only pixels with non-negative values.
# if the log file already exists, overwrite it with the new data.
specflux(imagename="my.im", box="10,10,45,50", mask="my.im>=0", unit="km/s", logfile="my.log", overwrite=True)

# Extract the spectral profile using "sum" as the aggregate function from a cube over a given region:
specflux(imagename="myimage.image", box="10,10,45,50", mask="my.im>=0", function="sum", unit="km/s", logfile="profile.log", overwrite=True)

# Calculate the integrated line flux over a given region and channel range
# (this value will be reported as "Total Flux" in the output of specflux)
specflux(imagename="myimage.image", region="myregion.crtf", chans="14~25", unit="km/s", logfile="integrated_line_flux.log", overwrite=True)


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['stretch'] = stretch
        mytmp['function'] = function
        mytmp['unit'] = unit
        mytmp['major'] = major
        mytmp['minor'] = minor
        mytmp['logfile'] = logfile
        mytmp['overwrite'] = overwrite
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'specflux.xml')

        casalog.origin('specflux')
        if trec.has_key('specflux') and casac.utils().verify(mytmp, trec['specflux']) :
            result = task_specflux.specflux(imagename, region, box, chans, stokes, mask, stretch, function, unit, major, minor, logfile, overwrite)

        else :
          result = False
        return result
