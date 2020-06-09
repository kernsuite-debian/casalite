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
from task_statwt import statwt
class statwt_cli_:
    __name__ = "statwt"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (statwt_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'selectdata':None, 'field':None, 'spw':None, 'intent':None, 'array':None, 'observation':None, 'scan':None, 'combine':None, 'timebin':None, 'slidetimebin':None, 'chanbin':None, 'minsamp':None, 'statalg':None, 'fence':None, 'center':None, 'lside':None, 'zscore':None, 'maxiter':None, 'fitspw':None, 'excludechans':None, 'wtrange':None, 'flagbackup':None, 'preview':None, 'datacolumn':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, selectdata=None, field=None, spw=None, intent=None, array=None, observation=None, scan=None, combine=None, timebin=None, slidetimebin=None, chanbin=None, minsamp=None, statalg=None, fence=None, center=None, lside=None, zscore=None, maxiter=None, fitspw=None, excludechans=None, wtrange=None, flagbackup=None, preview=None, datacolumn=None, ):

        """Compute and set weights based on variance of data.
        Arguments :
                vis: Name of measurement set
                   Default Value: 

                selectdata: Enable data selection parameters
                   Default Value: True

                field: Selection based on field names or field index numbers. Default is all.
                   Default Value: 

                spw: Selection based on spectral windows:channels. Default is all.
                   Default Value: 

                intent: Selection based on intents. Default is all.
                   Default Value: 

                array: Selection based on array IDs. Default is all.
                   Default Value: 

                observation: Selection based on observation IDs. Default is all.
                   Default Value: 

                scan: Select data by scan numbers.
                   Default Value: 

                combine: Ignore changes in these columns (scan, field, and/or state) when aggregating samples to compute weights. The value "corr" is also supported to aggregate samples across correlations.
                   Default Value: 

                timebin: Length for binning in time to determine statistics. Can either be integer to be multiplied by the representative integration time, a quantity (string) in time units
                   Default Value: 0.001s

                slidetimebin: Use a sliding window for time binning, as opposed to time block processing?
                   Default Value: False

                chanbin: Channel bin width for computing weights. Can either be integer, in which case it is interpreted as number of channels to include in each bin, or a string "spw" or quantity with frequency units.
                   Default Value: spw

                minsamp: Minimum number of unflagged visibilities required for computing weights in a sample. Must be >= 2.
                   Default Value: 2

                statalg: Statistics algorithm to use for computing variances. Supported values are "chauvenet", "classic", "fit-half", and "hinges-fences". Minimum match is supported, although the full string must be specified for the subparameters to appear in the inputs list.
                   Default Value: classic

                fence: Fence value for statalg="hinges-fences". A negative value means use the entire data set (ie default to the "classic" algorithm). Ignored if statalg is not "hinges-fences".
                   Default Value: -1

                center: Center to use for statalg="fit-half". Valid choices are "mean", "median", and "zero". Ignored if statalg is not "fit-half".
                   Default Value: mean

                lside: For statalg="fit-half", real data are <=; center? If false, real data are >= center. Ignored if statalg is not "fit-half".
                   Default Value: True

                zscore: For statalg="chauvenet", this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet\'s criterion. Ignored if statalg is not "chauvenet".
                   Default Value: -1

                maxiter: For statalg="chauvenet", this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if statalg is not "chauvenet".
                   Default Value: -1

                fitspw: Channels to include in the computation of weights. Specified as an MS select channel selection string.
                   Default Value: 

                excludechans: If True: invert the channel selection in fitspw and exclude the fitspw selection from the computation of the weights.
                   Default Value: False

                wtrange: Range of acceptable weights. Data with weights outside this range will be flagged. Empty array (default) means all weights are good.
                   Default Value: 

                flagbackup: Back up the state of flags before the run?
                   Default Value: True

                preview: Preview mode. If True, no data is changed, although the amount of data that would have been flagged is reported.
                   Default Value: False

                datacolumn: Data column to use to compute weights. Supported values are "data", "corrected", "residual", and "residual_data" (case insensitive, minimum match supported).
                   Default Value: corrected


        Example :

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
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'statwt'
        self.__globals__['taskname'] = 'statwt'
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
            myparams['intent'] = intent = self.parameters['intent']
            myparams['array'] = array = self.parameters['array']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['combine'] = combine = self.parameters['combine']
            myparams['timebin'] = timebin = self.parameters['timebin']
            myparams['slidetimebin'] = slidetimebin = self.parameters['slidetimebin']
            myparams['chanbin'] = chanbin = self.parameters['chanbin']
            myparams['minsamp'] = minsamp = self.parameters['minsamp']
            myparams['statalg'] = statalg = self.parameters['statalg']
            myparams['fence'] = fence = self.parameters['fence']
            myparams['center'] = center = self.parameters['center']
            myparams['lside'] = lside = self.parameters['lside']
            myparams['zscore'] = zscore = self.parameters['zscore']
            myparams['maxiter'] = maxiter = self.parameters['maxiter']
            myparams['fitspw'] = fitspw = self.parameters['fitspw']
            myparams['excludechans'] = excludechans = self.parameters['excludechans']
            myparams['wtrange'] = wtrange = self.parameters['wtrange']
            myparams['flagbackup'] = flagbackup = self.parameters['flagbackup']
            myparams['preview'] = preview = self.parameters['preview']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']

        if type(wtrange)==float: wtrange=[wtrange]

        result = None

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
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'statwt.xml')

        casalog.origin('statwt')
        try :
          #if not trec.has_key('statwt') or not casac.casac.utils().verify(mytmp, trec['statwt']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['statwt'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('statwt', 'statwt.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'statwt'
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
          result = statwt(vis, selectdata, field, spw, intent, array, observation, scan, combine, timebin, slidetimebin, chanbin, minsamp, statalg, fence, center, lside, zscore, maxiter, fitspw, excludechans, wtrange, flagbackup, preview, datacolumn)

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
             tname = 'statwt'
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
#        paramgui.runTask('statwt', myf['_ip'])
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
        a['combine']  = ''
        a['timebin']  = '0.001s'
        a['slidetimebin']  = False
        a['chanbin']  = 'spw'
        a['minsamp']  = 2
        a['statalg']  = 'classic'
        a['fitspw']  = ''
        a['excludechans']  = False
        a['wtrange']  = []
        a['flagbackup']  = True
        a['preview']  = False
        a['datacolumn']  = 'corrected'

        a['selectdata'] = {
                    0:odict([{'value':True}, {'field':""}, {'spw':""}, {'observation':""}, {'intent':""}, {'array':""}, {'scan':""}])}
        a['statalg'] = {
                    0:{'value':'classic'}, 
                    1:odict([{'value':'hinges-fences'}, {'fence':-1}]), 
                    2:odict([{'value':'fit-half'}, {'center':'mean'}, {'lside':True}]), 
                    3:odict([{'value':'chauvenet'}, {'zscore':-1}, {'maxiter':-1}])}

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
    def description(self, key='statwt', subkey=None):
        desc={'statwt': 'Compute and set weights based on variance of data.',
               'vis': 'Name of measurement set',
               'selectdata': 'Enable data selection parameters',
               'field': 'Selection based on field names or field index numbers. Default is all.',
               'spw': 'Selection based on spectral windows:channels. Default is all.',
               'intent': 'Selection based on intents. Default is all.',
               'array': 'Selection based on array IDs. Default is all.',
               'observation': 'Selection based on observation IDs. Default is all.',
               'scan': 'Select data by scan numbers.',
               'combine': 'Ignore changes in these columns (scan, field, and/or state) when aggregating samples to compute weights. The value "corr" is also supported to aggregate samples across correlations.',
               'timebin': 'Length for binning in time to determine statistics. Can either be integer to be multiplied by the representative integration time, a quantity (string) in time units',
               'slidetimebin': 'Use a sliding window for time binning, as opposed to time block processing?',
               'chanbin': 'Channel bin width for computing weights. Can either be integer, in which case it is interpreted as number of channels to include in each bin, or a string "spw" or quantity with frequency units.',
               'minsamp': 'Minimum number of unflagged visibilities required for computing weights in a sample. Must be >= 2.',
               'statalg': 'Statistics algorithm to use for computing variances. Supported values are "chauvenet", "classic", "fit-half", and "hinges-fences". Minimum match is supported, although the full string must be specified for the subparameters to appear in the inputs list.',
               'fence': 'Fence value for statalg="hinges-fences". A negative value means use the entire data set (ie default to the "classic" algorithm). Ignored if statalg is not "hinges-fences".',
               'center': 'Center to use for statalg="fit-half". Valid choices are "mean", "median", and "zero". Ignored if statalg is not "fit-half".',
               'lside': 'For statalg="fit-half", real data are <=; center? If false, real data are >= center. Ignored if statalg is not "fit-half".',
               'zscore': 'For statalg="chauvenet", this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet\'s criterion. Ignored if statalg is not "chauvenet".',
               'maxiter': 'For statalg="chauvenet", this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if statalg is not "chauvenet".',
               'fitspw': 'Channels to include in the computation of weights. Specified as an MS select channel selection string.',
               'excludechans': 'If True: invert the channel selection in fitspw and exclude the fitspw selection from the computation of the weights.',
               'wtrange': 'Range of acceptable weights. Data with weights outside this range will be flagged. Empty array (default) means all weights are good.',
               'flagbackup': 'Back up the state of flags before the run?',
               'preview': 'Preview mode. If True, no data is changed, although the amount of data that would have been flagged is reported.',
               'datacolumn': 'Data column to use to compute weights. Supported values are "data", "corrected", "residual", and "residual_data" (case insensitive, minimum match supported).',

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
        a['intent']  = ''
        a['array']  = ''
        a['observation']  = ''
        a['scan']  = ''
        a['combine']  = ''
        a['timebin']  = '0.001s'
        a['slidetimebin']  = False
        a['chanbin']  = 'spw'
        a['minsamp']  = 2
        a['statalg']  = 'classic'
        a['fence']  = -1
        a['center']  = 'mean'
        a['lside']  = True
        a['zscore']  = -1
        a['maxiter']  = -1
        a['fitspw']  = ''
        a['excludechans']  = False
        a['wtrange']  = []
        a['flagbackup']  = True
        a['preview']  = False
        a['datacolumn']  = 'corrected'

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['selectdata']  == True:
            a['field'] = ""
            a['spw'] = ""
            a['observation'] = ""
            a['intent'] = ""
            a['array'] = ""
            a['scan'] = ""

        if self.parameters['statalg']  == 'hinges-fences':
            a['fence'] = -1

        if self.parameters['statalg']  == 'fit-half':
            a['center'] = 'mean'
            a['lside'] = True

        if self.parameters['statalg']  == 'chauvenet':
            a['zscore'] = -1
            a['maxiter'] = -1

        if a.has_key(paramname) :
              return a[paramname]
statwt_cli = statwt_cli_()
