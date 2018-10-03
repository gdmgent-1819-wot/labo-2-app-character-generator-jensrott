import firebase_admin
from firebase_admin import credentials, db
from sense_hat import SenseHat
from time import time, sleep
import os
import sys
import random
from math import floor, ceil

serviceAccountKey = '../serviceAccountKey.json'
databaseURL = 'https://wot1-34143.firebaseio.com/'

try:
    cred = credentials.Certificate(serviceAccountKey)
    default_app = firebase_admin.initialize_app(cred, options={
        'databaseURL' : databaseURL
    })
    
    firebase_ref_pi_arcade_characters = db.reference('patterns')

except:
    print('Unable to initialize Firebase: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

try:
    # SenseHat
    sense_hat = SenseHat()
    sense_hat.set_imu_config(False, False, False)

except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

# constants
COLOR_BLUE = (0, 0, 255)
COLOR_BLACK = (0, 0, 0)

# get random arcade matrix
def get_random_arcade_matrix():
    pattern = ''
    matrix = []
    for r in range(0,8):
        temp_str = ''
        for c in range(0, 4):
            temp_str = temp_str + str(round(random.random()))

        # spiegeling
        temp_str = temp_str + temp_str[::-1]
        pattern = pattern + temp_str                   


    for p in range(0,64):
        bit = int(pattern[p])
        color = COLOR_BLUE if bit == 1 else COLOR_BLACK
        matrix.append(color)

    return(matrix)

def fetch_pattern_from_firebase_and_display():

    # Reference to the database
    fb_patterns_db = firebase_ref_pi_arcade_characters.get()

    # Initialize an empty array where the patterns go into
    fb_pattern = []

    # If there are any patterns
    if fb_patterns_db is not None:
        for key, val in fb_patterns_db.items():
            patterns_from_db = val['patterns']
            fb_pattern.append(patterns_from_db)

        # If there is something in the fb_pattern
        while i < len(fb_pattern):
            i = 0;
            # Looping over the characters from the db and create one to display
            character = fb_pattern

            # Put the character we created on the sense hat
            sense_hat.set_pixels(character)

            # Add one to the counter so we see how many items are into the db
            i += 1 
            sleep(3)

    else:
        sense_hat.show_message = 'No patterns found..'
        print('No patterns found..')


def main():
    while True:
        fetch_pattern_from_firebase_and_display()
        # matrix = get_random_arcade_matrix()
        # sense_hat.set_pixels(matrix)

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sys.exit(0)