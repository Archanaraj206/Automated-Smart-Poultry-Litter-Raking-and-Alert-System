# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 23:21:01 2024

@author: Archana Raj
"""

import streamlit as st
import cv2
from twilio.rest import Client
import time
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO(r"C:\Users\Archana Raj\Desktop\360 PYTHON CODES\360 MY PROJECTS\best.pt")

# Function to perform inference on video frames and send alert after 2 minutes
def perform_inference_and_notify(video_file_path):
    start_time = time.time()
    cap = cv2.VideoCapture(video_file_path)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret:
            break
        
        # Perform inference on the frame
        results = model(frame)
        
        # Check if certain conditions are met (customize this based on your requirements)
        # For example, check if a certain class is detected
        
        # Check if 2 minutes have passed
        if time.time() - start_time >= 2 * 60:  # 2 minutes in seconds
            # Send SMS alert using Twilio
            send_sms_alert("Alert! litter raking not done.")  # You can customize the message
            break

    cap.release()

# Function to send SMS alert using Twilio
def send_sms_alert(body):
    # Twilio credentials
    # Twilio credentials
    account_sid = '******************************'
    auth_token = '******************************'
    twilio_number = '+********'
    to_number = '+91**********' # Change this to your phone number
 

    # Initialize Twilio client
    client = Client(account_sid, auth_token)

    # Send SMS
    message = client.messages.create(
        body="litter raking is not done",
        from_=twilio_number,
        to=to_number
    )
    st.write("SMS sent successfully!")

# Streamlit app
def main():
    st.title("YOLOv8 Poultry Farm Alert System")
    uploaded_file = st.file_uploader("Upload a video", type=["mp4", "avi"])

    if uploaded_file is not None:
        # Save the uploaded video file
        video_file_path = "uploaded_video.mp4"  # Save the file with a specific name
        with open(video_file_path, "wb") as f:
            f.write(uploaded_file.read())

        # Perform inference on the uploaded video
        perform_inference_and_notify(video_file_path)

if __name__ == "__main__":
    main()