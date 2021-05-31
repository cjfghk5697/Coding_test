total=[]

a= int(input())
weight=[[0] * 2 for i in range(a)]
tall=[[0] * 2 for i in range(a)]
rank=[]
for s in range(a):
    weight[s],tall[s] = list(map(int, input().split()))
    
for i in range(a):
    z=1
    for j in range(a):
        if weight[i]<weight[j] and tall[i]<tall[j]:
            z+=1
    rank.append(z)
for i in rank:
    print(i,end=' ')
