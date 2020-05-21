for i in range(int(input())):
    n=list(map(int,input().split()))
    if(n[0]<n[1]):
        print("Case #"+str(i+1)+": 0")
    else:    
        l=list(map(int,input().split()))
        j,count,c=0,0,0
        for r in range(n[0]):
            if(l[r])==(n[1]-j):
                count+=1
                j+=1
            if(count==n[1]):
                c+=1
                count,j=0,0
        print("Case #"+str(i+1)+": "+str(c))
