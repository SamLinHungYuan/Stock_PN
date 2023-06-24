import yfinance as yf

# 定義要獲取資料的台灣股票ISIN
stock_isin = '2330.TW'  # 這裡以台積電（股票代號：2330）的ISIN為例

# 定義起訖日期
start_date = '2023-01-01'
end_date = '2023-02-01'

# 使用yfinance庫來獲取台灣股票的日資料
stock_data = yf.download(stock_isin, start=start_date, end=end_date)

# 輸出獲取的資料
print(stock_data)
