from sqlalchemy import Column, String, Integer
from database.setup import Base, session
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'
    podcasts = relationship("Podcast", back_populates="user", cascade="all, delete")

    id = Column(Integer, primary_key=True) 
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)


    def __repr__(self):
        return f"<User(id = {self.id}, name = '{self.name}', email = '{self.email}')>"
    
    @classmethod
    def create_user(cls, name, email):
        user = cls(name = name, email = email)
        session.add(user)
        session.commit()
        return user
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls,user_id):
        user = session.query(cls).filter_by(id=user_id).first()
        return user
    
    @classmethod
    def find_by_name(cls,name):
        user = session.query(cls).filter_by(name=name).first()
        return user
    
    @classmethod
    def get_password(cls,password):
        password = session.query(cls).filter_by(password = password)
        return password
    
    @classmethod
    def get_email(cls,email):
        email = session.query(cls).filter_by(email=email)
        return email
        
    
    @classmethod
    def delete_by_id(cls,user_id):
        user = cls.find_by_id(user_id)
        if user:
            session.delete(user)
            session.commit()
            return True
        return False
    
   

    
    def email_provider(self):
        return self.email.split('@')[-1] if '@' in self.email else None
    
    def update_user(self, name=None, email = None):
        if name is not None:
            self.name = name
        if email is not None:
            self.email = email
        session.commit()      
        print(f"✅ User {self.id} updated successfully.")                
  


    


