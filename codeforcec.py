

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    total = sum(a)
    
   
    if total % n != 0:
        print(-1)
        continue
    
    x = total // n
    k = sum(1 for ai in a if ai > x)
    print(k)
