
# Write your solution here:
class Person:
    def __init__(self, name: str):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def name(self):
        return self.__name

    def numbers(self):
        return self.__numbers

    def address(self):
        return self.__address

    def add_number(self, number: str):
        self.__numbers.append(number)

    def add_address(self, address: str):
        self.__address = address


class PhoneBook(Person):
    def __init__(self):
        self.__persons = {}

    def add_number(self, name: str, number: int):
        if name not in self.__persons:
            person = Person(name)
            self.__persons[name] = person
            person.add_number(number)
        else:
            self.__persons[name].add_number(number)

    def add_address(self, name: str, address: str):
        if name not in self.__persons:
            person = Person(name)
            self.__persons[name] = person
            person.add_address(address)
        else:
            self.__persons[name].add_address(address)

    def get_entry(self, name: str):
        if name not in self.__persons:
            return None
        return self.__persons[name]

    def all_entries(self):
        return self.__persons


class PhoneBookApplication():
    def __init__(self):
        self.__phonebook = PhoneBook()

    def help(self):
        print("commands: ")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_number(self):
        name = input("name: ")
        number = input("number: ")
        self.__phonebook.add_number(name, number)

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)
        if person is None:
            print("address unknown")
            print("number unknown")
            return
        if person.numbers():
            for number in person.numbers():
                print(number)
        else:
            print("number unknown")
        if person.address() is not None:
            print(person.address())
        else:
            print("address unknown")

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_number()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()
            else:
                self.help()


# # when testing, no code should be outside application except the following:
application = PhoneBookApplication()
application.execute()
