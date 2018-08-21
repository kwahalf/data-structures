from abc import ABCMeta, abstractmethod


class Person(object):
    """class Room"""
    __metaclass__ = ABCMeta 
     
    def __init__(self, name=None, person_id=None, wants_accomodation=None):
        self.person_id = person_id
        self.name = name
        self.role = None
        self.wants_accomodation = wants_accomodation
        self.rooms = []
    
    def occupy_room(self, room):
        self.rooms.append(room)
    
    def vaccate_room(self, room):
        self.occupants.remove(room)
   
    def __repr__(self):
        return '%s(name=%s, want_accomodation=%s)' % (
            self.__class__.__name__, 
            self.name,
            self.want_accomodation
        )
    def __str__(self):
        return Self.name
      
class Staff(Person):
  """class Staff """
  def __init__(self, name=None, person_id=None, want_accomodation=None):
        Person.__init__(
            self,
            name=name,
            person_id=person_id,
            want_accomodation=want_accomodation)
        self.role = "STAFF"
        self.has_office = False
        
class Fellow(Person):
  """class Fellow """
  def __init__(self, name=None, person_id=None, wants_accomodation=None):
        Person.__init__(
            self,
            name=name,
            person_id=person_id,
            wants_accomodation=wants_accomodation)
        self.role = "FELLOW"
        self.has_office = False
        self.has_accomodation = False
 