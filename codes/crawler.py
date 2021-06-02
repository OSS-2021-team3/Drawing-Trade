import pyupbit
import matplotlib.pyplot as plt
import os

# default interval = 60
def carwl(data_path):
    # if there is no folder make folder to save data
    if not os.path.isdir(data_path):
        os.mkdir(data_path)

    # get pandas dataframe and make matplot .png file
    tickers = pyupbit.get_tickers("KRW")
    for i in tickers:
        df = pyupbit.get_ohlcv(i,interval="minute60")

        # choose close price
        df = df['close']
        
        # save graphs
        plt.plot(df)
        plt.savefig(data_path+i)
        plt.clf()
        
    return tickers

def gettickers():
    return pyupbit.get_tickers("KRW")
