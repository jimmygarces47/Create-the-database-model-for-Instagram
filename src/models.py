import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'Usuario'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250))
    firts_name = Column(String(250))
    last_name = Column(String(250))
    email=Column(String(30))

    def to_dict(self):
        return {}

class Follower(Base):
    __tablename__ = 'Followers'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer,primary_key=True)
    user_from_id= Column(Integer,ForeignKey('Usuario.id'))
    user_to_id= Column(Integer,ForeignKey('Usuario.id'))
    User= relationship(User)

class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer,primary_key=True)
    user_id= Column(Integer,ForeignKey('Usuario.id')) 
    Foranea_user_id=relationship(User)    

class Media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer,primary_key=True)
    types= Column(Integer)
    url= Column(Integer)
    post_id= Column(Integer,ForeignKey('Post.id'))
    Foranea_id=relationship(Post)

class Comment (Base):
    __tablename__ = 'Comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id= Column(Integer,primary_key=True)
    Comment_text= Column(Integer)
    author_id=Column(Integer,ForeignKey('Usuario.id'))
    post_id= Column(Integer,ForeignKey('Post.id'))
    Foranea_post_id=relationship(Post)
    Foranea_author_id=relationship((User)) 






## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e