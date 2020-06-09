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
import task_imdev
def imdev(imagename='', outfile='', region='', box='', chans='', stokes='', mask='', overwrite=False, stretch=False, grid=[1, 1], anchor='ref', xlength='1pix', ylength='1pix', interp='cubic', stattype='sigma', statalg='classic', zscore=-1, maxiter=-1):

        """Create an image that can represent the statistical deviations of the input image.
    This application creates an image that reflects the statistics of the input image. The output image has
    the same dimensions and coordinate system as the (selected region in) input image. The grid parameter
    describes how many pixels apart "grid" pixels are. Statistics are computed around each grid pixel. Grid
    pixels are limited to the direction plane only; independent statistics are computed for each direction plane
    (ie at each frequency/stokes pixel should the input image happen to have such additional axes). Using the
    xlength and ylength parameters, one may specify either a rectangular or circular region around each grid
    point that defines which surrounding pixels are used in the statistic computation for individual grid points.
    If the ylength parameter is the empty string, then a circle of diameter provided by xlength centered on
    the grid point is used. If ylength is not empty, then a rectangular box of dimensions xlength x ylength centered
    on the grid pixel is used. These two parameters may be specified in pixels, using either numerical values or
    valid quantities with "pix" as the unit (eg "4pix"). Otherwise, they must be specified as valid angular
    quantities, with recognized units (eg "4arcsec"). As with other region selections in CASA, full pixels are
    included in the computation even if the specified region includes only a fraction of that pixel. BEWARE OF
    MACHINE PRECISION ISSUES, because you may get a smaller number of pixels included in a region than you
    expect if you specify, eg, an integer number of pixels. In such cases, you probably want to specify that
    number plus a small epsilon value (eg "2.0001pix" rather than "2pix") to mitigate machine precision issues
    when computing region extents.

    The output image is formed by putting the statistics calculated at each grid point at the corresponding
    grid point in the output image. Interpolation of these output values is then used to compute values at
    non-grid-point pixels. The user may specify which interpolation algorithm to use for this computation
    using the interp parameter.
    
    The input image pixel mask is copied to the output image. If interpolation is performed, output pixels are
    masked where the interpolation fails.

    ANCHORING THE GRID

    The user may choose at which pixel to "anchor" the grid. For example, if one specifies grid=[4,4] and
    anchor=[0,0], grid points will be located at pixels [0,0], [0,4], [0,8] ... [4,0], [4,4], etc. This
    is exactly the same grid that would be produced if the user specified anchor=[4,4] or anchor=[20,44].
    If the user specifies anchor=[1, 2] and grid=[4,4], then the grid points will be at pixels [1,2], [5,2],
    [9,2]... [5,2], [5,6], etc. and the resulting grid is the same as it would be if the user specified eg
    anchor=[9,10] or anchor=[21, 18]. The value "ref", which is the default, indicates that the reference
    pixel of the input image should be used to anchor the grid. The x and y values of this pixel will be
    rounded to the nearest integer if necessary.

    SUPPORTED STATISTICS AND STATISTICS ALGORITHMS

    One may specify which statistic should be represented using the stattype parameter. The following values
    are recognized (minimum match supported):

    iqr                   inner quartile range (q3 - q1)
    max                   maximum
    mean                  mean
    medabsdevmed, madm    median absolute deviation from the median
    median                median
    min                   minimum
    npts                  number of points
    q1                    first quartile
    q3                    third quartile
    rms                   rms
    sigma, std            standard deviation
    sumsq                 sum of squares
    sum                   sum
    var                   variance
    xmadm                 median absolute deviation from the median multipied by x, where x is the reciprocal of Phi^-1(3/4),
                          where Phi^-1 is the reciprocal of the quantile function. Numerically, x = 1.482602218505602. See, eg,
                          https://en.wikipedia.org/wiki/Median_absolute_deviation#Relation_to_standard_deviation

    Using the statalg parameter, one may also select whether to use the Classical or Chauvenet/ZScore statistics algorithm to
    compute the desired statistic (see the help for ia.statistics() or imstat for a full description of these algorithms).

    # compute standard deviations in circles of diameter 10arcsec around
    # grid pixels spaced every 4 x 5 pixels and anchored at pixel [30, 40],
    # and use linear interpolation to compute values at non-grid-pixels
    imdev("my.im", "sigma.im", grid=[4, 5], anchor=[30, 40], xlength="10arcsec", stattype="sigma", interp="lin", statalg="cl")

    # compute median of the absolute deviations from the median values using
    # the z-score/Chauvenet algorithm, by fixing the maximum z-score to determine outliers to 5.
    # Use cubic interpolation to compute values for non-grid-point pixels. Use a rectangular region
    # of dimensions 5arcsec x 20arcsec centered on each grid point as the region in which to include
    # pixels for the computation of stats for that grid point.
    imdev("my.im", "madm.im", grid=[4, 5], anchor=[30, 40], xlength="5arcsec", ylength="20arcsec, stattype="madm", interp="cub", statalg="ch", zscore=5)

        """
        if type(grid)==int: grid=[grid]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['overwrite'] = overwrite
        mytmp['stretch'] = stretch
        mytmp['grid'] = grid
        mytmp['anchor'] = anchor
        mytmp['xlength'] = xlength
        mytmp['ylength'] = ylength
        mytmp['interp'] = interp
        mytmp['stattype'] = stattype
        mytmp['statalg'] = statalg
        mytmp['zscore'] = zscore
        mytmp['maxiter'] = maxiter
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'imdev.xml')

        casalog.origin('imdev')
        if trec.has_key('imdev') and casac.utils().verify(mytmp, trec['imdev']) :
            result = task_imdev.imdev(imagename, outfile, region, box, chans, stokes, mask, overwrite, stretch, grid, anchor, xlength, ylength, interp, stattype, statalg, zscore, maxiter)

        else :
          result = False
        return result
