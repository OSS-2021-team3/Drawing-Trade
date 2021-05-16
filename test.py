import pyupbit
import matplotlib.pyplot as plt
import cv2

# get pandas dataframe and make matplot .png file
tickers = pyupbit.get_tickers("KRW")
for i in tickers:
    df = pyupbit.get_ohlcv(i,interval="minute30")
    df = df['close']
    plt.plot(df)
    plt.savefig(i)
    plt.clf()

# from .png file to opencv for input file
x= 100;y=70;w=455;h=345
for i in tickers:
    graph = cv2.imread(i+".png")[y:y+h,x:x+w].copy()
    
    # just show result img
    cv2.imshow("result",graph)
    key = cv2.waitKey(0)
    cv2.destroyAllWindows()


