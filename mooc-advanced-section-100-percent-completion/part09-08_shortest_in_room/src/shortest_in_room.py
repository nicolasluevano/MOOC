# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name


class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)


    def is_empty(self):
        return not self.persons

    def combined_height(self):
        combined_height = 0
        for person in self.persons:
            combined_height += person.height
        return combined_height

    def shortest(self):
        if not self.persons:
            return None
        else:
            shortest_height = self.persons[0].height
            shortest_person = self.persons[0]
            for person in self.persons:
                if person.height < shortest_height:
                    shortest_height = person.height
                    shortest_person = person
            return shortest_person
            

    def remove_shortest(self):
        if not self.persons:
            return None
        shortest = self.shortest()
        for person in self.persons:
            if person == shortest:
                self.persons.remove(person)
                return person
                

    def print_contents(self):
        print(f'There are {len(self.persons)} persons in the room, and their combined height is {self.combined_height()} cm')
        for person in self.persons:
            print(f'{person.name} ({person.height} cm)')

if __name__ == "__main__":
    room = Room()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))

    print()

    print("Is the room empty?", room.is_empty())
    print("Shortest:", room.shortest())

    print()

    room.print_contents()
