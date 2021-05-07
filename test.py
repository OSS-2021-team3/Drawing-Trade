import pyupbit
import matplotlib.pyplot as plt

df = pyupbit.get_ohlcv('KRW-BTC',interval="minute30")
print(df)

plt.plot(df['close'])
plt.savefig('foo.png')