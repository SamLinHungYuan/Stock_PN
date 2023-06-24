## 相關參考資源

- [talib 參考網站](https://havocfuture.tw/blog/python-indicators-talib)：這個網站提供了有關使用 talib 庫計算技術指標的相關資訊。
- [亞力電機的股票參考網站](https://www.wantgoo.com/stock/1514/technical-chart)：您可以在這個網站上查看亞力電機（股票代號 1514）的技術圖表和相關資訊。
- [DataFrame 的參考網站](https://www.learncodewithmike.com/2020/11/python-pandas-dataframe-tutorial.html)：這個網站提供了有關使用 Pandas 的 DataFrame 進行資料操作和分析的教學資源。

## 需求

1. 驗證 talib 是否與現有股票的數據一致。
2. 寫一個判斷的函數，根據以下條件計算最新的日 K 棒，並返回相應數值：

   - 當日 K 棒最低價大於等於上布林價格，返回 0。
   - 當日 K 棒最高價小於等於上布林價格，且最低價大於等於中布林價格，返回 1。
   - 當日 K 棒最高價小於等於中布林價格，且最低價大於等於下布林價格，返回 2。
   - 當日 K 棒最高價小於等於上下布林價格，返回 3。
   - 如果以上條件都不符合，返回 5。

   這個函數使用 Python 和 talib 库來計算布林通道值並判斷符合的條件。