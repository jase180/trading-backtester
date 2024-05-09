import csv
from polygon import RESTClient

def get_historical_data_polygon(ticker):
    client = RESTClient("CP7pXlsPyynAOZbpAqB8OX98ANuOG4Os") #to be regenerated when program is public

    aggs = []
    for a in client.list_aggs(
        ticker,
        1,
        "day",
        "2022-05-15",
        "2024-05-08",
        limit=50000 ,
    ):
        aggs.append(a)

    return aggs

def write_to_csv(aggs, csv_file):
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['timestamp', 'open', 'high', 'low', 'close', 'volume'])  # Write header
        for agg in aggs:
            writer.writerow([agg.timestamp, agg.open, agg.high, agg.low, agg.close, agg.volume])

def main():
    ticker = 'COST'
    aggs = get_historical_data_polygon(ticker)
    write_to_csv(aggs, f"{ticker}.csv")

if __name__ == "__main__":
    main()