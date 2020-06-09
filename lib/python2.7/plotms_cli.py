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
from task_plotms import plotms
class plotms_cli_:
    __name__ = "plotms"
    rkey = None
    i_am_a_casapy_task = None
    # The existence of the i_am_a_casapy_task attribute allows help()
    # (and other) to treat casapy tasks as a special case.

    def __init__(self) :
       self.__bases__ = (plotms_cli_,)
       self.__doc__ = self.__call__.__doc__

       self.parameters={'vis':None, 'gridrows':None, 'gridcols':None, 'rowindex':None, 'colindex':None, 'plotindex':None, 'xaxis':None, 'xdatacolumn':None, 'xframe':None, 'xinterp':None, 'yaxis':None, 'ydatacolumn':None, 'yframe':None, 'yinterp':None, 'yaxislocation':None, 'selectdata':None, 'field':None, 'spw':None, 'timerange':None, 'uvrange':None, 'antenna':None, 'scan':None, 'correlation':None, 'array':None, 'observation':None, 'intent':None, 'feed':None, 'msselect':None, 'averagedata':None, 'avgchannel':None, 'avgtime':None, 'avgscan':None, 'avgfield':None, 'avgbaseline':None, 'avgantenna':None, 'avgspw':None, 'scalar':None, 'transform':None, 'freqframe':None, 'restfreq':None, 'veldef':None, 'shift':None, 'extendflag':None, 'extcorr':None, 'extchannel':None, 'iteraxis':None, 'xselfscale':None, 'yselfscale':None, 'xsharedaxis':None, 'ysharedaxis':None, 'customsymbol':None, 'symbolshape':None, 'symbolsize':None, 'symbolcolor':None, 'symbolfill':None, 'symboloutline':None, 'coloraxis':None, 'customflaggedsymbol':None, 'flaggedsymbolshape':None, 'flaggedsymbolsize':None, 'flaggedsymbolcolor':None, 'flaggedsymbolfill':None, 'flaggedsymboloutline':None, 'xconnector':None, 'timeconnector':None, 'plotrange':None, 'title':None, 'titlefont':None, 'xlabel':None, 'xaxisfont':None, 'ylabel':None, 'yaxisfont':None, 'showmajorgrid':None, 'majorwidth':None, 'majorstyle':None, 'majorcolor':None, 'showminorgrid':None, 'minorwidth':None, 'minorstyle':None, 'minorcolor':None, 'showlegend':None, 'legendposition':None, 'plotfile':None, 'expformat':None, 'verbose':None, 'exprange':None, 'highres':None, 'dpi':None, 'width':None, 'height':None, 'overwrite':None, 'showgui':None, 'clearplots':None, 'callib':None, 'headeritems':None, 'showatm':None, 'showtsky':None, 'showimage':None, }


    def result(self, key=None):
            #### and add any that have completed...
            return None


    def __call__(self, vis=None, gridrows=None, gridcols=None, rowindex=None, colindex=None, plotindex=None, xaxis=None, xdatacolumn=None, xframe=None, xinterp=None, yaxis=None, ydatacolumn=None, yframe=None, yinterp=None, yaxislocation=None, selectdata=None, field=None, spw=None, timerange=None, uvrange=None, antenna=None, scan=None, correlation=None, array=None, observation=None, intent=None, feed=None, msselect=None, averagedata=None, avgchannel=None, avgtime=None, avgscan=None, avgfield=None, avgbaseline=None, avgantenna=None, avgspw=None, scalar=None, transform=None, freqframe=None, restfreq=None, veldef=None, shift=None, extendflag=None, extcorr=None, extchannel=None, iteraxis=None, xselfscale=None, yselfscale=None, xsharedaxis=None, ysharedaxis=None, customsymbol=None, symbolshape=None, symbolsize=None, symbolcolor=None, symbolfill=None, symboloutline=None, coloraxis=None, customflaggedsymbol=None, flaggedsymbolshape=None, flaggedsymbolsize=None, flaggedsymbolcolor=None, flaggedsymbolfill=None, flaggedsymboloutline=None, xconnector=None, timeconnector=None, plotrange=None, title=None, titlefont=None, xlabel=None, xaxisfont=None, ylabel=None, yaxisfont=None, showmajorgrid=None, majorwidth=None, majorstyle=None, majorcolor=None, showminorgrid=None, minorwidth=None, minorstyle=None, minorcolor=None, showlegend=None, legendposition=None, plotfile=None, expformat=None, verbose=None, exprange=None, highres=None, dpi=None, width=None, height=None, overwrite=None, showgui=None, clearplots=None, callib=None, headeritems=None, showatm=None, showtsky=None, showimage=None, ):

        """A plotter/interactive flagger for visibility data.

        Detailed Description:


                Task for plotting and interacting with visibility data and
                calibration tables.

                Plotms provides a variety of axis choices (including data column)
                along with selection, averaging, and transformation options for
                MeasurementSets.  Flag extension parameters are also available for
                interactive flagging operations in the plotter.
        
                All of the provided parameters can also be set using the GUI once
                the application has been launched or through the plotms tool (pm).

                Most of the basic plotms functions will work for calibration tables.
                The correlation selection string may be used to select polarization
                in a cal table, including ratio plots ("/").  The antenna selection
                string is used to select antenna1 only, rather than baselines as in
                an MS. When plotting parameterized CalTables, such as delays, antpos,
                gaincurve, or opacity, plotms will currently just plot the simple
                parameters contained in the table, not the effective amplitudes or
                phases sampled at observing times, frequencies etc.  BPOLY and
                GSPLINE tables are supported but interactive flagging is not allowed.
                Features currently unsupported for CalTables include averaging,
                transformations (velocity conversions, etc.), and some axis and
                selection options which do not exist in these tables. In the plotms
                GUI, many options irrelevant for CalTables are not hidden when
                interacting with a CalTable, and such settings will be ignored (when
                benign) or cause an error message.
        

        Arguments :
                vis: Input MS or CalTable (blank for none)
                   Default Value: 

                gridrows: Number of subplot rows
                   Default Value: 1

                gridcols: Number of subplot columns
                   Default Value: 1

                rowindex: Row location of the plot (0-based)
                   Default Value: 0

                colindex: Column location of the plot (0-based)
                   Default Value: 0

                plotindex: Index to address a subplot (0-based)
                   Default Value: 0

                xaxis: Plot x-axis (blank for default/current)
                   Default Value: 
                   Allowed Values:
                                
                                scan
                                Scan
                                field
                                Field
                                time
                                Time
                                interval
                                time_interval
                                timeinterval
                                timeint
                                Interval
                                spw
                                Spw
                                channel
                                chan
                                Channel
                                frequency
                                freq
                                Frequency
                                correlation
                                corr
                                Corr
                                antenna1
                                ant1
                                Antenna1
                                antenna2
                                ant2
                                Antenna2
                                baseline
                                Baseline
                                row
                                Row
                                observation
                                Observation
                                intent
                                Intent
                                feed1
                                Feed1
                                feed2
                                Feed2
                                uvdist
                                UVdist
                                uvwave
                                uvdist_l
                                uvdistl
                                UVwave
                                u
                                U
                                v
                                V
                                w
                                W
                                uwave
                                Uwave
                                vwave
                                Vwave
                                wwave
                                Wwave
                                velocity
                                vel
                                Velocity
                                amp
                                amplitude
                                Amp
                                phase
                                Phase
                                real
                                Real
                                imag
                                imaginary
                                Imag
                                wt
                                Wt
                                weight
                                wt*amp
                                Wt*Amp
                                wtsp
                                WtSp
                                weightspectrum
                                WeightSpectrum
                                sigma
                                Sigma
                                sigmasp
                                SigmaSp
                                sigmaspectrum
                                SigmaSpectrum
                                flag
                                Flag
                                azimuth
                                Azimuth
                                elevation
                                Elevation
                                hourang
                                hourangle
                                HourAngle
                                parang
                                parangle
                                parallacticangle
                                ParAngle
                                antenna
                                ant
                                Antenna
                                ant-azimuth
                                Ant-Azimuth
                                ant-elevation
                                Ant-Elevation
                                ant-ra
                                Ant-RA
                                ant-dec
                                Ant-DEC
                                ant-parang
                                ant-parangle
                                ant-parallacticangle
                                Ant-Parangle
                                flagrow
                                FlagRow
                                gainamp
                                gamp
                                GainAmp
                                gainphase
                                gphase
                                GainPhase
                                gainreal
                                greal
                                GainReal
                                gainimag
                                gimag
                                GainImag
                                delay
                                del
                                Delay
                                swp
                                swpower
                                switchedpower
                                SwPower
                                spgain
                                tsys
                                Tsys
                                opac
                                opacity
                                Opac
                                snr
                                SNR
                                tec
                                TEC
                                antpos
                                Antenna Positions
                                antenna positions
                                radialvelocity
                                Radial Velocity
                                rho
                                Distance

                xdatacolumn: Data column to use for x-axis (blank for default/current).  Note that unspecified residuals are complex (vector) differences or ratios.
                   Default Value: 
                   Allowed Values:
                                
                                data
                                corrected
                                model
                                float
                                residual
                                corrected-model
                                corrected-model_vector
                                corrected-model_scalar
                                data-model
                                data-model_vector
                                data-model_scalar
                                corrected/model
                                corrected/model_vector
                                corrected/model_scalar
                                data/model
                                data/model_vector
                                data/model_scalar

                xframe: Coordinate frame to use for x-axis
                   Default Value: 
                   Allowed Values:
                                
                                icrs
                                j2000
                                b1950
                                galactic
                                azelgeo

                xinterp: Interpolation method for x-axis
                   Default Value: 
                   Allowed Values:
                                
                                nearest
                                cubic spline
                                spline

                yaxis: Plot y-axis (blank for default/current)
                   Default Value:  
                   Allowed Values:
                                
                                scan
                                Scan
                                field
                                Field
                                time
                                Time
                                interval
                                time_interval
                                timeinterval
                                timeint
                                Interval
                                spw
                                Spw
                                channel
                                chan
                                Channel
                                frequency
                                freq
                                Frequency
                                correlation
                                corr
                                Corr
                                antenna1
                                ant1
                                Antenna1
                                antenna2
                                ant2
                                Antenna2
                                baseline
                                Baseline
                                row
                                Row
                                observation
                                Observation
                                intent
                                Intent
                                feed1
                                Feed1
                                feed2
                                Feed2
                                uvdist
                                UVdist
                                uvwave
                                uvdist_l
                                uvdistl
                                UVwave
                                u
                                U
                                v
                                V
                                w
                                W
                                uwave
                                Uwave
                                vwave
                                Vwave
                                wwave
                                Wwave
                                velocity
                                vel
                                Velocity
                                amp
                                amplitude
                                Amp
                                phase
                                Phase
                                real
                                Real
                                imag
                                imaginary
                                Imag
                                wt
                                Wt
                                weight
                                wt*amp
                                Wt*Amp
                                wtsp
                                WtSp
                                weightspectrum
                                WeightSpectrum
                                sigma
                                Sigma
                                sigmasp
                                SigmaSp
                                sigmaspectrum
                                SigmaSpectrum
                                flag
                                Flag
                                azimuth
                                Azimuth
                                elevation
                                Elevation
                                hourang
                                hourangle
                                HourAngle
                                parang
                                parangle
                                parallacticangle
                                ParAngle
                                antenna
                                ant
                                Antenna
                                ant-azimuth
                                Ant-Azimuth
                                ant-elevation
                                Ant-Elevation
                                ant-ra
                                Ant-RA
                                ant-dec
                                Ant-DEC
                                ant-parang
                                ant-parangle
                                ant-parallacticangle
                                Ant-Parangle
                                flagrow
                                FlagRow
                                gainamp
                                gamp
                                GainAmp
                                gainphase
                                gphase
                                GainPhase
                                gainreal
                                greal
                                GainReal
                                gainimag
                                gimag
                                GainImag
                                delay
                                del
                                Delay
                                swp
                                swpower
                                switchedpower
                                SwPower
                                spgain
                                tsys
                                Tsys
                                opac
                                opacity
                                Opac
                                snr
                                SNR
                                tec
                                TEC
                                antpos
                                Antenna Positions
                                antenna positions
                                radialvelocity
                                Radial Velocity
                                rho
                                Distance
                                ra
                                RA
                                Right Ascension

                ydatacolumn: Data column to use for y-axis (blank for default/current). Note that unspecified residuals are complex (vector) differences or ratios.
                   Default Value: 
                   Allowed Values:
                                
                                data
                                corrected
                                model
                                float
                                residual
                                corrected-model
                                corrected-model_vector
                                corrected-model_scalar
                                data-model
                                data-model_vector
                                data-model_scalar
                                corrected/model
                                corrected/model_vector
                                corrected/model_scalar
                                data/model
                                data/model_vector
                                data/model_scalar

                yframe: Coordinate frame to use for y-axis
                   Default Value: 
                   Allowed Values:
                                
                                icrs
                                j2000
                                b1950
                                galactic
                                azelgeo

                yinterp: Interpolation method for y-axis
                   Default Value: 
                   Allowed Values:
                                
                                nearest
                                cubic spline
                                spline

                yaxislocation: Location of the y-axis (blank for default: left)
                   Default Value: 
                   Allowed Values:
                                
                                left
                                right

                selectdata: Enable data selection parameters
                   Default Value: True

                field: Field names or ids (blank for all)
                   Default Value: 

                spw: Spectral windows:channels (blank for all)
                   Default Value: 

                timerange: Time range (blank for all)
                   Default Value: 

                uvrange: UV range (blank for all)
                   Default Value: 

                antenna: Baseline/antenna names or ids (blank for all)
                   Default Value: 

                scan: Scan numbers (blank for all)
                   Default Value: 

                correlation: Correlations/polarizations (blank for all)
                   Default Value: 

                array: (Sub)array numbers (blank for all)
                   Default Value: 

                observation: Observation IDs (blank for all)
                   Default Value: 

                intent: Observing intent (blank for all)
                   Default Value: 

                feed: Feed numbers (blank for all)
                   Default Value: 

                msselect: MSSelection TaQL string (blank for none)
                   Default Value: 

                averagedata: Enable data averaging parameters
                   Default Value: True

                avgchannel: Average over channel (blank = False, otherwise value in channels)
                   Default Value: 

                avgtime: Average over time (blank = False, otherwise value in seconds)
                   Default Value: 

                avgscan: Average over scans. Only valid with time averaging
                   Default Value: False

                avgfield: Average over fields. Only valid with time averaging
                   Default Value: False

                avgbaseline: Average over all baselines (mutually exclusive with avgantenna)
                   Default Value: False

                avgantenna: Average per antenna (mutually exclusive with avgbaseline)
                   Default Value: False

                avgspw: Average over all spectral windows
                   Default Value: False

                scalar: Scalar averaging (False=vector averaging)
                   Default Value: False

                transform: Enable data transformations
                   Default Value: True

                freqframe: The frame in which to render frequency and velocity axes
                   Default Value: 
                   Allowed Values:
                                
                                LSRK
                                LSRD
                                BARY
                                GEO
                                TOPO
                                GALACTO
                                LGROUP
                                CMB

                restfreq: Rest frequency to use for velocity conversions 
                   Default Value: 

                veldef: The definition in which to render velocity 
                   Default Value: RADIO
                   Allowed Values:
                                RADIO
                                OPTICAL
                                TRUE

                shift: Adjust phases by this approximate phase center shift [dx,dy] (arcsec)
                   Default Value: 
           0.0
           0.0
       

                extendflag: Extend flagging to other data points not plotted
                   Default Value: False

                extcorr: Extend flags based on correlation 
                   Default Value: False

                extchannel: Extend flags based on channel
                   Default Value: False

                iteraxis: The axis over which to iterate
                   Default Value: 
                   Allowed Values:
                                
                                scan
                                Scan
                                field
                                Field
                                spw
                                Spw
                                baseline
                                Baseline
                                antenna
                                Antenna
                                time
                                Time
                                corr
                                Corr

                xselfscale: When True, iterated plots have a common x-axis range (scale).
                   Default Value: False

                yselfscale: When True, iterated plots have a common y-axis range (scale).
                   Default Value: False

                xsharedaxis: Iterated plots on a grid share a common external x-axis per column. Must also set xselfscale=True and gridrows>1.
                   Default Value: False

                ysharedaxis: Iterated plots on a grid share a common external y-axis per row. Must also set yselfscale=True and gridcols>1.
                   Default Value: False

                customsymbol: Enable custom symbol(s) for unflagged points
                   Default Value: False

                symbolshape: Shape of plotted unflagged symbols
                   Default Value: autoscaling
                   Allowed Values:
                                nosymbol
                                autoscaling
                                circle
                                square
                                diamond
                                pixel

                symbolsize: Size of plotted unflagged symbols
                   Default Value: 2

                symbolcolor: Color (name or hex code) of plotted unflagged symbols
                   Default Value: 0000ff

                symbolfill: Fill type of plotted unflagged symbols
                   Default Value: fill
                   Allowed Values:
                                fill
                                mesh1
                                mesh2
                                mesh3
                                nofill

                symboloutline: Outline plotted unflagged symbols
                   Default Value: False

                coloraxis: Selects data axis for colorizing
                   Default Value: 
                   Allowed Values:
                                
                                scan
                                Scan
                                field
                                Field
                                spw
                                Spw
                                antenna1
                                ant1
                                Antenna1
                                antenna2
                                ant2
                                Antenna2
                                baseline
                                Baseline
                                channel
                                chan
                                Channel
                                corr
                                Corr
                                time
                                Time
                                observation
                                Observation
                                intent
                                Intent

                customflaggedsymbol: Enable custom symbol(s) for flagged points
                   Default Value: False

                flaggedsymbolshape: Shape of plotted flagged symbols
                   Default Value: circle
                   Allowed Values:
                                nosymbol
                                autoscaling
                                circle
                                square
                                diamond
                                pixel

                flaggedsymbolsize: Size of plotted flagged symbols
                   Default Value: 2

                flaggedsymbolcolor: Color (name or hex code) of plotted flagged symbols
                   Default Value: ff0000

                flaggedsymbolfill: Fill type of plotted flagged symbols
                   Default Value: fill
                   Allowed Values:
                                fill
                                mesh1
                                mesh2
                                mesh3
                                nofill

                flaggedsymboloutline: Outline plotted flagged symbols
                   Default Value: False

                xconnector: Set connector for data points (blank="none"; "line","step")
                   Default Value: 
                   Allowed Values:
                                
                                none
                                line
                                step

                timeconnector: Connect points by time rather than x-axis
                   Default Value: False

                plotrange: Plot axes ranges: [xmin,xmax,ymin,ymax]
                   Default Value: 

                title: Title at top of plot
                   Default Value: 

                titlefont: Font size for plot title
                   Default Value: 0

                xlabel: Text for horizontal x-axis. Blank for default.
                   Default Value: 

                xaxisfont: Font size for x-axis label
                   Default Value: 0

                ylabel: Text for vertical y-axis. Blank for default.
                   Default Value: 

                yaxisfont: Font size for y-axis label
                   Default Value: 0

                showmajorgrid: Show major grid lines
                   Default Value: False

                majorwidth: Line width in pixels of major grid lines
                   Default Value: 1

                majorstyle: Major grid line style
                   Default Value: 
                   Allowed Values:
                                
                                solid
                                dash
                                dot
                                none

                majorcolor: Color (name or hex code) of major grid lines
                   Default Value: B0B0B0

                showminorgrid: Show minor grid lines
                   Default Value: False

                minorwidth: Line width in pixels of minor grid lines
                   Default Value: 1

                minorstyle: Minor grid line style
                   Default Value: 
                   Allowed Values:
                                
                                solid
                                dash
                                dot
                                none

                minorcolor: Color (name or hex code) of minor grid lines
                   Default Value: D0D0D0

                showlegend: Show a legend on the plot.
                   Default Value: False

                legendposition: Legend position, default upperRight.
                   Default Value: 
                   Allowed Values:
                                
                                upperRight
                                upperLeft
                                lowerRight
                                lowerLeft
                                exteriorRight
                                exteriorLeft
                                exteriorTop
                                exteriorBottom

                plotfile: Name of plot file to save automatically
                   Default Value: 

                expformat: Export format type. If not provided, plotfile extension will be used to determine type.
                   Default Value: 
                   Allowed Values:
                                
                                jpg
                                png
                                pdf
                                ps
                                txt

                verbose: Include metadata in text export
                   Default Value: True

                exprange: Range of iteration plots to export, one plotfile per page.  Multipage pdf exports are not supported.
                   Default Value: 
                   Allowed Values:
                                
                                current
                                all

                highres: Use high resolution
                   Default Value: False

                dpi: DPI of exported plot
                   Default Value: -1

                width: Width in pixels of exported plot
                   Default Value: -1

                height: Height in pixels of exported plot
                   Default Value: -1

                overwrite: Overwrite plot file if it already exists
                   Default Value: False

                showgui: Show GUI
                   Default Value: True

                clearplots: Remove any existing plots so new ones can replace them.
                   Default Value: True

                callib: Calibration library string or filename for on-the-fly calibration.
                   Default Value: 

                headeritems: Comma-separated list of pre-defined page header items.
                   Default Value: 

                showatm: Compute and overlay the atmospheric transmission curve
                   Default Value: False

                showtsky: Compute and overlay the sky temperature curve
                   Default Value: False

                showimage: Compute and overlay the image sideband curve
                   Default Value: False

        Returns: void

        Example :


        Task for plotting and interacting with visibility
        data.  Limited support for caltable plotting is also
        included as of CASA v4.1.

        A variety of axes choices (including data column) along 
        with MS selection and averaging options are provided for data 
        selection.  Flag extension parameters are also available for
        flagging operations in the plotter.
        
        All of the provided parameters can also be set using the GUI once
        the application has been launched.  Additional and more specific
        operations are available through the GUI and/or through the plotms
        tool (pm).

        Most basic functions (plotting, iteration, locate, flagging)
        will work for most CalTables. Parameterized CalTables
        (delays, antpos, gaincurve, opacity), will, at best, currently 
        just plot the simple parameters contained in the
        table, not the effective amplitudes or phases sampled at
        observing times, frequencies etc.  BPOLY and GSPLINE tables
        are not yet supported.   Features currently unsupported for
        CalTables include Averaging, Transformations (velocity 
        conversions, etc.), and some details of selection (channel and 
        polarization selection are not yet enabled) and axes choices 
        (geometry options are not yet enabled).  In the plotms gui,
        many options irrelevant for CalTables are not yet hidden when
        interacting with a CalTable, and such settings will be ignored
        (when benign) or cause an error message.

    Keyword arguments:
    vis -- input MS or CalTable
           default: ''  (will merely launch the gui)
    gridrows -- Number of subplot rows
                    default: 1 
    gridcols -- Number of subplot columns
                    default: 1
    rowindex -- Row location of the subplot (0-based).
                    default: 0
    colindex -- Column location of the subplot (0-based).
                    default: 0
    plotindex -- Index to address a subplot (0-based). 
                    default: 0                         
    xaxis, yaxis -- what to plot on the two axes
                    default: '' (defaults are xaxis='time',
                                 yaxis='amp' on first execution;
                                 thereafter the most recent
                                 settings are used)
              valid options (=indicates valid synonyms): 
               MS Ids and other meta info:
                 'scan'   (number)
                 'field'  (index)
                 'time',  
                 'interval'='timeint'='timeinterval'='time_interval'
                 'spw'    (index)
                 'chan'='channel'    (index)  
                 'freq'='frequency'  (GHz)
                 'vel'='velocity'   (km/s)
                 'corr'='correlation'  (index)
                 'ant1'='antenna1'   (index)
                 'ant2'='antenna2'   (index)
                 'baseline'  (a baseline index) 
                 'row'   (absoute row Id from the MS)
                 'observation' (index)
                 'intent'      (index)
                 'feed1'       (index)
                 'feed2'       (index)
               Visibility values, flags:
                 'amp'='amplitude'
                 'phase'  (deg)
                 'real'  
                 'imag'='imaginary'
                 'wt'='weight'  (unchannelized)
                 'wtsp'='weightspectrum'
                 'flag'
                 'flagrow'
               Observational geometry:
                 'uvdist'  (meters)
                 'uvwave'='uvdistl'='uvdist_l'  (wavelengths, per channel)
                 'u'  (meters)
                 'v'  (meters)
                 'w'  (meters)
                 'uwave'  ('u' in wavelengths, per channel)
                 'vwave'  ('v' in wavelengths, per channel)
                 'wwave'  ('w' in wavelengths, per channel)
                 'azimuth'  (at array reference; degrees)
                 'elevation'  (at array reference; degrees)
                 'hourang'='hourangle'  (at array reference; hours)
                 'parang'='parangle'='parallacticangle'  (at array reference; degrees)
               Antenna-based (only works vs. data Ids):
                 'ant'='antenna'
                 'ant-azimuth' 
                 'ant-elevation'
                 'ant-ra'
                 'ant-dec'
                 'ant-parang'='ant-parangle'
               Calibration:
                 'gainamp'='gamp'
                 'gainphase'='gphase'
                 'gainreal'='greal'
                 'gainimag'='gimag'
                 'delay'='del'
                 'opacity'='opac'
                 'swpower'='swp'='switchedpower'='spgain'


      >>> xaxis, yaxis expandable parameters
        xdatacolumn, 
        ydatacolumn  -- data column to use for Visibility values:
                        default: '' ('data' on first execution;
                                     thereafter the most recent
                                     setting is used)
                        valid options:  'data'      (observed)
                                        'corrected'='corr'
                                        'model'
                                        'residual'  (aliases 'corrected-model')
                                        'corrected-model'
                                        'data-model'
                                        'data/model'
                                        'corected/model'
                                        'float'
                        Note that residuals are complex (vector) differences or ratios.
    
    selectdata -- data selection parameters flag
                  default: True  (reveals data selection parameters
                                  described below)
                  Consult listobs output for data selection values,
                  and see help par.selectdata for more detailed 
                  information on syntax; also, visit
                  http://casa.nrao.edu/other_doc.shtml and click
                  on "Measurement Set selection syntax" for more
                  tips on using data selection parameters in CASA)

      >>> selectdata expandable parameters:

      field -- Select field using field id(s) or field name(s).
              default: ''=all fields
              If field string is a non-negative integer, it is assumed a
                field index,  otherwise, it is assumed a field name
              field='0~2'; field ids 0,1,2
              field='0,4,5~7'; field ids 0,4,5,6,7
              field='3C286,3C295'; field named 3C286 and 3C295
              field = '3,4C*'; field id 3, all names starting with 4C
      spw -- Select spectral window/channels
               type 'help par.selection' for more examples.
             spw='0~2,4'; spectral windows 0,1,2,4 (all channels)
             spw='<2';  spectral windows less than 2 (i.e. 0,1)
             spw='0:5~61'; spw 0, channels 5 to 61, INCLUSIVE
             spw='*:5~61'; all spw with channels 5 to 61
             spw='0,10,3:3~45'; spw 0,10 all channels, spw 3, channels 3 to 45.
             spw='0~2:2~6'; spw 0,1,2 with channels 2 through 6 in each.
             spw='0:0~10;15~60'; spectral window 0 with channels 0-10,15-60
                       NOTE ';' to separate channel selections

      timerange  -- Select data based on time range:
              default = '' (all); examples,
              timerange = 'YYYY/MM/DD/hh:mm:ss~YYYY/MM/DD/hh:mm:ss'
              Note: if YYYY/MM/DD is missing date defaults to first day in data set
              timerange='09:14:0~09:54:0' picks 40 min on first day
              timerange= '25:00:00~27:30:00' picks 1 hr to 3 hr 30min on NEXT day
              timerange='09:44:00' pick data within one integration of time
              timerange='>10:24:00' data after this time
      uvrange -- Select data within uvrange (default units meters)
              default: '' (all); example:
              uvrange='0~1000klambda'; uvrange from 0-1000 kilo-lambda
              uvrange='>4klambda';uvranges greater than 4 kilo lambda

      antenna -- Select data based on antenna/baseline
              default: '' (all, including auto-correlations, if present)
              If antenna string is a non-negative integer, it is assumed an
                antenna index, otherwise, it is assumed as an antenna name
              antenna='5&6'; baseline between antenna index 5 and index 6.
              antenna='!ea02'; exclude EVLA antenna 2.
              antenna='ea13;!ea22'; EVLA antenna 13, excluding antenna 22.
              antenna='VA05&VA06'; baseline between VLA antenna 5 and 6.
              antenna='5&6;7&8'; baselines with indices 5-6 and 7-8
              antenna='5'; all baselines with antenna index 5
              antenna='05'; all baselines with antenna number 05 (VLA old name)
              antenna='5,6,10'; all baselines with antennas 5,6,10 index numbers
              NB: For explicit selections, use a single ampersand (&) to
              select only cross-correlations among the specified antennas, 
              double ampersands (&&) to select cross- and
              auto-correlations among the specified antennas, and
              triple ampersands (&&&) to select only
              auto-correlations.  E.g.:
              antenna='*&'; selects all cross-correlation baseline
                            (excludes all auto-correlations)
              antenna='*&&&'; selects all auto-correlation baselines
                              (excludes all cross-correlations)
              antenna='1&&1,2,3'; selects baselines 1-1 (auto), 1-2,1-3 (cross)
              antenna='VA05&&&'; selects the VA05 autocorrelation
              See the link noted above for more information.
      scan -- Scan numbers or ranges.
              default: ''  (all scans)
              scan='1,2,6,43'; scans 1, 2, 6, and 43
              scan='3~14'; scans 3 through 14, inclusive
      correlation -- Select by correlation (polarization when plotting cal tables)
                default: ''  (all correlations/polarizations)
                For measurement sets: 'RR','RL','LR','LL','XX','XY','YX','YY'
                For cal tables: 'R','L','RL','X','Y','XY','/' (for ratio plots)
                or any comma-separated combination;
                use basis (R/L or X/Y) appropriate to the table
      array -- Select the array id
               default: ''  (all array ids)
      observation -- Select by observation ID(s).
                     default: ''-->all;
                     observation='0' (select obsID 0)
      intent -- Select observing intent  
                default: ''  (no selection by intent)  
                intent='*BANDPASS*'  (selects data labelled with  
                    BANDPASS intent)
      feed -- Select by feed IDs
              default: '' (all feeds)
              feed='1~2'
      msselect -- Optional TaQL data selection

    averagedata -- data averaging parameters flag
                   default: True   (reveals expandable parameters
                                    described below)
      >>> averagedata expandable parameters
        avgchannel -- average over channel?  either blank for none, or a value
                      in channels.
                      default: '' (no channel averaging).
        avgtime -- average over time?  either blank for none, or a value in
                   seconds.
                   default: '' (no time averaging).
        avgscan -- average over scans?  only valid if time averaging is turned
                   on.
                   default: False.
        avgfield -- average over fields?  only valid if time averaging is
                    turned on.
                    default: False.
        avgbaseline -- average over selected baselines; mutually 
                       exclusive with avgantenna.
                       default: False.  (no averaging over baseline)
        avgantenna -- form per-antenna averages; mutually exclusive with
                      avgbaseline.
                      default: False.   (no per-antenna averaging)
        avgspw -- average over selected spectral windows?
                  default: False.  (no average of spectral windows)
        scalar -- scalar averaging?
                  default: False  (i.e., do vector averaging)
    
    transform -- apply various transformations on data for plotting
                 default: True
      >>> transform expandable parameters
        freqframe -- the coordinate frame in which to render frequency and velocity axes
                 default: ''  (unspecified: will use frame in which data were taken)
                 options: LSRK, LSRD, BARY, GEO, TOPO, GALACTO, LGROUP, CMB
        restfreq -- the rest frequency to use in velocity conversions (MHz)
                 default: '' (use spw central frequency and show relative velocity)
                 example: '22235.08MHz'
        veldef -- the velocity definition to use
                 default: 'RADIO'
                 options: 'RADIO','OPT','TRUE'
        shift -- adjust phase according to a phase center shift [dx,dy] (arcsec)
                 NB: the phase shift in plotms is an approximate transformation
                 default: [0,0]  (no shift)

    extendflag -- have flagging extend to other data points?
                  default: False.
      >>> extendflag expandable parameters
        extcorr -- extend flags based on correlation? 
                   default: False.
        extchannel -- extend flags based on channel?

    iteraxis -- axis upon which iterate plots (one plot per page, for now)
                default: '' (no iteration)
                options: 'scan','field','spw','baseline','antenna','time','corr',''
      >>> iteraxis expandable parameters
        xselfscale -- When True, iterated plots have a common x-axis range (scale).
        yselfscale -- When True, iterated plots have a common y-axis range (scale).
                      default: false, which will scale all plots individually
        xsharedaxis -- Iterated plots on a grid share a common external x-axis per column (must also set xselfscale=True and gridcols>1) 
                      default: false, each plot will have its own x-axis.
        ysharedaxis -- Iterated plots on a grid share a common external y-axis per row (must also set yselfscale=True and gridrows>1)
                      default: false, each plot will have its own y-axis.              

    customsymbol -- If true, use a custom symbol for drawing unflagged points
                    default: False
      >>> customsymbol expandable parameters
        symbolshape -- If true, use a custom shape to draw unflagged symbols
                       default: 'autoscaling' (ignores symbolsize)
                       options: 'autoscaling', 'circle', 'square', 'diamond', 'pixel', 'nosymbol'
        symbolsize -- size of the unflagged symbols in pixels
                      default: 2
        symbolcolor -- color to use for unflagged symbols; can be a RGB hex code or a color name
                       default: '0000ff'
                       example: 'purple'
        symbolfill -- type of fill to use for unflagged symbols
                      default: 'fill'
                      options: 'fill', 'mesh1', 'mesh2', 'mesh3', 'nofill'
        symboloutline -- If true, outline unflagged symbols in black

    coloraxis -- axis upon which to colorize the plotted points
                options (= indicates synonyms):
                    'scan',  'field',  'spw',  'antenna1'='ant1',  'antenna2'='ant2',
                    'baseline',  'channel'='chan',  'corr'='correlation', 'time', 
                    'observation', 'intent'
                default: ''  (use a single color for all points)

    customflaggedsymbol -- If true, use a custom symbol for drawing flagged points
                           default: False
      >>> customflaggedsymbol expandable parameters
        symbolshape -- If true, use a custom shape to draw flagged symbols
                       default: 'nosymbol'
                       options: 'autoscaling', 'circle', 'square', 'diamond', 'pixel', 'nosymbol'
        symbolsize -- size of the flagged symbols in pixels
                      default: 2
        symbolcolor -- color to use for flagged symbols; can be a RGB hex code or a color name
                       default: '0000ff'
                       example: 'purple'
        symbolfill -- type of fill to use for flagged symbols
                      default: 'fill'
                      options: 'fill', 'mesh1', 'mesh2', 'mesh3', 'nofill'
        symboloutline -- If true, outline flagged symbols in black

    plotrange -- manual plot axis ranges: [xmin,xmax,ymin,ymax]
                 Does not affect data selection.
                 default: []; both axes will be autoscaled according
                 to the ranges found in the selected data
                 If xmin=xmax (or ymin=ymax) then that axis will
                 be autoscaled, e.g.:
                 [0,0,-2.0,14.0]; autoscale the xaxis, and use 
                                  ymin=-2.0, ymax=14.0

    title  -- title along top of plot (called "canvas" in some places)
    titlefont -- plot title font size
                 default: 0 (autosize depending on grid)
    xlabel -- text to label horizontal axis, with formatting using '%%'
    xaxisfont -- x-axis font size
                 default: 0 (autosize)
    ylabel -- text to label horizontal axis, with formatting using '%%' 
    yaxisfont -- y-axis font size
                 default: 0 (autosize)
    
    
    showmajorgrid  -- show major grid lines 
                  default: False
      >>>  showmajorgrid expandable parameters
        majorwidth  -- line width in pixels of major grid lines
        majorstyle  -- major grid line style: solid dash dot none
        majorcolor  -- color in hex code of major grid lines

    showminorgrid  -- show minor grid lines
                  default: False
      >>>  showminorgrid expandable parameters
        minorwidth  --  line width in pixels of minor grid lines
        minorstyle  --  minor grid line style: solid dash dot none
        minorcolor  --  color in hex code of minor grid lines

    plotfile -- name of plot file to save automatically
                default: ''  (i.e., draw an interactive plot in the gui)
      >>> plotfile expandable parameters
        expformat -- export format type; if 'txt' is used an ASCII dump of the plotted points is generated (also available in the export tab)
                     default:  ''   (plotfile extension will be used)
                     options: 'jpg', 'png', 'ps', 'pdf', 'txt'
        verbose -- when export format is 'txt', print metadata for x and y values
                   default: True 
        exprange -- pages to export for iteration plots
                    default:   ''
                    options: 'current', 'all'             
        highres -- use high resolution in exported plot 
                   default: False (use screen resolution)
        dpi -- DPI of exported plot
               default: -1 (not set)
        width -- width of exported plot
                 default: -1 (not set)
        height -- height of exported plot
                  default: -1 (not set)
        overwrite -- overwrite plot file if it already exists
                     default: False
      
    callib -- calibration library string, list of strings, or filename
              default: '' 
    
    showgui - Whether or not to display the plotting GUI
              default: True
              
    headeritems -- append header items specific to this plot to the current list
                of page header items.
                Comma-separated string of header item selection keywords.
                Allowed keywords: 'obsdate','obstime','filename','projid',
                                  'targname','targdir','telescope','observer',
                                  'ycolumn'
                default: ''
                example: 'filename,projid,targname'




        """
        if not hasattr(self, "__globals__") or self.__globals__ == None :
           self.__globals__=stack_frame_find( )
        #casac = self.__globals__['casac']
        casalog = self.__globals__['casalog']
        casa = self.__globals__['casa']
        #casalog = casac.casac.logsink()
        self.__globals__['__last_task'] = 'plotms'
        self.__globals__['taskname'] = 'plotms'
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
            myparams['gridrows'] = gridrows = self.parameters['gridrows']
            myparams['gridcols'] = gridcols = self.parameters['gridcols']
            myparams['rowindex'] = rowindex = self.parameters['rowindex']
            myparams['colindex'] = colindex = self.parameters['colindex']
            myparams['plotindex'] = plotindex = self.parameters['plotindex']
            myparams['xaxis'] = xaxis = self.parameters['xaxis']
            myparams['xdatacolumn'] = xdatacolumn = self.parameters['xdatacolumn']
            myparams['xframe'] = xframe = self.parameters['xframe']
            myparams['xinterp'] = xinterp = self.parameters['xinterp']
            myparams['yaxis'] = yaxis = self.parameters['yaxis']
            myparams['ydatacolumn'] = ydatacolumn = self.parameters['ydatacolumn']
            myparams['yframe'] = yframe = self.parameters['yframe']
            myparams['yinterp'] = yinterp = self.parameters['yinterp']
            myparams['yaxislocation'] = yaxislocation = self.parameters['yaxislocation']
            myparams['selectdata'] = selectdata = self.parameters['selectdata']
            myparams['field'] = field = self.parameters['field']
            myparams['spw'] = spw = self.parameters['spw']
            myparams['timerange'] = timerange = self.parameters['timerange']
            myparams['uvrange'] = uvrange = self.parameters['uvrange']
            myparams['antenna'] = antenna = self.parameters['antenna']
            myparams['scan'] = scan = self.parameters['scan']
            myparams['correlation'] = correlation = self.parameters['correlation']
            myparams['array'] = array = self.parameters['array']
            myparams['observation'] = observation = self.parameters['observation']
            myparams['intent'] = intent = self.parameters['intent']
            myparams['feed'] = feed = self.parameters['feed']
            myparams['msselect'] = msselect = self.parameters['msselect']
            myparams['averagedata'] = averagedata = self.parameters['averagedata']
            myparams['avgchannel'] = avgchannel = self.parameters['avgchannel']
            myparams['avgtime'] = avgtime = self.parameters['avgtime']
            myparams['avgscan'] = avgscan = self.parameters['avgscan']
            myparams['avgfield'] = avgfield = self.parameters['avgfield']
            myparams['avgbaseline'] = avgbaseline = self.parameters['avgbaseline']
            myparams['avgantenna'] = avgantenna = self.parameters['avgantenna']
            myparams['avgspw'] = avgspw = self.parameters['avgspw']
            myparams['scalar'] = scalar = self.parameters['scalar']
            myparams['transform'] = transform = self.parameters['transform']
            myparams['freqframe'] = freqframe = self.parameters['freqframe']
            myparams['restfreq'] = restfreq = self.parameters['restfreq']
            myparams['veldef'] = veldef = self.parameters['veldef']
            myparams['shift'] = shift = self.parameters['shift']
            myparams['extendflag'] = extendflag = self.parameters['extendflag']
            myparams['extcorr'] = extcorr = self.parameters['extcorr']
            myparams['extchannel'] = extchannel = self.parameters['extchannel']
            myparams['iteraxis'] = iteraxis = self.parameters['iteraxis']
            myparams['xselfscale'] = xselfscale = self.parameters['xselfscale']
            myparams['yselfscale'] = yselfscale = self.parameters['yselfscale']
            myparams['xsharedaxis'] = xsharedaxis = self.parameters['xsharedaxis']
            myparams['ysharedaxis'] = ysharedaxis = self.parameters['ysharedaxis']
            myparams['customsymbol'] = customsymbol = self.parameters['customsymbol']
            myparams['symbolshape'] = symbolshape = self.parameters['symbolshape']
            myparams['symbolsize'] = symbolsize = self.parameters['symbolsize']
            myparams['symbolcolor'] = symbolcolor = self.parameters['symbolcolor']
            myparams['symbolfill'] = symbolfill = self.parameters['symbolfill']
            myparams['symboloutline'] = symboloutline = self.parameters['symboloutline']
            myparams['coloraxis'] = coloraxis = self.parameters['coloraxis']
            myparams['customflaggedsymbol'] = customflaggedsymbol = self.parameters['customflaggedsymbol']
            myparams['flaggedsymbolshape'] = flaggedsymbolshape = self.parameters['flaggedsymbolshape']
            myparams['flaggedsymbolsize'] = flaggedsymbolsize = self.parameters['flaggedsymbolsize']
            myparams['flaggedsymbolcolor'] = flaggedsymbolcolor = self.parameters['flaggedsymbolcolor']
            myparams['flaggedsymbolfill'] = flaggedsymbolfill = self.parameters['flaggedsymbolfill']
            myparams['flaggedsymboloutline'] = flaggedsymboloutline = self.parameters['flaggedsymboloutline']
            myparams['xconnector'] = xconnector = self.parameters['xconnector']
            myparams['timeconnector'] = timeconnector = self.parameters['timeconnector']
            myparams['plotrange'] = plotrange = self.parameters['plotrange']
            myparams['title'] = title = self.parameters['title']
            myparams['titlefont'] = titlefont = self.parameters['titlefont']
            myparams['xlabel'] = xlabel = self.parameters['xlabel']
            myparams['xaxisfont'] = xaxisfont = self.parameters['xaxisfont']
            myparams['ylabel'] = ylabel = self.parameters['ylabel']
            myparams['yaxisfont'] = yaxisfont = self.parameters['yaxisfont']
            myparams['showmajorgrid'] = showmajorgrid = self.parameters['showmajorgrid']
            myparams['majorwidth'] = majorwidth = self.parameters['majorwidth']
            myparams['majorstyle'] = majorstyle = self.parameters['majorstyle']
            myparams['majorcolor'] = majorcolor = self.parameters['majorcolor']
            myparams['showminorgrid'] = showminorgrid = self.parameters['showminorgrid']
            myparams['minorwidth'] = minorwidth = self.parameters['minorwidth']
            myparams['minorstyle'] = minorstyle = self.parameters['minorstyle']
            myparams['minorcolor'] = minorcolor = self.parameters['minorcolor']
            myparams['showlegend'] = showlegend = self.parameters['showlegend']
            myparams['legendposition'] = legendposition = self.parameters['legendposition']
            myparams['plotfile'] = plotfile = self.parameters['plotfile']
            myparams['expformat'] = expformat = self.parameters['expformat']
            myparams['verbose'] = verbose = self.parameters['verbose']
            myparams['exprange'] = exprange = self.parameters['exprange']
            myparams['highres'] = highres = self.parameters['highres']
            myparams['dpi'] = dpi = self.parameters['dpi']
            myparams['width'] = width = self.parameters['width']
            myparams['height'] = height = self.parameters['height']
            myparams['overwrite'] = overwrite = self.parameters['overwrite']
            myparams['showgui'] = showgui = self.parameters['showgui']
            myparams['clearplots'] = clearplots = self.parameters['clearplots']
            myparams['callib'] = callib = self.parameters['callib']
            myparams['headeritems'] = headeritems = self.parameters['headeritems']
            myparams['showatm'] = showatm = self.parameters['showatm']
            myparams['showtsky'] = showtsky = self.parameters['showtsky']
            myparams['showimage'] = showimage = self.parameters['showimage']

        if type(shift)==float: shift=[shift]
        if type(plotrange)==float: plotrange=[plotrange]
        if type(callib)==str: callib=[callib]

        result = None

#
#    The following is work around to avoid a bug with current python translation
#
        mytmp = {}

        mytmp['vis'] = vis
        mytmp['gridrows'] = gridrows
        mytmp['gridcols'] = gridcols
        mytmp['rowindex'] = rowindex
        mytmp['colindex'] = colindex
        mytmp['plotindex'] = plotindex
        mytmp['xaxis'] = xaxis
        mytmp['xdatacolumn'] = xdatacolumn
        mytmp['xframe'] = xframe
        mytmp['xinterp'] = xinterp
        mytmp['yaxis'] = yaxis
        mytmp['ydatacolumn'] = ydatacolumn
        mytmp['yframe'] = yframe
        mytmp['yinterp'] = yinterp
        mytmp['yaxislocation'] = yaxislocation
        mytmp['selectdata'] = selectdata
        mytmp['field'] = field
        mytmp['spw'] = spw
        mytmp['timerange'] = timerange
        mytmp['uvrange'] = uvrange
        mytmp['antenna'] = antenna
        mytmp['scan'] = scan
        mytmp['correlation'] = correlation
        mytmp['array'] = array
        mytmp['observation'] = observation
        mytmp['intent'] = intent
        mytmp['feed'] = feed
        mytmp['msselect'] = msselect
        mytmp['averagedata'] = averagedata
        mytmp['avgchannel'] = avgchannel
        mytmp['avgtime'] = avgtime
        mytmp['avgscan'] = avgscan
        mytmp['avgfield'] = avgfield
        mytmp['avgbaseline'] = avgbaseline
        mytmp['avgantenna'] = avgantenna
        mytmp['avgspw'] = avgspw
        mytmp['scalar'] = scalar
        mytmp['transform'] = transform
        mytmp['freqframe'] = freqframe
        mytmp['restfreq'] = restfreq
        mytmp['veldef'] = veldef
        mytmp['shift'] = shift
        mytmp['extendflag'] = extendflag
        mytmp['extcorr'] = extcorr
        mytmp['extchannel'] = extchannel
        mytmp['iteraxis'] = iteraxis
        mytmp['xselfscale'] = xselfscale
        mytmp['yselfscale'] = yselfscale
        mytmp['xsharedaxis'] = xsharedaxis
        mytmp['ysharedaxis'] = ysharedaxis
        mytmp['customsymbol'] = customsymbol
        mytmp['symbolshape'] = symbolshape
        mytmp['symbolsize'] = symbolsize
        mytmp['symbolcolor'] = symbolcolor
        mytmp['symbolfill'] = symbolfill
        mytmp['symboloutline'] = symboloutline
        mytmp['coloraxis'] = coloraxis
        mytmp['customflaggedsymbol'] = customflaggedsymbol
        mytmp['flaggedsymbolshape'] = flaggedsymbolshape
        mytmp['flaggedsymbolsize'] = flaggedsymbolsize
        mytmp['flaggedsymbolcolor'] = flaggedsymbolcolor
        mytmp['flaggedsymbolfill'] = flaggedsymbolfill
        mytmp['flaggedsymboloutline'] = flaggedsymboloutline
        mytmp['xconnector'] = xconnector
        mytmp['timeconnector'] = timeconnector
        mytmp['plotrange'] = plotrange
        mytmp['title'] = title
        mytmp['titlefont'] = titlefont
        mytmp['xlabel'] = xlabel
        mytmp['xaxisfont'] = xaxisfont
        mytmp['ylabel'] = ylabel
        mytmp['yaxisfont'] = yaxisfont
        mytmp['showmajorgrid'] = showmajorgrid
        mytmp['majorwidth'] = majorwidth
        mytmp['majorstyle'] = majorstyle
        mytmp['majorcolor'] = majorcolor
        mytmp['showminorgrid'] = showminorgrid
        mytmp['minorwidth'] = minorwidth
        mytmp['minorstyle'] = minorstyle
        mytmp['minorcolor'] = minorcolor
        mytmp['showlegend'] = showlegend
        mytmp['legendposition'] = legendposition
        mytmp['plotfile'] = plotfile
        mytmp['expformat'] = expformat
        mytmp['verbose'] = verbose
        mytmp['exprange'] = exprange
        mytmp['highres'] = highres
        mytmp['dpi'] = dpi
        mytmp['width'] = width
        mytmp['height'] = height
        mytmp['overwrite'] = overwrite
        mytmp['showgui'] = showgui
        mytmp['clearplots'] = clearplots
        mytmp['callib'] = callib
        mytmp['headeritems'] = headeritems
        mytmp['showatm'] = showatm
        mytmp['showtsky'] = showtsky
        mytmp['showimage'] = showimage
        pathname='file://' + casa['dirs']['xml'] + '/'
        trec = casac.casac.utils().torecord(pathname+'plotms.xml')

        casalog.origin('plotms')
        try :
          #if not trec.has_key('plotms') or not casac.casac.utils().verify(mytmp, trec['plotms']) :
            #return False

          casac.casac.utils().verify(mytmp, trec['plotms'], True)
          scriptstr=['']
          saveinputs = self.__globals__['saveinputs']

          # Save .last file for this task execution. MPI servers don't write it (CASR-329).
          from mpi4casa.MPIEnvironment import MPIEnvironment
          do_full_logging = MPIEnvironment.is_mpi_disabled_or_client()
          if type(self.__call__.func_defaults) is NoneType:
              saveinputs=''
          else:
              saveinputs('plotms', 'plotms.last', myparams, self.__globals__,scriptstr=scriptstr, do_save_inputs=do_full_logging)

          tname = 'plotms'
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
          result = plotms(vis, gridrows, gridcols, rowindex, colindex, plotindex, xaxis, xdatacolumn, xframe, xinterp, yaxis, ydatacolumn, yframe, yinterp, yaxislocation, selectdata, field, spw, timerange, uvrange, antenna, scan, correlation, array, observation, intent, feed, msselect, averagedata, avgchannel, avgtime, avgscan, avgfield, avgbaseline, avgantenna, avgspw, scalar, transform, freqframe, restfreq, veldef, shift, extendflag, extcorr, extchannel, iteraxis, xselfscale, yselfscale, xsharedaxis, ysharedaxis, customsymbol, symbolshape, symbolsize, symbolcolor, symbolfill, symboloutline, coloraxis, customflaggedsymbol, flaggedsymbolshape, flaggedsymbolsize, flaggedsymbolcolor, flaggedsymbolfill, flaggedsymboloutline, xconnector, timeconnector, plotrange, title, titlefont, xlabel, xaxisfont, ylabel, yaxisfont, showmajorgrid, majorwidth, majorstyle, majorcolor, showminorgrid, minorwidth, minorstyle, minorcolor, showlegend, legendposition, plotfile, expformat, verbose, exprange, highres, dpi, width, height, overwrite, showgui, clearplots, callib, headeritems, showatm, showtsky, showimage)

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
             tname = 'plotms'
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
#        paramgui.runTask('plotms', myf['_ip'])
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
        a['gridrows']  = 1
        a['gridcols']  = 1
        a['rowindex']  = 0
        a['colindex']  = 0
        a['plotindex']  = 0
        a['xaxis']  = ''
        a['yaxis']  = '', []
        a['yaxislocation']  = ''
        a['selectdata']  = True
        a['averagedata']  = True
        a['transform']  = True
        a['extendflag']  = False
        a['iteraxis']  = ''
        a['customsymbol']  = False
        a['coloraxis']  = ''
        a['customflaggedsymbol']  = False
        a['xconnector']  = ''
        a['plotrange']  = []
        a['title']  = ''
        a['titlefont']  = 0
        a['xlabel']  = ''
        a['xaxisfont']  = 0
        a['ylabel']  = ''
        a['yaxisfont']  = 0
        a['showmajorgrid']  = False
        a['showminorgrid']  = False
        a['showlegend']  = False
        a['plotfile']  = ''
        a['showgui']  = True
        a['callib']  = ['']
        a['headeritems']  = ''
        a['showatm']  = False
        a['showtsky']  = False
        a['showimage']  = False

        a['xaxis'] = {
                    0:{'value':''}, 
                    1:odict([{'value':'amp'}, {'xdatacolumn':''}]), 
                    2:odict([{'value':'amplitude'}, {'xdatacolumn':''}]), 
                    3:odict([{'value':'phase'}, {'xdatacolumn':''}]), 
                    4:odict([{'value':'real'}, {'xdatacolumn':''}]), 
                    5:odict([{'value':'imag'}, {'xdatacolumn':''}]), 
                    6:odict([{'value':'imaginary'}, {'xdatacolumn':''}]), 
                    7:odict([{'value':'ant-ra'}, {'xframe':''}, {'xinterp':''}]), 
                    8:odict([{'value':'ant-dec'}, {'xframe':''}, {'xinterp':''}]), 
                    9:{'value':'scan'}, 
                    10:{'value':'Scan'}, 
                    11:{'value':'field'}, 
                    12:{'value':'time'}, 
                    13:{'value':'time_interval'}, 
                    14:{'value':'timeinterval'}, 
                    15:{'value':'timeint'}, 
                    16:{'value':'spw'}, 
                    17:{'value':'channel'}, 
                    18:{'value':'chan'}, 
                    19:{'value':'frequency'}, 
                    20:{'value':'freq'}, 
                    21:{'value':'correlation'}, 
                    22:{'value':'corr'}, 
                    23:{'value':'antenna1'}, 
                    24:{'value':'ant1'}, 
                    25:{'value':'antenna2'}, 
                    26:{'value':'ant2'}, 
                    27:{'value':'baseline'}, 
                    28:{'value':'uvdist'}, 
                    29:{'value':'uvwave'}, 
                    30:{'value':'uvdist_l'}, 
                    31:{'value':'uvdistl'}, 
                    32:{'value':'u'}, 
                    33:{'value':'v'}, 
                    34:{'value':'w'}, 
                    35:{'value':'uwave'}, 
                    36:{'value':'vwave'}, 
                    37:{'value':'wwave'}, 
                    38:{'value':'velocity'}, 
                    39:{'value':'vel'}, 
                    40:{'value':'wt'}, 
                    41:{'value':'wtsp'}, 
                    42:{'value':'weight'}, 
                    43:{'value':'weightspectrum'}, 
                    44:{'value':'sigma'}, 
                    45:{'value':'sigmasp'}, 
                    46:{'value':'sigmaspectrum'}, 
                    47:{'value':'imwt'}, 
                    48:{'value':'flag'}, 
                    49:{'value':'azimuth'}, 
                    50:{'value':'elevation'}, 
                    51:{'value':'hourang'}, 
                    52:{'value':'hourangle'}, 
                    53:{'value':'parang'}, 
                    54:{'value':'parangle'}, 
                    55:{'value':'parallacticangle'}, 
                    56:{'value':'antenna'}, 
                    57:{'value':'ant'}, 
                    58:{'value':'ant-azimuth'}, 
                    59:{'value':'ant-elevation'}, 
                    60:{'value':'ant-hourang'}, 
                    61:{'value':'ant-hourangle'}, 
                    62:{'value':'ant-parang'}, 
                    63:{'value':'ant-parangle'}, 
                    64:{'value':'ant-parallacticangle'}, 
                    65:{'value':'row'}, 
                    66:{'value':'flagrow'}, 
                    67:{'value':'observation'}, 
                    68:{'value':'intent'}, 
                    69:{'value':'feed'}, 
                    70:{'value':'ra'}}
        a['yaxis'] = {
                    0:{'value':''}, 
                    1:odict([{'value':'amp'}, {'ydatacolumn':''}]), 
                    2:odict([{'value':'amplitude'}, {'ydatacolumn':''}]), 
                    3:odict([{'value':'phase'}, {'ydatacolumn':''}]), 
                    4:odict([{'value':'real'}, {'ydatacolumn':''}]), 
                    5:odict([{'value':'imag'}, {'ydatacolumn':''}]), 
                    6:odict([{'value':'imaginary'}, {'ydatacolumn':''}]), 
                    7:odict([{'value':'ant-ra'}, {'yframe':''}, {'yinterp':''}]), 
                    8:odict([{'value':'ant-dec'}, {'yframe':''}, {'yinterp':''}]), 
                    9:{'value':'scan'}, 
                    10:{'value':'Scan'}, 
                    11:{'value':'field'}, 
                    12:{'value':'time'}, 
                    13:{'value':'time_interval'}, 
                    14:{'value':'timeinterval'}, 
                    15:{'value':'timeint'}, 
                    16:{'value':'spw'}, 
                    17:{'value':'channel'}, 
                    18:{'value':'chan'}, 
                    19:{'value':'frequency'}, 
                    20:{'value':'freq'}, 
                    21:{'value':'correlation'}, 
                    22:{'value':'corr'}, 
                    23:{'value':'antenna1'}, 
                    24:{'value':'ant1'}, 
                    25:{'value':'antenna2'}, 
                    26:{'value':'ant2'}, 
                    27:{'value':'baseline'}, 
                    28:{'value':'uvdist'}, 
                    29:{'value':'uvwave'}, 
                    30:{'value':'uvdist_l'}, 
                    31:{'value':'uvdistl'}, 
                    32:{'value':'u'}, 
                    33:{'value':'v'}, 
                    34:{'value':'w'}, 
                    35:{'value':'uwave'}, 
                    36:{'value':'vwave'}, 
                    37:{'value':'wwave'}, 
                    38:{'value':'velocity'}, 
                    39:{'value':'vel'}, 
                    40:{'value':'wt'}, 
                    41:{'value':'wtsp'}, 
                    42:{'value':'weight'}, 
                    43:{'value':'weightspectrum'}, 
                    44:{'value':'sigma'}, 
                    45:{'value':'sigmasp'}, 
                    46:{'value':'sigmaspectrum'}, 
                    47:{'value':'imwt'}, 
                    48:{'value':'flag'}, 
                    49:{'value':'azimuth'}, 
                    50:{'value':'elevation'}, 
                    51:{'value':'hourang'}, 
                    52:{'value':'hourangle'}, 
                    53:{'value':'parang'}, 
                    54:{'value':'parangle'}, 
                    55:{'value':'parallacticangle'}, 
                    56:{'value':'antenna'}, 
                    57:{'value':'ant'}, 
                    58:{'value':'ant-azimuth'}, 
                    59:{'value':'ant-elevation'}, 
                    60:{'value':'ant-hourang'}, 
                    61:{'value':'ant-hourangle'}, 
                    62:{'value':'ant-parang'}, 
                    63:{'value':'ant-parangle'}, 
                    64:{'value':'ant-parallacticangle'}, 
                    65:{'value':'row'}, 
                    66:{'value':'flagrow'}, 
                    67:{'value':'observation'}, 
                    68:{'value':'intent'}, 
                    69:{'value':'feed'}}
        a['selectdata'] = {
                    0:odict([{'value':True}, {'field':''}, {'spw':''}, {'timerange':''}, {'uvrange':''}, {'antenna':''}, {'scan':''}, {'correlation':''}, {'array':''}, {'observation':''}, {'intent':''}, {'feed':''}, {'msselect':''}]), 
                    1:{'value':False}}
        a['averagedata'] = {
                    0:odict([{'value':True}, {'avgchannel':''}, {'avgtime':''}, {'avgscan':False}, {'avgfield':False}, {'avgbaseline':False}, {'avgantenna':False}, {'avgspw':False}, {'scalar':False}]), 
                    1:{'value':False}}
        a['transform'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'freqframe':''}, {'restfreq':''}, {'veldef':'RADIO'}, {'shift':[0.0, 0.0]}])}
        a['extendflag'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'extcorr':False}, {'extchannel':False}])}
        a['iteraxis'] = {
                    0:odict([{'notvalue':''}, {'xselfscale':False}, {'yselfscale':False}, {'xsharedaxis':False}, {'ysharedaxis':False}])}
        a['customsymbol'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'symbolshape':'autoscaling'}, {'symbolsize':2}, {'symbolcolor':'0000ff'}, {'symbolfill':'fill'}, {'symboloutline':False}])}
        a['customflaggedsymbol'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'flaggedsymbolshape':'nosymbol'}, {'flaggedsymbolsize':2}, {'flaggedsymbolcolor':'ff0000'}, {'flaggedsymbolfill':'fill'}, {'flaggedsymboloutline':False}])}
        a['plotfile'] = {
                    0:odict([{'notvalue':''}, {'expformat':''}, {'verbose':True}, {'exprange':''}, {'highres':False}, {'dpi':-1}, {'width':-1}, {'height':-1}, {'overwrite':False}])}
        a['showgui'] = {
                    0:odict([{'value':True}, {'clearplots':True}]), 
                    1:odict([{'value':False}, {'clearplots':True}])}
        a['showmajorgrid'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'majorwidth':0}, {'majorstyle':''}, {'majorcolor':''}])}
        a['showminorgrid'] = {
                    0:{'value':False}, 
                    1:odict([{'value':True}, {'minorwidth':0}, {'minorstyle':''}, {'minorcolor':''}])}
        a['xconnector'] = {
                    0:{'value':''}, 
                    1:{'value':'none'}, 
                    2:odict([{'value':'line'}, {'timeconnector':False}]), 
                    3:odict([{'value':'step'}, {'timeconnector':False}])}

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
    def description(self, key='plotms', subkey=None):
        desc={'plotms': 'A plotter/interactive flagger for visibility data.',
               'vis': 'Input MS or CalTable (blank for none)',
               'gridrows': 'Number of subplot rows',
               'gridcols': 'Number of subplot columns',
               'rowindex': 'Row location of the plot (0-based)',
               'colindex': 'Column location of the plot (0-based)',
               'plotindex': 'Index to address a subplot (0-based)',
               'xaxis': 'Plot x-axis (blank for default/current)',
               'xdatacolumn': 'Data column to use for x-axis (blank for default/current).  Note that unspecified residuals are complex (vector) differences or ratios.',
               'xframe': 'Coordinate frame to use for x-axis',
               'xinterp': 'Interpolation method for x-axis',
               'yaxis': 'Plot y-axis (blank for default/current)',
               'ydatacolumn': 'Data column to use for y-axis (blank for default/current). Note that unspecified residuals are complex (vector) differences or ratios.',
               'yframe': 'Coordinate frame to use for y-axis',
               'yinterp': 'Interpolation method for y-axis',
               'yaxislocation': 'Location of the y-axis (blank for default: left)',
               'selectdata': 'Enable data selection parameters',
               'field': 'Field names or ids (blank for all)',
               'spw': 'Spectral windows:channels (blank for all)',
               'timerange': 'Time range (blank for all)',
               'uvrange': 'UV range (blank for all)',
               'antenna': 'Baseline/antenna names or ids (blank for all)',
               'scan': 'Scan numbers (blank for all)',
               'correlation': 'Correlations/polarizations (blank for all)',
               'array': '(Sub)array numbers (blank for all)',
               'observation': 'Observation IDs (blank for all)',
               'intent': 'Observing intent (blank for all)',
               'feed': 'Feed numbers (blank for all)',
               'msselect': 'MSSelection TaQL string (blank for none)',
               'averagedata': 'Enable data averaging parameters',
               'avgchannel': 'Average over channel (blank = False, otherwise value in channels)',
               'avgtime': 'Average over time (blank = False, otherwise value in seconds)',
               'avgscan': 'Average over scans. Only valid with time averaging',
               'avgfield': 'Average over fields. Only valid with time averaging',
               'avgbaseline': 'Average over all baselines (mutually exclusive with avgantenna)',
               'avgantenna': 'Average per antenna (mutually exclusive with avgbaseline)',
               'avgspw': 'Average over all spectral windows',
               'scalar': 'Scalar averaging (False=vector averaging)',
               'transform': 'Enable data transformations',
               'freqframe': 'The frame in which to render frequency and velocity axes',
               'restfreq': 'Rest frequency to use for velocity conversions ',
               'veldef': 'The definition in which to render velocity ',
               'shift': 'Adjust phases by this approximate phase center shift [dx,dy] (arcsec)',
               'extendflag': 'Extend flagging to other data points not plotted',
               'extcorr': 'Extend flags based on correlation ',
               'extchannel': 'Extend flags based on channel',
               'iteraxis': 'The axis over which to iterate',
               'xselfscale': 'When True, iterated plots have a common x-axis range (scale).',
               'yselfscale': 'When True, iterated plots have a common y-axis range (scale).',
               'xsharedaxis': 'Iterated plots on a grid share a common external x-axis per column. Must also set xselfscale=True and gridrows>1.',
               'ysharedaxis': 'Iterated plots on a grid share a common external y-axis per row. Must also set yselfscale=True and gridcols>1.',
               'customsymbol': 'Enable custom symbol(s) for unflagged points',
               'symbolshape': 'Shape of plotted unflagged symbols',
               'symbolsize': 'Size of plotted unflagged symbols',
               'symbolcolor': 'Color (name or hex code) of plotted unflagged symbols',
               'symbolfill': 'Fill type of plotted unflagged symbols',
               'symboloutline': 'Outline plotted unflagged symbols',
               'coloraxis': 'Selects data axis for colorizing',
               'customflaggedsymbol': 'Enable custom symbol(s) for flagged points',
               'flaggedsymbolshape': 'Shape of plotted flagged symbols',
               'flaggedsymbolsize': 'Size of plotted flagged symbols',
               'flaggedsymbolcolor': 'Color (name or hex code) of plotted flagged symbols',
               'flaggedsymbolfill': 'Fill type of plotted flagged symbols',
               'flaggedsymboloutline': 'Outline plotted flagged symbols',
               'xconnector': 'Set connector for data points (blank="none"; "line","step")',
               'timeconnector': 'Connect points by time rather than x-axis',
               'plotrange': 'Plot axes ranges: [xmin,xmax,ymin,ymax]',
               'title': 'Title at top of plot',
               'titlefont': 'Font size for plot title',
               'xlabel': 'Text for horizontal x-axis. Blank for default.',
               'xaxisfont': 'Font size for x-axis label',
               'ylabel': 'Text for vertical y-axis. Blank for default.',
               'yaxisfont': 'Font size for y-axis label',
               'showmajorgrid': 'Show major grid lines',
               'majorwidth': 'Line width in pixels of major grid lines',
               'majorstyle': 'Major grid line style',
               'majorcolor': 'Color (name or hex code) of major grid lines',
               'showminorgrid': 'Show minor grid lines',
               'minorwidth': 'Line width in pixels of minor grid lines',
               'minorstyle': 'Minor grid line style',
               'minorcolor': 'Color (name or hex code) of minor grid lines',
               'showlegend': 'Show a legend on the plot.',
               'legendposition': 'Legend position, default upperRight.',
               'plotfile': 'Name of plot file to save automatically',
               'expformat': 'Export format type. If not provided, plotfile extension will be used to determine type.',
               'verbose': 'Include metadata in text export',
               'exprange': 'Range of iteration plots to export, one plotfile per page.  Multipage pdf exports are not supported.',
               'highres': 'Use high resolution',
               'dpi': 'DPI of exported plot',
               'width': 'Width in pixels of exported plot',
               'height': 'Height in pixels of exported plot',
               'overwrite': 'Overwrite plot file if it already exists',
               'showgui': 'Show GUI',
               'clearplots': 'Remove any existing plots so new ones can replace them.',
               'callib': 'Calibration library string or filename for on-the-fly calibration.',
               'headeritems': 'Comma-separated list of pre-defined page header items.',
               'showatm': 'Compute and overlay the atmospheric transmission curve',
               'showtsky': 'Compute and overlay the sky temperature curve',
               'showimage': 'Compute and overlay the image sideband curve',

              }

#
# Set subfields defaults if needed
#

        if(desc.has_key(key)) :
           return desc[key]

    def itsdefault(self, paramname) :
        a = {}
        a['vis']  = ''
        a['gridrows']  = 1
        a['gridcols']  = 1
        a['rowindex']  = 0
        a['colindex']  = 0
        a['plotindex']  = 0
        a['xaxis']  = ''
        a['xdatacolumn']  = ''
        a['xframe']  = ''
        a['xinterp']  = ''
        a['yaxis']  = '', []
        a['ydatacolumn']  = ''
        a['yframe']  = ''
        a['yinterp']  = ''
        a['yaxislocation']  = ''
        a['selectdata']  = True
        a['field']  = ''
        a['spw']  = ''
        a['timerange']  = ''
        a['uvrange']  = ''
        a['antenna']  = ''
        a['scan']  = ''
        a['correlation']  = ''
        a['array']  = ''
        a['observation']  = ''
        a['intent']  = ''
        a['feed']  = ''
        a['msselect']  = ''
        a['averagedata']  = True
        a['avgchannel']  = ''
        a['avgtime']  = ''
        a['avgscan']  = False
        a['avgfield']  = False
        a['avgbaseline']  = False
        a['avgantenna']  = False
        a['avgspw']  = False
        a['scalar']  = False
        a['transform']  = True
        a['freqframe']  = ''
        a['restfreq']  = ''
        a['veldef']  = 'RADIO'
        a['shift']  = [0.0, 0.0]
        a['extendflag']  = False
        a['extcorr']  = False
        a['extchannel']  = False
        a['iteraxis']  = ''
        a['xselfscale']  = False
        a['yselfscale']  = False
        a['xsharedaxis']  = False
        a['ysharedaxis']  = False
        a['customsymbol']  = False
        a['symbolshape']  = 'autoscaling'
        a['symbolsize']  = 2
        a['symbolcolor']  = '0000ff'
        a['symbolfill']  = 'fill'
        a['symboloutline']  = False
        a['coloraxis']  = ''
        a['customflaggedsymbol']  = False
        a['flaggedsymbolshape']  = 'circle'
        a['flaggedsymbolsize']  = 2
        a['flaggedsymbolcolor']  = 'ff0000'
        a['flaggedsymbolfill']  = 'fill'
        a['flaggedsymboloutline']  = False
        a['xconnector']  = ''
        a['timeconnector']  = False
        a['plotrange']  = []
        a['title']  = ''
        a['titlefont']  = 0
        a['xlabel']  = ''
        a['xaxisfont']  = 0
        a['ylabel']  = ''
        a['yaxisfont']  = 0
        a['showmajorgrid']  = False
        a['majorwidth']  = 1
        a['majorstyle']  = ''
        a['majorcolor']  = 'B0B0B0'
        a['showminorgrid']  = False
        a['minorwidth']  = 1
        a['minorstyle']  = ''
        a['minorcolor']  = 'D0D0D0'
        a['showlegend']  = False
        a['legendposition']  = ''
        a['plotfile']  = ''
        a['expformat']  = ''
        a['verbose']  = True
        a['exprange']  = ''
        a['highres']  = False
        a['dpi']  = -1
        a['width']  = -1
        a['height']  = -1
        a['overwrite']  = False
        a['showgui']  = True
        a['clearplots']  = True
        a['callib']  = ['']
        a['headeritems']  = ''
        a['showatm']  = False
        a['showtsky']  = False
        a['showimage']  = False

        #a = sys._getframe(len(inspect.stack())-1).f_globals

        if self.parameters['xaxis']  == 'amp':
            a['xdatacolumn'] = ''

        if self.parameters['xaxis']  == 'amplitude':
            a['xdatacolumn'] = ''

        if self.parameters['xaxis']  == 'phase':
            a['xdatacolumn'] = ''

        if self.parameters['xaxis']  == 'real':
            a['xdatacolumn'] = ''

        if self.parameters['xaxis']  == 'imag':
            a['xdatacolumn'] = ''

        if self.parameters['xaxis']  == 'imaginary':
            a['xdatacolumn'] = ''

        if self.parameters['xaxis']  == 'ant-ra':
            a['xframe'] = ''
            a['xinterp'] = ''

        if self.parameters['xaxis']  == 'ant-dec':
            a['xframe'] = ''
            a['xinterp'] = ''

        if self.parameters['yaxis']  == 'amp':
            a['ydatacolumn'] = ''

        if self.parameters['yaxis']  == 'amplitude':
            a['ydatacolumn'] = ''

        if self.parameters['yaxis']  == 'phase':
            a['ydatacolumn'] = ''

        if self.parameters['yaxis']  == 'real':
            a['ydatacolumn'] = ''

        if self.parameters['yaxis']  == 'imag':
            a['ydatacolumn'] = ''

        if self.parameters['yaxis']  == 'imaginary':
            a['ydatacolumn'] = ''

        if self.parameters['yaxis']  == 'ant-ra':
            a['yframe'] = ''
            a['yinterp'] = ''

        if self.parameters['yaxis']  == 'ant-dec':
            a['yframe'] = ''
            a['yinterp'] = ''

        if self.parameters['selectdata']  == True:
            a['field'] = ''
            a['spw'] = ''
            a['timerange'] = ''
            a['uvrange'] = ''
            a['antenna'] = ''
            a['scan'] = ''
            a['correlation'] = ''
            a['array'] = ''
            a['observation'] = ''
            a['intent'] = ''
            a['feed'] = ''
            a['msselect'] = ''

        if self.parameters['averagedata']  == True:
            a['avgchannel'] = ''
            a['avgtime'] = ''
            a['avgscan'] = False
            a['avgfield'] = False
            a['avgbaseline'] = False
            a['avgantenna'] = False
            a['avgspw'] = False
            a['scalar'] = False

        if self.parameters['transform']  == True:
            a['freqframe'] = ''
            a['restfreq'] = ''
            a['veldef'] = 'RADIO'
            a['shift'] = [0.0, 0.0]

        if self.parameters['extendflag']  == True:
            a['extcorr'] = False
            a['extchannel'] = False

        if self.parameters['iteraxis']  != '':
            a['xselfscale'] = False
            a['yselfscale'] = False
            a['xsharedaxis'] = False
            a['ysharedaxis'] = False

        if self.parameters['customsymbol']  == True:
            a['symbolshape'] = 'autoscaling'
            a['symbolsize'] = 2
            a['symbolcolor'] = '0000ff'
            a['symbolfill'] = 'fill'
            a['symboloutline'] = False

        if self.parameters['customflaggedsymbol']  == True:
            a['flaggedsymbolshape'] = 'nosymbol'
            a['flaggedsymbolsize'] = 2
            a['flaggedsymbolcolor'] = 'ff0000'
            a['flaggedsymbolfill'] = 'fill'
            a['flaggedsymboloutline'] = False

        if self.parameters['plotfile']  != '':
            a['expformat'] = ''
            a['verbose'] = True
            a['exprange'] = ''
            a['highres'] = False
            a['dpi'] = -1
            a['width'] = -1
            a['height'] = -1
            a['overwrite'] = False

        if self.parameters['showgui']  == True:
            a['clearplots'] = True

        if self.parameters['showgui']  == False:
            a['clearplots'] = True

        if self.parameters['showmajorgrid']  == True:
            a['majorwidth'] = 0
            a['majorstyle'] = ''
            a['majorcolor'] = ''

        if self.parameters['showminorgrid']  == True:
            a['minorwidth'] = 0
            a['minorstyle'] = ''
            a['minorcolor'] = ''

        if self.parameters['xconnector']  == 'line':
            a['timeconnector'] = False

        if self.parameters['xconnector']  == 'step':
            a['timeconnector'] = False

        if a.has_key(paramname) :
              return a[paramname]
plotms_cli = plotms_cli_()
