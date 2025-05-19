import yfinance as yf
import matplotlib.pyplot as plt

# Download Nvidia stock data for 2025
nvda = yf.Ticker("NVDA")
nvda_2025 = nvda.history(start="2025-01-01", end="2026-01-01")

# Plot the closing price
plt.figure(figsize=(10, 5))
plt.plot(nvda_2025.index, nvda_2025['Close'], label='NVDA Close Price')
plt.title('Nvidia Stock Prices in 2025')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.savefig('nvidia_stock_2025.png')
plt.close()

"nvidia_stock_2025.png saved."