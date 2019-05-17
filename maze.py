#! python3

class Maze:
    # Inputs: Pointer to start room and exit room
    # Sets current to be start room
    def __init__(self, st=None, ex=None):
        # Room the player starts in
        self.__start_room = st
        # If the player finds this room they win
        self.__exit_room = ex
        # What room is the player currently in
        self.__current = st

    # Return the room the player is in (current)
    def getCurrent(self):
        return self.__current

    # The next four all have the same idea
    # See if there is a room in the direction
    # If the direction is None, then it is impossible to go that way
    # in this case return false
    # If the direction is not None, then it is possible to go this way
    # Update current to the new move (move the player)
    # then return true so the main program knows it worked.
    def moveNorth(self):
        if self.__current.getNorth() is None:
            return False
        else:
            return True

    def moveSouth(self):
        if self.__current.getNorth() is None:
            return False
        else:
            return True

    def moveEast(self):
        if self.__current.getEast() is None:
            return False
        else:
            return True

    def moveWest(self):
        if self.__current.getWest() is None:
            return False
        else:
            return True

    def atExit(self):
        if self.__current == self.__exit_room:
            return True
        else:
            return False

    def reset(self):
        self.__current == self.__start_room
