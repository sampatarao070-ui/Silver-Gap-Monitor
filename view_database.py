
import sqlite3

conn = sqlite3.connect("spread_data.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM spreads")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()