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
from task_sdimaging import sdimaging
class sdimaging_cli_:
    __name__ = "sdimaging"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (sdimaging_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'infiles':None, 'outfile':None, 'overwrite':None, 'field':None, 'spw':None, 'antenna':None, 'scan':None, 'intent':None, 'mode':None, 'nchan':None, 'start':None, 'width':None, 'veltype':None, 'outframe':None, 'gridfunction':None, 'convsupport':None, 'truncate':None, 'gwidth':None, 'jwidth':None, 'imsize':None, 'cell':None, 'phasecenter':None, 'projection':None, 'ephemsrcname':None, 'pointingcolumn':None, 'restfreq':None, 'stokes':None, 'minweight':None, 'brightnessunit':None, 'clipminmax':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, infiles=None, outfile=None, overwrite=None, field=None, spw=None, antenna=None, scan=None, intent=None, mode=None, nchan=None, start=None, width=None, veltype=None, outframe=None, gridfunction=None, convsupport=None, truncate=None, gwidth=None, jwidth=None, imsize=None, cell=None, phasecenter=None, projection=None, ephemsrcname=None, pointingcolumn=None, restfreq=None, stokes=None, minweight=None, brightnessunit=None, clipminmax=None, ):

        """SD task: imaging for total power and spectral data

        Detailed Description:

Task sdimaging creates an image from input single-dish data sets.
The input can be either total power and spectral data. 

The coordinate of output image is defined by four axes, i.e., two
spatial axes, frequency and polarization axes.\n
By default, spatial coordinate of image is defined so that the all
pointing directions in POINTING tables of input data sets are covered
with the cell size, 1/3 of FWHM of primary beam of antennas in the
first MS. Therefore, it is often easiest to leave spatial definitions
at the default values. It is also possible to define spatial axes of
the image by specifying the image center direction (phasecenter),
number of image pixel (imsize) and size of the pixel (cell).\n
The frequency coordinate of image is defined by three parameters,
the number of channels (nchan), the channel id/frequency/velocity of
the first channel (start), and channel width (width).There are three
modes available to define unit of start and width, i.e., 'channel' (use
channel indices), 'frequency' (use frequency unit, e.g., 'GHz'),
and 'velocity' (use velocity unit, e.g., 'km/s'). By default, nchan,
start, and width are defined so that all selected spectral windows are
covered with the channel width equal to separation of first two
channels selected.\n
Finally, polarizations of image is defined by stokes parameter or
polarization. For example, stokes='XXYY' produces an image cube with
each plane contains the image of one of the polarizations, while
stokes='I' produces a 'total intensity' or Stokes I image.\n

The task also supports various grid function (convolution kernel) to
weight spectra as well as an option to remove the most extreme minimum 
and maximum (unweighted) values prior to computing the gridded pixel 
values. See description below for details of gridfunction available.

  
        Arguments :
                infiles: a list of names of input SD Measurementsets (only MS is allowed for this task)
                   Default Value: 

                outfile: name of output image
                   Default Value: 

                overwrite: overwrite the output file if already exists [True, False]
                   Default Value: False

                field: select data by field IDs and names, e.g. "3C2*" (""=all)
                   Default Value: 

                spw: select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
                   Default Value: 

                antenna: select data by antenna names or IDs, e.g, "PM03" ("" = all antennas)
                   Default Value: 

                scan: select data by scan numbers, e.g. "21~23" (""=all)
                   Default Value: 

                intent: select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
                   Default Value: OBSERVE_TARGET#ON_SOURCE

                mode: spectral gridding type
                   Default Value: channel
                   Allowed Values:
                                channel
                                frequency
                                velocity

                nchan:  number of channels (planes) in output image (-1=all)
                   Default Value: -1

                start: start of output spectral dimension, e.g. "0", "110GHz", "-20km/s"
                   Default Value: 0

                width: width of output spectral channels
                   Default Value: 1

                veltype: velocity definition
                   Default Value: radio
                   Allowed Values:
                                radio
                                optical
                                true
                                relativistic

                outframe: velocity frame of output image (""=current frame or LSRK for multiple-MS inputs)
                   Default Value: 
                   Allowed Values:
                                lsrk
                                lsrd
                                bary
                                geo
                                topo
                                galacto
                                lgroup
                                cmb
                                

                gridfunction: gridding function for imaging (see description in help)
                   Default Value: BOX
                   Allowed Values:
                                BOX
                                PB
                                SF
                                GAUSS
                                GJINC
                                box
                                pb
                                sf
                                gauss
                                gjinc

                convsupport: convolution support for gridding
                   Default Value: -1

                truncate: truncation radius for gridding
                   Default Value: -1

                gwidth: HWHM for gaussian
                   Default Value: -1

                jwidth: c-parameter for jinc function
                   Default Value: -1

                imsize: x and y image size in pixels, e.g., [64,64]. Single value: same for both spatial axes ([] = number of pixels to cover whole pointings in MSes)
                   Default Value: 

                cell: x and y cell size, (e.g., ["8arcsec","8arcsec"]. default unit arcmin. ("" = 1/3 of FWHM of primary beam)
                   Default Value: 

                phasecenter: image center direction: position or field index, e.g., "J2000 17:30:15.0 -25.30.00.0". ("" = the center of pointing directions in MSes)
                   Default Value: 

                projection: map projection type
                   Default Value: SIN
                   Allowed Values:
                                SIN
                                CAR
                                TAN
                                SFL

                ephemsrcname: ephemeris source name, e.g. "MARS"
                   Default Value: 

                pointingcolumn: pointing data column to use
                   Default Value: direction
                   Allowed Values:
                                target
                                pointing_offset
                                source_offset
                                encoder
                                direction

                restfreq: rest frequency to assign to image, e.g., "114.5GHz"
                   Default Value: 

                stokes: stokes parameters or polarization types to image, e.g. "I", "XX"
                   Default Value: 

                minweight: Minimum weight ratio to the median of weight used in weight correction and weight beased masking
                   Default Value: 0.1
                   Allowed Values:
                                0

                brightnessunit: Overwrite the brightness unit in image (\'\' = respect the unit in MS) [\'K\' or \'Jy/beam\']
                   Default Value: 
                   Allowed Values:
                                
                                K
                                Jy/beam

                clipminmax: Clip minimum and maximum value from each pixel. Note the benefit of clipping is lost when the number of integrations contributing to each gridded pixel is small, or where the incidence of spurious datapoints is approximately or greater than the number of beams (in area) encompassed by expected image.
                   Default Value: False

        Returns: void

        Example :

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
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'sdimaging'
        self.__globals__['taskname'] = 'sdimaging'
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

            myparams['infiles'] = infiles = self.parameters['infiles']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['mode'] = mode = self.parameters['mode']
            myparams['nchan'] = nchan = self.parameters['nchan']
            myparams['start'] = start = self.parameters['start']
            myparams['width'] = width = self.parameters['width']
            myparams['veltype'] = veltype = self.parameters['veltype']
            myparams['outframe'] = outframe = self.parameters['outframe']
            myparams['gridfunction'] = gridfunction = self.parameters['gridfunction']
            myparams['convsupport'] = convsupport = self.parameters['convsupport']
            myparams['truncate'] = truncate = self.parameters['truncate']
            myparams['gwidth'] = gwidth = self.parameters['gwidth']
            myparams['jwidth'] = jwidth = self.parameters['jwidth']
            myparams['imsize'] = imsize = self.parameters['imsize']
            myparams['cell'] = cell = self.parameters['cell']
            myparams['phasecenter'] = phasecenter = self.parameters['phasecenter']
            myparams['projection'] = projection = self.parameters['projection']
            myparams['ephemsrcname'] = ephemsrcname = self.parameters['ephemsrcname']
            myparams['pointingcolumn'] = pointingcolumn = self.parameters['pointingcolumn']
            myparams['restfreq'] = restfreq = self.parameters['restfreq']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['minweight'] = minweight = self.parameters['minweight']
            myparams['brightnessunit'] = brightnessunit = self.parameters['brightnessunit']
            myparams['clipminmax'] = clipminmax = self.parameters['clipminmax']

        if type(infiles)==str: infiles=[infiles]

        result = None

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
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'sdimaging.xml')

        casalog.origin('sdimaging')
        try :
          #if not trec.has_key('sdimaging') or not casac.casac.utils().verify(mytmp, trec['sdimaging']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['sdimaging'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('sdimaging', 'sdimaging.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'sdimaging'
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
          result = sdimaging(infiles, outfile, overwrite, field, spw, antenna, scan, intent, mode, nchan, start, width, veltype, outframe, gridfunction, convsupport, truncate, gwidth, jwidth, imsize, cell, phasecenter, projection, ephemsrcname, pointingcolumn, restfreq, stokes, minweight, brightnessunit, clipminmax)

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
             tname = 'sdimaging'
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
#        paramgui.runTask('sdimaging', myf['_ip'])
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
        a['infiles']  = ['']
        a['outfile']  = ''
        a['overwrite']  = False
        a['field']  = ''
        a['spw']  = ''
        a['antenna']  = ''
        a['scan']  = ''
        a['intent']  = 'OBSERVE_TARGET#ON_SOURCE'
        a['mode']  = 'channel'
        a['outframe']  = ''
        a['gridfunction']  = 'BOX'
        a['imsize']  = []
        a['cell']  = ''
        a['phasecenter']  = ''
        a['projection']  = 'SIN'
        a['ephemsrcname']  = ''
        a['pointingcolumn']  = 'direction'
        a['restfreq']  = ''
        a['stokes']  = ''
        a['minweight']  = 0.1
        a['brightnessunit']  = ''
        a['clipminmax']  = False

        a['mode'] = {
                    0:odict([{'value':'channel'}, {'nchan':-1}, {'start':''}, {'width':''}]), 
                    1:odict([{'value':'frequency'}, {'nchan':-1}, {'start':''}, {'width':''}]), 
                    2:odict([{'value':'velocity'}, {'nchan':-1}, {'start':''}, {'width':''}, {'veltype':'radio'}])}
        a['gridfunction'] = {
                    0:{'value':'BOX'}, 
                    1:{'value':'box'}, 
                    2:odict([{'value':'SF'}, {'convsupport':-1}]), 
                    3:odict([{'value':'sf'}, {'convsupport':-1}]), 
                    4:{'value':'PB'}, 
                    5:{'value':'pb'}, 
                    6:odict([{'value':'GAUSS'}, {'truncate':-1}, {'gwidth':-1}]), 
                    7:odict([{'value':'gauss'}, {'truncate':-1}, {'gwidth':-1}]), 
                    8:odict([{'value':'GJINC'}, {'truncate':-1}, {'gwidth':-1}, {'jwidth':-1}]), 
                    9:odict([{'value':'gjinc'}, {'truncate':-1}, {'gwidth':-1}, {'jwidth':-1}])}

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
    def description(self, key='sdimaging', subkey=None):
        desc={'sdimaging': 'SD task: imaging for total power and spectral data',
               'infiles': 'a list of names of input SD Measurementsets (only MS is allowed for this task)',
               'outfile': 'name of output image',
               'overwrite': 'overwrite the output file if already exists [True, False]',
               'field': 'select data by field IDs and names, e.g. "3C2*" (""=all)',
               'spw': 'select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)',
               'antenna': 'select data by antenna names or IDs, e.g, "PM03" ("" = all antennas)',
               'scan': 'select data by scan numbers, e.g. "21~23" (""=all)',
               'intent': 'select data by observational intent, e.g. "*ON_SOURCE*" (""=all)',
               'mode': 'spectral gridding type ["channel", "frequency", "velocity"]',
               'nchan': ' number of channels (planes) in output image (-1=all)',
               'start': 'start of output spectral dimension, e.g. "0", "110GHz", "-20km/s"',
               'width': 'width of output spectral channels',
               'veltype': 'velocity definition ["radio", "optical", "true" or "relativistic"] ',
               'outframe': 'velocity frame of output image ["lsrk", "lsrd", "bary", "geo", "topo", "galacto", "lgroup", "cmb"] (""=current frame or LSRK for multiple-MS inputs) ',
               'gridfunction': 'gridding function for imaging ["BOX", "SF", "PB", "GAUSS" or "GJINC"] (see description in help)',
               'convsupport': 'convolution support for gridding',
               'truncate': 'truncation radius for gridding',
               'gwidth': 'HWHM for gaussian',
               'jwidth': 'c-parameter for jinc function',
               'imsize': 'x and y image size in pixels, e.g., [64,64]. Single value: same for both spatial axes ([] = number of pixels to cover whole pointings in MSes)',
               'cell': 'x and y cell size, (e.g., ["8arcsec","8arcsec"]. default unit arcmin. ("" = 1/3 of FWHM of primary beam)',
               'phasecenter': 'image center direction: position or field index, e.g., "J2000 17:30:15.0 -25.30.00.0". ("" = the center of pointing directions in MSes)',
               'projection': 'map projection type',
               'ephemsrcname': 'ephemeris source name, e.g. "MARS"',
               'pointingcolumn': 'pointing data column to use ["direction", "target", "pointing_offset", "source_offset" or "encoder"]',
               'restfreq': 'rest frequency to assign to image, e.g., "114.5GHz"',
               'stokes': 'stokes parameters or polarization types to image, e.g. "I", "XX"',
               'minweight': 'Minimum weight ratio to use',
               'brightnessunit': 'Overwrite the brightness unit in image (\'\' = respect the unit in MS) [\'K\' or \'Jy/beam\']',
               'clipminmax': 'Clip minimum and maximum value from each pixel',

              }

#
# Set subfields defaults if needed
#
        if(subkey == 'channel'):
          desc['start'] = 'Begin the output cube at the frequency of this channel in the MS'
        if(subkey == 'channel'):
          desc['width'] = 'Width of output channel relative to MS channel (# to average)("" = 1 channel) '
        if(subkey == 'frequency'):
          desc['start'] = 'Frequency of first channel: e.g. "1.4GHz" (""= first channel in first SpW of MS)'
        if(subkey == 'frequency'):
          desc['width'] = 'Channel width: e.g "1.0kHz"(""=width of first channel in first SpW of MS)'
        if(subkey == 'velocity'):
          desc['start'] = 'Velocity of first channel: e.g "0.0km/s"(""=first channel in first SpW of MS)'
        if(subkey == 'velocity'):
          desc['width'] = 'Channel width e.g "-1.0km/s" (""=width of first channel in first SpW of MS)'

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['infiles']  = ['']
        a['outfile']  = ''
        a['overwrite']  = False
        a['field']  = ''
        a['spw']  = ''
        a['antenna']  = ''
        a['scan']  = ''
        a['intent']  = 'OBSERVE_TARGET#ON_SOURCE'
        a['mode']  = 'channel'
        a['nchan']  = -1
        a['start']  = 0
        a['width']  = 1
        a['veltype']  = 'radio'
        a['outframe']  = ''
        a['gridfunction']  = 'BOX'
        a['convsupport']  = -1
        a['truncate']  = -1
        a['gwidth']  = -1
        a['jwidth']  = -1
        a['imsize']  = []
        a['cell']  = ''
        a['phasecenter']  = ''
        a['projection']  = 'SIN'
        a['ephemsrcname']  = ''
        a['pointingcolumn']  = 'direction'
        a['restfreq']  = ''
        a['stokes']  = ''
        a['minweight']  = 0.1
        a['brightnessunit']  = ''
        a['clipminmax']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mode']  == 'channel':
            a['nchan'] = -1
            a['start'] = ''
            a['width'] = ''

        if self.parameters['mode']  == 'frequency':
            a['nchan'] = -1
            a['start'] = ''
            a['width'] = ''

        if self.parameters['mode']  == 'velocity':
            a['nchan'] = -1
            a['start'] = ''
            a['width'] = ''
            a['veltype'] = 'radio'

        if self.parameters['gridfunction']  == 'SF':
            a['convsupport'] = -1

        if self.parameters['gridfunction']  == 'sf':
            a['convsupport'] = -1

        if self.parameters['gridfunction']  == 'GAUSS':
            a['truncate'] = -1
            a['gwidth'] = -1

        if self.parameters['gridfunction']  == 'gauss':
            a['truncate'] = -1
            a['gwidth'] = -1

        if self.parameters['gridfunction']  == 'GJINC':
            a['truncate'] = -1
            a['gwidth'] = -1
            a['jwidth'] = -1

        if self.parameters['gridfunction']  == 'gjinc':
            a['truncate'] = -1
            a['gwidth'] = -1
            a['jwidth'] = -1

        if a.has_key(paramname) :
              return a[paramname]
sdimaging_cli = sdimaging_cli_()
