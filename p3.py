import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

np.random.seed(10)
date_range = pd.date_range(start="2022-01-01", end="2023-01-01", freq="D")

data = pd.DataFrame({
    "Date": date_range,
    "Value_A": np.random.normal(100, 10, len(date_range)),
    "Value_B": np.random.normal(200, 20, len(date_range)),
})
data.set_index("Date", inplace=True)

def groupby_mechanics(data):
    print("\n--- GroupBy Mechanics ---")
    grouped = data.resample('M').mean()
    print(grouped)

def data_formats(data):
    print("\n--- Data Formats ---")
    print("\nVector Format:",data["Value_A"].head())
    print("\nMultivariate Time Series:",data.head())
     
def time_series_forecasting(data):
    print("\n--- Forecasting ---")
    ts = data["Value_A"]
    
    train = ts[:int(0.8 * len(ts))]
    test = ts[int(0.8 * len(ts)):]
    
    model = ExponentialSmoothing(train, seasonal="add", seasonal_periods=30).fit()
    forecast = model.forecast(len(test))
    
    plt.figure(figsize=(12, 6))
    plt.plot(train, label="Train")
    plt.plot(test, label="Test")
    plt.plot(forecast, label="Forecast")
    plt.legend()
    plt.title("Time Series Forecasting")
    plt.show()
    
groupby_mechanics(data)
data_formats(data)
time_series_forecasting(data)

