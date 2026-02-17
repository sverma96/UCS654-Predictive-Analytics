from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import smtplib
from email.message import EmailMessage
import os
from topsis.topsis import topsis  # from your package

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    file = request.files["file"]
    weights = request.form["weights"]
    impacts = request.form["impacts"]
    email = request.form["email"]

    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    output_path = os.path.join(UPLOAD_FOLDER, "result.csv")

    file.save(input_path)

    # Convert weights and impacts
    weights = [float(w) for w in weights.split(",")]
    impacts = impacts.split(",")

    # Run TOPSIS
    topsis(input_path, weights, impacts, output_path)

    # Send email
    send_email(email, output_path)

    return "Result sent to email successfully!"

def send_email(receiver_email, file_path):
    sender_email = "abc@gmail.com"
    sender_password = "abcd efgh ijkl mnop"


    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Please find the TOPSIS result attached.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="result.csv",
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

if __name__ == "__main__":
    app.run(debug=True)
