# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.10
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_synthesisimager')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_synthesisimager')
    _synthesisimager = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_synthesisimager', [dirname(__file__)])
        except ImportError:
            import _synthesisimager
            return _synthesisimager
        if fp is not None:
            try:
                _mod = imp.load_module('_synthesisimager', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _synthesisimager = swig_import_helper()
    del swig_import_helper
else:
    import _synthesisimager
del _swig_python_version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

class synthesisimager(_object):
    """Proxy of C++ casac::synthesisimager class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, synthesisimager, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, synthesisimager, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _synthesisimager.delete_synthesisimager
    __del__ = lambda self: None

    def __init__(self):
        """__init__(self) -> synthesisimager"""
        this = _synthesisimager.new_synthesisimager()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def selectdata(self, *args, **kwargs):
        """
        selectdata(self, selpars) -> bool



        Summary
        	Select data from one MS

        Description



        Input Parameters:
        	selpars		 All parameters that control selection within one MS 

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_selectdata(self, *args, **kwargs)


    def tuneselectdata(self):
        """
        tuneselectdata(self) -> record *



        Summary
        	reselect the data to match image definition

        Description


        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_tuneselectdata(self)


    def defineimage(self, *args, **kwargs):
        """
        defineimage(self, impars, gridpars) -> bool



        Summary
        	Define image coordinate systems FTMs

        Description



        Input Parameters:
        	impars		 All parameters that control image coordinate system definition 
        	gridpars	 All parameters that control ftmachines and gridding parameters 

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_defineimage(self, *args, **kwargs)


    def setdata(self, *args, **kwargs):
        """
        setdata(self, msname, spw, freqbeg, freqend, freqframe, field, antenna, timestr, scan, obs, state, uvdist, taql, usescratch=False, readonly=False, incrmodel=False) -> bool



        Summary
        	Select data from one MS via conventional parameters (in lieu of selectdata)

        Description

        Select data from one MS. Call this function in succession if there are
        multiple MSs. 


        Input Parameters:
        	msname		 Name of one measurement set 
        	spw		 Spectral Window / Channel / Frequency selection 
        	freqbeg		 Starting frequency/velocity/channel as a string with units. If spw is also supplied, the intersection will be used 
        	freqend		 End frequency/velocity/channel as a string with units. 
        	freqframe	 Frequency frame in which freqbeg and freqend are specified. LSRK 
        	field		 Field selection 
        	antenna		 Antenna / Baseline selection 
        	timestr		 Time range selection 
        	scan		 Scan selection 
        	obs		 Observation id selection 
        	state		 Scan Intent or State selection 
        	uvdist		 UV range selection 
        	taql		 Generic taql selection 
        	usescratch	 Use scratch column (True) or virtual records (False) for model data false 
        	readonly	 Open the MS in readonly mode. No model data will be written. false 
        	incrmodel	 Subtract existing model data and start with residuals false 

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_setdata(self, *args, **kwargs)


    def setimage(self, *args, **kwargs):
        """
        setimage(self, imagename, nx=128, ny=-1, cellx, celly, stokes, phasecenter, nchan=-1, freqstart, freqstep, restfreq, facets=1, ftmachine, ntaylorterms=1, reffreq, projection, distance, freqframe, tracksource=False, trackdir, overwrite=True, padding=1.0, useautocorr=False, usedoubleprec=True, wprojplanes=1, convfunc, startmodel, aterm=True, psterm=True, mterm=False, wbawp=True, cfcache, dopointing=False, dopbcorr=True, conjbeams=False, computepastep=360.0, rotatepastep=5.0) -> bool



        Summary
        	Define the image coordinate systems and types via conventinal parameters in lieu of defineimage

        Description

        Define the image coordinate systems and shapes.


        Input Parameters:
        	imagename	 Base image name 
        	nx		 Total number of spatial pixels in x 128 
        	ny		 Total number of spatial pixels in y -1 
        	cellx		 Cellsize in x (e.g. '1arcsec') 1.0 
        	celly		 Cellsize in y (e.g. '1arcsec') 
        	stokes		 Stokes parameters to image (e.g. 'IQUV') IV IQU IQUV I 
        	phasecenter	 Direction of phase center as a diretion measure or a field id 0 
        	nchan		 Number of channels; a -1 (default) means all the channels as selected in selectvis and combined into one continuum channel -1 
        	freqstart	 Start channel; A 0-relative channel number of the spwid or a frequency quantity or a velocity quantity or radial velocity measure 0 
        	freqstep	 Step in channel; integer for number of channels or frequency quantity or velocity quantity or radial velocity measure 1 
        	restfreq	 rest frequency to use; default =\> use the one available in ms 
        	facets		 Number of facets on each axis 1 
        	ftmachine	 FT-Machine type gridft 
        	ntaylorterms	 Number of terms for a spectral Taylor expansion 1 
        	reffreq		 Reference Frequency of the image. Also used in the Taylor expansion. 
        	projection	 Image coordinate system projection SIN 
        	distance	 Distance to object: usually ignore this! (m) 0.0 
        	freqframe	 Frequency frame in which freqstart and freqstep are specified. LSRK 
        	tracksource	 Track a source. false 
        	trackdir	 Name of moving source, e.g planet or moon, to keep fixed in image 
        	overwrite	 Overwrite the image if it exists (true) true 
        	padding		 FFT padding 1.0 
        	useautocorr	 Use auto correlations false 
        	usedoubleprec	 Double Precision gridding or not true 
        	wprojplanes	 Number of w-projection planes 1 
        	convfunc	 Name of convolution function SF 
        	startmodel	 Starting model ( image name or component list name ) 
        	aterm		 Set the antenna aperture tmer (aterm) on/off true 
        	psterm		 Set the Prolate Spheroidal term (psterm) on/off true 
        	mterm		 Set the mosaic term (mterm) on/off false 
        	wbawp		 Set usage of the wide-band A-Projection algorithm true 
        	cfcache		 Name of convolution function disk cache 
        	dopointing	 Control application of the pointing correction false 
        	dopbcorr	 Control normalization of the raw image by the model PB true 
        	conjbeams	 Set conjbeams on/off false 
        	computepastep	 Increment in PA after which re-computation of the GCFs is triggered. 360.0 implies compute GCFs for only the first PA value encountered in the MS. 360.0 
        	rotatepastep	 Increment in PA after which trigger in-memory rotation of the GCF nearest to the current PA value in the CF cache. 5.0 

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_setimage(self, *args, **kwargs)


    def setweighting(self, *args, **kwargs):
        """
        setweighting(self, type, rmode, noise, robust=0.0, fieldofview, npixels=0, multifield=False, usecubebriggs=False, uvtaper) -> bool



        Summary
        	Set parameters to control weighting during imaging

        Description



        Input Parameters:
        	type		 Data weighting scheme natural 
        	rmode		 rmode norm 
        	noise		 Noise level 
        	robust		 Robustness weighting factor 0.0 
        	fieldofview	 Field of view 
        	npixels		 NPixels 0 
        	multifield	 Multifield false 
        	usecubebriggs	 Use per channel weight density calculation for Briggs style weighting false 
        	uvtaper		 Parameters of uv-taper Gaussian 

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_setweighting(self, *args, **kwargs)


    def makepsf(self):
        """
        makepsf(self) -> bool



        Summary
        	Make the psf

        Description


        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_makepsf(self)


    def apparentsens(self):
        """
        apparentsens(self) -> record *



        Summary
        	Calculate apparent aggregate sensitivity in the selected visibilities

        Description


        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_apparentsens(self)


    def predictmodel(self):
        """
        predictmodel(self) -> bool



        Summary
        	Predict model visibilities.

        Description


        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_predictmodel(self)


    def drygridding(self, *args, **kwargs):
        """
        drygridding(self, cflist) -> bool



        Summary
        	Run a dry gridding run.

        Description



        Input Parameters:
        	cflist		 List of CFs 

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_drygridding(self, *args, **kwargs)


    def fillcfcache(self, *args, **kwargs):
        """
        fillcfcache(self, cflist, ftmname, cfcpath, pstermon=False, atermon=True, conjbeams=False) -> bool



        Summary

            Fill a potentially blank CFCache held inside the AWProject-class
            FTMachines.


        Description



        Input Parameters:
        	cflist		 List of CFs 
        	ftmname		 Name of the FTMachine used 
        	cfcpath		 Path to the CFCache on the disk 
        	pstermon	 Is the PS-term ON? false 
        	atermon		 Is the A-term ON? true 
        	conjbeams	 Use WB A-Projection algorithm (use frequency-conjugate beams)? false 

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_fillcfcache(self, *args, **kwargs)


    def reloadcfcache(self):
        """
        reloadcfcache(self) -> bool



        Summary

            Re-load the CFCache, the name of which should already be set in
            the tool.


        Description


        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_reloadcfcache(self)


    def executemajorcycle(self, *args, **kwargs):
        """
        executemajorcycle(self, controls) -> bool



        Summary
        	Run a major cycle

        Description



        Input Parameters:
        	controls	 All parameters that control major cycle 

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_executemajorcycle(self, *args, **kwargs)


    def makepb(self):
        """
        makepb(self) -> bool



        Summary
        	Make the primary beam

        Description


        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_makepb(self)


    def makesdimage(self):
        """
        makesdimage(self) -> bool



        Summary
        	Make the single-dish image

        Description


        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_makesdimage(self)


    def makesdpsf(self):
        """
        makesdpsf(self) -> bool



        Summary
        	Make the single-dish PSF

        Description


        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_makesdpsf(self)


    def makeimage(self, *args, **kwargs):
        """
        makeimage(self, type, image, compleximage, model=0) -> bool



        Summary
        	calculate images of different type by gridding

        Description

        This tool function actually does gridding (and Fourier inversion if
        needed) of visibility data to make an image. It allows calculation of
        various types of image:
        egin{description}
        \item[observed] Make the dirty image from the DATA column ({m default})
        \item[model] Make the dirty image from the MODEL\_DATA column
        \item[corrected] Make the dirty image from the CORRECTED\_DATA column
        \item[residual] Make the dirty image from the difference of the
        CORRECTED\_DATA and MODEL\_DATA columns
        \item[psf] Make the point spread function
        \item[singledish] Make a single dish image
        \item[coverage] Make a single dish or mosaic coverage image
        \item[holography] Make a complex holography image (experimental)

        nd{description}


        Input Parameters:
        	type		 Type of output image observed observed model corrected residual psf singledish coverage holography 
        	image		 Name of output image 
        	compleximage	 Name of output complex image 
        	model		 In case of multifield which image 0 

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_makeimage(self, *args, **kwargs)


    def unlockimages(self, imagefieldid=0):
        """
        unlockimages(self, imagefieldid=0) -> bool



        Summary
        	release some images attached to this process

        Description

          Try to unlock images if the need arise


        Input Parameters:
        	imagefieldid	 which image or outlier to unlock 0 

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_unlockimages(self, imagefieldid)


    def estimatememory(self):
        """
        estimatememory(self) -> variant *



        Summary
        	Get an estimate in kilobytes of memory that will be needed

        Description

          This function returns an estimate of the memory (RAM) to be used by sythesisimager tool. Need to be run after functions setdata and defineimage are done

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_estimatememory(self)


    def getimstore(self, id=0):
        """
        getimstore(self, id=0) -> casac::synthesisimstore *



        Summary
        	Get Image Store

        Description



        Input Parameters:
        	id		 Image field id 0 

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_getimstore(self, id)


    def getcsys(self):
        """
        getcsys(self) -> record *



        Summary
        	get internally stored coordsys record

        Description


        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_getcsys(self)


    def updatenchan(self):
        """
        updatenchan(self) -> int



        Summary
        	get internally stored updated nchan 

        Description


        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_updatenchan(self)


    def getweightdensity(self):
        """
        getweightdensity(self) -> string



        Summary
        	Save natural gridded wt to disk.

        Description


        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_getweightdensity(self)


    def setweightdensity(self, *args, **kwargs):
        """
        setweightdensity(self, type) -> bool



        Summary
        	Load the gridded weight density into image weighting generation  

        Description

             Load the gridded weight density into image weighting; useful in parallel when weight density is combined into one image and loaded in each process. if no imagename is passed the imagename.weight is loaded 


        Input Parameters:
        	type		 name of image holding combined weight density 

        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_setweightdensity(self, *args, **kwargs)


    def done(self):
        """
        done(self) -> bool



        Summary
        	Close the tool

        Description


        --------------------------------------------------------------------------------

        """
        return _synthesisimager.synthesisimager_done(self)

synthesisimager_swigregister = _synthesisimager.synthesisimager_swigregister
synthesisimager_swigregister(synthesisimager)

# This file is compatible with both classic and new-style classes.

