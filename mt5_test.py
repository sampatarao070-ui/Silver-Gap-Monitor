
import MetaTrader5 as mt5

# Connect to MT5
if not mt5.initialize():
    print("Initialization failed")
    print(mt5.last_error())
    quit()

symbol = "XAGUSD"

# Make sure the symbol is selected
mt5.symbol_select(symbol, True)

tick = mt5.symbol_info_tick(symbol)

if tick:
    print("MT5 Silver Price")
    print("Bid:", tick.bid)
    print("Ask:", tick.ask)
else:
    print("Could not get price")

mt5.shutdown()