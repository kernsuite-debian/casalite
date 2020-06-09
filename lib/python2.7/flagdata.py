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
import task_flagdata
def flagdata(vis='', mode='manual', autocorr=False, inpfile='', reason='any', tbuff=0.0, spw='', field='', antenna='', uvrange='', timerange='', correlation='', scan='', intent='', array='', observation='', feed='', clipminmax=[], datacolumn='DATA', clipoutside=True, channelavg=False, chanbin=1, timeavg=False, timebin='0s', clipzeros=False, quackinterval=1.0, quackmode='beg', quackincrement=False, tolerance=0.0, addantenna='', lowerlimit=0.0, upperlimit=90.0, ntime='scan', combinescans=False, timecutoff=4.0, freqcutoff=3.0, timefit='line', freqfit='poly', maxnpieces=7, flagdimension='freqtime', usewindowstats='none', halfwin=1, extendflags=True, winsize=3, timedev='', freqdev='', timedevscale=5.0, freqdevscale=5.0, spectralmax=1E6, spectralmin=0.0, antint_ref_antenna='', minchanfrac=0.6, verbose=False, extendpols=True, growtime=50.0, growfreq=50.0, growaround=False, flagneartime=False, flagnearfreq=False, minrel=0.0, maxrel=1.0, minabs=0, maxabs=-1, spwchan=False, spwcorr=False, basecnt=False, fieldcnt=False, name='Summary', action='apply', display='', flagbackup=True, savepars=False, cmdreason='', outfile='', overwrite=True, writeflags=True):

        """All-purpose flagging task based on data-selections and flagging modes/algorithms.

FOR MORE INFORMATION, SEE THE TASK PAGES OF FLAGDATA IN CASA DOCS:
https://casa.nrao.edu/casadocs/


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['mode'] = mode
        mytmp['autocorr'] = autocorr
        mytmp['inpfile'] = inpfile
        mytmp['reason'] = reason
        mytmp['tbuff'] = tbuff
        mytmp['spw'] = spw
        mytmp['field'] = field
        mytmp['antenna'] = antenna
        mytmp['uvrange'] = uvrange
        mytmp['timerange'] = timerange
        mytmp['correlation'] = correlation
        mytmp['scan'] = scan
        mytmp['intent'] = intent
        mytmp['array'] = array
        mytmp['observation'] = observation
        mytmp['feed'] = feed
        mytmp['clipminmax'] = clipminmax
        mytmp['datacolumn'] = datacolumn
        mytmp['clipoutside'] = clipoutside
        mytmp['channelavg'] = channelavg
        mytmp['chanbin'] = chanbin
        mytmp['timeavg'] = timeavg
        mytmp['timebin'] = timebin
        mytmp['clipzeros'] = clipzeros
        mytmp['quackinterval'] = quackinterval
        mytmp['quackmode'] = quackmode
        mytmp['quackincrement'] = quackincrement
        mytmp['tolerance'] = tolerance
        mytmp['addantenna'] = addantenna
        mytmp['lowerlimit'] = lowerlimit
        mytmp['upperlimit'] = upperlimit
        mytmp['ntime'] = ntime
        mytmp['combinescans'] = combinescans
        mytmp['timecutoff'] = timecutoff
        mytmp['freqcutoff'] = freqcutoff
        mytmp['timefit'] = timefit
        mytmp['freqfit'] = freqfit
        mytmp['maxnpieces'] = maxnpieces
        mytmp['flagdimension'] = flagdimension
        mytmp['usewindowstats'] = usewindowstats
        mytmp['halfwin'] = halfwin
        mytmp['extendflags'] = extendflags
        mytmp['winsize'] = winsize
        mytmp['timedev'] = timedev
        mytmp['freqdev'] = freqdev
        mytmp['timedevscale'] = timedevscale
        mytmp['freqdevscale'] = freqdevscale
        mytmp['spectralmax'] = spectralmax
        mytmp['spectralmin'] = spectralmin
        mytmp['antint_ref_antenna'] = antint_ref_antenna
        mytmp['minchanfrac'] = minchanfrac
        mytmp['verbose'] = verbose
        mytmp['extendpols'] = extendpols
        mytmp['growtime'] = growtime
        mytmp['growfreq'] = growfreq
        mytmp['growaround'] = growaround
        mytmp['flagneartime'] = flagneartime
        mytmp['flagnearfreq'] = flagnearfreq
        mytmp['minrel'] = minrel
        mytmp['maxrel'] = maxrel
        mytmp['minabs'] = minabs
        mytmp['maxabs'] = maxabs
        mytmp['spwchan'] = spwchan
        mytmp['spwcorr'] = spwcorr
        mytmp['basecnt'] = basecnt
        mytmp['fieldcnt'] = fieldcnt
        mytmp['name'] = name
        mytmp['action'] = action
        mytmp['display'] = display
        mytmp['flagbackup'] = flagbackup
        mytmp['savepars'] = savepars
        mytmp['cmdreason'] = cmdreason
        mytmp['outfile'] = outfile
        mytmp['overwrite'] = overwrite
        mytmp['writeflags'] = writeflags
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'flagdata.xml')

        casalog.origin('flagdata')
        if trec.has_key('flagdata') and casac.utils().verify(mytmp, trec['flagdata']) :
            result = task_flagdata.flagdata(vis, mode, autocorr, inpfile, reason, tbuff, spw, field, antenna, uvrange, timerange, correlation, scan, intent, array, observation, feed, clipminmax, datacolumn, clipoutside, channelavg, chanbin, timeavg, timebin, clipzeros, quackinterval, quackmode, quackincrement, tolerance, addantenna, lowerlimit, upperlimit, ntime, combinescans, timecutoff, freqcutoff, timefit, freqfit, maxnpieces, flagdimension, usewindowstats, halfwin, extendflags, winsize, timedev, freqdev, timedevscale, freqdevscale, spectralmax, spectralmin, antint_ref_antenna, minchanfrac, verbose, extendpols, growtime, growfreq, growaround, flagneartime, flagnearfreq, minrel, maxrel, minabs, maxabs, spwchan, spwcorr, basecnt, fieldcnt, name, action, display, flagbackup, savepars, cmdreason, outfile, overwrite, writeflags)

        else :
          result = False
        return result
