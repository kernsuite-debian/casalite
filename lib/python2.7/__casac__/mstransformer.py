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
        mname = '.'.join((pkg, '_mstransformer')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_mstransformer')
    _mstransformer = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_mstransformer', [dirname(__file__)])
        except ImportError:
            import _mstransformer
            return _mstransformer
        if fp is not None:
            try:
                _mod = imp.load_module('_mstransformer', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _mstransformer = swig_import_helper()
    del swig_import_helper
else:
    import _mstransformer
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

class mstransformer(_object):
    """Proxy of C++ casac::mstransformer class."""

    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, mstransformer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, mstransformer, name)
    __repr__ = _swig_repr
    __swig_destroy__ = _mstransformer.delete_mstransformer
    __del__ = lambda self: None

    def __init__(self):
        """__init__(self) -> mstransformer"""
        this = _mstransformer.new_mstransformer()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this

    def done(self):
        """
        done(self) -> bool



        Summary
        	Destroy the mstransformer tool
        Example:

        mt.done()


        --------------------------------------------------------------------------------

        """
        return _mstransformer.mstransformer_done(self)


    def config(self, *args, **kwargs):
        """
        config(self, pars) -> bool



        Summary
        	Configure the mstransformer tool.

        Input Parameters:
        	pars		 The record (dictionary) pars must contain at least the input MS name and output MS name. Other parameters that can go in the dictionary are the MS data selection parameters such as: spw, scan, antenna, field, state, correlation, array, uvrange, timerange, observation and any of the transformation parameters. This function can be run again to change the current parameters or add new ones. For the full list of parameters, please see help mstransform. Example: myparams = {'inputms':'myfile.ms', 'outputms':'myout.ms', 'datacolumn':'DATA', 'spw':'0,1,2', 'combinespws':True} 

        Example:

        mt.config(pars)

        --------------------------------------------------------------------------------

        """
        return _mstransformer.mstransformer_config(self, *args, **kwargs)


    def open(self):
        """
        open(self) -> bool



        Summary
        	Open the MS and select the data

        Description
        	It assumes that mt.config() was run before.
        Example:

        mt.open()

        --------------------------------------------------------------------------------

        """
        return _mstransformer.mstransformer_open(self)


    def run(self):
        """
        run(self) -> record *



        Summary
        	Execute the mstransformer tool and apply the transformations

        Description

        Execute the tool and apply the transformations.

        Example:

        mt.run()

        --------------------------------------------------------------------------------

        """
        return _mstransformer.mstransformer_run(self)


    def mergespwtables(self, *args, **kwargs):
        """
        mergespwtables(self, filenames) -> bool



        Summary
        	Merge the spw sub-tables of a list of subMSs.

        Description

                      Merge the spw sub-tables of a list of subMSs.


        Input Parameters:
        	filenames	 List of tables/MS names. 

        Example:

        mt.mergespwtables([])

        --------------------------------------------------------------------------------

        """
        return _mstransformer.mstransformer_mergespwtables(self, *args, **kwargs)

mstransformer_swigregister = _mstransformer.mstransformer_swigregister
mstransformer_swigregister(mstransformer)

# This file is compatible with both classic and new-style classes.

