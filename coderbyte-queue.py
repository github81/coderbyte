

class Node:
	def __init__(self,val):
		self.val = val
		self.next = None
		
class Queue:
	def __init__(self):
		self.front = None
		self.back = None
		self.size = 0
		
	def enqueue(self,val):
		newNode = Node(val)
		if self.size == 0:
			self.front = newNode
			self.back = newNode
		else:
			self.back.next = newNode
			self.back = newNode
		self.size+=1
			
	def dequeue(self):
		if self.size == 0:
			return None
		if self.size == 1:
			self.back = None			
		val = self.front.val
		self.front = self.front.next
		self.size-=1
		return val
		
if __name__=='__main__':
	
		q = Queue()
		q.enqueue('a')
		q.enqueue('b')
		q.enqueue('c')
		print(q.dequeue())
		print(q.dequeue())
		q.enqueue('d')
		print(q.dequeue())
		print(q.dequeue())
		print(q.size)
		print(q.front)
		print(q.back)
		print(q.dequeue())
