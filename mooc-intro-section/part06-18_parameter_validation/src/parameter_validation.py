# Write your solution here
def new_person(name: str, age: int):

    if name == '':
        raise ValueError("name cannot be empty string")
    if len(name.split()) < 2:
        raise ValueError("name contains less than two words")
    if len(name) > 40:
        raise ValueError("name is longer than 40 character")
    if age < 0:
        raise ValueError("age cannot be a negative number")
    if age > 150:
        raise ValueError("age cannot be greater than 150")
    else:
        print(name, age)
        return name, age


if __name__ == "__main__":
    print(new_person("nicolas", 22))

# new_person("nicolas", 22)
