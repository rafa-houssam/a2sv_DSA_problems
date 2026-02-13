n=int(input())
data={}
for _ in range(n):
    name,phone=input().split(" ")
    data[name]=phone
while(True):
    try:
        
        name=input()
        if (name==""):
            break
        print(f"{name}="+data[name] if name in data.keys() else "Not found ")
    except EOFError:
        break
