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
from task_impv import impv
class impv_cli_:
    __name__ = "impv"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (impv_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'imagename':None, 'outfile':None, 'mode':None, 'start':None, 'end':None, 'center':None, 'length':None, 'pa':None, 'width':None, 'unit':None, 'overwrite':None, 'region':None, 'chans':None, 'stokes':None, 'mask':None, 'stretch':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, imagename=None, outfile=None, mode=None, start=None, end=None, center=None, length=None, pa=None, width=None, unit=None, overwrite=None, region=None, chans=None, stokes=None, mask=None, stretch=None, ):

        """Construct a position-velocity image by choosing two points in the direction plane.
        Arguments :
                imagename: Name of the input image
                   Default Value: 

                outfile: Output image name. If empty, no image is written.
                   Default Value: 

                mode: If "coords", use start and end values. If "length", use center, length, and pa values.
                   Default Value: coords

                start: The starting pixel in the direction plane (array of two values).
                   Default Value: 

                end: The ending pixel in the direction plane (array of two values).
                   Default Value: 

                center: The center point in the direction plane (array of two values). If specified, length and pa must also be specified and neither of start nor end may be specified.
                   Default Value: 

                length: The length of the segment in the direction plane. If specified, center and pa must also be specified and neither of start nor end may be specified.
                   Default Value: 

                pa: The position angle of the segment in the direction plane, measured from north through east. If specified, center and length must also be specified and neither of start nor end may be specified.
                   Default Value: 

                width: Width of slice for averaging pixels perpendicular to the slice. Must be an odd positive integer or valid quantity. See help for details.
                   Default Value: 1

                unit: Unit for the offset axis in the resulting image. Must be a unit of angular measure.
                   Default Value: arcsec

                overwrite: Overwrite the output if it exists?
                   Default Value: False

                region: Region selection. Default is entire image. No selection is permitted in the direction plane.
                   Default Value: ""

                chans: Channels to use.  Channels must be contiguous. Default is to use all channels.
                   Default Value: 

                stokes: Stokes planes to use. Planes must be contiguous. Default is to use all stokes.
                   Default Value: 

                mask: Mask to use. Default is none.
                   Default Value: 

                stretch: Stretch the mask if necessary and possible? Default False
                   Default Value: False

        Returns: image

        Example :

PARAMETER SUMMARY
imagename        Name of the input (CASA, FITS, MIRIAD) image
outfile          Name of output CASA image. Must be specified.
mode             Indicates which sets of parameters to use for defining the slice. mode="coords" means use
                 start and end parameters. mode="length" means use center, length, and pa parameters to define
                 the slice.
start            The starting pixel in the direction plane (array of two values), such as [20, 5] or ["14h20m20.5s","-30d45m25.4s"].
                 Used iff mode="coords".
end              The ending pixel in the direction plane (array of two values), such as [200, 300].
                 Used iff mode="coords".
center           The center of the slice in the direction plane (array of two values), such as [20, 5] or ["14h20m20.5s","-30d45m25.4s"]. 
                 Used iff mode="length".
length           The length of the slice in the direction plane. May be specified as a single numerical value, in which
                 case it is interpreted as the number of pixels, or as a valid quantity which must be conformant with
                 the direction axes units (eg "40arcsec", {"value": 40, "unit": "arcsec"}).
                 Used iff mode="length".
pa               Position angle of the slice, measured from the direction of positive latitude of the positive longitude
                 (eg north through east in an equatorial coordinate system). Must be expressed as a valid angular
                 quantity (eg "40deg", {"value": 40, "unit": "deg"}).
                 Used iff mode="length".
width            Width of slice for averaging pixels perpendicular to the slice which must be an odd positive integer or
                 valid quantity. The averaging using this value occurs after the image has been rotated so the slice lies horizontally.
                 An integer value is interpreted as the number of pixels to average.
                 A value of 1 means no averaging. A value of 3 means average one pixel on each
                 side of the slice and the pixel on the slice. A value of 5 means average 2 pixels
                 on each side of the slice and the pixel on the slice, etc. If a quantity (eg. "4arcsec", qa.quantity("4arcsec"))
                 is specified, the equivalent number of pixels is calculated, and if necessary, rounded up
                 to the next odd integer.
unit             Allows the user to set the unit for the angular offset axis. Must be a unit of angular
                 measure.
overwrite        If output file is specified, this parameter controls if an already existing file by the
                 same name can be overwritten. If true, the user is not prompted, the file
                 if it exists is automatically overwritten.
region           Region specification. Default is to not use a region. If specified,
                 the entire direction plane must be specified. If specified do not specify chans or stokes.
chans            Optional contiguous frequency channel number specification. Default is all channels.
                 If specified, do not specify region.  
stokes           Contiguous stokes planes specification. If specified, do not specify region.
mask             Mask to use. Default is none.
stretch          Stretch the input mask if necessary and possible. Only used if a mask is specified.
                 

Create a position-velocity image. The way the slice is specified is controlled by the mode parameter. When
mode="coords", start end end are used to specified the points between which a slice is taken in the direction
coordinate. If mode="length"  center, pa (position angle), and length are used to specify the slice. The spectral
extent of the resulting image will be that provided by the region specification or the entire spectral range of
the input image if no region is specified. One may not specify a region in direction space; that is accomplished by
specifying the slice as described previously. The parameters start and end may be specified as two
element arrays of numerical values, in which case these values will be interpreted as pixel locations in the input
image. Alternatively, they may be expressed as arrays of two strings each representing the direction. These strings
can either represent quantities (eg ["40.5deg", "0.5rad") or be sexigesimal format (eg ["14h20m20.5s","-30d45m25.4s"],
["14:20:20.5s","-30.45.25.4"]). In addition, they may be expressed as a single string containing the longitude-like and
latitude-like values and optionally a reference frame value, eg "J2000 14:20:20.5s -30.45.25.4".The center parameter can
be specified in the same way. The length parameter may be specified as a single numerical value, in which case it is
interpreted as the length in pixels, or a valid quantity, in which case it must have units conformant with the
direction axes units. The pa (position angle) parameter must be specified as a valid quantity with angular units.
The position angle is interpreted in the usual astronomical sense; eg measured from north through east in an equatorial
coordinate system. The slice in this case starts at the specified position angle and ends on the opposite side of
the specified center. Thus pa="45deg" means start at a point at a pa of 45 degrees relative to the specified center and
end at a point at a pa of 215 degrees relative to the center. Either start/end or center/pa/length must be specified;
if a parameter from one of these sets is specified, a parameter from the other set may not be specified. In either
case, the end points of the segment must fail within the input image, and they both must be at least 2 pixels from the
edge of the input image to facilite rotation (see below).

One may specify a width, which represents the number of pixels centered along and perpendicular
to the direction slice that are used for averaging along the slice. The width may be specified as an integer, in which
case it must be positive and odd. Alternatively, it may be specified as a valid quantity string (eg, "4arcsec") or
quantity record (eg qa.quantity("4arcsec"). In this case, units must be conformant to the direction axes units (usually
angular units) and the specified quantity will be rounded up, if necessary, to the next highest equivalent odd integer number
of pixels. The default value of 1 represents no averaging.
A value of 3 means average one pixel on each side of the slice and the pixel on the slice. 
Note that this width is applied to pixels in the image after it has been rotated (see below for a description
of the algorithm used).
 
One may specify the unit for the angular offset axis.
        
Internally, the image is first rotated, padding if necessary to include relevant pixels that would otherwise
be excluded by the rotation operation, so that the slice is horizontal, with the starting pixel left of the
ending pixel. Then, the pixels within the specified width of the slice are averaged and the resulting image is
written and/or returned. The output image has a linear coordinate in place of the direction coordinate of the
input image, and the corresponding axis represents angular offset with the center pixel having a value of 0.
        
The equivalent coordinate system, with a (usually) rotated direction coordinate (eg, RA and Dec) is written
to the output image as a table record. It can be retrieved using the table tool as shown in the example below.
        
# create a pv image with the position axis running from ra, dec pixel positions of [45, 50] to [100, 120]
# in the input image
impv(imagename="my_spectral_cube.im", outfile="mypv.im", start=[45,50], end=[100,120])
# analyze the pv image, such as get statistics
pvstats = imstat("mypv.im")
#
# get the alternate coordinate system information
tb.open("mypv.im")
alternate_csys_record = tb.getkeyword("misc")["secondary_coordinates"]
tb.done()
    
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'impv'
        self.__globals__['taskname'] = 'impv'
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
            myparams['mode'] = mode = self.parameters['mode']
            myparams['start'] = start = self.parameters['start']
            myparams['end'] = end = self.parameters['end']
            myparams['center'] = center = self.parameters['center']
            myparams['length'] = length = self.parameters['length']
            myparams['pa'] = pa = self.parameters['pa']
            myparams['width'] = width = self.parameters['width']
            myparams['unit'] = unit = self.parameters['unit']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['region'] = region = self.parameters['region']
            myparams['chans'] = chans = self.parameters['chans']
            myparams['stokes'] = stokes = self.parameters['stokes']
            myparams['mask'] = mask = self.parameters['mask']
            myparams['stretch'] = stretch = self.parameters['stretch']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['imagename'] = imagename
        mytmp['outfile'] = outfile
        mytmp['mode'] = mode
        mytmp['start'] = start
        mytmp['end'] = end
        mytmp['center'] = center
        mytmp['length'] = length
        mytmp['pa'] = pa
        mytmp['width'] = width
        mytmp['unit'] = unit
        mytmp['overwrite'] = overwrite
        mytmp['region'] = region
        mytmp['chans'] = chans
        mytmp['stokes'] = stokes
        mytmp['mask'] = mask
        mytmp['stretch'] = stretch
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'impv.xml')

        casalog.origin('impv')
        try :
          #if not trec.has_key('impv') or not casac.casac.utils().verify(mytmp, trec['impv']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['impv'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('impv', 'impv.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'impv'
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
          result = impv(imagename, outfile, mode, start, end, center, length, pa, width, unit, overwrite, region, chans, stokes, mask, stretch)

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
             tname = 'impv'
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
#        paramgui.runTask('impv', myf['_ip'])
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
        a['mode']  = 'coords'
        a['width']  = 1
        a['unit']  = 'arcsec'
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''

        a['outfile'] = {
                    0:odict([{'notvalue':''}, {'overwrite':False}])}
        a['mask'] = {
                    0:odict([{'notvalue':''}, {'stretch':False}])}
        a['chans'] = {
                    0:odict([{'value':''}, {'region':""}])}
        a['mode'] = {
                    0:odict([{'value':'coords'}, {'start':""}, {'end':""}]), 
                    1:odict([{'value':'length'}, {'center':""}, {'length':""}, {'pa':""}])}

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
    def description(self, key='impv', subkey=None):
        desc={'impv': 'Construct a position-velocity image by choosing two points in the direction plane.',
               'imagename': 'Name of the input image',
               'outfile': 'Output image name. If empty, no image is written.',
               'mode': 'If "coords", use start and end values. If "length", use center, length, and pa values.',
               'start': 'The starting pixel in the direction plane (array of two values).',
               'end': 'The ending pixel in the direction plane (array of two values).',
               'center': 'The center point in the direction plane (array of two values). If specified, length and pa must also be specified and neither of start nor end may be specified.',
               'length': 'The length of the segment in the direction plane. If specified, center and pa must also be specified and neither of start nor end may be specified.',
               'pa': 'The position angle of the segment in the direction plane, measured from north through east. If specified, center and length must also be specified and neither of start nor end may be specified.',
               'width': 'Width of slice for averaging pixels perpendicular to the slice. Must be an odd positive integer or valid quantity. See help for details.',
               'unit': 'Unit for the offset axis in the resulting image. Must be a unit of angular measure.',
               'overwrite': 'Overwrite the output if it exists?',
               'region': 'Region selection. Default is entire image. No selection is permitted in the direction plane.',
               'chans': 'Channels to use.  Channels must be contiguous. Default is to use all channels.',
               'stokes': 'Stokes planes to use. Planes must be contiguous. Default is to use all stokes.',
               'mask': 'Mask to use. Default is none.',
               'stretch': 'Stretch the mask if necessary and possible? Default False',

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
        a['mode']  = 'coords'
        a['start']  = ''
        a['end']  = ''
        a['center']  = ''
        a['length']  = ''
        a['pa']  = ''
        a['width']  = 1
        a['unit']  = 'arcsec'
        a['overwrite']  = False
        a['region']  = ""
        a['chans']  = ''
        a['stokes']  = ''
        a['mask']  = ''
        a['stretch']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['outfile']  != '':
            a['overwrite'] = False

        if self.parameters['mask']  != '':
            a['stretch'] = False

        if self.parameters['chans']  == '':
            a['region'] = ""

        if self.parameters['mode']  == 'coords':
            a['start'] = ""
            a['end'] = ""

        if self.parameters['mode']  == 'length':
            a['center'] = ""
            a['length'] = ""
            a['pa'] = ""

        if a.has_key(paramname) :
              return a[paramname]
impv_cli = impv_cli_()
