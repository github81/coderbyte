
#[a,b,c]

#								[]
#								[a]
# b				[b,a]						[a,b]
# c		[c,b,a]	[b,c,a]	[b,a,c]		[c,a,b]	[a,c,b]	[a,b,c]	


def permutations(l):

	if not l:
		return [[]]
	
	first = l[0]
	rest = l[1:]
	permWithoutFirst = permutations(rest)
	permWithFirst = []
	for p in permWithoutFirst:
		for i in range(0,len(p)+1,1):
			tl = p[:]
			tl.insert(i,first)
			permWithFirst.append(tl)
			
	return permWithFirst

if __name__=="__main__":
	l = ['a','b','c']
	print(permutations(l))




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
        return ""
    
    first = inputStr[0]
    rest = inputStr[1:]
    strWithoutFirst = PowerSet(rest)
    strWithFirst = []
    for s in strWithoutFirst:
        #print(s)
        s += first
        strWithFirst.append(s)
        
    return strWithoutFirst
	
		

if __name__ == '__main__':
	#l = ['a','b','c']
	#print(combinations(l))
	print(PowerSet("abc"))

