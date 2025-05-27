from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base, session

class Episode(Base):
    __tablename__ = 'episodes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    duration = Column(Integer)  
    listened = Column(Boolean, default=False)
    rating = Column(Integer, nullable=True)  
    note = Column(String, nullable=True)
    podcast_id = Column(Integer, ForeignKey('podcasts.id'), nullable=False)

    podcast = relationship("Podcast", back_populates="episodes")

    def __repr__(self):
        return (f"<Episode(id={self.id}, title='{self.title}', duration={self.duration} mins, "
                f"listened={self.listened}, rating={self.rating}, note='{self.note}')>")

    
    @classmethod
    def create_episode(cls, title, duration, podcast_id):
        episode = cls(title=title, duration=duration, podcast_id=podcast_id)
        session.add(episode)
        session.commit()
        return episode

    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    
    @classmethod
    def find_by_id(cls, episode_id):
        return session.query(cls).filter_by(id=episode_id).first()

    
    @classmethod
    def get_by_podcast(cls, podcast_id):
        return session.query(cls).filter_by(podcast_id=podcast_id).all()


    @classmethod
    def delete_by_id(cls, episode_id):
        episode = cls.find_by_id(episode_id)
        if episode:
            session.delete(episode)
            session.commit()
            return True
        return False

    
    def update(self, title=None, duration=None, listened=None, rating=None, note=None, podcast_id=None):
        if title is not None:
            self.title = title
        if duration is not None:
            self.duration = duration
        if listened is not None:
            self.listened = listened
        if rating is not None:
            self.rating = rating
        if note is not None:
            self.note = note
        if podcast_id is not None:
            self.podcast_id = podcast_id
        session.commit()

    
    def mark_listened(self):
        self.listened = True
        session.commit()