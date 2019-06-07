a,b=[int(a)  for a in input().split()]
for i in range(a,b):
        s=0
        c=11
        while(i!=0):
                r=i%10
                s=s+r*r*r
                i=i//10
        if(c==s):
                print(c,end=' ')
        
