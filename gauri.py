import streamlit as st
import datetime
import time

# Page Config
st.set_page_config(page_title="❤️ One Month To Go ❤️", page_icon="🎉", layout="centered")

# Background styling
page_bg = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #ffdde1, #ee9ca7);
    color: #2b2b2b;
    font-family: 'Trebuchet MS', sans-serif;
}
h1, h2, h3 {
    text-align: center;
    color: #d63384;
}
.big-heart {
    font-size: 50px;
    text-align: center;
    margin: 20px 0;
}
.memory-box {
    background: rgba(255, 255, 255, 0.7);
    border-radius: 15px;
    padding: 30px 100px 30px 100px;
    margin: 20px 0;
    text-align: justify;
}
.countdown-container {
    display: flex;
    justify-content: center;
    gap: 15px;
    margin-top: 20px;
}
.countdown-box {
    background: white;
    border-radius: 12px;
    padding: 15px 25px;
    text-align: center;
    box-shadow: 2px 2px 10px rgba(0,0,0,0.15);
}
.countdown-number {
    font-size: 40px;
    font-weight: bold;
    color: #ff3366;
}
.countdown-label {
    font-size: 16px;
    color: #444;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Target Date
target_date = datetime.datetime(2025, 10, 28, 0, 0, 0)

# Title
st.markdown("<h1>⏳ One Month To Go! 🎂</h1>", unsafe_allow_html=True)
st.markdown("<div class='big-heart'>💖💫✨</div>", unsafe_allow_html=True)

# Lovely Message
st.markdown(
    """
    <div class='memory-box'>
    <h3>Bas ek mahina aur... 🎉</h3>
    <p>
    Meri jaan, aaj se exactly ek mahine baad aapka birthday aa raha hai 💕<br>
    Aur main already excited hoon aapke surprises ke liye! 🥰<br>
    Hihihi aapko kya laga mai website ke baare me bhool gaya...😎<br>
    Har memory aapke saath ek nayi kahani likhti hai -<br>
    Hamara vo first unexpected unwanted meetup 😂, woh JEE vaali baatein, <br>
    vo first call us din shaam ko chhat pr, aur hamara bhaiyaa se saiyaann tak ka safar 🤣, <br>
    sab kuch yaad karenge aapki birthday par 😍✨  
    </p>
    <p>Chaliye countdown shuru karte hain... aapke special din ke liye! 🎂🎁</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Countdown function
def countdown(target):
    now = datetime.datetime.now()
    diff = target - now
    days, seconds = diff.days, diff.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return days, hours, minutes, seconds

# Live countdown with placeholder
placeholder = st.empty()

while True:
    days, hours, minutes, seconds = countdown(target_date)
    with placeholder.container():
        st.markdown(
            f"""
            <div class='countdown-container'>
                <div class='countdown-box'>
                    <div class='countdown-number'>{days}</div>
                    <div class='countdown-label'>Days</div>
                </div>
                <div class='countdown-box'>
                    <div class='countdown-number'>{hours}</div>
                    <div class='countdown-label'>Hours</div>
                </div>
                <div class='countdown-box'>
                    <div class='countdown-number'>{minutes}</div>
                    <div class='countdown-label'>Minutes</div>
                </div>
                <div class='countdown-box'>
                    <div class='countdown-number'>{seconds}</div>
                    <div class='countdown-label'>Seconds</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class='memory-box'>
            <p style='font-size:18px;'>💌 Har second aapke SPECIAL DAY ki taraf ek aur step hai...💞<br>
            😚 Can't wait to celebrate YOU TURNING 19 MERI JAAANNNN! 🩷</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    time.sleep(1)
