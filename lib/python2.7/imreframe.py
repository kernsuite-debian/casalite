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
import task_imreframe
def imreframe(imagename='', output='', outframe='lsrk', epoch='', restfreq=''):

        """Change the frame in which the image reports its spectral values

            imagename -- name of casa image file to process on
            output         -- name of output image  '' means modify the input image itself
                 default: '';
            outframe     -- new spectral frame in which the frequency or
                                  velocity will be reported for.
                 Options: 'lsrk','lsrd','bary','geo','topo','galacto',
                          'lgroup','cmb'
                 default: 'lsrk'
            >>>
                 epoch    -- when outframe is 'topo' or 'geo' a time in UTC is needed
                                 to decide when to do the frequency conversion. '' is to use
                                 the epoch of the input image
                       default= ''

            restfreq -- Specify rest frequency to use for output image
               default=''; '' means use the restfrequency already in input image
               For example for
               NH_3 (1,1) put restfreq='23.694496GHz'


        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['output'] = output
        mytmp['outframe'] = outframe
        mytmp['epoch'] = epoch
        mytmp['restfreq'] = restfreq
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'imreframe.xml')

        casalog.origin('imreframe')
        if trec.has_key('imreframe') and casac.utils().verify(mytmp, trec['imreframe']) :
            result = task_imreframe.imreframe(imagename, output, outframe, epoch, restfreq)

        else :
          result = False
        return result
