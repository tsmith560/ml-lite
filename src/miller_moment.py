from .recommender import (
    recommend_beer_by_tags,
    recommend_swag_by_tags,
    recommend_song_by_tags
)

def generate_miller_moment(beer_df, swag_df, song_df, tags=None):
    beer = recommend_beer_by_tags(beer_df, tags)
    swag = recommend_swag_by_tags(swag_df, tags)
    song = recommend_song_by_tags(song_df, tags)

    return {
        "beer": beer,
        "swag": swag,
        "song": song
    }
