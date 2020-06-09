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
        mname = '.'.join((pkg, '_imagemetadata')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_imagemetadata')
    _imagemetadata = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_imagemetadata', [dirname(__file__)])
        except ImportError:
            import _imagemetadata
            return _imagemetadata
        if fp is not None:
            try:
                _mod = imp.load_module('_imagemetadata', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _imagemetadata = swig_import_helper()
    del swig_import_helper
else:
    import _imagemetadata
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

class imagemetadata(_object):
    """Proxy of C++ casac::imagemetadata class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, imagemetadata, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, imagemetadata, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _imagemetadata.delete_imagemetadata
    __del__ = lambda self: None

    def __init__(self):
        """__init__(self) -> imagemetadata"""
        this = _imagemetadata.new_imagemetadata()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def add(self, *args, **kwargs):
        """
        add(self, key, value) -> bool



        Summary
        	Add a key-value pair if possible.

        Description

                Add a key-value pair if possible.


        Input Parameters:
        	key		 The name of the FITS or other keyword. 
        	value		 Associated value to add. 

        Example:

        imd.open('myim.im')
        # add a keyword 'test' with value 'first'
        if add('test', 'first'):
            print 'test=first has been added'
        else:
            print 'Unable to add key test'
        imd.done()

        --------------------------------------------------------------------------------

        """
        return _imagemetadata.imagemetadata_add(self, *args, **kwargs)


    def close(self):
        """
        close(self) -> bool



        Summary
        	Close the image metadata tool. Synonym for done().

        Description


        This function closes the image metadata tool.  This means that it detaches the
        tool from its underlying metadata object. Methods cannot be run on it until it
        is opened with another or the same image.


        Example:


        imd.open('myim.im')
        # do stuff
        imd.close()


        --------------------------------------------------------------------------------

        """
        return _imagemetadata.imagemetadata_close(self)


    def done(self):
        """
        done(self) -> bool



        Summary
        	Close the image metadata tool. Synonym for close().

        Description


        This function closes the image metadata tool.  This means that it detaches the
        tool from its underlying metadata object. Methods cannot be run on it until it
        is opened with another or the same image.


        Example:


        imd.open('myim.im')
        # do stuff
        imd.done()


        --------------------------------------------------------------------------------

        """
        return _imagemetadata.imagemetadata_done(self)


    def get(self, *args, **kwargs):
        """
        get(self, key) -> variant *



        Summary
        	Get the value associated with the specified, case-insensitive FITS keyword.

        Description

                Get the value associated with the specified, case-insensitive FITS keyword.


        Input Parameters:
        	key		 The name of the FITS or other keyword. 

        Example:

        imd.open('myim.im')
        imtype = imd.get('imtype')
        imd.done()

        --------------------------------------------------------------------------------

        """
        return _imagemetadata.imagemetadata_get(self, *args, **kwargs)


    def list(self, verbose=True):
        """
        list(self, verbose=True) -> record *



        Summary
        	Get a dictionary of FITS-like header items.

        Description

                Get a listing of traditional FITS-like 'header' items.


        Input Parameters:
        	verbose		 If true, print listing to logger true 

        Example:

        imd.open('myim.im')
        mylist = imd.list(False)
        imd.done()
        crval1 = mylist{'crval1'}

        --------------------------------------------------------------------------------

        """
        return _imagemetadata.imagemetadata_list(self, verbose)


    def open(self, infile):
        """
        open(self, infile) -> bool



        Summary
        	Open this image metadata tool providing access to an image's metadata.

        Description


        This method creates access to the specified image's metadata.



        Input Parameters:
        	infile		 Image name. The image can be in any \casa\ supported format. 

        Example:


        immd.open('myim.im')
        # do stuff with the tool and then close it.
        immd.done()


        --------------------------------------------------------------------------------

        """
        return _imagemetadata.imagemetadata_open(self, infile)


    def remove(self, *args, **kwargs):
        """
        remove(self, key, value) -> bool



        Summary
        	Remove or clear the value of a keyword if possible.

        Description

                Remove or clear the value of a keyword if possible. If key='masks', a value specifying the mask
                to remove may be specified. If no value is specified, all masks are removed.


        Input Parameters:
        	key		 The name of the FITS or other keyword. 
        	value		 Value to remove if the key is multi-valued. Only used in the case of key='masks'. 

        Example:

        imd.open('myim.im')
        # clear the brightness unit
        if imd.remove('bunit'):
            print 'bunit has been cleared'
        else:
            print 'Unable to clear bunit'
        imd.done()

        --------------------------------------------------------------------------------

        """
        return _imagemetadata.imagemetadata_remove(self, *args, **kwargs)


    def set(self, *args, **kwargs):
        """
        set(self, key, value) -> bool



        Summary
        	Set a keyword to the specified value if possible.

        Description

                Set a key-value pair if possible.


        Input Parameters:
        	key		 The name of the FITS or other keyword. 
        	value		 Associated value to set. 

        Example:


            Note that when setting the reference value of a polarizaiton axis, one must
            provide an array of stokes/polarization strings (['I', 'Q', 'XX']) that is the
            same length as the stokes axis. If the stokes axis is degenerate, one can alternatively
            provide a string indicating the stokes value.

        imd.open('myim.im')
        # Set keyword 'telescope' with value 'Argus Array'
        if imd.set('telescope', 'Argus Array'):
            print 'telescope has been updated'
        else:
            print 'Unable to update telescope.'
        imd.done()

        # set polarizations for an image with three pixels on the stokes axis crval3
        imd.open('myim.im')
        if imd.set('crval3', [XY, LL, 'Q']):
            print 'polarization values have been updated'
        else:
            print 'Unable to update polarization values.'
        imd.done()


        --------------------------------------------------------------------------------

        """
        return _imagemetadata.imagemetadata_set(self, *args, **kwargs)

imagemetadata_swigregister = _imagemetadata.imagemetadata_swigregister
imagemetadata_swigregister(imagemetadata)

# This file is compatible with both classic and new-style classes.


