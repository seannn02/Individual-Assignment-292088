import pandas as pd
import yfinance as yf

users = {}

def register_user(email, password):
    if email in users:
        return False
    users[email] = password
    return True

def authenticate_user(email, password):
    return users.get(email) == password

def get_closing_prices(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data['Close']

def analyze_closing_prices(data):
    avg_price = data.mean()
    perc_change = ((data.iloc[-1] - data.iloc[0]) / data.iloc[0]) * 100
    high_price = data.max()
    low_price = data.min()
    return {
        "Average Closing Price": avg_price.item(),
        "Percentage Change (%)": perc_change.item(),
        "Highest Closing Price": high_price.item(),
        "Lowest Closing Price": low_price.item()
    }

def save_to_csv(email, ticker, analysis, filename):
    data = {"Email": [email], "Ticker": [ticker]}
    data.update({key: [value] for key, value in analysis.items()})
    df = pd.DataFrame(data)
    df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)

def read_from_csv(filename):
    try:
        data = pd.read_csv(filename)
        print(data.to_string(index=False))
    except FileNotFoundError:
        print("No saved data found.")

