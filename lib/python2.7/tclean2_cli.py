#
# This file was generated using xslt from its XML file
#
# Copyright 2014, Associated Universities Inc., Washington DC
#
import sys
import os
import datetime
#from casac import *
import casac
import string
import time
import inspect
import numpy
from casa_stack_manip import stack_frame_find
from odict import odict
from types import *
from task_tclean2 import tclean2
class tclean2_cli_:
    __name__ = "tclean2"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (tclean2_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'selectdata':None, 'field':None, 'spw':None, 'timerange':None, 'uvrange':None, 'antenna':None, 'scan':None, 'observation':None, 'intent':None, 'datacolumn':None, 'imagename':None, 'imsize':None, 'cell':None, 'phasecenter':None, 'stokes':None, 'projection':None, 'startmodel':None, 'specmode':None, 'reffreq':None, 'nchan':None, 'start':None, 'width':None, 'outframe':None, 'veltype':None, 'restfreq':None, 'interpolation':None, 'gridder':None, 'facets':None, 'chanchunks':None, 'wprojplanes':None, 'aterm':None, 'psterm':None, 'wbawp':None, 'conjbeams':None, 'cfcache':None, 'computepastep':None, 'rotatepastep':None, 'pblimit':None, 'normtype':None, 'deconvolver':None, 'scales':None, 'nterms':None, 'scalebias':None, 'restoringbeam':None, 'outlierfile':None, 'weighting':None, 'robust':None, 'npixels':None, 'uvtaper':None, 'niter':None, 'gain':None, 'threshold':None, 'cycleniter':None, 'cyclefactor':None, 'minpsffraction':None, 'maxpsffraction':None, 'interactive':None, 'usemask':None, 'mask':None, 'pbmask':None, 'maskthreshold':None, 'maskresolution':None, 'restart':None, 'savemodel':None, 'makeimages':None, 'calcres':None, 'calcpsf':None, 'restoremodel':None, 'writepb':None, 'ranks':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, selectdata=None, field=None, spw=None, timerange=None, uvrange=None, antenna=None, scan=None, observation=None, intent=None, datacolumn=None, imagename=None, imsize=None, cell=None, phasecenter=None, stokes=None, projection=None, startmodel=None, specmode=None, reffreq=None, nchan=None, start=None, width=None, outframe=None, veltype=None, restfreq=None, interpolation=None, gridder=None, facets=None, chanchunks=None, wprojplanes=None, aterm=None, psterm=None, wbawp=None, conjbeams=None, cfcache=None, computepastep=None, rotatepastep=None, pblimit=None, normtype=None, deconvolver=None, scales=None, nterms=None, scalebias=None, restoringbeam=None, outlierfile=None, weighting=None, robust=None, npixels=None, uvtaper=None, niter=None, gain=None, threshold=None, cycleniter=None, cyclefactor=None, minpsffraction=None, maxpsffraction=None, interactive=None, usemask=None, mask=None, pbmask=None, maskthreshold=None, maskresolution=None, restart=None, savemodel=None, makeimages=None, calcres=None, calcpsf=None, restoremodel=None, writepb=None, ranks=None, ):

        """Radio Interferometric Image Reconstruction

        Detailed Description:
Form images from visibilities and reconstruct a sky model.
                This task handles continuum images and spectral line cubes,
                supports outlier fields, contains standard clean based algorithms
                along with algorithms for multi-scale and wideband image
                reconstruction, widefield imaging correcting for the w-term,
                full primary-beam imaging and joint mosaic imaging (with
                heterogeneous array support for ALMA).

        
        Arguments :
                vis: Name(s) of input visibility file(s)
                                default: none;
                                example: vis='ngc5921.ms'
                                vis=['ngc5921a.ms','ngc5921b.ms']; multiple MSes
                
                   Default Value: 

                field:  Select fields to image or mosaic.  Use field id(s) or name(s).
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

                
                   Default Value: 

                spw:  Select spectral window/channels
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

                
                   Default Value: 

                timerange: Range of time to select from data

                                default: '' (all); examples,
                                timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                                Note: if YYYY/MM/DD is missing date defaults to first
                                day in data set
                                timerange='09:14:0~09:54:0' picks 40 min on first day
                                timerange='25:00:00~27:30:00' picks 1 hr to 3 hr
                                30min on NEXT day
                                timerange='09:44:00' pick data within one integration
                                of time
                                timerange='> 10:24:00' data after this time
                                For multiple MS input, a list of timerange strings can be
                                used:
                                timerange=['09:14:0~09:54:0','> 10:24:00']
                                timerange='09:14:0~09:54:0''; apply the same timerange for
                                all input MSes

                
                   Default Value: 

                uvrange: Select data within uvrange (default unit is meters)
                                default: '' (all); example:
                                uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
                                uvrange='> 4klambda';uvranges greater than 4 kilo lambda
                                For multiple MS input, a list of uvrange strings can be
                                used:
                                uvrange=['0~1000klambda','100~1000klamda']
                                uvrange='0~1000klambda'; apply 0-1000 kilo-lambda for all
                                input MSes
                
                   Default Value: 

                antenna: Select data based on antenna/baseline

                                default: '' (all)
                                If antenna string is a non-negative integer, it is
                                assumed to be an antenna index, otherwise, it is
                                considered an antenna name.
                                antenna='5\&6'; baseline between antenna index 5 and
                                index 6.
                                antenna='VA05\&VA06'; baseline between VLA antenna 5
                                and 6.
                                antenna='5\&6;7\&8'; baselines 5-6 and 7-8
                                antenna='5'; all baselines with antenna index 5
                                antenna='05'; all baselines with antenna number 05
                                (VLA old name)
                                antenna='5,6,9'; all baselines with antennas 5,6,9
                                index number
                                For multiple MS input, a list of antenna strings can be
                                used:
                                antenna=['5','5\&6'];
                                antenna='5'; antenna index 5 for all input MSes
                                antenna='!DV14'; use all antennas except DV14

                
                   Default Value: 

                scan: Scan number range

                                default: '' (all)
                                example: scan='1~5'
                                For multiple MS input, a list of scan strings can be used:
                                scan=['0~100','10~200']
                                scan='0~100; scan ids 0-100 for all input MSes

                
                   Default Value: 

                observation: Observation ID range
                                default: '' (all)
                                example: observation='1~5'
                
                   Default Value: 

                intent: Scan Intent(s)

                                default: '' (all)
                                example: intent='TARGET_SOURCE'
                                example: intent='TARGET_SOURCE1,TARGET_SOURCE2'
                                example: intent='TARGET_POINTING*'
                
                   Default Value: 

                datacolumn: Data column to image (data or observed, corrected)
                                default:'corrected'
                                ( If 'corrected' does not exist, it will use 'data' instead )

                
                   Default Value: corrected

                imagename: Pre-name of output images

                                example : imagename='try'

                                Output images will be (a subset of) :

                                try.psf              - Point spread function
                                try.residual      - Residual image
                                try.image         - Restored image
                                try.model         - Model image (contains only flux components)
                                try.sumwt        - Single pixel image containing sum-of-weights.
                                (for natural weighting, sensitivity=1/sqrt(sumwt))

                                Widefield projection algorithms (gridder=mosaic,awproject) will
                                compute the following images too.
                                try.weight        - FT of gridded weights or the
                                un-normalized sum of PB-square (for all pointings)
                                try.pb               -  PB = sqrt(weight) normalized to a maximum of 1.0

                                For multi-term wideband imaging, all relevant images above will
                                have additional .tt0,.tt1, etc suffixes to indicate Taylor terms,
                                plus the following extra output images.
                                try.alpha            - spectral index
                                try.alpha.error   - estimate of error on spectral index
                                try.beta              - spectral curvature (if nterms \> 2)

                                Tip : Include a directory name in 'imagename' for all
                                output images to be sent there instead of the
                                current working directory : imagename='mydir/try'

                                Tip : Restarting an imaging run without changing 'imagename'
                                implies continuation from the existing model image on disk.
                                - If 'startmodel' was initially specified it needs to be set to ""
                                for the restart run (or tclean will exit with an error message).
                                - By default, the residual image and psf will be recomputed
                                but if no changes were made to relevant parameters between
                                the runs, set calcres=False, calcpsf=False to resume directly from
                                the minor cycle without the (unnecessary) first major cycle.
                                To automatically change 'imagename' with a numerical
                                increment, set restart=False (see tclean docs for 'restart').

                                Note : An imaging run with niter=0 will not produce an output restored
                                image (extension .image) since there is no .model to restore.
                                The .residual image is the (un-deconvolved or dirty) output image.

                
                   Default Value: 

                imsize: Number of pixels
                                example :  imsize = [350,250]
                                imsize = 500 is equivalent to [500,500]
                                To take proper advantage of internal optimized FFT routines, the
                                number of pixels must be even and factorizable by 2,3,5,7 only.
                
                   Default Value: 100

                cell: Cell size
                                example: cell=['0.5arcsec,'0.5arcsec'] or
                                cell=['1arcmin', '1arcmin']
                                cell = '1arcsec' is equivalent to ['1arcsec','1arcsec']
                
                   Default Value: "1arcsec"

                phasecenter: Phase center of the image (string or field id)
                                example: phasecenter=6
                                phasecenter='J2000 19h30m00 -40d00m00'
                                phasecenter='J2000 292.5deg  -40.0deg'
                                phasecenter='J2000 5.105rad  -0.698rad'
                                phasecenter='ICRS 13:05:27.2780 -049.28.04.458'
                
                   Default Value: 

                stokes: Stokes Planes to make
                                default='I'; example: stokes='IQUV';
                
                                Options: 'I','IV','QU','IQ','UV','IQUV','RR','LL','XX','YY','RRLL','XXYY'


                                Note : Due to current internal code constraints, if any correlation pair
                                is flagged, no data for that row in the MS will be used.
                                So, in an MS with XX,YY, if only YY is flagged, neither a
                                Stokes I image nor an XX image can be made. In such a
                                situation, please split out only the unflagged correlation into
                                a separate MS. This constraint shall be removed (where logical)
                                in a future release.

                                Note : Currently (due to software constraints) options for which the number
                                of correlation planes differs from the number of stokes planes are
                                not supported.  Please use appropriate combinations of stokes planes
                                until this is fixed. For example, to get Stokes Q, use 'QU' for data
                                with circular feeds and 'IQ' for data with linear feeds, or use 'IQUV'.

                
                   Default Value: I
                   Allowed Values:
                                I
                                IV
                                QU
                                IQ
                                UV
                                IQUV
                                RR
                                LL
                                XX
                                YY
                                RRLL
                                XXYY

                projection: Coordinate projection
                                Examples : SIN,   NCP
                                A list of supported (but untested) projections can be found here :
                                http://casa.nrao.edu/active/docs/doxygen/html/classcasa_1_1Projection.html#a3d5f9ec787e4eabdce57ab5edaf7c0cd

                

                
                   Default Value: SIN

                startmodel: Name of starting model image

                                The contents of the supplied starting model image will be
                                copied to the imagename.model before the run begins.

                                example : startmodel = 'singledish.im'

                                For deconvolver='mtmfs', one image per Taylor term must be provided.
                                example : startmodel = ['try.model.tt0', 'try.model.tt1']
                                startmodel = ['try.model.tt0']  will use a starting model only
                                for the zeroth order term.
                                startmodel = ['','try.model.tt1']  will use a starting model only
                                for the first order term.

                                This starting model can be of a different image shape and size from
                                what is currently being imaged. If so, an image regrid is first triggered
                                to resample the input image onto the target coordinate system.

                                A common usage is to set this parameter equal to a single dish image

                                [ Note : If an error occurs during image resampling/regridding,
                                please try using task imregrid to resample the starting model
                                image onto a CASA image with the target shape and
                                coordinate system before supplying it via startmodel ]

                
                   Default Value: 

                specmode: Spectral definition mode (mfs,cube,cubedata)

                                mode='mfs' : Continuum imaging with only one output image channel.
                                (mode='cont' can also be used here)

                                mode='cube' : Spectral line imaging with one or more channels
                                Parameters start, width,and nchan define the spectral
                                coordinate system and can be specified either in terms
                                of channel numbers, frequency or velocity in whatever
                                spectral frame is specified in 'outframe'.
                                All internal and output images are made only in the
                                LSRK frame, with automatic internal software Doppler
                                tracking. Therefore a spectral line observed over an
                                extended time range will line up appropriately.

                                (Note : If the input parameters are specified in a frame
                                other than LSRK, the viewer can be used to relabel
                                the spectral axis in that frame - via the spectral
                                reference option under axis label properties in the
                                data display options window.)

                                mode='cubedata' : Spectral line imaging with one or more channels
                                There is no internal software Doppler tracking so
                                a spectral line observed over an extended time range
                                may be smeared out in frequency. There is strictly
                                no valid spectral frame with which to label the ouput
                                images, but they will list the frame defined in the MS.


                
                   Default Value: mfs
                   Allowed Values:
                                mfs
                                cont
                                cube
                                cubedata

                reffreq: Reference frequency of the output image coordinate system

                                Example :  reffreq='1.5GHz'    as a string with units.

                                By default, it is calculated as the middle of the selected frequency range.

                                For deconvolver='mtmfs' the Taylor expansion is also done about
                                this specified reference frequency.

                
                   Default Value: 

                nchan: Number of channels in the output image
                                For default (=-1), the number of channels will be automatically determined
                                based on data selected by 'spw' with 'start' and 'width'.
                                It is often easiest to leave nchan at the default value.
                                example: nchan=100

                
                   Default Value: -1

                start: First channel (e.g. start=3,start=\'1.1GHz\',start=\'15343km/s\')
                                of output cube images specified by data channel number (integer),
                                velocity (string with a unit),  or frequency (string with a unit).
                                Default:''; The first channel is automatically determined based on
                                the 'spw' channel selection and 'width'.
                                When the channel number is used along with the channel selection
                                in 'spw' (e.g. spw='0:6~100'),
                                'start' channel number is RELATIVE (zero-based) to the selected
                                channels in 'spw'. So for the above example,
                                start=1 means that the first image channel is the second selected
                                data channel, which is channel 7.
                                For specmode='cube', when velocity or frequency is used it is
                                interpreted with the frame defined in outframe. [The parameters of
                                the desired output cube can be estimated by using the 'transform'
                                functionality of 'plotms']
                                examples: start='5.0km/s'; 1st channel, 5.0km/s in outframe
                                start='22.3GHz'; 1st channel, 22.3GHz in outframe
                
                   Default Value: 

                width: Channel width (e.g. width=2,width=\'0.1MHz\',width=\'10km/s\') of output cube images
                                specified by data channel number (ingeter), velocity (string with a unit), or
                                or frequency (string with a unit).
                                Default:''; data channel width
                                The sign of width defines the direction of the channels to be incremented.
                                For width specified in velocity or frequency with '-' in front  gives image channels in
                                decreasing velocity or frequency, respectively.
                                For specmode='cube', when velocity or frequency is used it is interpreted with
                                the reference frame defined in outframe.
                                examples: width='2.0km/s'; results in channels with incresing velocity
                                width='-2.0km/s';  results in channels with decreasing velocity
                                width='40kHz'; results in channels with increasing frequency
                                width=-2; results in channels averaged of 2 data channels incremented from
                                high to low channel numbers

                
                   Default Value: 

                outframe: Spectral reference frame in which to interpret \'start\' and \'width\'
                                Options: '','LSRK','LSRD','BARY','GEO','TOPO','GALACTO','LGROUP','CMB'
                                example: outframe='bary' for Barycentric frame

                                REST -- Rest frequency
                                LSRD -- Local Standard of Rest (J2000)
                                -- as the dynamical definition (IAU, [9,12,7] km/s in galactic coordinates)
                                LSRK -- LSR as a kinematical (radio) definition
                                -- 20.0 km/s in direction ra,dec = [270,+30] deg (B1900.0)
                                BARY -- Barycentric (J2000)
                                GEO --- Geocentric
                                TOPO -- Topocentric
                                GALACTO -- Galacto centric (with rotation of 220 km/s in direction l,b = [90,0] deg.
                                LGROUP -- Local group velocity -- 308km/s towards l,b = [105,-7] deg (F. Ghigo)
                                CMB -- CMB velocity -- 369.5km/s towards l,b = [264.4, 48.4] deg (F. Ghigo)
                                DEFAULT = LSRK

                
                   Default Value: LSRK

                veltype: Velocity type (radio, z, ratio, beta, gamma, optical)
                                For start and/or width specified in velocity, specifies the velocity definition
                                Options: 'radio','optical','z','beta','gamma','optical'
                                NOTE: the viewer always defaults to displaying the 'radio' frame,
                                but that can be changed in the position tracking pull down.

                                The different types (with F = f/f0, the frequency ratio), are:

                                Z = (-1 + 1/F)
                                RATIO = (F) *
                                RADIO = (1 - F)
                                OPTICAL == Z
                                BETA = ((1 - F2)/(1 + F2))
                                GAMMA = ((1 + F2)/2F) *
                                RELATIVISTIC == BETA (== v/c)
                                DEFAULT == RADIO
                                Note that the ones with an '*' have no real interpretation
                                (although the calculation will proceed) if given as a velocity.

                
                   Default Value: radio

                restfreq: List of rest frequencies or a rest frequency in a string.
                                Specify rest frequency to use for output image.
                                *Currently it uses the first rest frequency in the list for translation of
                                velocities. The list will be stored in the output images.
                                Default: []; look for the rest frequency stored in the MS, if not available,
                                use center frequency of the selected channels
                                examples: restfreq=['1.42GHz']
                                restfreq='1.42GHz'

                
                   Default Value: 

                interpolation: Spectral interpolation (nearest,linear,cubic)

                                Interpolation rules to use when binning data channels onto image channels
                                and evaluating visibility values at the centers of image channels.

                                Note : 'linear' and 'cubic' interpolation requires data points on both sides of
                                each image frequency. Errors  are therefore possible at edge  channels, or near
                                flagged data channels. When image channel width is much larger than the data
                                channel width there is nothing much to be gained using linear or cubic thus
                                not worth the extra computation involved.


                
                   Default Value: linear
                   Allowed Values:
                                nearest
                                linear
                                cubic

                gridder: Gridding options (standard, wproject, widefield, mosaic, awproject)

                                The following options choose different gridding convolution
                                functions for the process of convolutional resampling of the measured
                                visibilities onto a regular uv-grid prior to an inverse FFT.
                                Model prediction (degridding) also uses these same functions.
                                Several wide-field effects can be accounted for via careful choices of
                                convolution functions. Gridding (degridding) runtime will rise in
                                proportion to the support size of these convolution functions (in uv-pixels).

                                standard : Prolate Spheroid with 3x3 uv pixel support size

                                [ This mode can also be invoked using 'ft' or 'gridft' ]

                                wproject : W-Projection algorithm to correct for the widefield
                                non-coplanar baseline effect. [Cornwell et.al 2008]

                                wprojplanes is the number of distinct w-values at
                                which to compute and use different gridding convolution
                                functions (see help for wprojplanes).
                                Convolution function support size can range
                                from 5x5 to few 100 x few 100.

                                [ This mode can also be invoked using 'wprojectft' ]

                                widefield : Facetted imaging with or without W-Projection per facet.

                                A set of facets x facets subregions of the specified image
                                are gridded separately using their respective phase centers
                                (to minimize max W). Deconvolution is done on the joint
                                full size image, using a PSF from the first subregion.

                                wprojplanes=1 : standard prolate spheroid gridder per facet.
                                wprojplanes > 1 : W-Projection gridder per facet.
                                nfacets=1, wprojplanes > 1 : Pure W-Projection and no facetting
                                nfacets=1, wprojplanes=1 : Same as standard,ft,gridft

                                A combination of facetting and W-Projection is relevant only for
                                very large fields of view.

                                mosaic : A-Projection with azimuthally symmetric beams without
                                sidelobes, beam rotation or squint correction.
                                Gridding convolution functions per visibility are computed
                                from FTs of PB models per antenna.
                                This gridder can be run on single fields as well as mosaics.

                                VLA : PB polynomial fit model (Napier and Rots, 1982)
                                ALMA : Airy disks for a 10.7m dish (for 12m dishes) and
                                6.25m dish (for 7m dishes) each with 0.75m
                                blockages (Hunter/Brogan 2011). Joint mosaic
                                imaging supports heterogeneous arrays for ALMA.

                                Typical gridding convolution function support sizes are
                                between 7 and 50 depending on the desired
                                accuracy (given by the uv cell size or image field of view).

                                [ This mode can also be invoked using 'mosaicft' or 'ftmosaic' ]

                                awproject : A-Projection with azimuthally asymmetric beams and
                                including beam rotation, squint correction,
                                conjugate frequency beams and W-projection.
                                [Bhatnagar et.al, 2008]

                                Gridding convolution functions are computed from
                                aperture illumination models per antenna and optionally
                                combined with W-Projection kernels and a prolate spheroid.
                                This gridder can be run on single fields as well as mosaics.

                                VLA : Uses ray traced model (VLA and EVLA) including feed
                                leg and subreflector shadows, off-axis feed location
                                (for beam squint and other polarization effects), and
                                a Gaussian fit for the feed beams (Ref: Brisken 2009)
                                ALMA : Similar ray-traced model as above (but the correctness
                                of its polarization properties remains un-verified).

                                Typical gridding convolution function support sizes are
                                between 7 and 50 depending on the desired
                                accuracy (given by the uv cell size or image field of view).
                                When combined with W-Projection they can be significantly larger.

                                [ This mode can also be invoked using 'awprojectft' ]

                                imagemosaic : (untested implementation)
                                Grid and iFT each pointing separately and combine the
                                images as a linear mosaic (weighted by a PB model) in
                                the image domain before a joint minor cycle.

                                VLA/ALMA PB models are same as for gridder='mosaicft'

                                ------ Notes on PB models :

                                (1) Several different sources of PB models are used in the modes
                                listed above. This is partly for reasons of algorithmic flexibility
                                and partly due to the current  lack of a common beam model
                                repository or consensus on what beam models are most appropriate.

                                (2) For ALMA and gridder='mosaic', ray-traced (TICRA) beams
                                are also available via the vpmanager tool.
                                For example, call the following before the tclean run.
                                vp.setpbimage(telescope="ALMA",
                                compleximage='/home/casa/data/trunk/alma/responses/ALMA_0_DV__0_0_360_0_45_90_348.5_373_373_GHz_ticra2007_VP.im',
                                antnames=['DV'+'%02d'%k for k in range(25)])
                                ( Currently this will work only for non-parallel runs )


                                ------ Note on PB masks :

                                In tclean, A-Projection gridders (mosaic and awproject) produce a
                                .pb image and use the 'pblimit' subparameter to decide normalization
                                cutoffs and construct an internal T/F mask in the .pb and .image images.
                                However, this T/F mask cannot directly be used during deconvolution
                                (which needs a 1/0 mask). There are two options for making a pb based
                                deconvolution mask.
                                -- Run tclean with niter=0 to produce the .pb, construct a 1/0 image
                                with the desired threshold (using ia.open('newmask.im');
                                ia.calc('iif("xxx.pb">0.3,1.0,0.0)');ia.close() for example),
                                and supply it via the 'mask' parameter in a subsequent run
                                (with calcres=F and calcpsf=F to restart directly from the minor cycle).
                                -- Run tclean with usemask='pb' for it to automatically construct
                                a 1/0 mask from the internal T/F mask from .pb at a fixed 0.2 threshold.

                                ----- Note on making PBs for gridders other than mosaic,awproject

                                For now, to construct a .pb image with gridders other than
                                mosaic and awproject please use the following script based
                                on the old imager tool.

                                from recipes import makepb
                                makepb.makePB(vis='xxx.ms',field='0~5',
                                imtemplate='template.im',
                                outimage='try.pb', pblimit=0.2)

                                ( where template.im is any output image from the tclean run
                                for which .pb is to be made. The coordinate system to use for
                                .pb is picked from this template image )

                                Here too, to use a pb-level mask for deconvolution, run tclean with
                                niter=0, make the .pb image using the above recipe script (with its
                                internal T/F mask set at pblimit) and then either make a 1/0 mask
                                image at whatever desired pb level and supply it via 'mask' or set
                                usemask='pb' to automatically construct a 1/0 mask at the 0.2 level.

            
                   Default Value: standard
                   Allowed Values:
                                standard
                                ft
                                gridft
                                widefield
                                wproject
                                wprojectft
                                mosaic
                                ftmosaic
                                mosaicft
                                imagemosaic
                                awproject
                                awprojectft

                facets: Number of facets on a side

                        A set of (facets x facets) subregions of the specified image
                        are gridded separately using their respective phase centers
                        (to minimize max W). Deconvolution is done on the joint
                        full size image, using a PSF from the first subregion/facet.

            
                   Default Value: 1

                chanchunks: Number of channel chunks to grid separately

                        For large image cubes, the gridders can run into memory limits
                        as they loop over all available image planes for each row of data
                        accessed. To prevent this problem, we can grid subsets of channels
                        in sequence so that at any given time only part of the image cube
                        needs to be loaded into memory. This parameter controls the
                        number of chunks to split the cube into.

                        Example :  chanchunks = 4

                        [ This feature is experimental and may have restrictions on how
                        chanchunks is to be chosen. For now, please pick chanchunks so
                        that nchan/chanchunks is an integer. ]

            
                   Default Value: 1

                wprojplanes: Number of distinct w-values at which to compute and use different
                        gridding convolution functions for W-Projection

                        An appropriate value of wprojplanes depends on the presence/absence
                        of a bright source far from the phase center, the desired dynamic
                        range of an image in the presence of a bright far out source,
                        the maximum w-value in the measurements, and the desired trade off
                        between accuracy and computing cost.

                        As a (rough) guide, VLA L-Band D-config may require a
                        value of 128 for a source 30arcmin away from the phase
                        center. A-config may require 1024 or more. To converge to an
                        appropriate value, try starting with 128 and then increasing
                        it if artifacts persist. W-term artifacts (for the VLA) typically look
                        like arc-shaped smears in a synthesis image or a shift in source
                        position between images made at different times. These artifacts
                        are more pronounced the further the source is from the phase center.

                        There is no harm in simply always choosing a large value (say, 1024)
                        but there will be a significant performance cost to doing so, especially
                        for gridder='awproject' where it is combined with A-Projection.

                        wprojplanes=-1 is an option for gridder='widefield' or 'wproject'
                        in which the number of planes is automatically computed.

            
                   Default Value: 1

                aterm: Use aperture illumination functions during gridding

                        This parameter turns on the A-term of the AW-Projection gridder.
                        Gridding convolution functions are constructed from aperture illumination
                        function models of each antenna.

            
                   Default Value: True

                psterm: Use prolate spheroidal during gridding
                   Default Value: False

                wbawp: Use frequency dependent A-terms
                        Scale aperture illumination functions appropriately with frequency
                        when gridding and combining data from multiple channels.
            
                   Default Value: True

                conjbeams: Use conjugate frequency for wideband A-terms

                        While gridding data from one frequency channel, choose a
                        convolution function from a 'conjugate' frequency such that
                        the resulting baseline primary beam is approximately constant
                        across frequency. For a system in which the primary beam scales
                        with frequency, this step will eliminate instrumental spectral
                        structure from the measured data and leave only the sky spectrum
                        for the minor cycle to model and reconstruct [Bhatnagar et.al,2013].

                        As a rough guideline for when this is relevant, a source at the half
                        power point of the PB at the center frequency will see an artificial
                        spectral index of -1.4 due to the frequency dependence of the PB
                        [Sault and Wieringa, 1994].  If left uncorrected during gridding, this
                        spectral structure must be modeled in the minor cycle (using the
                        mtmfs algorithm) to avoid dynamic range limits (of a few hundred
                        for a 2:1 bandwidth).

            
                   Default Value: True

                cfcache: Convolution function cache directory name

                        Name of a directory in which to store gridding convolution functions.
                        This cache is filled at the beginning of an imaging run. This step can be time
                        consuming but the cache can be reused across multiple imaging runs that
                        use the same image parameters (cell size, field-of-view, spectral data
                        selections, etc).

                        By default, cfcache = imagename + '.cf'

            
                   Default Value: 

                computepastep: At what parallactic angle interval to recompute aperture
                        illumination functions (deg)

                        This parameter controls the accuracy of the aperture illumination function
                        used with AProjection for alt-az mount dishes where the AIF rotates on the
                        sky as the synthesis image is built up.

            
                   Default Value: 360.0

                rotatepastep: At what parallactic angle interval to rotate nearest
                        aperture illumination function (deg)

                        Instead of recomputing the AIF for every timestep's parallactic angle,
                        the nearest existing AIF is picked and rotated in steps of this amount.

                        For example, computepastep=360.0 and rotatepastep=5.0 will compute
                        the AIFs at only the starting parallactic angle and all other timesteps will
                        use a rotated version of that AIF at the nearest 5.0 degree point.

            
                   Default Value: 360.0

                pblimit: PB gain level at which to cut off normalizations

                        Divisions by .pb during normalizations have a cut off at a .pb gain
                        level given by pblimit. Outside this limit, image values are set to zero.
                        Additionally, an internal T/F mask is applied to the .pb, .image and
                        .residual images to mask out (T) all invalid pixels outside the pblimit area.

                        Note : This internal T/F mask cannot be used as a deconvolution mask.
                        To do so, please follow the steps listed above in the Notes for the
                        'gridder' parameter.

            
                   Default Value: 0.2

                normtype: Normalization type (flatnoise, flatsky)

                        Gridded (and FT'd) images represent the PB-weighted sky image.
                        Qualitatively it can be approximated as two instances of the PB
                        applied to the sky image (one naturally present in the data
                        and one introduced during gridding via the convolution functions).

                        xxx.weight : Weight image approximately equal to sum ( square ( pb ) )
                        xxx.pb : Primary beam calculated as  sqrt ( xxx.weight )

                        normtype='flatnoise' : Divide the raw image by sqrt(.weight) so that
                        the input to the minor cycle represents the
                        product of the sky and PB. The noise is 'flat'
                        across the region covered by each PB.

                        normtype='flatsky' : Divide the raw image by .weight so that the input
                        to the minor cycle represents only the sky.
                        The noise is higher in the outer regions of the
                        primary beam where the sensitivity is low.

                        normtype='pbsquare' : No normalization after gridding and FFT.
                        The minor cycle sees the sky times pb square
                        [not yet implemented]

            
                   Default Value: flatnoise

                deconvolver: Name of minor cycle algorithm (hogbom,clark,multiscale,mtmfs,mem,clarkstokes)

                        Each of the following algorithms operate on residual images and psfs
                        from the gridder and produce output model and restored images.
                        Minor cycles stop and a major cycle is triggered when cyclethreshold
                        or cycleniter are reached. For all methods, components are picked from
                        the entire extent of the image or (if specified) within a mask.

                        hogbom : An adapted version of Hogbom Clean [Hogbom, 1974]
                        - Find the location of the peak residual
                        - Add this delta function component to the model image
                        - Subtract a scaled and shifted PSF of the same size as the image
                        from regions of the residual image where the two overlap.
                        - Repeat

                        clark : An adapted version of Clark Clean [Clark, 1980]
                        - Find the location of max(I^2+Q^2+U^2+V^2)
                        - Add delta functions to each stokes plane of the model image
                        - Subtract a scaled and shifted PSF within a small patch size
                        from regions of the residual image where the two overlap.
                        - After several iterations trigger a Clark major cycle to subtract
                        components from the visibility domain, but without de-gridding.
                        - Repeat

                        ( Note : 'clark' maps to imagermode='' in the old clean task.
                        'clark_exp' is another implementation that maps to
                        imagermode='mosaic' or 'csclean' in the old clean task
                        but the behaviour is not identical. For now, please
                        use deconvolver='hogbom' if you encounter problems. )

                        clarkstokes : Clark Clean operating separately per Stokes plane

                        (Note : 'clarkstokes_exp' is an alternate version. See above.)

                        multiscale : MultiScale Clean [Cornwell, 2008]
                        - Smooth the residual image to multiple scale sizes
                        - Find the location and scale at which the peak occurs
                        - Add this multiscale component to the model image
                        - Subtract a scaled,smoothed,shifted PSF (within a small
                        patch size per scale) from all residual images
                        - Repeat from step 2

                        mtmfs : Multi-term (Multi Scale) Multi-Frequency Synthesis [Rau and Cornwell, 2011]
                        - Smooth each Taylor residual image to multiple scale sizes
                        - Solve a NTxNT system of equations per scale size to compute
                        Taylor coefficients for components at all locations
                        - Compute gradient chi-square and pick the Taylor coefficients
                        and scale size at the location with maximum reduction in
                        chi-square
                        - Add multi-scale components to each Taylor-coefficient
                        model image
                        - Subtract scaled,smoothed,shifted PSF (within a small patch size
                        per scale) from all smoothed Taylor residual images
                        - Repeat from step 2


                        mem : Maximum Entropy Method [Cornwell and Evans, 1985]
                        - Iteratively solve for values at all individual pixels via the
                        MEM method. It minimizes an objective function of
                        chi-square plus entropy (here, a measure of difference
                        between the current model and a flat prior model).

                        (Note : This MEM implementation is not very robust.
                        Improvements will be made in the future.)



            
                   Default Value: hogbom
                   Allowed Values:
                                hogbom
                                clark
                                clarkstokes
                                clark_exp
                                clarkstokes_exp
                                multiscale
                                mtmfs
                                mem

                scales: List of scale sizes (in pixels) for multi-scale and mtmfs algorithms.
                        -->  scales=[0,6,20]
                        This set of scale sizes should represent the sizes
                        (diameters in units of number of pixels)
                        of dominant features in the image being reconstructed.

                        The smallest scale size is recommended to be 0 (point source),
                        the second the size of the synthesized beam and the third 3-5
                        times the synthesized beam, etc. For example, if the synthesized
                        beam is 10" FWHM and cell=2",try scales = [0,5,15].

                        For numerical stability, the largest scale must be
                        smaller than the image (or mask) size and smaller than or
                        comparable to the scale corresponding to the lowest measured
                        spatial frequency (as a scale size much larger than what the
                        instrument is sensitive to is unconstrained by the data making
                        it harder to recovery from errors during the minor cycle).
            
                   Default Value: 

                nterms: Number of Taylor coefficients in the spectral model

                        - nterms=1 : Assume flat spectrum source
                        - nterms=2 : Spectrum is a straight line with a slope
                        - nterms=N : A polynomial of order N-1

                        From a Taylor expansion of the expression of a power law, the
                        spectral index is derived as alpha = taylorcoeff_1 / taylorcoeff_0

                        Spectral curvature is similarly derived when possible.

                        The optimal number of Taylor terms depends on the available
                        signal to noise ratio, bandwidth ratio, and spectral shape of the
                        source as seen by the telescope (sky spectrum x PB spectrum).

                        nterms=2 is a good starting point for wideband EVLA imaging
                        and the lower frequency bands of ALMA (when fractional bandwidth
                        is greater than 10%) and if there is at least one bright source for
                        which a dynamic range of greater than few 100 is desired.

                        Spectral artifacts for the VLA often look like spokes radiating out from
                        a bright source (i.e. in the image made with standard mfs imaging).
                        If increasing the number of terms does not eliminate these artifacts,
                        check the data for inadequate bandpass calibration. If the source is away
                        from the pointing center, consider including wide-field corrections too.

                        (Note : In addition to output Taylor coefficient images .tt0,.tt1,etc
                        images of spectral index (.alpha), an estimate of error on
                        spectral index (.alpha.error) and spectral curvature (.beta,
                        if nterms is greater than 2) are produced.
                        - These alpha, alpha.error and beta images contain
                        internal T/F masks based on a threshold computed
                        as peakresidual/10. Additional masking based on
                        .alpha/.alpha.error may be desirable.
                        - .alpha.error is a purely empirical estimate derived
                        from the propagation of error during the division of
                        two noisy numbers (alpha = xx.tt1/xx.tt0) where the
                        'error' on tt1 and tt0 are simply the values picked from
                        the corresponding residual images. The absolute value
                        of the error is not always accurate and it is best to intepret
                        the errors across the image only in a relative sense.)


            
                   Default Value: 2

                scalebias: A numerical control to bias the solution towards smaller scales.

                        The peak from each scale's smoothed residual is
                        multiplied by ( 1 - smallscalebias * scale/maxscale )
                        to increase or decrease the amplitude relative to other scales,
                        before the scale with the largest peak is chosen.

                        smallscalebias=0.6 (default) applies a slight bias towards small
                        scales, ranging from 1.0 for a point source to
                        0.4 for the largest scale size

                        Values larger than 0.6 will bias the solution towards smaller scales.
                        Values smaller than 0.6 will tend towards giving all scales equal weight.

            
                   Default Value: 0.6

                restoringbeam:  Restoring beam shape/size to use.

                        - restoringbeam='' or ['']
                        A Guassian fitted to the PSF main lobe (separately per image plane).

                        - restoringbeam='10.0arcsec'
                        Use a circular Gaussian of this width for all planes

                        - restoringbeam=['8.0arcsec','10.0arcsec','45deg']
                        Use this elliptical Gaussisn for all planes

                        - restoringbeam='common'
                        Automatically estimate a common beam shape/size appropriate for
                        all planes.

                        Note : For any restoring beam different from the native resolution
                        the model image is convolved with the beam and added to
                        residuals that have been convolved to the same target resolution.

            
                   Default Value: 

                outlierfile: Name of outlier-field image definitions

                        A text file containing sets of parameter=value pairs,
                        one set per outlier field.

                        Example :   outlierfile='outs.txt'

                        Contents of outs.txt :

                        imagename=tst1
                        nchan=1
                        imsize=[80,80]
                        cell=[8.0arcsec,8.0arcsec]
                        phasecenter=J2000 19:58:40.895 +40.55.58.543
                        mask=circle[[40pix,40pix],10pix]

                        imagename=tst2
                        nchan=1
                        imsize=[100,100]
                        cell=[8.0arcsec,8.0arcsec]
                        phasecenter=J2000 19:58:40.895 +40.56.00.000
                        mask=circle[[60pix,60pix],20pix]

                        The following parameters are currently allowed to be different between
                        the main field and the outlier fields (i.e. they will be recognized if found
                        in the outlier text file). If a parameter is not listed, the value is picked from
                        what is defined in the main task input.

                        imagename, imsize, cell, phasecenter, startmodel, mask
                        specmode, nchan, start, width, nterms, reffreq,
                        gridder, deconvolver, wprojplanes

                        Note : 'specmode' is an option, so combinations of mfs and cube
                        for different image fields, for example, are supported.
                        'deconvolver' and 'gridder' are also options that allow different
                        imaging or deconvolution algorithm per image field.

                        For example, multiscale with wprojection and 16 w-term planes
                        on the main field and mtmfs with nterms=3 and wprojection
                        with 64 planes on a bright outlier source for which the frequency
                        dependence of the primary beam produces a strong effect that
                        must be modeled.   The traditional alternative to this approach is
                        to first image the outlier, subtract it out of the data (uvsub) and
                        then image the main field.

                        Note : If you encounter a use-case where some other parameter needs
                        to be allowed in the outlier file (and it is logical to do so), please
                        send us feedback. The above is an initial list.

            
                   Default Value: 

                weighting: Weighting scheme (natural,uniform,briggs,superuniform,radial)

                        During gridding of the dirty or residual image, each visibility value is
                        multiplied by a weight before it is accumulated on the uv-grid.
                        The PSF's uv-grid is generated by gridding only the weights (weightgrid).

                        weighting='natural' : Gridding weights are identical to the data weights
                        from the MS. For visibilities with similar data weights,
                        the weightgrid will follow the sample density
                        pattern on the uv-plane. This weighting scheme
                        provides the maximum imaging sensitivity at the
                        expense of a possibly fat PSF with high sidelobes.
                        It is most appropriate for detection experiments
                        where sensitivity is most important.

                        weighting='uniform' : Gridding weights per visibility data point are the
                        original data weights divided by the total weight of
                        all data points that map to the same uv grid cell :
                        ' data_weight / total_wt_per_cell '.

                        The weightgrid is as close to flat as possible resulting
                        in a PSF with a narrow main lobe and suppressed
                        sidelobes. However, since heavily sampled areas of
                        the uv-plane get down-weighted, the imaging
                        sensitivity is not as high as with natural weighting.
                        It is most appropriate for imaging experiments where
                        a well behaved PSF can help the reconstruction.

                        weighting='briggs' :  Gridding weights per visibility data point are given by
                        'data_weight / ( A / total_wt_per_cell + B ) ' where
                        A and B vary according to the 'robust' parameter.

                        robust = -2.0 maps to A=1,B=0 or uniform weighting.
                        robust = +2.0 maps to natural weighting.
                        (robust=0.5 is equivalent to robust=0.0 in AIPS IMAGR.)

                        Robust/Briggs weighting generates a PSF that can
                        vary smoothly between 'natural' and 'uniform' and
                        allow customized trade-offs between PSF shape and
                        imaging sensitivity.

                        weighting='superuniform' : This is similar to uniform weighting except that
                        the total_wt_per_cell is replaced by the
                        total_wt_within_NxN_cells around the uv cell of
                        interest.  ( N = subparameter 'npixels' )

                        This method tends to give a PSF with inner
                        sidelobes that are suppressed as in uniform
                        weighting but with far-out sidelobes closer to
                        natural weighting. The peak sensitivity is also
                        closer to natural weighting.

                        weighting='radial' : Gridding weights are given by ' data_weight * uvdistance '

                        This method approximately minimizes rms sidelobes
                        for an east-west synthesis array.

                        For more details on weighting please see Chapter3
                        of Dan Briggs' thesis (http://www.aoc.nrao.edu/dissertations/dbriggs)

            
                   Default Value: natural

                robust: Robustness parameter for Briggs weighting.

                        robust = -2.0 maps to uniform weighting.
                        robust = +2.0 maps to natural weighting.
                        (robust=0.5 is equivalent to robust=0.0 in AIPS IMAGR.)

            
                   Default Value: 0.5

                npixels: Number of pixels to determine uv-cell size for super-uniform weighting
                        (0 defaults to -/+ 3 pixels)

                        npixels -- uv-box used for weight calculation
                        a box going from -npixel/2 to +npixel/2 on each side
                        around a point is used to calculate weight density.

                        npixels=2 goes from -1 to +1 and covers 3 pixels on a side.

                        npixels=0 implies a single pixel, which does not make sense for
                        superuniform weighting. Therefore, if npixels=0 it will
                        be forced to 6 (or a box of -3pixels to +3pixels) to cover
                        7 pixels on a side.

            
                   Default Value: 0

                uvtaper: uv-taper on outer baselines in uv-plane

                        Apply a Gaussian taper in addition to the weighting scheme specified
                        via the 'weighting' parameter. Higher spatial frequencies are weighted
                        down relative to lower spatial frequencies to suppress artifacts
                        arising from poorly sampled areas of the uv-plane. It is equivalent to
                        smoothing the PSF obtained by other weighting schemes and can be
                        specified either as a Gaussian in uv-space (eg. units of lambda)
                        or as a Gaussian in the image domain (eg. angular units like arcsec).

                        uvtaper = [bmaj, bmin, bpa]

                        NOTE: the on-sky FWHM in arcsec is roughly  the uv taper/200 (klambda).
                        default: outertaper=[]; no outer taper applied
                        example: outertaper=['5klambda']  circular taper
                        FWHM=5 kilo-lambda
                        outertaper=['5klambda','3klambda','45.0deg']
                        outertaper=['10arcsec'] on-sky FWHM 10 arcseconds
                        outertaper=['300.0'] default units are lambda
                        in aperture plane

            
                   Default Value: 
                
            

                niter: Maximum number of iterations

                        A stopping criterion based on total iteration count.

                        Iterations are typically defined as the selecting one flux component
                        and partially subtracting it out from the residual image.

                        niter=0 : Do only the initial major cycle (make dirty image, psf, pb, etc)

                        niter larger than zero : Run major and minor cycles.

                        Note : Global stopping criteria vs major-cycle triggers

                        In addition to global stopping criteria, the following rules are
                        used to determine when to terminate a set of minor cycle iterations
                        and trigger major cycles [derived from Cotton-Schwab Clean, 1984]

                        'cycleniter' : controls the maximum number of iterations per image
                        plane before triggering a major cycle.
                        'cyclethreshold' : Automatically computed threshold related to the
                        max sidelobe level of the PSF and peak residual.

                        The first criterion to be satisfied takes precedence.

                        Note :  Iteration counts for cubes or multi-field images :
                        For images with multiple planes (or image fields) on which the
                        deconvolver operates in sequence, iterations are counted across
                        all planes (or image fields). The iteration count is compared with
                        'niter' only after all channels/planes/fields have completed their
                        minor cycles and exited either due to 'cycleniter' or 'cyclethreshold'.
                        Therefore, the actual number of iterations reported in the logger
                        can sometimes be larger than the user specified value in 'niter'.
                        For example, with niter=100, cycleniter=20,nchan=10,threshold=0,
                        a total of 200 iterations will be done in the first set of minor cycles
                        before the total is compared with niter=100 and it exits.


            
                   Default Value: 0

                gain: Loop gain

                        Fraction of the source flux to subtract out of the residual image
                        for the CLEAN algorithm and its variants.

                        A low value (0.2 or less) is recommended when the sky brightness
                        distribution is not well represented by the basis functions used by
                        the chosen deconvolution algorithm. A higher value can be tried when
                        there is a good match between the true sky brightness structure and
                        the basis function shapes.  For example, for extended emisison,
                        multiscale clean with an appropriate set of scale sizes will tolerate
                        a higher loop gain than Clark clean (for example).

            

            
                   Default Value: 0.1

                threshold: Stopping threshold (number in units of Jy, or string)

                        A global stopping threshold that the peak residual (within clean mask)
                        across all image planes is compared to.

                        threshold = 0.005  : 5mJy
                        threshold = '5.0mJy'

                        Note : A 'cyclethreshold' is internally computed and used as a major cycle
                        trigger. It is related what fraction of the PSF can be reliably
                        used during minor cycle updates of the residual image. By default
                        the minor cycle iterations terminate once the peak residual reaches
                        the first sidelobe level of the brightest source.

                        'cyclethreshold' is computed as follows using the settings in
                        parameters 'cyclefactor','minpsffraction','maxpsffraction','threshold' :

                        psf_fraction = max_psf_sidelobe_level * 'cyclefactor'
                        psf_fraction = max(psf_fraction, 'minpsffraction');
                        psf_fraction = min(psf_fraction, 'maxpsffraction');
                        cyclethreshold = peak_residual * psf_fraction
                        cyclethreshold = max( cyclethreshold, 'threshold' )

                        'cyclethreshold' is made visible and editable only in the
                        interactive GUI when tclean is run with interactive=True.
            
                   Default Value: 0.0

                cycleniter: Maximum number of minor-cycle iterations (per plane) before triggering
                        a major cycle

                        For example, for a single plane image, if niter=100 and cycleniter=20,
                        there will be 5 major cycles after the initial one (assuming there is no
                        threshold based stopping criterion). At each major cycle boundary, if
                        the number of iterations left over (to reach niter) is less than cycleniter,
                        it is set to the difference.

                        Note : cycleniter applies per image plane, even if cycleniter x nplanes
                        gives a total number of iterations greater than 'niter'. This is to
                        preserve consistency across image planes within one set of minor
                        cycle iterations.

            
                   Default Value: -1

                cyclefactor: Scaling on PSF sidelobe level to compute the minor-cycle stopping threshold.

                        Please refer to the Note under the documentation for 'threshold' that
                        discussed the calculation of 'cyclethreshold'

                        cyclefactor=1.0 results in a cyclethreshold at the first sidelobe level of
                        the brightest source in the residual image before the minor cycle starts.

                        cyclefactor=0.5 allows the minor cycle to go deeper.
                        cyclefactor=2.0 triggers a major cycle sooner.

            
                   Default Value: 1.0

                minpsffraction: PSF fraction that marks the max depth of cleaning in the minor cycle

                        Please refer to the Note under the documentation for 'threshold' that
                        discussed the calculation of 'cyclethreshold'

                        For example, minpsffraction=0.5 will stop cleaning at half the height of
                        the peak residual and trigger a major cycle earlier.

            
                   Default Value: 0.05

                maxpsffraction: PSF fraction that marks the minimum depth of cleaning in the minor cycle

                        Please refer to the Note under the documentation for 'threshold' that
                        discussed the calculation of 'cyclethreshold'

                        For example, maxpsffraction=0.8 will ensure that at least the top 20
                        percent of the source will be subtracted out in the minor cycle even if
                        the first PSF sidelobe is at the 0.9 level (an extreme example), or if the
                        cyclefactor is set too high for anything to get cleaned.

            
                   Default Value: 0.8

                interactive: Modify masks and parameters at runtime

                        interactive=True will trigger an interactive GUI at every major cycle
                        boundary (after the major cycle and before the minor cycle).

                        Options for runtime parameter modification are :

                        Interactive clean mask : Draw a 1/0 mask (appears as a contour) by hand.
                        If a mask is supplied at the task interface or if
                        automasking is invoked, the current mask is
                        displayed in the GUI and is available for manual
                        editing.

                        Note : If a mask contour is not visible, please
                        check the cursor display at the bottom of
                        GUI to see which parts of the mask image
                        have ones and zeros. If the entire mask=1
                        no contours will be visible.


                        Operation buttons :  -- Stop execution now (restore current model and exit)
                        -- Continue on until global stopping criteria are reached
                        without stopping for any more interaction
                        -- Continue with minor cycles and return for interaction
                        after the next major cycle.

                        Iteration control : -- max cycleniter :  Trigger for the next major cycle

                        The display begins with
                        [ min( cycleniter, niter - itercount ) ]
                        and can be edited by hand.

                        -- iterations left :  The display begins with [niter-itercount ]
                        and can be edited to increase or
                        decrease the total allowed niter.

                        -- threshold : Edit global stopping threshold

                        -- cyclethreshold : The display begins with the
                        automatically computed value
                        (see Note in help for 'threshold'),
                        and can be edited by hand.

                        All edits will be reflected in the log messages that appear
                        once minor cycles begin.


                        [ For scripting purposes, replacing True/False with 1/0 will get tclean to
                        return an imaging summary dictionary to python ]

            
                   Default Value: False

                usemask: Type of mask(s) to be used for deconvolution

                        user: (default) mask image(s) or user specified region file(s) or string CRTF expression(s)
                        subparameters: mask, pbmask
                        pb: primary beam mask
                        subparameter: pbmask

                        Example: usemask="pb", pbmask=0.2
                        Construct a mask at the 0.2 pb gain level.
                        (Currently, this option will work only with
                        gridders that produce .pb (i.e. mosaic and awproject)
                        or if an externally produced .pb image exists on disk)

                        auto-thresh: automask  by threshold for deconvolution
                        subparameters : maskthreshold, maskresolution, pbmask

                        if pbmask is >0.0, after automask algorithm is run, it limits the mask to within
                        a pb gain level of pbmask (This option will work only with
                        gridders that produce .pb (i.e. mosaic and awproject)
                        or if an externally produced .pb image exists on disk)

            
                   Default Value: user
                   Allowed Values:
                                user
                                pb
                                auto-thresh

                mask: Mask (a list of image name(s) or region file(s) or region string(s)

            
                        The name of a CASA image or region file or region string that specifies
                        a 1/0 mask to be used for deconvolution. Only locations with value 1 will
                        be considered for the centers of flux components in the minor cycle.

                        Manual mask options/examples :

                        mask='xxx.mask'  : Use this CASA image named xxx.mask and containing
                        ones and zeros as the mask. If this image is a different
                        shape from what is being made it will be resampled to
                        the target coordinate system before being used.

                        [ Note : If an error occurs during image resampling or
                        if the expected mask does not appear, please try
                        using tasks 'imregrid' or 'makemask' to resample
                        the mask image onto a CASA image with the target
                        shape and coordinates and supply it via the 'mask'
                        parameter. ]

                        mask='xxx.crtf' : A text file with region strings and the following on the first line
                        ( #CRTFv0 CASA Region Text Format version 0 )
                        This is the format of a file created via the viewer's region
                        tool when saved in CASA region file format.

                        mask='circle[[40pix,40pix],10pix]'  : A CASA region string.

                        mask=['xxx.mask','xxx.crtf', 'circle[[40pix,40pix],10pix]']  : a list of masks


            


                        Note : Mask images for deconvolution must contain 1 or 0 in each pixel.
                        Such a mask is different from an internal T/F mask that can be
                        held within each CASA image. These two types of masks are not
                        automatically interchangeable, so please use the makemask task
                        to copy between them if you need to construct a 1/0 based mask
                        from a T/F one.

                        Note : Work is in progress to generate more flexible masking options and
                        enable more controls.

            
                   Default Value: 

                pbmask: primary beam mask

                        Examples : pbmask=0.0 (default, no pb mask)
                        pbmask=0.2 (construct a mask at the 0.2 pb gain level)

            
                   Default Value: 0.0

                maskthreshold: threshold for automasking
                        Threshold value in a string with a unit, sigma (e.g. 3.0)  or fraction of peak (e.g, 0.05)
                        For a float value, if it is >= 1.0, it is interpreted as sigma (i.e. sigma*rms for threshold). If it is < 1.0, it is interpreted as
                        the fraction of peak.

                        Examples : threshold = '1.0mJy'
                        threshold = 0.05  (threshold used is 0.05 * peak)
                        threshold = 5.0 ( threshold used is 5.0 * rms )
                        threshold = '' (default, use 3.0 * rms )
            
                   Default Value: 

                maskresolution: resolution for automasking
                        Examples : maskresolution='10arcsec'
                        maskresolution=''  (default, use a restoring beam major axis)
            
                   Default Value: 

                restart:  Restart using existing images (and start from an existing model image)
                        or automatically increment the image name and make a new image set.

                        True : Re-use existing images. If imagename.model exists the subsequent
                        run will start from this model (i.e. predicting it using current gridder
                        settings and starting from the residual image).  Care must be taken
                        when combining this option with startmodel. Currently, only one or
                        the other can be used.

                        startmodel='', imagename.model exists :
                        - Start from imagename.model
                        startmodel='xxx', imagename.model does not exist :
                        - Start from startmodel
                        startmodel='xxx', imagename.model exists :
                        - Exit with an error message requesting the user to pick
                        only one model.  This situation can arise when doing one
                        run with startmodel='xxx' to produce an output
                        imagename.model that includes the content of startmodel,
                        and wanting to restart a second run to continue deconvolution.
                        Startmodel should be set to '' before continuing.

                        If any change in the shape or coordinate system of the image is
                        desired during the restart, please change the image name and
                        use the startmodel (and mask) parameter(s) so that the old model
                        (and mask) can be regridded to the new coordinate system before starting.

                        False : A convenience feature to increment imagename with '_1', '_2',
                        etc as suffixes so that all runs of tclean are fresh starts (without
                        having to change the imagename parameter or delete images).

                        This mode will search the current directory for all existing
                        imagename extensions, pick the maximum, and adds 1.
                        For imagename='try' it will make try.psf, try_2.psf, try_3.psf, etc.

                        This also works if you specify a directory name in the path :
                        imagename='outdir/try'.  If './outdir' does not exist, it will create it.
                        Then it will search for existing filenames inside that directory.

                        If outlier fields are specified, the incrementing happens for each
                        of them (since each has its own 'imagename').  The counters are
                        synchronized across imagefields, to make it easier to match up sets
                        of output images.  It adds 1 to the 'max id' from all outlier names
                        on disk.  So, if you do two runs with only the main field
                        (imagename='try'), and in the third run you add an outlier with
                        imagename='outtry', you will get the following image names
                        for the third run :  'try_3' and 'outtry_3' even though
                        'outry' and 'outtry_2' have not been used.


            
                   Default Value: True

                savemodel: Options to save model visibilities (none, virtual, modelcolumn)

                        Often, model visibilities must be created and saved in the MS
                        to be later used for self-calibration (or to just plot and view them).

                        none : Do not save any model visibilities in the MS. The MS is opened
                        in readonly mode.

                        Model visibilities can be predicted in a separate step by
                        restarting tclean with niter=0,savemodel=virtual or modelcolumn
                        and not changing any image names so that it finds the .model on
                        disk (or by changing imagename and setting startmodel to the
                        original imagename).

                        virtual : In the last major cycle, save the image model and state of the
                        gridder used during imaging within the SOURCE subtable of the
                        MS. Images required for de-gridding will also be stored internally.
                        All future references to model visibilities will activate the
                        (de)gridder to compute them on-the-fly.  This mode is useful
                        when the dataset is large enough that an additional model data
                        column on disk may be too much extra disk I/O, when the
                        gridder is simple enough that on-the-fly recomputing of the
                        model visibilities is quicker than disk I/O.

                        modelcolumn : In the last major cycle, save predicted model visibilities
                        in the MODEL_DATA column of the MS. This mode is useful when
                        the de-gridding cost to produce the model visibilities is higher
                        than the I/O required to read the model visibilities from disk.
                        This mode is currently required for gridder='awproject'.
                        This mode is also required for the ability to later pull out
                        model visibilities from the MS into a python array for custom
                        processing.

                        Note 1 : The imagename.model  image on disk will always be constructed
                        if the minor cycle runs. This savemodel parameter applies only to
                        model visibilities created by de-gridding the model image.

                        Note 2 :  It is possible for an MS to have both a virtual model
                        as well as a model_data column, but under normal operation,
                        the last used mode will get triggered.  Use the delmod task to
                        clear out existing models from an MS if confusion arises.

            
                   Default Value: none

                makeimages:  List of output images.
                        This option is mainly to force uniformity of outputs
                        for scripting purposes while retaining the feature of
                        making only the images actually needed for a given run.

                        makeimages='auto' : Make only the images necessary for a run.
                        For example, for a niter=0 run, there will be no
                        .model or .image.   For a non A-Projection run,
                        there will be no .pb image.

                        makeimages='choose' : Pick from a list of options either for
                        performance reasons (calcres, calcpsf)
                        or to ensure consistent output products.

            
                   Default Value: auto

                calcres: Calculate initial residual image

                        This parameter controls what the first major cycle does.

                        calcres=False with niter greater than 0 will assume that
                        a .residual image already exists  and that the minor cycle can
                        begin without recomputing it.

                        calcres=False with niter=0 implies that only the PSF will be made
                        and no data will be gridded.

                        calcres=True requires that calcpsf=True or that the .psf and .sumwt
                        images already exist on disk (for normalization purposes).

                        Usage example : For large runs (or a pipeline scripts) it may be
                        useful to first run tclean with niter=0 to create
                        an initial .residual to look at and perhaps make
                        a custom mask for. Imaging can be resumed
                        without recomputing it.

            
                   Default Value: True

                calcpsf: Calculate PSF

                        This parameter controls what the first major cycle does.

                        calcpsf=False will assume that a .psf image already exists
                        and that the minor cycle can begin without recomputing it.
            
                   Default Value: True

                restoremodel: Restore the model image

                        Construct a restored image : imagename.image by convolving the model
                        image with a clean beam and adding the residual image to the result.
                        If a restoringbeam is specified, the residual image is also
                        smoothed to that target resolution before adding it in.

                        restoremodel='auto' : Run the restore step only if deconvolution
                        iterations have been performed
                        restoremodel=True : Always run the restore step. If a .model does
                        not exist, make an empty one and create
                        the restored image from the residuals
                        ( with additional smoothing if needed ).
                        With algorithm='mtmfs', this will construct
                        Taylor coefficient maps from the residuals and
                        compute .alpha and .alpha.error.

            
                   Default Value: auto

                writepb: Make a primary beam image

                        Construct an imagename.pb image normalized to 1.0 at its peak.

                        writepb='auto' : Construct a PB only for A-Projection gridders that
                        produce .weight images
                        [ .pb = sqrt(.weight) / max( sqrt(.weight) ) ]

                        writepb=True : Always construct a .pb image. For gridders that do not
                        produce .weight, construct .pb explicitly.
                        Note : For now, this option will create an empty image.

                        ( The makepb script can be used as described in the
                        gridder section to make .pb images externally )
            
                   Default Value: auto

                ranks: 
                                List of MPI ranks to use for imaging sub-cluster

                                Run major cycles in parallel (this feature is experimental)

                                Parallel tclean will run only if casa has already been started
                                using mpirun.  Please refer to HPC documentation for details on
                                how to start this on your system.

                                Example :  mpirun -n 3 -xterm 0 `which casa`

                                Continuum Imaging :
                                -  Data are partitioned (in time) into NProc pieces
                                -  Gridding/iFT is done separately per partition
                                -  Images (and weights) are gathered and then normalized
                                - One non-parallel minor cycle is run
                                - Model image is scattered to all processes
                                - Major cycle is done in parallel per partition

                                Cube Imaging :
                                - Data and Image coordinates are partitioned (in freq) into NProc pieces
                                - Each partition is processed independently (major and minor cycles)
                                - All processes are synchronized at major cycle boundaries for convergence checks
                                - At the end, cubes from all partitions are concatenated along the spectral axis

                                Note 1 :  Iteration control for cube imaging is independent per partition.
                                - There is currently no communication between them to synchronize
                                information such as peak residual and cyclethreshold. Therefore,
                                different chunks may trigger major cycles at different levels.
                                - For cube imaging in parallel, there is currently no interactive masking.
                                (Proper synchronization of iteration control is work in progress.)

            
                   Default Value: 

        Returns: void

        Example :


                This is the first release of our refactored imager code. Although most features have
                been used and validated, there are many details that have not been thoroughly tested.
                Feedback will be much appreciated.


                Usage Examples :
                -----------------------

                (A) A suite of test programs that demo all usable modes of tclean on small test datasets
                https://svn.cv.nrao.edu/svn/casa/branches/release-4_5/gcwrap/python/scripts/tests/test_refimager.py
                (B) A set of demo examples for ALMA imaging
                https://casaguides.nrao.edu/index.php/TCLEAN_and_ALMA



    
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'tclean2'
        self.__globals__['taskname'] = 'tclean2'
        ###
        self.__globals__['update_params'](func=self.__globals__['taskname'],printtext=False,ipython_globals=self.__globals__)
        ###
        ###
        #Handle globals or user over-ride of arguments
        #
        if type(self.__call__.func_defaults) is NoneType:
            function_signature_defaults={}
        else:
            function_signature_defaults=dict(zip(self.__call__.func_code.co_varnames[1:],self.__call__.func_defaults))
        useLocalDefaults = False

        for item in function_signature_defaults.iteritems():
                key,val = item
                keyVal = eval(key)
                if (keyVal == None):
                        #user hasn't set it - use global/default
                        pass
                else:
                        #user has set it - use over-ride
                        if (key != 'self') :
                           useLocalDefaults = True

        myparams = {}
        if useLocalDefaults :
           for item in function_signature_defaults.iteritems():
               key,val = item
               keyVal = eval(key)
               exec('myparams[key] = keyVal')
               self.parameters[key] = keyVal
               if (keyVal == None):
                   exec('myparams[key] = '+ key + ' = self.itsdefault(key)')
                   keyVal = eval(key)
                   if(type(keyVal) == dict) :
                      if len(keyVal) > 0 :
                         exec('myparams[key] = ' + key + ' = keyVal[len(keyVal)-1][\'value\']')
                      else :
                         exec('myparams[key] = ' + key + ' = {}')

        else :
            print ''

            myparams['vis'] = vis = self.parameters['vis']
            myparams['selectdata'] = selectdata = self.parameters['selectdata']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']
            myparams['imagename'] = imagename = self.parameters['imagename']
            myparams['imsize'] = imsize = self.parameters['imsize']
            myparams['cell'] = cell = self.parameters['cell']
            myparams['phasecenter'] = phasecenter = self.parameters['phasecenter']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['projection'] = projection = self.parameters['projection']
            myparams['startmodel'] = startmodel = self.parameters['startmodel']
            myparams['specmode'] = specmode = self.parameters['specmode']
            myparams['reffreq'] = reffreq = self.parameters['reffreq']
            myparams['nchan'] = nchan = self.parameters['nchan']
            myparams['start'] = start = self.parameters['start']
            myparams['width'] = width = self.parameters['width']
            myparams['outframe'] = outframe = self.parameters['outframe']
            myparams['veltype'] = veltype = self.parameters['veltype']
            myparams['restfreq'] = restfreq = self.parameters['restfreq']
            myparams['interpolation'] = interpolation = self.parameters['interpolation']
            myparams['gridder'] = gridder = self.parameters['gridder']
            myparams['facets'] = facets = self.parameters['facets']
            myparams['chanchunks'] = chanchunks = self.parameters['chanchunks']
            myparams['wprojplanes'] = wprojplanes = self.parameters['wprojplanes']
            myparams['aterm'] = aterm = self.parameters['aterm']
            myparams['psterm'] = psterm = self.parameters['psterm']
            myparams['wbawp'] = wbawp = self.parameters['wbawp']
            myparams['conjbeams'] = conjbeams = self.parameters['conjbeams']
            myparams['cfcache'] = cfcache = self.parameters['cfcache']
            myparams['computepastep'] = computepastep = self.parameters['computepastep']
            myparams['rotatepastep'] = rotatepastep = self.parameters['rotatepastep']
            myparams['pblimit'] = pblimit = self.parameters['pblimit']
            myparams['normtype'] = normtype = self.parameters['normtype']
            myparams['deconvolver'] = deconvolver = self.parameters['deconvolver']
            myparams['scales'] = scales = self.parameters['scales']
            myparams['nterms'] = nterms = self.parameters['nterms']
            myparams['scalebias'] = scalebias = self.parameters['scalebias']
            myparams['restoringbeam'] = restoringbeam = self.parameters['restoringbeam']
            myparams['outlierfile'] = outlierfile = self.parameters['outlierfile']
            myparams['weighting'] = weighting = self.parameters['weighting']
            myparams['robust'] = robust = self.parameters['robust']
            myparams['npixels'] = npixels = self.parameters['npixels']
            myparams['uvtaper'] = uvtaper = self.parameters['uvtaper']
            myparams['niter'] = niter = self.parameters['niter']
            myparams['gain'] = gain = self.parameters['gain']
            myparams['threshold'] = threshold = self.parameters['threshold']
            myparams['cycleniter'] = cycleniter = self.parameters['cycleniter']
            myparams['cyclefactor'] = cyclefactor = self.parameters['cyclefactor']
            myparams['minpsffraction'] = minpsffraction = self.parameters['minpsffraction']
            myparams['maxpsffraction'] = maxpsffraction = self.parameters['maxpsffraction']
            myparams['interactive'] = interactive = self.parameters['interactive']
            myparams['usemask'] = usemask = self.parameters['usemask']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['pbmask'] = pbmask = self.parameters['pbmask']
            myparams['maskthreshold'] = maskthreshold = self.parameters['maskthreshold']
            myparams['maskresolution'] = maskresolution = self.parameters['maskresolution']
            myparams['restart'] = restart = self.parameters['restart']
            myparams['savemodel'] = savemodel = self.parameters['savemodel']
            myparams['makeimages'] = makeimages = self.parameters['makeimages']
            myparams['calcres'] = calcres = self.parameters['calcres']
            myparams['calcpsf'] = calcpsf = self.parameters['calcpsf']
            myparams['restoremodel'] = restoremodel = self.parameters['restoremodel']
            myparams['writepb'] = writepb = self.parameters['writepb']
            myparams['ranks'] = ranks = self.parameters['ranks']

        if type(uvtaper)==str: uvtaper=[uvtaper]
        if type(ranks)==int: ranks=[ranks]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['selectdata'] = selectdata
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['timerange'] = timerange
        mytmp['uvrange'] = uvrange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['observation'] = observation
        mytmp['intent'] = intent
        mytmp['datacolumn'] = datacolumn
        mytmp['imagename'] = imagename
        mytmp['imsize'] = imsize
        mytmp['cell'] = cell
        mytmp['phasecenter'] = phasecenter
        mytmp['stokes'] = stokes
        mytmp['projection'] = projection
        mytmp['startmodel'] = startmodel
        mytmp['specmode'] = specmode
        mytmp['reffreq'] = reffreq
        mytmp['nchan'] = nchan
        mytmp['start'] = start
        mytmp['width'] = width
        mytmp['outframe'] = outframe
        mytmp['veltype'] = veltype
        mytmp['restfreq'] = restfreq
        mytmp['interpolation'] = interpolation
        mytmp['gridder'] = gridder
        mytmp['facets'] = facets
        mytmp['chanchunks'] = chanchunks
        mytmp['wprojplanes'] = wprojplanes
        mytmp['aterm'] = aterm
        mytmp['psterm'] = psterm
        mytmp['wbawp'] = wbawp
        mytmp['conjbeams'] = conjbeams
        mytmp['cfcache'] = cfcache
        mytmp['computepastep'] = computepastep
        mytmp['rotatepastep'] = rotatepastep
        mytmp['pblimit'] = pblimit
        mytmp['normtype'] = normtype
        mytmp['deconvolver'] = deconvolver
        mytmp['scales'] = scales
        mytmp['nterms'] = nterms
        mytmp['scalebias'] = scalebias
        mytmp['restoringbeam'] = restoringbeam
        mytmp['outlierfile'] = outlierfile
        mytmp['weighting'] = weighting
        mytmp['robust'] = robust
        mytmp['npixels'] = npixels
        mytmp['uvtaper'] = uvtaper
        mytmp['niter'] = niter
        mytmp['gain'] = gain
        mytmp['threshold'] = threshold
        mytmp['cycleniter'] = cycleniter
        mytmp['cyclefactor'] = cyclefactor
        mytmp['minpsffraction'] = minpsffraction
        mytmp['maxpsffraction'] = maxpsffraction
        mytmp['interactive'] = interactive
        mytmp['usemask'] = usemask
        mytmp['mask'] = mask
        mytmp['pbmask'] = pbmask
        mytmp['maskthreshold'] = maskthreshold
        mytmp['maskresolution'] = maskresolution
        mytmp['restart'] = restart
        mytmp['savemodel'] = savemodel
        mytmp['makeimages'] = makeimages
        mytmp['calcres'] = calcres
        mytmp['calcpsf'] = calcpsf
        mytmp['restoremodel'] = restoremodel
        mytmp['writepb'] = writepb
        mytmp['ranks'] = ranks
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'tclean2.xml')

        casalog.origin('tclean2')
        try :
          #if not trec.has_key('tclean2') or not casac.casac.utils().verify(mytmp, trec['tclean2']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['tclean2'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('tclean2', 'tclean2.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'tclean2'
          spaces = ' '*(18-len(tname))
          casalog.post('\n##########################################'+
                       '\n##### Begin Task: ' + tname + spaces + ' #####')
          # Don't do telemetry from MPI servers (CASR-329)
          if do_full_logging and casa['state']['telemetry-enabled']:
              #casalog.poststat('Begin Task: ' + tname)
              task_starttime = str(datetime.datetime.now())
          if type(self.__call__.func_defaults) is NoneType:
              casalog.post(scriptstr[0]+'\n', 'INFO')
          else:
              casalog.post(scriptstr[1][1:]+'\n', 'INFO')

          # Effective call to the task as defined in gcwrap/python/scripts/task_*
          result = tclean2(vis, selectdata, field, spw, timerange, uvrange, antenna, scan, observation, intent, datacolumn, imagename, imsize, cell, phasecenter, stokes, projection, startmodel, specmode, reffreq, nchan, start, width, outframe, veltype, restfreq, interpolation, gridder, facets, chanchunks, wprojplanes, aterm, psterm, wbawp, conjbeams, cfcache, computepastep, rotatepastep, pblimit, normtype, deconvolver, scales, nterms, scalebias, restoringbeam, outlierfile, weighting, robust, npixels, uvtaper, niter, gain, threshold, cycleniter, cyclefactor, minpsffraction, maxpsffraction, interactive, usemask, mask, pbmask, maskthreshold, maskresolution, restart, savemodel, makeimages, calcres, calcpsf, restoremodel, writepb, ranks)

          if do_full_logging and casa['state']['telemetry-enabled']:
              task_endtime = str(datetime.datetime.now())
              casalog.poststat( 'Task ' + tname + ' complete. Start time: ' + task_starttime + ' End time: ' + task_endtime )
          casalog.post('##### End Task: ' + tname + '  ' + spaces + ' #####'+
                       '\n##########################################')

        except Exception, instance:
          if(self.__globals__.has_key('__rethrow_casa_exceptions') and self.__globals__['__rethrow_casa_exceptions']) :
             raise
          else :
             #print '**** Error **** ',instance
             tname = 'tclean2'
             casalog.post('An error occurred running task '+tname+'.', 'ERROR')
             pass
        casalog.origin('')

        return result
#
#
#
#    def paramgui(self, useGlobals=True, ipython_globals=None):
#        """
#        Opens a parameter GUI for this task.  If useGlobals is true, then any relevant global parameter settings are used.
#        """
#        import paramgui
#        if not hasattr(self, "__globals__") or self.__globals__ == None :
#           self.__globals__=stack_frame_find( )
#
#        if useGlobals:
#            if ipython_globals == None:
#                myf=self.__globals__
#            else:
#                myf=ipython_globals
#
#            paramgui.setGlobals(myf)
#        else:
#            paramgui.setGlobals({})
#
#        paramgui.runTask('tclean2', myf['_ip'])
#        paramgui.setGlobals({})
#
#
#
#
    def defaults(self, param=None, ipython_globals=None, paramvalue=None, subparam=None):
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        if ipython_globals == None:
            myf=self.__globals__
        else:
            myf=ipython_globals

        a = odict()
        a['vis']  = ''
        a['selectdata']  = True
        a['datacolumn']  = 'corrected'
        a['imagename']  = ''
        a['imsize']  = [100]
        a['cell']  = ["1arcsec"]
        a['phasecenter']  = ''
        a['stokes']  = 'I'
        a['projection']  = 'SIN'
        a['startmodel']  = ''
        a['specmode']  = 'mfs'
        a['gridder']  = 'standard'
        a['deconvolver']  = 'hogbom'
        a['outlierfile']  = ''
        a['weighting']  = 'natural'
        a['niter']  = 0
        a['usemask']  = 'user'
        a['restart']  = True
        a['savemodel']  = 'none'
        a['makeimages']  = 'auto'
        a['ranks']  = []

        a['selectdata'] = {
                    0:odict([{'value':True}, {'field':""}, {'spw':""}, {'timerange':""}, {'uvrange':""}, {'antenna':""}, {'scan':""}, {'observation':""}, {'intent':""}])}
        a['specmode'] = {
                    0:odict([{'value':'mfs'}, {'reffreq':""}]), 
                    1:odict([{'value':'cube'}, {'nchan':-1}, {'start':""}, {'width':""}, {'outframe':""}, {'veltype':"radio"}, {'restfreq':[]}, {'interpolation':"linear"}, {'chanchunks':1}]), 
                    2:odict([{'value':'cubedata'}, {'nchan':-1}, {'start':""}, {'width':""}, {'veltype':"radio"}, {'restfreq':[]}, {'interpolation':"linear"}, {'chanchunks':1}])}
        a['gridder'] = {
                    0:{'value':'standard'}, 
                    1:odict([{'value':'widefield'}, {'wprojplanes':1}, {'facets':1}]), 
                    2:odict([{'value':'wproject'}, {'wprojplanes':1}]), 
                    3:odict([{'value':'wprojectft'}, {'wprojplanes':1}]), 
                    4:odict([{'value':'mosaic'}, {'pblimit':0.2}, {'normtype':"flatnoise"}]), 
                    5:odict([{'value':'mosaicft'}, {'pblimit':0.2}, {'normtype':"flatnoise"}]), 
                    6:odict([{'value':'ftmosaic'}, {'pblimit':0.2}, {'normtype':"flatnoise"}]), 
                    7:odict([{'value':'imagemosaic'}, {'wprojplanes':1}, {'pblimit':0.2}, {'normtype':"flatnoise"}]), 
                    8:odict([{'value':'awproject'}, {'wprojplanes':1}, {'pblimit':0.2}, {'normtype':"flatnoise"}, {'psterm':False}, {'aterm':True}, {'cfcache':""}, {'computepastep':360.0}, {'rotatepastep':360.0}, {'wbawp':False}, {'conjbeams':False}]), 
                    9:odict([{'value':'awprojectft'}, {'wprojplanes':1}, {'pblimit':0.2}, {'normtype':"flatnoise"}, {'psterm':False}, {'aterm':True}, {'cfcache':""}, {'computepastep':360.0}, {'rotatepastep':360.0}, {'wbawp':False}, {'conjbeams':False}])}
        a['weighting'] = {
                    0:odict([{'value':'natural'}, {'uvtaper':[]}]), 
                    1:{'value':'uniform'}, 
                    2:odict([{'value':'briggs'}, {'robust':0.5}, {'npixels':0}, {'uvtaper':[]}])}
        a['deconvolver'] = {
                    0:odict([{'value':'hogbom'}, {'restoringbeam':[]}]), 
                    1:odict([{'value':'clark'}, {'restoringbeam':[]}]), 
                    2:odict([{'value':'multiscale'}, {'scales':[]}, {'smallscalebias':0.6}, {'restoringbeam':[]}]), 
                    3:odict([{'value':'mtmfs'}, {'scales':[]}, {'nterms':2}, {'restoringbeam':[]}]), 
                    4:odict([{'value':'aasp'}, {'restoringbeam':[]}])}
        a['niter'] = {
                    0:odict([{'notvalue':0}, {'gain':0.1}, {'threshold':0.0}, {'cycleniter':-1}, {'cyclefactor':1.0}, {'minpsffraction':0.05}, {'maxpsffraction':0.8}, {'interactive':False}])}
        a['usemask'] = {
                    0:{'value':'none'}, 
                    1:odict([{'value':'user'}, {'mask':""}, {'pbmask':0.0}]), 
                    2:odict([{'value':'pb'}, {'pbmask':0.2}]), 
                    3:odict([{'value':'auto-thresh'}, {'pbmask':0.0}, {'maskthreshold':""}, {'maskresolution':""}])}
        a['makeimages'] = {
                    0:{'value':'auto'}, 
                    1:odict([{'value':'choose'}, {'calcres':True}, {'calcpsf':True}, {'restoremodel':'auto'}, {'writepb':'auto'}])}

### This function sets the default values but also will return the list of
### parameters or the default value of a given parameter
        if(param == None):
                myf['__set_default_parameters'](a)
        elif(param == 'paramkeys'):
                return a.keys()
        else:
            if(paramvalue==None and subparam==None):
               if(a.has_key(param)):
                  return a[param]
               else:
                  return self.itsdefault(param)
            else:
               retval=a[param]
               if(type(a[param])==dict):
                  for k in range(len(a[param])):
                     valornotval='value'
                     if(a[param][k].has_key('notvalue')):
                        valornotval='notvalue'
                     if((a[param][k][valornotval])==paramvalue):
                        retval=a[param][k].copy()
                        retval.pop(valornotval)
                        if(subparam != None):
                           if(retval.has_key(subparam)):
                              retval=retval[subparam]
                           else:
                              retval=self.itsdefault(subparam)
                     else:
                        retval=self.itsdefault(subparam)
               return retval


#
#
    def check_params(self, param=None, value=None, ipython_globals=None):
      if ipython_globals == None:
          myf=self.__globals__
      else:
          myf=ipython_globals
#      print 'param:', param, 'value:', value
      try :
         if str(type(value)) != "<type 'instance'>" :
            value0 = value
            value = myf['cu'].expandparam(param, value)
            matchtype = False
            if(type(value) == numpy.ndarray):
               if(type(value) == type(value0)):
                  myf[param] = value.tolist()
               else:
                  #print 'value:', value, 'value0:', value0
                  #print 'type(value):', type(value), 'type(value0):', type(value0)
                  myf[param] = value0
                  if type(value0) != list :
                     matchtype = True
            else :
               myf[param] = value
            value = myf['cu'].verifyparam({param:value})
            if matchtype:
               value = False
      except Exception, instance:
         #ignore the exception and just return it unchecked
         myf[param] = value
      return value
#
#
    def description(self, key='tclean2', subkey=None):
        desc={'tclean2': 'Radio Interferometric Image Reconstruction',
               'vis': 'Name of input visibility file(s)',
               'selectdata': 'Enable data selection parameters',
               'field': 'field(s) to select',
               'spw': 'spw(s)/channels to select',
               'timerange': 'Range of time to select from data',
               'uvrange': 'Select data within uvrange',
               'antenna': 'Select data based on antenna/baseline',
               'scan': 'Scan number range',
               'observation': 'Observation ID range',
               'intent': 'Scan Intent(s)',
               'datacolumn': 'Data column to image(data,corrected)',
               'imagename': 'Pre-name of output images',
               'imsize': 'Number of pixels',
               'cell': 'Cell size',
               'phasecenter': 'Phase center of the image',
               'stokes': 'Stokes Planes to make',
               'projection': 'Coordinate projection (SIN, HPX)',
               'startmodel': 'Name of starting model image',
               'specmode': 'Spectral definition mode (mfs,cube,cubedata)',
               'reffreq': 'Reference frequency',
               'nchan': 'Number of channels in the output image',
               'start': 'First channel (e.g. start=3,start=\'1.1GHz\',start=\'15343km/s\')',
               'width': 'Channel width (e.g. width=2,width=\'0.1MHz\',width=\'10km/s\')',
               'outframe': 'Spectral reference frame in which to interpret \'start\' and \'width\'',
               'veltype': 'Velocity type (radio, z, ratio, beta, gamma, optical)',
               'restfreq': 'List of rest frequencies',
               'interpolation': 'Spectral interpolation (nearest,linear,cubic)',
               'gridder': 'Gridding options (standard, wproject, widefield, mosaic, awproject)',
               'facets': 'Number of facets on a side',
               'chanchunks': 'Number of channel chunks',
               'wprojplanes': 'Number of distinct w-values for convolution functions',
               'aterm': 'Use aperture illumination functions during gridding',
               'psterm': 'Use prolate spheroidal during gridding',
               'wbawp': 'Use wideband A-terms',
               'conjbeams': 'Use conjugate frequency for wideband A-terms',
               'cfcache': '>Convolution function cache directory name',
               'computepastep': 'At what parallactic angle interval to recompute AIFs (deg)',
               'rotatepastep': 'At what parallactic angle interval to rotate nearest AIF (deg) ',
               'pblimit': '>PB gain level at which to cut off normalizations ',
               'normtype': 'Normalization type (flatnoise, flatsky)',
               'deconvolver': 'Minor cycle algorithm (hogbom,clark,multiscale,mtmfs,mem,clarkstokes)',
               'scales': 'List of scale sizes (in pixels) for multi-scale algorithms',
               'nterms': 'Number of Taylor coefficients in the spectral model',
               'scalebias': 'A bias towards smaller scale sizes',
               'restoringbeam': 'Restoring beam shape to use. Default is the PSF main lobe',
               'outlierfile': 'Name of outlier-field image definitions',
               'weighting': 'Weighting scheme (natural,uniform,briggs)',
               'robust': 'Robustness parameter',
               'npixels': 'Number of pixels to determine uv-cell size (0 : -/+ 3 pixels)',
               'uvtaper': 'uv-taper on outer baselines in uv-plane',
               'niter': 'Maximum number of iterations',
               'gain': 'Loop gain',
               'threshold': 'Stopping threshold ',
               'cycleniter': 'Maximum number of minor-cycle iterations',
               'cyclefactor': 'Scaling on PSF sidelobe level to compute the minor-cycle stopping threshold.',
               'minpsffraction': 'PSF fraction that marks the max depth of cleaning in the minor cycle',
               'maxpsffraction': 'PSF fraction that marks the minimum depth of cleaning in the minor cycle ',
               'interactive': 'Modify masks and parameters at runtime',
               'usemask': 'Type of mask(s) for deconvolution (user,pb,auto-thresh)',
               'mask': 'Mask (a list of image name(s) or region file(s) or region string(s) )',
               'pbmask': 'primary beam mask',
               'maskthreshold': 'threshold for automasking (string with unit, e.g. "1.0mJy", sigma,  or fraction of peak ,e.g. 0.1)',
               'maskresolution': 'resolution for automasking (string, e.g. "10arcsec")',
               'restart': 'True : Re-use existing images. False : Increment imagename',
               'savemodel': 'Options to save model visibilities (none, virtual, modelcolumn)',
               'makeimages': 'List of output images (auto,choose)',
               'calcres': 'Calculate initial residual image',
               'calcpsf': 'Calculate PSF',
               'restoremodel': 'Restore the model image',
               'writepb': 'Make a primary beam image',
               'ranks': 'List of participating ranks',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['selectdata']  = True
        a['field']  = ''
        a['spw']  = ''
        a['timerange']  = ''
        a['uvrange']  = ''
        a['antenna']  = ''
        a['scan']  = ''
        a['observation']  = ''
        a['intent']  = ''
        a['datacolumn']  = 'corrected'
        a['imagename']  = ''
        a['imsize']  = [100]
        a['cell']  = ["1arcsec"]
        a['phasecenter']  = ''
        a['stokes']  = 'I'
        a['projection']  = 'SIN'
        a['startmodel']  = ''
        a['specmode']  = 'mfs'
        a['reffreq']  = ''
        a['nchan']  = -1
        a['start']  = ''
        a['width']  = ''
        a['outframe']  = 'LSRK'
        a['veltype']  = 'radio'
        a['restfreq']  = []
        a['interpolation']  = 'linear'
        a['gridder']  = 'standard'
        a['facets']  = 1
        a['chanchunks']  = 1
        a['wprojplanes']  = 1
        a['aterm']  = True
        a['psterm']  = False
        a['wbawp']  = True
        a['conjbeams']  = True
        a['cfcache']  = ''
        a['computepastep']  = 360.0
        a['rotatepastep']  = 360.0
        a['pblimit']  = 0.2
        a['normtype']  = 'flatnoise'
        a['deconvolver']  = 'hogbom'
        a['scales']  = []
        a['nterms']  = 2
        a['scalebias']  = 0.6
        a['restoringbeam']  = []
        a['outlierfile']  = ''
        a['weighting']  = 'natural'
        a['robust']  = 0.5
        a['npixels']  = 0
        a['uvtaper']  = ['']
        a['niter']  = 0
        a['gain']  = 0.1
        a['threshold']  = 0.0
        a['cycleniter']  = -1
        a['cyclefactor']  = 1.0
        a['minpsffraction']  = 0.05
        a['maxpsffraction']  = 0.8
        a['interactive']  = False
        a['usemask']  = 'user'
        a['mask']  = ''
        a['pbmask']  = 0.0
        a['maskthreshold']  = ''
        a['maskresolution']  = ''
        a['restart']  = True
        a['savemodel']  = 'none'
        a['makeimages']  = 'auto'
        a['calcres']  = True
        a['calcpsf']  = True
        a['restoremodel']  = 'auto'
        a['writepb']  = 'auto'
        a['ranks']  = []

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['selectdata']  == True:
            a['field'] = ""
            a['spw'] = ""
            a['timerange'] = ""
            a['uvrange'] = ""
            a['antenna'] = ""
            a['scan'] = ""
            a['observation'] = ""
            a['intent'] = ""

        if self.parameters['specmode']  == 'mfs':
            a['reffreq'] = ""

        if self.parameters['specmode']  == 'cube':
            a['nchan'] = -1
            a['start'] = ""
            a['width'] = ""
            a['outframe'] = ""
            a['veltype'] = "radio"
            a['restfreq'] = []
            a['interpolation'] = "linear"
            a['chanchunks'] = 1

        if self.parameters['specmode']  == 'cubedata':
            a['nchan'] = -1
            a['start'] = ""
            a['width'] = ""
            a['veltype'] = "radio"
            a['restfreq'] = []
            a['interpolation'] = "linear"
            a['chanchunks'] = 1

        if self.parameters['gridder']  == 'widefield':
            a['wprojplanes'] = 1
            a['facets'] = 1

        if self.parameters['gridder']  == 'wproject':
            a['wprojplanes'] = 1

        if self.parameters['gridder']  == 'wprojectft':
            a['wprojplanes'] = 1

        if self.parameters['gridder']  == 'mosaic':
            a['pblimit'] = 0.2
            a['normtype'] = "flatnoise"

        if self.parameters['gridder']  == 'mosaicft':
            a['pblimit'] = 0.2
            a['normtype'] = "flatnoise"

        if self.parameters['gridder']  == 'ftmosaic':
            a['pblimit'] = 0.2
            a['normtype'] = "flatnoise"

        if self.parameters['gridder']  == 'imagemosaic':
            a['wprojplanes'] = 1
            a['pblimit'] = 0.2
            a['normtype'] = "flatnoise"

        if self.parameters['gridder']  == 'awproject':
            a['wprojplanes'] = 1
            a['pblimit'] = 0.2
            a['normtype'] = "flatnoise"
            a['psterm'] = False
            a['aterm'] = True
            a['cfcache'] = ""
            a['computepastep'] = 360.0
            a['rotatepastep'] = 360.0
            a['wbawp'] = False
            a['conjbeams'] = False

        if self.parameters['gridder']  == 'awprojectft':
            a['wprojplanes'] = 1
            a['pblimit'] = 0.2
            a['normtype'] = "flatnoise"
            a['psterm'] = False
            a['aterm'] = True
            a['cfcache'] = ""
            a['computepastep'] = 360.0
            a['rotatepastep'] = 360.0
            a['wbawp'] = False
            a['conjbeams'] = False

        if self.parameters['weighting']  == 'natural':
            a['uvtaper'] = []

        if self.parameters['weighting']  == 'briggs':
            a['robust'] = 0.5
            a['npixels'] = 0
            a['uvtaper'] = []

        if self.parameters['deconvolver']  == 'hogbom':
            a['restoringbeam'] = []

        if self.parameters['deconvolver']  == 'clark':
            a['restoringbeam'] = []

        if self.parameters['deconvolver']  == 'multiscale':
            a['scales'] = []
            a['smallscalebias'] = 0.6
            a['restoringbeam'] = []

        if self.parameters['deconvolver']  == 'mtmfs':
            a['scales'] = []
            a['nterms'] = 2
            a['restoringbeam'] = []

        if self.parameters['deconvolver']  == 'aasp':
            a['restoringbeam'] = []

        if self.parameters['niter']  != 0:
            a['gain'] = 0.1
            a['threshold'] = 0.0
            a['cycleniter'] = -1
            a['cyclefactor'] = 1.0
            a['minpsffraction'] = 0.05
            a['maxpsffraction'] = 0.8
            a['interactive'] = False

        if self.parameters['usemask']  == 'user':
            a['mask'] = ""
            a['pbmask'] = 0.0

        if self.parameters['usemask']  == 'pb':
            a['pbmask'] = 0.2

        if self.parameters['usemask']  == 'auto-thresh':
            a['pbmask'] = 0.0
            a['maskthreshold'] = ""
            a['maskresolution'] = ""

        if self.parameters['makeimages']  == 'choose':
            a['calcres'] = True
            a['calcpsf'] = True
            a['restoremodel'] = 'auto'
            a['writepb'] = 'auto'

        if a.has_key(paramname) :
              return a[paramname]
tclean2_cli = tclean2_cli_()
