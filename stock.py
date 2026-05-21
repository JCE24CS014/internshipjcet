
import requests

api_key = "d87e921r01ql0hsle1qgd87e921r01ql0hsle1r0"

symbol = "AAPL"

url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={api_key}"

response = requests.get(url)

data = response.json()

print("Current Price:", data['c'])
print("High Price:", data['h'])
print("Low Price:", data['l'])
print("Opening Price:", data['o'])
print("Previous Close:", data['pc'])