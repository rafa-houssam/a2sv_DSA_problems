from math import floor


t=int(input())


for i in range(t):
    n=int(input())
    if(n==1 or n==2):
        print(0)
    else:

        if(n%2==0):
            print(int(n/2-1))
        else:
            print(int(floor(n/2)))
