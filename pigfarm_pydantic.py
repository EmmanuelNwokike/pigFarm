from dataclasses import dataclass, field
from typing import List, Optional
from datetime import date

### farmer class

@dataclass

class Farmer:
    id:str
    name:str
    contact:str
    barns: List ['Barn'] = field(default_factory=list)

    def manageFarm(self):
        print(f"Managing farm for Farmer: {self.name}")
        for barn in self.barns:
            print(f"  - Barn ID: {barn.id}, Location: {barn.location}")


### barn class
    
@dataclass
class Barn:
    id: str
    location: str
    capacity: int
    pigs: List['Pig'] = field(default_factory=list)   # A barn houses many pigs
    farmer: Optional[Farmer] = None                   # Each barn is managed by one farmer

    def addPig(self, pig: 'Pig'):
        if len(self.pigs) < self.capacity:
            self.pigs.append(pig)
            print(f"Pig {pig.id} added to Barn {self.id}")
        else:
            print(f"Barn {self.id} is at full capacity.")


### pig class

@dataclass
class Pig:
    id: str
    breed: str
    dob: date
    status: str
    weight: float
    barn: Optional[Barn] = None
    feeds: List['Feed'] = field(default_factory=list)  # A pig consumes many feeds

    def recordHealth(self):
        print(f"Recording health for Pig {self.id}: Status - {self.status}, Weight - {self.weight}kg")


### Feed class

@dataclass
class Feed:
    id: str
    type: str
    quantity: float
    pigs: List[Pig] = field(default_factory=list)  # Many-to-many between pigs and feeds

    def feedPig(self, pig: Pig):
        self.pigs.append(pig)
        pig.feeds.append(self)
        print(f"Fed Pig {pig.id} with {self.quantity}kg of {self.type}")
