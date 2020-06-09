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
import task_cvel
def cvel(vis='', outputvis='', passall=False, field='', spw='', selectdata=True, antenna='', timerange='', scan='', array='', mode='channel', nchan=-1, start=0, width=1, interpolation='linear', phasecenter='', restfreq='', outframe='', veltype='radio', hanning=False):

        """regrid an MS to a new spectral window / channel structure or frame

       vis -- Name of input visibility file
               default: none; example: vis='ngc5921.ms'    

       outputvis -- Name of output measurement set (required)
               default: none; example: vis='ngc5921-regridded.ms'    
               
       passall --  if False, data not meeting the selection is omitted/deleted 
               or flagged (if in-row); if True, data not meeting the selection 
               on field and spw is passed through without modification
               default: False; example: 
               field='NGC5921'
               passall=False : only data from NGC5921 is included in output MS, 
                         no data from other fields (e.g. 1331+305) is included
               passall=True : data from NGC5921 is transformed by cvel, all other 
                         fields are passed through unchanged 

       field -- Select fields in mosaic.  Use field id(s) or field name(s).
                  ['go listobs' to obtain the list id's or names]
              default: ''= all fields
              If field string is a non-negative integer, it is assumed to
                  be a field index otherwise, it is assumed to be a 
                  field name
              field='0~2'; field ids 0,1,2
              field='0,4,5~7'; field ids 0,4,5,6,7
              field='3C286,3C295'; field named 3C286 and 3C295
              field = '3,4C*'; field id 3, all names starting with 4C

       spw --Select spectral window/channels
              NOTE: This selects the data passed as the INPUT to mode
              default: ''=all spectral windows and channels
                spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
                spw='0:5~61'; spw 0, channels 5 to 61
                spw='<2';   spectral windows less than 2 (i.e. 0,1)
                spw='0,10,3:3~45'; spw 0,10 all channels, spw 3, 
                                   channels 3 to 45.
                spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
                spw='0:0~10;15~60'; spectral window 0 with channels 
                                    0-10,15-60
                spw='0:0~10,1:20~30,2:1;2;3'; spw 0, channels 0-10,
                      spw 1, channels 20-30, and spw 2, channels, 1,2 and 3

       selectdata -- Other data selection parameters
              default: True

  >>> selectdata=True expandable parameters

              antenna -- Select data based on antenna/baseline
                  default: '' (all)
                  If antenna string is a non-negative integer, it is 
                    assumed to be an antenna index, otherwise, it is
                    considered an antenna name.
                  antenna='5&6'; baseline between antenna index 5 and 
                                 index 6.
                  antenna='VA05&VA06'; baseline between VLA antenna 5 
                                       and 6.
                  antenna='5&6;7&8'; baselines 5-6 and 7-8
                  antenna='5'; all baselines with antenna index 5
                  antenna='05'; all baselines with antenna number 05 
                                (VLA old name)
                  antenna='5,6,9'; all baselines with antennas 5,6,9 
                                   index numbers

              timerange  -- Select data based on time range:
                 default = '' (all); examples,
                  timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                  Note: if YYYY/MM/DD is missing date defaults to first 
                        day in data set
                  timerange='09:14:0~09:54:0' picks 40 min on first day
                  timerange= '25:00:00~27:30:00' picks 1 hr to 3 hr 
                             30min on NEXT day
                  timerange='09:44:00' pick data within one integration 
                             of time
                  timerange='>10:24:00' data after this time

              scan -- Scan number range.
                  default: '' (all)
                  example: scan='1~5'
                  Check 'go listobs' to insure the scan numbers are in 
                        order.

              array -- Select data by (sub)array indices
                  default: '' (all); example:
                  array='0~2'; arrays 0 to 2 

      mode -- Frequency Specification:
               NOTE: See examples below:
               default: 'channel'
                 mode = 'channel'; Use with nchan, start, width to specify
                         output spw. Produces equidistant grid based on first
                         selected channel. See examples below.
                 mode = 'velocity', means channels are specified in 
                      velocity.
                 mode = 'frequency', means channels are specified in 
                      frequency.
                 mode = 'channel_b', alternative 'channel' mode.
                         Does not force an equidistant grid. Faster.

  >>> mode expandable parameters 
               Start, width are given in units of channels, frequency 
                  or velocity as indicated by mode 
               nchan -- Number of channels in output spw
                 default: -1 = all channels; example: nchan=3
               start -- Start or end input channel (zero-based) depending on the sign of the width parameter
                 default=0; example: start=5
               width -- Output channel width in units of the input
                     channel width (sign indicates whether the start parameter is lower(+) or upper(-) end of the range)
                 default=1; example: width=4
               interpolation -- Interpolation method (linear, nearest, cubic, spline, fftshift)
                 default = 'linear'
           examples:
               spw = '0,1'; mode = 'channel'
                  will produce a single spw containing all channels in spw 
                       0 and 1
               spw='0:5~28^2'; mode = 'channel'
                  will produce a single spw made with channels 
                       (5,7,9,...,25,27)
               spw = '0'; mode = 'channel': nchan=3; start=5; width=4
                  will produce an spw with 3 output channels
                  new channel 1 contains data from channels (5+6+7+8)
                  new channel 2 contains data from channels (9+10+11+12)
                  new channel 3 contains data from channels (13+14+15+16)
               spw = '0:0~63^3'; mode='channel'; nchan=21; start = 0; 
                   width = 1
                  will produce an spw with 21 channels
                  new channel 1 contains data from channel 0
                  new channel 2 contains data from channel 2
                  new channel 21 contains data from channel 61
               spw = '0:0~40^2'; mode = 'channel'; nchan = 3; start = 
                   5; width = 4
                  will produce an spw with three output channels
                  new channel 1 contains channels (5,7)
                  new channel 2 contains channels (13,15)
                  new channel 3 contains channels (21,23)

      phasecenter -- Direction measure  or fieldid. To be used in mosaics to indicate
               the center direction to be used in the spectral coordinate transformation.
               default: '' => first field selected ; example: phasecenter=6
               or phasecenter='J2000 19h30m00 -40d00m00'

      restfreq -- Specify rest frequency to use for output visibilities
               default='' Occasionally it is necessary to set this (for
               example some VLA spectral line data).  For example for
               NH_3 (1,1) put restfreq='23.694496GHz'

      outframe -- output reference frame (not case-sensitive)
               possible values: LSRK, LSRD, BARY, GALACTO, LGROUP, CMB, GEO, TOPO, or SOURCE
               (SOURCE is meant for solar system work and corresponds to GEO + radial velocity
               correction for ephemeris objects).
               default='' (keep original reference frame) ; example: outframe='BARY'     

      veltype -- definition of velocity (in mode)
               default = 'radio'

      hanning -- if true, Hanning smooth frequency channel data to remove Gibbs ringing

==================================================================

The intent of cvel is to transform channel labels and the 
visibilities to a spectral reference frame which is appropriate
for the science analysis, e.g. from TOPO to LSRK to correct for 
Doppler shifts throughout the time of the observation. Naturally, 
this will change the shape of the spectral feature to some extent. 
According to the Nyquist theorem you should oversample a spectrum 
with twice the numbers of channels to retain the shape. Based on 
some tests, however, we recommend to observe with at least 
3-4 times the number of channels for each significant spectral 
feature (like 3-4 times the linewidth). This will minimize 
regridding artifacts in cvel.

If cvel has already established the grid that is desired for the
imaging, clean should be run with exactly the same frequency/velocity 
parameters as used in cvel in order to avoid additional regridding in 
clean.

Hanning smoothing is optionally offered in cvel, but tests have 
shown that already the regridding process itself, if it involved 
a transformation from TOPO to a non-terrestrial reference frame, 
implies some smoothing (due to channel interpolation) such that 
Hanning smoothing may not be necessary.

        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['outputvis'] = outputvis
        mytmp['passall'] = passall
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['selectdata'] = selectdata
        mytmp['antenna'] = antenna
        mytmp['timerange'] = timerange
        mytmp['scan'] = scan
        mytmp['array'] = array
        mytmp['mode'] = mode
        mytmp['nchan'] = nchan
        mytmp['start'] = start
        mytmp['width'] = width
        mytmp['interpolation'] = interpolation
        mytmp['phasecenter'] = phasecenter
        mytmp['restfreq'] = restfreq
        mytmp['outframe'] = outframe
        mytmp['veltype'] = veltype
        mytmp['hanning'] = hanning
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'cvel.xml')

        casalog.origin('cvel')
        if trec.has_key('cvel') and casac.utils().verify(mytmp, trec['cvel']) :
            result = task_cvel.cvel(vis, outputvis, passall, field, spw, selectdata, antenna, timerange, scan, array, mode, nchan, start, width, interpolation, phasecenter, restfreq, outframe, veltype, hanning)

        else :
          result = False
        return result
