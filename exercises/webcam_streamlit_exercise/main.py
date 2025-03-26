import streamlit as st
import cv2, time

st.title("Motion Detector")
button = st.button("Start")

if button:
    streamlit_image = st.empty()
    webcam = cv2.VideoCapture(0)

    while True:
        current_day = time.strftime("%A")
        current_time = time.strftime("%H:%M:%S")
        check, frame = webcam.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        cv2.putText(img=frame, text=current_day, org=(50, 50)
                    , fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(255, 0, 0), thickness=2)

        cv2.putText(img=frame, text=current_time, org=(60, 130)
                    , fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(255, 0, 0), thickness=2)

        streamlit_image.image(frame)
