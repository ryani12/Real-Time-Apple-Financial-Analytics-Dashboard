import os
import pandas as pd
from dotenv import load_dotenv
from alpha_vantage.timeseries import TimeSeries

# Load environment variables from .env file
load_dotenv()

# Access environment variables
alpha_vantage_api_key = os.getenv('ALPHA_VANTAGE_API_KEY')


# API key
ts = TimeSeries(key='alpha_vantage_api_key')

# Get daily stock prices for AAPL
data, meta_data = ts.get_daily(symbol='AAPL', outputsize = 'full')


# Convert the data to a pandas DataFrame
df = pd.DataFrame.from_dict(data, orient='index')

# Save the DataFrame to a CSV file
df.to_csv('aapl_stock_data.csv')

