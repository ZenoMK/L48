import pandas as pd
import numpy as np

def fahrenheit_to_celsius(x):
    return (x - 32) * (5/9)


hp_hws_temp = pd.read_csv("../data/HVACdata/hp_hws_temp.csv")
hp_hws_temp["date"] = pd.to_datetime(hp_hws_temp["date"])
missing = pd.date_range(hp_hws_temp.date.min(), hp_hws_temp.date.max(), freq='1min').difference(hp_hws_temp.date)
hp_hws_temp.resample("1T").fillna(method=None)
#hp_new = pd.date_range(hp_hws_temp, start = "2018-01-01 00:00:00", end = "2020-01-01 00:00:00", freq="15min")#hp_hws_temp.iloc[::15]
#hp_new.loc[:,"hp_hws_temp"] = fahrenheit_to_celsius(hp_new["hp_hws_temp"])
print(missing)