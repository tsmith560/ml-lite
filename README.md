# ML Lite: The Recommender You Can Crush All Summer 🍺☀️📘

A lighthearted recommender system that pairs light beers, swag, and summer songs to create your perfect summer beer experience. Inspired by the simple joys of summer and a bit of playful randomness.


# Features
- Randomly recommends a beer, swag item, and song based on optional user tags
- Easter egg for a special Miller. Lite. moment with cursed swag and exclusive content
- Interactive Streamlit app for easy use and fun exploration
- Data-driven from curated CSV datasets


# Getting Started
Prerequisites:
Python 3.8+
Streamlit
pandas


# Installation:

# 1.) Clone this repository
git clone https://github.com/yourusername/ml-lite.git
cd ml-lite

# 2.) Install dependencies
pip install -r requirements.txt

# 3.) Run the app
streamlit run app.py

# Usage
- Run the app and type your preferred tags to filter recommendations.
- Hit the button to generate a random summer beer Moment.
- Can you find the easter egg?

# Project Structure

ml-lite/
├── data/           # CSV files for beers, swag, and songs
├── src/            # Python modules for recommendation logic
│   ├── recommender.py
│   ├── miller_moment.py
│   └── utils.py
├── app.py          # Streamlit app entry point
├── requirements.txt
└── README.md

# Datasets
- beer.csv: Contains beer data with attributes like name, tagline, ABV, origin, and tags.
- swag.csv: Contains swag items with name, description, tags, and image paths.
- song.csv: Contains song details including title, artist, tags, and Spotify links.

# License
MIT License — see LICENSE file for details.
