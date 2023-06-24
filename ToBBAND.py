import getStockData as stock_data


def toBBAND(data):
    data = data.reset_index() 
    for index, row in data.iterrows():
        print(row['Date'],row['Open'])
    return 0


if __name__ == '__main__':
    data = stock_data.getStockData()
    result = toBBAND(data)
    print(f"result={result}")
