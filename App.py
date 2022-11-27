import sqlite3
from flask import Flask, request, render_template

app = Flask(__name__)
app.secret_key = "!@#$%)(*&^~"

@app.route("/searching", methods=["GET", "POST"])
def hello():
    if request.method == "POST" and "bar" in request.form:
        s = request.form.get("bar")
        sb = s.lower()
        con=sqlite3.connect("db")
        c = con.cursor()
        c.execute("SELECT * FROM websites WHERE name LIKE (?)", (sb,))
        items = c.fetchall()
        con.commit()
        con.close()
        return render_template("results.html", messages = items)
    return render_template("index.html")

app.run(port=5000)
