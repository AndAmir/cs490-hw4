from flask import Flask, render_template
import os
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    tv_shows = ['Mythbusters', 'Spongebob', 'Phineas and Ferb', 'Teletubbies', 'Bob the Builder']
    tv_shows_images = ['https://upload.wikimedia.org/wikipedia/en/2/24/MythBusters_title_screen.jpg',
        'https://upload.wikimedia.org/wikipedia/en/thumb/2/22/SpongeBob_SquarePants_logo_by_Nickelodeon.svg/1200px-SpongeBob_SquarePants_logo_by_Nickelodeon.svg.png',
        'https://upload.wikimedia.org/wikipedia/en/thumb/6/6e/Phineas_and_Ferb_logo.svg/1200px-Phineas_and_Ferb_logo.svg.png',
        'https://upload.wikimedia.org/wikipedia/en/5/5a/Teletubbies_Logo.png',
        'https://upload.wikimedia.org/wikipedia/en/thumb/c/c6/Bob_the_Builder_logo.svg/1200px-Bob_the_Builder_logo.svg.png']
    return render_template(
        'index.html',
        my_shows = tv_shows,
        my_shows_len = len(tv_shows),
        my_shows_images = tv_shows_images,
        my_shows_images_len = len(tv_shows_images)
        )


app.run(
    port = 8080,
    host=os.getenv('IP','0.0.0.0'),
    debug=True
)
