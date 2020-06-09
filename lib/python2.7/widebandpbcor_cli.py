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
from task_widebandpbcor import widebandpbcor
class widebandpbcor_cli_:
    __name__ = "widebandpbcor"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (widebandpbcor_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'imagename':None, 'nterms':None, 'threshold':None, 'action':None, 'reffreq':None, 'pbmin':None, 'field':None, 'spwlist':None, 'chanlist':None, 'weightlist':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, imagename=None, nterms=None, threshold=None, action=None, reffreq=None, pbmin=None, field=None, spwlist=None, chanlist=None, weightlist=None, ):

        """Wideband PB-correction on the output of the MS-MFS algorithm

        Detailed Description:
WideBand Primary-beam correction. It computes a set of PBs at the specified frequencies, calculates Taylor-coefficient images that represent the PB spectrum, performs a polynomial division to PB-correct the output Taylor-coefficient images from clean(nterms&gt;1), and recompute spectral index (and curvature) using the PB-corrected Taylor-coefficient images 
        Arguments :
                vis: Name of measurement set. 
                   Default Value: 

                imagename: Name-prefix of multi-termimages to operate on. 
                   Default Value: 

                nterms: Number of taylor terms to use
                   Default Value: 2

                threshold: Intensity above which to re-calculate spectral index 
                   Default Value: 

                action: PB-correction (pbcor) or only calc spectral-index (calcalpha)
                   Default Value: pbcor
                   Allowed Values:
                                pbcor
                                calcalpha

                reffreq: Reference frequency (if specified in clean)
                   Default Value: 

                pbmin: PB threshold below which to not correct
                   Default Value: 0.2

                field: Fields to include in the PB calculation
                   Default Value: 

                spwlist: List of N spw ids
                   Default Value: 
    
        

                chanlist: List of N channel ids
                   Default Value: 
    
        

                weightlist: List of N weights (relative)
                   Default Value: 
    
        

        Returns: void

        Example :


   Wide-band Primary-beam correction

    (1) Compute a set of Primary Beams at the specified frequencies
    (2) Calculate Taylor-coefficient images that represent the PB spectrum
    (3) Perform a polynomial division to PB-correct the output Taylor-coefficient
          images from the MS-MFS algorithm ( clean(nterms>1) )
    (4) Recompute spectral index (and curvature) using the corrected Taylor-coefficient images.

   [ Optionally, skip PB-correction, and only recalculate spectral index
      with a different threshold ]

   This is a temporary task, meant for use until a widebandpbcor option is enabled from
   within the tclean task.

   An output directory named imagename.pbcor.workdirectory is created, and filled with
   an image-cube of the evaluated primary beams at all specified frequencies,
   Taylor-coefficients, and a 'spectral index' due to the primary beam.  
   Note that for the actual pb-correction, only the Taylor-coefficient images are used.
 
   Task parameters :

   vis -- Name of input visibility file
           example : vis = 'ngc5921.ms'
              Only one MS can be specified here, and it must contain at-least one
               timestep of data at all frequencies required to calculate the PB spectrum. 

              Note : If the imaging was done using a list of MSs, and any one MS covers
                        the entire frequency range, then it will suffice to supply only that one
                        MS.  This MS is used only to extract frequencies at which to compute
                        primary beams before fitting Taylor polynomials.

              Note : In case of multiple MSs that cover different frequency ranges, 
                        please split/concat a small fraction of the data from each MS to form
                        one single MS that contains the full frequency range. This task uses
                        the MS only for frequency meta-data.

   imagename -- Pre-name of input and output images. Same as in the clean task.           
           example : imagename = 'run1'
              Restored-images ( run1.image.tt0,etc) and residual images ( run1.residual.tt0, etc.. )
              must be available on disk. 

   nterms -- Number of Taylor terms to be used to model the frequency-dependence 
                 of the primary beam.
           example : nterms = 2
                nterms must be less than or equal to the number of frequencies specified via
                spwlist, chanlist and weightlist.
                nterms=1 will do a standard division by the average PB computed over all
                specified frequencies.

   threshold -- Flux level in the restored intensity map, below which to not 
                     recalculate spectral index. 
           example : threshold = '0.1Jy'

   action -- Choice of PB-correction with spectral-index recalculation
                or only spectral-index recalculation (using the specified threshold)
           example : action='pbcor'  or action='calcalpha'
               
           With action='pbcor', the following output images are created/overwritten.

              - imagename.pbcor.workdirectory  :  This directory contains an image cube with
                PBs at the list of specified frequencies, and Taylor-coefficient images that
                describe the PB spectrum.
                   -  imagename.pb.cube : Concatenated cube of PBs 
                   -  imagename.pb.tt0, tt1, ... : Taylor coefficients describing the PB spectrum
                   -  imagename.pb.alpha : Spectral index of the PB (for information only)
              - imagename.image.pbcor.tt0,tt1,... : Corrected Taylor coefficients
              - imagename.pbcor.image.alpha : Corrected Spectral Index
              - imagename.pbcor.image.alpha.error : New error map.

            With action='calcalpha', the following output images are created/overwritten
              - imagename.image.alpha : Corrected Spectral Index
              - imagename.image.alpha.error : New error map.

   reffreq -- Reference frequency about which the Taylor-expansion is defined.
            example : reffreq = '1.5GHz'
                 If left unspecified, it is picked from the input restored image.
                 Note : If reffreq was specified during task clean to produce the images
                           it must be specified here. 

   pbmin -- PB gain level below which to not compute Taylor-coefficients or
                apply PB-corrections.
            example : pbmin = 0.1

   field -- Field selection for the Primary Beam calculation. 
            example : field = '3C291'
                This field selection must be identical to that used in 'clean'

   spwlist -- List of SPW ids for which to make separate Primary Beams
   chanlist -- List of channel ids, within the above SPW ids, at which to make PBs.

             example :  spwlist=[0,1,2], chanlist=[32,32,32] 
                          Make PBs at frequencies corresponding to channel 32 of
                          spws 0,1 and 2.
             example :  spwlist=[0,0,0], chanlist=[0,10,20]
                           Make PBs at frequencies corresponding to channels 0,10,20
                           of spw 0
 
                   Primary beams are computed at these specified frequencies and 
                   for pointings selected by 'field'.  Taylor-coefficients that represent
                   the PB spectrum are computed from these images.

   weightlist -- List of relative weights to apply to the PBs selected via the
                     spwlist,chanlist parameters. Weights should approximately represent the
                     sum-of-weights applicable during imaging each of these frequencies.
              example : weightlist=[0.5,1.0,1.0] 
                                 The first frequency had less usable data due to flagged RFI,
                                 but the other two had relatively equal weight.
                     These weights are applied to the PB spectrum while computing
                     PB Taylor-coefficients. Setting weights to anything other than 1.0
                     makes a difference only with very lop-sided weights. 


    NOTE : One frequently asked question relates to how best to choose spwlist,chanlist,weightlist.

               The basic principles at work here are

               (1) Imaging = fitting a polynomial to a noisy spectrum (with weights). 
                                      The polynomial represents I(nu) x P(nu)

               (2) PB model = fitting a polynomial to a collection of PBs at different 
                                       frequencies (with weights). The polynomial represents P(nu)

               (3) Dividing the two polynomials via their coefficients.

               Steps (1) and (2) need to be consistent with each other (w.r.to frequencies used 
               and their weights) to produce fits that when divided give exactly only the sky parameters. 
               Unless you use the same math (and code) for both, they won't be exactly consistent. 
               The way to minimize differences is to choose a list of frequencies (via spws/chans)
               and weights for widebandpbcor that resemble the frequency structure of the data you 
               have used for imaging. 
               For example, if you have 3 spws in your data and the middle spw has a factor of 10 
               less weight in the data, then, using just one channel each from the two outer spws for 
               the PB modeling may be close enough to using all 3 spws. Or, you could also pick 
               the middle channel of all 3 spws, and assign weights as [1.0, 0.1, 1.0].


  
        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'widebandpbcor'
        self.__globals__['taskname'] = 'widebandpbcor'
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

            myparams['vis'] = vis = self.parameters['vis']
            myparams['imagename'] = imagename = self.parameters['imagename']
            myparams['nterms'] = nterms = self.parameters['nterms']
            myparams['threshold'] = threshold = self.parameters['threshold']
            myparams['action'] = action = self.parameters['action']
            myparams['reffreq'] = reffreq = self.parameters['reffreq']
            myparams['pbmin'] = pbmin = self.parameters['pbmin']
            myparams['field'] = field = self.parameters['field']
            myparams['spwlist'] = spwlist = self.parameters['spwlist']
            myparams['chanlist'] = chanlist = self.parameters['chanlist']
            myparams['weightlist'] = weightlist = self.parameters['weightlist']

        if type(spwlist)==int: spwlist=[spwlist]
        if type(chanlist)==int: chanlist=[chanlist]
        if type(weightlist)==float: weightlist=[weightlist]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['imagename'] = imagename
        mytmp['nterms'] = nterms
        mytmp['threshold'] = threshold
        mytmp['action'] = action
        mytmp['reffreq'] = reffreq
        mytmp['pbmin'] = pbmin
        mytmp['field'] = field
        mytmp['spwlist'] = spwlist
        mytmp['chanlist'] = chanlist
        mytmp['weightlist'] = weightlist
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'widebandpbcor.xml')

        casalog.origin('widebandpbcor')
        try :
          #if not trec.has_key('widebandpbcor') or not casac.casac.utils().verify(mytmp, trec['widebandpbcor']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['widebandpbcor'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('widebandpbcor', 'widebandpbcor.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'widebandpbcor'
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
          result = widebandpbcor(vis, imagename, nterms, threshold, action, reffreq, pbmin, field, spwlist, chanlist, weightlist)

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
             tname = 'widebandpbcor'
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
#        paramgui.runTask('widebandpbcor', myf['_ip'])
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
        a['vis']  = ''
        a['imagename']  = ''
        a['nterms']  = 2
        a['threshold']  = ''
        a['action']  = 'pbcor'

        a['action'] = {
                    0:odict([{'value':'pbcor'}, {'reffreq':''}, {'pbmin':0.2}, {'field':''}, {'spwlist':[]}, {'chanlist':[]}, {'weightlist':[]}])}

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
    def description(self, key='widebandpbcor', subkey=None):
        desc={'widebandpbcor': 'Wideband PB-correction on the output of the MS-MFS algorithm',
               'vis': 'Name of measurement set. ',
               'imagename': 'Name-prefix of multi-termimages to operate on. ',
               'nterms': 'Number of taylor terms to use',
               'threshold': 'Intensity above which to re-calculate spectral index ',
               'action': 'PB-correction (pbcor) or only calc spectral-index (calcalpha)',
               'reffreq': 'Reference frequency (if specified in clean)',
               'pbmin': 'PB threshold below which to not correct',
               'field': 'Fields to include in the PB calculation',
               'spwlist': 'List of N spw ids',
               'chanlist': 'List of N channel ids',
               'weightlist': 'List of N weights (relative)',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['imagename']  = ''
        a['nterms']  = 2
        a['threshold']  = ''
        a['action']  = 'pbcor'
        a['reffreq']  = ''
        a['pbmin']  = 0.2
        a['field']  = ''
        a['spwlist']  = []
        a['chanlist']  = []
        a['weightlist']  = []

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['action']  == 'pbcor':
            a['reffreq'] = ''
            a['pbmin'] = 0.2
            a['field'] = ''
            a['spwlist'] = []
            a['chanlist'] = []
            a['weightlist'] = []

        if a.has_key(paramname) :
              return a[paramname]
widebandpbcor_cli = widebandpbcor_cli_()
