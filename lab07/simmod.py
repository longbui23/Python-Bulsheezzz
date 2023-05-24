import pandas as pd
import numpy as np
import warnings

from constants import *
from emissions_parser import emissions
from concs_pulse_decay import pulse_decay_runner
from radiative_forcing import calc_radiative_forcing
from heat_diffusion import continuous_diffusion_model

#Model Parameters
run_start_year = 1765.          #Run start year
run_end_year = 2100.            #Inclusive of end year
dt = 1 #/ 100.                  #years
rcp = '8.5'                     #RCP scenario
carbon_model = 'pulse response' #'pulse response', 'box diffusion', or 'BEAM'
normalize_2000_conc = False      #Normalize concentrations to historical year-2000 values
c_sens = 1.25                   #Climate sensativity (T = F / LAMBDA)

warnings.simplefilter(action='ignore', category=FutureWarning)
pd.set_option('mode.chained_assignment', None)

def run_simmod_orig(run_start_year, run_end_year, dt, rcp, 
                    CO2_PPM_1750, CH4_PPB_1750, N2O_PPB_1750,
                    c_sens, add_start = 0, 
                    add_end = 0, c_add = 0, ch4_add = 0, n2o_add = 0):

    """
    Run the various parts of SimMod and export images and CSV files.
    """
    run_years = (run_end_year - run_start_year + 1)
    emission_vals = emissions(run_start_year, run_end_year, dt, rcp, 
                              CO2_PPM_1750, CH4_PPB_1750, N2O_PPB_1750,
                              add_start, add_end, c_add, ch4_add, n2o_add)
    conc = pulse_decay_runner(run_years, dt, emission_vals)

    if normalize_2000_conc == True:
        conc['co2_ppm'] = (
            conc['co2_ppm'] - 
            conc.loc[conc['year'] == 2000, 'co2_ppm'].min() +
            emission_vals.loc[emission_vals['year'] == 2000, 'rcp_co2_ppm'].min()
        )
        conc['ch4_ppb'] = (
            conc['ch4_ppb'] - 
            conc.loc[conc['year'] == 2000, 'ch4_ppb'].min() +
            emission_vals.loc[emission_vals['year'] == 2000, 'rcp_ch4_ppb'].min()
        )
        conc['n2o_ppb'] = (
            conc['n2o_ppb'] - 
            conc.loc[conc['year'] == 2000, 'n2o_ppb'].min() +
            emission_vals.loc[emission_vals['year'] == 2000, 'rcp_n2o_ppb'].min()
        )

    forcing = calc_radiative_forcing(conc, CO2_PPM_1750, CH4_PPB_1750, N2O_PPB_1750)
    warming = continuous_diffusion_model(forcing, run_years, dt, c_sens)
    return warming


#def run_simmod(start_year, end_year, rcp, CO2_1750_ppm, CH4_1750_ppb, N2O_1750_ppb, CS_param, out_file):
def run_simmod(start_year, end_year, rcp, CS_param, out_file):
    """ Run a climate simulation for the specified range of years using
         * the given rcp (e.g. '2.6', '4.5', '6.0' or '8.5')
         * the climate sensitivity parameter
         * and the full path and name of the output file into which the result are written.
    """

#    results = run_simmod_orig(start_year, end_year, dt, rcp, 
#                              CO2_1750_ppm, CH4_1750_ppb, N2O_1750_ppb, CS_param)

    results = run_simmod_orig(start_year, end_year, dt, rcp, 
                              CO2_PPM_1750, CH4_PPB_1750, N2O_PPB_1750, CS_param)

    results.to_csv(out_file)
