import pyupbit
import matplotlib.pyplot as plt
import cv2

# get pandas dataframe and make matplot .png file
df = pyupbit.get_ohlcv('KRW-BTC',interval="minute90")['close']
plt.plot(df)
plt.savefig('temp.png')

# from .png file to opencv for input file
x= 100;y=70;w=455;h=345
graph = cv2.imread('temp.png')[y:y+h,x:x+w].copy()

# just show result img
cv2.imshow("result",graph)
key = cv2.waitKey(0)
cv2.destroyAllWindows()