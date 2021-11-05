#! /usr/bin/python

import tweepy
import random
import spacy
import search
import json

nlp = spacy.load("data/model-best")

class Messenger():
    
    def __init__(self, message, status):
        # Find the file and open it
        file = open(".secrets/keys.json")
        
        # Parse JSON
        keys = json.load(file)
        
        # Log in
        auth = tweepy.OAuthHandler(
            keys["API"],
            keys["API_SECRET"]
        )
        auth.set_access_token(
            keys["ACCESS"],
            keys["ACCESS_SECRET"]
        )
        
        api = tweepy.API(auth)
        api.update_status(
            status=message,
            in_reply_to_status_id=status.id,
            auto_populate_reply_metadata=True
        )
        

class Listener(tweepy.Stream): # <-- "Inheritance"

    def on_status(self, status):
        self.determine_genres(status)

    def determine_genres(self, status):
        prediction = nlp(status.text.lower())
        predictions = prediction.cats
        predictions = [predict for predict in predictions if predictions[predict] > .8]
        try:
            prediction = random.choice(predictions)
            # Break the following out by title, artist in separate
            # variables
            result = random.choice(self.search_genre(prediction))
            Messenger(
                f'Try "{result[1]}" by {result[0]}; it\'s {prediction}.',
                status
            )
        except IndexError:
            print("I don't know that one!")
    
    def search_genre(self, genre):
        artist_id = search.by_tag(genre)
        return search.by_artist_id(artist_id) # <-- returns many
