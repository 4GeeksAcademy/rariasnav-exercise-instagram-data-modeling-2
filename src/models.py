import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}
    
class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    description_profile = Column(String(250), nullable=False)

    def to_dict(self):
        return{}

class Likes(Base):
    __tablename__='likes'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    comment_like = Column(Integer)
    story_like = Column(Integer)
    post_like = Column(Integer)
    message_like = Column(Integer)
    asnwer_like = Column(Integer)

    def to_dict(self):
        return{}    
    
class Comment(Base):
    __tablename__='comment'   
    id = Column(Integer, primary_key=True) 
    user_id = Column(Integer, ForeignKey('user.id'))
    post_comment = Column(String(250))
    story_comment = Column(String(250))
    comment_comment = Column(String(250))
    like_comment = Column(Integer, ForeignKey('likes.comment_like'))
    likes = relationship(Likes)

    def to_dict(self):
        return{}
    
class Answer(Base):
    __tablename__='answer'   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    story_answer = Column(String(250))
    like_answer = Column(Integer, ForeignKey('answer.asnwer_like'))
    likes = relationship(Likes)

    def to_dict(self):
        return{}
    
class Post(Base):
    __tablename__='post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    likes_post = Column(Integer, ForeignKey('likes.post_like'))
    likes = relationship(Likes)
    comment_post = Column(String(250, ForeignKey('comment.post_comment')))
    comment = relationship(Comment)

    def to_dict(self):
        return{}

class Story(Base):
    __tablename__='story'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    like_story = Column(Integer, ForeignKey('likes.story_like'))
    likes = relationship(Likes)
    comment_story = Column(String(250), ForeignKey('comment.story_comment'))
    comment = relationship(Comment)
    answer_story = Column(String(250), ForeignKey('answer.story_answer'))
    answer = relationship(Answer)

    def to_dict(self):
        return{}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
