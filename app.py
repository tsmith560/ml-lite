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
def set_background():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://raw.githubusercontent.com/tsmith560/ml-lite/main/assets/ml_lite_bg.jpg");
            background-repeat: repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

#Call set background function
set_background()

st.title("🍺 ML Lite: ML-Crafted Hot Summer Sizzle Generator")

st.markdown("""
## Welcome to **ML Lite: The Recommender You Can Crush All Summer**
This is your ultimate *cursed* summer recommender system. Enjoy it at your favorite local gas station.

Just enter a few tags that describe your vibe (e.g. `river`, `American`, `tragedy`, `country`, `ripped jeans`) and we’ll find the perfect light beer, summer anthem, and seasonal swag to match your moment.

⚠️ Warning: Perfectly accurate every time. Always. Flawless. Grab yourself a cold one!
""")


# Let user enter tags as free text, comma separated
tag_input = st.text_input("Enter your tags (comma separated):", "")

# Convert input string to list of tags (strip whitespace, lowercase)
tags = [tag.strip().lower() for tag in tag_input.split(",")] if tag_input else None

if st.button("Generate Miller Moment"):
    moment = generate_miller_moment(beer_df, swag_df, song_df, tags)

    st.markdown("### 🍺 YOUR MILLER MOMENT 🍺")
    st.write(f"**Beer:** {moment['beer']['name']} — {moment['beer']['tagline']} ({moment['beer']['abv']}% ABV, {moment['beer']['origin']})")
    st.write(f"**Swag:** {moment['swag']['name']} — {moment['swag']['description']}")
    st.image(moment['swag']['image_path'], width=300)
    st.write(f"**Song:** {moment['song']['title']} by {moment['song']['artist']}")
    st.write(f"[Listen on Spotify]({moment['song']['spotify_url']})")
