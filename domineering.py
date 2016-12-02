
# Min-max Algorithm for Simulating 4 x 4 Domineering Game
# CS539 Game theory, algorithms and applications @Illinois tech
# Author: L. Zhuo
# Date: 10/28/2016

# ==================================  BUILD THE STRATEGY TREE ============================#
"""
1) Generate tree of all possible moves
2) Each position or node of the tree holds a Heuristic Value
3) Algorithm then starts from bottom of tree. deciding best move for that player and removing all bad moves

members class Node:
depth:				begins from 0
player:				{1,-1} represent Left(vertical) and Right(horizontal)
children[]:			a list containing the child nodes
createChildren():	the function to create children
board[][]:			the status of board at this Node
availables[]:		the list of available locations to place a domino
"""


from sys import maxsize

BSIZE = 4
COUNT_LEAVES = 0
COUNT_ALLNODES = 0

threshold = 2

# =================================== Tree Builder =======================================
# player: 	decide which player to expand the current node
# depth: 	mark the depth of the node
# in_edge:		the edge passing to the node, indicating placing to some location leads to the node

class Node(object): 

	def __init__(self, depth, player, board, edge):
		global COUNT_ALLNODES
		self.depth = depth
		self.player = player
		self.value = 0
		self.edge = edge
		self.children = []
		self.board = copyBoard(board)
		self.availableLocs = availableLocations(board, player, tag='all')
		#self.updateRemaining()
		self.createChildren()
		COUNT_ALLNODES += 1
		#print board

	# create children, until the tree reaches its leaves, i.e. the remaining is 0-length
	def createChildren(self):

		#(overwhelm, winner) = isOverwhelmed(board, threshold)
		#if overwhelm:
		#	self.value = maxsize * winner
		#	return

		if len(self.availableLocs) <= 0:
			global COUNT_LEAVES
			self.value = -maxsize * self.player
			COUNT_LEAVES += 1
			return

		for r in self.availableLocs:
			i = r[0]
			j = r[1]
			placeOnBoard(self.board, i, j, self.player)
			#subtractRemaining(remaining_v, remaining_h, r, self.player)
			child = Node(self.depth + 1, switch(self.player), self.board, r)
			removeFromBoard(self.board, i, j, self.player)
			#addRemaining(remaining_v, remaining_h, r, self.player, self.board)

			self.children.append(child)

	# the remaining places to add the dominoes, indicated by the first grid coordinate
	"""
	def updateRemaining(self):
		if self.player == 1:
			for i in range(BSIZE-1):
				for j in range(BSIZE):
					if self.board[i][j] == 0 and self.board[i+1][j] == 0:
						self.remaining.append((i,j))
		else:
			for i in range(BSIZE):
				for j in range(BSIZE-1):
					if self.board[i][j] == 0 and self.board[i][j+1] == 0:
						self.remaining.append((i,j))
"""

def availableLocations(board, player, tag='all'):
	
	res = []
	
	if tag == 'sym':
		if sum(map(sum,board)) == 0:
			for i in range((BSIZE + 1)/2):
				for j in range((BSIZE + 1)/2):
					res.append((i,j))
			return res


	for i in range(BSIZE):
		for j in range(BSIZE):
			if canPlaceOn(board, i, j, player):
				res.append((i,j))

	return res	

# consider the symmetry?
def availableLocationsSymmetry(board, player):



def copyBoard(board):
	res = []
	for i in range(len(board)):
		tmp = []
		for j in range(len(board[i])):
			tmp.append(board[i][j])
		res.append(tmp)
	return res


# Heuristic function for evaluating the overwhelming advantage that is highly possible to end
# input: the board
# 0 1 0 0 0
# 0 1 0 0 0
# 0 0 0 1 0
# 1 1 0 1 0
# 0 0 0 0 0   
# -> left player has 2 slots and right player only 1
# players are numbered 1 and -1

def numSlotsForTwoPLayers(board):

	num_slot_left = 0
	num_slot_right = 0

	# store the temp subtracting and adding back slots
	tmp_left = []
	tmp_right = []


	for i in range(BSIZE):
		for j in range(BSIZE):
			
			# recognizing the slots
			if canPlaceOn(board, i, j, 1):
				if not canPlaceOn(board, i, j, -1) and not canPlaceOn(board, i+1, j, -1):
					num_slot_left += 1
					placeOnBoard(board, i, j, 1)
					tmp_left.append((i,j))

			if canPlaceOn(board, i, j, -1):
				if not canPlaceOn(board, i, j, 1) and not canPlaceOn(board, i, j+1, 1):
					num_slot_right += 1
					placeOnBoard(board, i, j, -1)
					tmp_right.append((i,j))

	for i in range(len(tmp_left)):
		removeFromBoard(board, tmp_left[i][0], tmp_left[i][1], 1)

	for i in range(len(tmp_right)):
		removeFromBoard(board, tmp_right[i][0], tmp_right[i][1], -1)

	return (num_slot_left, num_slot_right)


# Evaluate whether the player can place a domino in the (i,j) of the board
# This function is of time O(1)
def canPlaceOn(board, i, j, player):
	if player == 1:
		if i >= BSIZE - 1:
			return False
		elif board[i][j] + board[i+1][j] == 0:
			return True
		else:
			return False
	else:
		if j >= BSIZE - 1:
			return False
		elif board[i][j] + board[i][j+1] == 0:
			return True
		else:
			return False


def isOverwhelmed(board, threshold):
	 (l, r) = numSlotsForTwoPLayers(board)
	 if abs(l - r) >= threshold:
	 	if l > r: 
	 		winner = 1
	 	else:
	 		winner = -1
	 	return (True, winner)
	 else:
	 	return (False, 0)


# place the domino on the board
def placeOnBoard(board, i, j, player):

	if canPlaceOn(board, i, j, player):
		board[i][j] = 1
		if player == 1:
			board[i+1][j] = 1
		else:
			board[i][j+1] = 1
		return 1
	else:
		return 0


# remove a domino from board
def removeFromBoard(board, i, j, player):
	board[i][j] = 0
	if player == 1:
		board[i+1][j] = 0
	else:
		board[i][j+1] = 0


# define if there is such a dominoe on the board
def existDomino(board, i, j, player):
	if player == 1:
		if i < BSIZE - 1:
			if board[i][j] == 1 and board[i+1][j] == 1:
				return True
			else:
				return False
		else:
			return False
	else:
		if j < BSIZE - 1:
			if board[i][j] == 1 and board[i][j+1] == 1:
				return True
			else:
				return False
		else:
			return False


def initializeBoard(board):

	#board = [[0]*BSIZE]*BSIZE
	for i in range(BSIZE):
		board.append([0]*BSIZE)
		"""
	for i in range(BSIZE-1):
		for j in range(BSIZE):
			remaining_v.append((i,j))
			remaining_h.append((j,i))
			"""


def switch(player):
	return -1/player


## ================================ MinMax function ==================================
## recursively calling
"""
function minimax(node, depth, maximizingPlayer)
	if depth = 0 or node is a terminal node
		return the Heuristic value of node
	if maximizingPlayer
		bestValue = -inf
		for each child of node:
				v = minimax(child, depth + 1, switch(maximizingPlayer))
				bestValue = max(bestValue, v)
		return bestValue
	else
		bestValue = inf
		for each child of node:
				v = minimax(child, depth + 1, maximizingPlayer)
				bestValue = min(bestValue, v)
		return bestValue
"""

def minMax(startingNode, player):
	if(abs(startingNode.value) == maxsize):
		return startingNode.value

	bestValue = maxsize * (-1) * player

	which = 0

	if player == 1:
		for i in range(len(startingNode.children)):
			child = startingNode.children[i]
			val = minMax(child, switch(player))
			if val > bestValue:
				which = i
				bestValue = val

	else:
		for i in range(len(startingNode.children)):
			child = startingNode.children[i]
			val = minMax(child, switch(player))
#			bestValue = min(bestValue, val)
			if val < bestValue:
				which = i
				bestValue = val
	
	#print startingNode.depth, which
	return bestValue


# check whether some player wins
def winCheck(board, player):

	if len(availableLocations(board, player)) == 0:
		print "*"*60
		if player == 1:
			print "Vertical player can not place anymore. The horizontal player wins!"
		else:
			print "Horizontal player can not place anymore. The vertical player wins!"
		print "*"*60
		return 0

	return 1


# print the board neatly
def printBoard(board):

	print "The board is:"

	for i in range(BSIZE):
		for j in range(BSIZE):

			if board[i][j]:
				print '*',
			else:
				print 'o',
		print



# =================================== THE MAIN FUNCTION ===================================
if __name__ == "__main__":

	depth = 0
	curPlayer = 1

	board = []
	initializeBoard(board)

	root = Node(0, 1, board, None)

	#print COUNT_ALLNODES
	#print COUNT_LEAVES

	print "*" * 60
	print "INSTRUCTIONS: type in the location you desire to place the domino like 1,2\n"
	print "It indicates the left part of the domino when you are horizontal player,"
	print "or the upper part of the domino when you are vertical player.\n"
	print "The first player who cannot place more domino on the board will lose."
	print "*" * 60, '\n'

	terminate = 0

	while not terminate:

		inputCorrect = 1

		while 1:
			while True:
				choice = input("Choose your location to place the domino. Type as x,y: ");

				try:
					x = int(choice[0])
					y = int(choice[1])
					break;
				except:
					# Generating exception when the input format is bad.
					print "Incorrect input format. Re-enter:"
		
			# Reject the placement on an illegal place
			if canPlaceOn(board, x, y, curPlayer):
				break;
			else:
				print "You cannot place there.\n"

		placeOnBoard(board, x, y, curPlayer)

		if winCheck(board, -1 * curPlayer):
			curPlayer *= -1
			node = Node(depth + 1, curPlayer, board, None)

			bestVal = -1 * curPlayer * maxsize

			for i in range(len(node.children)):

				child = node.children[i]; 
				val = minMax(child, switch(curPlayer))

				if abs(curPlayer * maxsize - val) <= abs(curPlayer * maxsize - bestVal):
					bestEdge = node.children[i].edge
					bestVal = val

			print "Computer chooses to locate at ", bestEdge
			placeOnBoard(board, bestEdge[0], bestEdge[1], curPlayer)
			curPlayer *= -1

			printBoard(board)

			if not winCheck(board, curPlayer):
				printBoard(board)
				terminate = 1

		else:
			printBoard(board)
			terminate = 1

	print "Ending of the demo"


