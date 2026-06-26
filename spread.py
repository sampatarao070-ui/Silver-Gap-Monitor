
import requests
import MetaTrader5 as mt5
import time

if not mt5.initialize():
    print("MT5 Initialization Failed")
    quit()

while True:
    try:
        url = "https://open-api.bingx.com/openApi/swap/v2/quote/ticker"

        params = {
            "symbol": "NCCOXAG2USD-USDT"
        }

        response = requests.get(url, params=params)
        data = response.json()

        bingx_price = float(data["data"]["lastPrice"])

        tick = mt5.symbol_info_tick("XAGUSD")

        if tick is None:
            print("MT5 Symbol not found")
            break

        mt5_price = tick.ask

        spread = bingx_price - mt5_price

        print("-" * 40)
        print("BingX Price :", bingx_price)
        print("MT5 Price   :", mt5_price)
        print("Spread      :", round(spread, 3))

        time.sleep(5)

    except Exception as e:
        print("Error:", e)
        break

mt5.shutdown()