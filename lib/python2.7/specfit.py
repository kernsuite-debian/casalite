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
import task_specfit
def specfit(imagename='', box='', region='', chans='', stokes='', axis=-1, mask='', ngauss=1, poly=-1, estimates='', minpts=1, multifit=False, model='', residual='', amp='', amperr='', center='', centererr='', fwhm='', fwhmerr='', integral='', integralerr='', wantreturn=True, stretch=False, logresults=True, pampest=[], pcenterest=[], pfwhmest=[], pfix=[], gmncomps=0, gmampcon=[], gmcentercon=[], gmfwhmcon=[], gmampest=[0.0], gmcenterest=[0.0], gmfwhmest=[0.0], gmfix='', logfile='', append=True, pfunc='', goodamprange=[0.0], goodcenterrange=[0.0], goodfwhmrange=[0.0], sigma='', outsigma=''):

        """Fit 1-dimensional gaussians and/or polynomial models to an image or image region

This task simultaneously fits one or more gaussian singlets lorentzian singlets, gaussian multiplets, and/or a polynomial to one dimensional profiles.

PARAMETER SUMMARY
imagename       Name of the input (CASA, FITS, MIRIAD) image
box             Rectangular region to select in direction plane.
                for details. Default is to use the entire direction plane.
region          Region selection. Default is to use the
                full image.
chans           Channels to use. Default is to use
                all channels.
stokes          Stokes planes to use. Default is
                to use all Stokes planes.
axis            Axis along which to do the fit(s). <0 means use the spectral axis or the
                zeroth axis if a spectral axis is not present.
mask            Mask to use. Default is none.
stretch         Stretch the input mask if necessary and possible? Only used if a mask is specified.

ngauss          Maximum number of gaussians to fit.
poly            Order of polynomial to fit. <0 means do not fit a polynomial.
estimates       Name of file containing initial gaussian estimates.
minpts          Minimum number of points necessary to attempt a fit.
multifit        Fit models at each pixel in region (true) or average profiles and fit a single model (false).
model           Name of model image to write.
residual        Name of residual image to write.
amp             Name of amplitude solution image. Default: do not write the image ("")
amperr          Name of amplitude solution error image. Default: do not write the image ("")
center          Name of center solution image. Default: do not write the image ("")
centererr       Name of center solution error image. Default: do not write the image ("")
fwhm            Name of fwhm solution image. Default: do not write the image ("")
fwhmerr         Name of fwhm solution error image. Default: do not write the image ("")
integral        Name of integral solution image. Default: do not write the image ("")
integralerr     Name of integral solution error image. Default: do not write the image ("")
wantreturn      If true, return a record summarizing the fit results, if false, return false.
stretch         Stretch the mask if necessary and possible?
logresults      Output results to logger?
pampest         Initial estimate of PCF profile (gaussian or lorentzian) amplitudes.
pcenterest      Initial estimate PCF profile centers, in pixels.
pfwhmest        Initial estimate PCF profile FWHMs, in pixels.
pfix            PCF profile parameters to fix during fit.
pfunc           PCF singlet functions to fit. "gaussian" or "lorentzian" (minimal match supported). Unspecified means all gaussians.
gmncomps        Number of components in each Gaussian multiplet to fit.
gmampcon        The amplitude ratio constraints for non-reference components to reference component in gaussian multiplets.
gmcentercon     The center offset constraints (in pixels) for non-reference components to reference component in gaussian multiplets.
gmfwhmcon       The FWHM  ratio constraints for non-reference components to reference component in gaussian multiplets.
gmampest        Initial estimate of individual gaussian amplitudes in gaussian multiplets.
gmcenterest     Initial estimate of individual gaussian centers in gaussian multiplets, in pixels.
gmfwhmest       Initial estimate of individual gaussian FWHMss in gaussian multiplets, in pixels.
gmfix           Parameters of individual gaussians in gaussian multiplets to fix during fit.
logfile         File in which to log results. Default is not to write a logfile.
append          Append results to logfile? Logfile must be specified. Default is to append. False means overwrite existing file if it exists.
goodamprange    Acceptable amplitude solution range. 0 => all amplitude solutions are acceptable. [0.0] => All amplitude solutions are acceptable.
goodcenterrange Acceptable center solution range in pixels relative to region start. [0.0] => all center solutions are acceptable.
goodfwhmrange   Acceptable FWHM solution range in pixels. [0.0] => all FWHM solutions are acceptable.
sigma           Standard deviation array or image name.
outsigma        Name of output image used for standard deviation. Ignored if sigma is empty.

This task simultaneously performs a non-linear, least squares fit using the Levenberg-Marquardt algorithm of one or more gaussian singlets,
one or more lorentzian singlets, one or more gaussian multiplets, and/or a polynomial to one dimensional profiles. A description of the
fitting algorithm may be found in AIPS++ Note 224 (http://www.astron.nl/casacore/trunk/casacore/doc/notes/224.html) and in Numerical Recipes
by W.H. Press et al., Cambridge University Press. A gaussian/lorentzian singlet is a gaussian/lorentzian whose parameters (amplitude,
center position, and width) are all independent from any other feature that may be simultaneously fit. A gaussian multiplet is a set of two or
more gaussian lines in which at least one (and possibly two or three) parameter of each line is dependent on the parameter of another,
single (reference) profile in the multiplet. For example, one can specify a doublet in which the amplitude of the first line is 0.6 times the
amplitude of the zeroth line and/or the center of the first line is 20 pixels from the center of the zeroth line, and/or the fwhm of the first
line is identical (in pixels) to that of the zeroth line. There is no limit to the number of components one can specify in a multiplet
(except of course that the number of parameters to be fit should be significantly less than the number of data points), but there can be only
a single reference profile in a multiplet to which to tie constraints of parameters of the other profiles in the set.

AXIS
The axis parameter indicates on which axis profiles should be fit; a value <0 indicates the spectral axis should be used, or if one does not exist,
that the zeroth axis should be used.

MINIMUM NUMBER OF PIXELS
The minpts parameter indicates the minimum number of unmasked pixels that must be present in order for a fit
to be attempted. When multifit=T, positions with too few good points will be masked in any output images.

ONE FIT OF REGION AVERAGE OR PIXEL BY PIXEL FIT
The multifit parameter indicates if profiles should be fit at each pixel in the selected region (true), or if the profiles in that region should be
averaged and the fit done to that average profile (false).

POLYNOMIAL FITTING
The order of the polynomial to fit is specified only via the poly parameter. If poly<0, no polynomial will be fit. No initial estimates of
coefficients can be specified; these are determined automatically.

GAUSSIAN SINGLET FITTING
In the absence of an estimates file and no estimates being specified by the p*est parameters, and gmncomps=0 or is empty, the ngauss parameter
indicates the maximum number of gaussian singlets that should be fit. The initial estimates of the parameters for these gaussians will be attempted
automatically in this case. If it deems appropriate, the fitter will fit fewer than this number. In the case where an estimates file is supplied,
ngauss is ignored (see below). ngauss is also ignored if the p*est parameters are specified or if gmncomps is not an empty array or, if an integer,
is greater than zero. If estimates is not specified or the p*est parameters are not specified and ngauss=0, gmncomps is empty or 0, and poly<0,
an error will occur as this indicates there is nothing to fit.

One can specify initial estimates of gaussian singlet parameters via an estimates file or the pampest, pcenterest, pfwhmest, and optionally, the
pfix parameters. The latter is the recommended way to specify these estimates as support for estimates files may be deprecated in the future. No matter
which option is used, an amplitude initial estimate must always be nonzero.  A negative fwhm estimate will be silently changed to positve.

SPECIFYING INITIAL ESTIMATES FOR GAUSSIAN AND LORENTZIAN SINGLETS (RECOMMENDED METHOD)
One may specify initial estimates via the pampest, pcenterest, and pfwhmest parameters. In the case of a single gaussian or lorentzian singlet,
these parameters can be numbers. pampest must be specified in image brightness units, pcenterest must be given in the number of pixels from the
zeroth pixel, and pfwhmest must be given in pixels. Optionally pfix can be specified and in the case of a single gaussian or lorentzian singlet
can be a string. In it is coded which parameters should be held constant during the fix. Any combination of "p" (amplitude), "c" (center), or "f"
(fwhm) is allowed; eg pfix="pc" means fix both the amplitude and center during the fit. In the case of more than one gaussian and/or lorentzian
singlets, these parameters must be specified as arrays of numbers. The length of the arrays indicates the number of singlets to fit and must be
the same for all the p*est parameters.

If no parameters are to be fixed for any of the singlets, pfix can be set to the empty string. However, if at least one parameter of one singlet
is to be fixed, pfix must be an array of strings and have a length equal to the p*est arrays. Singlets which are not to have any parameters fixed
should be represented as an empty string in the pfix array. So, for example, if one desires to fit three singlets and fix the fwhm of the middle
one, one must specify pfix=["", "f", ""], the empty strings indicating no parameters of the zeroth and second singlet should be held constant.

In the case of multifit=True, the initial estimates, whether from the p*est parameters or from a file (see below), will be applied to the location
of the first fit. This is normally the bottom left corner of the region selected. If masked, not enough good points to perform a fit, or the
attempted fit fails, the fitting proceeds to the next pixel with the pixel value of the lowest numbered axis changing the fastest. Once a
successful fit has been performed, subsequent fits will use the results of a fit for a nearest pixel for which a previous fit was successful as the
initial estimate for the parameters at the current location. The fixed parameter string will be honored for every fit performed when multifit=True.

One specifies what type of PCF profile to fit via the pfunc parameter. A PCF function is one that can be parameterized by a peak, center, and FWHM,
as both gaussian and lorentzian singlets can. If all singlets to be fit are gaussians, one can set pfunc equal to the empty string and all snglets
will be assumed to be gaussians. If at least one lorentzian is to be fit, pfunc must be specified as a string (in the case of a single singlet) or
an array of strings (in the case of multiple singlets). The position of each string corresponds to the positions of the initial estimates in the
p*est and pfix arrays. Minimal match ("g", "G", "l", or "L") is supported. So, if one wanted to simultaneously fit two gaussian and two lorentzian
singlets, the zeroth and last of which were lorentzians, one would specify pfunc=["L", "G", "G", "L"].

ESTIMATES FILE FOR GAUSSIAN SINGLETS (NONRECOMMENDED METHOD)
Initial estimates for gaussian singlets can be specified in an estimates file. Estimates files may be deprecated in the future in favor of the
p*est parameters, so it is recommended users use those parameters instead. If an estimates file is desired to be used, the p*est parameters
must be 0 or empty and mgncomps must be 0 or empty. Only gaussian singlets can be specified in an estimates file. If one desires to fit one or
more gaussian multiplets and/or one or more lorentzian singlets simultaneously, the p*est parameters must be used to specify the initial parameters
of all gaussian singlets to fit; one cannot use an estimates file in this case. If an estimates file is specified, a polynomial
can be fit simultaneously by specifying the poly parameter. The estimates file must contain initial estimates of parameters
for all gaussian singlets to be fit. The number of gaussian singlets to fit is gotten from the number of estimates in the file. The file can contain
comments which are indicated by a "#" at the beginning of a line. All non-comment lines will be interpreted as initial estimates. The
format of such a line is

[peak intensity], [center], [fwhm], [optional fixed parameter string]

The first three values are required and must be numerical values. The peak intensity must be expressed in image brightness units, while the
center must be specified in pixels offset from the zeroth pixel, and fwhm must be specified in pixels. The fourth value is optional and if present,
represents the parameter(s) that should be held constant during the fit. Any combination of the characters 'p' (peak), 'c' (center), and 'f' (fwhm) are
permitted, eg "fc" means hold the fwhm and the center constant during the fit. Fixed parameters will have no error associated with them. Here is an
example file:

# estimates file indicating that two gaussians should be fit
# first guassian estimate, peak=40, center at pixel number 10.5, fwhm = 5.8 pixels, all parameters allowed to vary during
# fit
40, 10.5, 5.8
# second gaussian, peak = 4, center at pixel number 90.2, fwhm = 7.2 pixels, hold fwhm constant
4, 90.2, 7.2, f
# end file

GAUSSIAN MULTIPLET FITTING
Any number of gaussian multiplets, each containing any number of two or more components, can be simultaneously fit, optionally with a
polynomial and/or any number of gaussian and/or lorentzian singlets, the only caveat being that the number of parameters to be fit should be
significantly less than the number of data points. The gmncomps parameter indicates the number of multiplets to fit and the number of
components in each multiplet. In the case of a single multiplet, an integer (>1) can be specified. For example, mgncomps=4 means fit a
single quadruplet of gaussians. In the case of 2 or more multiplets, and array of integers (all >1) must be specified. For example,
gmncomps=[2, 4, 3] means 3 seperate multiples are to be fit, the zeroth being a doublet, the first being a quadruplet, and the second
being a triplet.

Initial estimates of all gaussians in all multiplets are specified via the gm*est parameters which must be arrays of numbers. The order
starts with the zeroth component of the zeroth multiplet to the last component of the zeroth multiplet, then the zeroth component of
the first multiplet to the last compoenent of the first multiplet, etc to the zeroth component of the last multiplet to the last
element of the last multiplet. The zeroth element of a multiplet is defined as the reference component of that multiplet and has the special
significance that it is the profile to which all constraints of all other profiles in that multiplet are referenced (see below). So,
in our example of gmncomps=[2, 4, 3], gmampest, gmcenterest, and gmfwhmest must each be nine (the total number of individual gaussian
profiles summed over all multiplets) element arrays. The zeroth, second, and sixth elements represent parameters of the reference profiles
in the zeroth, first, and second multiplet, respectively.

The fixed relationships between the non-reference profile(s) and the reference profile of a multiplet are specified via the gmampcon,
gmcentercon, and gmfwhmcon parameters. At least one, and any combination, of constraints can be specified for any non-reference
component of a multiplet. The amplitude ratio of a non-reference line to that of the reference line is set in gmampcon. The ratio of
the fwhm of a non-reference line to that of the reference line is set in gmfwhmcon. The offset in pixels of the center position of
a non-reference line to that of the reference line is set in gmcentercon. In the case where a parameter is not constrained for any
non-reference line of any multiplet, the value of the associated parameter must be 0. In the case of
a single doublet, a constraint may be specified as a number or an array of a single number. For example, mgncomps=2 and gmampcon=0.65
and gmcentercon=[32.4] means there is a single doublet to fit where the amplitude ratio of the first to the zeroth line is constained
to be 0.65 and the center of the first line is constrained to be offset by 32.4 pixels from the center of the zeroth line. In cases
of a total of three or more gaussians, the constraints parameters must be specified as arrays with lengths equal to the total number
of gaussians summed over all multiplets minus the number of reference lines (one per multiplet, or just number of multiplets, since
reference lines cannot be constrained by themselves). In the cases where an array must be specified but a component in that array
does not have that constraint, 0 should be specified. Here's an example

gmncomps=[2, 4, 3]
gmampcon=  [ 0  ,  0.2,  0  , 0.1,   4.5,   0  ]
gcentercon=[24.2, 45.6, 92.7, 0  , -22.8, -33.5]
gfwhmcon=""

In this case we have our previous example of one doublet, one quadruplet, and one triplet. The first component of the doublet has the constraint
that its center is offset by 24.2 pixels from the zeroth (reference) component. The first component of the quadruplet is constrained to have
an amplitude of 0.2 times that of the quadruplet's zeroth component and its center is constrained to be offset by 45.6 pixels from the
reference component. The second component of the quadruplet is constained to have its center offset by 92.7 pixels from the associated
reference component and the third component is constrained to have an amplitude of 0.1 times that of the associated reference component.
The first component of the triplet is constrained to have an amplitude of 4.5 times that of its associated reference component and its center
is constrained to be offset by -22.8 pixels from the reference component's center. The second component of the triplet is constrained to have
its center offset by -33.5 pixels from the center of the reference component. No lines have FWHM constraints, so the empty string can be given
for that parameter. Note that using 0 to indicate no constraint for line center means that one cannot specify a line centered at the same
position as the reference component but having a different FWHM from the reference component. If you must specify this very unusual case,
try using a very small positive (or even negative) value for the center constraint.

Note that when a parameter for a line is constrained, the corresponding value for that component in the corresponding gm*est array is
ignored and the value of the constrained parameter is automatically used instead. So let's say, for our example above, we had specified
the following estimates:

gmampest =     [ 1,   .2,  2,   .1,    .1,   .5,  3,    2, 5]
gmcenterest =  [20, 10  , 30, 45.2, 609  , -233, 30, -859, 1]

Before any fitting is done, the constraints would be taken into account and these arrays would be implicitly rewritten as:

gmampest =     [ 1,   .2,  2,   .4,    .1,   .2,  3, 13.5,  5  ]
gmcenterest =  [20, 44.2, 30, 75.6, 127.7, -233, 30,  7.2, -3.5]

The value of gmfwhmest would be unchanged since there are no FWHM constraints in this example.

In addition to be constrained by values of the reference component, parameters of individual components can be fixed. Fixed parameters
are specified via the gmfix parameter. If no parameters are to be fixed, gmfix can be specified as the empty string or a zero element
array. In the case where any parameter is to be fixed, gmfix must be specified as an array of strings with length equal to the total number of
components summed over all multiplets. These strings encode which parameters to be fixed for the corresponding components. If
a component is to have no parameters fixed, an empty string is used. In other cases one or more of any combination of parameters can
be fixed using "p", "c", and/or "f" described above for fixing singlet parameters. There are a couople of special cases
to be aware of. In the case where a non-reference component parameter is constrained and the corresponding reference component parameter is
set as fixed, that parameter in the non-reference parameter will automatically be fixed even if it was specified not to be fixed in
the gmfix array. This is the only way the constraint can be honored afterall. In the converse case of when a constrained parameter of a
non-reference component is specified as fixed, but the corresponding parameter in the reference component is not specified to be fixed,
an error will occur. Fixing an unconstrained parameter in a non-reference component is always legal as is fixing any combination of
parameters in a reference component (with the above caveat that corresponding constrained parameters in non-reference components will
be silently held fixed as well).

The same rules that apply to singlets when multifit=True apply to multiplets.

LIMITING RANGES FOR SOLUTION PARAMETERS
In cases of low (or no) signal to noise spectra, it is still possible for the fit to converge, but often to a
nonsensical solution. The astronomer can use her knowledge of the source to filter out obviously bogus solutions.
Any solution which contains a NaN value as a value or error in any one of its parameters is automatically marked as
invalid.

One can also limit the ranges of solution parameters to known "good" values via the goodamprange, goodcenterrange, and goodfwhmrange
parameters. Any combination can be specified and the limit constraints will be ANDed together. The ranges apply to all PCF components
that might be fit; choosing ranges on a component by component basis is not supported. If specified,
an array of exactly two numerical values must be given to indicate the range of acceptable solution values for
that parameter.  goodamprange is expressed in terms of image brightness units. goodcenterrange is expressed in terms of pixels
from the zeroth pixel in the specified region. goodfwhmrange is expressed in terms of pixels (only non-negative values should be
given for FWHM range endpoints). In the case of a multiple-PCF fit, if any of the corresponding solutions are outside the specified
ranges, the entire solution is considered to be invalid.

In addition, solutions for which the absolute value of the ratio of the amplitude error to the amplitude exceeds 100 or the
ratio of the FWHM error to the FWHM exceeds 100 are automatically marked as invalid.

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

One can write the normalized standard deviation image used in the fit but specifying its name in outsigma. This image can then be
used as sigma for subsequent runs.

RETURNED DICTIONARY STRUCTURE
The dictionary returned (if wantreturn=True) has a (necessarily) complex structure. First, there are keys "xUnit" and "yUnit" whose values are
the abscissa unit and the ordinate unit described by simple strings. Next there are arrays giving a broad overview of the
fit quality. These arrays have the shape of the specified region collapsed along the fit axis with the axis corresponding to the fit
axis having length of 1:

attempted: a boolean array indicating which fits were attempted (eg if too few unmasked points, a fit will not be attempted).
converged: a boolean array indicating which fits converged. False if the fit was not attempted.
valid:     a boolean array indicating which solutions fall within the specified valid ranges of parameter space  (see
           section LIMITING RANGES FOR SOLUTION PARAMETERS for details).
niter:     an int array indicating the number of iterations for each profile, <0 if the fit did not converge
ncomps:    the number of components (gaussian singlets + lorentzian singlets + gaussian multiplets + polynomial) fit for the profile,
           <0 if the fit did not converge
direction: a string array containing the world direction coordinate for each profile

There is a "type" array having number of dimensions equal to the number of dimensions in the above arrays plus one. The shape of
the first n-1 dimensions is the same as the shape of the above arrays. The length of the last dimension is equal to the number of
components fit. The values of this array are strings describing the components that were fit at each possition ("POLYNOMIAL",
"GAUSSIAN" in the case of gaussian singlets, "LORENTZIAN" in the case of lorentzian singlets, and ""GAUSSIAN MULTPLET").

If any gaussian singlets were fit, there will be a subdictionary accessible via the "gs" key which will have subkeys "amp", "ampErr", "center",
"centerErr", "fwhm", "fwhmErr, "integral", and "integralErr". Each of these arrays will have one more dimension than the overview arrays described
above. The shape of the first n-1 dimensions will be the same as the shape of the arrays described above, while the final dimension will
have length equal to the maximum number of gaussian singlets that were fit. Along this axis will be the
corresponding fit result or associated error (depending on the array's associated key) of the fit for that singlet component number. In cases where
the fit did not converge, or that particular component was excluded from the fit, a value of NAN will be present.

If any lorentzian singlets were fit, their solutions will be accessible via the "ls" key. These arrays follow the same rules
as the "gs" arrays described above.

If any gaussian multiplets were fit, there will be subdictionaries accessible by keys "gm0", "gm1", ..., "gm{n-1}" where n is the number of gaussian
muliplets that were fit. Each of these dictionaries will have the same arrays described above for gaussian singlets. The last dimension
will have length equal to the number of components in that particular multiplet. Each pixel along the last axis will be the parameter solution
value or error for that component number in the multiplet, eg the zeroth pixel along that axis contains
the parameter solution or error for the reference component of the multiplet.

The polynomial coefficient solutions and errors are not returned, although they are logged.

OUTPUT IMAGES
In addition to the returned dictionary, optionally one or more of any combination of output images can be written.
The model and residual parameters indicate the names of the model and residual images to be written; blank values inidcate that these images
should not be written.

One can also write none, any or all of the solution and error images for Gaussian singlet, Lorentzian singlet,  and Gaussian multiplet fits
via the parameters amp, amperr, center, centererr, fwhm, fwhmerr, integral, and integralerr when doing multi-pixel fits. These images simply
contain the arrays described for the associated parameter solutions or errors described in previous sections. In the case of Lorentzian
singlets, "_ls" is appended to the image names, in the case of Gaussian multiplets, "_gm" is appended. Pixels for which fits were not attempted or did not converge will be masked as bad. The last axis of these images
is a linear axis and repesents component number (and is named accordingly). In the case where multiple Gaussian singlets and/or
Lorentzians are fitted, the image names are further appended with an underscore and the relevant component number ("_0", "_1", etc).
In the case of Gaussian multiplets, the image names are appended with an underscore, followed by the number of the relevant
multiplet group, followed by an underscore, followed by the number of the component in that group (eg, "image_gm_3_4" represents
component number 4 of multiplet group number 3). Pixels for which fits were not attempted, did not converge, or converged but
have values of NaN (not a number) or INF (infinity) will be masked as bad.

Writing analogous images for polynomial coefficients is not supported.

EXAMPLE
res = specif(imagename="myspectrum.im", ngauss=2, box="3,3,4,5", poly=2, multifit=true, wantreturn=True)

        """
        if type(gmampest)==float: gmampest=[gmampest]
        if type(gmcenterest)==float: gmcenterest=[gmcenterest]
        if type(gmfwhmest)==float: gmfwhmest=[gmfwhmest]
        if type(goodamprange)==float: goodamprange=[goodamprange]
        if type(goodcenterrange)==float: goodcenterrange=[goodcenterrange]
        if type(goodfwhmrange)==float: goodfwhmrange=[goodfwhmrange]

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
        mytmp['ngauss'] = ngauss
        mytmp['poly'] = poly
        mytmp['estimates'] = estimates
        mytmp['minpts'] = minpts
        mytmp['multifit'] = multifit
        mytmp['model'] = model
        mytmp['residual'] = residual
        mytmp['amp'] = amp
        mytmp['amperr'] = amperr
        mytmp['center'] = center
        mytmp['centererr'] = centererr
        mytmp['fwhm'] = fwhm
        mytmp['fwhmerr'] = fwhmerr
        mytmp['integral'] = integral
        mytmp['integralerr'] = integralerr
        mytmp['wantreturn'] = wantreturn
        mytmp['stretch'] = stretch
        mytmp['logresults'] = logresults
        mytmp['pampest'] = pampest
        mytmp['pcenterest'] = pcenterest
        mytmp['pfwhmest'] = pfwhmest
        mytmp['pfix'] = pfix
        mytmp['gmncomps'] = gmncomps
        mytmp['gmampcon'] = gmampcon
        mytmp['gmcentercon'] = gmcentercon
        mytmp['gmfwhmcon'] = gmfwhmcon
        mytmp['gmampest'] = gmampest
        mytmp['gmcenterest'] = gmcenterest
        mytmp['gmfwhmest'] = gmfwhmest
        mytmp['gmfix'] = gmfix
        mytmp['logfile'] = logfile
        mytmp['append'] = append
        mytmp['pfunc'] = pfunc
        mytmp['goodamprange'] = goodamprange
        mytmp['goodcenterrange'] = goodcenterrange
        mytmp['goodfwhmrange'] = goodfwhmrange
        mytmp['sigma'] = sigma
        mytmp['outsigma'] = outsigma
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'specfit.xml')

        casalog.origin('specfit')
        if trec.has_key('specfit') and casac.utils().verify(mytmp, trec['specfit']) :
            result = task_specfit.specfit(imagename, box, region, chans, stokes, axis, mask, ngauss, poly, estimates, minpts, multifit, model, residual, amp, amperr, center, centererr, fwhm, fwhmerr, integral, integralerr, wantreturn, stretch, logresults, pampest, pcenterest, pfwhmest, pfix, gmncomps, gmampcon, gmcentercon, gmfwhmcon, gmampest, gmcenterest, gmfwhmest, gmfix, logfile, append, pfunc, goodamprange, goodcenterrange, goodfwhmrange, sigma, outsigma)

        else :
          result = False
        return result