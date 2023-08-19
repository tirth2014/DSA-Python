"""
M-Coloring Problem
https://practice.geeksforgeeks.org/problems/m-coloring-problem-1587115620/1#

Given an undirected graph and an integer M. The task is to
determine if the graph can be colored with at most M colors such that
no two adjacent vertices of the graph are colored with the same color.
Here coloring of a graph means the assignment of colors to all vertices.
Print 1 if it is possible to colour vertices and 0 otherwise.

Your Task:
Your task is to complete the function graphColoring() which takes the 2d-array graph[], the number of colours and the number of nodes as inputs and returns true if answer exists otherwise false. 1 is printed if the returned value is true, 0 otherwise. The printing is done by the driver's code.
Note: In Example there are Edges not the graph.Graph will be like, if there is an edge between vertex X and vertex Y graph[] will contain 1 at graph[X-1][Y-1], else 0. In 2d-array graph[ ], nodes are 0-based indexed, i.e. from 0 to N-1.Function will be contain 2-D graph not the edges.

Ex:
graph =
[[0, 1, 1, 1],
[1, 0, 1, 0],
[1, 1, 0, 1],
[1, 0, 1, 0]]
k=3 V=4
Output: 1 (Means True It's possible to color this graph with 3 colors)

GFG Input for above ex:
4
3
5
1 2 2 3 3 4 4 1 1 3

Expected Time Complexity: O(M^N).
Expected Auxiliary Space: O(N).

Constraints:
1 ≤ N ≤ 20
1 ≤ E ≤ (N*(N-1))/2
1 ≤ M ≤ N

"""

if __name__ == '__main__':

    def graphColoring(graph, k, V):

        assigned_colors = [-1] * V

        # Check if any adjacent vertex in graph has same color 
        def same_adj_vertex_color(ind_v, color):
            for ind_g in range(len(graph[0])):
                # vertex ind_v and ind_g are adjacent if they have an edge between them
                if graph[ind_v][ind_g] == 1:
                    if assigned_colors[ind_g] == color:
                        return True
            return False

        def dfs(ind_v=0):
            # Colors assigned to all graph vertices
            if ind_v == V:
                return True # MISSION SUCCESSFUL

            for color in range(k):
                if not same_adj_vertex_color(ind_v, color):
                    assigned_colors[ind_v] = color                  
                    if dfs(ind_v + 1):
                        return True   # No need to explore further if all the graph vertices have been successfully assigned colors [ MISSION SUCCESSFUL ]
                    assigned_colors[ind_v] = -1  # backtrack
            return False

        return dfs()
#{ 
  # Driver Code Starts
  #Initial Template for Python 3
    V = int(input("V: "))
    k = int(input("k: "))
    m = int(input("m: "))
    list = [int(x) for x in input().strip().split()]
    graph = [[0 for i in range(V)] for j in range(V)]
    cnt = 0
    for i in range(m):
        graph[list[cnt] - 1][list[cnt + 1] - 1] = 1
        graph[list[cnt + 1] - 1][list[cnt] - 1] = 1
        cnt += 2
    if (graphColoring(graph, k, V) == True):
        print(1)
    else:
        print(0)
# } Driver Code Ends      
