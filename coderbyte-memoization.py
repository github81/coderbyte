import time

# 0,0 -> 0
# 0,1 -> 0
# 1,0 -> 0
# 1,1 -> 1

def travellingSalesman(x, y):

	route = {}
	def moveDownRight(x, y):

		if (x,y) in route:
			return route[(x,y)]
		if x == 0 or y == 0:
			return 0
		if x == 1 and y == 1:
			return 1
		
		route[(x-1,y)] = moveDownRight(x-1,y)
		route[(x,y-1)] = moveDownRight(x,y-1)
		route[(y,x-1)] = route[(x-1,y)]
		route[(y-1,x)] = route[(x,y-1)]
		return  route[(x-1,y)] + route[(x,y-1)]

	return moveDownRight(x, y)


def travellingSalesman2(x, y):

	route = {}
	def moveDownRight(x, y):

		if (x,y) in route:
			return route[(x,y)]
		if x == 0 or y == 0:
			return 0
		if x == 1 and y == 1:
			return 1
		
		route[(x,y)] = moveDownRight(x-1,y) + moveDownRight(x,y-1)
		route[(y,x)] = route[(x,y)]
		return  route[(x,y)]

	return moveDownRight(x, y)

def canSum(targetSum,arr):

	if targetSum == 0:
		return True
	if targetSum < 0:
		return False
	
	for i in arr:
		return canSum(targetSum-i,arr)

	return False
	

def minimumStepsToOne(num):

	if num == 1:
		return 0
	
	s = 0	
	while num != 1:
	
		if num%3==0:
			num //= 3
			s += 1
			

if __name__ == '__main__':

	'''
	print("before {}".format(int(round(time.time() * 1000))))
	print(travellingSalesman(50,50))
	print("after {}".format(int(round(time.time() * 1000))))
	#pass
	
	print("before {}".format(int(round(time.time() * 1000))))
	print(travellingSalesman2(50,50))
	print("after {}".format(int(round(time.time() * 1000))))
	'''
	
	print(canSum(7,[2,3])) # false
	print(canSum(7,[5,3,4,7])) # true
	#print(canSum(7,[2,4])) # false
	#print(canSum(7,[2,3,5])) # true
	#print(canSum(300,[7,14])) # false
	#print(canSum(7,[0])) # false
	
