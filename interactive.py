n=int(input())

j=2
ans="Yes"
cnt=0
for i in range(1,n):
    if j<=i:
        j=i+1
    while j<=n:
        print("?",i,j)
        ans=input()
        if ans=="No":
            break
        j+=1
    
    cnt+=j-i-1

print("!",cnt)