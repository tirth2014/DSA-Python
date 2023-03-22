# NOTE:  Same frequency ma multiple numbers hoi sake chhe...keep it in mind

# Time Complexity: O(n log k)
# Space Complexity: O(n)

from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq  = Counter(nums)
        return [key for key,_ in freq.most_common(k)]
      

# Time Complexity:   O(n log n)
# Space Complexity: O(n)      
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_dt = {}
        res = []
        for num in nums:
            cnt_dt[num] = 1 if num not in cnt_dt else cnt_dt[num] + 1
        
        freq_lst = [(k,freq) for k,freq in cnt_dt.items()]   # List of (num,freq) tuples 
        freq_lst.sort(key = lambda x: x[1],reverse=True)

        i = 0
        while k > 0:
            res.append(freq_lst[i][0])
            i+=1
            k-=1
        return res
      
      
# Time: O(N + KlogN), where N <= 10^5 is length of nums array, K <= N.
#            => heapify(maxHeap) costs O(N)
#            => heappop(maxHeap) k times costs O(KlogN)
# Space: O(N)      
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_dt = {}
        res = []
        for num in nums:
            cnt_dt[num] = 1 if num not in cnt_dt else cnt_dt[num] + 1
        
        heap = [(-freq,k) for k,freq in cnt_dt.items()]
        heapq.heapify(heap)

        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k-=1
        
        return res
        
        
# Using Bucket Sort - O(N)
# Space: O(N)  
# Since the array nums has size of n, the frequency can be up to n.
# We can create bucket to store numbers by frequency.
# Then start bucketIdx = n, we can get the k numbers which have largest frequency.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt_dt = {}
        res = []
        n = len(nums)
        for num in nums:
            cnt_dt[num] = 1 if num not in cnt_dt else cnt_dt[num] + 1

        bucket = [[] for _ in range(n+1)]

        [bucket[freq].append(num) for num, freq in cnt_dt.items()]

        bucketIdx = n

        while not bucket[bucketIdx]:
            bucketIdx -= 1

        while k > 0:
            for num in bucket[bucketIdx]:
                res.append(num)
                k -= 1
            bucketIdx -= 1

        return res
      
# Bucket is a list of lists...it will store list of all numbers of frequency = freq at index freq.     


        
                  
        
        
        
        
                 
        
            
          
