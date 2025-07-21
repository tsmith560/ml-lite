# Unified recommender system with unified output

from src.recommender import (
    recommend_random_beer,
    recommend_random_swag,
    recommend_random_song
)

def generate_miller_moment(beer_df, swag_df, song_df):
    beer = recommend_random_beer(beer_df)
    swag = recommend_random_swag(swag_df)
    song = recommend_random_song(song_df)

    moment = {
        "beer": beer,
        "swag": swag,
        "song": song
    }

    return moment
