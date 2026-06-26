
import sqlite3
import requests
import MetaTrader5 as mt5
import time
from datetime import datetime

# -------------------------
# Connect to SQLite
# -------------------------
conn = sqlite3.connect("spread_data.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS spreads (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    bingx_price REAL,
    mt5_price REAL,
    spread REAL
)
""")

conn.commit()

# -------------------------
# Connect to MT5
# -------------------------
if not mt5.initialize():
    print("MT5 Initialization Failed")
    quit()

# -------------------------
# Run Forever
# -------------------------
while True:

    # -------- BingX Price --------
    url = "https://open-api.bingx.com/openApi/swap/v2/quote/ticker"

    params = {
        "symbol": "NCCOXAG2USD-USDT"
    }

    response = requests.get(url, params=params)
    data = response.json()

    bingx_price = float(data["data"]["lastPrice"])

    # -------- MT5 Price --------
    tick = mt5.symbol_info_tick("XAGUSD")

    mt5_price = tick.bid

    # -------- Spread --------
    spread = round(bingx_price - mt5_price, 3)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # -------- Save to Database --------
    cursor.execute(
        """
        INSERT INTO spreads
        (timestamp,bingx_price,mt5_price,spread)
        VALUES (?,?,?,?)
        """,
        (timestamp, bingx_price, mt5_price, spread)
    )

    conn.commit()

    print("-----------------------------------")
    print("Time :", timestamp)
    print("BingX :", bingx_price)
    print("MT5   :", mt5_price)
    print("Spread:", spread)

    time.sleep(5) 