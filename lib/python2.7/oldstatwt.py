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
import task_oldstatwt
def oldstatwt(vis='', dorms=False, byantenna=False, sepacs=True, fitspw='', fitcorr='', combine='', timebin='0s', minsamp=2, field='', spw='', antenna='', timerange='', scan='', intent='', array='', correlation='', observation='', datacolumn='corrected'):

        """ Reweight visibilities according to their scatter (Experimental)

    The WEIGHT and SIGMA columns of measurement sets are often set to arbitrary
    values (e.g. 1), or theoretically estimated from poorly known antenna and
    receiver properties.  Many tasks (e.g. clean) are insensitive to an overall
    scale error in WEIGHT, but are affected by errors in the relative weights
    between visibilities.  Other tasks, such as uvmodelfit, or anything which
    depends on theoretical estimates of the noise, require (reasonably) correct
    weights and sigmas.  oldstatwt empirically measures the visibility scatter
    (typically as a function of time, antenna, and/or baseline) and uses that
    to set WEIGHT and SIGMA. It is important that all necessary calibrations
    are applied to the data prior to running this task for correct determination of
    weights and sigmas.

    Note: Some of the parameters (byantenna, sepacs, fitcorr, and timebin)
          are not fully implemented for CASA 3.4.


        Keyword arguments:
        vis -- Name of the measurement set.
                default: none; example: vis='ngc5921.ms'

        dorms -- Estimate the scatter using rms instead of the standard
                 deviation?

                 Ideally the visibilities used to estimate the scatter, as
                 selected by fitspw and fitcorr, should be pure noise.  If you
                 know for certain that they are, then setting dorms to True
                 will give the best result.  Otherwise, use False (standard
                 sample standard deviation).  More robust scatter estimates
                 like the interquartile range or median absolute deviation from
                 the median are not offered because they require sorting by
                 value, which is not possible for complex numbers.
               default: False

        byantenna -- Assume that the noise is factorable by antenna (feed).
                     If false, treat it separately for each baseline
                     (recommended if there is strong signal).
               default: False (*** byantenna=True is not yet implemented)

        sepacs -- If solving by antenna, treat autocorrelations separately.
                  (Acknowledge that what autocorrelations "see" is very
                   different from what crosscorrelations see.)
               default: True (*** not yet implemented)


        --- Data Selection (see help par.selectdata for more detailed
            information)

        fitspw -- The (ideally) signal-free spectral window:channels to
                  estimate the scatter from.
               default: '' (All)

        fitcorr -- The (ideally) signal-free correlations to
                   estimate the scatter from.
               default: '' (All)
               *** not yet implemented

        combine -- Let samples span multiple spws, corrs, scans, and/or states.
                   combine = 'spw': Recommended when a line spans an entire spw
                                    - set fitspw to the neighboring spws and
                                    apply their weight to the line spw(s).
                                    However, the effect of the line signal per
                                    visibility may be relatively harmless
                                    compared to the noise difference between
                                    spws.
                   combine = 'scan': Can be useful when the scan number
                                     goes up with each integration,
                                     as in many WSRT MSes.
                   combine = ['scan', 'spw']: disregard scan and spw
                                              numbers when gathering samples.
                   combine = 'spw,scan': Same as above.
              default: '' (None)

        timebin -- Sample interval.
                   default: '0s' or '-1s' (1 integration at a time)
                   example: timebin='30s'
                            '10' means '10s'
                   *** not yet implemented

        minsamp -- Minimum number of unflagged visibilities for estimating the
                   scatter.  Selected visibilities for which the weight cannot
                   be estimated will be flagged.  Note that minsamp is
                   effectively at least 2 if dorms is False, and 1 if it is
                   True.

        field -- Select field using field id(s) or field name(s).
                  [run listobs to obtain the list id's or names]
               default: ''=all fields If field string is a non-negative
               integer, it is assumed to be a field index
               otherwise, it is assumed to be a field name
               field='0~2'; field ids 0,1,2
               field='0,4,5~7'; field ids 0,4,5,6,7
               field='3C286,3C295'; fields named 3C286 and 3C295
               field = '3,4C*'; field id 3, all names starting with 4C

        spw -- Select spectral window/channels for changing WEIGHT and SIGMA.
               default: ''=all spectral windows and channels
               spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
               spw='<2';  spectral windows less than 2 (i.e. 0,1)
               spw='0:5~61'; spw 0, channels 5 to 61
               spw='0,10,3:3~45'; spw 0,10 all channels, spw 3 - chans 3 to 45.
               spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
               spw = '*:3~64'  channels 3 through 64 for all sp id's
                       spw = ' :3~64' will NOT work.
               oldstatwt does not support multiple channel ranges per spectral
               window (';') because it is not clear whether to keep the ranges
               in the original spectral window or make a new spectral window
               for each additional range.

        antenna -- Select antennas/baselines for changing WEIGHT and SIGMA.
               default: '' (all)
                Non-negative integers are assumed to be antenna indices, and
                anything else is taken as an antenna name.

                Examples:
                antenna='5&6': baseline between antenna index 5 and index 6.
                antenna='VA05&VA06': baseline between VLA antenna 5 and 6.
                antenna='5&6;7&8': baselines 5-6 and 7-8
                antenna='5': all baselines with antenna 5
                antenna='5,6,10': all baselines including antennas 5, 6, or 10
                antenna='5,6,10&': all baselines with *only* antennas 5, 6, or
                                       10.  (cross-correlations only.  Use &&
                                       to include autocorrelations, and &&&
                                       to get only autocorrelations.)
                antenna='!ea03,ea12,ea17': all baselines except those that
                                           include EVLA antennas ea03, ea12, or
                                           ea17.
        timerange -- Select data based on time range:
               default = '' (all); examples,
               timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
               Note: if YYYY/MM/DD is missing date, timerange defaults to the
               first day in the dataset
               timerange='09:14:0~09:54:0' picks 40 min on first day
               timerange='25:00:00~27:30:00' picks 1 hr to 3 hr 30min
               on next day
               timerange='09:44:00' data within one integration of time
               timerange='>10:24:00' data after this time
        scan -- Scan number range
            default: ''=all
        intent -- Select by scan intent (state).  Case sensitive.
            default: '' = all
            Examples:
            intent = 'CALIBRATE_ATMOSPHERE_REFERENCE'
            intent = 'calibrate_atmosphere_reference'.upper() # same as above
            # Select states that include one or both of CALIBRATE_WVR.REFERENCE
            # or OBSERVE_TARGET_ON_SOURCE.
            intent = 'CALIBRATE_WVR.REFERENCE, OBSERVE_TARGET_ON_SOURCE'
        array -- (Sub)array number range
            default: ''=all
        correlation -- Select correlations, e.g. 'rr, ll' or ['XY', 'YX'].
                       default '' (all).
                       NB: In CASA v4.5, non-trivial correlation selection has
                       been disabled since it was not working correctly, and
                       it is likely undesirable to set the weights in a
                       correlation-dependent way.

        observation -- Select by observation ID(s).
                       default: '' = all
       datacolumn -- Which data column to calculate the scatter from
                  default='corrected'; example: datacolumn='data'
                  Options: 'data', 'corrected', 'model', 'float_data'
                  note: 'corrected' will fall back to DATA if CORRECTED_DATA
                        is absent.


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['dorms'] = dorms
        mytmp['byantenna'] = byantenna
        mytmp['sepacs'] = sepacs
        mytmp['fitspw'] = fitspw
        mytmp['fitcorr'] = fitcorr
        mytmp['combine'] = combine
        mytmp['timebin'] = timebin
        mytmp['minsamp'] = minsamp
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['antenna'] = antenna
        mytmp['timerange'] = timerange
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['array'] = array
        mytmp['correlation'] = correlation
        mytmp['observation'] = observation
        mytmp['datacolumn'] = datacolumn
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'oldstatwt.xml')

        casalog.origin('oldstatwt')
        if trec.has_key('oldstatwt') and casac.utils().verify(mytmp, trec['oldstatwt']) :
            result = task_oldstatwt.oldstatwt(vis, dorms, byantenna, sepacs, fitspw, fitcorr, combine, timebin, minsamp, field, spw, antenna, timerange, scan, intent, array, correlation, observation, datacolumn)

        else :
          result = False
        return result
