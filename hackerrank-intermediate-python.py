

def modify_array():

	li = [9, 8, 7, 2, 3, 3]
	a = len(li)
	c = 0
	li = map(int,li)
	
	for i in range(0,a):
		if len(li) == 0:
			break
		mi = min(li)
		if mi == li[0]:
			li.pop(0)
		c = li.count(mi)
		for d in range(0,c):
			li.remove(mi)
			c += 1

	return c


#space = [1,2,3,1,2]

#s	sp	num		i	x	space[i]
#[0]	0	1		0	3	1

	
def disk_space_analysis(x, space):
	
	s = []
	s.append(0)
	sp = 0
	num = 1
	for i in range(0,len(space)):
		if i < x:
			if space[i] < space[len(s)-1]:
				s.pop()
				s.append(i)
		else:
			idx = space[len(s)-1]
			if idx >= num:
				s.append(i if space[i] < space[idx] else idx)
			else:
				s.append(i)
				j = num
				c = 0
				while c < x:
					if space[j] < space[len(s)-1]:
						s.pop()
						s.append(j)
					c+=1
					j+=1
			num+=1

	print(s)
	l = [space[s[i]] for i in range(0,len(s))]
	print(l)
	#return max([space[s[i]] for i in range(s)])

def disk_space_analysis2(x,space):

	s = []
	s.append(0)
	sp = 0
	num = 1
	for i in range(0,len(space)):
		if i < x:
			if space[i] < space[len(s)-1]:
				s.pop()
				s.append(i)
		else:
			top = s[len(s)-1]
			if top >= num:
				t = i if space[i] < space[top] else top
			else:
				s.append(i)
				j = num
				c = 0
				while c < x:
					top = s[len(s)-1]
					if space[j] < space[top]:
						s.pop()
						s.append(j)
					j+=1
					c+=1
			num+=1	
			
	
	print(s)


def minSlidingWindow(nums: 'List[int]', k: 'int') -> 'List[int]':
	if k == 1:
		return max(nums)
	n = len(nums)
	if n * k == 0:
		return []

	left = [0] * n
	left[0] = nums[0]
	right = [0] * n
	right[n - 1] = nums[n - 1]
	for i in range(1, n):
		# from left to right
		if i % k == 0:
			# block start
			left[i] = nums[i]
		else:
			left[i] = min(left[i - 1], nums[i])
		# from right to left
		j = n - i - 1
		if (j + 1) % k == 0:
			# block end
			right[j] = nums[j]
		else:
			right[j] = min(right[j + 1], nums[j])

	output = []
	for i in range(n - k + 1):
		output.append(min(left[i + k - 1], right[i]))

	print(output)
	return max(output)
		
	
def modify_array(s):
	
	if len(s) <= 2:
		return 0
		
	i = 1
	j = len(s)-2
	
	f_prev_num = s[0]
	b_curr_num = s[len(s)-1]
	mc1 = 0
	mc2 = 0
	s1 = []
	s2 = []	
	while i < len(s):
		if s[i] < f_prev_num:
			#print("{},{}".format(s[i],f_prev_num))
			mc1 += abs(f_prev_num - s[i])
		else:
			f_prev_num = s[i]
		
		if s[j] < b_curr_num:
			mc2 += abs(b_curr_num - s[j])
		else:
			b_curr_num = s[j]
		
		i+=1
		j-=1

	#print(mc1)
	#print(mc2)
	return mc1 if mc1 < mc2 else mc2	
	#return mc2


	#s = [0,1,2,5,6,5,7]

def modify_array2(a):

	from queue import PriorityQueue

	d_mc = 0
	d_pq = PriorityQueue()
	
	i_mc = 0
	i_pq = PriorityQueue()
	
	n = len(a)
	for i in range(n):
	
		#d_tmp = 0
		i_tmp = 0
		
		#if not d_pq.empty():
		#	d_tmp = d_pq.get()
		#	d_pq.put(d_tmp)
			
		if not i_pq.empty():
			i_tmp = i_pq.get()
			i_pq.put(i_tmp)
			
		#if not d_pq.empty() and d_tmp < a[i]:
		#	d_mc += abs(a[i] - d_tmp)
		#	d_pq.get()
			
		if not i_pq.empty() and i_tmp > a[i]:
			i_mc += abs(a[i] - i_tmp)
			i_pq.get()
		
		#d_pq.put(a[i])
		i_pq.put(a[i])
		
		
	return i_mc
	#return d_mc if d_mc < i_mc else i_mc
	
#s = [0,1,2,5,6,5,7]
#s = [1,3,1,1,3,1,3]

#my version
def modify_array3(a):

	i_mc = 0
	i_q = []
	
	d_mc = 0
	d_q = []
	
	for i in range(0,len(a)):
	
		i_tmp = 0
		if len(i_q) > 0:
			i_tmp = i_q[len(i_q)-1]

		d_tmp = 0
		if len(d_q) > 0:
			d_tmp = d_q[len(d_q)-1]

		if len(i_q) > 0 and i_tmp > a[i]:
			i_mc += abs(a[i] - i_tmp)
			i_q.append(i_tmp)
		else:
			i_q.append(a[i])

		if len(d_q) > 0 and d_tmp < a[i]:
			d_mc += abs(a[i] - d_tmp)
			d_q.append(d_tmp)
		else:
			d_q.append(a[i])
		
		#i_q.append(a[i])	
		#d_q.append(a[i])	

	print("{},{}".format(i_mc,i_q))
	print("{},{}".format(d_mc,d_q))
	
	return i_mc if i_mc < d_mc else d_mc
	
	
def modify_array4(a):

	i_mc = 0
	i_q = []
		
	for i in range(0,len(a)):
	
		i_tmp = 0
		if len(i_q) > 0:
			i_tmp = i_q[len(i_q)-1]

		if len(i_q) > 0 and i_tmp > a[i]:
			i_mc += abs(a[i] - i_tmp)
		i_q.append(a[i])

		
		#i_q.append(a[i])	
		#d_q.append(a[i])	

	print("{},{}".format(i_mc,i_q))
	#print("{},{}".format(d_mc,d_q))
	
	return i_mc
	#return i_mc if i_mc < d_mc else d_mc			


# Python3 program of the above approach
import sys
 
# Dp array to memoized
# the value recursive call
dp = [[ 0 for x in range(1000)]
          for y in range(1000)]
 
# Function to find the minimum increment
# or decrement needed to make the array
# sorted
def minimumIncDec(arr, N, maxE, minE):
 
    # If only one element is present,
    # then arr[] is sorted
    if (N == 0):
        return 0
 
    # If dp[N][maxE] is precalculated,
    # then return the result
    if (dp[N][maxE]):
        return dp[N][maxE]
 
    ans = sys.maxsize
 
    # Iterate from minE to maxE which
    # placed at previous index
    for k in range(minE, maxE + 1):
 
        # Update the answer according to
        # recurrence relation
        x = minimumIncDec(arr, N - 1, k, minE)
        ans = min(ans, x + abs(arr[N - 1] - k))
 
    # Memoized the value
    # for dp[N][maxE]
    dp[N][maxE] = ans
 
    # Return the final result
    return dp[N][maxE]
 


def modify_array5(arr):

	a_arr = sorted(arr)
	d_arr = sorted(arr,reverse=True)
	
	a_sum = 0
	d_sum = 0
	
	for i in range(len(arr)):
		a_sum += abs(arr[i]-a_arr[i])
		d_sum += abs(arr[i]-d_arr[i])
	
	return a_sum if a_sum < d_sum else d_sum

import bisect

def parse(seq):
    for i in range(len(seq)):
        seq[i] -= i

def patience_sort(array):
    piles = [array[0]]
    for x in range(1, len(array)):
        i = bisect.bisect_right(piles, array[x])
        if i != len(piles):
            piles[i] = array[x]
        else:
            piles.append(array[x])
    return len(piles)


# working version
def getMinimumOps(ar):
     
    print(ar)
    n = len(ar)
    small = min(ar)
    large = max(ar)
    i_dp = [[ 0 for i in range(large + 1)] for i in range(n)]
    d_dp = [[ 0 for i in range(large + 1)] for i in range(n)]

 
    for j in range(small, large + 1):
        #print("{},{}".format(ar[0],j))
        i_dp[0][j] = abs(ar[0] - j)
        d_dp[0][j] = abs(ar[0] - j)
        

    for i in range(1, n):
        i_min = 10**9
        d_min = 10**9
        #print("next row {}".format(i))
        for j in range(small, large + 1):
        #for j in range(large,small-1,-1):
             
            i_min = min(i_min, i_dp[i - 1][j])
            #print("{},{},{},{},{}".format(i,j,i_min,dp[i-1][j],ar[i]))
            i_dp[i][j] = i_min + abs(ar[i] - j)
                        

    ans = 10**9
    for j in range(small, large + 1):
        ans = min(ans, i_dp[n - 1][j])
        #print(ans)

    #ans=0
    return ans
    




def modify_array_lonnie(arr):

	s = []
	s1 = []
	mc_1 = 0
	mc_2 = 0
	
	print(arr)
	min = arr[len(arr)-1]
	max = arr[0]
	s.insert(0,min)
	s1.insert(0,max)
	for j in range(len(arr)-2,-1,-1):
		if arr[j] <= min:
			min = arr[j]
			s.insert(0,arr[j])
		else:
			mc_1 += abs(arr[j]-min)
			s.insert(0,min)
				
		i = len(arr)-j-1
		if arr[i] <= max:
			max = arr[i]
			s1.append(arr[i])
		else:
			mc_2 += abs(arr[i]-max)
			s1.append(max)

	print(s)
	print(s1)
	print(mc_1)
	print(mc_2)
	return mc_1 if mc_1 < mc_2 else mc_2
		

#can submit
def modify_array_lonnie2(arr):

	print(arr)
	#print([9, 8, 7, 4, 5, 4])
	s = []
	s1 = []
	mc_1 = 0
	mc_2 = 0
	n = len(arr)
	mn=arr[0]
	mx=arr[n-1]
	s.insert(0,mn)
	s1.insert(0,mx)

	#s = [9,8,7,2,3,3]
		
	#s = [0,1,2,5,6,5,7]
	
	for i in range(1,n):

		if arr[i] >= mn:
			mn = arr[i]
			s.append(mn)
		elif arr[i] < mn:
			mc_1 += abs(arr[i]-mn)
			s.append(mn)
			
		j = n-i-1
		if arr[j] < mx:
			mc_2 += abs(arr[j]-mx)
			s1.insert(0,mx)
		elif arr[j] >= mx:
			mx = arr[j]
			s1.insert(0,mx)
			
	print("{},{}".format(s,mc_1))
	print("{},{}".format(s1,mc_2))
				
	return mc_1 if mc_1 < mc_2 else mc_2
	

def disk_space_analysis(space, k):

	if k == 1:
		return max(space)
	n = len(space)
	if n * k == 0:
		return []

	fp = 0
	sp = 0


#space = [1,2,3,1,2]

def disk_space_analysis_jing(space,k):

	max = 0
	for i in range(0,len(space)-k+1):
	
		#print("{},{}".format)
		mn = min(space[i:i+k])
		if mn > max:
			max = mn
			
	return max
			
	


if __name__ == "__main__":

	s = [1,2,3,1,2]
	print(disk_space_analysis_jing(s,3))


	#s = [0,1,2,5,6,5,7]
	#s = [9,8,7,2,3,3]
	#s = [1,2,3,3,4]
	#s = [1,3,1,1,3,1,3]
	#s = [95,	9847,	3752,	5621,	7012,	1986,	3090,	1383,	6257,	9501,	7004,	6181,	9387,	9137,	9305,	7795,	9310,	3904,	8328,	6656,	8123,	1796,	2754,	4372,	5200,	3893,	8568,	4436,	3973,	8498,	1879,	2731,	4651,	4388,	453,	2465,	2669,	6384,	819,	8565,	1952,	7219,	4362,	3012,	9380,	2645,	4800,	2945,	5778,	1993,	1170,	1356,	8557,	1497,	8921,	670,	5155,	9115,	1095,	9400,	9451,	9344,	4393,	4201,	8167,	8129,	2004,	8839,	1457,	7682,	1881,	9266,	6366,	9889,	242,	5318,	5248,	3670,	7381,	6567,	2317,	2162,	6670,	5876,	1179,	2482,	9270,	4326,	4166,	6122,	2016,	3008,	5349,	1723,	5816,	4030,]
	
	#s = [95,	9847,	3752,	5621,	7012,	1986,	3090,	1383]
	#s = [95,        ,   3752,   5621,   7012,                       ]
	#s = [95,    3752,   3752,   5621,   7012,   7012,   7012,   7012]
	
	
	#s = [9,8,7,2,2,3,4]
	#s = [9,8,7,4,5,4]
	#print(modify_array_lonnie2(s))

	#s = [9,8,7,3,2,3,4,5]
	#s = [9,8,7,2,2,2,2]
	#s = [1,3,1,1,3,1,3]
	#s = [1,2,3,2]
	#s = [95, 9847, 3752, 5621, 7012, 1986, 3090, 1383]
	#s = [95,	9847,	3752,	5621,	7012,	1986,	3090,	1383,	6257,	9501,	7004,	6181,	9387,	9137,	9305,	7795,	9310,	3904,	8328,	6656,	8123,	1796,	2754,	4372,	5200,	3893,	8568,	4436,	3973,	8498,	1879,	2731,	4651,	4388,	453,	2465,	2669,	6384,	819,	8565,	1952,	7219,	4362,	3012,	9380,	2645,	4800,	2945,	5778,	1993,	1170,	1356,	8557,	1497,	8921,	670,	5155,	9115,	1095,	9400,	9451,	9344,	4393,	4201,	8167,	8129,	2004,	8839,	1457,	7682,	1881,	9266,	6366,	9889,	242,	5318,	5248,	3670,	7381,	6567,	2317,	2162,	6670,	5876,	1179,	2482,	9270,	4326,	4166,	6122,	2016,	3008,	5349,	1723,	5816,	4030,]
	
	#print(getMinimumOps(s))

	#arr = [ 5, 4, 3, 2, 1 ]
	#N = len(arr)
 
	# Find the minimum and maximum
	# element from the arr[]
	#minE = min(arr)
	#maxE = max(arr)
 
	# Function Call
	#print(minimumIncDec(arr, N, maxE, minE))
	
	#s = [9,8,7,2,2,3]
	#s = [9,7,7,2,5,2]
	#s = [1,2,3,3,4]
	
	#s = [1,3,1,1,3,1,3]
	#s = [1,1,1,1,3,3,3]
	
	#s = [3,3,3,3,1,1,1]
	#s = [5,4,4,8,10,1,2]
	#s = [4,4,4,8,10,10,10]
	#s = [10,10,10,10,10,10,1,1]
	#s = [10,10,10,10,10,1,1]
	#    5,5,8,10,10,10]
	#s = [4,4,4,8,8,]

	#s = [3,2,1,4,5,4]
	#s = [2,2,2,4,5,5]
	#print(modify_array(s))
	#print(modify_array2(s))

	#s = [0,1,2,5,6,5,7]
	#s = [2,2,2,4,4,4]
	#s = [1,3,1,1,3,1,3]
	#s = [9,8,7,2,2,3]
	#s = [1,3,1,1,3,1,3]
	#s = [5,4,4,8,10,1,2]
	#print(modify_array3(s))
	#print(modify_array4(s))
	#print(modify_array5(s))
	
	#space = [1,2,3,1,2,3,3,4]
	# 1,2,3 => 1
	# 2,3,1 => 1
	# 3,1,2 => 1
	# 1,2,3 => 1
	# 2,3,3 => 2
	# 3,3,4 => 3
	#x = 3
	#disk_space_analysis(x, space)
	##print(minSlidingWindow(space,x))
