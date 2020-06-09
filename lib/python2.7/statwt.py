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
import task_statwt
def statwt(vis='', selectdata=True, field='', spw='', intent='', array='', observation='', scan='', combine='', timebin='0.001s', slidetimebin=False, chanbin='spw', minsamp=2, statalg='classic', fence=-1, center='mean', lside=True, zscore=-1, maxiter=-1, fitspw='', excludechans=False, wtrange=[], flagbackup=True, preview=False, datacolumn='corrected'):

        """Compute and set weights based on variance of data.
        IF NOT RUN IN PREVIEW MODE, THIS APPLICATION WILL MODIFY THE WEIGHT, WEIGHT SPECTRUM, FLAG,
        AND FLAG_ROW COLUMNS OF THE INPUT MS. IF YOU WANT A PRISTINE COPY OF THE INPUT MS TO BE
        PRESERVED, YOU SHOULD MAKE A COPY OF IT BEFORE RUNNING THIS APPLICATION.

        This application computes weights for the WEIGHT and WEIGHT_SPECTRUM (if present) columns
        based on the variance of values in the CORRECTED_DATA or DATA column. If the MS does not
        have the specified data column, the application will fail. The following algorithm is used:

        1. For unflagged data in each sample, create two sets of values, one set is composed solely
           of the real part of the data values, the other set is composed solely of the imaginary
           part of the data values.
        2. Compute the variance of each of these sets, vr and vi.
        3. Compute veq = (vr + vi)/2.
        4. The associated weight is just the reciprocal of veq. The weight will have unit
           of (data unit)^(-2), eg Jy^(-2).

        Data are aggregated on a per-baseline, per-data description ID basis. Data are aggregated
        in bins determined by the specified values of the timebin and chanbin parameters. By default,
        data for separate correlations are aggregated separately. This behavior can be overriden
        by specifying combine="corr" (see below).

        RULES REGARDING CREATING/INITIALIZING WEIGHT_SPECTRUM COLUMN

        1. If run in preview mode (preview=True), no data are modified and no columns are added.
        2. Else if the MS already has a WEIGHT_SPECTRUM and this column has been initialized (has values),
           it will always be populated with the new weights.  The WEIGHT column will be populated with
           the corresponding median values of the associated WEIGHT_SPECTRUM array.
        3. Else if the frequency range specified for the sample is not the default ("spw"), the
           WEIGHT_SPECTRUM column will be created (if it doesn't already exist) and the new weights
           will be written to it.  The WEIGHT column should be populated with the corresponding median
           values of the WEIGHT_SPECTRUM array.
        4. Otherwise the single value for each spectral window will be written to the WEIGHT column;
           the WEIGHT_SPECTRUM column will not be added if it doesn't already exist, and if it does,
           it will remain uninitialized (no values will be written to it).

        TIME BINNING

        One of two algorithms can be used for time binning. If slidetimebin=True, then
        a sliding time bin of the specified width is used. If slidetimebin=False, then
        block time processing is used. The sliding time bin algorithm will generally be
        both more memory intensive and take longer than the block processing algorithm.
        Each algorithm is discussed in detail below.

        If the value of timebin is an integer, it means that the specified value should be
        multiplied by the representative integration time in the MS. This integration is the
        median value of all the values in the INTERVAL column. Flags are not considered in
        the integration time computation. If either extrema in the INTERVAL column differs from
        the median by more than 25%, the application will fail because the values vary too much
        for there to be a single, representative, integration time. The timebin parameter can
        also be specified as a quantity (string) that must have time conformant units.

        Block Time Processing

        The data are processed in blocks. This means that all weight spectrum values will be set to
        the same value for all points within the same time bin/channel bin/correlation bin (
        see the section on channel binning and description of combine="corr" for more details on
        channel binning and correlation binning).
        The time bins are not necessarily contiguous and are not necessarily the same width. The start
        of a bin is always coincident with a value from the TIME column, So for example, if values
        from the time column are [20, 60, 100, 140, 180, 230], and the width of the bins is chosen
        to be 110s, the first bin would start at 20s and run to 130s, so that data from timestamps
        20, 60, and 100 will be included in the first bin. The second bin would start at 140s, so that
        data for timestamps 140, 180, and 230 would be included in the second bin. Also, time binning
        does not span scan boundaries, so that data associated with different scan numbers will
        always be binned separately; changes in SCAN_NUMBER will cause a new time bin to be created,
        with its starting value coincident with the time of the new SCAN_NUMBER. Similar behavior can
        be expected for changes in FIELD_ID and ARRAY_ID. One can override this behavior for some
        columns by specifying the combine parameter (see below).

        Sliding Time Window Processing

        In this case, the time window is always centered on the timestamp of the row in question
        and extends +/-timebin/2 around that timestamp, subject the the time block boundaries.
        Rows with the same baselines and data description IDs which are included in that window
        are used for determining the weight of that row. The boundaries of the time block to which
        the window is restricted are determined by changes in FIELD_ID, ARRAY_ID, and SCAN_NUMBER.
        One can override this behavior for FIELD_ID and/or SCAN_NUMBER by specifying the combine
        parameter (see below). Unlike the time block processing algorithm, this sliding time window
        algorithm requires that details all rows for the time block in question are kept in memory,
        and thus the sliding window algorithm in general requires more memory than the  blcok
        processing method. Also, unlike the block processing method which computes a single value
        for all weights within a single bin, the sliding window method requires that each row
        (along with each channel and correlation bin) be processed individually, so in general
        the sliding window method will take longer than the block processing method.

        CHANNEL BINNING

        The width of channel bins is specified via the chanbin parameter. Channel binning occurs within
        individual spectral windows; bins never span multiple spectral windows. Each channel will
        be included in exactly one bin.

        The default value "spw" indicates that all channels in each spectral window are to be
        included in a single bin.

        Any other string value is interpreted as a quantity, and so should have frequency units, eg
        "1MHz". In this case, the channel frequencies from the CHAN_FREQ column of the SPECTRAL_WINDOW
        subtable of the MS are used to determine the bins. The first bin starts at the channel frequency
        of the 0th channel in the spectral window. Channels with frequencies that differ by less than
        the value specified by the chanbin parameter are included in this bin. The next bin starts at
        the frequency of the first channel outside the first bin, and the process is repeated until all
        channels have been binned.

        If specified as an integer, the value is interpreted as the number of channels to include in
        each bin. The final bin in the spectral window may not necessarily contain this number of
        channels. For example, if a spectral window has 15 channels, and chanbin is specified to be 6,
        then channels 0-5 will comprise the first bin, channels 6-11 the second, and channels 12-14 the
        third, so that only three channels will comprise the final bin.

        MINIMUM REQUIRED NUMBER OF VISIBILITIES

        The minsamp parameter allows the user to specify the minimum number of unflagged visibilities that
        must be present in a sample for that sample's weight to be computed. If a sample has less than
        this number of unflagged points, the associated weights of all the points in the sample are
        set to zero, and all the points in the sample are flagged.

        AGGREGATING DATA ACROSS BOUNDARIES

        By default, data are not aggregated across changes in values in the columns ARRAY_ID,
        SCAN_NUMBER, STATE_ID, FIELD_ID, and DATA_DESC_ID. One can override this behavior for
        SCAN_NUMBER, STATE_ID, and FIELD_ID by specifying the combine parameter. For example,
        specifying combine="scan" will ignore scan boundaries when aggregating data. Specifying
        combine="field, scan" will ignore both scan and field boundaries when aggregating data.

        Also by default, data for separate correlations are aggregated separately. Data for all
        correlations within each spectral window can be aggregated together by specifying
        "corr" in the combine parameter.

        Any combination and permutation of "scan", "field", "state", and "corr" are supported
        by the combine parameter. Other values will be silently ignored.

        STATISTICS ALGORITHMS

        The supported statistics algorithms are described in detail in the imstat and ia.statistics()
        help. For the current application, these algorithms are used to compute vr and vi (see above),
        such that the set of the real parts of the visibilities and the set of the imaginary parts of
        the visibilities are treated as independent data sets.

        RANGE OF ACCEPTABLE WEIGHTS

        The wtrange parameter allows one to specify the acceptable range (inclusive, except for zero)
        for weights. Data with weights computed to be outside this range will be flagged. If not
        specified (empty array), all weights are considered to be acceptable. If specified, the array
        must contain exactly two nonnegative numeric values. Note that data with weights of zero are
        always flagged.

        EXCLUDING CHANNELS

        Channels can be excluded from the computation of the weights by specifying the excludechans
        parameter. This parameter accepts a valid MS channel selection string. Data associated with
        the selected channels will not be used in computing the weights.

        PREVIEW MODE

        By setting preview=True, the application is run in "preview" mode. In this mode, no data
        in the input MS are changed, although the amount of data that the application would have
        flagged is reported.

        DATA COLUMN

        The datacolumn parameter can be specified to indicate which data column should be used
        for computing the weights. The values "corrected" for the CORRECTED_DATA column and "data"
        for the DATA column are supported (minimum match, case insensitive).

        OTHER CONSIDERATIONS

        Flagged values are not used in computing the weights, although the associated weights of
        these values are updated.

        If the variance for a set of data is 0, all associated flags for that data are set to True,
        and the corresponding weights are set to 0.

        EXAMPLE

        # update the weights of an MS using time binning of 300s
        statwt("my.ms", timebin="300s")
    
        """
        if type(wtrange)==float: wtrange=[wtrange]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['selectdata'] = selectdata
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['intent'] = intent
        mytmp['array'] = array
        mytmp['observation'] = observation
        mytmp['scan'] = scan
        mytmp['combine'] = combine
        mytmp['timebin'] = timebin
        mytmp['slidetimebin'] = slidetimebin
        mytmp['chanbin'] = chanbin
        mytmp['minsamp'] = minsamp
        mytmp['statalg'] = statalg
        mytmp['fence'] = fence
        mytmp['center'] = center
        mytmp['lside'] = lside
        mytmp['zscore'] = zscore
        mytmp['maxiter'] = maxiter
        mytmp['fitspw'] = fitspw
        mytmp['excludechans'] = excludechans
        mytmp['wtrange'] = wtrange
        mytmp['flagbackup'] = flagbackup
        mytmp['preview'] = preview
        mytmp['datacolumn'] = datacolumn
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'statwt.xml')

        casalog.origin('statwt')
        if trec.has_key('statwt') and casac.utils().verify(mytmp, trec['statwt']) :
            result = task_statwt.statwt(vis, selectdata, field, spw, intent, array, observation, scan, combine, timebin, slidetimebin, chanbin, minsamp, statalg, fence, center, lside, zscore, maxiter, fitspw, excludechans, wtrange, flagbackup, preview, datacolumn)

        else :
          result = False
        return result
