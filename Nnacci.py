##Calculate N step fibonnaci sequence (for example tribonacci)
## This example calcualtes an 11 step fibonnaci (i.e. 11Nacci) 

print("Nnacci calc 11:")
An =0
def fiblike(start):
	addnum = len(start)
	memo = start[:]
	def fibber(n):
		try:
			return memo[n]
		except IndexError:
			ans = sum(fibber(i) for i in range(n-addnum, n))
			memo.append(ans)
			return ans
	return fibber



fibo = fiblike([1] + [2**i for i in range(11-1)])
for i in range(1000) :
    An = fibo(i)
#Calculate the odds Of An / 2N
print(An/2**1000)
