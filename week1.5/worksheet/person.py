# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """
    def __init__(self,name, birth):
        """creates a person with a date of birth and a name"""
        self.name = name
        self.birth = birth
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if len(name) == 0:
            raise ValueError("No name found")
        if not isinstance(birth, date):
            raise TypeError("Date of birth must be an actual date object")
    def initials(self):
        """returns the initials of the person"""
        return "".join(word[0].upper() for word in self.name.split())
    def is_birthday(self):
        """returns true if today is the person's birthday, otherwise returns false"""
        today = date.today()
        if today.month ==self.birth.month and today.day == self.birth.day:
            return True
        else:
            return False
    