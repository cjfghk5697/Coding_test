from bisect import bisect_left 

k=0
n=int(input())
array=list(map(int,input().split()))
left_index=bisect_left(array,-1)


for i in range(left_index,n):
    if i==array[i]:
        print(i)
        k=1

if k==0:
    print(-1)
        
