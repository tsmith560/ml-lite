from recommender import (
    recommend_beer_by_tags,
    recommend_swag_by_tags,
    recommend_song_by_tags
)


def generate_miller_moment(beer_df, swag_df, song_df, tags=None):
    # Easter egg trigger phrase check
    if tags and any("not miller lite" in tag.lower() for tag in tags):
        # Hardcoded Easter egg items
        beer = {
            "name": "Miller. Lite.",
            "tagline": "Cursed Pyramid of Miller.",
            "abv": 4.2,
            "origin": "The Darkest Corner of Your Fridge",
        
        }

        swag = {
            "name": "The Cursed Beer-A-Mid",
            "description": "So many Miller Lites for the super Miller Lite fan!",
            "image_path": st.image('https://raw.githubusercontent.com/tsmith560/ml-lite/main/assets/miller_lite_beeramid.jpg')
        }

        song = {
            "title": "Fifteen Beers",
            "artist": "Johnny Paycheck",
            "spotify_url": "https://open.spotify.com/track/16af4zImXB5vP2Xat1ZV4l?si=9dbe65351ee4434b"
        }

        return {
            "beer": beer,
            "swag": swag,
            "song": song
        }

    # Normal recommender logic below
    beer = recommend_beer_by_tags(beer_df, tags)
    swag = recommend_swag_by_tags(swag_df, tags)
    song = recommend_song_by_tags(song_df, tags)

    return {
        "beer": beer,
        "swag": swag,
        "song": song
    }
