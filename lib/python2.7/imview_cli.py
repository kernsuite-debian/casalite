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
from task_imview import imview
class imview_cli_:
    __name__ = "imview"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (imview_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'raster':None, 'contour':None, 'zoom':None, 'axes':None, 'out':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, raster=None, contour=None, zoom=None, axes=None, out=None, ):

        """View an image

        Detailed Description:

        The imview task will display images in raster, contour, vector or
        marker form.  Images can be blinked, and movies are available
        for spectral-line image cubes.

        Executing the imview task will bring up a display panel
        window, which can be resized.  If no data file was specified,
        a Load Data window will also appear. Click on the desired data
        file and choose the display type; the rendered data should appear
        on the display panel.

        A Data Display Options window will also appear.  It has drop-down
        subsections for related options, most of which are self-explanatory.

        The state of the imview task -- loaded data and related display
        options -- can be saved in a 'restore' file for later use.
        You can provide the restore filename on the command line or
        select it from the Load Data window.

        It is possible to use the viewer GUI tool to perform image manipulation
        and analysis tasks that are not available from the command-line start.
    
        Arguments :
                raster: (Optional)  Raster filename (string) or complete raster config dictionary. The allowed dictionary keys are file (string), scaling (numeric), range (2 element numeric vector), colormap (string), and colorwedge (bool).
                   Default Value: 

                contour: (Optional)  Contour filename (string) or complete contour config dictionary. The allowed dictionary keys are file (string), levels (numeric vector), unit (float), and base (float).
                   Default Value: 

                zoom: (Optional)  zoom can specify intermental zoom (integer), zoom region read from a file (string) or dictionary specifying the zoom region. The dictionary can have two forms. It can be either a simple region specified with blc (2 element vector) and trc (2 element vector) [along with an optional coord key ("pixel" or "world"; pixel is the default) or a complete region rectangle e.g. loaded with "rg.fromfiletorecord( )". The dictionary can also contain a channel (integer) field which indicates which channel should be displayed.
                   Default Value: 1

                axes: (Optional)  this can either be a three element vector (string) where each element describes what should be found on each of the x, y, and z axes or a dictionary containing fields "x", "y" and "z" (string).
                   Default Value: 

                out: (Optional)  Output filename or complete output config dictionary. If a string is passed, the file extension is used to determine the output type (jpg, pdf, eps, ps, png, xbm, xpm, or ppm). If a dictionary is passed, it can contain the fields, file (string), scale (float), dpi (int), or orient (landscape or portrait). The scale field is used for the bitmap formats (i.e. not ps or pdf) and the dpi parameter is used for scalable formats (pdf or ps).
                   Default Value: 

        Returns: void

        Example :

        The imview task provides access to a subset of all of the configuration
        options for loading and configuring the display of images in the casaviewer.
        This interface will evolve and eventually provide access to nearly all of 
        the image options available in the casaviewer.

        To simply create a casaviewer to set up interactively, you can use:

            imview

        To open a particular image:

            imview "ngc5921.clean.image"

        to open an image and overlay a contour:

            imview "ngc5921.clean.image", "ngc5921.clean.image"

        or equivalently:

            imview( raster="ngc5921.clean.image", contour="ngc5921.clean.image" )

        to output an image:

            imview( raster="ngc5921.clean.image", out="ngc5921-01.png" )    
            

        There are five optional parameters for imview -- raster, contour, zoom,
        axes, and out. Each of these parameters can take a few different forms and 
        are treated as python dictionaries:

        raster  -- (string) image file to open
                   (dict)   file (string)     => image file to open
                            scaling (float)   => scaling power cycles
                            range (float*2)   => data range
                            colormap (string) => name of colormap
                            colorwedge (bool) => show color wedge?
        contour -- (string) file to load as a contour
                   (dict)   file (string)     => file to load
                            levels (float*N)  => relative levels
                            base (numeric)    => zero in relative levels
                            unit (numeric)    => one in the relative levels
        zoom    -- (int)    integral zoom level
                   (string) region file to load as the zoom region
                   (dict)   blc (numeric*2)   => bottom left corner
                            trc (numeric*2)   => top right corner
                            coord (string)    => pixel or world
                            channel (int)     => chanel to display
                   (dict)   <region record>   => record loaded
                                                 e.g. rg.fromfiletorecord( )
        axes    -- (string*3) demension to display on the x, y, and z axes
                   (dict)     x               => dimension for x-axes
                              y               => dimension for y-axes
                              z               => dimension for z-axes
        out     -- (string) file with a supported extension
                            [jpg, pdf, eps, ps, png, xbm, xpm, ppm]
                    (dict)    file (string)   => filename
                              format (string) => valid ext (filename ext overrides)
                              scale (numeric) => scale for non-eps, non-ps output
                              dpi (numeric)   => dpi for eps or ps output
                              orient (string) => portrait or landscape

        Examples: 

        1)  A subset (zoom) of a raster image. Note the notation of curly brackets:

            imview(raster="ngc5921.clean.image", out="ngc5921-02.png",
                   zoom={'channel': 10, 'blc': [113,109], 'trc': [141,136]} )


        2) An overlay of a raster image, ngc5921.clean.image, with a
        contour map of the same image ngc5921.clean.image. Data ranges
        are selected, as well as the colormap and the scaling cycles
        of the raster image. Contours are autogenerated and The x-axis
        will be Declination. The image is written out to a file named 
        myout.png in the png format.

        imview(raster={'file': 'ngc5921.clean.image',
                       'range': [-0.01,0.03],
                       'colormap': 'Hot Metal 2',
                       'scaling': -1},
               contour={'file': 'ngc5921.clean.image'},
               axes={'x':'Declination'} ,
               zoom={'channel': 7, 'blc': [75,75], 'trc': [175,175],
                     'coord': 'pixel'},
               out='myout.png')

        3) As example (2) but with an integral zoom level and no output to a file

        imview(raster={'file': 'ngc5921.clean.image', 
                       'range': [-0.01,0.03], 
                       'colormap': 'Hot Metal 2'}, 
               contour={'file': 'ngc5921.clean.image'}, 
               axes={'x':'Declination'} , 
               zoom=2)

        4) Now, the contour levels are explicitely given, a region file is used
        to define the zoom area

        imview(raster={'file': 'ngc5921.clean.image',
                       'range': [-0.01,0.03],
                       'colormap': 'Hot Metal 2'},
               contour={'file': 'ngc5921.clean.image',
                        'levels': [-0.2, 0.2, 0.25, 0.3, 0.35, 0.4, 0.6, 0.8] },
               zoom='myregion.rgn')

        specifying "zoom={'file': 'myregion.rgn', 'channel': 10}" would result
        in the same level of zoom and would display channel number 10 from
        the cube.


    
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'imview'
        self.__globals__['taskname'] = 'imview'
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

            myparams['raster'] = raster = self.parameters['raster']
            myparams['contour'] = contour = self.parameters['contour']
            myparams['zoom'] = zoom = self.parameters['zoom']
            myparams['axes'] = axes = self.parameters['axes']
            myparams['out'] = out = self.parameters['out']


        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['raster'] = raster
        mytmp['contour'] = contour
        mytmp['zoom'] = zoom
        mytmp['axes'] = axes
        mytmp['out'] = out
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'imview.xml')

        casalog.origin('imview')
        try :
          #if not trec.has_key('imview') or not casac.casac.utils().verify(mytmp, trec['imview']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['imview'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('imview', 'imview.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'imview'
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
          result = imview(raster, contour, zoom, axes, out)

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
             tname = 'imview'
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
#        paramgui.runTask('imview', myf['_ip'])
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
        a['raster']  = {}
        a['contour']  = {}
        a['zoom']  = 1
        a['axes']  = {}
        a['out']  = ''


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
    def description(self, key='imview', subkey=None):
        desc={'imview': 'View an image',
               'raster': '(Optional)  Raster filename (string) or complete raster config dictionary. The allowed dictionary keys are file (string), scaling (numeric), range (2 element numeric vector), colormap (string), and colorwedge (bool).',
               'contour': '(Optional)  Contour filename (string) or complete contour config dictionary. The allowed dictionary keys are file (string), levels (numeric vector), unit (float), and base (float).',
               'zoom': '(Optional)  zoom can specify intermental zoom (integer), zoom region read from a file (string) or dictionary specifying the zoom region. The dictionary can have two forms. It can be either a simple region specified with blc (2 element vector) and trc (2 element vector) [along with an optional coord key ("pixel" or "world"; pixel is the default) or a complete region rectangle e.g. loaded with "rg.fromfiletorecord( )". The dictionary can also contain a channel (integer) field which indicates which channel should be displayed.',
               'axes': '(Optional)  this can either be a three element vector (string) where each element describes what should be found on each of the x, y, and z axes or a dictionary containing fields "x", "y" and "z" (string).',
               'out': '(Optional)  Output filename or complete output config dictionary. If a string is passed, the file extension is used to determine the output type (jpg, pdf, eps, ps, png, xbm, xpm, or ppm). If a dictionary is passed, it can contain the fields, file (string), scale (float), dpi (int), or orient (landscape or portrait). The scale field is used for the bitmap formats (i.e. not ps or pdf) and the dpi parameter is used for scalable formats (pdf or ps).',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['raster']  = {}
        a['contour']  = {}
        a['zoom']  = 1
        a['axes']  = {}
        a['out']  = ''

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if a.has_key(paramname) :
              return a[paramname]
imview_cli = imview_cli_()
