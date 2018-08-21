from abc import ABCMeta, abstractmethod


class Room(object):
    """class Room"""
    __metaclass__ = ABCMeta 

    room_count = 0
     
    def __init__(self, name=None, max_capacity=None):
        self.room_id = self.room_count
        self.room_count += 1
        self.name = name
        self.max_capacity = max_capacity
        self.occupants = []
        
    def add_occupant(self, occupant):
        if self.is_full():
            return false
        self.occupants.append(occupant)
        return True
    
    def remove_occupant(self, occupant):
        if self.is_an_occupant(occupant):
            self.occupants.remove(occupant)
            return True
        return false
    
    def is_an_occupant(self, occupant):
        return occupant in self.occupants
    
    def is_full(self):
        return len(self.occupants) >= self.max_capacity
    
    def __repr__(self):
        return '%s(name=%s, purpose=%s, max_capacity=%s)' % (
            self.__class__.__name__, 
            self.name,
            self.purpose,
            self.max_capacity
        )
    def __str__(self):
        return Self.name
      
class OfficeSpace(Room):
    """class OfficeSpace """
    def __init__(self, name=None, max_capacity=6):
        Room.__init__(self, name=name, max_capacity=max_capacity)
        self.purpose = "OFFICE"
        
class LivingSpace(Room):
    """class LivingSpace """
    def __init__(self, name=None, max_capacity=4):
        Room.__init__(self, name=name, max_capacity=max_capacity)
        self.purpose = "LIVINGSPACE"
        