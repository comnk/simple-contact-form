from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("index.html")

@app.errorhandler(sqlite3.IntegrityError)
def duplicate_entries(e):
    return redirect("/")

@app.route("/handle_data", methods=["GET", "POST"])
def handle_data():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["user_message"]

    if request.method == "POST":
        conn = sqlite3.connect("form_data.db", timeout=20)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO form_data (`user_name`, `email`, `txt`) VALUES (?,?,?)", (name, email, message))
        conn.commit()
        conn.close()


    return render_template("thank-you.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)