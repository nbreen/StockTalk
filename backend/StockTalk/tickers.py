#imports
from get_all_tickers import get_tickers as gt
import os
import csv

stock_tickers = gt.get_tickers()

if os.path.exists("valid_tickers.csv"):
	os.remove("valid_tickers.csv")

with open("valid_tickers.csv", "w") as f:
	wr = csv.writer(f)
	for ticker in stock_tickers:
		wr.writerow([ticker])

f.close()

