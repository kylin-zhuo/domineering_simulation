# print the board neatly
def printBoard(board):

	print "The current board is:"

	for i in range(4):
		for j in range(4):

			if board[i][j]:
				print '*',
			else:
				print 'o',
		print



if __name__ == '__main__':
	board = [[0,1,0,0],[0,1,0,0],[1,1,0,0],[0,0,0,0]]

	printBoard(board)