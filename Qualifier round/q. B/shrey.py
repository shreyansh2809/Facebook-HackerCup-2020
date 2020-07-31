import sys
sys.stdin = open('alchemy_input.txt','r')
sys.stdout = open('output1.txt','w')

t=int(input())
for j in range(1,t+1):
	n=int(input())
	s=input()
	cnta=s.count('A')
	cntb=s.count('B')
	z=abs(cnta-cntb)
	out='N'
	if z==1:
		out='Y'
	print('Case #{}: {}'.format(j,out))
