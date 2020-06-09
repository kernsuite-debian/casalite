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
import task_spxfit
def spxfit(imagename='', box='', region='', chans='', stokes='', axis=-1, mask='', minpts=1, multifit=False, spxtype='plp', spxest=[], spxfix=[], div=0, spxsol='', spxerr='', model='', residual='', wantreturn=True, stretch=False, logresults=True, logfile='', append=True, sigma='', outsigma=''):

        """Fit a 1-dimensional model(s) to an image(s) or region for determination of spectral index.

This task fits a power logarithmic polynomial or a logarithmic tranformed polynomial to one dimensional profiles for determination of spectral indices.

PARAMETER SUMMARY
imagename       Name of the input image(s). More than one image name can be given as an
                array, in which case the images are concatenated along the specified axis
                and the resultant image is what is used by the fitter. In this case,
                all images must have the same dimensions along all axes other than the fit axis.
box             Rectangular region to select in direction plane.
                Default is to use the entire direction plane.
region          Region selection. Default is to use the full image.
chans           Channels to use. Default is to use all channels.
stokes          Stokes planes to use. Default is to use all Stokes planes.
axis            Axis along which to do the fit(s). <0 means use the spectral axis or the
                zeroth axis if a spectral axis is not present.
mask            Mask to use. Default is none.
stretch         Stretch the input mask if necessary and possible? Only used if a mask is specified.

minpts          Minimum number of points necessary to attempt a fit.
multifit        Fit models at each pixel in region (true) or average profiles and fit a single model (false).
spxtype         Type of function to fit. "plp" => power logarithmic polynomial, "ltp" => logarithmic
                transformed polynomial.
spxest          REQUIRED. Initial estimates as array of numerical values for the spectral index
                function coefficients. eg [1.5, -0.8] if fitting a plp function thought to be close to
                1.5*(x/div)**(-0.8), or [0.4055, -0.8] if fitting an lpt function thought to be close to
                ln(1.5) - 0.8*ln(x/div).
spxfix          Fix the corresponding spx function coefficients during the fit. True=>hold fixed
div             Divisor (numerical value or quantity) to use in the logarithmic terms of the plp or ltp
                function. 0 => calculate a useful value on the fly.
spxsol          Name of the function coeffecients solution image to write.
spxerr          Name of the function coeffecients error image to write.
model           Name of model image to write.
residual        Name of residual image to write.
wantreturn      If true, return a record summarizing the fit results, if false, return false.
stretch         Stretch the mask if necessary and possible?
logresults      Output results to logger?
logfile         File in which to log results. Default is not to write a logfile.
append          Append results to logfile? Logfile must be specified. Default is to append. False means overwrite existing file if it exists.
sigma           Standard deviation numerical array, image name (string), or string array of names of images which will be
                concatenated to create the sigma image that is used by the fitter.
outsigma        Name of output image used for standard deviation. Ignored if sigma is empty.

This application performs a non-linear, least squares fits using the Levenberg-Marquardt algorithm of either a power logarithmic polynomial or a
logarithmic tranformed polynomial to pixel values along a specified axis of an image or images. A description of the fitting algorithm may be found
in AIPS++ Note 224 (http://www.astron.nl/casacore/trunk/casacore/doc/notes/224.html) and in Numerical Recipes by W.H. Press et al., Cambridge
University Press. These functions are most often used for fitting the spectral index and higher order terms of a spectrum. A power logarithmic
polynomial (plp) has the form

y = c0*(x/div)**(c1 + c2*ln(x/div) + c3*ln(x/div)**2 + ... + cn*ln(x/div)**(n - 1))

and a logarithmic transformed polynomial (ltp) is simply the result of this equation after taking the natural log of both sides so that it has the form

ln(y) = c0 + c1*ln(x/div) + c2*ln(x/div)**2 +  ... + cn*ln(x/div)**n

Because the logarithm of the ordinate values must be taken before fitting a logarithmic transformed polynomial,
all non-positive pixel values are effectively masked for the purposes of fitting.

The coefficients of the two forms are equal to each other except that c0 in the second equation is equal to
ln(c0) of the first. In the case of fitting a spectral index, which is traditionally represented as alpha, is
equal to c1.

In both cases, div is a numerical value used to scale abscissa values so they are closer to unity when they are sent to the fitter. This generally
improves the probability that the fit will converge. This parameter may be specified via the div parameter. A value of 0
(the default) indicates that the application should determine a reasonable value for div, which is determined via

div = 10**int(log10(sqrt(min(x)*max(x))))

where min(x) and max(x) are the minimum and maximum abscissa values, respectively.

So, for example, if S(nu) is proportional to nu**alpha and you expect alpha to be near -0.8 and the value of S(nu) is 1.5 at
1e9 Hz and your image(s) have spectral units of Hz, you would specify spxest=[1.5, -0.8] and div=1e9 when fitting a plp function,
or spxest=[0.405, -0.8] and div=1e9 if fitting an ltp function close to ln(1.5) - 0.8*ln(x/div).


A CAUTIONARY NOTE
Note that the likelihood of getting a reliable solution increases with the number of good data points as well as the goodness
of the initial estimate. It is possible that the first solution found might not be the best one, and
so, if a solution is found, it is recommended that the fit be repeated using the solution of the previous fit as the
initial estimatE for the new fit. This process should be repeated until the solutions from one fit to the next differ only insignificantly.
The convergent solution is very likely the best solution.

AXIS
The axis parameter indicates on which axis profiles should be fit; a value <0 indicates the spectral axis should be used,
or if one does not exist, that the zeroth axis should be used.

MINIMUM NUMBER OF PIXELS
The minpts parameter indicates the minimum number of unmasked pixels that must be present in order for a fit
to be attempted. When multifit=T, positions with too few good points will be masked in any output images.

ONE FIT OF REGION AVERAGE OR PIXEL BY PIXEL FIT
The multifit parameter indicates if profiles should be fit at each pixel in the selected region (true), or if the profiles in that region should be
averaged and the fit done to that average profile (false).

FUNCTION TYPE
Which function to fit is specified in the spxtype parameter. Only two values (case insensitive) are supported. A value of
"plp" indicates that a power logarithmic polynomial should be fit. A value of "ltp" indicates a logarithmic transformed
polynomial should be fit.

INCLUDING STANDARD DEVIATIONS OF PIXEL VALUES
If the standard deviations of the pixel values in the input image are known and they vary in the image (eg they are higher for pixels
near the edge of the band), they can be included in the sigma parameter. This parameter takes either an array or an image name. The
array or image must have one of three shapes: 1. the shape of the input image, 2. the same dimensions as the input image with the lengths
of all axes being one except for the fit axis which must have length corresponding to its length in the input image, or 3. be one
dimensional with lenght equal the the length of the fit axis in the input image. In cases 2 and 3, the array or pixels in sigma will
be replicated such that the image that is ultimately used is the same shape as the input image. The values of sigma must be non-negative.
It is only the relative values that are important. A value of 0 means that pixel should not be used in the fit. Other than that, if pixel
A has a higher standard deviation than pixel B, then pixel A is noisier than pixel B and will receive a lower weight when the fit is done.
The weight of a pixel is the usual

weight = 1/(sigma*sigma)

In the case of multifit=F, the sigma values at each pixel along the fit axis in the hyperplane perpendicular to the fit axis which includes
that pixel are averaged and the resultant averaged standard deviation spectrum is the one used in the fit. Internally, sigma values are normalized
such that the maximum value is 1. This mitigates a known overflow issue.

One can write the normalized standard deviation image used in the fit by specifying its name in outsigma. This image can then be
used as sigma for subsequent runs.

RETURNED DICTIONARY STRUCTURE
The returned dictionary has a (necessarily) complex structure. First, there are keys "xUnit" and "yUnit" whose values are
the abscissa unit and the ordinate unit described by simple strings. Next there are arrays giving a broad overview of the
fit quality. These arrays have the shape of the specified region collapsed along the fit axis with the axis corresponding to the fit
axis having length of 1:

attempted: a boolean array indicating which fits were attempted (eg if too few unmasked points, a fit will not be attempted).
converged: a boolean array indicating which fits converged. False if the fit was not attempted.
valid:     a boolean array indicating which solutions fall within the specified valid ranges of parameter space. Any solution for
           which a value or error is NaN is automatically marked as invalid.
niter:     an int array indicating the number of iterations for each profile, <0 if the fit did not converge
direction: a string array containing the world direction coordinate for each profile

There is a "type" array having number of dimensions equal to the number of dimensions in the above arrays plus one. The shape of
the first n-1 dimensions is the same as the shape of the above arrays. The length of the last dimension is equal to the number of
components fit. The values of this array are all "POWER LOGARITHMIC POLYNOMIAL" or "LOGARITHMIC TRANSFORMED POLYNOMIAL", depending
on which type function was fit.

There will be a subdictionary accessible via the "plp" or "ltp" key (depending on which type of function was fit) which will have
subkeys "solution" and "error" which will each have an array of values. Each of these arrays will have one more dimension than the overview arrays
described above. The shape of the first n-1 dimensions will be the same as the shape of the overview arrays described above, while the
final dimension will have length equal to the number of parameters that were fit. Along this axis will be the
corresponding fit result or associated error (depending on the array's associated key) of the fit. In cases where
the fit was not attempted or did not converge, a value of NAN will be present.

OUTPUT IMAGES
In addition to the returned dictionary, optionally one or more of any combination of output images can be written.
The model and residual parameters indicate the names of the model and residual images to be written; empty values inidcate that these images
should not be written.

The parameters spxsol and spxerr are the names of the solution and error images to write, respectively. In cases
where more than one coefficient are fit, the image names will be appended with an underscore followed by the relevant
coefficient number ("_0", "_1", etc). These images contain the arrays for the associated parameter solutions or errors
described in previous sections. Pixels for which fits were not attempted, did not converge, or converged but have values
of NaN (not a number) or INF (infinity) will be masked as bad.

LPT vs PLP
Ultimately, the choice of which functional form to use in determining the spectral index is up to the user and should be based
on the scientific goals. However, below is a summary of one user's experience and preferences as an example:

If the weights are known or can be determined from the images (eg. the source-free image rms and a fractional calibration error) then I
favor a weighted fit using the non-linear (power-law) model. An unweighted fit using the non-linear model will, in general, give far
too much leverage to large flux values.

If the weights are unknown or will not be considered by the fitting algorithm, then I prefer the log-transformed polynomial model. However,
this does not work well in low signal-to-noise regions. A conservative mask could be created such that only high s/n areas are fit,
but this could hinder many science objectives.

EXAMPLES

res = spxfit(imagename=["im0.im","im1.im"], multifit=true, spxtype="plp", spxest=[0.5,2,0.1], div="1GHz", spxsol="myplpsolutions.im")


        """
        if type(spxest)==float: spxest=[spxest]
        if type(spxfix)==bool: spxfix=[spxfix]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['box'] = box
        mytmp['region'] = region
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['axis'] = axis
        mytmp['mask'] = mask
        mytmp['minpts'] = minpts
        mytmp['multifit'] = multifit
        mytmp['spxtype'] = spxtype
        mytmp['spxest'] = spxest
        mytmp['spxfix'] = spxfix
        mytmp['div'] = div
        mytmp['spxsol'] = spxsol
        mytmp['spxerr'] = spxerr
        mytmp['model'] = model
        mytmp['residual'] = residual
        mytmp['wantreturn'] = wantreturn
        mytmp['stretch'] = stretch
        mytmp['logresults'] = logresults
        mytmp['logfile'] = logfile
        mytmp['append'] = append
        mytmp['sigma'] = sigma
        mytmp['outsigma'] = outsigma
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'spxfit.xml')

        casalog.origin('spxfit')
        if trec.has_key('spxfit') and casac.utils().verify(mytmp, trec['spxfit']) :
            result = task_spxfit.spxfit(imagename, box, region, chans, stokes, axis, mask, minpts, multifit, spxtype, spxest, spxfix, div, spxsol, spxerr, model, residual, wantreturn, stretch, logresults, logfile, append, sigma, outsigma)

        else :
          result = False
        return result