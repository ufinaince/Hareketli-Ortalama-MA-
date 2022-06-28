# Gerekli kütüphanelerin import işlemi
import pandas as pd
import yfinance as yf


# Yahoo Finance üzerinden ilgili hisse senedinin verilerine erişimi sağlayan fonksiyon
def dataImporter(symbol="", date='2017-01-01', inBist=True):
    if inBist:
        symbol = symbol + ".IS"
        df = yf.download(symbol,
                         start=date,
                         progress=False)

    else:
        df = yf.download(symbol,
                         start=date,
                         progress=False)
    return df


# APPLE hisse senedinin verilerini df adında bir dataframe'de tutmak
df = dataImporter("AAPL", inBist=False)

# Hisse senedinin kapanış değerlerinin görselleştirilmesi
df['Close'].plot()

# Hisse senedinin 20 günlük Hareketli Ortlamasının hesaplanması ve ardından görselleştirilmesi
df['Close'].rolling(window=20).mean().plot()

# Hisse senedinin 20 günlük Hareketli Ortlamasının ve normal değerlerinin görselleştirilmesi
df['Close'].plot(figsize=(10, 6))
df['Close'].rolling(window=20).mean().plot()

# Hisse senedinin 20 günlük Hareketli Ortlamasının hesaplanması ve dataframe'e yeni bir değişken olarak atanması
df['MA'] = df['Close'].rolling(window=20).mean()
