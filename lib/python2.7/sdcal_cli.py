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
from task_sdcal import sdcal
class sdcal_cli_:
    __name__ = "sdcal"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (sdcal_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'infile':None, 'calmode':None, 'fraction':None, 'noff':None, 'width':None, 'elongated':None, 'applytable':None, 'interp':None, 'spwmap':None, 'outfile':None, 'overwrite':None, 'field':None, 'spw':None, 'scan':None, 'intent':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, infile=None, calmode=None, fraction=None, noff=None, width=None, elongated=None, applytable=None, interp=None, spwmap=None, outfile=None, overwrite=None, field=None, spw=None, scan=None, intent=None, ):

        """ MS SD calibration task

        Detailed Description:

Task sdcal implements a single-dish data calibration scheme similar to that of 
interferometry, i.e., generate calibration tables (caltables) and apply them. 
Available calibration modes are:
    'ps', 'otfraster', 'otf' for sky calibration
    'tsys' for Tsys calibration 
Each mode generates a caltable.
Caltables can be applied to the data by combining calibration
modes with the keyword 'apply'.

Calibration is applicable for fast moving source even like the moon which moves
quickly outside of the field of view (see the note of 'otf' mode in below).

Calibration mode must be set in accordance with the observing mode
of the data. Use case for each mode is as follows:
    'ps': position switch (including OTF) with explicit
          reference (OFF) spectra
    'otfraster': raster OTF scan without explicit OFFs
    'otf': non-raster OTF (e.g. double-circle) scan without explicit OFFs

So, if the data contains explicit reference spectra, 'ps' should
be used. Otherwise, 'otfraster' or 'otf' should be used.
In 'otfraster' and 'otf' modes, an edge marker automatically marks spectra from
specific regions of the observation pattern as reference (OFF) spectra.
These specific regions are:
- in 'otfraster' mode: regions near the beginning and the end of the raster 
scan lines.
- in 'otf' mode: regions near the periphery of the observation pattern.
Note: The 'otfraster' mode is designed for OTF observations without explicit OFF
spectra. However, it should work even if explicit reference spectra exist.
In that case, these spectra are ignored and spectra marked by edge marker are 
used as reference. 
Note: Detection of periphery scans in 'otf' mode is available for fast moving
sources, e.g., Sun, Moon. It is often the case antennas keep track of source motion
during the observations of moving sources so that the source is always at the map center.
In order to handle such observations, pheriphery search is done in the source frame
for known moving sources, in which the source is always at a rest position.

Apart from the way reference spectra are selected, the procedure to derive 
calibrated spectra is the same for all modes. Selected (or preset) 
OFF integrations are separated based on continuity in time domain, 
averaged in each segment, and then interpolated to timestamps for ON 
integrations. Effectively, it means that OFF integrations are 
averaged by each OFF spectrum for 'ps' mode, averaged by either ends 
of each raster row for 'otfraster' mode. The formula for calibrated 
spectrum is

    Tsys * (ON - OFF) / OFF. 

  
        Arguments :
                infile: name of input SD dataset (must be MS)
                   Default Value: 

                calmode: SD calibration mode
                   Default Value: ps
                   Allowed Values:
                                ps
                                otfraster
                                otf
                                tsys
                                apply
                                ps,apply
                                tsys,apply
                                ps,tsys,apply
                                otfraster,apply
                                otfraster,tsys,apply
                                otf,apply
                                otf,tsys,apply

                fraction: fraction of the OFF data to mark
                   Default Value: 10%

                noff: number of the OFF data to mark
                   Default Value: -1

                width: width of the pixel for edge detection
                   Default Value: 0.5

                elongated: whether observed area is elongated in one direction or not
                   Default Value: False

                applytable: (List of) sky and/or tsys tables
                   Default Value: 

                interp: Interpolation type in time[,freq]. Valid options for time are "nearest", "linear", and "cubic", while valid options for frequency include "nearest", "linear", "cspline", or any numeric string that indicates an order of polynomial interpolation. You can specify interpolation type for time and frequency separately by joining two of the above options by comma (e.g., "linear,cspline").
                   Default Value: 

                spwmap: A dictionary indicating spw combinations to apply Tsys calibration to target. The key should be spw for Tsys calibration and its associated value must be a list of science spws to be applied.
                   Default Value: {}

                outfile: name of output file (See a WARNING in help)
                   Default Value: 

                overwrite: overwrite the output file if already exists
                   Default Value: False

                field: select data by field IDs and names, e.g. "3C2*" ("" = all)
                   Default Value: 

                spw: select data by spw IDs (spectral windows), e.g., "3,5,7" ("" = all)
                   Default Value: 

                scan: select data by scan numbers, e.g. "21~23" (""=all)
                   Default Value: 

                intent: select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE" (""=all)
                   Default Value: 

        Returns: void

        Example :

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
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'sdcal'
        self.__globals__['taskname'] = 'sdcal'
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
            myparams['calmode'] = calmode = self.parameters['calmode']
            myparams['fraction'] = fraction = self.parameters['fraction']
            myparams['noff'] = noff = self.parameters['noff']
            myparams['width'] = width = self.parameters['width']
            myparams['elongated'] = elongated = self.parameters['elongated']
            myparams['applytable'] = applytable = self.parameters['applytable']
            myparams['interp'] = interp = self.parameters['interp']
            myparams['spwmap'] = spwmap = self.parameters['spwmap']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['intent'] = intent = self.parameters['intent']


        result = None

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
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'sdcal.xml')

        casalog.origin('sdcal')
        try :
          #if not trec.has_key('sdcal') or not casac.casac.utils().verify(mytmp, trec['sdcal']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['sdcal'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('sdcal', 'sdcal.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'sdcal'
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
          result = sdcal(infile, calmode, fraction, noff, width, elongated, applytable, interp, spwmap, outfile, overwrite, field, spw, scan, intent)

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
             tname = 'sdcal'
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
#        paramgui.runTask('sdcal', myf['_ip'])
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
        a['calmode']  = 'ps'
        a['field']  = ''
        a['spw']  = ''
        a['scan']  = ''

        a['calmode'] = {
                    0:odict([{'value':'ps'}, {'outfile':''}, {'overwrite':False}]), 
                    1:odict([{'value':'otfraster'}, {'fraction':'10%'}, {'noff':-1}, {'outfile':''}, {'overwrite':False}, {'intent':'OBSERVE_TARGET#ON_SOURCE'}]), 
                    2:odict([{'value':'otf'}, {'fraction':'10%'}, {'outfile':''}, {'overwrite':False}, {'intent':'OBSERVE_TARGET#ON_SOURCE'}]), 
                    3:odict([{'value':'tsys'}, {'outfile':''}, {'overwrite':False}]), 
                    4:odict([{'value':'apply'}, {'applytable':''}, {'interp':''}, {'spwmap':{}}]), 
                    5:odict([{'value':'ps,apply'}, {'applytable':''}, {'interp':''}, {'spwmap':{}}]), 
                    6:odict([{'value':'tsys,apply'}, {'applytable':''}, {'interp':''}, {'spwmap':{}}]), 
                    7:odict([{'value':'ps,tsys,apply'}, {'applytable':''}, {'interp':''}, {'spwmap':{}}]), 
                    8:odict([{'value':'otfraster,apply'}, {'fraction':'10%'}, {'noff':-1}, {'applytable':''}, {'interp':''}, {'spwmap':{}}, {'intent':'OBSERVE_TARGET#ON_SOURCE'}]), 
                    9:odict([{'value':'otfraster,tsys,apply'}, {'fraction':'10%'}, {'noff':-1}, {'applytable':''}, {'interp':''}, {'spwmap':{}}]), 
                    10:odict([{'value':'otf,apply'}, {'fraction':'10%'}, {'applytable':''}, {'interp':''}, {'spwmap':{}}, {'intent':'OBSERVE_TARGET#ON_SOURCE'}]), 
                    11:odict([{'value':'otf,tsys,apply'}, {'fraction':'10%'}, {'applytable':''}, {'interp':''}, {'spwmap':{}}])}

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
    def description(self, key='sdcal', subkey=None):
        desc={'sdcal': ' MS SD calibration task',
               'infile': 'name of input SD dataset (must be MS)',
               'calmode': 'SD calibration mode ["ps","otfraster","otf","tsys","apply", and allowed combinations]',
               'fraction': 'fraction of the OFF data to mark',
               'noff': 'number of the OFF data to mark',
               'width': 'width of the pixel for edge detection',
               'elongated': 'whether observed area is elongated in one direction or not',
               'applytable': '(List of) sky and/or tsys tables',
               'interp': 'Interpolation type in time[,freq]. Valid options for time are "nearest", "linear", and "cubic", while valid options for frequency include "nearest", "linear", "cspline", or any numeric string that indicates an order of polynomial interpolation. You can specify interpolation type for time and frequency separately by joining two of the above options by comma (e.g., "linear,cspline").',
               'spwmap': 'A dictionary indicating spw combinations to apply Tsys calibration to target. The key should be spw for Tsys calibration and its associated value must be a list of science spws to be applied.',
               'outfile': 'name of output file (See a WARNING in help)',
               'overwrite': 'overwrite the output file if already exists [True, False]',
               'field': 'select data by field IDs and names, e.g. "3C2*" ("" = all)',
               'spw': 'select data by spw IDs (spectral windows), e.g., "3,5,7" ("" = all)',
               'scan': 'select data by scan numbers, e.g. "21~23" (""=all)',
               'intent': 'select data by observation intent, e.g. "OBSERVE_TARGET#ON_SOURCE" (""=all)',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['infile']  = ''
        a['calmode']  = 'ps'
        a['fraction']  = '10%'
        a['noff']  = -1
        a['width']  = 0.5
        a['elongated']  = False
        a['applytable']  = ''
        a['interp']  = ''
        a['spwmap']  = {}
        a['outfile']  = ''
        a['overwrite']  = False
        a['field']  = ''
        a['spw']  = ''
        a['scan']  = ''
        a['intent']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['calmode']  == 'ps':
            a['outfile'] = ''
            a['overwrite'] = False

        if self.parameters['calmode']  == 'otfraster':
            a['fraction'] = '10%'
            a['noff'] = -1
            a['outfile'] = ''
            a['overwrite'] = False
            a['intent'] = 'OBSERVE_TARGET#ON_SOURCE'

        if self.parameters['calmode']  == 'otf':
            a['fraction'] = '10%'
            a['outfile'] = ''
            a['overwrite'] = False
            a['intent'] = 'OBSERVE_TARGET#ON_SOURCE'

        if self.parameters['calmode']  == 'tsys':
            a['outfile'] = ''
            a['overwrite'] = False

        if self.parameters['calmode']  == 'apply':
            a['applytable'] = ''
            a['interp'] = ''
            a['spwmap'] = {}

        if self.parameters['calmode']  == 'ps,apply':
            a['applytable'] = ''
            a['interp'] = ''
            a['spwmap'] = {}

        if self.parameters['calmode']  == 'tsys,apply':
            a['applytable'] = ''
            a['interp'] = ''
            a['spwmap'] = {}

        if self.parameters['calmode']  == 'ps,tsys,apply':
            a['applytable'] = ''
            a['interp'] = ''
            a['spwmap'] = {}

        if self.parameters['calmode']  == 'otfraster,apply':
            a['fraction'] = '10%'
            a['noff'] = -1
            a['applytable'] = ''
            a['interp'] = ''
            a['spwmap'] = {}
            a['intent'] = 'OBSERVE_TARGET#ON_SOURCE'

        if self.parameters['calmode']  == 'otfraster,tsys,apply':
            a['fraction'] = '10%'
            a['noff'] = -1
            a['applytable'] = ''
            a['interp'] = ''
            a['spwmap'] = {}

        if self.parameters['calmode']  == 'otf,apply':
            a['fraction'] = '10%'
            a['applytable'] = ''
            a['interp'] = ''
            a['spwmap'] = {}
            a['intent'] = 'OBSERVE_TARGET#ON_SOURCE'

        if self.parameters['calmode']  == 'otf,tsys,apply':
            a['fraction'] = '10%'
            a['applytable'] = ''
            a['interp'] = ''
            a['spwmap'] = {}

        if a.has_key(paramname) :
              return a[paramname]
sdcal_cli = sdcal_cli_()
