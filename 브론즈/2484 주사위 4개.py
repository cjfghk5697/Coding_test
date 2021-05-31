a=int(input(""))
count=[[0] * 6 for i in range(a)]
array = [[0] * 4 for i in range(a)]
total=[0 for i in range(a)]
result=[0 for i in range(a)]
for i in range(a):
    array[i]=list(map(int, input().split()))
    for z in range(0,4):
        count[i][(array[i][z])-1]+=1
for i in range(a):
    f=list(reversed(count[i]))
    h=f.index(max(f))
    if h==0:
        h=6
    elif h==1:
        h=5
    elif h==2:
        h=4
    result[i]=h*100
    for z in range(0,6):
        if count[i][z]==4:
            result[i] = 50000 + (z+1) * 5000  
        elif count[i][z]==3:
            result[i] = 10000 + (z+1) * 1000
        elif count[i][z]==2:
            result[i]=1000+(z+1)*100
            for k in range(0,6):
                if count[i][k]==2:
                    if k!=z:
                        result[i]=2000+(z+1)*500+500*(k+1)
                    
               
adda=max(result)
print(adda)
