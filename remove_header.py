


with open("data/kaggle_data_set/stocks_latest/stock_prices_latest.csv",'r') as f:
    with open("updated_test.csv",'w') as f1:
        next(f) # skip header line
        for line in f:
            f1.write(line)