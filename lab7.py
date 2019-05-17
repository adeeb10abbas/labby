#! python3
from room import Room
from maze import Maze


my_rooms = []
my_rooms.append(Room("This room is the entrance."))
my_rooms.append(Room("This room has a table. Maybe a dinning room?"))
my_rooms.append(Room("This room has a study table."))
my_rooms.append(Room("This room has a knife. Maybe it is a kitchen?"))
my_rooms.append(Room("This room has a washing machine in it"))
my_rooms.append(Room("This room looks like its a boys' room"))
my_rooms.append(Room("This room looks like its a girls' room"))
my_rooms.append(Room("This is a indoor swimming pool"))
my_rooms.append(Room("This is a toilet"))
my_rooms.append(Room("This is a wardrobe of ties"))
my_rooms.append(Room("This is a library"))
my_rooms.append(Room("This is the exit. Hooray! Lucky you"))

my_rooms[0].setNorth(my_rooms[1])
my_rooms[1].setEast(my_rooms[2])
my_rooms[1].setSouth(my_rooms[0])
my_rooms[2].setNorth(my_rooms[3])
my_rooms[2].setWest(my_rooms[1])
my_rooms[3].setWest(my_rooms[4])
my_rooms[3].setSouth(my_rooms[2])
my_rooms[4].setNorth(my_rooms[5])
my_rooms[4].setEast(my_rooms[3])
my_rooms[5].setWest(my_rooms[6])
my_rooms[5].setSouth(my_rooms[4])
my_rooms[6].setNorth(my_rooms[7])
my_rooms[6].setEast(my_rooms[5])
my_rooms[7].setEast(my_rooms[8])
my_rooms[7].setSouth(my_rooms[6])
my_rooms[8].setEast(my_rooms[9])
my_rooms[8].setWest(my_rooms[7])
my_rooms[9].setSouth(my_rooms[10])
my_rooms[9].setWest(my_rooms[8])
my_rooms[10].setEast(my_rooms[11])
my_rooms[10].setNorth(my_rooms[9])
my_rooms[11].setWest(my_rooms[10])

# Making the maze
# Setting the start and exit room
my_maze = Maze(my_rooms[0], my_rooms[11])



def main():
    while True:
        #print(my_maze.getCurrent())
        inp = input("Where would you like to go? north south east west reset\n")
        if inp.lower() == 'north':
            if my_maze.moveNorth() is True:
                my_maze.moveNorth()
                print(my_maze.getCurrent())
            else:
                print("Invalid Move")

        elif inp.lower() == 'south':
            if my_maze.moveSouth() is True:
                my_maze.moveSouth()
                print(my_maze.getCurrent())
            else:
                print("Invalid Move")

        elif inp.lower() == 'east':

            if my_maze.moveEast() is True:
                my_maze.moveEast()
                print(my_maze.getCurrent())
            else:
                print("Invalid Move")
        elif inp.lower() == 'west':

            if my_maze.moveWest() is True:
                my_maze.moveWest()
                print(my_maze.getCurrent())
            else:
                print("Invalid Move")




main()