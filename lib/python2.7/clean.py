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
import task_clean
def clean(vis='', imagename='', outlierfile='', field='', spw='', selectdata=True, timerange='', uvrange='', antenna='', scan='', observation='', intent='', mode='mfs', resmooth=False, gridmode='', wprojplanes=-1, facets=1, cfcache='cfcache.dir', rotpainc=5.0, painc=360.0, aterm=True, psterm=False, mterm=True, wbawp=False, conjbeams=True, epjtable='', interpolation='linear', niter=500, gain=0.1, threshold='0.0mJy', psfmode='clark', imagermode='csclean', ftmachine='mosaic', mosweight=False, scaletype='SAULT', multiscale=[0], negcomponent=-1, smallscalebias=0.6, interactive=False, mask=[], nchan=-1, start=0, width=1, outframe='', veltype='radio', imsize=[256, 256], cell=['1.0arcsec'], phasecenter='', restfreq='', stokes='I', weighting='natural', robust=0.0, uvtaper=False, outertaper=[''], innertaper=['1.0'], modelimage='', restoringbeam=[''], pbcor=False, minpb=0.2, usescratch=False, noise='1.0Jy', npixels=0, npercycle=100, cyclefactor=1.5, cyclespeedup=-1, nterms=1, reffreq='', chaniter=False, flatnoise=True, allowchunk=False):

        """Invert and deconvolve images with selected algorithm
       The clean task has many options:
 
        1)  Make 'dirty' image and 'dirty' beam (psf)
        2)  Multi-frequency-continuum images or spectral channel imaging
        3)  Full Stokes imaging
        4)  Mosaicking of several pointings
        5)  Multi-scale cleaning
        6)  Widefield cleaning
        7)  Interactive clean boxing
        8)  Use starting model (eg from single dish)
 
 
       vis -- Name(s) of input visibility file(s)
               default: none; 
               example: vis='ngc5921.ms'
                        vis=['ngc5921a.ms','ngc5921b.ms']; multiple MSes
       imagename -- Pre-name of output images:
               default: none; example: imagename='m2'
               output images are:
                 m2.image; cleaned and restored image
                        With or without primary beam correction
                 m2.psf; point-spread function (dirty beam)
                 m2.flux;  relative sky sensitivity over field
                 m2.flux.pbcoverage;  relative pb coverage over field 
                                      (gets created only for ft='mosaic')
                 m2.model; image of clean components
                 m2.residual; image of residuals
                 m2.interactive.mask; image containing clean regions
               To include outlier fields: 
                 imagename=['n5921','outlier1','outlier2'] 
       outlierfile --- Text file name which contains image names, sizes, field
                       centers (See 'HINTS ON CLEAN WITH FLANKING FIELDS' below 
                       for the format of this outlier file.)
       field -- Select fields to image or mosaic.  Use field id(s) or name(s).
                  ['go listobs' to obtain the list id's or names]
               default: ''= all fields
                 If field string is a non-negative integer, it is assumed to
                 be a field index otherwise, it is assumed to be a 
                 field name
                 field='0~2'; field ids 0,1,2
                 field='0,4,5~7'; field ids 0,4,5,6,7
                 field='3C286,3C295'; field named 3C286 and 3C295
                 field = '3,4C*'; field id 3, all names starting with 4C
                 For multiple MS input, a list of field strings can be used:
                 field = ['0~2','0~4']; field ids 0-2 for the first MS and 0-4
                         for the second 
                 field = '0~2'; field ids 0-2 for all input MSes
       spw -- Select spectral window/channels
               NOTE: channels de-selected here will contain all zeros if
                         selected by the parameter mode subparameters.    
               default: ''=all spectral windows and channels
                 spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                 spw='0:5~61'; spw 0, channels 5 to 61
                 spw='<2';   spectral windows less than 2 (i.e. 0,1)
                 spw='0,10,3:3~45'; spw 0,10 all channels, spw 3, 
                                    channels 3 to 45.
                 spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
                 For multiple MS input, a list of spw strings can be used:
                 spw=['0','0~3']; spw ids 0 for the first MS and 0-3 for the second
                 spw='0~3' spw ids 0-3 for all input MS
                 spw='3:10~20;50~60' for multiple channel ranges within spw id 3
                 spw='3:10~20;50~60,4:0~30' for different channel ranges for spw ids 3 and 4
                 spw='0:0~10,1:20~30,2:1;2;3'; spw 0, channels 0-10,
                      spw 1, channels 20-30, and spw 2, channels, 1,2 and 3
                 spw='1~4;6:15~48' for channels 15 through 48 for spw ids 1,2,3,4 and 6
                  
       selectdata -- Other data selection parameters
               default: True

  >>> selectdata=True expandable parameters
               See help par.selectdata for more on these

               timerange  -- Select data based on time range:
                   default: '' (all); examples,
                   timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                   Note: if YYYY/MM/DD is missing date defaults to first 
                         day in data set
                   timerange='09:14:0~09:54:0' picks 40 min on first day
                   timerange='25:00:00~27:30:00' picks 1 hr to 3 hr 
                             30min on NEXT day
                   timerange='09:44:00' pick data within one integration 
                             of time
                   timerange='>10:24:00' data after this time
                   For multiple MS input, a list of timerange strings can be
                   used:
                   timerange=['09:14:0~09:54:0','>10:24:00']
                   timerange='09:14:0~09:54:0''; apply the same timerange for
                                                 all input MSes 
               uvrange -- Select data within uvrange (default units meters)
                   default: '' (all); example:
                   uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                   uvrange='>4klambda';uvranges greater than 4 kilo lambda
                   For multiple MS input, a list of uvrange strings can be
                   used:
                   uvrange=['0~1000klambda','100~1000klamda']
                   uvrange='0~1000klambda'; apply 0-1000 kilo-lambda for all
                                            input MSes
               antenna -- Select data based on antenna/baseline
                   default: '' (all)
                   If antenna string is a non-negative integer, it is 
                   assumed to be an antenna index, otherwise, it is
                   considered an antenna name.
                   antenna='5&6'; baseline between antenna index 5 and 
                                 index 6.
                   antenna='VA05&VA06'; baseline between VLA antenna 5 
                                       and 6.
                   antenna='5&6;7&8'; baselines 5-6 and 7-8
                   antenna='5'; all baselines with antenna index 5
                   antenna='05'; all baselines with antenna number 05 
                                (VLA old name)
                   antenna='5,6,9'; all baselines with antennas 5,6,9 
                                   index number
                   For multiple MS input, a list of antenna strings can be
                   used:
                   antenna=['5','5&6'];
                   antenna='5'; antenna index 5 for all input MSes
               scan -- Scan number range.
                   default: '' (all)
                   example: scan='1~5'
                   For multiple MS input, a list of scan strings can be used:
                   scan=['0~100','10~200']
                   scan='0~100; scan ids 0-100 for all input MSes
                   Check 'go listobs' to insure the scan numbers are in order.
               observation -- Observation ID range.
                   default: '' (all)
                   example: observation='1~5'
               intent -- Scan intent (case sensitive)
                   default: '' (all)
                   example: intent='TARGET_SOURCE'  
                   example: intent='TARGET_SOURCE1,TARGET_SOURCE2'  
                   example: intent='TARGET_POINTING*'

       mode -- Frequency Specification:
               NOTE: Channels deselected with spw parameter will contain all
                     zeros. 
               See examples below.
               default: 'mfs'
                 mode = 'mfs' means produce one image from all 
                      specified data.
                 mode = 'channel'; Use with nchan, start, width to specify
                        output image cube. 
                 mode = 'velocity', channels are specified in velocity.
                 mode = 'frequency', channels are specified in frequency.

  >>> mode='mfs' expandable parameters 
               Make a continuum image from the selected frequency
               channels/range using Multi-frequency synthesis
               algorithm for wide-band narrow field imaging.  
               mode='mfs' examples:
               spw = '0,1'; mode = 'mfs'
                  will produce one image made from all channels in spw 
                       0 and 1
               spw='0:5~28^2'; mode = 'mfs'
                  will produce one image made with channels 
                       (5,7,9,...,25,27)

             nterms -- Number of Taylor terms to be used to model the
               frequency dependence of the sky emission.  nterms=1 is
               equivalent to assuming no frequency dependence.
               nterms>1 runs the MS-MFS algorithm, and the choice of nterms 
               should depend on the expected shape and SNR of the spectral
               structure, across the chosen bandwidth. Output images 
               represent taylor-coefficients of the sky spectrum
               (images with file-name extensions of tt0,tt1,etc). 
               A spectral index map is also  computed as the ratio of the 
               first two terms (following the convention of I(nu) = I(ref_nu) x (nu/nu_0)^alpha).
               Additionally, a spectral-index error image is made
               by treating taylor-coefficient residuals as errors, and propagating
               them through the division used to compute spectral-index. 
               It is meant to be a guide to which parts of the spectral-index 
               image to trust, and the values may not always represent a 
               statistically-correct error.

               For more details about this algorithm, please refer to 
               "A multi-scale multi-frequency deconvolution algorithm for synthesis
                 imaging in radio interferometry", Rau and Cornwell, AA, Volume 532, 2011     
  
               ** Note that the software implementation of the MS-MFS algorithm
               for nterms>1 currently does not allow combination with  
               mosaics, and pbcor.**

             reffreq -- The reference frequency (for nterms>1) about which
                the Taylor expansion is done. reffreq='' defaults to the
                middle frequency of the selected range. 

  >>> mode='channel', 'velocity', and 'frequency' expandable parameters

               nchan -- Total number of channels in the output image.
                 Example: nchan=100. 
                 Default: -1; Automatically selects enough channels to cover 
                 data selected by 'spw' consistent with 'start' and 'width'. 
                 It is often easiest to leave nchan at the default value. 

               start -- First channel, velocity, or frequency. 
                 For mode='channel'; This selects the channel index number 
                 from the MS (0 based) that you want to correspond to the
                 first channel of the output cube. The output cube will be
                 in frequency space with the first channel having the
                 frequency of the MS channel selected by start.  start=0
                 refers to the first channel in the first selected spw, even
                 if that channel is de-selected in the spw parameter.
                 Channels de-selected by the spw parameter will be filled with
                 zeros if included by the start parameter. For example,
                 spw=3~8:3~100 and start=2 will produce a cube that starts on
                 the third channel (recall 0 based) of spw index 3, and the
                 first channel will be blank.
                 example:start=5
                 For mode='velocity' or 'frequency': default=''; 
                 starts at first input channel of first input spw
                 examples: start='5.0km/s', or start='22.3GHz'.

               width -- Output channel width
                 For mode='channel', default=1; >1 indicates channel averaging
                 example: width=4.
                 For mode= 'velocity' or 'frequency', default=''; width of
                 first input channel, or more precisely, the difference 
                 in frequencies between the first two selected channels. 
                 -- For example if channels 1 and 3 are selected with spw, 
                  then the default width will be the difference between their
                  frequencies, and not the width of channel 1. 
                 -- Similarly, if the selected data has uneven channel-spacing,
                   the default width will be picked from the first two selected
                   channels. In this case, please specify the desired width.
                 When specifying the width, one must give units
                 examples: width='1.0km/s', or width='24.2kHz'.
                 Setting width>0 gives channels of increasing frequency for 
                 mode='frequency', and increasing velocity for mode='velocity'. 

               interpolation -- Interpolation type for spectral gridding onto 
                 the uv-plane. Options: 'nearest', 'linear', or 'cubic'.
                 default = 'linear' 
                 Note : 'linear' and 'cubic' interpolation requires data
                        points on both sides of each image frequency. Errors
                        are therefore possible at edge  channels, or near
                        flagged data channels.
                When image channel width is much larger than the data channel width 
                there is nothing much to be gained using linear or cubic thus not worth
                the extra computation  involved.

              resmooth -- if the cube has a different restoring beam/channel. Restore 
                                image to a common beam  or leave as is (default)
                                options: True or False
                                default = False 
  
               chaniter -- specify how spectral CLEAN is performed, 
                 default: chaniter=False;
                 example: chaniter=True; step through channels 

               outframe -- For mode='velocity', 'frequency', or 'channel':
                             default spectral reference frame of output image
                 Options: '','LSRK','LSRD','BARY','GEO','TOPO','GALACTO',
                          'LGROUP','CMB'
                 default: ''; same as input data
                 example: frame='bary' for Barycentric frame 

               veltype -- for mode='velocity' gives the velocity definition
                 Options: 'radio','optical' 
                 default: 'radio'
                 NOTE: the viewer always defaults to displaying the 'radio'
                   frame, but that can be changed in the position tracking
                   pull down.

           mode='channel' examples:
               spw = '0'; mode = 'channel': nchan=3; start=5; width=4
                  will produce an image with 3 output planes
                  plane 1 contains data from channels (5+6+7+8)
                  plane 2 contains data from channels (9+10+11+12)
                  plane 3 contains data from channels (13+14+15+16)
               spw = '0:0~63^3'; mode='channel'; nchan=21; start = 0; 
                   width = 1
                  will produce an image with 20 output planes
                  Plane 1 contains data from channel 0
                  Plane 2 contains date from channel 2
                  Plane 21 contains data from channel 61
               spw = '0:0~40^2'; mode = 'channel'; nchan = 3; start = 
                   5; width = 4
                  will produce an image with three output planes
                  plane 1 contains channels (5,7)
                  plane 2 contains channels (13,15)
                  plane 3 contains channels (21,23)

       psfmode -- method of PSF calculation to use during minor cycles:
               default: 'clark': Options: 'clark','clarkstokes', 'hogbom'
               'clark'  use smaller beam (faster, usually good enough);
                for stokes images clean components peaks are searched
               in the I^2+Q^2+U^2+V^2 domain 
               'clarkstokes' locate clean components independently in
               each stokes image
               'hogbom' full-width of image (slower, better for poor 
               uv-coverage)
               Note:  psfmode will also be used to clean if imagermode = ''
       imagermode -- Advanced imaging e.g. mosaic or Cotton-Schwab clean
               default: imagermode='csclean': Options: '', 'csclean', 'mosaic'
               ''  => psfmode cleaning algorithm used
               NOTE: imagermode 'mosaic' (and/or) any gridmode not blank 
                         (and/or) nterms>1 : will always use CS style clean. 

  >>> gridmode='' expandable parameters
               The default value of '' has no effect.
        
  >>> gridmode='widefield' expandable parameters
               Apply corrections for non-coplanar effects during imaging
               using the W-Projection algorithm (Cornwell et al. IEEE JSTSP
               (2008)) or faceting or a combination of the two.

               wprojplanes is the number of pre-computed w-planes used for
                   the W-Projection algorithm.  wprojplanes=1 disables
                   correction for non-coplanar effects.  default value wprojpanes=-1
                   means clean will determine the number to use. 
               facets is the number of facets on each side of the image 
                   (i.e. the total number of facets is 'facets x facets'). 
                   If wprojplanes>1, W-Projection is done for each facet.
                   Usually when many wprojection convolution functions 
                   sizes are  above ~400 pixels , 
                   it might be faster to use a few facets with wprojection.

  >>> gridmode='aprojection' expandable parameters
               Corrects for the (E)VLA time-varying PB effects
               including polarization squint using the A-Projection
               algorithm (Bhatnagar et al., AandA, 487, 419 (2008)).
               This can optinally include w-projection also.

               wprojplanes is the number of pre-computed w-planes used
               for W-Projection algorithm.  wprojplanes=1 disables
               correction for non-coplanar effects.

               cfcache is the name of the directory to store the
               convolution functions and weighted sensitivty pattern
               function. 
               
               
               

               rotpainc (in degrees) is the Parallactic Angle increment
               used for OTF rotation of the convolution function.

               painc (in degrees) is the Parallactic Angle increment
               used to compute the convolution functions.

  >>> imagermode='mosaic' expandable parameter(s):
               Make a mosaic of the different pointings (uses csclean style
               too)
               mosweight -- Individually weight the fields of the mosaic
                   default: False; example: mosweight=True
                   This can be useful if some of your fields are more
                   sensitive than others (i.e. due to time spent 
                   on-source); this parameter will give more weight to 
                   higher sensitivity fields in the overlap regions.
               ftmachine -- Gridding method for the mosaic;
                   Options: 'mosaic' , 'ft' or 'wproject' 
                   default: 'mosaic'; 
                   'ft' or 'wproject' implies standard interferometric 2D or widefield gridding. The residual visibilities are 
                   imaged for each pointing and combined in the image plane with the 
                   appropriate PB to make the mosaic.
                    
                   'mosaic' (grid using the Fourier transform of PB as convolution function 
                   and mosaic combination is done in visibilities). 
                   ONLY if imagermode='mosaic' is chosen and
                   ftmachine='mosaic', is heterogeneous imaging (CARMA, ALMA) or 
                   wideband beam accounting 
                   possible using the right convolution derived from primary beams for
                   each baseline and for different frequencies
                   CAVEAT: ftmachine='mosaic' uses Fourier transforms of the primary beams/pointing
                   for mosaicing. Making an image which is too small for the pointing coverages will cause
                   aliasing due to standard Fourier transform wrap around. 

               scaletype -- Controls scaling of pixels in the image plane.
                   (controls what is seen if interactive=True)
                   It does *not* affect the scaling of the *final* image -
                   that is done by pbcor.
                   default='SAULT'; example: scaletype='PBCOR'
                   Options: 'PBCOR','SAULT'
                     'SAULT' when interactive=True shows the residual
                             with constant noise across the mosaic. 
                             Can also be achieved by setting pbcor=False.
                     'PBCOR' uses the SAULT scaling scheme for
                             deconvolution, but if interactive=True shows the
                             primary beam corrected image during interactive. 

               cyclefactor -- Controls the threshhold at which the
                   deconvolution cycle will pause to degrid and subtract the
                   model from the visibilities.
                   With poor PSFs, reconcile often (cyclefactor=4 or 5) for
                   reliability. 
                   With good PSFs, use cyclefactor = 1.5 to 2.0 for speed. 
                   Note: threshold = cyclefactor * max sidelobe * max residual
                   default: 1.5; example: cyclefactor=4
               cyclespeedup -- The major cycle threshold doubles in this
                   number of iterations.
                   Default: -1 (no doubling)
                   Example: cyclespeedup=3
                   Try cyclespeedup = 50 to speed up cleaning.

               flatnoise -- Controls whether searching for clean components
                   is done in a constant noise residual image (True) or in an
                   optimal signal-to-noise residual image (False) when
                   ftmosaic='mosaic' is chosen.
                   default=True

  >>> imagermode='csclean' expandable parameter(s): 
               Image using the Cotton-Schwab algorithm in between major cycles

               cyclefactor -- See above, under imagermode='mosaic'.
               cyclespeedup -- See above, under imagermode='mosaic'.

       multiscale -- set of scales to use in deconvolution.  If set,
               cleans with several resolutions using Hogbom clean. The
               scale sizes are in units of cellsize.  So if
               cell='2arcsec', a multiscale scale=10 => 20arcsec.  The
               first scale is recommended to  be 0 (point), we suggest the
               second be on the order of synthesized beam, the third 3-5
               times the synthesized beam, etc..  Avoid making the largest
               scale too large relative to the image width or the scale of
               the lowest measured spatial frequency.  For example, if the
               synthesized beam is 10" FWHM and cell=2", try
               multiscale = [0,5,15].
               
               default: multiscale=[] (standard CLEAN with psfmode algorithm,
               no multi-scale).
               Example: multiscale = [0,5,15] 

  >>> multiscale expandable parameter(s): 
               negcomponent -- Stop component search when the largest scale
                 has found this number of negative components;
                 -1 means continue component search even if the largest
                 component is negative.  default: -1; example: negcomponent=50
               smallscalebias -- A bias toward smaller scales. 
                   The peak flux found at each scale is weighted by 
                   a factor = 1 - smallscalebias*scale/max_scale, so
                   that Fw = F*factor.
                   Typically the values range from 0.2 to 1.0.
                   default: 0.6

       imsize -- Image size in pixels (x, y).  DOES NOT HAVE TO BE A POWER
                 OF 2 (but has to be even and factorizable to 2,3,5,7 only).
               default = [256,256]; example: imsize=[350,350]
               imsize = 500 is equivalent to [500,500]
               If include outlier fields, e.g., [[400,400],[100,100]] or
               use outlierfile.
               Avoid odd-numbered imsize.
       cell -- Cell size (x,y)
               default= '1.0arcsec';
               example: cell=['0.5arcsec,'0.5arcsec'] or
               cell=['1arcmin', '1arcmin']
               cell = '1arcsec' is equivalent to ['1arcsec','1arcsec']
               NOTE:cell = 2.0 => ['2arcsec', '2arcsec']
       phasecenter -- direction measure  or fieldid for the mosaic center
               default: '' => first field selected ; 
               example: phasecenter=6
                        phasecenter='J2000 19h30m00 -40d00m00'
                        phasecenter='J2000 292.5deg  -40.0deg'
                        phasecenter='J2000 5.105rad  -0.698rad'
               If include outlier fields, 
                e.g. ['J2000 19h30m00 -40d00m00',J2000 19h25m00 -38d40m00']
               or use outlierfile.
       restfreq -- Specify rest frequency to use for output image
               default='' Occasionally it is necessary to set this (for
               example some VLA spectral line data).  For example for
               NH_3 (1,1) put restfreq='23.694496GHz'
       stokes -- Stokes parameters to image
               default='I'; example: stokes='IQUV';
               Options: 'I','Q','U','V','IV','QU','IQ','UV','IQU','IUV','IQUV','RR','LL','XX','YY','RRLL','XXYY'
       niter -- Maximum number iterations,
               if niter=0, then no CLEANing is done ("invert" only).
               (niter=0 can be used instead of the 'ft' task to predict/save a model)
               For cube or multi field images niter is the maximum number of iteration 
               clean will use for each image plane.
               The number of iterations used may be less that niter if threshold value 
                is reached 
               default: 500; example: niter=5000
       gain -- Loop gain for CLEANing
               default: 0.1; example: gain=0.5
       threshold -- Flux level at which to stop CLEANing
               default: '0.0mJy'; 
               example: threshold='2.3mJy'  (always include units)
                        threshold = '0.0023Jy'
                        threshold = '0.0023Jy/beam' (okay also)
       interactive -- use interactive clean (with GUI viewer)
               default: interactive=False
               example: interactive=True
               interactive clean allows the user to build the cleaning
               mask interactively using the viewer.  The viewer will
               appear every npercycle interation, but modify as needed
               The final interactive mask is saved in the file
               imagename_interactive.mask.  The initial masks use the
               union of mask and cleanbox (see below).

  >>> interactive=True expandable parameters
               npercycle -- this is the  number of iterations between each
                 interactive update of the mask.  It is important to modify
                 this number interactively during the cleaning, starting with
                 a low number like 20, but then increasing as more extended
                 emission is encountered.

       mask -- Specification of cleanbox(es), mask image(s), primary beam
               coverage level, and/or region(s) to be used for CLEANing.
               CLEAN tends to perform better, and is less likely to diverge,
               if the CLEAN component placement is limited by a mask to where
               real emission is expected to be.  As long as the image has the
               same shape (size), mask images (e.g. from a previous interactive
               session) can be used for a new execution.  NOTE: the initial
               clean mask actually used is the union of what is specified in mask
               and <imagename>.mask
               default: [] or '' : no masking; Possible specification types:
               (a) Cleanboxes, specified using the CASA region format
                    (http://casaguides.nrao.edu/index.php?title=CASA_Region_Format)
                    Example : mask='box [ [ 100pix , 130pix] , [120pix, 150pix ] ]'
                       mask='circle [ [ 120pix , 40pix] ,6pix ]'
                       mask='circle[[19h58m52.7s,+40d42m06.04s ], 30.0arcsec]'
                   If used with a spectral cube, it will apply to all channels.
                   Multiple regions may be specified as a list of pixel ranges.
                    Example :  mask= ['circle [ [ 120pix , 40pix] ,6pix ]', 
                                                 'box [ [ 100pix , 130pix] , [120pix, 150pix ] ]' ]
               (b) Filename with cleanbox shapes defined using the CASA region format.
                   Example: mask='mycleanbox.txt'
                     The file 'mycleanbox.txt' contains : 
                          box [ [ 100pix , 130pix ] , [ 120pix, 150pix ] ]
                          circle [ [ 150pix , 150pix] ,10pix ]
                          rotbox [ [ 60pix , 50pix ] , [ 30pix , 30pix ] , 30deg ]
               (c) Filename for image mask.  Example: mask='myimage.mask'
                   Multiple mask files may be specified.
                   example : mask=[ 'mask1.mask', 'mask2.mask' ]
               (d) Filename for region specification (e.g. from viewer).
                   Example: mask='myregion.rgn'
               (e) Combinations of the above options.
                   Example: mask=['mycleanbox.txt', 'myimage.mask',
                                  'myregion.rgn','circle [ [ 120pix , 40pix] ,6pix ]']
               (f) Threshold on primary-beam.
                   A number between 0 and 1, used as a threshhold of primary
                   beam coverage.  The primary beam coverage map (imagename +
                   '.flux(.pbcoverage)') will be made and the CLEAN component
                   placement will be limited to where it is > the number.
               (g) True or False.
                   True: like (f), but use minpb as the number.
                   False: go maskless (and expect trouble).
            (For masks for multiple fields, please see 'HINTS ON CLEAN WITH FLANKING FIELDS' below)

       uvtaper -- Apply additional uv tapering of the visibilities.
               default: uvtaper=False; example: uvtaper=True

  >>> uvtaper=True expandable parameters
               outertaper -- uv-taper on outer baselines in uv-plane
                   [bmaj, bmin, bpa] taper Gaussian scale in uv or 
                   angular units. NOTE: the on-sky FWHM in arcsec is roughly
                   the uv taper/200 (klambda).
                   default: outertaper=[]; no outer taper applied
                   example: outertaper=['5klambda']  circular taper 
                                FWHM=5 kilo-lambda
                            outertaper=['5klambda','3klambda','45.0deg']
                            outertaper=['10arcsec'] on-sky FWHM 10 arcseconds
                            outertaper=['300.0'] default units are lambda 
                                in aperture plane
               innertaper -- uv-taper in center of uv-plane
                   [bmaj,bmin,bpa] Gaussian scale at which taper falls to 
                   zero at uv=0
                   default: innertaper=[]; no inner taper applied
                   NOT YET IMPLEMENTED                
       modelimage -- Name of model image(s) to initialize cleaning. If
               multiple images, then these will be added together to
               form initial staring model NOTE: these are in addition
               to any initial model in the <imagename>.model image file
               default: '' (none); example: modelimage='orion.model'
               modelimage=['orion.model','sdorion.image'] Note: if the
               units in the image are Jy/beam as in a single-dish
               image, then it will be converted to Jy/pixel as in a
               model image, using the restoring beam in the image
               header and zeroing negatives.  If the image is in Jy/pixel then it is taken 
               as is.
                
               When nterms>1, a one-to-one mapping is done between images
               in this list and Taylor-coefficients. If more than nterms 
               images are  specified, only the first nterms are used.
               It is valid to supply fewer than nterms model images.
               Example : Supply an estimate of the continuum flux from a
                         previous imaging run. 
       weighting -- Weighting to apply to visibilities:
               default='natural'; example: weighting='uniform';
               Options: 'natural','uniform','briggs', 
                        'superuniform','briggsabs','radial'

  >>> Weighting expandable parameters
               For details on weighting please see Chapter3
               of late Dr. Brigg's thesis (http://www.aoc.nrao.edu/dissertations/dbriggs)
               For weighting='briggs' and 'briggsabs'
                   robust -- Brigg's robustness parameter
                   default=0.0; example: robust=0.5;
                   Options: -2.0 to 2.0; -2 (uniform)/+2 (natural)
               For weighting='briggsabs'
                   noise   -- noise parameter to use for Briggs "abs" 
                   weighting
                   example noise='1.0mJy'
               npixels -- uv-box used for weight calculation
                              a box going from -npixel/2 to +npixel/2 on each side
                              around a point is used to calculate weight density.
                              0 means box is pixel size
                   example npixels=2
                   Default = 0
               Exception: when choosing superuniform it does not make sense to 
               use npixels=0 as it is  uniform thus if npixels is 0  it will be forced to 6 or 
               a box from -3pixels  to 3pixels
                   
       restoringbeam -- Output Gaussian restoring beam for CLEAN image
               [bmaj, bmin, bpa] elliptical Gaussian restoring beam
               default units are in arc-seconds for bmaj,bmin, degrees
               for bpa default: restoringbeam=[]; Use PSF calculated
               from dirty beam. 
               example: restoringbeam=['10arcsec'] circular Gaussian 
                        FWHM 10 arcseconds example:
                        restoringbeam=['10.0','5.0','45.0deg'] 10"x5" 
                        at 45 degrees

       pbcor -- Output primary beam-corrected image
                If pbcor=False, the final output image is NOT corrected for
                the PB pattern (particularly important for mosaics), and
                therefore is not "flux correct". Correction can also be
                done after the  fact using immath to divide
                <imagename>.image by the <imagename>.flux image. 
                default: pbcor=False; output un-corrected image 
                example: pbcor=True; output pb-corrected image (masked outside
                         minpb) 

       minpb -- Minimum PB level to use for pb-correction and pb-based masking.
                    default=0.2;
                    example: minpb=0.01 
               When imagermode is *not* 'mosaic' :
                  minpb is applied to the flux image (sensitivity-weighted pb).
                  minpb is used to create a mask, only when pbcor=True
               When imagermode='mosaic' :
                  minpb is applied to the flux.pbcoverage image 
                        (mosaic pb with equal weight per pointing)
                   minpb is always used to create a mask (regardless of
                   pbcor=True/False) 

       usescratch -- if True will create scratch columns if they are 
               not there. And after clean completes the predicted model 
               visibility is from the clean components are written to the ms. This increases
               the ms size by the data volume. if False then the model is saved in the ms
               header and the calculation of the visibilities is done on the fly when using 
               calibration or plotms. Use True if you want to access the moedl visibilities 
               in python, say.

       allowchunk -- Partition the image cube by channel-chunks.
               default=False;  
                  False: Major cycle grids all channels.  Minor cycle steps 
                            through all channels before the next major cycle.
                  True:  Major and minor cycles are performed one chunk
                            at a time, and output images cubes are concatenated.
       async -- Run asynchronously 
               default = False; do not run asychronously


        ======================================================================

                             HINTS ON CLEAN WITH FLANKING FIELDS

              There are two ways of specifying multi-field images for clean.

              (a) Task parameters are used to define the first(main) field.
                   A text file containing definitions of all additional fields is supplied
                   to the 'outlierfile' task parameter.  

                   This outlier file must contain the following parameters per field
                     Required : imagename, imsize, phasecenter     
                     Optional : mask, modelimage
                   The parameter set for each field must begin with 'imagename'. 
                   Parameters can be listed in a single line or span multiple lines.
                    
                   Example : Three fields. 
                    
                    - Task Inputs :
                       imagename = 'M1_0'
                       outlierfile='outlier.txt'
                       imsize = [1024,1024]
                       phasecenter = 'J2000 13h27m20.98 43d26m28.0'
                   
                    - Contents of outlier file 'outlier.txt':
                       imagename = 'M1_1' 
                       imsize = [128,128]
                       phasecenter = 'J2000 13h30m52.159 43d23m08.02'
                       mask = ['out1.mask', 'circle[[40pix,40pix],5pix]' ]
                       modelimage = 'out1.model'
                       imagename = 'M1_2' 
                       imsize = [128,128]
                       phasecenter = 'J2000 13h24m08.16 43d09m48.0'
                    
                     In this example, the first field 'M1_0' is defined using
                     main task parameters. The next two 'M1_1' and 'M1_2' 
                     are listed in the file 'outlier.txt'.  A mask and modelimage 
                     has been supplied only for the second field (M1_1). Fields
                     with unspecified masks will use the full field for cleaning.


                (b) Specify all fields as lists for each task parameter :
                     
                    Parameters that support lists for multi-field specification : 
                      'imagename', 'imsize', 'phasecenter','mask','modelimage'

                    Example : Three fields (same as above)

                       imagename = ['M1_0','M1_1','M1_2]
                       imsize = [[1024,1024],[128,128],[128,128]]
                       phasecenter = ['J2000 13h27m20.98 43d26m28.0',
                                      'J2000 13h30m52.159 43d23m08.02',
                                      'J2000 13h24m08.16 43d09m48.0']
                       mask=[[''], ['out1.mask','circle[[40pix,40pix],5pix]'],['']] 
                       modelimage=[[''],['out1.model'],['']]

                     Note : All lists must have the same length.

                In the examples for both (a) and (b), the following images will be made:
                M1_0.image, M1_1.image, M1_2.image     cleaned images
                M1.0.model, M1_1.model, M1_2.model     model images
                M1.0.residual, M1_1.residual, M1_2.residual     residual images

          
             Note : The old AIPS-style outlier-file and boxfile formats have been deprecated. 
                       However, due to user-requests, they will continue be supported
                       in CASA 3.4. Note that the old outlier file format does not support 
                       the specification of modelimage and mask for each field. 
                       The new format is more complete, and less ambiguous, so please 
                       consider updating your scripts.

  
        """
        if type(multiscale)==int: multiscale=[multiscale]
        if type(imsize)==int: imsize=[imsize]
        if type(cell)==float: cell=[cell]
        if type(outertaper)==str: outertaper=[outertaper]
        if type(innertaper)==str: innertaper=[innertaper]
        if type(restoringbeam)==str: restoringbeam=[restoringbeam]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['imagename'] = imagename
        mytmp['outlierfile'] = outlierfile
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['selectdata'] = selectdata
        mytmp['timerange'] = timerange
        mytmp['uvrange'] = uvrange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['observation'] = observation
        mytmp['intent'] = intent
        mytmp['mode'] = mode
        mytmp['resmooth'] = resmooth
        mytmp['gridmode'] = gridmode
        mytmp['wprojplanes'] = wprojplanes
        mytmp['facets'] = facets
        mytmp['cfcache'] = cfcache
        mytmp['rotpainc'] = rotpainc
        mytmp['painc'] = painc
        mytmp['aterm'] = aterm
        mytmp['psterm'] = psterm
        mytmp['mterm'] = mterm
        mytmp['wbawp'] = wbawp
        mytmp['conjbeams'] = conjbeams
        mytmp['epjtable'] = epjtable
        mytmp['interpolation'] = interpolation
        mytmp['niter'] = niter
        mytmp['gain'] = gain
        if type(threshold) == str :
           mytmp['threshold'] = casac.quanta().quantity(threshold)
        else :
           mytmp['threshold'] = threshold
        mytmp['psfmode'] = psfmode
        mytmp['imagermode'] = imagermode
        mytmp['ftmachine'] = ftmachine
        mytmp['mosweight'] = mosweight
        mytmp['scaletype'] = scaletype
        mytmp['multiscale'] = multiscale
        mytmp['negcomponent'] = negcomponent
        mytmp['smallscalebias'] = smallscalebias
        mytmp['interactive'] = interactive
        mytmp['mask'] = mask
        mytmp['nchan'] = nchan
        mytmp['start'] = start
        mytmp['width'] = width
        mytmp['outframe'] = outframe
        mytmp['veltype'] = veltype
        mytmp['imsize'] = imsize
        if type(cell) == str :
           mytmp['cell'] = casac.quanta().quantity(cell)
        else :
           mytmp['cell'] = cell
        mytmp['phasecenter'] = phasecenter
        mytmp['restfreq'] = restfreq
        mytmp['stokes'] = stokes
        mytmp['weighting'] = weighting
        mytmp['robust'] = robust
        mytmp['uvtaper'] = uvtaper
        mytmp['outertaper'] = outertaper
        mytmp['innertaper'] = innertaper
        mytmp['modelimage'] = modelimage
        mytmp['restoringbeam'] = restoringbeam
        mytmp['pbcor'] = pbcor
        mytmp['minpb'] = minpb
        mytmp['usescratch'] = usescratch
        mytmp['noise'] = noise
        mytmp['npixels'] = npixels
        mytmp['npercycle'] = npercycle
        mytmp['cyclefactor'] = cyclefactor
        mytmp['cyclespeedup'] = cyclespeedup
        mytmp['nterms'] = nterms
        mytmp['reffreq'] = reffreq
        mytmp['chaniter'] = chaniter
        mytmp['flatnoise'] = flatnoise
        mytmp['allowchunk'] = allowchunk
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'clean.xml')

        casalog.origin('clean')
        if trec.has_key('clean') and casac.utils().verify(mytmp, trec['clean']) :
            result = task_clean.clean(vis, imagename, outlierfile, field, spw, selectdata, timerange, uvrange, antenna, scan, observation, intent, mode, resmooth, gridmode, wprojplanes, facets, cfcache, rotpainc, painc, aterm, psterm, mterm, wbawp, conjbeams, epjtable, interpolation, niter, gain, threshold, psfmode, imagermode, ftmachine, mosweight, scaletype, multiscale, negcomponent, smallscalebias, interactive, mask, nchan, start, width, outframe, veltype, imsize, cell, phasecenter, restfreq, stokes, weighting, robust, uvtaper, outertaper, innertaper, modelimage, restoringbeam, pbcor, minpb, usescratch, noise, npixels, npercycle, cyclefactor, cyclespeedup, nterms, reffreq, chaniter, flatnoise, allowchunk)

        else :
          result = False
        return result
