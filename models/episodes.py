from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database.setup import Base, session

class Episode(Base):
    __tablename__ = 'episodes'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    duration = Column(Integer)
    listened = Column(Boolean, default=False)
    podcast_id = Column(Integer, ForeignKey('podcasts.id'), nullable=False)

    podcast = relationship("Podcast", back_populates="episodes")

    def __repr__(self):
        return f"<Episode(id={self.id}, title='{self.title}', duration={self.duration} mins, listened={self.listened})>"

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
    def delete_by_id(cls, episode_id):
        episode = cls.find_by_id(episode_id)
        if episode:
            session.delete(episode)
            session.commit()
            return True
        return False

    def mark_listened(self):
        self.listened = True
        session.commit()