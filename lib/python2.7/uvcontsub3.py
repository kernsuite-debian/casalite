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
import task_uvcontsub3
def uvcontsub3(vis='', fitspw='', combine='', fitorder=0, field='', spw='', scan='', intent='', correlation='', observation=''):

        """An experimental clone of uvcontsub
  
        uvcontsub3 is an experimental clone of uvcontsub with the goal of taking
        less time and temporary disk space.

        Continuum fitting and subtraction in the uv plane:
        
        This task estimates the continuum emission by fitting polynomials to
        the real and imaginary parts of the spectral windows and channels
        selected by fitspw.  This fit represents a model of the continuum in 
        all channels.
        
        The fitted continuum spectrum is subtracted from all channels 
        selected in spw, and the result (presumably only line emission)
        is stored in a new MS (vis + ".contsub").
        It will read from the CORRECTED_DATA column of vis if it is present,
        or DATA if it is not.  Whichever column is read is presumed to have
        already been calibrated.

        Keyword arguments:
        vis -- Name of input visibility file
                default: none; example: vis='ngc5921.ms'

        fitspw -- Selection of spectral windows and channels to use in the
                  fit for the continuum, using general spw:chan syntax.
                  See the note under combine.
                default: '' (all)
                example: fitspw='0:5~30;40~55'

        combine -- Let the continuum estimation span multiple spectral windows.
                   default = '' (Make separate estimates for each spw.)
                   combine = 'spw': Necessary when one or more of the spws are
                                    completely blanketed by lines, so the estimate
                                    must be made in different spws.

        fitorder -- Polynomial order for the fits of the continuum w.r.t.
                    frequency.  fitorders > 1 are strongly discouraged
                    because high order polynomials have more flexibility, may
                    absorb line emission, and tend go wild at the edges of
                    fitspw, which is not what you want.

                default: 0 (constant); example: fitorder=1

        field -- Field selection for continuum estimation and subtraction.
                 The estimation and subtraction is done for each selected field
                 in turn.  (Run listobs to get lists of the ID and names.)
               default: ''=all fields.  If the field string is a non-negative
                        integer, it is assumed to be a field index
                        otherwise, it is assumed to be a field name
               field='0~2'; field ids 0,1,2
               field='0,4,5~7'; field ids 0,4,5,6,7
               field='3C286,3C295'; fields named 3C286 and 3C295
               field = '3,4C*'; field id 3, all names starting with 4C

        spw -- Select spectral windows for the output.
               default: ''=all spectral windows
               N.B. uvcontsub3 does not yet support exclusion by channels for
                    the output.  Meanwhile, use split to further reduce the size
                    of the output MS if desired.
               spw='0~2,4'; spectral windows 0,1,2,4
               spw='<2';  spectral windows less than 2 (i.e. 0,1)

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

        correlation -- Select correlations, e.g. 'rr, ll' or ['XY', 'YX'].
                       default '' (all).

        observation -- Select by observation ID(s).
                       default: '' = all


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['fitspw'] = fitspw
        mytmp['combine'] = combine
        mytmp['fitorder'] = fitorder
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['correlation'] = correlation
        mytmp['observation'] = observation
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'uvcontsub3.xml')

        casalog.origin('uvcontsub3')
        if trec.has_key('uvcontsub3') and casac.utils().verify(mytmp, trec['uvcontsub3']) :
            result = task_uvcontsub3.uvcontsub3(vis, fitspw, combine, fitorder, field, spw, scan, intent, correlation, observation)

        else :
          result = False
        return result
