class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for ch in people:
        Person(ch["name"], ch["age"])
    for ch in people:
        if ch.get("wife") is not None:
            Person.people[ch["name"]].wife = Person.people[ch["wife"]]
        if ch.get("husband") is not None:
            Person.people[ch["name"]].husband = Person.people[ch["husband"]]
    return list(Person.people.values())
