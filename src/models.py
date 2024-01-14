import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Fav_List(Base):
    __tablename__ = 'fav_list'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user'), nullable=False)
    fimls_id = Column(Integer, ForeignKey('films'), nullable=False)
    vehicles_id = Column(Integer, ForeignKey('vehicles'), nullable=False)
    characters_id = Column(Integer, ForeignKey('characters'), nullable=False)
    Planets_id = Column(Integer, ForeignKey('planets'), nullable=False)
    
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(25), unique=True, nullable=False)
    password = Column(String(50), unique=False, nullable=False)
    favorite_films = relationship('fav_list', backref='user')

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    director = Column(String(250))
    producer = Column(String(250), nullable=False)
    release_date = Column(String(50))
    person_id = Column(Integer, ForeignKey('person.id'))
    favorite = relationship('fav_list', backref='films')

class Vehicles(Base):
    __tablename__ = 'vehicles'
    id  = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    model = Column(String(50), unique=False, nullable=False)
    manufacturer = Column(String(50), unique=False, nullable=False)
    cost_in_credits = Column(Integer, unique=False, nullable=False)
    length = Column(Integer, unique=False, nullable=False)
    max_atmosphering_speed = Column(Integer, unique=False, nullable=False)
    crew = Column(Integer, unique=False, nullable=False)
    passengers =  Column(Integer, unique=False, nullable=False)
    cargo_capacity = Column(Integer, unique=False, nullable=False)
    consumables = Column(String(50), unique=False, nullable=False)
    vehicle_class = Column(String(50), unique=False, nullable=False)
    favorite = relationship('fav_list', backref='vehicles')

class Characters(Base):
    __tablename__ = 'characters'
    id  = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    date_of_birth = Column(DateTime(), unique=False, nullable=False)
    eye_color = Column(String(50), unique=False, nullable=False)
    hair_color = Column(String(50), unique=False, nullable=False)
    height = Column(Integer, unique=False, nullable=False)
    mass = Column(Integer, unique=False, nullable=False)
    gender = Column(String(50), unique=False, nullable=False)
    skin_color = Column(String(50), unique=False, nullable=False)
    favorite = relationship('fav_list', backref='characters')

class Planets(Base):
    __tablename__ = 'planets'
    id  = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    rotation_period = Column(Integer, unique=False, nullable=False)
    orbital_period  = Column(Integer, unique=False, nullable=False)
    diameter = Column(Integer, unique=False, nullable=False)
    climate = Column(String(50), unique=False, nullable=False)
    gravity = Column(String(50), unique=False, nullable=False)
    terrain = Column(String(50), unique=False, nullable=False)
    surface_water = Column(Integer, unique=False, nullable=False)
    population = Column(Integer, unique=False, nullable=False)
    favorite = relationship('fav_list', backref='planets')

    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')