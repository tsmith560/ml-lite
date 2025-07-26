import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "src"))

#Streamlit basic app code
import streamlit as st

#Import Miller Moment
from miller_moment import generate_miller_moment
import pandas as pd

# Load data csv's
@st.cache_data
def load_data():
    beer_df = pd.read_csv("data/beer.csv")
    swag_df = pd.read_csv("data/swag.csv")
    song_df = pd.read_csv("data/song.csv")
    return beer_df, swag_df, song_df

beer_df, swag_df, song_df = load_data()

# Def set background function with hosted asset
import streamlit as st

# Set page config
st.set_page_config(page_title="ML Lite", layout="centered")

# Add custom CSS
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://raw.githubusercontent.com/tsmith560/ml-lite/main/assets/ml_lite_ml_mart_bg.jpg');
        background-repeat: no-repeat;
        background-size: 100% 100%;
        background-position: center;
        background-attachment: fixed;  
    }
    .opaque-box {
        background-color: rgba(255, 255, 0, 0.85);
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.4);
    }
    .title-text {
        font-size: 3em;
        color: #002868; /* Miller Lite Blue */
        font-family: Impact, Charcoal, sans-serif;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .subtitle-text {
        font-size: 1.25em;
        color: #BF0A30; /* Miller Lite Red */
        text-align: center;
        font-family: Comic Sans MS, cursive, sans-serif;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)


# Title + Description Section (wrapped in opaque box)
st.markdown("""
<div class="opaque-box">
    <div class="title-text">ML Lite: The Recommender You Can Crush All Summer</div>
    <div class="subtitle-text">Part NASCAR, part beer run, all machine learning.</div>
    <p>This app is the world's most questionable light beer recommender system. 
    It uses tags like <i>"summery"</i>, <i>"American"</i>, or <i>"cursed"</i> to pair you with 
    beers, songs, and moments that define a very specific energy. 
    Think: Miller Lite at 100°F in a Walmart parking lot.</p>
</div>
""", unsafe_allow_html=True)

# User Input for Tags
tag_input = st.text_input("Enter your tags (comma separated):", "")
tags = [tag.strip().lower() for tag in tag_input.split(",")] if tag_input else None

# Results Section (also wrapped in opaque box)
if st.button("Generate ML Moment"):
    moment = generate_miller_moment(beer_df, swag_df, song_df, tags)

    # Use a container with the CSS class
    st.markdown('<div class="opaque-yellow-box">', unsafe_allow_html=True)

    st.markdown("### 🍺 YOUR MILLER MOMENT 🍺")
    st.write(f"**Beer:** {moment['beer']['name']} — {moment['beer']['tagline']} ({moment['beer']['abv']}% ABV, {moment['beer']['origin']})")
    st.write(f"**Swag:** {moment['swag']['name']} — {moment['swag']['description']}")
    st.image(moment['swag']['image_path'], width=300)
    st.write(f"**Song:** {moment['song']['title']} by {moment['song']['artist']}")
    st.markdown(f"[Listen on Spotify]({moment['song']['spotify_url']})")  # Keep this markdown for clickable link

    st.markdown('</div>', unsafe_allow_html=True)
