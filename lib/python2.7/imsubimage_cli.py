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
from task_imsubimage import imsubimage
class imsubimage_cli_:
    __name__ = "imsubimage"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (imsubimage_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'outfile':None, 'box':None, 'region':None, 'chans':None, 'stokes':None, 'mask':None, 'dropdeg':None, 'overwrite':None, 'verbose':None, 'stretch':None, 'keepaxes':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, outfile=None, box=None, region=None, chans=None, stokes=None, mask=None, dropdeg=None, overwrite=None, verbose=None, stretch=None, keepaxes=None, ):

        """Create a (sub)image from a region of the image
        Arguments :
                imagename: Input image name.  Default is unset.
                   Default Value: 

                outfile: Output image name.  Default is unset.
                   Default Value: 

                box: Rectangular region to select in direction plane. Default is to use the entire direction plane.
                   Default Value: 

                region: Region selection. Default is to use the full image.
                   Default Value: 

                chans: Channels to use. Default is to use all channels.
                   Default Value: 

                stokes: Stokes planes to use. Default is to use all Stokes planes.
                   Default Value: 

                mask: Mask to use. Default is none.
                   Default Value: 

                dropdeg: Drop degenerate axes
                   Default Value: False

                overwrite: Overwrite (unprompted) pre-existing output file?
                   Default Value: False

                verbose: Post additional informative messages to the logger
                   Default Value: True

                stretch: Stretch the mask if necessary and possible? 
                   Default Value: False

                keepaxes: If dropdeg=True, these are the degenerate axes to keep. Nondegenerate axes are implicitly always kept.
                   Default Value: 

        Returns: image

        Example :

PARAMETER SUMMARY
imagename        Name of the input image
outfile          Name of output file. Must be specified.
box              Rectangular region to select in direction plane. 
                 for details. Default is to use the entire direction plane.
region           Region selection. Default is to use
                 the full image.
chans            Channels to use. Default is to use
                 all channels.
stokes           Stokes planes to use. Default is to
                 use all Stokes planes.
mask             Mask to use. Default ("") is none.
dropdeg          If True, all degenerate axes in the input image will be excluded in the output image.
overwrite        If True, a pre-existing file of the same name as outfile will be overwritten.
verbose          Post additional informative messages to the logger.
stretch          Stretch the input mask if necessary and possible. Only used if a mask is specified.
                 
keepaxes         If dropdeg=True, these are the degenerate axes to keep. Nondegenerate axes are
                 implicitly always kept.
       

OVERVIEW

This task copies all or part of the image to a new image specified by outfile.
Both float and complex valued images are supported.

Sometimes it is useful to drop axes of length one (degenerate axes).
Set {\stfaf dropdeg} equal to True if you want to do this.

The output mask is the combination (logical OR) of the default input
\pixelmask\ (if any) and the OTF mask.  Any other input \pixelmasks\
will not be copied.  Use function maskhandler if you
need to copy other masks too.

If the mask has fewer dimensions than the image and if the shape
of the dimensions the mask and image have in common are the same,
the mask will automatically have the missing dimensions added so
it conforms to the image.

If stretch is true and if the number of mask dimensions is less than
or equal to the number of image dimensions and some axes in the
mask are degenerate while the corresponding axes in the image are not,
the mask will be stetched in the degenerate dimensions. For example,
if the input image has shape [100, 200, 10] and the input
mask has shape [100, 200, 1] and stretch is true, the mask will be
stretched along the third dimension to shape [100, 200, 10]. However if
the mask is shape [100, 200, 2], stretching is not possible and an
error will result.

EXAMPLES

# make a subimage containing only channels 4 to 6 of the original image,
imsubimage(imagename="my.im", outfile="first.im", chans="4~6")

# Same as above command, just specifying chans in an alternate, more verbose
# way
imsubimage(imagename="my.im", outfile="second.im", chans="range=[4pix,6pix]")

# Same as the above command, but even more verbose way of specifying the spectral
# selection. Assumes the direction axes are axes numbers 0 and 1.
ia.open("my.im")
shape = ia.shape()
axes = ia.coordsys().names()
ia.done()
xmax = shape[axes.index("Right Ascension")] - 1
ymax = shape[axes.index("Declination")] - 1
reg = "box[[0pix,0pix],[" + str(xmax) + "pix, " + str(ymax) + "pix]] range=[4pix,6pix]"
imsubimage(imagename="my.im", outfile="third.im", region=reg)

# As an example of the usage of the keepaxes parameter, consider an image
# that has axes RA, Dec, Stokes, and Freq. The Stokes and Freq axes are both
# degenerate while the RA and Dec axes are not, and it is desired to make a
# subimage in which the Stokes axis is discarded. The following command will
# accomplish that.
imsubimage(imagename="my.im", outfile="discarded_stokes.im", dropdeg=True, keepaxes=[3])


        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'imsubimage'
        self.__globals__['taskname'] = 'imsubimage'
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
            myparams['box'] = box = self.parameters['box']
            myparams['region'] = region = self.parameters['region']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['dropdeg'] = dropdeg = self.parameters['dropdeg']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['verbose'] = verbose = self.parameters['verbose']
            myparams['stretch'] = stretch = self.parameters['stretch']
            myparams['keepaxes'] = keepaxes = self.parameters['keepaxes']

        if type(keepaxes)==int: keepaxes=[keepaxes]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['box'] = box
        mytmp['region'] = region
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['dropdeg'] = dropdeg
        mytmp['overwrite'] = overwrite
        mytmp['verbose'] = verbose
        mytmp['stretch'] = stretch
        mytmp['keepaxes'] = keepaxes
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'imsubimage.xml')

        casalog.origin('imsubimage')
        try :
          #if not trec.has_key('imsubimage') or not casac.casac.utils().verify(mytmp, trec['imsubimage']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['imsubimage'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('imsubimage', 'imsubimage.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'imsubimage'
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
          result = imsubimage(imagename, outfile, box, region, chans, stokes, mask, dropdeg, overwrite, verbose, stretch, keepaxes)

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
             tname = 'imsubimage'
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
#        paramgui.runTask('imsubimage', myf['_ip'])
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
        a['box']  = ''
        a['region']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['dropdeg']  = False
        a['verbose']  = True

        a['mask'] = {
                    0:odict([{'notvalue':''}, {'stretch':False}])}
        a['outfile'] = {
                    0:odict([{'notvalue':''}, {'overwrite':False}])}
        a['dropdeg'] = {
                    0:odict([{'value':True}, {'keepaxes':[]}])}

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
    def description(self, key='imsubimage', subkey=None):
        desc={'imsubimage': 'Create a (sub)image from a region of the image',
               'imagename': 'Input image name.  Default is unset.',
               'outfile': 'Output image name.  Default is unset.',
               'box': 'Rectangular region to select in direction plane. Default is to use the entire direction plane.',
               'region': 'Region selection. Default is to use the full image.',
               'chans': 'Channels to use. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Default is to use all Stokes planes.',
               'mask': 'Mask to use. Default is none.',
               'dropdeg': 'Drop degenerate axes',
               'overwrite': 'Overwrite (unprompted) pre-existing output file?',
               'verbose': 'Post additional informative messages to the logger',
               'stretch': 'Stretch the mask if necessary and possible? ',
               'keepaxes': 'If dropdeg=True, these are the degenerate axes to keep. Nondegenerate axes are implicitly always kept.',

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
        a['box']  = ''
        a['region']  = ''
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['dropdeg']  = False
        a['overwrite']  = False
        a['verbose']  = True
        a['stretch']  = False
        a['keepaxes']  = []

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if self.parameters['outfile']  != '':
            a['overwrite'] = False

        if self.parameters['dropdeg']  == True:
            a['keepaxes'] = []

        if a.has_key(paramname) :
              return a[paramname]
imsubimage_cli = imsubimage_cli_()
