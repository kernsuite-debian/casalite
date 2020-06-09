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
import task_msuvbin
def msuvbin(vis='', field='', spw='', taql='', outvis='', phasecenter='', nx=1000, ny=1000, cell='1arcsec', ncorr=1, nchan=1, fstart='1GHz', fstep='1kHz', wproject=False, memfrac=0.5):

        """grid the visibility data onto a defined uniform grid (in the form of an ms); multiple MS\'s can be done onto the same grid




       Keyword arguments:
       vis -- Name of input visibility file
              default: none; example: vis='ngc5921.ms'
       field -- Field name list
               default: '' ==> all
               field = '1328+307'  specifies source '1328+307'
               field = '4' specified field with index 4
       spw -- Spw selection
               default: spw = '' (all spw)
               spw='2'
       taql  --TaQl expression for data selection (see http://www.astron.nl/casacore/trunk/casacore/doc/notes/199.html)
               default taql=''
               Example select all data where U > 1 m in the ms
               taql='UVW[0] > 1'
       outvis -- name of output grid
               default: ''  The user has to give something here
       phasecenter -- phasecenter of the grid
               default= ''
                phasecenter='J2000 18h03m04 -20d00m45.1'
      nx  -- number of pixels along the x axis of the grid
               default: 1000
               nx=1200
      ny  -- number of pixels along the y axis of the grid
               default: 1000
               ny=1200
       cell -- cellsize of the grid (given in sky units)
               default: '1arcsec'
               cell='0.1arcsec'
        ncorr -- number of correlation/polarization plane in uv grid (allowed 1, 2, 4)
               default: 1
               ncorr=4
        nchan -- number of spectral channel
               default: 1
               nchan=2000
        fstart -- frequency of the first channel
               default: '1GHz';  User has to give something useful here
        fstep -- spectral channel width
               default: '1kHz'
        wproject -- do wprojection correction while gridding
                default: False
                wproject=True
        memfrac -- control how much of computer's memory is available for  gridding
                default=0.5
                memfrac=0.9

 
        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['taql'] = taql
        mytmp['outvis'] = outvis
        mytmp['phasecenter'] = phasecenter
        mytmp['nx'] = nx
        mytmp['ny'] = ny
        mytmp['cell'] = cell
        mytmp['ncorr'] = ncorr
        mytmp['nchan'] = nchan
        mytmp['fstart'] = fstart
        mytmp['fstep'] = fstep
        mytmp['wproject'] = wproject
        mytmp['memfrac'] = memfrac
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'msuvbin.xml')

        casalog.origin('msuvbin')
        if trec.has_key('msuvbin') and casac.utils().verify(mytmp, trec['msuvbin']) :
            result = task_msuvbin.msuvbin(vis, field, spw, taql, outvis, phasecenter, nx, ny, cell, ncorr, nchan, fstart, fstep, wproject, memfrac)

        else :
          result = False
        return result
