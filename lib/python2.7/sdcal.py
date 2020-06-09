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
import task_sdcal
def sdcal(infile='', calmode='ps', fraction='10%', noff=-1, width=0.5, elongated=False, applytable='', interp='', spwmap={}, outfile='', overwrite=False, field='', spw='', scan='', intent=''):

        """ MS SD calibration task
Keyword arguments:
infile -- Name of input SD dataset
calmode -- Calibration mode. If you want to generate calibration table 
           or apply existing calibration tables, set calmode to a simple 
           string. If you want to calibrate data on-the-fly, set calmode 
           to a composite (comma-separated) string. So far, sky calibration has  
           three types, 'ps', 'otfraster' and 'otf'. If observation is 
           configured to observe reference position, calmode must be 
           'ps'. Otherwise, 'otfraster' or 'otf' should be used.
        options: 'ps','otfraster','otf','tsys','apply'
        default: 'ps'
        example: Here is an example for composite calmode.
                 'ps,apply' (do sky cal and apply)
                 'ps,tsys,apply' (do sky and Tsys cal and apply)
    >>> calmode expandable parameter
        fraction -- Edge marker parameter of 'otfraster'.
                    Specify a number of OFF integrations (at each
                    side of the raster rows in 'otfraster' mode)
                    as a fraction of total number of integrations.
                    In 'otfraster' mode, number of integrations 
                    to be marked as OFF, n_off, is determined by 
                    the following formula,

                        n_off = floor(fraction * n),

                    where n is number of integrations per raster 
                    row. Note that n_off from both sides will be  
                    marked as OFF so that twice of specified 
                    fraction will be marked at most. For example, 
                    if you specify fraction='10%', resultant 
                    fraction of OFF integrations will be 20% at 
                    most.
                default: '10%'
                options: '20%' in string style or float value less 
                         than 1.0 (e.g. 0.15).
                         'auto' is available only for 'otfraster'. 
        noff -- Edge marking parameter for 'otfraster'.
                It is used to specify a number of OFF spectra near 
                edge directly. Value of noff comes before setting 
                by fraction. Note that n_off from both sides will 
                be marked as OFF so that twice of specified noff 
                will be marked at most.
                default: -1 (use fraction)
                options: any positive integer

        applytable -- List of sky/Tsys calibration tables you want to 
                      apply.
                default: ''
        interp -- Interpolation method in time and frequency axis. 
                  Set comma separated method strings if you want 
                  to use different interpolation in time and 
                  frequency. 
                options: 'linear', 'nearest', 'cspline', 'cubic', 
                         any numeric string indicating an order 
                         of polynomial.
                         Note that 'cubic' is available for time only, 
                         and that 'cspline' and numeric strings are 
                         available for frequency only.
                default: '' (linear in time and frequency)
                example: 'linear,cspline' (linear in time, cubic 
                                           spline in frequency)
                         'linear,3' (linear in time, third order 
                                     polynomial in frequency)
                         'nearest' (nearest in time and frequency)
        spwmap -- Dictionary defining transfer of Tsys calibration. 
                  Key must be spw for Tsys and its value must be 
                  a list of spws for science target.
                default: {}
                example: {1: [5,6], 3: [7,8]}
                         Tsys in spw 1 is transferred to spws 5 and 6 
                         while Tsys in spw 3 is to spws 7 and 8.
field -- select data by field IDs and names
        default: '' (use all fields)
        example: field='3C2*' (all names starting with 3C2)
                 field='0,4,5~7' (field IDs 0,4,5,6,7)
                 field='0,3C273' (field ID 0 or field named 3C273)
        this selection is in addition to the other selections to data
spw -- select data by spw IDs (spectral windows)
        NOTE this task only supports spw ID selction and ignores channel
        selection.
        default: '' (use all spws and channels)
        example: spw='3,5,7' (spw IDs 3,5,7; all channels)
                 spw='<2' (spw IDs less than 2, i.e., 0,1; all channels)
                 spw='30~45GHz' (spw IDs with the center frequencies in range 30-45GHz; all channels)
        this selection is in addition to the other selections to data
        NOTE spw input must be '' (''= all) in calmode='tsys'.
scan -- select data by scan numbers
        default: '' (use all scans)
        example: scan='21~23' (scan IDs 21,22,23)
        this selection is in addition to the other selections to data
        NOTE scan input must be '' (''= all) in calmode='tsys'.
outfile -- Name of output file
        NOTE if you omit and calmode doesn't include 'apply', the task 
        will use default outfile name based on infile and predefined 
        suffix ('_sky' for sky, '_tsys' for Tsys).
        default: '' (<infile>_<suffix> for calibration) 
overwrite -- overwrite the output file if already exists
        options: (bool) True,False
        default: False
        NOTE this parameter is ignored when outform='ASCII'


DESCRIPTION:

Task sdcal is an implementation of a calibration scheme like as 
interferometry, i.e., generate caltables and apply them. Available 
calibration modes are 'ps', 'otfraster', 'otf', and 'tsys'. 
Those modes generates caltables for sky or Tsys calibration. 
The caltables can be applied to the data by using calmode 'apply'.

First three calibration modes, 'ps', 'otfraster', and 'otf', 
generate sky calibration tables. The user should choose appropriate 
calibration mode depending on the data. Use case for each mode is 
as follows:

    'ps': position switch (including OTF) with explicit
          reference (OFF) spectra
    'otfraster': raster OTF scan without explicit OFFs
    'otf': fast-scan observation with Lissajous or 
           double-circle trajectory

So, if the data contains explicit reference spectra, 'ps' should
be used. The 'otfraster' mode is appropriate for raster OTF. 
For non-raster OTF data, 'otf' mode is available to support fast-
scanning observation. In 'otfraster' mode, the task first try to 
find several integrations near edge as OFF spectra, then the data 
are calibrated using those OFFs. If the observing pattern is raster, 
you should use the 'otfraster' mode to calibrate data. 
The 'otfraster' mode is designed for OTF observations without 
explicit OFF spectra. However, these modes should work even if
explicit reference spectra exist. In this case, these spectra will be
ignored and spectra near edges detected by edge marker will be used as
reference. In 'otf' mode, the task detects integrations near edges of 
observed area, and detected integrations are regarded as OFFs. 
This mode is specifically designed for fast-scan mode, which takes 
the data contiguously by moving antenna along trajectory that 
imitates random spatial data sampling, which is implemented as 
either Lissajous or double-circle pattern. 


Except for how to choose OFFs, the procedure to derive calibrated
spectra is common for the above three modes. Selected (or preset) OFF
integrations are separated by its continuity in time domain, averaged in
each segment, then interpolated to timestamps for ON integrations.
Effectively, it means that OFF integrations are averaged by each
OFF spectrum for 'ps' mode, averaged by either ends of each raster
row for 'otfraster' mode. The formula for calibrated spectrum
is

    Tsys * (ON - OFF) / OFF. 
  
You can calibrate data on-the-fly like sdcal task by setting 
calmode to a composite calmode string separated by comma. 
For example, calmode='ps,apply' means doing sky calibration and 
apply it on-the-fly. In this case, caltable is generated as a 
temporary plain table and will be deleted at the end.
Allowed calibration modes in this task is as follows:

    ps
        generate sky caltable using 'ps' mode
    otfraster
        generate sky caltable using 'otfraster' mode
    otf
        generate sky caltable using 'otf' mode
    tsys
        generate tsys caltable
    apply
        apply caltables specified by applytable parameter
    ps,apply
        generate temporary sky caltable using 'ps' mode and
        apply it. also apply caltables specified by applytable 
    ps,tsys,apply
        generate temporary sky caltable using 'ps' mode as well
        as temporary tsys caltable, and apply them. 
    otfraster,apply
        generate temporary sky caltable using 'otfraster' mode
        and apply it. also apply caltables specified by applytable 
    otfraster,tsys,apply
        generate temporary sky caltable using 'otfraster' mode
        as well as temporary tsys caltable, and apply them. 
    otf,apply
        generate temporary sky caltable using 'otf' mode
        and apply it. also apply caltables specified by applytable 
    otf,tsys,apply
        generate temporary sky caltable using 'otf' mode
        as well as temporary tsys caltable, and apply them. 

There are several control parameters for sky/Tsys calibration and 
application of caltables. See the above parameter description.

In ALMA, Tsys measurement is usually done using different spectral
setup from spectral windows for science target. In this case, sdcal
transfers Tsys values to science spectral windows in the application
stage. To do that, the user has to give a list of spectral windows for
Tsys measurement as well as mapping between spectral windows for Tsys
measurement and scicence target. These can be specified by parameters
'tsysspw' and 'spwmap', which are defined as subparameters of 'calmode'.
For example, suppose that Tsys measurements for science windows 17, 19,
21, and 23 are done in spw 9, 11, 13, and 15, respectively. 
In this case, tsysspw and spwmap should be specified as follows:

    tsysspw = '9,11,13,15'
    spwmap = {9:[17],11:[19],13:[21],15:[23]}

Below is an example of full specification of task parameters for calmode
of 'ps,tsys,apply':

    default(sdcal)
    infile = 'foo.ms'
    calmode = 'ps,tsys,apply'
    spw = ''
    tsysspw = '9,11,13,15'
    spwmap = {9:[17],11:[19],13:[21],15:[23]}
    sdcal()

Note that, in contrast to applycal task, spwmap must be a dictionary
with Tsys spectral window as key and a list of corresponding science
spectral window as value. Note also that the parameter 'spw' should
not be used to specify a list of spectral windows for Tsys measurement.
It is intended to select data to be calibrated so that the list should
contain spectral windows for both science target and Tsys measurement.
The task will fail if you use 'spw' instead of 'tsysspw'. 


For Tsys calibration, the user is able to choose whether Tsys is
averaged in spectral axis or not. If tsysavg is False (default),
resulting Tsys is spectral value. On the other hand, when tsysavg
is True, Tsys is averaged in spectral axis before output. The channel
range for averaging is whole channels by default. If channel range is
specified by tsysspw string, it is used for averaging. The user can
specify channel range with ms selection syntax. For example,

    tsysspw = '1:0~100'

specifies spw 1 for Tsys calibration and channel range between channel
0 and 100 for averaging. You can specify more than one ranges per spw.

    tsysspw = '1:0~100;200~400'

In this case, selected ranges are between 0 and 100 plus 200 and 400.
Note that even if multiple ranges are selected, the task average whole
ranges together and output single averaged value. You can specify multiple
spws by separating comma.

    tsysspw = '1:0~100,3:400~500'
Note that specified channel range is ignored if tsysavg is False.
  
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['calmode'] = calmode
        mytmp['fraction'] = fraction
        mytmp['noff'] = noff
        mytmp['width'] = width
        mytmp['elongated'] = elongated
        mytmp['applytable'] = applytable
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'sdcal.xml')

        casalog.origin('sdcal')
        if trec.has_key('sdcal') and casac.utils().verify(mytmp, trec['sdcal']) :
            result = task_sdcal.sdcal(infile, calmode, fraction, noff, width, elongated, applytable, interp, spwmap, outfile, overwrite, field, spw, scan, intent)

        else :
          result = False
        return result
