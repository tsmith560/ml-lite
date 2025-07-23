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

st.title("🍺 ML Lite: Miller Moment Generator")

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
