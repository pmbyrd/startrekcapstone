import csv
import random
import requests
from faker import Faker
from werkzeug.security import generate_password_hash
from datetime import datetime
import string

fake = Faker()


USERS_CSV_HEADERS = ['email', 'username', 'avatar', 'password', 'bio', 'first_name', 'last_name', 'location']
NUM_USERS = 500

def generate_bio():
    words = []
    for _ in range(5):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 10)))
        words.append(word)
    return ' '.join(words).capitalize() + '.'

def generate_users_csv(file_path):
    image_urls = [
        f"https://randomuser.me/api/portraits/{kind}/{i}.jpg"
        for kind, count in [("lego", 10), ("men", 100), ("women", 100)]
        for i in range(count)
    ]

    with open(file_path, 'w') as users_csv:
        users_writer = csv.DictWriter(users_csv, fieldnames=USERS_CSV_HEADERS)
        users_writer.writeheader()

        for i in range(NUM_USERS):
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            password_hash = generate_password_hash('password')

            users_writer.writerow(dict(
                email=email,
                username=fake.user_name(),
                avatar=random.choice(image_urls),
                password=password_hash,
                bio=' '.join([generate_bio() for _ in range(5)]),
                first_name=first_name,
                last_name=last_name,
                location=fake.city()
            ))

if __name__ == '__main__':
    generate_users_csv('app/trek_blueprints/users/generator/users.csv')

            