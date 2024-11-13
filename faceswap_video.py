#NeitXD
# faceswap_video.py
import requests
import os
import logging

logging.basicConfig(level=logging.INFO)
API_URL = os.getenv("API_URL")
API_TOKEN = os.getenv("API_TOKEN")

def swap_face_video(video_path):
    try:
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        files = {"video": open(video_path, "rb")}
        response = requests.post(API_URL, headers=headers, files=files)
        response.raise_for_status()
        return response.content
    except requests.exceptions.RequestException as e:
        logging.error(f"Face swap video failed: {e}")
        return None
