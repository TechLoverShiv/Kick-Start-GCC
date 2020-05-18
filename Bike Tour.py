for i in range(int(input())): 
    m=int(input(""))
    l=list(map(int,input().split()))
    count=0  
    for j in range(1,m-1):
        if (l[j]>l[j-1] and l[j]>l[j+1]):
            count +=1
    print("Case #%d: %d" %(i+1,count))
