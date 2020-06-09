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
from task_imdev import imdev
class imdev_cli_:
    __name__ = "imdev"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (imdev_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'outfile':None, 'region':None, 'box':None, 'chans':None, 'stokes':None, 'mask':None, 'overwrite':None, 'stretch':None, 'grid':None, 'anchor':None, 'xlength':None, 'ylength':None, 'interp':None, 'stattype':None, 'statalg':None, 'zscore':None, 'maxiter':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, outfile=None, region=None, box=None, chans=None, stokes=None, mask=None, overwrite=None, stretch=None, grid=None, anchor=None, xlength=None, ylength=None, interp=None, stattype=None, statalg=None, zscore=None, maxiter=None, ):

        """Create an image that can represent the statistical deviations of the input image.
        Arguments :
                imagename: Input image name
                   Default Value: 

                outfile: Output image file name. If left blank (the default), no image is written but a new image tool referencing the collapsed image is returned.
                   Default Value: 

                region: Region selection. Default is to use the full image.
                   Default Value: 

                box: Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.
                   Default Value: 

                chans: Channels to use. Default is to use all channels.
                   Default Value: 

                stokes: Stokes planes to use. Default is to use all Stokes planes.
                   Default Value: 

                mask: Mask to use. Default setting is none. 
                   Default Value: 

                overwrite: Overwrite (unprompted) pre-existing output file? Ignored if "outfile" is left blank. 
                   Default Value: False

                stretch: Stretch the mask if necessary and possible? Default value is False.
                   Default Value: False

                grid: x,y grid spacing. Array of exactly two positive integers.
                   Default Value: 
            11
        

                anchor: x,y anchor pixel location. Either "ref" to use the image reference pixel, or an array of exactly two integers.
                   Default Value: ref

                xlength: Either x coordinate length of box, or diameter of circle. Circle is used if ylength is empty string.
                   Default Value: 1pix

                ylength: y coordinate length of box. Use a circle if ylength is empty string.
                   Default Value: 1pix

                interp: Interpolation algorithm to use. One of "nearest", "linear", "cubic", or "lanczos". Minimum match supported.
                   Default Value: cubic

                stattype: Statistic to compute. See full description for supported statistics.
                   Default Value: sigma

                statalg: Statistics computation algorithm to use. Supported values are "chauvenet" and "classic", Minimum match is supported.
                   Default Value: classic

                zscore: For chauvenet, this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet"s criterion. Ignored if algorithm is not "chauvenet".
                   Default Value: -1

                maxiter: For chauvenet, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if algortihm is not "chauvenet".
                   Default Value: -1

        Returns: bool

        Example :

    This application creates an image that reflects the statistics of the input image. The output image has
    the same dimensions and coordinate system as the (selected region in) input image. The grid parameter
    describes how many pixels apart "grid" pixels are. Statistics are computed around each grid pixel. Grid
    pixels are limited to the direction plane only; independent statistics are computed for each direction plane
    (ie at each frequency/stokes pixel should the input image happen to have such additional axes). Using the
    xlength and ylength parameters, one may specify either a rectangular or circular region around each grid
    point that defines which surrounding pixels are used in the statistic computation for individual grid points.
    If the ylength parameter is the empty string, then a circle of diameter provided by xlength centered on
    the grid point is used. If ylength is not empty, then a rectangular box of dimensions xlength x ylength centered
    on the grid pixel is used. These two parameters may be specified in pixels, using either numerical values or
    valid quantities with "pix" as the unit (eg "4pix"). Otherwise, they must be specified as valid angular
    quantities, with recognized units (eg "4arcsec"). As with other region selections in CASA, full pixels are
    included in the computation even if the specified region includes only a fraction of that pixel. BEWARE OF
    MACHINE PRECISION ISSUES, because you may get a smaller number of pixels included in a region than you
    expect if you specify, eg, an integer number of pixels. In such cases, you probably want to specify that
    number plus a small epsilon value (eg "2.0001pix" rather than "2pix") to mitigate machine precision issues
    when computing region extents.

    The output image is formed by putting the statistics calculated at each grid point at the corresponding
    grid point in the output image. Interpolation of these output values is then used to compute values at
    non-grid-point pixels. The user may specify which interpolation algorithm to use for this computation
    using the interp parameter.
    
    The input image pixel mask is copied to the output image. If interpolation is performed, output pixels are
    masked where the interpolation fails.

    ANCHORING THE GRID

    The user may choose at which pixel to "anchor" the grid. For example, if one specifies grid=[4,4] and
    anchor=[0,0], grid points will be located at pixels [0,0], [0,4], [0,8] ... [4,0], [4,4], etc. This
    is exactly the same grid that would be produced if the user specified anchor=[4,4] or anchor=[20,44].
    If the user specifies anchor=[1, 2] and grid=[4,4], then the grid points will be at pixels [1,2], [5,2],
    [9,2]... [5,2], [5,6], etc. and the resulting grid is the same as it would be if the user specified eg
    anchor=[9,10] or anchor=[21, 18]. The value "ref", which is the default, indicates that the reference
    pixel of the input image should be used to anchor the grid. The x and y values of this pixel will be
    rounded to the nearest integer if necessary.

    SUPPORTED STATISTICS AND STATISTICS ALGORITHMS

    One may specify which statistic should be represented using the stattype parameter. The following values
    are recognized (minimum match supported):

    iqr                   inner quartile range (q3 - q1)
    max                   maximum
    mean                  mean
    medabsdevmed, madm    median absolute deviation from the median
    median                median
    min                   minimum
    npts                  number of points
    q1                    first quartile
    q3                    third quartile
    rms                   rms
    sigma, std            standard deviation
    sumsq                 sum of squares
    sum                   sum
    var                   variance
    xmadm                 median absolute deviation from the median multipied by x, where x is the reciprocal of Phi^-1(3/4),
                          where Phi^-1 is the reciprocal of the quantile function. Numerically, x = 1.482602218505602. See, eg,
                          https://en.wikipedia.org/wiki/Median_absolute_deviation#Relation_to_standard_deviation

    Using the statalg parameter, one may also select whether to use the Classical or Chauvenet/ZScore statistics algorithm to
    compute the desired statistic (see the help for ia.statistics() or imstat for a full description of these algorithms).

    # compute standard deviations in circles of diameter 10arcsec around
    # grid pixels spaced every 4 x 5 pixels and anchored at pixel [30, 40],
    # and use linear interpolation to compute values at non-grid-pixels
    imdev("my.im", "sigma.im", grid=[4, 5], anchor=[30, 40], xlength="10arcsec", stattype="sigma", interp="lin", statalg="cl")

    # compute median of the absolute deviations from the median values using
    # the z-score/Chauvenet algorithm, by fixing the maximum z-score to determine outliers to 5.
    # Use cubic interpolation to compute values for non-grid-point pixels. Use a rectangular region
    # of dimensions 5arcsec x 20arcsec centered on each grid point as the region in which to include
    # pixels for the computation of stats for that grid point.
    imdev("my.im", "madm.im", grid=[4, 5], anchor=[30, 40], xlength="5arcsec", ylength="20arcsec, stattype="madm", interp="cub", statalg="ch", zscore=5)

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'imdev'
        self.__globals__['taskname'] = 'imdev'
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
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['region'] = region = self.parameters['region']
            myparams['box'] = box = self.parameters['box']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['stretch'] = stretch = self.parameters['stretch']
            myparams['grid'] = grid = self.parameters['grid']
            myparams['anchor'] = anchor = self.parameters['anchor']
            myparams['xlength'] = xlength = self.parameters['xlength']
            myparams['ylength'] = ylength = self.parameters['ylength']
            myparams['interp'] = interp = self.parameters['interp']
            myparams['stattype'] = stattype = self.parameters['stattype']
            myparams['statalg'] = statalg = self.parameters['statalg']
            myparams['zscore'] = zscore = self.parameters['zscore']
            myparams['maxiter'] = maxiter = self.parameters['maxiter']

        if type(grid)==int: grid=[grid]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['overwrite'] = overwrite
        mytmp['stretch'] = stretch
        mytmp['grid'] = grid
        mytmp['anchor'] = anchor
        mytmp['xlength'] = xlength
        mytmp['ylength'] = ylength
        mytmp['interp'] = interp
        mytmp['stattype'] = stattype
        mytmp['statalg'] = statalg
        mytmp['zscore'] = zscore
        mytmp['maxiter'] = maxiter
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'imdev.xml')

        casalog.origin('imdev')
        try :
          #if not trec.has_key('imdev') or not casac.casac.utils().verify(mytmp, trec['imdev']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['imdev'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('imdev', 'imdev.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'imdev'
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
          result = imdev(imagename, outfile, region, box, chans, stokes, mask, overwrite, stretch, grid, anchor, xlength, ylength, interp, stattype, statalg, zscore, maxiter)

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
             tname = 'imdev'
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
#        paramgui.runTask('imdev', myf['_ip'])
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
        a['outfile']  = ''
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['overwrite']  = False
        a['grid']  = [1, 1]
        a['anchor']  = 'ref'
        a['xlength']  = '1pix'
        a['ylength']  = '1pix'
        a['interp']  = 'cubic'
        a['stattype']  = 'sigma'
        a['statalg']  = 'classic'

        a['mask'] = {
                    0:odict([{'notvalue':''}, {'stretch':False}])}
        a['statalg'] = {
                    0:{'value':'classic'}, 
                    1:odict([{'value':'chauvenet'}, {'zscore':-1}, {'maxiter':-1}])}

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
    def description(self, key='imdev', subkey=None):
        desc={'imdev': 'Create an image that can represent the statistical deviations of the input image.',
               'imagename': 'Input image name',
               'outfile': 'Output image file name. If left blank (the default), no image is written but a new image tool referencing the collapsed image is returned.',
               'region': 'Region selection. Default is to use the full image.',
               'box': 'Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.',
               'chans': 'Channels to use. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Default is to use all Stokes planes.',
               'mask': 'Mask to use. Default setting is none. ',
               'overwrite': 'Overwrite (unprompted) pre-existing output file? Ignored if "outfile" is left blank. ',
               'stretch': 'Stretch the mask if necessary and possible? Default value is False.',
               'grid': 'x,y grid spacing. Array of exactly two positive integers.',
               'anchor': 'x,y anchor pixel location. Either "ref" to use the image reference pixel, or an array of exactly two integers.',
               'xlength': 'Either x coordinate length of box, or diameter of circle. Circle is used if ylength is empty string.',
               'ylength': 'y coordinate length of box. Use a circle if ylength is empty string.',
               'interp': 'Interpolation algorithm to use. One of "nearest", "linear", "cubic", or "lanczos". Minimum match supported.',
               'stattype': 'Statistic to compute. See full description for supported statistics.',
               'statalg': 'Statistics computation algorithm to use. Supported values are "chauvenet" and "classic", Minimum match is supported.',
               'zscore': 'For chauvenet, this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet"s criterion. Ignored if algorithm is not "chauvenet".',
               'maxiter': 'For chauvenet, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if algortihm is not "chauvenet".',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['outfile']  = ''
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['overwrite']  = False
        a['stretch']  = False
        a['grid']  = [1, 1]
        a['anchor']  = 'ref'
        a['xlength']  = '1pix'
        a['ylength']  = '1pix'
        a['interp']  = 'cubic'
        a['stattype']  = 'sigma'
        a['statalg']  = 'classic'
        a['zscore']  = -1
        a['maxiter']  = -1

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if self.parameters['statalg']  == 'chauvenet':
            a['zscore'] = -1
            a['maxiter'] = -1

        if a.has_key(paramname) :
              return a[paramname]
imdev_cli = imdev_cli_()
