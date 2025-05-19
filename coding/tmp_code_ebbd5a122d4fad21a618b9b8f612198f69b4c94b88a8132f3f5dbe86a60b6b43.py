import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol
ticker_symbol = 'MSFT'

# Download the stock data for 2024
msft_data = yf.download(ticker_symbol, start='2024-01-01', end='2024-12-31')

# Plot the closing prices
plt.figure(figsize=(10, 6))
plt.plot(msft_data.index, msft_data['Close'], label='MSFT Close Price', color='blue')
plt.title('MSFT Stock Prices in 2024')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)

# Save the plot to a file
file_path = 'msft_stock_2024.png'
plt.savefig(file_path)
file_path