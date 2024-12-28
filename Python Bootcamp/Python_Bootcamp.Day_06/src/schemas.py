from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

spaceship_officers = Table(
    'spaceship_officers', Base.metadata,
    Column('spaceship_id', ForeignKey('spaceships.id'), primary_key=True),
    Column('officer_id', ForeignKey('officers.id'), primary_key=True)
)


class Spaceship(Base):
    __tablename__ = 'spaceships'

    id = Column(Integer, primary_key=True, index=True)
    alignment = Column(String, index=True)
    name = Column(String, index=True)
    class_ = Column(String, index=True)
    length = Column(Integer)
    crew_size = Column(Integer)
    armed = Column(Boolean)

    officers = relationship("Officer", secondary=spaceship_officers, back_populates="spaceships")


class Officer(Base):
    __tablename__ = 'officers'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    rank = Column(String)

    spaceships = relationship("Spaceship", secondary=spaceship_officers, back_populates="officers")
