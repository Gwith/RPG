class State:
    def __init__(self, starting_loc):
        self.alive = True
        self.location = starting_loc
        self.locations = {}

    def addloc(self, location):
        self.locations[location.name] = location

    def gotoloc(self, locname):
        self.location = self.locations[locname]


class Option:
    def __init__(self, text, action):
        self.text = text
        self.action = action


start_loc = Location("Courtyard",
                     "You're standing at the entrance to a castle",
                     [Option("Go Inside", GoToLocation("entrance")),
                      Option("Leave", KillPlayer("Scardy Cat"))])

hall = Location("Great Hall",
                    """You are standing in the entrance of the great hall.
The library is to the left, the Bed Chambers is to the right, .
                    [Option("Left", KillPlayer("The building collapses")),
                     Option("Right", KillPlayer("The building collapses")),
                     Option("straight", KillPlayer("The building collapses")),
                     Option("Upstairs", KillPlayer("The building collapses")),
                     Option("Outside", GoToLocation("start"))])
