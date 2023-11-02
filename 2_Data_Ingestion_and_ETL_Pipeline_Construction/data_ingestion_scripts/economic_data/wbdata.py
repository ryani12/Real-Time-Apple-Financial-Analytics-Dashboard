import collections.abc
collections.Sequence = collections.abc.Sequence

import wbdata
import pandas as pd
import datetime

# Set the country code and date range for the data you're interested in
country_code = "all"
data_date = datetime.datetime(1999, 1, 1), datetime.datetime(2022, 1, 1)

# Specify the World Bank indicator codes for the data you want to fetch
indicators = {
    'NY.GDP.MKTP.CD': 'GDP (current US$)',
    'NY.GDP.PCAP.CD': 'GDP per capita (current US$)',
    'SL.UEM.TOTL.ZS': 'Unemployment, total (% of total labor force)',
    'FP.CPI.TOTL.ZG': 'Inflation, consumer prices (annual %)',
    'BX.TRF.PWKR.CD.DT': 'Personal remittances, received (% of GDP)',
    'EN.ATM.CO2E.PC': 'CO2 emissions (metric tons per capita)',
    'EG.ELC.ACCS.ZS': 'Access to electricity (% of population)'
}

# Fetch the data from the World Bank
wb_data = wbdata.get_dataframe(indicators, country=country_code, data_date=data_date)

# Since the data is returned with the date as the index, you might want to reset the index for easier handling
wb_data_reset = wb_data.reset_index()

# Optionally, save the data to a CSV file
wb_data_reset.to_csv('economic_data.csv', index=False)
