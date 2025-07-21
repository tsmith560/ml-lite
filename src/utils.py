def recommend_random_beer(df):
    item = df.sample(1).iloc[0]
    return {
        "name": item["name"],
        "tagline": item["tagline"],
        "abv": item["abv"],
        "origin": item["origin"]
    }

def recommend_random_swag(df):
    item = df.sample(1).iloc[0]
    return {
        "name": item["name"],
        "description": item["description"],
        "image_path": item["image_path"]
    }

def recommend_random_song(df):
    item = df.sample(1).iloc[0]
    return {
        "title": item["title"],
        "artist": item["artist"],
        "spotify_url": item["spotify_url"]
    }
