import pandas as pd
import numpy as np
from constants import *


def emissions(run_start_year, run_end_year, dt, rcp,
              CO2_PPM_1750, CH4_PPB_1750, N2O_PPB_1750,
              add_start = 0, 
              add_end = 0, c_add = 0, ch4_add = 0, n2o_add = 0):
    """
    Take annual emissions from a RCP scenario and return
    emissions by specified start date, end date, and time step
    """
    run_years = run_end_year - run_start_year + 1 
    print(rcp)
    rcp_emissions = pd.read_csv('emissions/rcp_'+str(rcp)+'_data.csv', sep=',')
    historic_emissions = pd.read_csv('emissions/historical_ghgs.csv', sep=',')
    emissions = rcp_emissions.append(historic_emissions, ignore_index=True)
    emissions.sort_values(by='year', inplace=True)
    emissions.reset_index(inplace=True)
    if add_start > 0:
        emissions.loc[(
            (emissions['year'] >= add_start) & (emissions['year'] <= add_end), 
            'c_emissions_pg')] = emissions['c_emissions_pg'] + c_add
        emissions.loc[(
            (emissions['year'] >= add_start) & (emissions['year'] <= add_end), 
            'ch4_emissions_tg')] = emissions['ch4_emissions_tg'] + ch4_add
        emissions.loc[(
            (emissions['year'] >= add_start) & (emissions['year'] <= add_end), 
            'n2o_emissions_tg')] = emissions['n2o_emissions_tg'] + n2o_add
    
    total_years = emissions.shape[0]
    subset = emissions[int(run_start_year - 1765):int(run_end_year - 1765 + 1)]
    subset.reset_index(inplace=True)
    date = np.array([np.arange(0, run_years, dt)]).T
    columns = ['date']
    df = pd.DataFrame(date, columns=columns)
    steps = df.shape[0]

    for t in range(0,int(steps)):
        df.loc[t, 'year'] = subset['year'][int(df['date'][t])]
        df.loc[t, 'co2_pg'] = subset['c_emissions_pg'][int(df['date'][t])] * dt * C_TO_CO2
        df.loc[t, 'ch4_tg'] = subset['ch4_emissions_tg'][int(df['date'][t])] * dt
        df.loc[t, 'n2o_tg'] = subset['n2o_emissions_tg'][int(df['date'][t])] * dt
        df.loc[t, 'hist_forcing_wm2'] = subset['hist_forcing_wm2'][int(df['date'][t])]
        df.loc[t, 'co2_forcing_rcp'] = subset['co2_forcing_wm2'][int(df['date'][t])]
        df.loc[t, 'ch4_forcing_rcp'] = subset['ch4_forcing_wm2'][int(df['date'][t])]
        df.loc[t, 'n2o_forcing_rcp'] = subset['n2o_forcing_wm2'][int(df['date'][t])]
        df.loc[t, 'total_forcing_rcp'] = subset['total_forcing_wm2'][int(df['date'][t])]
        df.loc[t, 'rcp_co2_ppm'] = subset['co2_concentration_ppm'][int(df['date'][t])]
        df.loc[t, 'rcp_ch4_ppb'] = subset['ch4_concentration_ppb'][int(df['date'][t])]
        df.loc[t, 'rcp_n2o_ppb'] = subset['n2o_concentration_ppb'][int(df['date'][t])]
    
    df['rcp_co2_ppm'].fillna(CO2_PPM_1750, inplace=True)
    df['rcp_ch4_ppb'].fillna(CH4_PPB_1750, inplace=True)
    df['rcp_n2o_ppb'].fillna(N2O_PPB_1750, inplace=True)
    
    return df