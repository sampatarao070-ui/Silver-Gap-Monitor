
from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("spread_data.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM spreads")
    rows = cursor.fetchall()

    conn.close()

    if len(rows) == 0:
        return "No data found in database."

    latest = rows[-1]

    times = [row[1] for row in rows]
    spreads = [row[4] for row in rows]

    return render_template(
        "index.html",
        bingx=latest[2],
        mt5=latest[3],
        spread=latest[4],
        times=times,
        spreads=spreads
    )

if __name__ == "__main__":
    app.run(debug=True)