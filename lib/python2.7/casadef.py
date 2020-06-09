import os
task_directory = None
## CASAPATH is the primary environment variable
if os.environ.has_key('CASAPATH'):
    __casapath__ = os.environ['CASAPATH'].split(' ')[0]
    __casaarch__ = os.environ['CASAPATH'].split(' ')[1]
    if os.path.exists(__casapath__ + '/lib/python2.7/casapy.py'):
        task_directory = __casapath__ + '/lib/python2.7'
        python_library_directory = task_directory
    elif os.path.exists(__casapath__ + '/Resources/python/casapy.py'):
        task_directory = __casapath__ + '/Resources/python'
        python_library_directory = task_directory
    elif os.path.exists(__casapath__ + '/' + __casaarch__ + '/python2.7/casapy.py'):
        task_directory = __casapath__ + '/' + __casaarch__ + '/python2.7'
        python_library_directory = task_directory
## if CASAPATH does not yeild any result, check secondary variables...
if task_directory is None:
    if os.environ.has_key('__CASAPY_TASKDIR'):
        task_directory = os.environ['__CASAPY_TASKDIR']
    if os.environ.has_key('__CASAPY_PYTHONDIR'):
        python_library_directory = os.environ['__CASAPY_PYTHONDIR']
casa_version = "5.6.0"
if os.environ.get('CASAVERSION') is not None:
    casa_version = os.environ.get('CASAVERSION')
subversion_revision = "40000"
subversion_date = "Mon Aug  5 14:13:16 2019"
subversion_url = "git"
build_time = "Mon 2019/08/05 18:13:15 UTC"
