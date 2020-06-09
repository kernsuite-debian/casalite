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
import task_widebandpbcor
def widebandpbcor(vis='', imagename='', nterms=2, threshold='', action='pbcor', reffreq='', pbmin=0.2, field='', spwlist=[], chanlist=[], weightlist=[]):

        """Wideband PB-correction on the output of the MS-MFS algorithm

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
        if type(spwlist)==int: spwlist=[spwlist]
        if type(chanlist)==int: chanlist=[chanlist]
        if type(weightlist)==float: weightlist=[weightlist]

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
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'widebandpbcor.xml')

        casalog.origin('widebandpbcor')
        if trec.has_key('widebandpbcor') and casac.utils().verify(mytmp, trec['widebandpbcor']) :
            result = task_widebandpbcor.widebandpbcor(vis, imagename, nterms, threshold, action, reffreq, pbmin, field, spwlist, chanlist, weightlist)

        else :
          result = False
        return result