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
import task_uvmodelfit
def uvmodelfit(vis='', field='', spw='', selectdata=True, timerange='', uvrange='', antenna='', scan='', msselect='', niter=5, comptype='P', sourcepar=[1.0, 0.0, 0.0], varypar=[], outfile=''):

        """Fit a single component source model to the uv data

        Fit a single component source model to the uv data.  Three models
        are available: P=point; G=Gaussian; D=Disk.  Fitting parameters can
        be held fixed.   The results are given in the log and placed in a
        components file.

        Keyword arguments:
        vis -- Name of input visibility file 
                default: none; example: vis='ngc5921.ms'
                
        --- Data Selection
        field -- Select data based on field id(s) or name(s)
                default: '' (all); example: field='1'
                field='0~2' # field ids inclusive from 0 to 2
                field='3C*' # all field names starting with 3C
        spw -- Select data based on spectral window
                default: '' (all); example: spw='1'
                spw='<2' #spectral windows less than 2
                spw='>1' #spectral windows greater than 1
        selectdata -- Select a subset of the visibility using MSSelection
                default: False; example: selectdata=True
        timerange  -- Select data based on time range:
                default = '' (all); example,
                timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
                Note: YYYY/MM/DD can be dropped as needed:
                timerange='09:14:0~09:54:0' # this time range
                timerange='09:44:00' # data within one integration of time
                timerange='>10:24:00' # data after this time
                timerange='09:44:00+00:13:00' #data 13 minutes after time
        uvrange -- Select data within uvrange (default units kilo-lambda)
               default: '' (all); example:
               uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lamgda
               uvrange='>4klambda';uvranges greater than 4 kilo lambda
               uvrange='0~1000km'; uvrange in kilometers
        antenna -- Select data based on antenna/baseline
                default: '' (all); example: antenna='5&6' baseline 5-6
                antenna='5&6;7&8' #baseline 5-6 and 7-8
                antenna='5' # all baselines with antenna 5
                antenna='5,6' # all baselines with antennas 5 and 6
        scan -- Select data based on scan number - New, under developement
                default: '' (all); example: scan='>3'
        msselect -- Optional data selection (field,spw,time,etc)
                default:'' means select all; example:msselect='FIELD_ID==0', 
                msselect='FIELD_ID IN [0,1,2]' means select fields 0,1 and 2
                msselect='FIELD_ID <= 1 means select fields 0, 1
                msselect='FIELD_ID==0 && ANTENNA1 IN [0] && ANTENNA2 IN [2:26]'
                   means select field 0 and antennas 0 to 26, except antenna 1.
                Other msselect fields are: 'DATA_DESC_ID', 'SPECTRAL_WINDOW_ID',
                'POLARIZATION_ID', 'SCAN_NUMBER', 'TIME', 'UVW'
                See ccokbook for more details

        niter -- Number of fitting iterations to execute
                default: 5; example: niter=20
        comptype -- component model type
                default: 'P';
                Options: 'P' (point source), 'G' (elliptical gaussian),
                         'D' (elliptical disk)
        sourcepar -- Starting guess for component parameters
                default: [1,0,0];  (for comptype='P')
                IF comptype = 'P' then
                  sourcepar = [flux,xoff,yoff] where
                    flux = Jy, xoff = offset east (arcsec), yoff = offset north (arcsec).
                IF comptype = 'G' or 'D', then
                  sourcepar = [flux,xoff,yoff,majax,axrat,pos] where
                    majax = FWHM along the major axis (arcsec), axrat < 1 is
                    the ratio of minor to major axis, pos=angle in deg
        varypar -- Control which parameters to let vary in the fit
                default: [] (all vary);
                example: vary=[F,T,T]

        examples:

             fit a point:
                comptype = 'P'
                sourcepar = [0.4,0.2,-0.3];
                varypar = [T,T,T]

             fit a circular Gaussian:
                comptype = 'G'
                sourcepar = [1.4,0.3,-0.2,0.3, 1, 0]
                varypar    = [ T , T ,  T , T , F, F]
                    

        outfile -- Optional output component list table
                default: ''; example: outfile='componentlist.cl'


        How to get the output values:

            cl.open('componentlist.cl')
            fit = cl.getcompoent()             stores component information
            fit                                to see the whole mess
            flux = fit['flux']['value']        to store the I,Q,U,V, flux
            print flux

            ra = fit['shape']['direction']['m0']['value']
            dec =fit['shape']['direction']['m1']['value']
            print ra, dec

            bmaj = fit['shape']['majoraxis']['value']     to get major axis
            bmin = fit['shape']['minoraxis']['value']     to get minor axis
            


        """
        if type(sourcepar)==float: sourcepar=[sourcepar]
        if type(varypar)==bool: varypar=[varypar]

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['selectdata'] = selectdata
        mytmp['timerange'] = timerange
        mytmp['uvrange'] = uvrange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['msselect'] = msselect
        mytmp['niter'] = niter
        mytmp['comptype'] = comptype
        mytmp['sourcepar'] = sourcepar
        mytmp['varypar'] = varypar
        mytmp['outfile'] = outfile
        pathname='file://' + xmlpath( ) + '/'
        trec = casac.utils().torecord(pathname+'uvmodelfit.xml')

        casalog.origin('uvmodelfit')
        if trec.has_key('uvmodelfit') and casac.utils().verify(mytmp, trec['uvmodelfit']) :
            result = task_uvmodelfit.uvmodelfit(vis, field, spw, selectdata, timerange, uvrange, antenna, scan, msselect, niter, comptype, sourcepar, varypar, outfile)

        else :
          result = False
        return result
