import requests

API_KEY= "9F2PORCHWPLMBT6A"
#  
api_url = "https://www.alphavantage.co/" # step 1 base url
 
def get_stock_market(symbol,is_timeseries):
    query = f"query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(url=api_url+query)
    for key, value in response.json().items():
        # if key == "Time Series (Daily)":
            # continue
        # else:
            # print(key,value)
          if is_timeseries:
               print(key,value)
          else:
               if key == "Time Series (Daily)":
                    continue
    # print(response.json())

symbol = input("Enter the Symbol you want for the Stock Market API eg. (AMZN, IBM, GOGL):")
is_timeseries = False
get_stock_market(symbol,is_timeseries)