import streamlit as st
import streamlit.components.v1 as components
import json
import base64

# 1. Page Config
st.set_page_config(page_title="ಸಹಾಯಕ AI", layout="wide", initial_sidebar_state="collapsed")

# Function to convert local image to base64
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return ""

# Load local images
hero_bg = get_base64("image_825bf8.jpg")
arya_img = get_base64("chatbot.jpg") 

# Hide Streamlit elements
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .block-container {padding: 0rem !important;}
    </style>
""", unsafe_allow_html=True)

# HTML/CSS Layout
html_code = f"""
<!DOCTYPE html>
<html lang="kn">
<head>
    <style>
        body {{ margin: 0; font-family: sans-serif; display: flex; height: 100vh; background: #f4f4f4; }}
        
        /* Sidebar */
        #sidebar {{ width: 250px; background: #1b5e20; color: white; padding: 20px; display: flex; flex-direction: column; }}
        .nav-link {{ padding: 15px; margin: 10px 0; background: #ff9800; border-radius: 5px; cursor: pointer; font-weight: bold; }}
        .nav-item {{ padding: 10px; cursor: pointer; }}
        
        /* Main Content */
        #main {{ flex: 1; padding: 20px; }}
        .hero {{ background: url('data:image/jpeg;base64,{hero_bg}'); background-size: cover; padding: 50px; text-align: center; color: white; border-radius: 10px; }}
        .main-btn {{ background: #ff9800; border: none; padding: 15px 30px; border-radius: 5px; color: white; font-weight: bold; cursor: pointer; }}
        
        /* Cards */
        .card-container {{ display: flex; gap: 20px; margin-top: 30px; }}
        .card {{ background: white; padding: 20px; border-radius: 10px; flex: 1; box-shadow: 0 2px 5px rgba(0,0,0,0.1); text-align: center; }}
    </style>
</head>
<body>
    <div id="sidebar">
        <h2>ಸಹಾಯಕ AI</h2>
        <div class="nav-link">🏠 ಡ್ಯಾಶ್‌ಬೋರ್ಡ್</div>
        <div class="nav-item">☁️ ಹವಾಮಾನ</div>
        <div class="nav-item">🌿 ಬೆಳೆ ಸಲಹೆ</div>
        <div class="nav-item">💰 20+ ಆದಾಯ ಮಾರ್ಗಗಳು</div>
    </div>
    
    <div id="main">
        <div class="hero">
            <h1>ಮಾಹಿತಿಗಾಗಿ ಕೆಳಗಿನ ಬಟನ್ ಒತ್ತಿ</h1>
            <button class="main-btn">🎤 ಮಾಹಿತಿ ಪಡೆಯಲು ಮಾತನಾಡಿ</button>
        </div>
        
        <div class="card-container">
            <div class="card"><h3>☁️ ಹವಾಮಾನ</h3><p>ಮಾಹಿತಿಗಾಗಿ ಕಾಯಲಾಗುತ್ತಿದೆ...</p></div>
            <div class="card"><h3>🌿 ಬೆಳೆ ಸಲಹೆ</h3><p>ನಿಮ್ಮ ಭೂಮಿಗೆ ಒಪ್ಪುವ ಬೆಳೆಗಳ ಪಟ್ಟಿ...</p></div>
            <div class="card"><h3>💰 20+ ಆದಾಯ ಮಾರ್ಗಗಳು</h3><p>ಸಂಪೂರ್ಣ ಸಂಪನ್ಮೂಲ ಬಳಕೆ ವಿವರ...</p></div>
        </div>
    </div>
</body>
</html>
"""

components.html(html_code, height=800)
