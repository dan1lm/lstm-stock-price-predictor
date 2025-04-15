import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset
from torch.utils.data import DataLoader

import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

from alpha_vantage.timeseries import TimeSeries 

import os
from dotenv import load_dotenv
from config import config, ALPHA_VANTAGE_API_KEY

def download_data(config):
    time_series = TimeSeries(key=ALPHA_VANTAGE_API_KEY)
    data, meta_data = time_series.get_daily_adjusted(config["alpha_vantage"]["symbol"], outputsize=config["alpha_vantage"]["outputsize"])
    
    data_date = [date for date in data.keys()]
    data_date.reverse()
    
    data_close_price = [float(data[date][config["alpha_vantage"]["key_adjusted_close"]]) for date in data.keys()]
    data_close_price.reverse()
    data_close_price = np.array(data_close_price)
    
    num_data_points = len(data_date)
    display_date_range = "from " + data_date[0] + " to " + data_date[num_data_points-1]
    print("Number data points", num_data_points, display_date_range)
    return data_date, data_close_price, num_data_points, display_date_range


if __name__ == '__main__':
    print('Driver')