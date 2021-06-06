def dfs(V):
    count[V]=1
    print(V, end=' ')
    for i in range(1,N+1):
        if count[i]==0 and node[V][i]==1:
            dfs(i)
def bfs(V):
    count[V]=1
    count2=[V]
    while count2:
        V=count2.pop(0)
        print(V, end=' ')
        for i in range(1, N+1):
            if count[i]==0 and node[V][i]==1:
               count2.append(i)
               count[i]=1







N,M,V= map(int,input().split())
count=[0]*(N+1)
node=[[0]*(N+1) for i in range(N+1)]

for i in range(M):
    first,second=map(int,input().split())
    node[first][second]=1
    node[second][first]=1
dfs(V)
print()
count = [0] * (N + 1)
bfs(V)
            
    

