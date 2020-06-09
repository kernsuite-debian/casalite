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
import task_slsearch
def slsearch(tablename='', outfile='', freqrange=[84, 90], species=[''], reconly=False, chemnames=[''], qns=[''], intensity=[-1], smu2=[-1], loga=[-1], el=[-1], eu=[-1], rrlinclude=True, rrlonly=False, verbose=False, logfile='""', append=False):

        """Search a spectral line table.

PARAMETER SUMMARY

tablename      Input spectral line table name to search. If not specified, use the default table in the system.
outfile        Results table name. Blank means do not write the table to disk.
freqrange      Frequency range in GHz.
species        Species to search for.
reconly        List only NRAO recommended frequencies.
chemnames      Chemical names to search for.
qns            Resolved quantum numbers to search for.
intensity      CDMS/JPL intensity range. -1 -> do not use an intensity range.
smu2           S*mu*mu range in Debye**2. -1 -> do not use an S*mu*mu range.
loga           log(A) (Einstein coefficient) range. -1 -> do not use a loga range.
el             Lower energy state range in Kelvin. -1 -> do not use an el range.
eu             Upper energy state range in Kelvin. -1 -> do not use an eu range.
rrlinclude     Include RRLs in the result set?
rrlonly        Include only RRLs in the result set?
verbose        List result set to logger (and optionally logfile)?
logfile        List result set to this logfile (only used if verbose=True).
append         If true, append to logfile if it already exists, if false overwrite logfile it it exists. Only used if verbose=True and logfile not blank.

    Search the specfied spectral line table. The results table can be written to disk by specifying its name in the outfile parameter.
    If outfile is not specified (ie outfile=""), no table is created. Because Splatalogue does not have values for intensity, smu2,
    loga, eu, and el for radio recombination lines (rrls), one must specify to include RRLs in the specified frequency range in the
    output. In this case, RRLs will be included ignoring any filters on intensity, smu2, loga, eu, and el. One can also specify to
    list only RRLs. One can specify to list the search results to the logger via the verbose parameter. If verbose is False, no
    logger output is listed. If verbose=True, one can also specify that the results be listed to a logfile and if this file already
    exists, one can specify that the results be appended to it or to overwrite it with the results.
    
    # put search results in a table but do not list to the logger
    slsearch("myspectrallines.tbl", verbose=False)


        """
        if type(freqrange)==float: freqrange=[freqrange]
        if type(species)==str: species=[species]
        if type(chemnames)==str: chemnames=[chemnames]
        if type(qns)==str: qns=[qns]
        if type(intensity)==float: intensity=[intensity]
        if type(smu2)==float: smu2=[smu2]
        if type(loga)==float: loga=[loga]
        if type(el)==float: el=[el]
        if type(eu)==float: eu=[eu]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['tablename'] = tablename
        mytmp['outfile'] = outfile
        mytmp['freqrange'] = freqrange
        mytmp['species'] = species
        mytmp['reconly'] = reconly
        mytmp['chemnames'] = chemnames
        mytmp['qns'] = qns
        mytmp['intensity'] = intensity
        mytmp['smu2'] = smu2
        mytmp['loga'] = loga
        mytmp['el'] = el
        mytmp['eu'] = eu
        mytmp['rrlinclude'] = rrlinclude
        mytmp['rrlonly'] = rrlonly
        mytmp['verbose'] = verbose
        mytmp['logfile'] = logfile
        mytmp['append'] = append
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'slsearch.xml')

        casalog.origin('slsearch')
        if trec.has_key('slsearch') and casac.utils().verify(mytmp, trec['slsearch']) :
            result = task_slsearch.slsearch(tablename, outfile, freqrange, species, reconly, chemnames, qns, intensity, smu2, loga, el, eu, rrlinclude, rrlonly, verbose, logfile, append)

        else :
          result = False
        return result
