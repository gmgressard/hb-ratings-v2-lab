"""seed the database"""
import os
import json
import crud
import model
import server 

from random import choice, randint
from datetime import datetime


os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
    # TODO: get the title, overview, and poster_path from the movie
    # dictionary.
    title = movie.get("title")
    overview = movie.get("overview")
    poster_path = movie.get("poster_path")
    #  Then, get the release_date and convert it to a
    # datetime object with datetime.strptime
    release_date_str = movie.get("release_date")
    format_date = "%Y-%m-%d"
    release_date = datetime.strptime(release_date_str, format_date)



    # TODO: create a movie here and append it to movies_in_db
    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)