from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base, session


class Podcast(Base):
    __tablename__ = 'podcasts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    genre = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)


    user = relationship("User", back_populates="podcasts")
    episodess = relationship("Episode", back_populates="podcast", cascade="all, delete")

    def __repr__(self):
        return f"<Podcast(id={self.id}, title={self.title}, genre='{self.genre}')"
    

    @classmethod
    def create_podcast(cls,title,genre,user_id):
        podcast = cls(title=title, genre=genre, user_id=user_id)
        session.add(podcast)
        session.commit()
        return podcast
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, podcast_id):
        return session.query(cls).filter_by(id=podcast_id).first()
    
    @classmethod
    def delete_by_id(cls, podcast_id):
        podcast = cls.find_by_id(podcast_id)
        if podcast:
            session.delete(podcast)
            session.commit()
            return True
        return False
    
    def save(self):
        session.add(self)
        session.commit()

    def update(self, title=None, genre=None, user_id=None):
        if title:
            self.title = title
        if genre:
            self.genre = genre
        if user_id:
            self.user_id = user_id
        session.commit()
                        
