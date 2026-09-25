
class Event():
    def __init__(self, name, max_attendees: int):
        """
        Adding a name identifier for the event, a max attendee count, then two lists to view attendees, one by ID one by name
        """
        self.name = name
        self._max_attendees = max_attendees
        self.attendees = []
        self.attendees_id = []

    def information(self):
        """
        Prints key information about the event
        """
        print(f'{self.name} has {len(self.attendees)} attendees out of {self._max_attendees}')


    def add_attendee(self, attendees: list):
        """
        Adding a list of attendees and giving the option to add the maximum amount of attendees from the list
        """
        decision = "Y"

        if len(self.attendees) == self._max_attendees:
            return print("Cannot add any more attendees")

        if len(self.attendees) + len(attendees) > self._max_attendees:
            decision = input("Cannot add all attendees. \nWould you like to add as many as possible (Y/N): ")

        if decision == "Y":
            spaces = int(self._max_attendees - len(self.attendees))
            for attendee in attendees[0:spaces]:
                self.attendees.append(attendee.name)
                self.attendees_id.append(attendee.id)

        elif decision == "N":
            return False
        return None

    def remove_attendee(self, attendee):
        """
        Option to remove an attendee from any event
        """
        self.attendees_id.remove(attendee.id)
        self.attendees.remove(attendee.name)
