def getNumDeletedBlock(board):

	if not type(board).__name__ == 'list':
		return print("input type should be list")
	else:
		if len(board) == 0:
			return print("Empty list is not allowed")
		elif len(board) > 30:
			return print("m should be equal to or less than 30")
		elif len(board[0]) < 2:
			return print("n should be equal to or bigger than 2")
	
	rowMax = len(board) - 1
	colMax = len(board[0]) - 1			
	
	findBlock(board, rowMax, colMax)
	

def findBlock(board, rowMax, colMax):
	
	tranformedBoard = []
	result = []
	
	# j : row , i : column
	for j, element in enumerate(board):
		tranformedBoard.append(changeStrToList(element))
		for i, letter in enumerate(element):
			if letter is not None and i is not colMax and j is not rowMax:
				if letter is element[i+1] and letter is board[j+1][i] and letter is board[j+1][i+1]:
					result.append((j, i))

	if len(result) is not 0:
		nextRoundBoard = moveBlockDown(removeBlock(tranformedBoard, result))
		findBlock(nextRoundBoard, rowMax, colMax)
	else:
		return print(countRemovedBlock(tranformedBoard))


def removeBlock(board, removePoints):
	for point in removePoints:
		x = point[0]
		y = point[1]
		board[x][y] = "*"
		board[x+1][y] = "*"
		board[x][y+1] = "*"
		board[x+1][y+1] = "*"

	print("removeBlock", board)
	return board


def moveBlockDown(board):
	maxRow = len(board) - 1
	for idx, row in enumerate(board):
		for i in range(0, len(row)):
			if idx is not maxRow:
				if board[idx+1][i] is "*":
					board[idx+1][i] = row[i]
					board[idx][i] = None

	print("moveBlockDown", board)
	return board


def countRemovedBlock(board):
	removedBlockNum = 0
	for row in board:
		for element in row:
			if element is None:
				removedBlockNum += 1

	return removedBlockNum
		

def changeStrToList(str):
	result = []

	for letter in str:
		result.append(letter)

	return result


sampleData1 = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
getNumDeletedBlock(sampleData1)
sampleData2 = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]	
getNumDeletedBlock(sampleData2)