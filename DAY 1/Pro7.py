a,b,c,d = map(int,input().split())
if a-c < b-d:
    print("First")
elif a-c > b-d:
    print("Second")
else:
    print("Any")
