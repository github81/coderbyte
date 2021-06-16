



#[a,b,c]

#						[]
# a			[]						[a]
# b		[]		[b]				[a]		[a,b]
# c	[]				[b,c]	[a]				[a,b,c]	

def combinations(l):

	if not l:
		return [[]]
		
	first = l[0]
	rest = l[1:]
	
	combWithoutFirst = combinations(rest)
	combWithFirst = []
	for c in combWithoutFirst:
		nl = c[:]
		nl.append(first)
		combWithFirst.append(nl)
	
	return combWithoutFirst + combWithFirst
	

def PowerSet(inputStr):
    # Write your code here
	if len(inputStr) == 0:
		return [""]
    
	first = inputStr[0]
	rest = inputStr[1:]
	strWithoutFirst = PowerSet(rest)
	strWithFirst = []
	for s in strWithoutFirst:
		s += first
		strWithFirst.append(s)

	return sorted(strWithFirst + strWithoutFirst)

if __name__ == '__main__':
	#l = ['a','b','c']
	#print(combinations(l))
	print(PowerSet("abc"))
	

