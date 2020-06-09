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
import task_sdgaincal
def sdgaincal(infile='', calmode='doublecircle', radius='', smooth=True, antenna='', field='', spw='', scan='', intent='', applytable='', interp='', spwmap=[], outfile='', overwrite=False):

        """ MS SD gain calibration task
Keyword arguments:
infile -- Name of input SD dataset
calmode -- Gain calibration mode. Currently, only 'doublecircle' is supported.
        options: 'doublecircle'
        default: 'doublecircle'
    >>> calmode expandable parameter
        radius -- Radius of the central region for double circle calibration.
                  Default ('') is a radius of the primary beam. If numeric value
                  is given, it is interpreted as a value in arcsec.
                default: ''
                options: '20arcsec', 20.0
        smooth -- Whether apply smoothing during gain calibration or not.
                options: (bool) True, False
                default: True
antenna -- select data by antenna name or ID
        default: '' (use all antennas)
        example: 'PM03'
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
intent -- select data by observational intent, also referred to as 'scan intent'
        default: '' (use all scan intents)
        example: intent='*ON_SOURCE*' (any valid scan-intent expression accepted by the MSSelection module can be specified)
        this selection is in addition to the other selections to data
applytable -- List of sky/Tsys calibration tables you want to pre-apply.
                default: ''
    >>> applytable expandable parameter
       interp -- Interpolation type (in time[,freq]) to use for each gaintable.
                When frequency interpolation is relevant (bandpass solutions,
                frequency-dependent polcal solutions, ALMA Tsys)
                separate time-dependent and freq-dependent interp
                types with a comma (freq _after_ the comma).
                Specifications for frequency are ignored when the
                calibration table has no channel-dependence.
                Time-dependent interp options ending in 'PD' enable a
                "phase delay" correction per spw for non-channel-dependent
                calibration types.
                For multi-obsId datasets, 'perobs' can be appended to
                the time-dependent interpolation specification to
                enforce obsId boundaries when interpolating in time.
                Add 'flag' to the freq-dependent interpolation options
                to enforce channel-dependent flagging (rather than
                interpolation/extrapolation).
                default: '' --> 'linear,linear' for all gaintable(s)
                example: interp='nearest'   (in time, freq-dep will be
                                             linear, if relevant)
                         interp='linear,cubic'  (linear in time, cubic
                                                 in freq)
                         interp='linearperobs,splineflag' (linear in time
                                                          per obsId,
                                                          spline in
                                                          freq with
                                                          channelized
                                                          flagging)
                         interp=',spline'  (spline in freq; linear in
                                            time by default)
                         interp=['nearest,spline','linear']  (for multiple gaintables)
                Options: Time: 'nearest', 'linear', 'nearestPD', 'linearPD'
                         Freq: 'nearest', 'linear', 'cubic', 'spline',
                               'nearestflag', 'linearflag', 'cubicflag', 'splineflag',

       spwmap -- Spectral windows combinations to form for gaintable(s)
               default: [] (apply solutions from each spw to that spw only)
               Example:  spwmap=[0,0,1,1] means apply the caltable solutions
                         from spw = 0 to the spw 0,1 and spw 1 to spw 2,3.
                         spwmap=[[0,0,1,1],[0,1,0,1]]  (for multiple gaintables)

          Complicated example:

            gaintable=['tab1','tab2','tab3']
            gainfield='3C286'
            interp=['linear','nearest']
            spwmap=[[],[0,0,2]]

            This means: apply 3 cal tables, selecting only solutions for 3C286
            from tab1 (but all fields from tab2 and tab3, indicated by
            no gainfield entry for these files).  Linear interpolation
            (in time) will be used for 'tab1' and 'tab3' (default); 'tab2' will
            use nearest.  For the 'tab2', the calibration spws map
            will be mapped to the data spws according to 0->0, 0->1, 2->2.
            (I.e., for data spw=0 and 2, the spw mapping is one to one,
            but data spw 1 will be calibrated by solutions from spw 0.)

outfile -- Name of output caltable.
        default: '' (<infile>_<suffix> for calibration)
overwrite -- overwrite the output caltable if already exists
        options: (bool) True,False
        default: False


DESCRIPTION:
sdgaincal computes and removes a time-dependent gain variation in single-dish
data on a per-spectral-window and per-antenna basis. Presently the task
operates only on data taken with the ALMA fast-mapped, double-circle
observation modes [1]. This task exploits the fact that the double-circle mode
observes the same position in the center of the mapped field, approximately
circular every sub-cycle, and normalizes the gains throughout the entire
dataset, relative to the measured brightness at the center position.

Note that this gain calibration task is done independently of the atmosphere
(i.e. Tsys) and sky calibration steps. This can be applied through the sdcal
task. Alternatively, you can pass those caltables to applytable parameter to
apply them on-the-fly prior to gain calibration.

Presently, this task has only one calibration mode: calmode='doublecircle'.
In this mode, the size of the region that CASA regards as "the center" is
user-configurable via the expandable 'radius' (in arcsec) parameter (under
'calmode'). The default is to use the size of the primary beam. The data can
also be smoothed in the time domain, prior to computation of the gain variation.
Selection is by specral window/channels, field IDs, and antenna through the spw,
field, and antenna selection parameters. The default is to use all data for the
gain calibration. The caltable can be output with the 'outfile' parameter.

REFERENCE:
[1] Phillips et al, 2015. Fast Single-Dish Scans of the Sun Using ALMA
  
        """
        if type(spwmap)==int: spwmap=[spwmap]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['calmode'] = calmode
        mytmp['radius'] = radius
        mytmp['smooth'] = smooth
        mytmp['antenna'] = antenna
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['applytable'] = applytable
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'sdgaincal.xml')

        casalog.origin('sdgaincal')
        if trec.has_key('sdgaincal') and casac.utils().verify(mytmp, trec['sdgaincal']) :
            result = task_sdgaincal.sdgaincal(infile, calmode, radius, smooth, antenna, field, spw, scan, intent, applytable, interp, spwmap, outfile, overwrite)

        else :
          result = False
        return result
