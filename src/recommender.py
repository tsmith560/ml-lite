# recommender.py

from utils import (
    recommend_random_beer,
    recommend_random_swag,
    recommend_random_song
)

def recommend_beer_by_tags(df, tags):
    if not tags:
        return recommend_random_beer(df)
    filtered = df[df['tags'].apply(lambda x: any(tag in x for tag in tags))]
    if filtered.empty:
        return recommend_random_beer(df)
    return recommend_random_beer(filtered)

def recommend_swag_by_tags(df, tags):
    if not tags:
        return recommend_random_swag(df)
    filtered = df[df['tags'].apply(lambda x: any(tag in x for tag in tags))]
    if filtered.empty:
        return recommend_random_swag(df)
    return recommend_random_swag(filtered)

def recommend_song_by_tags(df, tags):
    if not tags:
        return recommend_random_song(df)
    filtered = df[df['tags'].apply(lambda x: any(tag in x for tag in tags))]
    if filtered.empty:
        return recommend_random_song(df)
    return recommend_random_song(filtered)
