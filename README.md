# 📍 Flask Geolocation Capture Project

A Python + Flask project that automatically captures a visitor's **location**, **IP address**, **browser info**, and **unique client ID**, then logs them for review. Admins can view entries in a secure dashboard with direct Google Maps links.

![Preview Diagram](flask_geolocation_diagram.png)

---

## 🚀 Features

✅ Auto location capture without button  
✅ Collects IP address, accuracy, browser, and UUID  
✅ Stores all logs in a CSV file  
✅ Admin dashboard with secure login  
✅ Google Maps integration for coordinates  
✅ "Copy Link" button for easy sharing  
🚫 No email / webhook included (by request)

---

## 📂 Project Structure

```
flask_geolocation_project/
├── app.py               # Flask backend
├── admin.json           # Admin credentials
├── templates/
│   ├── index.html       # Landing page (auto-capture)
│   ├── redirect.html    # Post-capture thank you
│   └── panel.html       # Admin panel (dark UI)
├── click_logs.csv       # Auto-generated log file
├── requirements.txt     # Python packages
└── flask_geolocation_diagram.png # Architecture image
```

---

## 🛠️ Installation

1. **Clone the repo**
```bash
git clone https://github.com/yourusername/flask-geolocation-capture.git
cd flask-geolocation-capture
```

2. **Create virtual environment (optional)**
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

- To change the admin credentials, edit `admin.json`:
```json
{
  "username": "admin",
  "password": "secret123"
}
```

---

## ▶️ Run the App

```bash
python app.py
```

Visit: [http://localhost:5000](http://localhost:5000)

---

## 🔐 Admin Panel

Go to: [http://localhost:5000/panel](http://localhost:5000/panel)  
Use the credentials from `admin.json` to login.

You can view all captured logs with location, accuracy, and browser details.

---

## 🧪 Test It Live

1. Share the main link (e.g. `http://localhost:5000`)
2. Ask a user to open it from their browser
3. Data gets silently logged and appears in the panel

---

## 📈 System Diagram

![Diagram](/scr/flask_geolocation_diagram.png)

---

## 📝 License

This project is for educational/demo purposes only. Not responsible for misuse.

---

## 💬 Support or Feedback?

If you want to add Telegram/Email/Webhook support, or deploy this publicly, open an issue or contact the author.
