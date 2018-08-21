from models.person import Person, Fellow, Staff
from models.room import Room, OfficeSpace, LivingSpace
from models.structures import Tree as BST
from models.structures import Queue, PriorityQueue

class Dojo(object):
    def __init__(self):
        self.rooms = []
        self.people = BST()
        self.unallocated_office_queue = Queue()
        self.living_space_queue = PriorityQueue()
        
    def create_room(self, room_name, purpose):
        """ method create room to add new rooms to dojo"""

        if [room for room in self.rooms
           if room_name.upper() == room.name.upper()]:
            print("{} already Exists in Dojo.".format(room_name.upper()))
            return "{} already Exists in Dojo.".format(room_name.upper())

        if str(purpose.upper()) == "OFFICE":
            room = OfficeSpace(name=str(room_name.upper()))
            self.rooms.append(room)
            print("{} {} created".format(room.name, room.purpose))
            self.allocate_office()
            return "Room Created"

        if purpose.upper() == "LIVINGSPACE":
            room = LivingSpace(name=str(room_name.upper()))
            self.rooms.append(room)
            print("{} {} created".format(room.name, room.purpose))
            self.allocate_living_space()
            return "Room Created"

        print("{} is not a valid room type.".format(purpose))
        return "{} is not a valid room type.".format(purpose)
      
    def add_person(
        self,
        first_name,
        second_name,
        role,
        wants_accomodation, 
        id_no,
        priority):
        """Check if the names provided are strings before proceeding"""

        person_name = str(first_name.upper()) + " " + str(second_name.upper())

        if self.people.find_by_id(int(id_no)):
            print("{} Exists in Dojo.".format(person_name))
            return "{} Exists in Dojo.".format(person_name)

        if role.upper() == "FELLOW" and wants_accomodation == "N":
            person = Fellow(
                name=person_name,
                person_id=int(id_no))
            self.people.insert(person)
            print("Fellow Added")
            self.unallocated_office_queue.enqueue(person.person_id)
            self.allocate_office()
            return "Fellow Added"

        if role.upper() == "FELLOW" and wants_accomodation == "Y":
            person = Fellow(
                name=person_name,
                person_id=int(id_no),
                wants_accomodation=True)
            self.people.insert(person)
            print("Fellow Added")
            self.unallocated_office_queue.enqueue(person.person_id)
            self.living_space_queue.enqueue(person.person_id, str(priority))
            self.allocate_office()
            self.allocate_living_space()
            return "Fellow Added"

        if role.upper() == "STAFF" and wants_accomodation == "N":
            person = Staff(
                name=person_name,
                person_id=int(id_no))
            self.people.insert(person)
            print("Staff Added ")
            self.unallocated_office_queue.enqueue(person.person_id)
            self.allocate_office()
            return "Staff Added"
        # If role is not defined
        else:
            print("either '{}' or '{}'is not a valid option."
              .format(role, wants_accomodation))

    def allocate_office(self):
        """ This method allocates an office to a person"""

        if self.rooms:
            rooms = [room for room in self.rooms if not room.is_full() 
                         if room.purpose == "OFFICE" ]
            if rooms:
                for office in rooms:
                    while not office.is_full(): 
                        if not self.unallocated_office_queue.peek():
                            print("office queue is empty")
                            break
                        person_id = self.unallocated_office_queue.dequeue()
                        office.add_occupant(person_id)
                        person = self.people.find_by_id(person_id)
                        person.occupy_room(office.room_id)
                        print("{} was allocated Office {} ".format(
                            person.name, office.name))

        else:
            print("No Office available for now ")
        
    def allocate_living_space(self):
        """ This method allocates an living space to a person"""

        if self.rooms:
            rooms = [room for room in self.rooms if not room.is_full() 
                             if room.purpose == "LIVINGSPACE" ]
            if rooms:
                for living_space in rooms:
                    while not living_space.is_full(): 
                        if not self.living_space_queue.peek():
                            print("living space queue is empty")
                            break  
                        person_id = self.living_space_queue.dequeue()
                        living_space.add_occupant(person_id)
                        person = self.people.find_by_id(person_id)
                        person.occupy_room(living_space.room_id)
                        print("{} was allocated living space {} ".format(
                            person.name, living_space.name))
        else:
            print("No living spaces available for now ")
            