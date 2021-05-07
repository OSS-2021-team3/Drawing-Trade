import pyupbit
import matplotlib.pyplot as plt
import cv2

df = pyupbit.get_ohlcv('KRW-BTC',interval="minute30")['close']
plt.plot(df)
plt.savefig('temp.png')

img = cv2.imread('temp.png')
x= 100;y=70;w=455;h=345
roi = img[y:y+h,x:x+w]
img2 = roi.copy()

cv2.imshow("roi",img2)

key = cv2.waitKey(0)
print(key)
cv2.destroyAllWindows()