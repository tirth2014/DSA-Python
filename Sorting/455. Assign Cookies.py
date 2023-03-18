# BRUTE FORCE
# time complexity: O(n^2)
# space complexity: O(1)  

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt,biscuit = 0,0
        for i in range(len(g)):
            given = False
            for j in range(biscuit,len(s)):
                if s[j] >= g[i]:
                    cnt+=1
                    biscuit = j+1  # Here I was doing mistake by biscuit += 1 means given biscuits were also getting repeated for other children.
                    given = True
                    break
            if not given:
                break
                # So that children vadhare hoy ane biscuit khuti gya hoy ya to size occhi hoy to pn outer loop continuously gumya na kare.
        return cnt
      
      
# Time Complexity = O(NlogN + MlogM) where N = |g| and M = |s|      
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        ichild = 0
        icookie = 0

        while ichild < len(g) and icookie < len(s):
            if s[icookie] >= g[ichild]:
                icookie += 1
                ichild+=1
                continue
            icookie+=1
        
        return ichild      
      
      
# Using priority queue (heapq)
# T.C:  O(nlogn + mlogm)
# S.C:  O(1)
import heapq
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        heapq.heapify(g)
        heapq.heapify(s)

        cnt = 0
        while g and s:
            if s[0] >= g[0]:
                heapq.heappop(s)
                heapq.heappop(g)
                cnt += 1
            else:
                heapq.heappop(s)

        return cnt
