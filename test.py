print "Hello"
import random
from fractions import gcd
from sets import Set

def brent(N):
    if N%2==0:
        return 2
    y,c,m = random.randint(1, N-1),random.randint(1, N-1),random.randint(1, N-1)
    g,r,q = 1,1,1
    while g==1:             
        x = y
        for i in range(r):
            y = ((y*y)%N+c)%N
        k = 0
        while (k<r and g==1):
            ys = y
            for i in range(min(m,r-k)):
                    y = ((y*y)%N+c)%N
                    q = q*(abs(x-y))%N
            g = gcd(q,N)
            k = k + m
        r = r*2
    if g==N:
        while True:
            ys = ((ys*ys)%N+c)%N
            g = gcd(abs(x-ys),N)
            if g>1:
                break   
    return g

inputs = [15, 21, 24, 30, 49]
outputs = {}

for n in inputs:
    my_num = n
    my_factors = Set()
    while True:
        if my_num != 1:
            f = brent(my_num)
            print str(n) + " " + str(f)
            my_factors.add(f)
            my_num = my_num / f
            outputs.setdefault(f,Set()).add(n)
        else:
            break
print outputs        
for i in outputs.keys():
    print str(i) + " " + str(sum(outputs[i]))
    
    
print "This code has bugs!"
        