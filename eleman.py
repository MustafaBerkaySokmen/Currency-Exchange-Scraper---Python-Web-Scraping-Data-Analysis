
import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
# Define start and end date of the data you'd like to retrieve.#
start_date = datetime.datetime(2012, 1, 1)
end_date = datetime.datetime(2022, 1, 1)
# Retrieve data from X-Rates website
url = f'https://www.x-rates.com/historical/?from=USD&to=TRY&amount=1&date={start_date.strftime('%Y-%m-%d') }'
df = pd.read_html(url)[0]
df.dropna(inplace=True)
# Define column names
col_names = [    'date',\n    'rate'\n]\n\n# Convert date strings to datetime objects\ndf['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')\n\ndf = df.set_index('date')\n\nprint(df)"

