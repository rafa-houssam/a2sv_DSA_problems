k,n,w=input().split()

total_sum=0
for i in range(1,int(w)+1):
    total_sum+=int(k)*i
if total_sum>int(n):
    print(total_sum-int(n))         
else:    print(0)