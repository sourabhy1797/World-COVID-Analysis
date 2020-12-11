import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset15 = pd.read_csv(r'C:\Users\yadavs\Downloads\ShanghaiSE.csv')

dataset15.index = dataset15['Date']

dt4 = dataset15

del dt4['Date']

del dt4['corona']

cr4 = dt4.corr()

cr4