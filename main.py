from database.setup import Base, engine
from models.user import User
from models.podcast import Podcast
from cli.menu import main_menu

Base.metadata.create_all(engine)

main_menu()
