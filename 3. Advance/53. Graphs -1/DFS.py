def path(n,e,u,v,source,dest):
    g = [[] for i in range n]
    visited = [False] *(n+1)
    dfs(source,g,visited)
    return visited[dest]

def dfs(s,g,v):
    if v[s] ==True:
        return
    
    v[s] = True
    for i in range(len(g[s])):
        vi = g[s][i]
        if v[vi] == False:
            dfs(vi,g[s],v)