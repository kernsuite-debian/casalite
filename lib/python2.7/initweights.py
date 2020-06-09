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
import task_initweights
def initweights(vis='', wtmode='nyq', tsystable='', gainfield='', interp='', spwmap=[], dowtsp=False):

        """Initializes weight information in the MS

      This task provides for initialization of the weight information
      in the MS.  For ALMA interferometry and EVLA data, it should not
      generally be necessary to use this task, as the weight information 
      should have been initialized properly at fill time (v4.2.2 and later).

      Several initialization modes are supported via the wtmode parameter.

      If wtmode='nyq' (the default), SIGMA and WEIGHT will be
      initialized according to bandwidth and integration time.  This
      is the theoretically correct mode for raw normalized visibilities.
      (e.g., ALMA).  For the EVLA, this is correct if switched-power
      and bandpass calibration will later be applied.  

      If wtmode='sigma', WEIGHT will be initialized according to the
      existing SIGMA column.  

      If wtmode='weight', WEIGHT_SPECTRUM will be initialized according
      to the existing WEIGHT column; dowtspec=T must be specified in
      this case.
 
      If wtmode='ones', SIGMA and WEIGHT will be initialized with 1.0,
      globally.  This is a traditional means of initializing weight
      information, and is adequate when the integration time and 
      bandwidth are uniform. It is not recommended for modern
      instruments (ALMA, EVLA), where variety in observational setups
      is common, and properly initialized and calibrated weights
      will be used for imaging sensitivity estimates.

      There are two EXPERIMENTAL modes, wtmode='tsys' and 'tinttsys'.
      In the modes, SIGMA and WEIGHT will be initialized according to
      Tsys, bandwidth, and integration time (used only in 'tinttsys'),
      i.e.,
          tsys    : weight=bw/Tsys^2
          tinttsys: weight=bw*t_int/Tsys^2
      These modes use Tsys values to calculate weight as is done in
      Tsys calibration. Tsys values are taken from a tsys calibration
      table given as tsystable. Selection of gain field (gainfield),
      interpolation method (interp), and spectral window mapping (spwmap)
      are supported, too.
      Available types of interpolation are,
          Time: 'nearest', 'linear', the variation of those with 'perobs',
                e.g., 'linearperobs' (enforce obsId boundaries in interpolation)
          Freq: 'nearest', 'linear', 'cubic', 'spline', and the variation
                of those with 'flag', e.g., 'linearflag' (with
                channelized flag).
      See the help of applycal for details of interpolations.
      Note if the weight in an MS is initialized with these modes and
      Tsys calibration table is applied with calwt=True after that, the
      weight would be contaminated by being devided by square of Tsys
      twice.
      !!! USERS ARE ADVICED TO USE THESE EXPERIMENTAL MODES WITH CARE !!!

      For the above wtmodes, if dowtsp=T (or if the WEIGHT_SPECTRUM
      column already exists), the WEIGHT_SPECTRUM column will be
      initialized (uniformly in channel in wtmode='nyq', 'sigma',
      'weight', and 'ones'), in a manner consistent with the
      disposition of the WEIGHT column.  If the WEIGHT_SPECTRUM 
      column does not exist, dowtsp=T will force its creation.
      Use of the WEIGHT_SPECTRUM column is only meaningful
      for ALMA data which will be calibrated with channelized
      Tsys information, or if the weights will become channelized
      after calibration, e.g., via averaging over time- and 
      channel-dependent flagging.  (A task for channel-dependent
      weight estimation from the data itself is also currently under
      development).
      In non-channelized modes (wtmode='nyq', 'sigma', 'weight', and
      'ones') or when dowtsp=F, SIGMA_SPECTRUM column will be removed
      from MS. On the other hand, SIGMA_SPECTRUM column is added and
      initialized in channelized modes (wtmode='tsys' and 'tinttsys')
      if dowtsp=T or WEIGHT_SPECTRUM already column exists.

      Two additional modes are available for managing the spectral
      weight info columns; these should be used with extreme care: If
      wtmode='delwtsp', the WEIGHT_SPECTRUM column will be deleted (if
      it exists).  If wtmode='delsigsp', the SIGMA_SPECTRUM column
      will be deleted (if it exists).  Note that creation of
      SIGMA_SPECTRUM is not supported via this method.

      Note that this task does not support any prior selection.  
      Intialization of the weight information must currently be done 
      globally or not at all.  This is to maintain consistency.

 
        """
        if type(spwmap)==int: spwmap=[spwmap]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['wtmode'] = wtmode
        mytmp['tsystable'] = tsystable
        mytmp['gainfield'] = gainfield
        mytmp['interp'] = interp
        mytmp['spwmap'] = spwmap
        mytmp['dowtsp'] = dowtsp
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'initweights.xml')

        casalog.origin('initweights')
        if trec.has_key('initweights') and casac.utils().verify(mytmp, trec['initweights']) :
            result = task_initweights.initweights(vis, wtmode, tsystable, gainfield, interp, spwmap, dowtsp)

        else :
          result = False
        return result
