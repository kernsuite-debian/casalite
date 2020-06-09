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
from task_importasdm import importasdm
class importasdm_cli_:
    __name__ = "importasdm"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (importasdm_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'asdm':None, 'vis':None, 'createmms':None, 'separationaxis':None, 'numsubms':None, 'corr_mode':None, 'srt':None, 'time_sampling':None, 'ocorr_mode':None, 'compression':None, 'lazy':None, 'asis':None, 'wvr_corrected_data':None, 'scans':None, 'ignore_time':None, 'process_syspower':None, 'process_caldevice':None, 'process_pointing':None, 'process_flags':None, 'tbuff':None, 'applyflags':None, 'savecmds':None, 'outfile':None, 'flagbackup':None, 'verbose':None, 'overwrite':None, 'showversion':None, 'useversion':None, 'bdfflags':None, 'with_pointing_correction':None, 'remove_ref_undef':None, 'convert_ephem2geo':None, 'polyephem_tabtimestep':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, asdm=None, vis=None, createmms=None, separationaxis=None, numsubms=None, corr_mode=None, srt=None, time_sampling=None, ocorr_mode=None, compression=None, lazy=None, asis=None, wvr_corrected_data=None, scans=None, ignore_time=None, process_syspower=None, process_caldevice=None, process_pointing=None, process_flags=None, tbuff=None, applyflags=None, savecmds=None, outfile=None, flagbackup=None, verbose=None, overwrite=None, showversion=None, useversion=None, bdfflags=None, with_pointing_correction=None, remove_ref_undef=None, convert_ephem2geo=None, polyephem_tabtimestep=None, ):

        """Convert an ALMA Science Data Model observation into a CASA visibility file (MS)

        Detailed Description:

Convert an ALMA Science Data Model observation into a CASA visibility
file (MS)

        Arguments :
                asdm: Name of input ASDM file (directory)
                     Default: none

                        Example: asdm='ExecBlock3'

                   Default Value: 

                vis: Root ms name. 
                     Default: none

                     Note that a prefix (.ms) is NOT appended to this
                     name.

                   Default Value: 

                createmms: Create a Multi-MS partitioned according to the given
separation axis.
                     Default: False
                     Options: False|True

                     For more detailed documentation on partition,
                     Multi-MS and the MPI use in CASA, please see CASA
                     Docs (https://casa.nrao.edu/casadocs/).

                   Default Value: False

                separationaxis: Axis to do parallelization across
                     Default: 'auto'
                     Options: 'scan', 'spw', 'baseline', 'auto'

                     * auto: will partition per scan/spw to obtain
                       optimal load balancing with the following
                       criteria:    
                       1 - Maximize the scan/spw/field distribution
                       across sub-MSs
                       2 - Generate sub-MSs with similar size
                     * 'scan' or 'spw': will partition the MS into
                       scan or spw. The individual sub-MSs may not be
                       balanced with respect to the number of rows.
                     * 'baseline': mostly useful for Single-Dish
                       data. This axis will partition the MS based on
                       the available baselines. If the user wants only
                       auto-correlations, use the
                       ocorr_mode='ao'. Note that if numsubms='auto',
                       partition will try to create as many subMSs as
                       the number of available servers in the
                       cluster. If the user wants to have one subMS
                       for each baseline, set the numsubms parameter
                       to a number higher than the number of baselines
                       to achieve this. 

                   Default Value: auto
                   Allowed Values:
                                auto
                                scan
                                spw
                                baseline

                numsubms: The number of sub-MSs to create in the Multi-Ms.
                     Default: 'auto'
                     Options: any integer number (example: numsubms=4)

                     The default 'auto' is to partition using the
                     number of available servers given when launching
                     CASA. If the task is unable to determine the
                     number of running servers, or the user did not
                     start CASA using mpicasa, numsubms will use 8 as
                     the default.

                        Example: Launch CASA with 5 engines, where 4
                        of them will be used to create the MMS (the
                        first engine is used as the MPIClient):
                        mpicasa -n 5 casa --nogui --log2term
                        CASA> importasdm('uid__A1', createmms=True)

                   Default Value: auto

                corr_mode: Correlation mode to be considered on input.
                     Default: 'all'
                     Options: ao, co, ac, or all

                   Default Value: all

                srt: Spectral resolution type.
                     Default: 'all'
                     Options: fr, ca, bw, or all

                   Default Value: all

                time_sampling: Specifies the time sampling (INTEGRATION and/or
SUBINTEGRATION) to be considered on input. 
                     Default: 'all'
                     Options: i, si, or all

                     A quoted string containing a sequence of i, si,
                     or all separated by whitespaces is expected

                   Default Value: all

                ocorr_mode: Output data for correlation mode AUTO_ONLY (ao) or
CROSS_ONLY (co) or CROSS_AND_AUTO (ca)
                     Default: 'ca'
                     Options: ao, co, ca

                   Default Value: ca
                   Allowed Values:
                                co
                                ao
                                ca

                compression: Produce compressed columns in the resulting measurement
set.
                     Default: False
                     Options: False|True

                   Default Value: False

                lazy: Make the MS DATA column read the ASDM Binary data
directly (faster import, smaller MS).
                     Default: False
                     Options: False|True

                     Instead of writing a copy of the visibilities
                     into a standard DATA column, lazy=True will make
                     importasdm only write a lookup-table such that
                     later access to the DATA column will read the
                     ASDM binary visibility data directly. This
                     requires that the ASDM not be removed from its
                     location as long the the DATA column is
                     needed. Use method ms.asdmref() to query and
                     manipulate the reference to the ASDM.

                     lazy=True will save ca. 50% disk space and
                     accelerate the DATA column access by
                     ca. 10%. lazy=True will only work when there is
                     visibility data in the ASDM, not with pure
                     radiometer data.

                   Default Value: False

                asis: Creates verbatim copies of the ASDM tables in the output
measurement set.
                     Default: none

                     The value given to this option must be a list of
                     table names separated by space characters; the
                     wildcard character '*' is  allowed in table
                     names.

                   Default Value: 

                wvr_corrected_data: Specifies which values are considerd in the ASDM binary
data to fill the DATA column in the MAIN table of the MS.
                     Default: no
                     Options: no|yes|both

                     * no: uncorrected data
                     * yes: corrected data
                     * both: for corrected and uncorrected data. Note
                       if both is selected, two measurement sets are
                       created, one with uncorrected data and the
                       other with corrected data (which name is
                       suffixed by '-wvr-corrected')

                   Default Value: no
                   Allowed Values:
                                no
                                yes
                                both

                scans: Processes only the scans specified in the option's value.
                     Default: none (all scans)

                     This value is a semicolon separated list of scan
                     specifications. A scan specification consists in
                     an exec bock index  followed by the character ':'
                     followed by a comma separated list of scan
                     indexes or scan index ranges. A scan index is
                     relative to the exec block it belongs to. Scan
                     indexes are  1-based while exec blocks's are
                     0-based. 

                        Examples: 
                        '0:1' 
                        '2:2~6' 
                        '0:1;1:2~6,8;2:,3:24~30'
                        '1,2' 
                        '3:' alone will be interpreted as 'all the
                        scans of the exec block#3'. An scan index or a
                        scan index range not preceded by an exec block
                        index will be interpreted as 'all the scans
                        with such indexes in all the exec blocks'.  

                   Default Value: 

                ignore_time: All the rows of the tables Feed, History, Pointing,
Source, SysCal, CalDevice, SysPower, and Weather are processed
independently of the time range of the selected exec block / scan.
                     Default: False
                     Options: False|True

                   Default Value: False

                process_syspower:  The SysPower table is processed if and only if this
parameter is set to true.
                     Default: True
                     Options: True|False

                   Default Value: True

                process_caldevice: The CalDevice table is processed if and only if this
parameter is set to true.
                     Default: True
                     Options: True|False

                   Default Value: True

                process_pointing: The Pointing table is processed if and only if this
parameter is set to true. 
                     Default: True
                     Options: True|False

                     If set to False, the POINTING table is empty in
                     the resulting MS

                   Default Value: True

                process_flags: Create online flags based on the Flag.xml, Antenna.xml
and SpectralWindow.xml files and copy them to the FLAG_CMD sub-table
of the MS.
                     Default: True
                     Options: True|False

                     The flags will NOT be applied unless  the
                     parameter applyflags is set to True. Optionally,
                     the flags can also be saved to an external ASCII
                     file if savecmds is set to True.

                   Default Value: True

                tbuff: Time padding buffer (seconds)
                     Subparameter of process_flags=True
                     Default: 0.0

                     NOTE: this time is in seconds. You should
                     currently set the value of tbuff to be 1.5x the
                     correlator integration time if greater than 1
                     second. For example, if the SDM has integrations
                     of 3 seconds, set tbuff=4.5.  Likewise, set
                     tbuff=15.0 for 10-sec integrations.

                   Default Value: 0.0

                applyflags: Apply the online flags to the MS.
                     Subparameter of process_flags=True
                     Default: False
                     Options: False|True

                   Default Value: False

                savecmds: Save the flag commands to an ASCII file given by the
parameter outfile. 
                     Subparameter of process_flags=True
                     Default: False
                     Options: False|True

                   Default Value: False

                outfile: Filename or list of filenames where to save the online
flag commands.
                     Subparameter of process_flags=True
                     Default: '' (it will save on a filename composed
                     from the MS name(s).) E.g., for vis='uid_A02.ms',
                     the outfile will be 'uid_A02_cmd.txt'.

                   Default Value: 

                flagbackup: Back up flag column before applying flags.
                     Default: True
                     Options: True|False

                   Default Value: True

                verbose: Produce log output as asdm2MS is being run
                     Default: False
                     Options: False|True

                   Default Value: False

                overwrite: Over write an existing MS(s) or MS(s), if the option
wvr_corrected_data='both'
                     Default: False  (do not overwrite)
                     Options: False|True

                     NOTE: the overwrite parameter affects all the
                     output of the task. If any of the following
                     exist, it will not overwrite them. MS(s),
                     .flagversions, online flag files. When set to
                     True, it will overwrite the MS, .flagversions and
                     online flag file.    

                   Default Value: False

                showversion: Report the version of asdm2MS being used
                     Default: False
                     Options: False|True

                   Default Value: False

                useversion: Version of asdm2MS to be used
                     Default: 'v3' (should work for all data)

                   Default Value: v3
                   Allowed Values:
                                v3
                                

                bdfflags: Set the MS FLAG column according to the ASDM _binary_
flags
                     Default: False
                     Options: False|True

                   Default Value: False

                with_pointing_correction: Add (ASDM::Pointing::encoder -
ASDM::Pointing::pointingDirection) to the value to be written in
MS::Pointing::direction
                     Default: False
                     Options: False|True

                   Default Value: False

                remove_ref_undef: If set to True then apply fixspwbackport on the resulting
MS(es).
                     Default: False
                     Options: False|True

                   Default Value: False

                convert_ephem2geo: if True, convert any attached ephemerides to the GEO
reference frame (time-spacing not changed)
                     Default: True
                     Options: True|False

                     ALMA uses ephemerides with observer location
                     equal to the ALMA site. For later processing of
                     the radial velocity information in, e.g. cvel,  a
                     geocentric ephemeris is needed. Setting this
                     option to True will perform the conversion of
                     positions and velocities on all attached
                     ephemerides in the imported MS. This will neither
                     change the time-spacing nor the duration of the
                     ephemeris. No interpolation in time is done.

                   Default Value: True

                polyephem_tabtimestep: Timestep (days) for the tabulation of polynomial
ephemerides. A value less than or equal to 0 disables tabulation.
                     Default: 0

                     Presently, VLA data can contain polynomial
                     ephemerides. ALMA data uses tabulated values.

                   Default Value: 0.

        Returns: void

        Example :
        
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTASDM IN CASA DOCS:
https://casa.nrao.edu/casadocs/
  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'importasdm'
        self.__globals__['taskname'] = 'importasdm'
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

            myparams['asdm'] = asdm = self.parameters['asdm']
            myparams['vis'] = vis = self.parameters['vis']
            myparams['createmms'] = createmms = self.parameters['createmms']
            myparams['separationaxis'] = separationaxis = self.parameters['separationaxis']
            myparams['numsubms'] = numsubms = self.parameters['numsubms']
            myparams['corr_mode'] = corr_mode = self.parameters['corr_mode']
            myparams['srt'] = srt = self.parameters['srt']
            myparams['time_sampling'] = time_sampling = self.parameters['time_sampling']
            myparams['ocorr_mode'] = ocorr_mode = self.parameters['ocorr_mode']
            myparams['compression'] = compression = self.parameters['compression']
            myparams['lazy'] = lazy = self.parameters['lazy']
            myparams['asis'] = asis = self.parameters['asis']
            myparams['wvr_corrected_data'] = wvr_corrected_data = self.parameters['wvr_corrected_data']
            myparams['scans'] = scans = self.parameters['scans']
            myparams['ignore_time'] = ignore_time = self.parameters['ignore_time']
            myparams['process_syspower'] = process_syspower = self.parameters['process_syspower']
            myparams['process_caldevice'] = process_caldevice = self.parameters['process_caldevice']
            myparams['process_pointing'] = process_pointing = self.parameters['process_pointing']
            myparams['process_flags'] = process_flags = self.parameters['process_flags']
            myparams['tbuff'] = tbuff = self.parameters['tbuff']
            myparams['applyflags'] = applyflags = self.parameters['applyflags']
            myparams['savecmds'] = savecmds = self.parameters['savecmds']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['flagbackup'] = flagbackup = self.parameters['flagbackup']
            myparams['verbose'] = verbose = self.parameters['verbose']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['showversion'] = showversion = self.parameters['showversion']
            myparams['useversion'] = useversion = self.parameters['useversion']
            myparams['bdfflags'] = bdfflags = self.parameters['bdfflags']
            myparams['with_pointing_correction'] = with_pointing_correction = self.parameters['with_pointing_correction']
            myparams['remove_ref_undef'] = remove_ref_undef = self.parameters['remove_ref_undef']
            myparams['convert_ephem2geo'] = convert_ephem2geo = self.parameters['convert_ephem2geo']
            myparams['polyephem_tabtimestep'] = polyephem_tabtimestep = self.parameters['polyephem_tabtimestep']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['asdm'] = asdm
        mytmp['vis'] = vis
        mytmp['createmms'] = createmms
        mytmp['separationaxis'] = separationaxis
        mytmp['numsubms'] = numsubms
        mytmp['corr_mode'] = corr_mode
        mytmp['srt'] = srt
        mytmp['time_sampling'] = time_sampling
        mytmp['ocorr_mode'] = ocorr_mode
        mytmp['compression'] = compression
        mytmp['lazy'] = lazy
        mytmp['asis'] = asis
        mytmp['wvr_corrected_data'] = wvr_corrected_data
        mytmp['scans'] = scans
        mytmp['ignore_time'] = ignore_time
        mytmp['process_syspower'] = process_syspower
        mytmp['process_caldevice'] = process_caldevice
        mytmp['process_pointing'] = process_pointing
        mytmp['process_flags'] = process_flags
        mytmp['tbuff'] = tbuff
        mytmp['applyflags'] = applyflags
        mytmp['savecmds'] = savecmds
        mytmp['outfile'] = outfile
        mytmp['flagbackup'] = flagbackup
        mytmp['verbose'] = verbose
        mytmp['overwrite'] = overwrite
        mytmp['showversion'] = showversion
        mytmp['useversion'] = useversion
        mytmp['bdfflags'] = bdfflags
        mytmp['with_pointing_correction'] = with_pointing_correction
        mytmp['remove_ref_undef'] = remove_ref_undef
        mytmp['convert_ephem2geo'] = convert_ephem2geo
        mytmp['polyephem_tabtimestep'] = polyephem_tabtimestep
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'importasdm.xml')

        casalog.origin('importasdm')
        try :
          #if not trec.has_key('importasdm') or not casac.casac.utils().verify(mytmp, trec['importasdm']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['importasdm'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('importasdm', 'importasdm.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'importasdm'
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
          result = importasdm(asdm, vis, createmms, separationaxis, numsubms, corr_mode, srt, time_sampling, ocorr_mode, compression, lazy, asis, wvr_corrected_data, scans, ignore_time, process_syspower, process_caldevice, process_pointing, process_flags, tbuff, applyflags, savecmds, outfile, flagbackup, verbose, overwrite, showversion, useversion, bdfflags, with_pointing_correction, remove_ref_undef, convert_ephem2geo, polyephem_tabtimestep)

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
             tname = 'importasdm'
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
#        paramgui.runTask('importasdm', myf['_ip'])
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
        a['asdm']  = ''
        a['vis']  = ''
        a['createmms']  = False
        a['corr_mode']  = 'all'
        a['srt']  = 'all'
        a['time_sampling']  = 'all'
        a['ocorr_mode']  = 'ca'
        a['compression']  = False
        a['lazy']  = False
        a['asis']  = ''
        a['wvr_corrected_data']  = 'no'
        a['scans']  = ''
        a['ignore_time']  = False
        a['process_syspower']  = True
        a['process_caldevice']  = True
        a['process_pointing']  = True
        a['process_flags']  = True
        a['flagbackup']  = True
        a['verbose']  = False
        a['overwrite']  = False
        a['showversion']  = False
        a['useversion']  = 'v3'
        a['bdfflags']  = False
        a['with_pointing_correction']  = False
        a['remove_ref_undef']  = False
        a['convert_ephem2geo']  = True
        a['polyephem_tabtimestep']  = 0.

        a['createmms'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'separationaxis':'auto'}, {'numsubms':'auto'}])}
        a['process_flags'] = {
                    0:odict([{'value':True}, {'tbuff':0.0}, {'applyflags':False}, {'savecmds':False}, {'outfile':''}]), 
                    1:{'value':False}}

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
    def description(self, key='importasdm', subkey=None):
        desc={'importasdm': 'Convert an ALMA Science Data Model observation into a CASA visibility file (MS)',
               'asdm': 'Name of input asdm directory (on disk)',
               'vis': 'Root name of the ms to be created. Note the .ms is NOT added',
               'createmms': 'Create a Multi-MS output',
               'separationaxis': 'Axis to do parallelization across (scan, spw, baseline, auto)',
               'numsubms': 'The number of SubMSs to create (auto or any number)',
               'corr_mode': 'Specifies the correlation mode to be considered on input. A quoted string containing a sequence of ao, co, ac,or all separated by whitespaces is expected',
               'srt': 'Specifies the spectral resolution type to be considered on input. A quoted string containing a sequence of fr, ca, bw, or all separated by whitespaces is expected',
               'time_sampling': 'Specifies the time sampling (INTEGRATION and/or SUBINTEGRATION)  to be considered on input. A quoted string containing a sequence of i, si, or all separated by whitespaces is expected',
               'ocorr_mode': 'Output data for correlation mode AUTO_ONLY (ao) or CROSS_ONLY (co) or CROSS_AND_AUTO (ca)',
               'compression': 'Flag for turning on data compression',
               'lazy': 'Make the MS DATA column read the ASDM Binary data directly (faster import, smaller MS)',
               'asis': 'Creates verbatim copies of the ASDMtables in the ouput measurement set. Value given must be a string of table names separated by spaces; A * wildcard is allowed.',
               'wvr_corrected_data': 'Specifies which values are considerd in the SDM binary data to fill the DATA column in the MAIN table of the MS; yes for corrected, no for uncorrected, both for corrected and uncorrected (resulting in two MSs)',
               'scans': 'Processes only the specified scans.  A scan specification consists in an exec bock index followed by the : character, followed by a comma separated list of scan indexes or scan index ranges. (e.g. 0:1;1:2~6,8;2:,3:24~30)',
               'ignore_time': 'All the rows of the tables Feed, History, Pointing, Source, SysCal, CalDevice, SysPower, and Weather are processed independently of the time range of the selected exec block / scan.',
               'process_syspower': 'Process the SysPower table?',
               'process_caldevice': 'Process the CalDevice table?',
               'process_pointing': 'Process the Pointing table?',
               'process_flags': 'Create online flags in the FLAG_CMD sub-table?',
               'tbuff': 'Time padding buffer (seconds)',
               'applyflags': 'Apply the flags to the MS.',
               'savecmds': 'Save flag commands to an ASCII file',
               'outfile': 'Name of ASCII file to save flag commands',
               'flagbackup': 'Back up flag column before applying flags.',
               'verbose': 'Output lots of information while the filler is working',
               'overwrite': 'Over write an existing MS(s)',
               'showversion': 'Report the version of asdm2MS being used',
               'useversion': 'Version of asdm2MS to be used (v3 default, should work for all data)',
               'bdfflags': 'Set the MS FLAG column according to the ASDM _binary_ flags',
               'with_pointing_correction': 'Add (ASDM::Pointing::encoder - ASDM::Pointing::pointingDirection) to the value to be written in MS::Pointing::direction',
               'remove_ref_undef': 'If set to True then apply fixspwbackport on the resulting MS(es).',
               'convert_ephem2geo': 'if True, convert any attached ephemerides to the GEO reference frame (time-spacing not changed)',
               'polyephem_tabtimestep': 'Timestep (days) for the tabulation of polynomial ephemerides. A value <= 0 disables tabulation.',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['asdm']  = ''
        a['vis']  = ''
        a['createmms']  = False
        a['separationaxis']  = 'auto'
        a['numsubms']  = 'auto'
        a['corr_mode']  = 'all'
        a['srt']  = 'all'
        a['time_sampling']  = 'all'
        a['ocorr_mode']  = 'ca'
        a['compression']  = False
        a['lazy']  = False
        a['asis']  = ''
        a['wvr_corrected_data']  = 'no'
        a['scans']  = ''
        a['ignore_time']  = False
        a['process_syspower']  = True
        a['process_caldevice']  = True
        a['process_pointing']  = True
        a['process_flags']  = True
        a['tbuff']  = 0.0
        a['applyflags']  = False
        a['savecmds']  = False
        a['outfile']  = ''
        a['flagbackup']  = True
        a['verbose']  = False
        a['overwrite']  = False
        a['showversion']  = False
        a['useversion']  = 'v3'
        a['bdfflags']  = False
        a['with_pointing_correction']  = False
        a['remove_ref_undef']  = False
        a['convert_ephem2geo']  = True
        a['polyephem_tabtimestep']  = 0.

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['createmms']  == True:
            a['separationaxis'] = 'auto'
            a['numsubms'] = 'auto'

        if self.parameters['process_flags']  == True:
            a['tbuff'] = 0.0
            a['applyflags'] = False
            a['savecmds'] = False
            a['outfile'] = ''

        if a.has_key(paramname) :
              return a[paramname]
importasdm_cli = importasdm_cli_()
