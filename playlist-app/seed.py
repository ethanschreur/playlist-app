from models import Playlist, Song, PlaylistSong, db
from app import app

db.drop_all()
db.create_all()
