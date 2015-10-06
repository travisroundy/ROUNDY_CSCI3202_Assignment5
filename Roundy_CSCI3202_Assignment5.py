#Travis Roundy
#CSCI 3202- Intro to AI
#Assignment 5

import sys

class Node():
	#THIS CLASS WILL STORE INFORMATION ABOUT EACH LOCATION IN THE GRAPH.
	def __init__(self):
		self.location = (int,int)
		self.utility = float
		self.reward = int
		self.value = int
		self.end = False
		self.reachable = True
		
def MDP(maze, epsilon):
	print("Updating Utilities....")
	utilities = []
	#THIS SETS UP THE MAZE WITH EACH LOCATION AS NODE IN ORDER TO STORE
	#INFORMATION ABOUT THE LOCATION DEFINED IN THE NODE CLASS.
	for i in range(0,8):
		for j in range(0,10):
			utility = 0
			if maze[i][j] == 1:
				temp = maze[i][j]
				maze[i][j] = Node()
				maze[i][j].utility = 0.0
				maze[i][j].reward = -1.0
				maze[i][j].value = temp
				maze[i][j].location = (i,j)
			elif maze[i][j] == 2:
				temp = maze[i][j]
				maze[i][j] = Node()
				maze[i][j].reachable = False
				maze[i][j].utility = 0.0
				maze[i][j].reward = 0.0
				maze[i][j].value = temp
				maze[i][j].location = (i,j)
			elif maze[i][j] == 3:
				temp = maze[i][j]
				maze[i][j] = Node()
				maze[i][j].utility = 0.0
				maze[i][j].reward = -2.0
				maze[i][j].value = temp
				maze[i][j].location = (i,j)
			elif maze[i][j] == 4:
				temp = maze[i][j]
				maze[i][j] = Node()
				maze[i][j].utility = 0.0
				maze[i][j].reward = 1.0
				maze[i][j].value = temp
				maze[i][j].location = (i,j)
			elif maze[i][j] == 50:
				temp = maze[i][j]
				maze[i][j] = Node()
				maze[i][j].utility = 50.0
				maze[i][j].reward = 50.0
				maze[i][j].value = temp
				maze[i][j].location = (i,j)
			else:
				temp = maze[i][j]
				maze[i][j] = Node()
				maze[i][j].utility = 0.0
				maze[i][j].reward = 0.0
				maze[i][j].value = temp
				maze[i][j].location = (i,j)
				
				
	#BEGIN VALUE ITERATION:
	#THE WHILE LOOP OCCURS UNTIL DELTA IS LESS THAN THE VALUE GIVEN
	#EACH TIME UPDATING UTILITIES
	gamma = 0.9
	v = 0
	delta = sys.maxint
	while (delta > epsilon*(1-gamma)/gamma):
		for x in range(0,8):
			for y in range(9,-1,-1):
				(u,v) = Transition(x,y,maze)
				if (x == 0 & y == 0):
					delta = u
				if u > delta:
					delta = u
				maze[x][y].utility = v	
				
	#BY THIS POINT, THE UTILITIES OF THE ALL STATES HAVE BEEN UPDATED
	#I PUT THEM INTO A UTILITIES LIST FOR STORAGE
	for x in range(0,8):
		utilities.append([])
		for y in range(0,10):
			utilities[x].append(maze[x][y].utility)
	#print utilities
			
	print("Utilities Updated!")
	#BEGINS TO FIND THE PATH THROUGH THE MAZE USING THE UTILITIES
	findPath(maze,7,0,0,9)
	
def findPath(maze,startx,starty,goalx,goaly):
	#THIS IS THE FUNCTION WHERE I FIND A PATH WITH BEST UTILITIES
	#UNTIL THE NODE IS AT THE END
	print("Determining Path...")
	path = []
	openNodes = []
	pathUtility = []
	count = 0
	startNode = maze[startx][starty]
	endNode = maze[goalx][goaly]
	endNode.end = True
	currentNode = startNode
	path.append(startNode.location)
	pathUtility.append(startNode.utility)
	
	while (currentNode.location != (0,9)):
		possibilities = []
		(cx,cy) = currentNode.location
		count = 0
		while count < 5:
			checkVal = 0
			if count == 0:
				if ((cx-1 <= 7) and (cx-1 >= 0)):
					if (maze[cx-1][cy].reachable == True) and ((maze[cx-1][cy].location) not in path) :
						checkUp = maze[cx-1][cy].utility
						if (maze[cx-1][cy].location not in path):
							possibleValue1 = (checkUp,maze[cx-1][cy])
							possibilities.append(possibleValue1)
							#print("checking u.. ", maze[cx-1][cy].location)
				else:
					possibleValue1 = (-sys.maxint,Node())
					possibilities.append(possibleValue1)
			if count == 1:
				if ((cy+1 <= 9) and (cy+1 >= 0)):
					if (maze[cx][cy+1].reachable == True) and ((maze[cx][cy+1].location) not in path):
						checkRight = maze[cx][cy+1].utility
						if (maze[cx][cy+1].location not in path):
							possibleValue2 = (checkRight,maze[cx][cy+1])
							possibilities.append(possibleValue2)
							#print("checking r.. ", maze[cx][cy+1].location)
				else:
					possibleValue2 = (-sys.maxint, Node())
					possibilities.append(possibleValue2)
			if count == 2:
				if ((cy-1 <= 9) and (cy-1 >= 0)):
					if (maze[cx][cy-1].reachable == True) and ((maze[cx][cy-1].location) not in path):
						checkLeft = maze[cx][cy-1].utility
						if (maze[cx-1][cy].location not in path):
							possibleValue3 = (checkLeft,maze[cx][cy-1])
							possibilities.append(possibleValue3)
							#print("checking l.. ", maze[cx][cy-1].location)
				else:
					possibleValue3 = (-sys.maxint,Node())
					possibilities.append(possibleValue3)
			if count == 3:
				if ((cx+1 <= 7) and (cx+1 >= 0)):
					if (maze[cx+1][cy].reachable == True) and ((maze[cx+1][cy].location) not in path):
						checkDown = maze[cx+1][cy].utility
						if (maze[cx+1][cy].location not in path):
							possibleValue4 = (checkDown,maze[cx+1][cy])
							possibilities.append(possibleValue4)
							#print("checking d.. ", maze[cx+1][cy].location)
				else: 
					possibleValue4 = (-sys.maxint,Node())
					possibilities.append(possibleValue4)

			if count == 4:
				valueNow = max(possibilities)
				currentNode = valueNow[1]
				path.append(currentNode.location)
				pathUtility.append(currentNode.utility)
				
			count = count + 1

	print("Solution Found!")
	print("((Location), Utility)")
	for p in range (0,len(path)):
		print(path[p],pathUtility[p])

	print("---------------------------------------------------------")
	print ""
		
				
def Transition(row,column,maze):
	#THIS FUNCTION IS USED TO DETERMINE THE VALUES OF THE UTILITIES
	#IT CHECKS THE ^ > v < DIRECTIONS WITH THE PROPER PROBABILITIES
	# AND RETURNS BOTH THE UTILITY VALUE AND THE DIFFERENCE
	actions = (">","^","v","<")
	utils = list()
	for a in actions:
		if a == ">":
			if (row != 0) & (row != 7) & (column != 9):
				utils.append((0.8 * maze[row][column+1].utility) + (0.1 * maze[row-1][column].utility) + (0.1 * maze[row+1][column].utility))
			else:
				utils.append(0)
		if a == "^":
			if (row != 0) & (column != 9) & (column != 0):
				utils.append((0.8 * maze[row-1][column].utility) + (0.1 * maze[row][column+1].utility) + (0.1 * maze[row][column-1].utility))
			else:
				value = 0
		if a == "v":
			if (row+1 != 8) & (column != 9) & (column != 0):
				utils.append((0.8 * maze[row+1][column].utility) + (0.1 * maze[row][column+1].utility) + (0.1 * maze[row][column-1].utility))
			else:
				utils.append(0)
		if a == "<":
			if (row-1 != 0 | row+1 != 8) & (column != 9) & (column != 0):
				utils.append((0.8 * maze[row][column-1].utility) + (0.1 * maze[row-1][column].utility) + (0.1 * maze[row+1][column].utility))
			else:
				utils.append(0)
	Ustate = maze[row][column].utility
	maxUtil = max(utils)
	maze[row][column].utility = (float(R(row,column,maze) + 0.9 * maxUtil))
	UNEXTstate = maze[row][column].utility
	return (float(abs(Ustate - UNEXTstate)),float(maze[row][column].utility))
	
def R(x, y, maze):
	#RETURNS REWARD OF STATE
	return maze[x][y].reward

def main():
	file_name = sys.argv[1]
	epsilon = float(sys.argv[2])
	with open(file_name) as f:
		maze = [[int(x) for x in line.split()] for line in f]
	MDP(maze,epsilon)
	
	

if __name__ == "__main__":					
	main()
