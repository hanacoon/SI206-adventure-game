class Player:

   def __init__(self,theRoom):
      self.currRoom = theRoom  # the current room
      self.lives = 3     # three lives
      self.treasure = [] # empty list

   def getPoints(self):
     # return the total points from my list of treasure

   def setRoom(self,theRoom):
      self.currRoom = theRoom

   def getRoom(self):
      return self.currRoom

   def getTreasure(self):
       return self.treasure

   def setTreasure(self, treasure):
       self.treasure = treasure

   def getLives(self):
       return self.lives

   def setLives(self, num):
       self.lives = num

   def addTreasure(self, tList):
      # remove the treasure from tList and add to self.treasure


class Room:

   def __init__(self, name, desc):
         self.name = name
         self.desc = desc    # description of the room
         self.rooms = dict() # new dictionary
         self.treasure = []  # empty list

   def __str__(self):
         return self.name + ": " + self.desc

   def getName(self):
       return self.name

   def setName(self,name):
       self.name = name

   def getDesc(self):
         return self.desc

   def setDesc(self, desc):
       self.desc = desc

   def setNext(self,dir,room):
         self.rooms[dir] = room

   def getNext(self, dir):
         return self.rooms[dir]

   def getRooms(self):
       return self.rooms

   def setRooms(self, roomDir):
       self.rooms = roomDir

   def getTreasure(self):
       return self.treasure

   def addTreasure(self, theTreasure):
       self.treasure.append(theTreasure)

   def setTreasure(self, treasure):
       self.treasure = treasure

   def isRoomInDir(self, dir):
       return dir in self.rooms


class Treasure:
    def __init__(self, name, desc, points):
        self.name = name
        self.desc = desc
        self.points = points

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getDesc(self):
        return self.desc

    def setDesc(self,desc):
        self.desc = desc

    def getPoints(self):
        return self.points

    def setPoints(self, points):
        self.points = points

class Game:

   def __init__(self):

      # create the rooms
      r1 = Room("Room 1", "The interior is blue")
      r2 = Room("Room 2", "It is dark and spooky")
      r3 = Room("Room 3", "It is hot in here")
      r4 = Room("Room 4", "The interior is yellow")
      r5 = Room("Room 5", "It is cold in here")
      r6 = Room("Room 6", "The room is all red")
      r7 = Room("Room 7", "The room is full of light")

      # create the dictionary of direciton and next room
      # r1 - r2 - r3
      # r4 - r5 - r6
      #           r7
      r1.setRooms({'e':r2, 's':r4})
      r2.setRooms({'e':r3, 'w':r1, 's': r5})
      r3.setRooms({'s':r6, 'w': r2})
      r4.setRooms({'n':r1, 'e':r5})
      r5.setRooms({'w':r4, 'e':r6, 'n': r2})
      r6.setRooms({'n':r3, 'w':r5, 'e':r7})
      r7.setRooms({'w': r6})

      # set my start and end rooms
      self.start = r1
      self.end = r7

      # create the treasure and add it to the rooms
      t1 = Treasure("Lamp", "A shiny gold lamp", 20)
      t2 = Treasure("Watch", "An old pocket watch", 30)
      t3 = Treasure("Stone", "A flowing stone", 20)
      t4 = Treasure("Necklace", "A gold necklace with sparkling stones", 50)
      t5 = Treasure("Book", "A hardcover book with gold letters", 20)
      r1.addTreasure(t1)
      r2.addTreasure(t2)
      r3.addTreasure(t3)
      r4.addTreasure(t4)
      r5.addTreasure(t5)

   def getStart(self):
       return self.start

   def setStart(self, start):
       self.start = start

   def getExit(self):
       return self.exit

   def setExit(self, exit):
       return self.exit

   def play(self):
       # create a player and set their start room
       # play while not done (not dead and not won)
       # print the current room name and description
       # print the treasure description for the treasure in the room
       # move the treasure from the room to the plaer
       # ask what direction to move
       # if that direction is not valid lose one life and if no more lives then you lose
       # if that direction is valid move to that room and if the exit room then check if enough points and if so you win otherwise keep playing


# create the game and play it
theGame = Game()
theGame.play()
