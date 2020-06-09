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
import task_rmfit
def rmfit(imagename='', rm='', rmerr='', pa0='', pa0err='', nturns='', chisq='', sigma=-1, rmfg=0.0, rmmax=0.0, maxpaerr=1e30):

        """Calculate rotation measure.
PARAMETER SUMMARY
imagename        Name(s) of the input image(s).
rm               Output rotation measure image name. If not specified, no image is written.
rmerr            Output rotation measure error image name. If not specified, no image is written.
pa0              Output position angle (degrees) at zero wavelength image name. If not specified, no image is written.
pa0err           Output position angle (degrees) at zero wavelength error image name. If not specified, no image is written.
nturns           Output number of turns image name. If not specified, no image is written.
chisq            Output reduced chi squared image name. If not specified, no image is written.
sigma            Estimate of the thermal noise.  A value less than 0 means auto estimate.
rmfg             Foreground rotation measure in rad/m/m to subtract.
rmmax            Maximum rotation measure in rad/m/m for which to solve. IMPORTANT TO SPECIFY.

This task generates the rotation measure image from stokes Q and U  measurements at several
different frequencies.  You are required to specify the name of at least one image with a polarization
axis containing stokes Q and U planes and with a frequency axis containing more than two pixels. The
frequencies do not have to be equally spaced (ie the frequency coordinate can be a tabular coordinate).
It will work out the position angle images for you. You may also specify multiple image names, in which
case these images will first be concatenated along the spectral axis using ia.imageconcat(). The requirments
are that for all images, the axis order must be the same and the number of pixels along each axis must
be identical, except for the spectral axis which may differ in length between images. The spectral axis need
not be contiguous from one image to another.

See also the fourierrotationmeasure 
function for a new Fourier-based approach.

Rotation measure algorithms that work robustly are few.  The main
problem is in trying to account for the $n- \pi$ ambiguity (see Leahy et
al, Astronomy \& Astrophysics, 156, 234 or Killeen et al;
http://www.atnf.csiro.au/\verb+~+nkilleen/rm.ps). 

The algorithm that this task uses is that of Leahy et al. in see
Appendix A.1.  But as in all these algorithms, the basic process is that
for each spatial pixel, the position angle vs frequency data is fit to
determine the rotation measure and the position angle at zero wavelength
(and associated errors).   An image containing the number of $n- \pi$ turns
that were added to the data at each spatial pixel and for which the best fit
was found can be written. The reduced chi-squared image for the fits can
also be written.

Note that no assessment of curvature (i.e. deviation
from the simple linear position angle - $\lambda^2$ functional form)
is made.  

Any combination of output images can be written.

The parameter sigma gives the thermal noise in Stokes Q and U.
By default it is determined automatically using the image data.  But if it
proves to be inaccurate (maybe not many signal-free pixels), it may be
specified. This is used for calculating the error in the position angles (via 
propagation of Gaussian errors).

The argument maxpaerr specifies the maximum allowable error in
the position angle that is acceptable.  The default is an infinite
value.  From the standard propagation of errors, the error in the
linearly polarized position angle is determined from the Stokes Q and
U images (at each directional pixel for each frequency). If the position angle
error for any pixel exceeds the specified value, the position angle at that pixel
is omitted from the fit. The process generates an error for the
fit and this is used to compute the errors in the output
images.  

Note that maxpaerr is not used to mask pixels in the output images.

The argument rmfg is used to specify a foreground RM value.  For
example, you may know the mean RM in some direction out of the Galaxy,
then including this can improve the algorithm by reducing ambiguity.

The parameter rmmax specifies the maximum absolute RM value that
should be solved for.  This quite an important parameter.  If you leave
it at the default, zero, no ambiguity handling will be
used.  So some apriori information should be supplied; this
is the basic problem with rotation measure algorithms.

EXAMPLES

# Calculate the rotation measure for a single polarization image
rmfit(imagename="mypol.im", rm="myrm.im", rmmax=50.0)

# calculate the rotation measure using a set of polarization images from
# different spectral windows or bands.

rmfit(imagename=["pol1.im", "pol2.im", "pol3.im", rm="myrm2.im", rmmax=50.0)


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['rm'] = rm
        mytmp['rmerr'] = rmerr
        mytmp['pa0'] = pa0
        mytmp['pa0err'] = pa0err
        mytmp['nturns'] = nturns
        mytmp['chisq'] = chisq
        mytmp['sigma'] = sigma
        mytmp['rmfg'] = rmfg
        mytmp['rmmax'] = rmmax
        mytmp['maxpaerr'] = maxpaerr
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'rmfit.xml')

        casalog.origin('rmfit')
        if trec.has_key('rmfit') and casac.utils().verify(mytmp, trec['rmfit']) :
            result = task_rmfit.rmfit(imagename, rm, rmerr, pa0, pa0err, nturns, chisq, sigma, rmfg, rmmax, maxpaerr)

        else :
          result = False
        return result
