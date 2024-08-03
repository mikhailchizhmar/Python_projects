from pydantic import BaseModel, model_validator
from enum import Enum


class Alignment(str, Enum):
    Ally = 'Ally'
    Enemy = 'Enemy'


class Class(str, Enum):
    Corvette = 'Corvette'
    Frigate = 'Frigate'
    Cruiser = 'Cruiser'
    Destroyer = 'Destroyer'
    Carrier = 'Carrier'
    Dreadnought = 'Dreadnought'


class Officer(BaseModel):
    first_name: str
    last_name: str
    rank: str


def assert_spaceship(ship: 'Spaceship') -> None:
    assert not (ship.name == 'Unknown' and ship.alignment == 'Ally')
    if ship.class_ == 'Corvette':
        assert 80 <= ship.length <= 250 and 4 <= ship.crew_size <= 10
    elif ship.class_ == 'Frigate':
        assert 300 <= ship.length <= 600 and 10 <= ship.crew_size <= 15 and ship.alignment == 'Ally'
    elif ship.class_ == 'Cruiser':
        assert 500 <= ship.length <= 1000 and 15 <= ship.crew_size <= 30
    elif ship.class_ == 'Destroyer':
        assert 800 <= ship.length <= 2000 and 50 <= ship.crew_size <= 80 and ship.alignment == 'Ally'
    elif ship.class_ == 'Carrier':
        assert 1000 <= ship.length <= 4000 and 120 <= ship.crew_size <= 250 and not ship.armed
    elif ship.class_ == 'Dreadnought':
        assert 5000 <= ship.length <= 20000 and 300 <= ship.crew_size <= 500


class Spaceship(BaseModel):
    alignment: Alignment
    name: str
    class_: Class
    length: int
    crew_size: int
    armed: bool
    officers: list[Officer]

    @model_validator(mode='after')
    def proper_spaceship(self) -> 'Spaceship':
        assert_spaceship(self)
        return self
