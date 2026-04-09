import streamlit as st
import streamlit.components.v1 as components
import json
import base64

# 1. Page Config
st.set_page_config(
    page_title="ಸಹಾಯಕ AI", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Function to convert local image to base64
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return ""

# Load local images - Updated chatbot.jpg here
welcome_bg = get_base64("image_7.jpg") 
hero_bg = get_base64("image_825bf8.jpg")
arya_img = get_base64("chatbot.jpg") 

# 2. Hide Streamlit UI elements
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0rem !important;}
        iframe {border-radius: 0px !important;}
    </style>
""", unsafe_allow_html=True)

# 3. Data
recommendation_data = {
    "weather": "ಉತ್ತರ ಕರ್ನಾಟಕದಲ್ಲಿ ಈ ವಾರ ಒಣ ಹವಾಮಾನವಿರುತ್ತದೆ. ಮಣ್ಣಿನ ತೇವಾಂಶ ಕಾಪಾಡಲು ಮಲ್ಚಿಂಗ್ ಅಥವಾ ಹನಿ ನೀರಾವರಿ ಬಳಸಿ.",
    "options": [
        {"name": "ಮೇಕೆ ಸಾಕಣೆ", "income": "₹15,000 - ₹40,000 ಲಾಭ", "how": "ಸಣ್ಣ ಪ್ರಮಾಣದಲ್ಲಿ ಆರಂಭಿಸಿ ಹಬ್ಬಗಳ ಸಮಯದಲ್ಲಿ ನೇರ ಮಾರಾಟ ಮಾಡಿ ಉತ್ತಮ ಲಾಭ ಗಳಿಸಿ."},
        {"name": "ಜೋಳದ ಹಿಟ್ಟು ತಯಾರಿ", "income": "ಮೌಲ್ಯವರ್ಧಿತ ಮಾರಾಟ", "how": "ಜೋಳವನ್ನು ಹಿಟ್ಟು ಮಾಡಿ ಪ್ಯಾಕ್ ಮಾಡಿ ನಗರದ ಅಂಗಡಿಗಳಿಗೆ ಪೂರೈಸಿ."},
        {"name": "ಬೇವಿನ ಎಣ್ಣೆ ತಯಾರಿಕೆ", "income": "₹500/ಲೀಟರ್ ವರೆಗೆ", "how": "ಬೇವಿನ ಬೀಜ ಸಂಗ್ರಹಿಸಿ ಸಣ್ಣ ಗಾಣದ ಮೂಲಕ ಎಣ್ಣೆ ತೆಗೆದು ನೈಸರ್ಗಿಕ ಕೀಟನಾಶಕವಾಗಿ ಮಾರಿ."},
        {"name": "ಸೇಂದ್ರೀಯ ಗೊಬ್ಬರ", "income": "ತ್ಯಾಜ್ಯದಿಂದ ಆದಾಯ", "how": "ಕೃಷಿ ತ್ಯಾಜ್ಯದಿಂದ ಗೊಬ್ಬರ ಮಾಡಿ ನರ್ಸರಿಗಳಿಗೆ ಮತ್ತು ತೋಟಗಾರರಿಗೆ ಮಾರಾಟ ಮಾಡಿ."}
    ]
}

json_data = json.dumps(recommendation_data)

# 4. HTML/CSS/JS
html_code = f"""
<!DOCTYPE html>
<html lang="kn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root {{ --primary: #1b5e20; --accent: #ff9800; --bg: #f4f7f4; --text-dark: #333; }}
        * {{ box-sizing: border-box; }}
        body {{ margin: 0; font-family: 'Segoe UI', sans-serif; display: flex; height: 100vh; width: 100vw; background: var(--bg); overflow: hidden; }}

        #welcome-screen {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(rgba(0,0,0,0.4), rgba(0,0,0,0.6)), 
                        url('data:image/jpeg;base64,{welcome_bg}');
            background-size: cover; background-position: center;
            display: flex; flex-direction: column; justify-content: center; align-items: center; z-index: 2000; color: white;
            text-align: center;
        }}

        #sidebar {{ width: 280px; background: var(--primary); color: white; display: none; flex-direction: column; padding: 30px 20px; }}
        .nav-link {{ padding: 15px; margin: 5px 0; border-radius: 10px; cursor: pointer; color: white; text-decoration: none; }}
        .nav-link.active {{ background: var(--accent); font-weight: bold; }}

        .content-section {{ flex: 1; display: none; flex-direction: column; overflow-y: auto; width: 100%; }}
        
        .hero {{ 
            padding: 100px 20px; text-align: center; color: white;
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                        url('data:image/jpeg;base64,{hero_bg}');
            background-size: cover; background-position: center;
        }}

        .main-btn {{ background: var(--accent); color: white; border: none; padding: 18px 45px; border-radius: 50px; font-size: 1.2rem; font-weight: bold; cursor: pointer; transition: 0.3s; }}
        
        .arya-avatar {{ position: fixed; bottom: 30px; right: 30px; width: 110px; display: none; z-index: 3000; cursor: pointer; }}
        .arya-avatar img {{ width: 100%; filter: drop-shadow(0 5px 15px rgba(0,0,0,0.4)); border-radius: 50%; border: 3px solid white; }}
        
        #arya-chat-box {{ position: fixed; bottom: 150px; right: 35px; background: white; padding: 18px; border-radius: 15px; display: none; width: 260px; z-index: 3001; color: #333; box-shadow: 0 5px 20px rgba(0,0,0,0.2); }}

        .guide-box {{ background: white; margin: 20px 40px; padding: 25px; border-radius: 15px; border-left: 8px solid var(--accent); }}
    </style>
</head>
<body>

    <div id="welcome-screen">
        <h1 style="font-size: 4rem; margin: 0;">ನಿಮ್ಮ ಶ್ರಮ, ನಿಮ್ಮ ಬದುಕು – ಹವಾಮಾನ ಪ್ರತಿರೋಧಕ ಜೀವನೋಪಾಯದ ಶಕ್ತಿ!</h1>
        <p style="font-size: 1.5rem; margin-top: 20px; margin-bottom: 40px;">ಕೃಷಿ ಮತ್ತು ಜೀವನೋಪಾಯದ ಸಮಗ್ರ ಸಲಹೆಗಾರ</p>
        <button class="main-btn" onclick="startApp()">ಪ್ರಾರಂಭಿಸಿ (Start)</button>
    </div>

    <nav id="sidebar">
        <h2 style="padding-left:10px; margin-bottom: 30px;">ಸಹಾಯಕ AI</h2>
        <div class="nav-link active" onclick="showSection('dashboard', 'ಡ್ಯಾಶ್‌ಬೋರ್ಡ್')">🏠 ಡ್ಯಾಶ್‌ಬೋರ್ಡ್</div>
        <div class="nav-link" onclick="showSection('weather-page', 'ಹವಾಮಾನ')">☁️ ಹವಾಮಾನ</div>
        <div class="nav-link" onclick="showSection('roi-page', 'ಆದಾಯ ಮಾರ್ಗಗಳು')">💰 ಆದಾಯ ಮಾರ್ಗಗಳು</div>
    </nav>

    <div id="arya-chat-box"></div>
    <div id="arya-bot" class="arya-avatar" onclick="aryaGreet()">
        <img src="data:image/jpeg;base64,{arya_img}" alt="Arya AI">
    </div>

    <main id="dashboard" class="content-section">
        <div class="hero">
            <h1>ಮಾಹಿತಿಗಾಗಿ ಕೆಳಗಿನ ಬಟನ್ ಒತ್ತಿ</h1>
            <button class="main-btn" onclick="getAdvice()">🎤 ಮಾಹಿತಿ ಪಡೆಯಿರಿ</button>
        </div>
    </main>

    <div id="weather-page" class="content-section">
        <div style="background:var(--primary); color:white; padding:60px; text-align:center;"><h1>ಹವಾಮಾನ ಮಾಹಿತಿ</h1></div>
        <div id="weather-full" style="padding:40px;"></div>
    </div>

    <div id="roi-page" class="content-section">
        <div style="background:var(--primary); color:white; padding:60px; text-align:center;"><h1>ಜೀವನೋಪಾಯದ ಮಾರ್ಗಗಳು</h1></div>
        <div id="roi-full" style="padding:20px;"></div>
    </div>

    <script>
        const appData = {json_data};

        function showBubble(text) {{
            const box = document.getElementById('arya-chat-box');
            box.innerText = text;
            box.style.display = 'block';
            setTimeout(() => {{ box.style.display = 'none'; }}, 4000);
        }}

        function aryaGreet() {{ showBubble("ನಮಸ್ಕಾರ, ನಾನು ಆರ್ಯ."); }}

        function startApp() {{
            document.getElementById('welcome-screen').style.display = 'none';
            document.getElementById('sidebar').style.display = 'flex';
            document.getElementById('arya-bot').style.display = 'block';
            showSection('dashboard', 'ಡ್ಯಾಶ್‌ಬೋರ್ಡ್');
        }}

        function showSection(sectionId, navText) {{
            document.querySelectorAll('.content-section').forEach(s => s.style.display = 'none');
            document.getElementById(sectionId).style.display = 'flex';
        }}

        function getAdvice() {{
            document.getElementById('weather-full').innerHTML = `<div class="guide-box">${{appData.weather}}</div>`;
            const optionsHtml = appData.options.map(o => `
                <div class="guide-box">
                    <b>${{o.name}}</b><br><span>💰 ${{o.income}}</span><br><p>${{o.how}}</p>
                </div>
            `).join("");
            document.getElementById('roi-full').innerHTML = optionsHtml;
            showSection('roi-page', 'ಆದಾಯ ಮಾರ್ಗಗಳು');
        }}
    </script>
</body>
</html>
"""

components.html(html_code, height=1000, scrolling=True)
