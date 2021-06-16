
class Node:

	def __init__(self,val):
		self.val = val
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None
		
	def append(self,val):
		
		if not self.head:
			self.head = Node(val)
			return
		
		curr = self.head
		while curr.next is not None:
			curr = curr.next
		curr.next = Node(val)

	# append recursive call		
	def appendRecur(self,val):
	
		if not self.head:
			self.head = Node(val)
			return
		
		self._append(val,self.head)
		
			
	def _append(self,val,curr):
	
		if curr.next is None:
			curr.next = Node(val)
			return

		self._append(val,curr.next)		
		
	def printList(self):
		
		print("printing ..")
		curr = self.head
		while curr is not None:
			print(curr.val)
			curr = curr.next
			
	def _printList(self,newHead):
	
		print("printing ..")
		while newHead is not None:
			print(newHead.val)
			newHead = newHead.next
			
	def doesContain(self,target):
	
		curr = self.head
		while curr is not None:
			if curr.val == target:
				return True
			curr = curr.next
		
		return False
		
	def doesContainRecur(self,target):
	
		return self._doesContain(target,self.head)
		
	def _doesContain(self,target,curr):
	
		if curr is None:
			return False
		if curr.val == target:
			return True
			
		return self._doesContain(target,curr.next)
	
	def sum(self):
		return self._sum(self.head)
		
	def _sum(self,curr):
	
		if curr is None:
			return 0
			
		return curr.val + self._sum(curr.next)
		
	def deleteValue(self,target):
	
		curr = self.head
		prev = None
		
		while curr is not None:
			if curr.val == target:
				if prev is not None:
					prev.next = curr.next
				else:
					prev = curr.next
					self.head = prev
				break
			prev = curr
			curr = curr.next
			
		return self.head
		
	def deleteValueRecur(self,target):
	
		self._deleteValue(target,None,self.head)
		
	def _deleteValue(self,target,prev,curr):
		
		if curr is None:
			return
		if curr.val == target:
			if prev is not None:
				prev.next = curr.next
			else:
				prev = curr.next
				return prev
		
		return self._deleteValue(target,curr,curr.next)
		
		
	def reverse(self):
		prev = None
		curr = self.head
		while curr is not None:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt
		return prev
		
	def reverseRecur(self):
	
		print("recursive ..")
		return self._reverse(self.head)
		
	def _reverse(self,curr,prev=None):
	
		if curr is None:
			return prev
		
		nxt = curr.next
		curr.next = prev
		
		return self._reverse(nxt,curr)
			
				
if __name__=="__main__":

	ll = LinkedList()
	ll.append(2)
	ll.append(3)
	ll.append(4)
	ll.append(5)
	ll.append(6)
	
	ll.printList()
	print(ll.doesContain(4))
	print(ll.doesContain(7))

	print(ll.sum())
	print(ll.doesContainRecur(4))
	print(ll.doesContainRecur(7))
	
#	ll.printList()
#	ll.deleteValue(4)
#	ll.printList()
#	ll.deleteValue(6)
#	ll.printList()
#	newHead = ll.deleteValue(2)
#	ll._printList(newHead)

#	ll.printList()
#	ll.deleteValueRecur(4)
#	ll.printList()
#	ll.deleteValue(6)
#	ll.printList()
#	ll.deleteValue(2)
#	ll.printList()

#	newHead = ll.reverse()
#	ll._printList(newHead)
	newHead = ll.reverseRecur()
	ll._printList(newHead)

	
