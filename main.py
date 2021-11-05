import json
import random
import tweepy

from Listener import Listener

def load_keys():
    # Find the file and open it
    file = open(".secrets/keys.json")
        
    # Parse JSON
    keys = json.load(file)

    return keys
    
def main():
    keys = load_keys()
    streamer = Listener(
        keys["API"],
        keys["API_SECRET"],
        keys["ACCESS"],
        keys["ACCESS_SECRET"]
    )
    streamer.filter(track=['@g4t0r_w1z4rd'])

if __name__ == "__main__":
    main()
