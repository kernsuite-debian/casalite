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
from task_immath import immath
class immath_cli_:
    __name__ = "immath"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (immath_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'mode':None, 'outfile':None, 'expr':None, 'varnames':None, 'sigma':None, 'polithresh':None, 'mask':None, 'region':None, 'box':None, 'chans':None, 'stokes':None, 'stretch':None, 'imagemd':None, 'prec':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, mode=None, outfile=None, expr=None, varnames=None, sigma=None, polithresh=None, mask=None, region=None, box=None, chans=None, stokes=None, stretch=None, imagemd=None, prec=None, ):

        """Perform math operations on images

        Detailed Description:
 math on images

        Arguments :
                imagename: a list of input images 
                   Default Value: 

                mode: mode for math operation (evalexpr, spix, pola, poli, lpoli, tpoli)
                   Default Value: evalexpr
                   Allowed Values:
                                evalexpr
                                spix
                                pola
                                poli
                                lpoli
                                tpoli

                outfile: File where the output is saved
                   Default Value: immath_results.im

                expr: Mathematical expression using images
                   Default Value: IM0

                varnames: a list of variable names to use with the image files
                   Default Value: 

                sigma: standard deviation of noise for debiasing
                   Default Value: 0.0mJy/beam

                polithresh: Threshold in linear polarization intensity image below which to mask pixels.
                   Default Value: 

                mask: Mask to use. Default is none.
                   Default Value: 

                region: Region selection. Default is to use the full image.
                   Default Value: 

                box: Rectangular region to select in direction plane. Default is to use the entire direction plane.
                   Default Value: 

                chans: Channels to use. Default is to use all channels.
                   Default Value: 

                stokes: Stokes planes to use. Default is to use all Stokes planes.
                   Default Value: 

                stretch: Stretch the mask if necessary and possible? See help stretch.par 
                   Default Value: False

                imagemd: An image name from which metadata should be copied. The input can be either an image listed under imagename or any other image on disk. Leaving this parameter unset may copy header metadata from any of the input images, which one is not guaranteed. 
                   Default Value: 

                prec: Precision for the output image pixels if mode="evalexpr" or "spix". "float" or "double" (minimum match supported)
                   Default Value: float

        Returns: bool

        Example :


    This task evaluates mathematical expressions involving existing
    image files. The results of the calculations are stored in the 
    designated output file.  Options are available to specify mathematical 
    expression directly or pre-defined expression for calculation of 
    spectral index image, and polarization intensity and position angle 
    images are available. The image file names imbedded in the expression or
    specified in the imagename parameter for the pre-defined calculations may
    be CASA images or FITS images.


    NOTE: Index values start at 0 Use the imhead task to see the range of
          index values for each axes.
    

    Keyword arguments:
    imagename  input image name(s)
               Default: none;
               Examples: mode='evalexpr'; imagename=['image1.im', 'image2.im' ]
               The text 'IM0' is replaced by 'image1.im' in the
               expression and 'IM1' is repalced with 'image2.im'
               mode='spix'; imagename=['image1.im','image2.im'] will calculate 
               an image of log(S1/S2)/log(f1/f2), where S1 and S2 are fluxes and 
               f1 and f2 are frequencies
               mode='pola'; imagename='multistokes.im' (where that image contains both Q and U
               stokes planes) or imagename=['imageQ.im','imageU.im'] will calculate 
               an image of polarization angle distribution, where imageQ.im and 
               imageU.im are Stokes Q and U images, respectively. Calculate 0.5*arctan(U/Q).
               mode='poli'; imagename=['imageQ.im','imageU.im','imageV.im'] will calculate
               total polarization intensity image, where imageQ.im, imageU.im, imageV.im
               are Stokes Q, U, and V images, respectively. Alternatively, with
               imagename = ['imageQ.im','imageU.im'] the linear polarization intensity
               image will be calculated. In the case where imagename is a single multi-stokes
               image, the total polarization image will be calculated if all of the Q, U, and
               V stokes planes are present, and the linear polarization intensity image will
               be calculated if the Q and U (but not V) planes are present. 

    mode       mode for mathematical operation
               Default: evalexpr
               Options: 'evalexpr' : evalulate a mathematical expression defined in 'expr' 
                        'spix' : spectalindex image 
                        'pola' : polarization position angle image 
                        'poli' : polarization intesity image 
              >>> mode expandable parameters
              sigma       (for mode='poli') standard deviation of noise of Stokes images with unit such as
                          Jy/beam to correct for bias 
                          Default: '0.0Jy/beam' (= no debiasing)
              polithresh  (for mode='pola') Quantity (eg '30uJy/beam') describing the linear (not total;
                          the stokes V contribution is not included) polarization threshold. A mask ('mask0')
                          is written to the output image and is False for all corresponding linear polarization
                          values below this threshold. This parameter overrides the mask input parameter
                          (below). Default ('') means use the value given in mask, or no masking if that
                          value is empty as well.
              expr        (for mode='evalexpr') A LEL expression with images.
                          Image file names are specified in the imagenames paramter, and
                          the variables IM0, IM1, ... (or optionally via the varnames parameter, see below)
                          are used to represent these files
                          in the expression. Explicit notations of file names in the 
                          expression are also supported, in which cases the file names must
                          be enclosed in double quotes (") and imagename is ignored.
                          Examples:
                          Make an image that is image1.im - image2.im
                          expr=' (IM0 - IM1 )'
                          or with an explicit notation, 
                          expr='("image1.im" - "image2.im")'
                          Clip an image below a value (0.5 in this case)
                          expr = ' iif( IM0 >=0.5, IM0, 0.0) '
                          Note: iif (a, b, c)   a is the boolean expression
                                                b is the value if true
                                                c is the value if false
                          Take the rms value of two images
                          expr = ' sqrt(IM0 * IM0 + IM1 * IM1) '
                          Build an image pixel by pixel from the minimum of (image2.im, 2*image1.im)
                          expr='min(IM1,2*max(IM0))'
               varnames   For mode="evalexpr". Instead of the default variable names IM0, IM1, ..., use
                          the names in this array to represent the input images.
    outfile    The output image. Overwriting an existing outfile is not permitted.
               Default: immath_results.im;  Example: outfile='results.im'
    mask       Mask to use. Default is none. Also see polithresh.
    stretch    Stretch the input mask if necessary and possible. See below.
    region     Region selection. Default is to use the full image.
    box        Rectangular region to select in direction plane. Default
               is to use the entire direction plane.
               Example: box='10,10,50,50'
    chans      Channels to use. Default is to use all channels.
    stokes     Stokes planes to use. Default is to use all Stokes planes.
               Not used in for cases of mode='poli' or mode='pola'
    imagemd    The image from which metadata should be copied to the output. Default means no guarantee from
                which image is used. The image must exist and should conform to the output image spec.

    Available functions in the expr and mask parameters:
    pi(), e(), sin(), sinh(), asinh(), cos(), cosh(), tan(), tanh(),
    atan(), exp(), log(), log10(), pow(), sqrt(), complex(), conj()
    real(), imag(), abs(), arg(), phase(), amplitude(), min(), max()
    round(), isgn(), floor(), ceil(), rebin(), spectralindex(), pa(), 
    iif(), indexin(), replace(), ...

    If the mask has fewer dimensions than the image and if the shape
    of the dimensions the mask and image have in common are the same,
    the mask will automatically have the missing dimensions added so
    it conforms to the image.

    For a full description of the allowed syntax see the 
    Lattice Expression Language (LEL) documentation on the at:
    http://aips2.nrao.edu/docs/notes/223/223.html

    NOTE: where indexing and axis numbering are used in the above
    functions they are 1-based, ie. numbering starts at 1.

    If stretch is true and if the number of mask dimensions is less than
    or equal to the number of image dimensions and some axes in the
    mask are degenerate while the corresponding axes in the image are not,
    the mask will be stetched in the degenerate axis dimensions. For example,
    if the input image has shape [100, 200, 10] and the input
    mask has shape [100, 200, 1] and stretch is true, the mask will be
    stretched along the third dimension to shape [100, 200, 10]. However if
    the mask is shape [100, 200, 2], stretching is not possible and an
    error will result.

    CAUTIONS REGARDING OUTPUT IMAGE METADATA, INCLUDING BRIGHTNESS UNIT

    EXCEPT IN THE CASES NOTED BELOW, THIS APPLICATION MAKES NO ATTEMPT TO
    DETERMINE WHAT THE CORRECT BRIGHTNESS UNIT OF THE OUTPUT IMAGE SHOULD BE. THIS
    RESPONSIBILITY LIES SOLELY WITH THE USER. The brightness unit of the output image
    can be modified using tool method ia.setbrightnessunit() or task imhead with
    mode='put' and hdkey='bunit'. 

    Note that when multiple image are used in the expression, there is
    no garauntee about which of those images will be used to create the metadata
    of the output image, unless imagemd is specified. If imagemd is specified, the following
    rules of metadata copying will be followed:
    
    1. The pixel data type of the image specified by imagemd and the output image must
    be the same.
    2. The metadata copied include the coordinate system (and so of course the dimensionality of
    the output image must correspond to the coordinate system to be copied), the image_info record
    (which contains things like the beam(s)), the misc_info record (should one exist in the image
    specified by imagemd), and the units.
    3. If the output image is a spectral image, the brightness units are set to the empty string.
    4. If the ouptut image is a polarization angle image, the brightness unit is set to "deg" and
    the stokes coordinate is set to have a single plane of type of Pangle.

    Examples:
    # Double all values in an image.
    immath( imagesname='myimage.im', expr='IM0*2', outfile='double.im' )
    # or with an explicit notation, 
    immath( expr='"myimage.im"*2', outfile='double.im' )

    # Taking the sin of an image and adding it to another
    # Note that the images need to be the same size
    immath(images=['image1.im', 'image2.im'], expr='sin(IM1)+IM0;',outfile='newImage.im')

    # Adding only the plane associated with the 'V' stokes value and
    # the 1st channel together in two images
    immath(imagename=[image1', 'image2'], expr='IM0+IM1',chans='1',stokes='V')


    # Selecting a single plane (5th channel), of the 3-D cube and  
    # adding it to the original image.  In this example the 2-D plane
    # gets expanded out and the values are applied to each plane in the 
    # 3-D cube. 
    default('immath')
    imagename='ngc7538.image'
    outfile='chanFive.im'
    expr='IM0'
    chans='5'
    go
    default('immath')
    imagename=['ngc7538.image', chanFive.im']
    outfile='ngc7538_chanFive.im'
    expr='IM0+IM1'
    go

    # Selecting and saving the inner 3/4 of an image for channels 40,42,44
    # as well as channels less than 10
    default('immath')
    imagename='my_image.im'
    expr='IM0'
    box='25,25,123,123'
    chans='<10;40,42,44'
    outfile='my_image_inner.im' )
    go

    # Dividing an image by another, making sure we aren't dividing by zero
    default('immath')
    imagename=['orion.image', 'my.image']
    expr='IM0/iif(IM1==0,1.0,IM1)'
    outfile='my_orion.image'
    go

    # Applying a mask to all of the images in the expression
    default('immath')
    imagename=['ngc7538.image','ngc7538_clean.image']
    expr='(IM0*10)+IM1'
    mask='"ngc7538.mask"'
    outfile='really_noisy_ngc7538.image'
    go


    # Applying a pixel mask contained in the image information
    default('immath')
    imagename='ngc5921.image'
    expr='IM0*10'
    mask='mask("ngc5921.mask")'
    outfile='ngc5921.masked.image'
    go

    # Creating a total polarization intensity image from an multi-stokes image
    # containing IQUV.
    default('immath')
    outfile='pol_intensity'
    stokes=''
    # in imagename, you can also specify a list containing single stokes images
    # of Q and U (for linear polarization intensity) and V (for total
    # polarization intensity)
    imagename='3C138_pcal'
    mode='poli'
    go

    # Creating a polarization position angle image 
    default('immath')
    outfile='pol_angle.im'
    mode='pola'
    # you can also do imagename=['Q.im','U.im'] for single stokes images, order of
    # the two Stokes images does not matter
    imagename='3C138_pcal' # multi-stokes image containing at least Q and U stokes 
    go 

    # same as before but write a mask with values of False for pixels for which the
    # corresponding linear polarization ( sqrt(Q*Q+U*U)) is less than 30 microJy/beam
    polithresh='30uJy/beam'
    go

    # Creating a spectral index image from the images at two different observing frequencies
    default('immath')
    outfile='mySource_sp.im'
    mode='spix'
    imagename=['mySource_5GHz.im','mySource_8GHz.im']
    go
    
    TEMPORARY IMAGES

    At this time, it is usually necessary for this task to create intermediate, temporary disk images.
    The names of these images start with '_immath' and are created in the directory in which the task
    is run. The task makes reasonable attempts to remove these images before it exits, but there are
    conceivably instances where the temporary images may not be automatically deleted. It is generally
    safe to delete them by hand, assuming no immath instance is currently in progress.

    The hope and plan is that the necessity of these images will decrease in the future (i.e. the computations
    will require only RAM and not temporary persistent storage of intermediate results).

 

        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'immath'
        self.__globals__['taskname'] = 'immath'
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
            myparams['mode'] = mode = self.parameters['mode']
            myparams['outfile'] = outfile = self.parameters['outfile']
            myparams['expr'] = expr = self.parameters['expr']
            myparams['varnames'] = varnames = self.parameters['varnames']
            myparams['sigma'] = sigma = self.parameters['sigma']
            myparams['polithresh'] = polithresh = self.parameters['polithresh']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['region'] = region = self.parameters['region']
            myparams['box'] = box = self.parameters['box']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['stretch'] = stretch = self.parameters['stretch']
            myparams['imagemd'] = imagemd = self.parameters['imagemd']
            myparams['prec'] = prec = self.parameters['prec']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['mode'] = mode
        mytmp['outfile'] = outfile
        mytmp['expr'] = expr
        mytmp['varnames'] = varnames
        mytmp['sigma'] = sigma
        mytmp['polithresh'] = polithresh
        mytmp['mask'] = mask
        mytmp['region'] = region
        mytmp['box'] = box
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['stretch'] = stretch
        mytmp['imagemd'] = imagemd
        mytmp['prec'] = prec
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'immath.xml')

        casalog.origin('immath')
        try :
          #if not trec.has_key('immath') or not casac.casac.utils().verify(mytmp, trec['immath']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['immath'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('immath', 'immath.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'immath'
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
          result = immath(imagename, mode, outfile, expr, varnames, sigma, polithresh, mask, region, box, chans, stokes, stretch, imagemd, prec)

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
             tname = 'immath'
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
#        paramgui.runTask('immath', myf['_ip'])
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
        a['mode']  = 'evalexpr'
        a['outfile']  = 'immath_results.im'
        a['mask']  = ''
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['imagemd']  = ''
        a['prec']  = 'float'

        a['mode'] = {
                    0:odict([{'value':'evalexpr'}, {'expr':""}, {'varnames':""}]), 
                    1:odict([{'value':'poli'}, {'sigma':"0.0mJy/beam"}]), 
                    2:odict([{'value':'lpoli'}, {'sigma':"0.0mJy/beam"}]), 
                    3:odict([{'value':'tpoli'}, {'sigma':"0.0mJy/beam"}]), 
                    4:odict([{'value':'pola'}, {'polithresh':""}]), 
                    5:{'value':'spix'}}
        a['mask'] = {
                    0:odict([{'notvalue':''}, {'stretch':False}])}

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
    def description(self, key='immath', subkey=None):
        desc={'immath': 'Perform math operations on images',
               'imagename': 'a list of input images ',
               'mode': 'mode for math operation (evalexpr, spix, pola, poli, lpoli, tpoli)',
               'outfile': 'File where the output is saved',
               'expr': 'Mathematical expression using images',
               'varnames': 'a list of variable names to use with the image files',
               'sigma': 'standard deviation of noise for debiasing',
               'polithresh': 'Threshold in linear polarization intensity image below which to mask pixels.',
               'mask': 'Mask to use. Default is none.',
               'region': 'Region selection. Default is to use the full image.',
               'box': 'Rectangular region to select in direction plane. Default is to use the entire direction plane.',
               'chans': 'Channels to use. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Default is to use all Stokes planes.',
               'stretch': 'Stretch the mask if necessary and possible? See help stretch.par ',
               'imagemd': 'An image name from which metadata should be copied. The input can be either an image listed under imagename or any other image on disk. Leaving this parameter unset may copy header metadata from any of the input images, which one is not guaranteed. ',
               'prec': 'Precision for the output image pixels if mode="evalexpr" or "spix". "float" or "double" (minimum match supported)',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['imagename']  = ''
        a['mode']  = 'evalexpr'
        a['outfile']  = 'immath_results.im'
        a['expr']  = 'IM0'
        a['varnames']  = ''
        a['sigma']  = '0.0mJy/beam'
        a['polithresh']  = ''
        a['mask']  = ''
        a['region']  = ''
        a['box']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['stretch']  = False
        a['imagemd']  = ''
        a['prec']  = 'float'

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mode']  == 'evalexpr':
            a['expr'] = ""
            a['varnames'] = ""

        if self.parameters['mode']  == 'poli':
            a['sigma'] = "0.0mJy/beam"

        if self.parameters['mode']  == 'lpoli':
            a['sigma'] = "0.0mJy/beam"

        if self.parameters['mode']  == 'tpoli':
            a['sigma'] = "0.0mJy/beam"

        if self.parameters['mode']  == 'pola':
            a['polithresh'] = ""

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if a.has_key(paramname) :
              return a[paramname]
immath_cli = immath_cli_()
