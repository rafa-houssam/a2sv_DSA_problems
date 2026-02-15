import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # Replace the logic below with the correct one for your problem
    maximum = max(a)
    distinct = len(set(a))
    print(maximum + distinct - 1)
