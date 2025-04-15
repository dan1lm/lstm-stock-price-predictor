import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import yfinance as yf
from config import config
import pandas as pd

def download_data(config):
    symbol = config["alpha_vantage"]["symbol"]
    
    data = yf.download(symbol, period="10y")
    
    print("Available columns:", data.columns.tolist())
    
    if isinstance(data.columns, pd.MultiIndex):
        price_column = ('Close', symbol)
    else:
        price_column = 'Close'
        
    data_date = data.index.strftime('%Y-%m-%d').tolist()
    data_close_price = data[price_column].values
    
    num_data_points = len(data_date)
    display_date_range = "from " + data_date[0] + " to " + data_date[num_data_points-1]
    print("Number data points", num_data_points, display_date_range)
    
    return data_date, data_close_price, num_data_points, display_date_range

if __name__ == '__main__':
    data_date, data_close_price, num_data_points, display_date_range = download_data(config)
    
    fig = figure(figsize=(25, 5), dpi=80)
    fig.patch.set_facecolor((1.0, 1.0, 1.0))
    
    plt.plot(data_date, data_close_price, color=config["plots"]["color_actual"])
    xticks = [data_date[i] if ((i%config["plots"]["xticks_interval"]==0 and (num_data_points-i) > config["plots"]["xticks_interval"]) or i==num_data_points-1) else None for i in range(num_data_points)]
    
    x = np.arange(0,len(xticks))
    
    plt.xticks(x, xticks, rotation='vertical')
    plt.title("Daily close price for " + config["alpha_vantage"]["symbol"] + ", " + display_date_range)
    
    plt.grid(which='major', axis='y', linestyle='--')
    plt.show()