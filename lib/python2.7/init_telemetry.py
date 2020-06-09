###
### Telemetry shutdown hook
###
from casa_shutdown import add_shutdown_hook
from telemetry import telemetry
import fnmatch
import os
from casac import casac
import __casac__
import atexit
import datetime

def logShutdown():
    if (casa['state']['telemetry-enabled'] == True):
        casalog.origin("CASAStop")
        casalog.poststat("Stopping CASA at: " + str(datetime.datetime.now()) + " Version " + casa['build']['version'] \
            + " Platform: " + platform.platform() +  " Start time: " + casa['state']['telemetry-starttime'] + " Variant: " + casa['variant'])

casa['state']['telemetry-enabled'] = True

casa_util = __casac__.utils.utils()

rcTelemetryFlag = str.upper(casa_util.getrc("EnableTelemetry"))

# Use the value from casarc file if it is set, otherwise leave it as is
if (rcTelemetryFlag):
    if (rcTelemetryFlag == 'TRUE'):
        casa['state']['telemetry-enabled'] = True
    if (rcTelemetryFlag == 'FALSE'):
        casa['state']['telemetry-enabled'] = False

# Use and environment variable if it is set
if (os.environ.has_key('CASA_ENABLE_TELEMETRY')):
    if (os.environ['CASA_ENABLE_TELEMETRY'].upper( ) == 'TRUE'):
        casa['state']['telemetry-enabled'] = True
    if (os.environ['CASA_ENABLE_TELEMETRY'].upper( ) == 'FALSE'):
        casa['state']['telemetry-enabled'] = False

# Command line telemetry flag is only used to enable telemetry temporarily
if (casa['flags'].telemetry == True):
    casa['state']['telemetry-enabled'] = True

if (casa['state']['telemetry-enabled'] == True):
    atexit.register(logShutdown)
    casatelemetry = telemetry(casa)
