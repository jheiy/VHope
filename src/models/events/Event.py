from src.models.elements import Character, Object


class Event():

    sequence_number = -1
    type = ""
    subject = None #Object/Character object

    def __init__(self, sequence_number, type, subject):
        self.sequence_number = sequence_number
        self.type = type
        self.subject = subject

    def  get_sequence_number(self):
        return self.sequence_number

    def get_type(self):
        return self.type

    def get_subject(self):
        return self.subject

    def get_characters_involved(self):
        characters = []

        if type(self.subject) == Character:
            characters.add(self.subject)

        return characters

    def get_objects_involved(self):
        objects = []

        if type(self.subject) == Object:
            objects.add(self.subject)

        return objects

