
import requests

url = "https://open-api.bingx.com/openApi/swap/v2/quote/ticker"

params = {
    "symbol": "NCCOXAG2USD-USDT"
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)
print(response.text)