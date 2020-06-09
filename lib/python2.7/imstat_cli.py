#
# This file was generated using xslt from its XML file
#
# Copyright 2014, Associated Universities Inc., Washington DC
#
import sys
import os
import datetime
#from casac import *
import casac
import string
import time
import inspect
import numpy
from casa_stack_manip import stack_frame_find
from odict import odict
from types import *
from task_imstat import imstat
class imstat_cli_:
    __name__ = "imstat"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (imstat_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'axes':None, 'region':None, 'box':None, 'chans':None, 'stokes':None, 'listit':None, 'verbose':None, 'mask':None, 'stretch':None, 'logfile':None, 'append':None, 'algorithm':None, 'fence':None, 'center':None, 'lside':None, 'zscore':None, 'maxiter':None, 'clmethod':None, 'niter':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, axes=None, region=None, box=None, chans=None, stokes=None, listit=None, verbose=None, mask=None, stretch=None, logfile=None, append=None, algorithm=None, fence=None, center=None, lside=None, zscore=None, maxiter=None, clmethod=None, niter=None, ):

        """Displays statistical information from an image or image region
        Arguments :
                imagename: Name of the input image
                   Default Value: 

                axes: List of axes to evaluate statistics over. Default is all axes.
                   Default Value: -1

                region: Region selection. Default is to use the full image.
                   Default Value: 

                box: Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.
                   Default Value: 

                chans: Channels to use. Default is to use all channels.
                   Default Value: 

                stokes: Stokes planes to use. Default is to use all Stokes planes.
                   Default Value: 

                listit: Print stats and bounding box to logger?
                   Default Value: True

                verbose: Print additional messages to logger?
                   Default Value: True

                mask: Mask to use. Default is none.
                   Default Value: 

                stretch: Stretch the mask if necessary and possible? 
                   Default Value: False

                logfile: Name of file to write fit results.
                   Default Value: 

                append: If logfile exists, append to it if True or overwrite it if False
                   Default Value: True

                algorithm: Algorithm to use. Supported values are "biweight", "chauvenet", "classic", "fit-half", and "hinges-fences". Minimum match is supported.
                   Default Value: classic

                fence: Fence value for hinges-fences. A negative value means use the entire data set (ie default to the "classic" algorithm). Ignored if algorithm is not "hinges-fences".
                   Default Value: -1

                center: Center to use for fit-half. Valid choices are "mean", "median", and "zero". Ignored if algorithm is not "fit-half".
                   Default Value: mean

                lside: For fit-half, use values <= center for real data if True? If False, use values >= center as real data. Ignored if algorithm is not "fit-half".
                   Default Value: True

                zscore: For chauvenet, this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet"s criterion. Ignored if algorithm is not "chauvenet".
                   Default Value: -1

                maxiter: For chauvenet, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if algorithm is not "chauvenet".
                   Default Value: -1

                clmethod: Method to use for calculating classical statistics. Supported methods are "auto", "tiled", and "framework". Ignored if algorithm is not "classic".
                   Default Value: auto

                niter: For biweight, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, do a fast, simple computation (see description). Ignored if the algorithm is not "biweight".
                   Default Value: 3

        Returns: void

        Example :


     Many parameters are determined from the specified region of an image.
     For this version, the region can be specified by a set of rectangular
     pixel coordinates, the channel ranges and the Stokes.

     For directed output, run as 
                    myoutput = imstat()
   

Keyword arguments:
imagename    Name of input image
             Default: none; Example: imagename='ngc5921_task.im'
axes         axes to compute statistics over. -1 => all axes.
region       Region selection. Default is
             to use the full image.
box          Rectangular region(s) to select in direction plane. See
             Default is to use the entire direction plane.
             Example: box='10,10,50,50'
             box = '10,10,30,30,35,35,50,50' (two boxes)
chans        Channels to use. Default is to use all channels.
             Example: chans='3~20'    
stokes       Stokes planes to use. Default is to
             use all Stokes planes.
             Example:stokes='I,Q'
listit       Print stats and bounding box to logger? 
verbose      Print additional messages to logger?
mask         Mask to use. Default is none.
stretch      Stretch the mask if necessary and possible? 
logfile      Name of file to write fit results.
append       If logfile exists, append to it (True) or overwrite it (False).
alogortihm   Algorithm to use to compute statistics. Supported values are "classic"
             and "hinges-fences" (minimum match supported.)
fence        Fence factor when algorithm = "hinges-fences". Negative values are not
             applicable and in these cases, the classic algorithm is used.
center       Center to use for "fit-half". Valid choices are "mean" (mean value of the
             selected pixels), "median" (median value of the selected pixels), and "zero"
             (0.0 is used as the center value). Ignored if algorithm is not "fit-half".
lside        For fit-half, use values <= center for the real data? If false, use
             values >= center as the real data. Ignored if algorithm is not "fit-half"
zscore       For chauvenet, this is the target maximum number of standard deviations data
             may have to be included. If negative, use Chauvenet's criterion. Ignored if
             algorithm is not "chauvenet".
maxiter      For chauvenet, this is the maximum number of iterations to attempt. Iterating
             will stop when either this limit is reached, or the zscore criterion is met.
             If negative, iterate until the zscore criterion is met. Ignored if algorithm is
             not "chauvenet".
clmethod     Method to use for calculating classical statistics. Supported methods are "auto",
             "tiled", and "framework". Ignored if algorithm is not "classic".
             
      General procedure:

         1.  Specify inputs, then

         2.  myoutput = imstat()
               or specify inputs directly in calling sequence to task
             myoutput = imstat(imagename='image.im', etc)

         3.  myoutput['KEYS'] will contain the result associated with any
               of the keys given below
        
        KEYS CURRENTLY AVAILABLE
        blc          - absolute PIXEL coordinate of the bottom left corner of 
                       the bounding box surrounding the selected region
        blcf         - Same as blc, but uses WORLD coordinates instead of pixels
        trc          - the absolute PIXEL coordinate of the top right corner 
                       of the bounding box surrounding the selected region
        trcf         - Same as trc, but uses WORLD coordinates instead of pixels
        flux         - the flux or flux density. See below for details.
        npts         - the number of unmasked points used
        max          - the maximum pixel value
        min          - minimum pixel value
        maxpos       - absolute PIXEL coordinate of maximum pixel value
        maxposf      - Same as maxpos, but uses WORLD coordinates instead of pixels
        minpos       - absolute pixel coordinate of minimum pixel value
        minposf      - Same as minpos, but uses WORLD coordinates instead of pixels
        sum          - the sum of the pixel values: $\sum I_i$
        sumsq        - the sum of the squares of the pixel values: $\sum I_i^2$
        mean         - the mean of pixel values: 
                       $\bar{I} = \sum I_i / n$
        sigma        - the standard deviation about the mean: 
                       $\sigma^2 = (\sum I_i - \bar{I})^2 / (n-1)$
        rms          - the root mean square: 
                       $\sqrt {\sum I_i^2 / n}$
        median       - the median pixel value
        medabsdevmed - the median of the absolute deviations from the 
                       median
        quartile     - the inner-quartile range. Find the points 
                       which are 25% largest and 75% largest (the median is 
                       50% largest).
    q1           - the first quartile.
    q3           - the third quartile

CURSOR AXES
The axes parameter allows one to set the cursor axes over which statistics 
are computed. For example, consider a 3-dimensional image for which axes=[0,2]. 
The statistics would be computed for each XZ (axes 0 and 2) plane in the
image.  One could then examine those statistics as a function of the Y
(axis 1) axis. 

Each statistic is stored in an array in its own field in the returned dictionary.
The dimensionality of these arrays is equal to the number of axes over which the
statistics were not evaluated (called the display axes). For example, if the input
image has four axes, and axes=[0], the output statistic arrays will have three dimensions.
If axes=[0, 1], the output statistic arrays will have two dimensions.

The shape of the output arrays when axes has a positive number of elements is based on
the region selection. If there is no region selection, the shape of the statistic arrays
is just the shape of the image along the display (non-cursor) axes. For example, if the
input image has dimensions of 300x400x4x80 (RA x Dec x Stokes x Freq) and axes=[0, 1],
in the absence of a region selection, the shape of the output statistic arrays will be
4x80. If there is a region selection, the shape of the output statistic arrays will be
determined by the number of planes along the display axes chosen in the region selection.
For example, continuing with our example, if axes=[0,1], chans="5~15;30~70", and
stokes="IV", the output statistic arrays will have shapes of 2x52. Only the selected
planes will be displayed in the logger output if verbose=True.

In the case where the image has a pixel mask, and/or the mask parameter is specified,
and because of this specification a plane is entirely masked, this element is included in
the statistic arrays (usually with a value of 0). It is not included in the logger output
if verbose=True. One can exclude such elements from computations on the output arrays by
using the numpy.extract() method. For example, to compute the minimum rms value, not
including any fully masked planes, one could use

stats = imstat(...)
rmsmin = numpy.min(numpy.extract(stats['npts']>0, stats['rms']))

Thus in the computation of rmsmin, only the rms elements are considered which have
associated values of npts that are not zero.

ALGORITHMS

Several types of statistical algorithms are supported:

* classic: This is the familiar algorithm, in which all unmasked pixels are used. One may choose
  one of two methods, which vary only by performance, for computing classic statistics, via the
  clmethod parameter. The "tiled" method is the old method and is fastest in cases where there are
  a large number of individual sets of statistics to be computed and a small number of data points
  per set. This can occur when one sets the axes parameter, which causes several individual sets of
  statistics to be computed. The "framework" method uses the new statistics framework to compute
  statistics. This method is fastest in the regime where one has a small number of individual sets
  of statistics to calculate, and each set has a large number of points. For example, this method
  is fastest when computing statistics over an entire image in one go (no axes specified). A third
  option, "auto", chooses which method to use by predicting which be faster based on the number of
  pixels in the image and the choice of the axes parameter.
  
* fit-half: This algorithm calculates statistics on a dataset created from real and virtual pixel values.
  The real values are determined by the input parameters center and lside. The parameter center
  tells the algorithm where the center value of the combined real+virtual dataset should be. Options
  are the mean or the median of the input image's pixel values, or at zero. The lside parameter tells
  the algorithm on which side of this center the real pixel values are located. True indicates that
  the real pixel values to be used are <= center. False indicates the real pixel values to be used
  are >= center. The virtual part of the dataset is then created by reflecting all the real values
  through the center value, to create a perfectly symmetric dataset composed of a real and a virtual
  component. Statistics are then calculated on this resultant dataset. These two parameters are
  ignored if algorithm is not "fit-half". Because the maximum value is virtual if lside is True and the
  minimum value is virtual if lside is False, the value of the maximum position (if lside=True) or
  minimum position (if lside=False) is not reported in the returned record.
  
* hinges-fences: This algorithm calculates statistics by including data in a range
  between Q1 - f*D and Q3 + f*D, inclusive, where Q1 is the first quartile of the distribution
  of unmasked data, subject to any specified pixel ranges, Q3 is the third quartile, D = Q3 - Q1
  (the inner quartile range), and f is the user-specified fence factor. Negative values of f
  indicate that the full distribution is to be used (ie, the classic algorithm is used). Sufficiently
  large values of f will also be equivalent to using the classic algorithm. For f = 0, only data
  in the inner quartile range is used for computing statistics. The value of fence is silently
  ignored if algorithm is not "hinges-fences".

* chauvenet: The idea behind this algorithm is to eliminate outliers based on a maximum z-score value.
  A z-score is the number of standard deviations a point is from the mean of a distribution. This
  method thus is meant to be used for (nearly) normal distributions. In general, this is an iterative
  process, with successive iterations discarding additional outliers as the remaining points become
  closer to forming a normal distribution. Iterating stops when no additional points lie beyond the
  specified zscore value, or, if zscore is negative, when Chauvenet's criterion is met (see below).
  The parameter maxiter can be set to a non-negative value to prematurely abort this iterative
  process. When verbose=T, the "N iter" column in the table that is logged represents the number
  of iterations that were executed.
  
  Chauvenet's criterion allows the target z-score to decrease as the number of points in the
  distribution decreases on subsequent iterations. Essentially, the criterion is that the probability
  of having one point in a normal distribution at a maximum z-score of z_max must be at least 0.5.
  z_max is therefore a function of (only) the number of points in the distrbution and is given by
  
  npts = 0.5/erfc(z_max/sqrt(2))
  
  where erfc() is the complementary error function. As iterating proceeds, the number of remaining
  points decreases as outliers are discarded, and so z_max likewise decreases. Convergence occurs when
  all remaining points fall within a z-score of z_max. Below is an illustrative table of z_max values
  and their corresponding npts values. For example, it is likely that there will be a 5-sigma "noise
  bump" in a perfectly noisy image with one million independent elements.
  
  z_max    npts
  1.0                1
  1.5                3
  2.0               10
  2.5               40
  3.0              185
  3.5            1,074
  4.0            7,893
  4.5           73,579
  5.0          872,138
  5.5       13,165,126
  6.0      253,398,672
  6.5    6,225,098,696
  7.0  195,341,107,722

NOTES ON FLUX DENSITIES AND FLUXES

Fluxes and flux densities are not computed if any of the following conditions is met:

1. The image does not have a direction coordinate
2. The image does not have a intensity-like brightness unit. Examples of such units
   are Jy/beam (in which case the image must also have a beam) and K.
3. There are no direction axes in the cursor axes that are used.
4. If the (specified region of the) image has a non-degenerate spectral axis,
   and the image has a tablular spectral axis (axis with varying increments)
5. Any axis that is not a direction nor a spectral axis that is included in the cursor
   axes is not degenerate within in specified region

Note that condition 4 may be removed in the future.

In cases where none of the above conditions is met, the flux density(ies) (intensities
integrated over direction planes) will be computed if any of the following conditions
are met:

1. The image has no spectral coordinate
2. The cursor axes do not include the spectral axis
3. The spectral axis in the chosen region is degenerate

In the case where there is a nondegenerate spectral axis that is included in the cursor
axes, the flux (flux density integrated over spectral planes) will be computed. In this
case, the spectral portion of the flux unit will be the velocity unit of the spectral
coordinate if it has one (eg, if the brightness unit is Jy/beam and the velocity unit is
km/s, the flux will have units of Jy.km/s). If not, the spectral portion of the flux unit
will be the frequency unit of the spectral axis (eg, if the brightness unit is K and the
frequency unit is Hz, the resulting flux unit will be K.arcsec2.Hz). 

In both cases of flux density or flux being computed, the resulting numerical value is
assigned to the "flux" key in the output dictionary.

ADDITIONAL EXAMPLES

        # Selected two box region
        # box 1, bottom-left coord is 2,3 and top-right coord is 14,15
        # box 2, bottom-left coord is 30,31 and top-right coord is 42,43
        imstat( 'myImage', box='2,3,14,15;30,31,42,43' )

        # Select the same two box regions but only channels 4 and 5
        imstat( 'myImage', box='2,3,14,15;30,31,42,43', chan='4~5' )

        # Select all channels greater the 20 as well as channel 0.
        # Then the mean and standard deviation are printed
        results = imstat( 'myImage', chans='>20;0' )
        print "Mean is: ", results['mean'], "  s.d. ", results['sigma']

        # Find statistical information for the Q stokes value only
        # then the I stokes values only, and printing out the statistical
        # values that we are interested in.
        s1 = imstat( 'myimage', stokes='Q' )
        s2 = imstat( 'myimage', stokes='I' )
        print "       |  MIN  |   MAX  | MEAN"
        print "  Q    | ",s1['min'][0],"  |  ",s1['max'][0],"  |  ",,"  |  ",s1['mean'][0]
        print "  I    | ",s2['min'][0],"  |  ",s2['max'][0],"  |  ",,"  |  ",s2['mean'][0]

# evaluate statistics for each spectral plane in an ra x dec x frequency image
myim = "noisy.im"
ia.fromshape(myim, [20,30,40])
# give pixels non-zero values
ia.addnoise()
ia.done()
# These are the display axes, the calculation of statistics occurs
# for each (hyper)plane along axes not listed in the axes parameter,
# in this case axis 2 (the frequency axis)
# display the rms for each frequency plane (your mileage will vary with
# the values).
stats = imstat(imagename=myim, axes=[0,1])
 stats["rms"]
  Out[10]: 
array([ 0.99576014,  1.03813124,  0.97749186,  0.97587883,  1.04189885,
        1.03784776,  1.03371549,  1.03153074,  1.00841606,  0.947155  ,
        0.97335404,  0.94389403,  1.0010221 ,  0.97151822,  1.03942156,
        1.01158476,  0.96957082,  1.04212773,  1.00589049,  0.98696715,
        1.00451481,  1.02307892,  1.03102005,  0.97334671,  0.95209879,
        1.02088714,  0.96999902,  0.98661619,  1.01039267,  0.96842754,
        0.99464947,  1.01536798,  1.02466023,  0.96956468,  0.98090756,
        0.9835844 ,  0.95698935,  1.05487967,  0.99846411,  0.99634868])



        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'imstat'
        self.__globals__['taskname'] = 'imstat'
        ###
        self.__globals__['update_params'](func=self.__globals__['taskname'],printtext=False,ipython_globals=self.__globals__)
        ###
        ###
        #Handle globals or user over-ride of arguments
        #
        if type(self.__call__.func_defaults) is NoneType:
            function_signature_defaults={}
        else:
            function_signature_defaults=dict(zip(self.__call__.func_code.co_varnames[1:],self.__call__.func_defaults))
        useLocalDefaults = False

        for item in function_signature_defaults.iteritems():
                key,val = item
                keyVal = eval(key)
                if (keyVal == None):
                        #user hasn't set it - use global/default
                        pass
                else:
                        #user has set it - use over-ride
                        if (key != 'self') :
                           useLocalDefaults = True

        myparams = {}
        if useLocalDefaults :
           for item in function_signature_defaults.iteritems():
               key,val = item
               keyVal = eval(key)
               exec('myparams[key] = keyVal')
               self.parameters[key] = keyVal
               if (keyVal == None):
                   exec('myparams[key] = '+ key + ' = self.itsdefault(key)')
                   keyVal = eval(key)
                   if(type(keyVal) == dict) :
                      if len(keyVal) > 0 :
                         exec('myparams[key] = ' + key + ' = keyVal[len(keyVal)-1][\'value\']')
                      else :
                         exec('myparams[key] = ' + key + ' = {}')

        else :
            print ''

            myparams['imagename'] = imagename = self.parameters['imagename']
            myparams['axes'] = axes = self.parameters['axes']
            myparams['region'] = region = self.parameters['region']
            myparams['box'] = box = self.parameters['box']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['listit'] = listit = self.parameters['listit']
            myparams['verbose'] = verbose = self.parameters['verbose']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['stretch'] = stretch = self.parameters['stretch']
            myparams['logfile'] = logfile = self.parameters['logfile']
            myparams['append'] = append = self.parameters['append']
            myparams['algorithm'] = algorithm = self.parameters['algorithm']
            myparams['fence'] = fence = self.parameters['fence']
            myparams['center'] = center = self.parameters['center']
            myparams['lside'] = lside = self.parameters['lside']
            myparams['zscore'] = zscore = self.parameters['zscore']
            myparams['maxiter'] = maxiter = self.parameters['maxiter']
            myparams['clmethod'] = clmethod = self.parameters['clmethod']
            myparams['niter'] = niter = self.parameters['niter']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['axes'] = axes
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['listit'] = listit
        mytmp['verbose'] = verbose
        mytmp['mask'] = mask
        mytmp['stretch'] = stretch
        mytmp['logfile'] = logfile
        mytmp['append'] = append
        mytmp['algorithm'] = algorithm
        mytmp['fence'] = fence
        mytmp['center'] = center
        mytmp['lside'] = lside
        mytmp['zscore'] = zscore
        mytmp['maxiter'] = maxiter
        mytmp['clmethod'] = clmethod
        mytmp['niter'] = niter
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'imstat.xml')

        casalog.origin('imstat')
        try :
          #if not trec.has_key('imstat') or not casac.casac.utils().verify(mytmp, trec['imstat']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['imstat'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('imstat', 'imstat.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'imstat'
          spaces = ' '*(18-len(tname))
          casalog.post('\n##########################################'+
                       '\n##### Begin Task: ' + tname + spaces + ' #####')
          # Don't do telemetry from MPI servers (CASR-329)
          if do_full_logging and casa['state']['telemetry-enabled']:
              #casalog.poststat('Begin Task: ' + tname)
              task_starttime = str(datetime.datetime.now())
          if type(self.__call__.func_defaults) is NoneType:
              casalog.post(scriptstr[0]+'\n', 'INFO')
          else:
              casalog.post(scriptstr[1][1:]+'\n', 'INFO')

          # Effective call to the task as defined in gcwrap/python/scripts/task_*
          result = imstat(imagename, axes, region, box, chans, stokes, listit, verbose, mask, stretch, logfile, append, algorithm, fence, center, lside, zscore, maxiter, clmethod, niter)

          if do_full_logging and casa['state']['telemetry-enabled']:
              task_endtime = str(datetime.datetime.now())
              casalog.poststat( 'Task ' + tname + ' complete. Start time: ' + task_starttime + ' End time: ' + task_endtime )
          casalog.post('##### End Task: ' + tname + '  ' + spaces + ' #####'+
                       '\n##########################################')

        except Exception, instance:
          if(self.__globals__.has_key('__rethrow_casa_exceptions') and self.__globals__['__rethrow_casa_exceptions']) :
             raise
          else :
             #print '**** Error **** ',instance
             tname = 'imstat'
             casalog.post('An error occurred running task '+tname+'.', 'ERROR')
             pass
        casalog.origin('')

        return result
#
#
#
#    def paramgui(self, useGlobals=True, ipython_globals=None):
#        """
#        Opens a parameter GUI for this task.  If useGlobals is true, then any relevant global parameter settings are used.
#        """
#        import paramgui
#        if not hasattr(self, "__globals__") or self.__globals__ == None :
#           self.__globals__=stack_frame_find( )
#
#        if useGlobals:
#            if ipython_globals == None:
#                myf=self.__globals__
#            else:
#                myf=ipython_globals
#
#            paramgui.setGlobals(myf)
#        else:
#            paramgui.setGlobals({})
#
#        paramgui.runTask('imstat', myf['_ip'])
#        paramgui.setGlobals({})
#
#
#
#
    def defaults(self, param=None, ipython_globals=None, paramvalue=None, subparam=None):
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        if ipython_globals == None:
            myf=self.__globals__
        else:
            myf=ipython_globals

        a = odict()
        a['imagename']  = ''
        a['axes']  = -1
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['listit']  = True
        a['verbose']  = True
        a['mask']  = ''
        a['logfile']  = ''
        a['algorithm']  = 'classic'

        a['mask'] = {
                    0:odict([{'notvalue':''}, {'stretch':False}])}
        a['logfile'] = {
                    0:odict([{'notvalue':''}, {'append':True}])}
        a['algorithm'] = {
                    0:odict([{'value':'classic'}, {'clmethod':'auto'}]), 
                    1:odict([{'value':'hinges-fences'}, {'fence':-1}]), 
                    2:odict([{'value':'fit-half'}, {'center':'mean'}, {'lside':True}]), 
                    3:odict([{'value':'chauvenet'}, {'zscore':-1}, {'maxiter':-1}]), 
                    4:odict([{'value':'biweight'}, {'niter':3}])}

### This function sets the default values but also will return the list of
### parameters or the default value of a given parameter
        if(param == None):
                myf['__set_default_parameters'](a)
        elif(param == 'paramkeys'):
                return a.keys()
        else:
            if(paramvalue==None and subparam==None):
               if(a.has_key(param)):
                  return a[param]
               else:
                  return self.itsdefault(param)
            else:
               retval=a[param]
               if(type(a[param])==dict):
                  for k in range(len(a[param])):
                     valornotval='value'
                     if(a[param][k].has_key('notvalue')):
                        valornotval='notvalue'
                     if((a[param][k][valornotval])==paramvalue):
                        retval=a[param][k].copy()
                        retval.pop(valornotval)
                        if(subparam != None):
                           if(retval.has_key(subparam)):
                              retval=retval[subparam]
                           else:
                              retval=self.itsdefault(subparam)
                     else:
                        retval=self.itsdefault(subparam)
               return retval


#
#
    def check_params(self, param=None, value=None, ipython_globals=None):
      if ipython_globals == None:
          myf=self.__globals__
      else:
          myf=ipython_globals
#      print 'param:', param, 'value:', value
      try :
         if str(type(value)) != "<type 'instance'>" :
            value0 = value
            value = myf['cu'].expandparam(param, value)
            matchtype = False
            if(type(value) == numpy.ndarray):
               if(type(value) == type(value0)):
                  myf[param] = value.tolist()
               else:
                  #print 'value:', value, 'value0:', value0
                  #print 'type(value):', type(value), 'type(value0):', type(value0)
                  myf[param] = value0
                  if type(value0) != list :
                     matchtype = True
            else :
               myf[param] = value
            value = myf['cu'].verifyparam({param:value})
            if matchtype:
               value = False
      except Exception, instance:
         #ignore the exception and just return it unchecked
         myf[param] = value
      return value
#
#
    def description(self, key='imstat', subkey=None):
        desc={'imstat': 'Displays statistical information from an image or image region',
               'imagename': 'Name of the input image',
               'axes': 'List of axes to evaluate statistics over. Default is all axes.',
               'region': 'Region selection. Default is to use the full image.',
               'box': 'Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.',
               'chans': 'Channels to use. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Default is to use all Stokes planes.',
               'listit': 'Print stats and bounding box to logger?',
               'verbose': 'Print additional messages to logger?',
               'mask': 'Mask to use. Default is none.',
               'stretch': 'Stretch the mask if necessary and possible? ',
               'logfile': 'Name of file to write fit results.',
               'append': 'If logfile exists, append to it if True or overwrite it if False',
               'algorithm': 'Algorithm to use. Supported values are "biweight", "chauvenet", "classic", "fit-half", and "hinges-fences". Minimum match is supported.',
               'fence': 'Fence value for hinges-fences. A negative value means use the entire data set (ie default to the "classic" algorithm). Ignored if algorithm is not "hinges-fences".',
               'center': 'Center to use for fit-half. Valid choices are "mean", "median", and "zero". Ignored if algorithm is not "fit-half".',
               'lside': 'For fit-half, use values <= center for real data if True? If False, use values >= center as real data. Ignored if algorithm is not "fit-half".',
               'zscore': 'For chauvenet, this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet"s criterion. Ignored if algorithm is not "chauvenet".',
               'maxiter': 'For chauvenet, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if algorithm is not "chauvenet".',
               'clmethod': 'Method to use for calculating classical statistics. Supported methods are "auto", "tiled", and "framework". Ignored if algorithm is not "classic".',
               'niter': 'For biweight, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, do a fast, simple computation (see description). Ignored if the algorithm is not "biweight".',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['axes']  = -1
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['listit']  = True
        a['verbose']  = True
        a['mask']  = ''
        a['stretch']  = False
        a['logfile']  = ''
        a['append']  = True
        a['algorithm']  = 'classic'
        a['fence']  = -1
        a['center']  = 'mean'
        a['lside']  = True
        a['zscore']  = -1
        a['maxiter']  = -1
        a['clmethod']  = 'auto'
        a['niter']  = 3

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if self.parameters['logfile']  != '':
            a['append'] = True

        if self.parameters['algorithm']  == 'classic':
            a['clmethod'] = 'auto'

        if self.parameters['algorithm']  == 'hinges-fences':
            a['fence'] = -1

        if self.parameters['algorithm']  == 'fit-half':
            a['center'] = 'mean'
            a['lside'] = True

        if self.parameters['algorithm']  == 'chauvenet':
            a['zscore'] = -1
            a['maxiter'] = -1

        if self.parameters['algorithm']  == 'biweight':
            a['niter'] = 3

        if a.has_key(paramname) :
              return a[paramname]
imstat_cli = imstat_cli_()
