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
from task_sdfit import sdfit
class sdfit_cli_:
    __name__ = "sdfit"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (sdfit_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'infile':None, 'datacolumn':None, 'antenna':None, 'field':None, 'spw':None, 'timerange':None, 'scan':None, 'pol':None, 'intent':None, 'timebin':None, 'timespan':None, 'polaverage':None, 'fitfunc':None, 'fitmode':None, 'nfit':None, 'thresh':None, 'avg_limit':None, 'minwidth':None, 'edge':None, 'outfile':None, 'overwrite':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, infile=None, datacolumn=None, antenna=None, field=None, spw=None, timerange=None, scan=None, pol=None, intent=None, timebin=None, timespan=None, polaverage=None, fitfunc=None, fitmode=None, nfit=None, thresh=None, avg_limit=None, minwidth=None, edge=None, outfile=None, overwrite=None, ):

        """Fit a spectral line

        Detailed Description:

Task sdfit is a basic line-fitter for single-dish spectra.
It assumes that the spectra have been calibrated in tsdcal
or sdreduce.
  
        Arguments :
                infile: name of input SD dataset
                   Default Value: 

                datacolumn: name of data column to be used ["data", "float_data", or "corrected_data"]
                   Default Value: data

                antenna: select data by antenna name or ID, e.g. "PM03"
                   Default Value: 

                field: select data by field IDs and names, e.g. "3C2*" (""=all)
                   Default Value: 

                spw: select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)
                   Default Value: 

                timerange: select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)
                   Default Value: 

                scan: select data by scan numbers, e.g. "21~23" (""=all)
                   Default Value: 

                pol: select data by polarization IDs, e.g. "XX,YY" (""=all)
                   Default Value: 

                intent: select data by observational intent, e.g. "*ON_SOURCE*" (""=all)
                   Default Value: 

                timebin: bin width for time averaging
                   Default Value: 

                timespan: span the timebin across "scan", "state", "field", or a combination of them (e.g., "scan,state")
                   Default Value: 

                polaverage: polarization averaging mode ("", "stokes" or "geometric").
                   Default Value: 
                   Allowed Values:
                                
                                stokes
                                geometric

                fitfunc: function for fitting
                   Default Value: gaussian
                   Allowed Values:
                                gaussian
                                lorentzian

                fitmode: mode for setting additional channel masks.
                   Default Value: list
                   Allowed Values:
                                auto
                                list

                nfit: list of number of lines to fit in maskline region.
                   Default Value: 0

                thresh: S/N threshold for linefinder
                   Default Value: 5.0

                avg_limit: channel averaging for broad lines
                   Default Value: 4

                minwidth: the minimum channel width to detect as a line
                   Default Value: 4

                edge: channels to drop at beginning and end of spectrum
                   Default Value: 00

                outfile: name of output file
                   Default Value: 

                overwrite: overwrite the output file if already exists
                   Default Value: False

        Returns: variant

        Example :

-----------------
Keyword arguments
-----------------
infile -- name of input SD dataset
datacolumn -- name of data column to be used
        options: 'data', 'float_data', or 'corrected_data'
        default: 'data'
antenna -- select data by antenna name or ID
        default: '' (use all antennas)
        example: 'PM03'
field -- select data by field IDs and names
        default: '' (use all fields)
        example: field='3C2*' (all names starting with 3C2)
                 field='0,4,5~7' (field IDs 0,4,5,6,7)
                 field='0,3C273' (field ID 0 or field named 3C273)
        this selection is in addition to the other selections to data
spw -- select data by IF IDs (spectral windows)/channels
        default: '' (use all IFs and channels)
        example: spw='3,5,7' (IF IDs 3,5,7; all channels)
                 spw='<2' (IF IDs less than 2, i.e., 0,1; all channels)
                 spw='30~45GHz' (IF IDs with the center frequencies in range 30-45GHz; all channels)
                 spw='0:5~61' (IF ID 0; channels 5 to 61; all channels)
                 spw='3:10~20;50~60' (select multiple channel ranges within IF ID 3)
                 spw='3:10~20,4:0~30' (select different channel ranges for IF IDs 3 and 4)
                 spw='1~4;6:15~48' (for channels 15 through 48 for IF IDs 1,2,3,4 and 6)
        this selection is in addition to the other selections to data
timerange -- select data by time range
        default: '' (use all)
        example: timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                 Note: YYYY/MM/DD can be dropped as needed:
                 timerange='09:14:00~09:54:00' # this time range
                 timerange='09:44:00' # data within one integration of time
                 timerange='>10:24:00' # data after this time
                 timerange='09:44:00+00:13:00' #data 13 minutes after time
        this selection is in addition to the other selections to data
scan -- select data by scan numbers
        default: '' (use all scans)
        example: scan='21~23' (scan IDs 21,22,23)
        this selection is in addition to the other selections to data
pol -- select data by polarization IDs
        default: '' (use all polarizations)
        example: pol='XX,YY' (polarizations XX and YY)
        this selection is in addition to the other selections to data
intent -- select data by observational intent, also referred to as 'scan intent'
        default: '' (use all scan intents)
        example: intent='*ON_SOURCE*' (any valid scan-intent expression accepted by the MSSelection module can be specified)
        this selection is in addition to the other selections to data
timebin -- bin width for time averaging. it must be a positive value.
        default: '' (no averaging over time)
        example: timebin='1s' (time averaging performed over 1 second bins)
    >>> timebin expandable parameters
        timespan -- span the timebin across 'scan', 'state', 'field', or a combination of them (e.g., 'scan,state')
                default: '' (average each scan, intent and field separately)
                example: 'scan' time averaging is done across scan ID boundaries
polaverage -- polarization averaging mode
        default: '' (no averaging over polarization)
        options: '', 'stokes', 'geometric'
fitfunc -- function for fitting
        options: 'gaussian', 'lorentzian'
        default: 'gaussian'
fitmode -- mode for fitting
        options: 'list' ('auto' and 'interact' will be available later)
        default: 'list'
        example: 'list' will use channel ranges specified in the parameter 
                        spw to fit for lines
                 'auto'  will use the linefinder to fit for lines
                        using the following parameters
                 'interact' allows adding and deleting mask 
                        regions by drawing rectangles on the plot 
                        with mouse. Draw a rectangle with LEFT-mouse 
                        to ADD the region to the mask and with RIGHT-mouse 
                        to DELETE the region. 
    >>> fitmode expandable parameters     
        nfit -- list of number of lines to fit in each region specified by the 
                parameter spw (only available in fitmode='list')
                default: [0] (no fitting)
                example: nfit=[1] for single line in single region,
                         nfit=[2] for two lines in single region,
                         nfit=[1,1] for single lines in each of two regions, etc.
        thresh -- S/N threshold for linefinder. a single channel S/N ratio
                  above which the channel is considered to be a detection.
                   (only available in fitmode='auto')
                default: 5
        avg_limit -- channel averaging for broad lines. a number of
                     consecutive channels not greater than this parameter
                     can be averaged to search for broad lines.
                    (only available in fitmode='auto')
                default: 4
        minwidth -- minimum number of consecutive channels required to
                    pass threshold
                    (only available in fitmode='auto')
                default: 4
        edge -- channels to drop at beginning and end of spectrum
                (only available in fitmode='auto')
                default: 0
                example: edge=[1000] drops 1000 channels at beginning AND end.
                         edge=[1000,500] drops 1000 from beginning and 500
                         from end

        Note: For bad baselines threshold should be increased,
        and avg_limit decreased (or even switched off completely by
        setting this parameter to 1) to avoid detecting baseline
        undulations instead of real lines.
outfile -- name of output file
        default: no output fit file
        example: 'mysd.fit'
overwrite -- overwrite the output file if already exists
        options: (bool) True, False
        default: False

-------
Returns
-------
a Python dictionary of line statistics
    keys: 'peak', 'cent', 'fwhm', 'nfit'
    example: each value except for 'nfit' is a list of lists with 
             a list of 2 entries [fitvalue,error] per component.
             e.g. xstat['peak']=[[234.9, 4.8],[234.2, 5.3]]
             for 2 components.

-----------
DESCRIPTION
-----------
Task sdfit is a basic line-fitter for single-dish spectra.
It assumes that the spectra have been calibrated in tsdcal
or sdreduce.

Note that multiple scans, IFs, and polarizations can in principle 
be handled, but we recommend that you use scan, field, spw, and pol
to give a single selection for each fit.

-------
POLARIZATION AVERAGE
-------
Two modes of polarization averaging are available. The default is 
'stokes' which is an average based on a formulation of Stokes 
parameter. In this mode, averaged data is calculated by 
(XX + YY) / 2 or (RR + LL) / 2. Other option is 'geometric', which 
is a conventional way of averaging in the field of single-dish 
data reduction. The averaged data is given by weighted average 
of XX and YY, or RR and LL. 

-------
FITMODE
-------
As described in the parameter description section, sdfit implements 
fitting modes 'list' and 'auto' so far. 
The 'list' mode allows users to set  initial guess manually. The only
controllable parameter for the guess is  range of the line region and
number of lines per region. In 'list' mode, users must give line 
region via spw parameter by using ms selection syntax while number of
lines per region can be specified via nfit parameter. For example,
 
    spw = '17:1500~2500'
    nfit = [1]

will set line region between channels 1500 and 2500 for spw 17, and
indicate that there is only one line in this region. Specifying single
region with multiple line is also possible but is not recommended.
In 'auto' mode, the line finder detects channel ranges of spectral lines
based on median absolute deviation (MAD) of the spectra using user defined
criteria, thres, avg_limit, minwidth, and edge. The number of channels
in both edges of spectra defined by edge parameter are ignored in line
detection. The median of lower 80% of MAD values in a spectrum is 
multiplied by thres parameter value to define a threshold of line 
detection. All channels with MAD above the threshold is detected as 
spectral line candidates and accepted as spectral lines only if the 
channel width of the line exceeds the value of minwidth parameter. The 
line detection is iteratively invoked for channel averaged spectra 
up to avg_limit.

  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'sdfit'
        self.__globals__['taskname'] = 'sdfit'
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

            myparams['infile'] = infile = self.parameters['infile']
            myparams['datacolumn'] = datacolumn = self.parameters['datacolumn']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['pol'] = pol = self.parameters['pol']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['timebin'] = timebin = self.parameters['timebin']
            myparams['timespan'] = timespan = self.parameters['timespan']
            myparams['polaverage'] = polaverage = self.parameters['polaverage']
            myparams['fitfunc'] = fitfunc = self.parameters['fitfunc']
            myparams['fitmode'] = fitmode = self.parameters['fitmode']
            myparams['nfit'] = nfit = self.parameters['nfit']
            myparams['thresh'] = thresh = self.parameters['thresh']
            myparams['avg_limit'] = avg_limit = self.parameters['avg_limit']
            myparams['minwidth'] = minwidth = self.parameters['minwidth']
            myparams['edge'] = edge = self.parameters['edge']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']

        if type(nfit)==int: nfit=[nfit]
        if type(edge)==int: edge=[edge]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['infile'] = infile
        mytmp['datacolumn'] = datacolumn
        mytmp['antenna'] = antenna
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['timerange'] = timerange
        mytmp['scan'] = scan
        mytmp['pol'] = pol
        mytmp['intent'] = intent
        mytmp['timebin'] = timebin
        mytmp['timespan'] = timespan
        mytmp['polaverage'] = polaverage
        mytmp['fitfunc'] = fitfunc
        mytmp['fitmode'] = fitmode
        mytmp['nfit'] = nfit
        mytmp['thresh'] = thresh
        mytmp['avg_limit'] = avg_limit
        mytmp['minwidth'] = minwidth
        mytmp['edge'] = edge
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'sdfit.xml')

        casalog.origin('sdfit')
        try :
          #if not trec.has_key('sdfit') or not casac.casac.utils().verify(mytmp, trec['sdfit']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['sdfit'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('sdfit', 'sdfit.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'sdfit'
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
          result = sdfit(infile, datacolumn, antenna, field, spw, timerange, scan, pol, intent, timebin, timespan, polaverage, fitfunc, fitmode, nfit, thresh, avg_limit, minwidth, edge, outfile, overwrite)

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
             tname = 'sdfit'
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
#        paramgui.runTask('sdfit', myf['_ip'])
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
        a['infile']  = ''
        a['datacolumn']  = 'data'
        a['antenna']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['timerange']  = ''
        a['scan']  = ''
        a['pol']  = ''
        a['intent']  = ''
        a['timebin']  = ''
        a['polaverage']  = ''
        a['fitfunc']  = 'gaussian'
        a['fitmode']  = 'list'
        a['outfile']  = ''
        a['overwrite']  = False

        a['timebin'] = {
                    0:odict([{'notvalue':''}, {'timespan':''}])}
        a['fitmode'] = {
                    0:odict([{'value':'list'}, {'nfit':[0]}]), 
                    1:odict([{'value':'auto'}, {'thresh':5.0}, {'avg_limit':4}, {'minwidth':4}, {'edge':[0]}]), 
                    2:odict([{'value':'interact'}, {'nfit':[0]}])}

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
    def description(self, key='sdfit', subkey=None):
        desc={'sdfit': 'Fit a spectral line',
               'infile': 'name of input SD dataset',
               'datacolumn': 'name of data column to be used ["data", "float_data", or "corrected_data"]',
               'antenna': 'select data by antenna name or ID, e.g. "PM03"',
               'field': 'select data by field IDs and names, e.g. "3C2*" (""=all)',
               'spw': 'select data by IF IDs (spectral windows), e.g. "3,5,7" (""=all)',
               'timerange': 'select data by time range, e.g. "09:14:0~09:54:0" (""=all) (see examples in help)',
               'scan': 'select data by scan numbers, e.g. "21~23" (""=all)',
               'pol': 'select data by polarization IDs, e.g. "XX,YY" (""=all)',
               'intent': 'select data by observational intent, e.g. "*ON_SOURCE*" (""=all)',
               'timebin': 'bin width for time averaging',
               'timespan': 'span the timebin across "scan", "state", "field", or a combination of them (e.g., "scan,state")',
               'polaverage': 'polarization averaging mode ("", "stokes" or "geometric").',
               'fitfunc': 'function for fitting ["gaussian", "lorentzian"]',
               'fitmode': 'mode for setting additional channel masks. "list" and "auto" are available now.',
               'nfit': 'list of number of lines to fit in maskline region.',
               'thresh': 'S/N threshold for linefinder',
               'avg_limit': 'channel averaging for broad lines',
               'minwidth': 'the minimum channel width to detect as a line',
               'edge': 'channels to drop at beginning and end of spectrum',
               'outfile': 'name of output file',
               'overwrite': 'overwrite the output file if already exists [True, False]',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['infile']  = ''
        a['datacolumn']  = 'data'
        a['antenna']  = ''
        a['field']  = ''
        a['spw']  = ''
        a['timerange']  = ''
        a['scan']  = ''
        a['pol']  = ''
        a['intent']  = ''
        a['timebin']  = ''
        a['timespan']  = ''
        a['polaverage']  = ''
        a['fitfunc']  = 'gaussian'
        a['fitmode']  = 'list'
        a['nfit']  = [0]
        a['thresh']  = 5.0
        a['avg_limit']  = 4
        a['minwidth']  = 4
        a['edge']  = [0, 0]
        a['outfile']  = ''
        a['overwrite']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['timebin']  != '':
            a['timespan'] = ''

        if self.parameters['fitmode']  == 'list':
            a['nfit'] = [0]

        if self.parameters['fitmode']  == 'auto':
            a['thresh'] = 5.0
            a['avg_limit'] = 4
            a['minwidth'] = 4
            a['edge'] = [0]

        if self.parameters['fitmode']  == 'interact':
            a['nfit'] = [0]

        if a.has_key(paramname) :
              return a[paramname]
sdfit_cli = sdfit_cli_()
