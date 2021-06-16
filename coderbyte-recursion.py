

def sum(l):
	
	if not l:
		return 0
	
	return l[0] + sum(l[1:])

def sum2(l):

	return _sum2(l,0)

def _sum2(l,idx):

	if idx == len(l):
		return 0

	return l[0] + _sum2(l,idx+1)

if __name__ == '__main__':
	l = [1,1,1,1,1,1,1,1]
	print(sum(l))
	print(sum2(l))
