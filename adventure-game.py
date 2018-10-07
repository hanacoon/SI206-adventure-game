#test comment

class Player:

	def __init__(self, currentRoom):
		self.currentRoom = currentRoom
		self.lives = 3
		self.treasure = list()

	### getter and setter for currentRoom
	def getRoom(self):
		return self.currentRoom
	def setRooms(self, newRoom):
		self.currentRoom = newRoom

	### getter and setter for lives
	def getLives(self):
		return self.lives
	def setLives(self, newLives):
		self.lives = newLives

	### getter and setter for treasure
	def getTreasure(self):
		return self.treasure
	def setTreasure(self, item):
		self.treasure.append(item)

class Room:

	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.rooms = dict() #dictionary
		self.treasure = list() #list

	### getter and setter for name
	def getName(self):
		return self.name
	def setName(self, newName):
		self.name = newName

	### getter and setter for description
	def getDescription(self):
		return self.description
	def setDescription(self, newDescription):
		self.description = newDescription

	### getter and setter for rooms
	def getRooms(self):
		return self.rooms
	def setRooms(self, direction, room):
		self.rooms[direction] = room

	### getter and setter for treasure
	def getTreasure(self):
		return self.treasure
	def setTreasure(self, newTreasure):
		self.treasure.append(newTreasure)

class Treasure:

	def __init__(self, name, description, points):
		self.name = name
		self.description = description
		self.points = points

	### getter and setter for name
	def getName(self):
		return self.name
	def setName(self, newName):
		self.name = newName

	### getter and setter for description
	def getDescription(self):
		return self.description
	def setDescription(self, newDescription):
		self.description = newDescription

	### getter and setter for points
	def getPoints(self):
		return self.points
	def setPoints(self, newPoints):
		self.points = newPoints

class Game:

	def __init__(self):
		startRoom = Room("start", "first room")
		exitRoom = Room("exit", "exit room")
		middleRoom = Room("middle", "middle room")
		treasureStart = Treasure("treasure1", "treasure for start room", 1)
		treasureMiddle = Treasure("treasure2", "treasure for middle room", 2)
		treasureExit = Treasure("treasure3", "treasure for exit room", 3)

		startRoom.setTreasure(treasureStart)
		startRoom.setRooms('e', middleRoom)
		middleRoom.setTreasure(treasureMiddle)
		middleRoom.setRooms('w', startRoom)
		middleRoom.setRooms('e', exitRoom)
		exitRoom.setTreasure(treasureExit)
		exitRoom.setRooms('w', middleRoom)

		self.startRoom = startRoom
		self.exitRoom = exitRoom

		player = Player(startRoom)
		self.player = player

	### getter and setter for start room
	def getStartRoom(self):
		return self.startRoom
	def setStartRoom(self, start):
		self.startRoom = start

	### getter and setter for exit room
	def getExitRoom(self):
		return self.exitRoom
	def setExitRoom(self, exit):
		self.exitRoom = exit

	### getter and setter for player
	def getPlayer(self):
		return self.player
	def setPlayer(self, newPlayer):
		self.player = newPlayer

### Unit tests for Room
room1 = Room("room1", "test room number 1")
room2 = Room("room2", "test room number 2")
room3 = Room("room3", "test room number 3")
treasure = Treasure("gold", "golden cup", 1)
room1.setTreasure("treasure1")
room1.setTreasure("treasure2")
room1.setTreasure("treasure3")
room1.setRooms('n', room2)
room2.setRooms('s', room1)
room1.setRooms('s', room3)
room3.setRooms('n', room1)
assert room1.getRooms() == {'n':room2, 's':room3}
assert room1.getTreasure() == ["treasure1", "treasure2", "treasure3"]
assert room1.getName() == "room1"
assert room1.getDescription() == "test room number 1"

### Unit tests for Player
room = Room("room", "test room")
player = Player(room)
assert player.getLives() == 3
assert player.getTreasure() == []
player.setTreasure("treasure!")
assert player.getTreasure() == ["treasure!"]

### Unit tests for Treasure
treasure = Treasure("t1", "treasure 1", 1)
assert treasure.getName() == "t1"
assert treasure.getPoints() == 1
treasure.setPoints(2)
treasure.getPoints() == 2

### Game testing
game = Game()
assert game.getStartRoom().getName() == "start"
assert game.getExitRoom().getName() == "exit"
assert game.getStartRoom().getTreasure()[0].getPoints() == 1
assert game.getExitRoom().getTreasure()[0].getPoints() == 3
