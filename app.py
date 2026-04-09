import streamlit as st
import streamlit.components.v1 as components
import json
import base64

# 1. Page Config for Maximum Width
st.set_page_config(
    page_title="ಸಹಾಯಕ AI", 
    layout="wide", 
    initial_sidebar_state="collapsed"
)

# Function to convert local image to base64 for HTML embedding
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Load your local images
# Ensure these files are in the same folder as your script
try:
    welcome_bg = get_base64("image_825efe.jpg")  # Your requested Welcome Background
    hero_bg = get_base64("image_825bf8.jpg")     # Dashboard Hero Background
    arya_img = get_base64("image_8d350a.jpg")    # Arya Chatbot Image
except FileNotFoundError:
    welcome_bg = ""
    hero_bg = ""
    arya_img = ""

# 2. Hide Streamlit Header/Footer
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0rem !important;}
        iframe {border-radius: 0px !important;}
    </style>
""", unsafe_allow_html=True)

# 3. Backend Data
recommendation_data = {
    "weather": "ಉತ್ತರ ಕರ್ನಾಟಕದಲ್ಲಿ ಈ ವಾರ ಒಣ ಹವಾಮಾನವಿರುತ್ತದೆ. ಮಣ್ಣಿನ ತೇವಾಂಶ ಕಾಪಾಡಲು ಮಲ್ಚಿಂಗ್ ಅಥವಾ ಹನಿ ನೀರಾವರಿ ಬಳಸಿ.",
    "options": [
        {"name": "ಮೇಕೆ ಸಾಕಣೆ", "income": "₹15,000 - ₹40,000 ಲಾಭ", "how": "ಸಣ್ಣ ಪ್ರಮಾಣದಲ್ಲಿ ಆರಂಭಿಸಿ ಹಬ್ಬಗಳ ಸಮಯದಲ್ಲಿ ನೇರ ಮಾರಾಟ ಮಾಡಿ ಉತ್ತಮ ಲಾಭ ಗಳಿಸಿ."},
        {"name": "ಜೋಳದ ಹಿಟ್ಟು ತಯಾರಿ", "income": "ಮೌಲ್ಯವರ್ಧಿತ ಮಾರಾಟ", "how": "ಜೋಳವನ್ನು ಹಿಟ್ಟು ಮಾಡಿ ಪ್ಯಾಕ್ ಮಾಡಿ ನಗರದ ಅಂಗಡಿಗಳಿಗೆ ಪೂರೈಸಿ."},
        {"name": "ಬೇವಿನ ಎಣ್ಣೆ ತಯಾರಿಕೆ", "income": "₹500/ಲೀಟರ್ ವರೆಗೆ", "how": "ಬೇವಿನ ಬೀಜ ಸಂಗ್ರಹಿಸಿ ಸಣ್ಣ ಗಾಣದ ಮೂಲಕ ಎಣ್ಣೆ ತೆಗೆದು ನೈಸರ್ಗಿಕ ಕೀಟನಾಶಕವಾಗಿ ಮಾರಿ."},
        {"name": "ಸೇಂದ್ರೀಯ ಗೊಬ್ಬರ", "income": "ತ್ಯಾಜ್ಯದಿಂದ ಆದಾಯ", "how": "ಕೃಷಿ ತ್ಯಾಜ್ಯದಿಂದ ಗೊಬ್ಬರ ಮಾಡಿ ನರ್ಸರಿಗಳಿಗೆ ಮತ್ತು ತೋಟಗಾರರಿಗೆ ಮಾರಾಟ ಮಾಡಿ."},
        {"name": "ನಾಟಿ ಕೋಳಿ ಸಾಕಣೆ", "income": "ಪ್ರತಿದಿನದ ಆದಾಯ", "how": "ಕೋಳಿ ಸಾಕಿ ಮೊಟ್ಟೆ ಮತ್ತು ಮಾಂಸವನ್ನು ಸ್ಥಳೀಯ ಸಂತೆಗಳಲ್ಲಿ ಮಾರಿ."},
        {"name": "ಹೈನುಗಾರಿಕೆ (Dairy)", "income": "ಮಾಸಿಕ ಹಾಲಿನ ಆದಾಯ", "how": "ಹಾಲಿನ ಡೈರಿಗೆ ಹಾಲು ನೀಡಿ ಹಾಗೂ ಸಗಣಿಯಿಂದ ಜೀವಾಮೃತ ಮಾಡಿ ಮಾರಾಟ ಮಾಡಿ."},
        {"name": "ಜೇನು ಸಾಕಣೆ", "income": "ಶುದ್ಧ ಜೇನಿನ ಲಾಭ", "how": "ತೋಟದ ಸುತ್ತ ಜೇನು ಪೆಟ್ಟಿಗೆ ಇಟ್ಟು ಜೇನು ಸಂಗ್ರಹಿಸಿ ಔಷಧೀಯ ರೂಪದಲ್ಲಿ ಮಾರಾಟ ಮಾಡಿ."},
        {"name": "ಕೃಷಿ ಪ್ರವಾಸೋದ್ಯಮ", "income": "ವಾರಾಂತ್ಯದ ಆದಾಯ", "how": "ನಗರದ ಜನರಿಗೆ ಹಳ್ಳಿ ಊಟ, ಎತ್ತಿನ ಗಾಡಿ ಸವಾರಿ ಮತ್ತು ತೋಟದ ವೀಕ್ಷಣೆ ಪ್ಯಾಕೇಜ್ ನೀಡಿ."}
    ]
}

json_data = json.dumps(recommendation_data)

# 4. Integrated HTML/CSS/JS
html_code = f"""
<!DOCTYPE html>
<html lang="kn">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        :root {{ --primary: #1b5e20; --accent: #ff9800; --bg: #f4f7f4; --text-dark: #333; }}
        * {{ box-sizing: border-box; }}
        body {{ margin: 0; font-family: 'Segoe UI', sans-serif; display: flex; height: 100vh; width: 100vw; background: var(--bg); overflow: hidden; color: var(--text-dark); }}

        /* Welcome Page with Local Image Base64 */
        #welcome-screen {{
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.7)), 
                        url('data:image/jpeg;base64,{welcome_bg}');
            background-size: cover; background-position: center;
            display: flex; flex-direction: column; justify-content: center;
            align-items: center; z-index: 2000; color: white;
            text-shadow: 2px 2px 10px rgba(0,0,0,0.5); text-align: center;
        }}

        #sidebar {{ width: 280px; background: var(--primary); color: white; display: none; flex-direction: column; padding: 30px 20px; box-shadow: 4px 0 15px rgba(0,0,0,0.2); }}
        .nav-link {{ padding: 15px; margin: 5px 0; border-radius: 10px; cursor: pointer; transition: 0.3s; color: white; text-decoration: none; }}
        .nav-link.active {{ background: var(--accent); font-weight: bold; }}

        .content-section {{ flex: 1; display: none; flex-direction: column; overflow-y: auto; padding-bottom: 50px; width: 100%; }}
        
        .hero {{ 
            padding: 100px 20px; text-align: center; color: white; width: 100%;
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
                        url('data:image/jpeg;base64,{hero_bg}');
            background-size: cover; background-position: center;
        }}

        .main-btn {{ background: var(--accent); color: white; border: none; padding: 18px 45px; border-radius: 50px; font-size: 1.2rem; font-weight: bold; cursor: pointer; box-shadow: 0 5px 15px rgba(0,0,0,0.3); margin-top: 15px; transition: 0.3s; }}
        
        .arya-avatar {{ position: fixed; bottom: 30px; right: 30px; width: 110px; display: none; z-index: 3000; cursor: pointer; }}
        .arya-avatar img {{ width: 100%; filter: drop-shadow(0 5px 15px rgba(0,0,0,0.4)); }}
        
        #arya-chat-box {{ position: fixed; bottom: 150px; right: 35px; background: white; padding: 18px; border-radius: 15px; box-shadow: 0 5px 20px rgba(0,0,0,0.2); display: none; width: 260px; z-index: 3001; line-height: 1.6; color: #333; }}

        .guide-box {{ background: white; margin: 20px 40px; padding: 25px; border-radius: 15px; border-left: 8px solid var(--accent); box-shadow: 0 4px 15px rgba(0,0,0,0.05); }}
        .card-container {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; padding: 40px; }}
        .card {{ background: white; padding: 30px; border-radius: 20px; text-align: center; cursor: pointer; box-shadow: 0 5px 20px rgba(0,0,0,0.05); border-top: 6px solid var(--accent); transition: 0.3s; }}
    </style>
</head>
<body>

    <div id="welcome-screen">
        <h1 style="font-size: 4rem; margin: 0;">ನಿಮ್ಮ ಹೊಲ, ನಿಮ್ಮ ಬದುಕು</h1>
        <p style="font-size: 1.5rem; margin-top: 20px; margin-bottom: 40px;">ಕೃಷಿ ಮತ್ತು ಜೀವನೋಪಾಯದ ಸಮಗ್ರ ಸಲಹೆಗಾರ</p>
        <button class="main-btn" onclick="startApp()">ಪ್ರಾರಂಭಿಸಿ (Start)</button>
    </div>

    <nav id="sidebar">
        <h2 style="padding-left:10px; margin-bottom: 30px;">ಸಹಾಯಕ AI</h2>
        <div class="nav-link active" onclick="showSection('dashboard', 'ಡ್ಯಾಶ್‌ಬೋರ್ಡ್')">🏠 ಡ್ಯಾಶ್‌ಬೋರ್ಡ್</div>
        <div class="nav-link" onclick="showSection('weather-page', 'ಹವಾಮಾನ')">☁️ ಹವಾಮಾನ</div>
        <div class="nav-link" onclick="showSection('crop-page', 'ಬೆಳೆ ಸಲಹೆ')">🌱 ಬೆಳೆ ಸಲಹೆ</div>
        <div class="nav-link" onclick="showSection('roi-page', 'ಆದಾಯ ಮಾರ್ಗಗಳು')">💰 ಆದಾಯ ಮಾರ್ಗಗಳು</div>
    </nav>

    <div id="arya-chat-box"></div>
    <div id="arya-bot" class="arya-avatar" onclick="aryaGreet()">
        <img src="data:image/jpeg;base64,{arya_img}" alt="Arya AI">
    </div>

    <main id="dashboard" class="content-section">
        <div class="hero">
            <h1 style="font-size: 2.5rem;">ಮಾಹಿತಿಗಾಗಿ ಕೆಳಗಿನ ಬಟನ್ ಒತ್ತಿ</h1>
            <button class="main-btn" onclick="getAdvice()">🎤 ಮಾಹಿತಿ ಪಡೆಯಿರಿ</button>
        </div>
        <div class="card-container">
            <div class="card" onclick="showSection('weather-page', 'ಹವಾಮಾನ')"><h3>☁️ ಹವಾಮಾನ ವರದಿ</h3><p>ಇಂದಿನ ವಾತಾವರಣದ ಬಗ್ಗೆ ತಿಳಿಯಿರಿ</p></div>
            <div class="card" onclick="showSection('crop-page', 'ಬೆಳೆ ಸಲಹೆ')"><h3>🌱 ಬೆಳೆ ಸಲಹೆ</h3><p>ಮಣ್ಣಿಗೆ ಸೂಕ್ತವಾದ ಬೆಳೆಗಳು</p></div>
            <div class="card" onclick="showSection('roi-page', 'ಆದಾಯ ಮಾರ್ಗಗಳು')"><h3>💰 ಆದಾಯ ಮಾರ್ಗಗಳು</h3><p>ಹೆಚ್ಚುವರಿ ಲಾಭ ಗಳಿಸುವ ದಾರಿ</p></div>
        </div>
    </main>

    <div id="weather-page" class="content-section">
        <div style="background:var(--primary); color:white; padding:60px; text-align:center;"><h1>ಹವಾಮಾನ ಮಾಹಿತಿ</h1></div>
        <div id="weather-full" style="padding:40px;">ಮಾಹಿತಿಗಾಗಿ ಮೈಕ್ ಬಟನ್ ಬಳಸಿ.</div>
    </div>

    <div id="roi-page" class="content-section">
        <div style="background:var(--primary); color:white; padding:60px; text-align:center;"><h1>ಜೀವನೋಪಾಯದ ಮಾರ್ಗಗಳು</h1></div>
        <div id="roi-full" style="padding:20px;"></div>
    </div>

    <script>
        const appData = {json_data};

        function showBubble(text, duration = 4000) {{
            const box = document.getElementById('arya-chat-box');
            box.innerText = text;
            box.style.display = 'block';
            setTimeout(() => {{ box.style.display = 'none'; }}, duration);
        }}

        function aryaGreet() {{ showBubble("ನಮಸ್ಕಾರ, ನಾನು ಆರ್ಯ. ನಿಮಗೆ ಯಾವ ಮಾಹಿತಿ ಬೇಕು?"); }}

        function startApp() {{
            document.getElementById('welcome-screen').style.display = 'none';
            document.getElementById('sidebar').style.display = 'flex';
            document.getElementById('arya-bot').style.display = 'block';
            showSection('dashboard', 'ಡ್ಯಾಶ್‌ಬೋರ್ಡ್');
            showBubble("ಸಹಾಯಕ ಎ ಐ ಗೆ ಸ್ವಾಗತ!");
        }}

        function showSection(sectionId, navText) {{
            document.querySelectorAll('.content-section').forEach(s => s.style.display = 'none');
            document.getElementById(sectionId).style.display = 'flex';
        }}

        function getAdvice() {{
            showBubble("ಮಾಹಿತಿಯನ್ನು ಸಿದ್ಧಪಡಿಸುತ್ತಿದ್ದೇನೆ...");
            document.getElementById('weather-full').innerHTML = `<div class="guide-box">${{appData.weather}}</div>`;
            const optionsHtml = appData.options.map(o => `
                <div class="guide-box">
                    <b style="color:var(--primary); font-size:1.1rem;">${{o.name}}</b><br>
                    <span>💰 ${{o.income}}</span><br>
                    <p style="margin-top:10px;">💡 <b>ವಿವರ:</b> ${{o.how}}</p>
                </div>
            `).join("");
            document.getElementById('roi-full').innerHTML = optionsHtml;
            showSection('roi-page', 'ಆದಾಯ ಮಾರ್ಗಗಳು');
            showBubble("ನಿಮಗಾಗಿ ವಿವರವಾದ ಪಟ್ಟಿ ಸಿದ್ಧವಾಗಿದೆ.");
        }}
    </script>
</body>
</html>
"""

# 5. Render to Streamlit
components.html(html_code, height=1000, scrolling=True)
