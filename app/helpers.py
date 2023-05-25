"""

This file contains helper functions for the application.

Placed here in the app folder for ease of use and so other files can easily import them.

"""

from datetime import datetime
from random import uniform, choice
from hashlib import md5

def get_random_datetime(year_gap=5):
    """Get a random datetime within the last few years."""

    now = datetime.now()
    then = now.replace(year=now.year - year_gap)
    random_timestamp = uniform(then.timestamp(), now.timestamp())

    return datetime.fromtimestamp(random_timestamp)

def generate_avatar(email, size=80):
    # Calculate the email hash
    email_hash = md5(email.encode('utf-8')).hexdigest()

    # Choose a random default avatar image
    default_avatars = [
        'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp', # Mystery person
        'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=identicon', # Geometric pattern
        'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=monsterid', # Monster
        'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=robohash', # Robot
        'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=wavatar', # Cartoon face
    ]
    default_avatar = choice(default_avatars)

    # Construct the Gravatar URL
    url = f'https://www.gravatar.com/avatar/{email_hash}?s={size}&d={default_avatar}'

    return url

test = get_random_datetime()
print (test)