import os
import sys,tty

class Snake:

	def __init__(self):
		self.body = [
					[4,1],
					[4,2],
					[4,3],
					[4,4]
						]
		
	def draw(self):
		os.system("clear")
		for r in range(1,11):
			print("-",end="")
		for r in range(1,11):
			for c in range(1,11):
				if [r,c] in self.body:
					print('*', end="")
				else:
					print(' ', end="")
			print("")
	
	def move(self, direction):
		head = self.body[len(self.body)-1]
		if direction == "up":
			newHead = map(sum, zip(head, [-1,0]))
		elif direction == "down":
			newHead = map(sum, zip(head, [1,0]))
		elif direction == "left":
			newHead = map(sum, zip(head, [0,-1]))
		else:			
			newHead = map(sum, zip(head, [0,1]))
		self.body.append(list(newHead))
		self.body.pop(0)
		#print(self.body)
		self.draw()


if __name__=='__main__':
	s = Snake()
	s.draw()
	run=True
	tty.setcbreak(sys.stdin)
	while run:
		val=ord(sys.stdin.read(1))
		if val==65:
			s.move("up")
		if val==66:
			s.move("down")
		if val==67:
			s.move("right")
		if val==68:
			s.move("left")
