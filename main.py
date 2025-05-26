from database.setup import Base, engine
from models.user import User

Base.metadata.create_all(engine)