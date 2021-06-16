

class Node:
	def __init__(self,val):
		self.val = val
		self.next = None
		
class Stack:
	def __init__(self):
		self.top = None
		self.size = 0
		
	def push(self,val):
		if self.size == 0:
			self.top = Node(val)
		else:
			pushedNode = Node(val)
			pushedNode.next = self.top
			self.top = pushedNode
		self.size+=1
		
	def getTop(self):
		return self.top.val
		
	def pop(self):
		if self.size == 0:
			return None
		val = self.top.val
		self.top = self.top.next
		self.size-=1
		return val
		
	def getSize(self):
		return self.size
			
if __name__=='__main__':

	s = Stack()
	s.push('a')
	s.push('b')
	s.push('c')
	print(s.pop())
	print(s.getSize())
	print(s.pop())
	print(s.pop())
	print(s.pop())
	print(s.getSize())
	
		
	