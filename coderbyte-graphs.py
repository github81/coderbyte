
vertices = ['A','B','C','D','E']
edges = [
		['A','B'],
		['A','D'],
		['B','C'],
		['C','D'],
		['C','E'],
		['D','E']
		]
		
vertexIndices = {
				'A': 0,
				'B': 1,
				'C': 2,
				'D': 3,
				'E': 4
				}		
edgesIndices = [
				[0,1,0,1,0],
				[1,0,1,0,0],
				[0,1,0,1,1],
				[1,0,1,0,1],
				[0,0,1,1,0]
				]

def isAdjacent(node1,node2):
	for e in edges:
		if (e[0] == node1 and e[1] == node2) or (e[1] == node1 and e[0] == node2):
			return True
	return False
	
def findAdjacentNodes(node):
	adjacentArray = []
	for e in edges:
		if e[0] == node:
			adjacentArray.append(e[1])
		elif e[1] == node:
			adjacentArray.append(e[0])	
	return adjacentArray
		

def isAdjacentMatrix(node1, node2):
	return True if edgesIndices[vertexIndices[node1]][vertexIndices[node2]] else False
	
def findAdjacentNodesMatrix(node):
	adjacentArray = []
	vertexArray = edgesIndices[vertexIndices[node]]
	for i in range(0,len(vertexArray)):
		if vertexArray[i] == 1:
			adjacentArray.push(vertices[i])
	return adjacentArray


if __name__=='__main__':

	print(findAdjacentNodes('A'))
	print(isAdjacent('C','D'))
	print(findAdjacentNodes('A'))
	print(isAdjacentMatrix('C','D'))
	print(findAdjacentNodes('C'))
	
