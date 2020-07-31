import sys
sys.stdin = open('travel_restrictions_input.txt','r')
sys.stdout = open('output1.txt','w')

t=int(input())
for k in range(1,t+1):
	n=int(input())
	inc=list(input())
	out=list(input())
	inc=['N']+inc
	out=['N']+out
	a=[]
	for i in range(n+1):
		l=[]
		for j in range(n+1):
			if(i==j):
				l.append('Y')
			else:
				l.append('N')
		a.append(l)
	for i in range(1,n):
		if(out[i]=='Y' and inc[i+1]=='Y'):
			a[i][i+1]='Y'
		else:
			a[i][i+1]='N'
		if(out[i+1]=='Y' and inc[i]=='Y'):
			a[i+1][i]='Y'
		else:
			a[i+1][i]='N'
	for i in range(3,n+1):
		for j in range(i-2,0,-1):
			if(a[i-1][j]=='Y' and a[i][j+1]=='Y'):
				a[i][j]='Y'
			else:
				a[i][j]='N'
	for i in range(n-2,0,-1):
		for j in range(i+2,n+1):
			if(a[i][j-1]=='Y' and a[i+1][j]=='Y'):
				a[i][j]='Y'
			else:
				a[i][j]='N'
	print("Case #{}:".format(k))
	for i in range(1,n+1):
		for j in range(1,n+1):
			print(a[i][j],end="")
		print()



