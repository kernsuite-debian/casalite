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
import task_imval
def imval(imagename='', region='', box='', chans='', stokes=''):

        """Get the data value(s) and/or mask value in an image.
     The data point(s) to be retrieved are those found in the specified
     region, which may be:
        1. A region file or text string, with the following caveat:
           * If the specified region is complex (eg, a union or intersection of multiple regions,
             only the first simple region in this set is used.
           * If the region is not rectangular, then the rectangular region that circumscribes the
             specified region (ie the bounding box) is used to retrieve values, since the returned
             arrays must be rectangular. The resulting mask values in this case are the result of
             anding the image mask values with the specified region mask values, eg
             if a pixel falls outside the specified region but within the bounding box, its returned
             mask value will be false even if its image mask value is true.
        2. A region specified by a set of rectangular
           pixel coordinates, the channel ranges and/or the Stokes.

     For directed output, run as 
                    myoutput = imval()
   

        Keyword arguments:
        imagename -- Name of input image
                Default: none; Example: imagename='ngc5921_task.im'
        region -- Region selection. Empty string (default) means use rules for box/chans/stokes specification.
                Example: region='myimage.im.rgn'
                         region='region1'
        box --  Rectangular region to select in direction plane. Empty string (default) means use the reference pixel.
                Default: '' (referencepixel values for the Directional coord); 
                Example: box='10,10,50,50'
                         box = '10,10,30,30,35,35,50,50' (two boxes)
        chans -- Channels to use. Default is to use all channels.
        stokes -- Stokes planes to use. Planes specified must be contiguous. Default is to use all Stokes planes.
                 Example: stokes='IQUV';  
                      stokes='I,Q'

      General procedure:

         1.  Specify inputs, then

         2.  myoutput = imval()
               or specify inputs directly in calling sequence to task
             myoutput = imsval(imagename='image.im', etc)

         3.  myoutput['KEYS'] will contain the result associated with any
               of the keys given below
        
        KEYS CURRENTLY AVAILABLE
        blc          - absolute PIXEL coordinate of the bottom left corner of 
                       the bounding box surrounding the selected region
        trc          - the absolute PIXEL coordinate of the top right corner 
                       of the bounding box surrOunding the selected region
        axes         - List the data stored in each axis of the data block.
        unit         - unit of the returned data values.
        data         - data value(s) found in the given region
        mask         - mask value(s) found in the given region. See important
                       note above regarding returned mask values for
                       non-rectangular regions.

        NOTE: The data returned is in the same order as it is internally
        stored, typically RA, DEC, spectral, stokes. Also both the data
        and mask values are returned as Python Numpy arrays, for more
        information on how to manipulate them see
             http://numpy.scipy.org/#array_interface


        Additional Examples
        # The value and mask value at a single point (5,17,2,Q)
        imval( 'myImage', box='5,5,17,17', chans=2, stokes='Q' )

        # Select and report on two box regions
        # box 1, bottom-left coord is 2,3 and top-right coord is 14,15
        # box 2, bottom-left coord is 30,31 and top-right coord is 42,43
        # Note that only the boxes for the 
        imval( 'myImage', box='2,3,14,15;30,31,42,43' )

        # Select the same two box regions but only channels 4 and 5
        imval( 'myImage', box='2,3,14,15;30,31,42,43', chan='4~5' )

        # Select all channels greater the 20 as well as channel 0.
        # Then the mean and standard deviation are printed
        # Note that the data returned is a Python numpy array which
        # has built in operations such as min, max, and means as
        # demonstrated here.
        results = imval( 'myImage', chans='>20;0' )
        imval_data=results['data']
        mask=results['mask']
        # holds the absolute coordinates of the associated pixels in imval_data
        coords = results['coords']
        print "Data max: ", imval_data.max(), "  mean is ", imval_data.mean()
        swapped_data=imval_data.swapaxes(0,2)
        swapped_mask=mask.swapaxes(0,2)
        print "Data values for 21st channel: \n", swapped_data[0]
        print "Mask values for 21st channel: \n", swapped_mask[0]

        """

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'imval.xml')

        casalog.origin('imval')
        if trec.has_key('imval') and casac.utils().verify(mytmp, trec['imval']) :
            result = task_imval.imval(imagename, region, box, chans, stokes)

        else :
          result = False
        return result
