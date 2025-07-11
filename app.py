from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("calendar.html")

@app.route("/events")
def get_events():
    # This endpoint can later return events from a DB
    return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)
