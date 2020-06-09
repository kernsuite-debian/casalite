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
import task_predictcomp
def predictcomp(objname='', standard='Butler-JPL-Horizons 2010', epoch='', minfreq='', maxfreq='', nfreqs=2, prefix='', antennalist='', showplot=False, savefig='', symb='.', include0amp=False, include0bl=False, blunit='', showbl0flux=False):

        """Make a component list for a known calibrator

    Writes a component list to disk and returns a dict of
    {'clist': filename of the component list,
     'objname': objname,
     'angdiam': angular diameter in radians (if used in clist),
     'standard': standard,
     'epoch': epoch,
     'freqs': pl.array of frequencies, in GHz,
     'antennalist': pl.array of baseline lengths, in m,
     'amps':  pl.array of predicted visibility amplitudes, in Jy,
     'savedfig': False or, if made, the filename of a plot.}
    or False on error.

    objname: An object supported by standard.
    standard: A standard for calculating flux densities, as in setjy.
              Default: 'Butler-JPL-Horizons 2010'
    epoch: The epoch to use for the calculations.   Irrelevant for
           extrasolar standards. (Uses UTC)
           Examples: '2011-12-31/5:34:12', '2011-12-31-5:34:12'
    minfreq: The minimum frequency to use.
             Example: '342.0GHz'
    maxfreq: The maximum frequency to use.
             Default: minfreq
             Example: '346.0GHz'
             Example: '', anything <= 0, or None: use minfreq.
    nfreqs:  The number of frequencies to use.
             Default: 1 if minfreq == maxfreq,
                      2 otherwise.
    prefix: The component list will be saved to
               prefix + 'spw0_<objname>_<minfreq><epoch>.cl'
            Default: '' 
            Example: "Bands3to7_"
                     (which could produce 'Bands3to7_Uranus_spw0_100GHz55877d.cl',
                      depending on the other parameters)
    antennalist: 'Observe' and plot the visibility amplitudes for this
                 antenna configuration.  The file should be in a format usable
                 by simdata.  The search path is:
                     .:casa['dirs']['data'] + '/alma/simmos/'
             Default: '' (None, just make clist.)
             Example: 'alma.cycle0.extended.cfg'

    Subparameters of antennalist:
    showplot: Whether or not to show a plot of S vs. |u| on screen.
              Subparameter of antennalist.
              Default: Necessarily False if antennalist is not specified.
                       True otherwise.
    savefig: Filename for saving a plot of S vs. |u|.
             Subparameter of antennalist.
             Default: '' 
             Examples: ''           (do not save the plot)
                       'myplot.png' (save to myplot.png)
    symb: One of matplotlib's codes for plot symbols: .:,o^v<>s+xDd234hH|_
          Default: '.'
    include0amp: Force the amplitude axis to start at 0?
                 Default: False
    include0bl: Force the baseline axis to start at 0?
                Default: False
    blunit: unit of the baseline axis ('' or 'klambda')
            Default:''=use a unit in the data
    showbl0flux: Print the zero baseline flux? 
                 Default: False 

     

        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['objname'] = objname
        mytmp['standard'] = standard
        mytmp['epoch'] = epoch
        mytmp['minfreq'] = minfreq
        mytmp['maxfreq'] = maxfreq
        mytmp['nfreqs'] = nfreqs
        mytmp['prefix'] = prefix
        mytmp['antennalist'] = antennalist
        mytmp['showplot'] = showplot
        mytmp['savefig'] = savefig
        mytmp['symb'] = symb
        mytmp['include0amp'] = include0amp
        mytmp['include0bl'] = include0bl
        mytmp['blunit'] = blunit
        mytmp['showbl0flux'] = showbl0flux
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'predictcomp.xml')

        casalog.origin('predictcomp')
        if trec.has_key('predictcomp') and casac.utils().verify(mytmp, trec['predictcomp']) :
            result = task_predictcomp.predictcomp(objname, standard, epoch, minfreq, maxfreq, nfreqs, prefix, antennalist, showplot, savefig, symb, include0amp, include0bl, blunit, showbl0flux)

        else :
          result = False
        return result
