from database.setup import Base, engine
from models.user import User
from models.podcast import Podcast

Base.metadata.create_all(engine)