from database.setup import Base, engine
from models.user import User
from models.podcast import Podcast
from cli.menu import menu

Base.metadata.create_all(engine)

menu()

