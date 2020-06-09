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
import task_immath
def immath(imagename='', mode='evalexpr', outfile='immath_results.im', expr='IM0', varnames='', sigma='0.0mJy/beam', polithresh='', mask='', region='', box='', chans='', stokes='', stretch=False, imagemd='', prec='float'):

        """Perform math operations on images

    This task evaluates mathematical expressions involving existing
    image files. The results of the calculations are stored in the 
    designated output file.  Options are available to specify mathematical 
    expression directly or pre-defined expression for calculation of 
    spectral index image, and polarization intensity and position angle 
    images are available. The image file names imbedded in the expression or
    specified in the imagename parameter for the pre-defined calculations may
    be CASA images or FITS images.


    NOTE: Index values start at 0 Use the imhead task to see the range of
          index values for each axes.
    

    Keyword arguments:
    imagename  input image name(s)
               Default: none;
               Examples: mode='evalexpr'; imagename=['image1.im', 'image2.im' ]
               The text 'IM0' is replaced by 'image1.im' in the
               expression and 'IM1' is repalced with 'image2.im'
               mode='spix'; imagename=['image1.im','image2.im'] will calculate 
               an image of log(S1/S2)/log(f1/f2), where S1 and S2 are fluxes and 
               f1 and f2 are frequencies
               mode='pola'; imagename='multistokes.im' (where that image contains both Q and U
               stokes planes) or imagename=['imageQ.im','imageU.im'] will calculate 
               an image of polarization angle distribution, where imageQ.im and 
               imageU.im are Stokes Q and U images, respectively. Calculate 0.5*arctan(U/Q).
               mode='poli'; imagename=['imageQ.im','imageU.im','imageV.im'] will calculate
               total polarization intensity image, where imageQ.im, imageU.im, imageV.im
               are Stokes Q, U, and V images, respectively. Alternatively, with
               imagename = ['imageQ.im','imageU.im'] the linear polarization intensity
               image will be calculated. In the case where imagename is a single multi-stokes
               image, the total polarization image will be calculated if all of the Q, U, and
               V stokes planes are present, and the linear polarization intensity image will
               be calculated if the Q and U (but not V) planes are present. 

    mode       mode for mathematical operation
               Default: evalexpr
               Options: 'evalexpr' : evalulate a mathematical expression defined in 'expr' 
                        'spix' : spectalindex image 
                        'pola' : polarization position angle image 
                        'poli' : polarization intesity image 
              >>> mode expandable parameters
              sigma       (for mode='poli') standard deviation of noise of Stokes images with unit such as
                          Jy/beam to correct for bias 
                          Default: '0.0Jy/beam' (= no debiasing)
              polithresh  (for mode='pola') Quantity (eg '30uJy/beam') describing the linear (not total;
                          the stokes V contribution is not included) polarization threshold. A mask ('mask0')
                          is written to the output image and is False for all corresponding linear polarization
                          values below this threshold. This parameter overrides the mask input parameter
                          (below). Default ('') means use the value given in mask, or no masking if that
                          value is empty as well.
              expr        (for mode='evalexpr') A LEL expression with images.
                          Image file names are specified in the imagenames paramter, and
                          the variables IM0, IM1, ... (or optionally via the varnames parameter, see below)
                          are used to represent these files
                          in the expression. Explicit notations of file names in the 
                          expression are also supported, in which cases the file names must
                          be enclosed in double quotes (") and imagename is ignored.
                          Examples:
                          Make an image that is image1.im - image2.im
                          expr=' (IM0 - IM1 )'
                          or with an explicit notation, 
                          expr='("image1.im" - "image2.im")'
                          Clip an image below a value (0.5 in this case)
                          expr = ' iif( IM0 >=0.5, IM0, 0.0) '
                          Note: iif (a, b, c)   a is the boolean expression
                                                b is the value if true
                                                c is the value if false
                          Take the rms value of two images
                          expr = ' sqrt(IM0 * IM0 + IM1 * IM1) '
                          Build an image pixel by pixel from the minimum of (image2.im, 2*image1.im)
                          expr='min(IM1,2*max(IM0))'
               varnames   For mode="evalexpr". Instead of the default variable names IM0, IM1, ..., use
                          the names in this array to represent the input images.
    outfile    The output image. Overwriting an existing outfile is not permitted.
               Default: immath_results.im;  Example: outfile='results.im'
    mask       Mask to use. Default is none. Also see polithresh.
    stretch    Stretch the input mask if necessary and possible. See below.
    region     Region selection. Default is to use the full image.
    box        Rectangular region to select in direction plane. Default
               is to use the entire direction plane.
               Example: box='10,10,50,50'
    chans      Channels to use. Default is to use all channels.
    stokes     Stokes planes to use. Default is to use all Stokes planes.
               Not used in for cases of mode='poli' or mode='pola'
    imagemd    The image from which metadata should be copied to the output. Default means no guarantee from
                which image is used. The image must exist and should conform to the output image spec.

    Available functions in the expr and mask parameters:
    pi(), e(), sin(), sinh(), asinh(), cos(), cosh(), tan(), tanh(),
    atan(), exp(), log(), log10(), pow(), sqrt(), complex(), conj()
    real(), imag(), abs(), arg(), phase(), amplitude(), min(), max()
    round(), isgn(), floor(), ceil(), rebin(), spectralindex(), pa(), 
    iif(), indexin(), replace(), ...

    If the mask has fewer dimensions than the image and if the shape
    of the dimensions the mask and image have in common are the same,
    the mask will automatically have the missing dimensions added so
    it conforms to the image.

    For a full description of the allowed syntax see the 
    Lattice Expression Language (LEL) documentation on the at:
    http://aips2.nrao.edu/docs/notes/223/223.html

    NOTE: where indexing and axis numbering are used in the above
    functions they are 1-based, ie. numbering starts at 1.

    If stretch is true and if the number of mask dimensions is less than
    or equal to the number of image dimensions and some axes in the
    mask are degenerate while the corresponding axes in the image are not,
    the mask will be stetched in the degenerate axis dimensions. For example,
    if the input image has shape [100, 200, 10] and the input
    mask has shape [100, 200, 1] and stretch is true, the mask will be
    stretched along the third dimension to shape [100, 200, 10]. However if
    the mask is shape [100, 200, 2], stretching is not possible and an
    error will result.

    CAUTIONS REGARDING OUTPUT IMAGE METADATA, INCLUDING BRIGHTNESS UNIT

    EXCEPT IN THE CASES NOTED BELOW, THIS APPLICATION MAKES NO ATTEMPT TO
    DETERMINE WHAT THE CORRECT BRIGHTNESS UNIT OF THE OUTPUT IMAGE SHOULD BE. THIS
    RESPONSIBILITY LIES SOLELY WITH THE USER. The brightness unit of the output image
    can be modified using tool method ia.setbrightnessunit() or task imhead with
    mode='put' and hdkey='bunit'. 

    Note that when multiple image are used in the expression, there is
    no garauntee about which of those images will be used to create the metadata
    of the output image, unless imagemd is specified. If imagemd is specified, the following
    rules of metadata copying will be followed:
    
    1. The pixel data type of the image specified by imagemd and the output image must
    be the same.
    2. The metadata copied include the coordinate system (and so of course the dimensionality of
    the output image must correspond to the coordinate system to be copied), the image_info record
    (which contains things like the beam(s)), the misc_info record (should one exist in the image
    specified by imagemd), and the units.
    3. If the output image is a spectral image, the brightness units are set to the empty string.
    4. If the ouptut image is a polarization angle image, the brightness unit is set to "deg" and
    the stokes coordinate is set to have a single plane of type of Pangle.

    Examples:
    # Double all values in an image.
    immath( imagesname='myimage.im', expr='IM0*2', outfile='double.im' )
    # or with an explicit notation, 
    immath( expr='"myimage.im"*2', outfile='double.im' )

    # Taking the sin of an image and adding it to another
    # Note that the images need to be the same size
    immath(images=['image1.im', 'image2.im'], expr='sin(IM1)+IM0;',outfile='newImage.im')

    # Adding only the plane associated with the 'V' stokes value and
    # the 1st channel together in two images
    immath(imagename=[image1', 'image2'], expr='IM0+IM1',chans='1',stokes='V')


    # Selecting a single plane (5th channel), of the 3-D cube and  
    # adding it to the original image.  In this example the 2-D plane
    # gets expanded out and the values are applied to each plane in the 
    # 3-D cube. 
    default('immath')
    imagename='ngc7538.image'
    outfile='chanFive.im'
    expr='IM0'
    chans='5'
    go
    default('immath')
    imagename=['ngc7538.image', chanFive.im']
    outfile='ngc7538_chanFive.im'
    expr='IM0+IM1'
    go

    # Selecting and saving the inner 3/4 of an image for channels 40,42,44
    # as well as channels less than 10
    default('immath')
    imagename='my_image.im'
    expr='IM0'
    box='25,25,123,123'
    chans='<10;40,42,44'
    outfile='my_image_inner.im' )
    go

    # Dividing an image by another, making sure we aren't dividing by zero
    default('immath')
    imagename=['orion.image', 'my.image']
    expr='IM0/iif(IM1==0,1.0,IM1)'
    outfile='my_orion.image'
    go

    # Applying a mask to all of the images in the expression
    default('immath')
    imagename=['ngc7538.image','ngc7538_clean.image']
    expr='(IM0*10)+IM1'
    mask='"ngc7538.mask"'
    outfile='really_noisy_ngc7538.image'
    go


    # Applying a pixel mask contained in the image information
    default('immath')
    imagename='ngc5921.image'
    expr='IM0*10'
    mask='mask("ngc5921.mask")'
    outfile='ngc5921.masked.image'
    go

    # Creating a total polarization intensity image from an multi-stokes image
    # containing IQUV.
    default('immath')
    outfile='pol_intensity'
    stokes=''
    # in imagename, you can also specify a list containing single stokes images
    # of Q and U (for linear polarization intensity) and V (for total
    # polarization intensity)
    imagename='3C138_pcal'
    mode='poli'
    go

    # Creating a polarization position angle image 
    default('immath')
    outfile='pol_angle.im'
    mode='pola'
    # you can also do imagename=['Q.im','U.im'] for single stokes images, order of
    # the two Stokes images does not matter
    imagename='3C138_pcal' # multi-stokes image containing at least Q and U stokes 
    go 

    # same as before but write a mask with values of False for pixels for which the
    # corresponding linear polarization ( sqrt(Q*Q+U*U)) is less than 30 microJy/beam
    polithresh='30uJy/beam'
    go

    # Creating a spectral index image from the images at two different observing frequencies
    default('immath')
    outfile='mySource_sp.im'
    mode='spix'
    imagename=['mySource_5GHz.im','mySource_8GHz.im']
    go
    
    TEMPORARY IMAGES

    At this time, it is usually necessary for this task to create intermediate, temporary disk images.
    The names of these images start with '_immath' and are created in the directory in which the task
    is run. The task makes reasonable attempts to remove these images before it exits, but there are
    conceivably instances where the temporary images may not be automatically deleted. It is generally
    safe to delete them by hand, assuming no immath instance is currently in progress.

    The hope and plan is that the necessity of these images will decrease in the future (i.e. the computations
    will require only RAM and not temporary persistent storage of intermediate results).

 

        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['mode'] = mode
        mytmp['outfile'] = outfile
        mytmp['expr'] = expr
        mytmp['varnames'] = varnames
        mytmp['sigma'] = sigma
        mytmp['polithresh'] = polithresh
        mytmp['mask'] = mask
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['stretch'] = stretch
        mytmp['imagemd'] = imagemd
        mytmp['prec'] = prec
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'immath.xml')

        casalog.origin('immath')
        if trec.has_key('immath') and casac.utils().verify(mytmp, trec['immath']) :
            result = task_immath.immath(imagename, mode, outfile, expr, varnames, sigma, polithresh, mask, region, box, chans, stokes, stretch, imagemd, prec)

        else :
          result = False
        return result