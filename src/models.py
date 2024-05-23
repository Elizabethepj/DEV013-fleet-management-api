"""configure models"""
from flask_sqlalchemy import SQLAlchemy

# Create an instance SQLAlchemy
db = SQLAlchemy()

# defines the Taxi model|


class Taxi(db.Model):
    """Taxi model"""
    __tablename__ = 'taxis'
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(20), nullable=False)

# Defines Trajectories model


class Trajectories(db.Model):
    """Trajectories model"""
    __tablename__ = 'trajectories'
    id = db.Column(db.Integer, primary_key=True)
    taxi_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.TIMESTAMP, nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
