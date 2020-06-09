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
import task_importasdm
def importasdm(asdm='', vis='', createmms=False, separationaxis='auto', numsubms='auto', corr_mode='all', srt='all', time_sampling='all', ocorr_mode='ca', compression=False, lazy=False, asis='', wvr_corrected_data='no', scans='', ignore_time=False, process_syspower=True, process_caldevice=True, process_pointing=True, process_flags=True, tbuff=0.0, applyflags=False, savecmds=False, outfile='', flagbackup=True, verbose=False, overwrite=False, showversion=False, useversion='v3', bdfflags=False, with_pointing_correction=False, remove_ref_undef=False, convert_ephem2geo=True, polyephem_tabtimestep=0.):

        """Convert an ALMA Science Data Model observation into a CASA visibility file (MS)        
FOR MORE INFORMATION, SEE THE TASK PAGES OF IMPORTASDM IN CASA DOCS:
https://casa.nrao.edu/casadocs/
  
        """

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
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'importasdm.xml')

        casalog.origin('importasdm')
        if trec.has_key('importasdm') and casac.utils().verify(mytmp, trec['importasdm']) :
            result = task_importasdm.importasdm(asdm, vis, createmms, separationaxis, numsubms, corr_mode, srt, time_sampling, ocorr_mode, compression, lazy, asis, wvr_corrected_data, scans, ignore_time, process_syspower, process_caldevice, process_pointing, process_flags, tbuff, applyflags, savecmds, outfile, flagbackup, verbose, overwrite, showversion, useversion, bdfflags, with_pointing_correction, remove_ref_undef, convert_ephem2geo, polyephem_tabtimestep)

        else :
          result = False
        return result
