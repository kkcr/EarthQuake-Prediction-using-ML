from flask import Flask, render_template, request, redirect, url_for, flash
from flask import jsonify
import requests
import sqlite3
import numpy as np
import pickle
import requests
from datetime import datetime
now = datetime.now()
import pandas as pd
import os
import base64
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from geopy.distance import geodesic
app = Flask(__name__)
app.secret_key = "your_secret_key"

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Load ML Model
with open('rf_model.pkl', 'rb') as file:
    rf_model = pickle.load(file)

X_min = np.array([22.00200, 127.0004, 0.0, 1960.0, 1.0, 1.0, 5.0], dtype=np.float64)
X_max = np.array([55.7300, 158.995, 700.0, 2024.0, 12.0, 31.0, 86377.0], dtype=np.float64)

dict = {}  # Store user session data

DATABASE = 'database.db'

def init_db():
    """Initialize the database."""
    with sqlite3.connect(DATABASE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        conn.commit()

def get_location(lat, lon):
    api_key="........................"
    # lat1=lat #Original
    lat1=17.7771285  #End
    # lon1=lon  #Original
    lon1=83.3615678  #End
    #lon1=-8.193 #test
    #lat1=71.19 #test
    # adjustments = [(0, 0), (0.0005, 0.0005), (-0.0005, -0.0005), (0.001, 0.001), (-0.001, -0.001)]
    adjustments = [(0, 0), (0, 0), (-0,0),(0, 0), (-0, -0)]
    city_candidates = []
    for lat_offset, lon_offset in adjustments:
        new_lat, new_lon = lat1 + lat_offset, lon1 + lon_offset
        opencage_url = f"https://api.opencagedata.com/geocode/v1/json?q={new_lat}+{new_lon}&key={api_key}"
        try:
            response = requests.get(opencage_url, timeout=5)
            response.raise_for_status()
            data = response.json()
            if not data.get("results"):
                print(f"No results for {new_lat}, {new_lon}")
                continue
            for result in data["results"]:
                components = result.get("components", {})
                city = components.get("city") or \
                       components.get("town") or \
                       components.get("municipality") or \
                       components.get("_normalized_city")
                if city:
                    distance = geodesic((lat1, lon1), (new_lat, new_lon)).meters
                    city_candidates.append((city, distance, new_lat, new_lon))
        except Exception as e:
            print(f"Error with OpenCage API for {new_lat}, {new_lon}: {e}")
    if city_candidates:
        city_candidates.sort(key=lambda x: x[1])
        return city_candidates[0][0]
    return "Unknown"

def authenticate_gmail():
    """Authenticate and return the Gmail API service."""
    creds = None
    token_file = 'token.json'
    
    if os.path.exists(token_file):
        from google.oauth2.credentials import Credentials
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_file, 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def create_message(sender, to, subject, body_text):
    """Create an email message."""
    to = to.strip()  # Ensure no extra spaces
    if not to or "@" not in to:
        print(" Invalid recipient email:", to)  # Debugging
        return None  # Prevent sending invalid email

    message = MIMEText(body_text, 'html')
    message['From'] = sender
    message['To'] = to
    message['Subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode('utf-8')
    
    print(" Email prepared for:", to)  # Debugging
    return {'raw': raw_message}

def send_email(service, message):
    """Send the email via Gmail API."""
    if not message:
        print(" Email message is None. Skipping send.")
        return

    try:
        sent_message = service.users().messages().send(userId='me', body=message).execute()
        print(f" Message sent successfully: {sent_message['id']}")
    except HttpError as error:
        print(f" Gmail API Error: {error}")

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        user = request.form['user'].strip()
        email = request.form['email'].strip()
        password = request.form['password'].strip()

        try:
            with sqlite3.connect(DATABASE) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO users (user, email, password) VALUES (?, ?, ?)", (user, email, password))
                conn.commit()
                flash('Sign up successful! Please log in.', 'success')
                return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Email already exists. Please log in.', 'error')
            return redirect(url_for('login'))
    
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_input = request.form['email'].strip()
        password = request.form['password'].strip()

        with sqlite3.connect(DATABASE) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT user, email FROM users WHERE (email = ? OR user = ?) AND password = ?", 
                           (user_input, user_input, password))
            user = cursor.fetchone()

            if user:
                dict["email"] = user[1]
                dict["user"] = user[0]
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid email/username or password!', 'error')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    email = dict.get("email", "Unknown")
    user = dict.get("user", "Guest")
    
    print(f" Dashboard Email: {email}")  # Debugging
    return render_template('dashboard.html', email=email, user=user)

@app.route("/getdata")
def jonkay():
    lat = round(float(request.args.get("lat")), 3)
    lon = round(float(request.args.get("lon")), 3)

    depth = 10  # Placeholder for elevation data
    now = datetime.now()
    year, month, day = now.year, now.month, now.day
    time_in_seconds = now.hour * 3600 + now.minute * 60 + now.second

    feature_names = ['latitude', 'longitude', 'depth', 'year', 'month', 'day', 'time_in_seconds']
    InputX = np.array([[lat, lon, depth, year, month, day, time_in_seconds]], dtype=np.float64)
    InputX_norm = (InputX - X_min) / (X_max - X_min)
    predicted_magnitude = rf_model.predict(InputX_norm)[0]

    print(f"Predicted Magnitude: {predicted_magnitude:.2f}")  

    city=get_location(lat,lon)
    print(city)

    if predicted_magnitude > 2:
        service = authenticate_gmail()
        sender_email = "capstoneuseonly@gmail.com"
        recipient_email = dict.get("email", "").strip()
        recipient_name = dict.get("user", "User")

        if not recipient_email:
            print(" No recipient email found. Skipping email alert.")
            return "No recipient email found", 400

        subject = "Earthquake Alert"
        body_text = "\n".join([
    f"<p style='font-size:16px; margin-top:5px;'>Dear {recipient_name},</p>",
    f"<p style='font-size:16px; margin-top:5px;'>We hope you are safe.An earthquake with a predicted magnitude of <b style='font-size:18px; color:red;'>{predicted_magnitude:.2f}</b> has been detected near your location.</p>",
    "<p style='font-size:16px; margin-top:7px;'><b>Important Information:</b></p>",
    "<ul style='font-size:16px; margin-top:5px;'>",
    "<li>This prediction is based on historical earthquake records and past data analysis.</li>",
    "<li>Not all earthquakes can be detected in advance.</li>",
    "<li>Earthquake alerts are not supported in all areas.</li>",
    "<li>Magnitude and shaking intensity estimates may have errors.</li>",
    "<li>You may or may not feel the predicted magnitude.</li>",
    "</ul>",
    "<p style='font-size:16px; margin-top:7px;'><b>Note:</b> <span style='color:blue;'>This prediction does not guarantee the occurrence of the disaster, but if it happens, it is likely to be at the estimated magnitude.</span></p>",
    "<p style='font-size:16px; margin-top:7px;'>We recommend staying alert and following safety measures. If you need assistance, please reach out to local authorities.</p>",
    "<p style='font-size:16px; margin-top:5px;'>Stay safe,</p>",
    "<p style='font-size:16px; font-weight:bold; margin-top:3px;'>Team Save-Life</p>"
])

        message = create_message(sender_email, recipient_email, subject, body_text)
        send_email(service, message)
        
    return render_template("home2.html", value=predicted_magnitude, email=dict["email"], user=dict["user"], lat=lat, lon=lon, city=city)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
