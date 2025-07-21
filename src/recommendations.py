# Define recommend random swag
def recommend_random_swag(df):
    item = df.sample(1).iloc[0]
    return {
        "name": item["name"],
        "description": item["description"],
        "image_path": item["image_path"]
    }

# Define recommend random beer
def recommend_random_beer(df):
    beer = df.sample(1).iloc[0]
    return {
        "name": beer["name"],
        "tagline": beer["tagline"],
        "abv": beer["abv"]
	"origin": beer["origin"]
    }

#Define recommend random song
def recommend_random_song(df):
    item = df.sample(1).iloc[0]
    return {
        "title": item["title"],
        "artist": item["artist"],
        "link": item["link"]
    }