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
import task_sdimaging
def sdimaging(infiles=[''], outfile='', overwrite=False, field='', spw='', antenna='', scan='', intent='OBSERVE_TARGET#ON_SOURCE', mode='channel', nchan=-1, start=0, width=1, veltype='radio', outframe='', gridfunction='BOX', convsupport=-1, truncate=-1, gwidth=-1, jwidth=-1, imsize=[], cell='', phasecenter='', projection='SIN', ephemsrcname='', pointingcolumn='direction', restfreq='', stokes='', minweight=0.1, brightnessunit='', clipminmax=False):

        """SD task: imaging for total power and spectral data
Keyword arguments:
infiles -- a list of names of input SD Measurementsets
        example: 'm100.PM01.ms'
                 ['m100.PM01.ms','m100.PM03.ms']; multiple MSes
outfile -- name of output image
        default: ''
        example: 'mySDimage.im'
overwrite -- overwrite the output file if already exists
        options: (bool) True,False
        default: False (do NOT overwrite)
        example: if True, existing file will be overwritten
field -- select data by field IDs and names
                If field string is a non-negative integer, it is assumed to
                be a field index otherwise, it is assumed to be a 
                field name
        default: '' (use all fields)
        example: field='3C2*' (all names starting with 3C2)
                 field='0,4,5~7' (field IDs 0,4,5,6,7)
                 field='0,3C273' (field ID 3 or filed named 3C273)
                 For multiple MS input, a list of field strings can be used:
                 field = ['0~2','0~4'] (field ids 0-2 for the first MS and 0-4
                         for the second) 
                 field = '0~2' (field ids 0-2 for all input MSes)
        this selection is in addition to the other selections to data
spw -- select data by spectral window IDs/channels
       NOTE: channels de-selected here will contain all zeros if
       selected by the parameter mode subparameters.    
        default: '' (use all IFs and channels)
        example: spw='3,5,7' (IF IDs 3,5,7; all channels)
                 spw='<2' (IF IDs less than 2, i.e., 0,1; all channels)
                 spw='30~45GHz' (IF IDs with the center frequencies in range 30-45GHz; all channels)
                 spw='0:5~61' (IF ID 0; channels 5 to 61; all channels)
                 spw='3:10~20;50~60' (select multiple channel ranges within IF ID 3)
                 spw='3:10~20,4:0~30' (select different channel ranges for IF IDs 3 and 4)
                 spw='1~4;6:15~48' (for channels 15 through 48 for IF IDs 1,2,3,4 and 6)
                 For multiple MS input, a list of spw strings can be used:
                 spw=['0','0~3'] (spw ids 0 for the first MS and 0-3 for the second)
                 spw='0~3' (spw ids 0-3 for all input MSes)
        this selection is in addition to the other selections to data
antenna -- select data by antenna names or IDs
           If antenna string is a non-negative integer, it is 
           assumed to be an antenna index, otherwise, it is
           considered an antenna name.
        default: '' (all baselines, i.e. all antenna in case of auto data)
        example: antenna='PM03'
                 For multiple MS input, a list of antenna strings can be used:
                 antenna=['5','6'] (antenna id5 for the first MS and 6 for the second)
                 antenna='5' (antenna index 5 for all input MSes)
        this selection is in addition to the other selections to data
scan -- select data by scan numbers
        default: '' (use all scans)
        example: scan='21~23' (scan IDs 21,22,23)
                 For multiple MS input, a list of scan strings can be used:
                 scan=['0~100','10~200'] (scan ids 0-100 for the first MS
                 and 10-200 for the second)
                 scan='0~100 (scan ids 0-100 for all input MSes)
        this selection is in addition to the other selections to data
intent -- select data by observational intent, also referred to as 'scan intent'
        default: 'OBSERVE_TARGET#ON_SOURCE' (ALMA ON-source intent)
        example: intent='' (use all scan intents)
                 intent='*ON_SOURCE*' (any valid scan-intent expression accepted by the MSSelection module can be specified)
                 For multiple MS input, a list of scan-intent expressions can be used:
                 intent=['ON_SOURCE','CALIBRATE_BANDPASS'] (scan intent ON_SOURCE for the first MS
                 and CALIBRATE_BANDPASS for the second)
        this selection is in addition to the other selections to data
mode -- spectral gridding type
        options: 'channel', 'velocity', 'frequency'
        default: 'channel'
    >>> mode expandable parameters
       nchan -- Total number of channels in the output image.
           default: -1; Automatically selects enough channels to cover 
                    data selected by 'spw' consistent with 'start' and 'width'.
                    It is often easiest to leave nchan at the default value. 
           example: nchan=100
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
           default: '' (the first input channel of first input spw)
           example: start=100 (mode='channel')
                    start='22.3GHz' (mode='frequency')
                    start='5.0km/s' (mode='velocity')
       width -- Output channel width
               For mode='channel', default=1; width>1 indicates channel averaging
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
       veltype -- Velocity definition
           Options: 'radio','optical','true','relativistic'
           default: 'radio'
outframe -- velocity reference frame of output image
        Options: '','LSRK','LSRD','BARY','GEO','TOPO','GALACTO',
                 'LGROUP','CMB'
        default: ''; same as input data or 'LSRK' for multiple-MS inputs
        example: frame='bary' for Barycentric frame 
gridfunction -- gridding function for imaging
        options: 'BOX' (Box-car), 'SF' (Spheroidal), 
                 'PB' (Primary-beam), 'GAUSS' (Gaussian),
                 'GJINC' (Gaussian*Jinc)
        default: 'BOX'
        example: 'SF'
    >>> gridfunction expandable parameter:
       convsupport -- convolution support for 'SF' 
           default: -1 (use default for each gridfunction)
           example: 3
       truncate -- truncattion radius of convolution kernel.
                   effective only for 'GAUSS' and 'GJINC'.
           default: '-1' (use default for each gridfunction)
           example: 3, '20arcsec', '3pixel'
       gwidth -- HWHM for gaussian. Effective only for 
                 'GAUSS' and 'GJINC'.
           default: '-1' (use default for each gridfunction)
           example: 3, '20arcsec', '3pixel'
       jwidth -- Width of jinc function. Effective only for 
                 'GJINC'.
           default: '-1' (use default for each gridfunction)
           example: 3, '20arcsec', '3pixel'
imsize -- x and y image size in pixels, symmetric for single value
        default: [] (=cover all pointings in MS)
        example: imsize=200 (equivalent to [200,200])
cell -- x and y cell size. default unit arcmin
        default: '' (= 1/3 of FWHM of primary beam)
        example: cell=['0.2arcmin, 0.2arcmin']
                 cell='0.2arcmin' (equivalent to example above)
phasecenter -- image phase center: direction measure or field ID
        default: '' (= the center of pointing directions in 
                     POINTING table of infiles)
        example: 6 (field id), 'J2000 13h44m00 -17d02m00',
                 'AZEL -123d48m29 15d41m41'
projection -- map projection type. See Calabretta & Greisen (2002) for detail.
        default: 'SIN' 
        options: 'SIN', 'CAR', 'TAN', 'SFL'
ephemsrcname -- ephemeris source name for moving source (solar sytem objects)
        default: '' (none)
        If specified source name matches one of the solar system 
        objects known by CASA (see examples below), the task realigns 
        the data by correcting spatial shifts of the source during 
        observation, so that the source appears to be fixed in the 
        image. If specified name doesn't match, the task will fail. 
        When moving source correction is applied, the source is fixed 
        to the position at the beginning of the on-source observation 
        in the data. Direction reference frame of output image refers 
        phasecenter (it is 'J2000' if phasecenter is empty). Note that 
        moving source correction is not applied unless the user 
        explicitly set ephemsrcname even if target field is one of 
        the solar system objects known by CASA. Note also that setting 
        'pointing_offset' or 'source_offset' to directioncolumn 
        disables moving source correction so that these values should 
        not be used when the user wants to activate moving source 
        correction. 
        examples: 'MERCURY', 'VENUS', 'MARS', 'JUPITER', 'SATURN',
                  'URANUS', 'NEPTUNE', 'PLUTO', 'SUN', 'MOON'
pointingcolumn -- pointing data column to use
        option: 'direction', 'target', 'pointing_offset', 'source_offset', encoder' 
        default: 'direction'
restfreq -- specify rest frequency to use for output image
        default: '' (refer input data)
        example: 1.0e11, '100GHz'
stokes -- stokes parameters or polarization types to image
        default: '' (use all polarizations)
        example: 'XX'
minweight -- Minimum weight ratio to the median of weight used in 
             weight correction and weight based masking
        default: 0.1
        example: minweight = 0.
brightnessunit -- Overwrite the brightness unit in image.
        default: '' (use the unit in MS)
        Options: '', 'K' (Kelvin), 'Jy/beam'
clipminmax -- Clip minimum and maximum value from each pixel. 
              Note the benefit of clipping is lost when the number of 
              integrations contributing to each gridded pixel is small, 
              or where the incidence of spurious datapoints is 
              approximately or greater than the number of beams (in area) 
              encompassed by expected image.
        default: False
        option: True, False


-----------------
Gridding Kernel
-----------------
The parameter gridfunction sets gridding function (convolution kernel)
for imaging. Currently, the task supports 'BOX' (Box-car), 'SF' (Prolate
Spheroidal Wave Function), 'GAUSS' (Gaussian), 'GJINC' (Gaussian*Jinc),
where Jinc(x) = J_1(pi*x/c)/(pi*x/c) with a first order Bessel function
J_1, and 'PB' (Primary Beam). For 'PB', correct antenna informations
should be included in input file.

There are four subparameters for gridfunction: convsupport, truncate, 
gwidth, and jwidth. The convsupport is an integer specifying cut-off 
radius for 'SF' in units of pixel. By default (convsupport=-1), 
the cut-off radius is set to 3 pixels. The truncate is a cut-off 
radius for 'GAUSS' or 'GJINC'. It accepts integer, float, and 
string values of numeric plus unit. Allowed units are angular 
units such as 'deg', 'arcmin', 'arcsec', and 'pixel'. Default unit 
is 'pixel' so that string without unit or numerical values (integer 
or float) will be interpreted as radius in pixel. Default value 
for truncate, which is used when negative radius is set, is 3*HWHM 
for 'GAUSS' and radius at first null for 'GJINC'. The gwidth is 
the HWHM of gaussian for 'GAUSS' and 'GJINC'. Default value is 
sqrt(log(2)) pixel for 'GAUSS' and 2.52*sqrt(log(2)) pixel for 
'GJINC'. The jwidth specifies width of the jinc function (parameter 
'c' in the definition above). Default is 1.55 pixel. Both gwidth 
jwidth allows integer, float, or string of numeric plus unit. 
Default values for gwidth and jwidth are taken from Mangum et al. 
(2007). Formula for 'GAUSS' and 'GJINC' are taken from Table 1 in 
the paper, and are written as below using gwidth and jwidth: 

   GAUSS: exp[-log(2)*(|r|/gwidth)**2]

   GJINC: J_1(pi*|r|/jwidth)/(pi*|r|/jwidth)
             * exp[-log(2)*(|r|/gwidth)^2]  


Reference: Mangum, et al. 2007, A&A, 474, 679-687 

--------------------
Mask in Output Image
--------------------
The parameter minweight defines a threshold of weight values 
to mask. The pixels in outfile whose weight is smaller than
minweight*median(weight) are masked out. The task also creates
a weight image with the name outfile.weight.

  
        """
        if type(infiles)==str: infiles=[infiles]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infiles'] = infiles
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['mode'] = mode
        mytmp['nchan'] = nchan
        mytmp['start'] = start
        mytmp['width'] = width
        mytmp['veltype'] = veltype
        mytmp['outframe'] = outframe
        mytmp['gridfunction'] = gridfunction
        mytmp['convsupport'] = convsupport
        mytmp['truncate'] = truncate
        mytmp['gwidth'] = gwidth
        mytmp['jwidth'] = jwidth
        mytmp['imsize'] = imsize
        mytmp['cell'] = cell
        mytmp['phasecenter'] = phasecenter
        mytmp['projection'] = projection
        mytmp['ephemsrcname'] = ephemsrcname
        mytmp['pointingcolumn'] = pointingcolumn
        mytmp['restfreq'] = restfreq
        mytmp['stokes'] = stokes
        mytmp['minweight'] = minweight
        mytmp['brightnessunit'] = brightnessunit
        mytmp['clipminmax'] = clipminmax
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'sdimaging.xml')

        casalog.origin('sdimaging')
        if trec.has_key('sdimaging') and casac.utils().verify(mytmp, trec['sdimaging']) :
            result = task_sdimaging.sdimaging(infiles, outfile, overwrite, field, spw, antenna, scan, intent, mode, nchan, start, width, veltype, outframe, gridfunction, convsupport, truncate, gwidth, jwidth, imsize, cell, phasecenter, projection, ephemsrcname, pointingcolumn, restfreq, stokes, minweight, brightnessunit, clipminmax)

        else :
          result = False
        return result
