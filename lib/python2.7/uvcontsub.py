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
import task_uvcontsub
def uvcontsub(vis='', field='', fitspw='', excludechans=False, combine='', solint='int', fitorder=0, spw='', want_cont=False):

        """Continuum fitting and subtraction in the uv plane

        Continuum fitting and subtraction in the uv plane:
            
        This task estimates the continuum emission by fitting polynomials to
        the real and imaginary parts of the spectral windows and channels
        selected by fitspw.  This fit represents a model of the continuum in 
        all channels.

        The fitted continuum spectrum is subtracted from all channels 
        selected in spw, and the result (presumably only line emission)
        is stored in a new MS (vis + ".contsub"). If an MS  
        with the output name already exists, it will be overwritten.
        It will read from the CORRECTED_DATA column of vis if it is present,
        or DATA if it is not.  Whichever column is read is presumed to have
        already been calibrated.

        If want_cont is True, the continuum fit is placed in a second new MS
        (vis + '.cont', also overwritten if it already exists).  
        N.B. because the continuum model is necessarily a
        smoothed fit, images made with it are liable to have their field of
        view reduced in some strange way.  Images of the continuum should be
        made by simply excluding the line channels (and probably averaging the
        remaining ones) in clean.

        Keyword arguments:
        vis -- Name of input visibility file
                default: none; example: vis='ngc5921.ms'
        field -- Field selection for continuum estimation and subtraction.
                 The estimation and subtraction is done for each selected field
                 in turn.  (Run listobs to get lists of the ID and names.)
                default: field = '' means select all fields
                field = 1 # will get field_id=1 (if you give it an 
                        integer, it will retrieve the source with that index.
                field = '1328+307'  specifies source '1328+307'
                field = '13*' will retrieve '1328+307' and any other fields
                   beginning with '13'
        fitspw -- Selection of spectral windows and channels to use in the
                  fit for the continuum, using general spw:chan syntax.
                  The ranges of channels also can be specified by frequencies as in
                  the MS selection syntax (spw ids are required but '*' can be 
                  used, see the example below).
                  See the note under combine.
                default: '' (all)
                example: fitspw='0:5~30;40~55'
                                 --> select the ranges by channels in the spw id 0 
                         fitspw='0:5~30;40~55,1:10~25;45~58,2'
                                 --> select channel ranges 5-30 and 40-55 for the spw id 0, 
                                        10-25 and 45-58 for spwid 1, and use all channels for the spw id 2
                         fitspw='0:113.767~114.528GHz;114.744~115.447GHz'
                                 --> select the ranges by frequencies in the spw id 0 
                         fitspw='0:113.767~114.528GHz;114.744~115.447GHz,1:111.892~112.654GHz;112.868~113.025GHz'
                                 --> select the different ranges by frequencies for the spw ids 0 and 1 
                         fitspw='*:113.767~114.528GHz;114.744~115.447GHz'
                                 --> select the same frequency ranges for all the relevant spws 
         >>> expandable parameter for fitspw 
          excludechans - if True, it will exclude the spws:channels specified in fitspw
                         for the fit
                default: False (use fitspw for the fit) 
                example: fitspw='0:114.528GHz~114.744GHz'; excludechans=True
                         --> exclude the frequency range, 114.528GHz - 114.744GHz in the spw id 0
        combine -- Data axes to combine for the continuum estimate.
                It must include 'spw' if spw contains spws that are not in
                fitspw!
                default: '' --> solutions will break at scan, field, and spw
                      boundaries according to solint
              Options: '', 'spw'', 'scan', or 'spw, scan'
              example: combine='spw' --> form spw-merged continuum estimate
        solint -- Timescale for per-baseline fit (units optional)
                default (recommended): 'int' --> no time averaging, do a
                                       fit for each integration and let the
                                       noisy fits average out in the image.

                example: solint='10s'  --> average to 10s before fitting
                         10 or '10' --> '10s' (unitless: assumes seconds)
                options: 'int' --> per integration
                         'inf' --> per scan

                If solint is longer than 'int', the continuum estimate can be
                corrupted by time smearing!

        fitorder -- Polynomial order for the fits of the continuum w.r.t.
                    frequency.  fitorders > 1 are strongly discouraged
                    because high order polynomials have more flexibility, may
                    absorb line emission, and tend go wild at the edges of
                    fitspw, which is not what you want.

                default: 0 (constant); example: fitorder=1

        spw -- Optional per spectral window selection of channels to include
               in the output.  See the note under combine.

               The spectral windows will be renumbered to start from 0, as in
               split.
        want_cont -- Create vis + '.cont' to hold the continuum estimate.
                default: 'False'; example: want_cont=True
                The continuum estimate will be placed in vis + '.cont'
        async -- Run task in a separate process (return CASA prompt)
                default: False; example: async=True


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['fitspw'] = fitspw
        mytmp['excludechans'] = excludechans
        mytmp['combine'] = combine
        mytmp['solint'] = solint
        mytmp['fitorder'] = fitorder
        mytmp['spw'] = spw
        mytmp['want_cont'] = want_cont
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'uvcontsub.xml')

        casalog.origin('uvcontsub')
        if trec.has_key('uvcontsub') and casac.utils().verify(mytmp, trec['uvcontsub']) :
            result = task_uvcontsub.uvcontsub(vis, field, fitspw, excludechans, combine, solint, fitorder, spw, want_cont)

        else :
          result = False
        return result
