class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        tortoise, hare = 0,0
        check = 0
        
        # tortoise and hare meets somewhere in the cycle! (not necessarily at start of cycle)
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            
            if tortoise == hare:
                break
                
        # return nums[tortoise]  (If we don't use the below loop then it'll fail because the above code will give ANY node in the cylce and below code is necessary to find the start node of a cycle
        # for example it fails for the testcase:   [2,5,9,6,9,3,8,9,7,1]    output = 8,  expected: 9
        
        # To find the start node of the cycle
        while True:
            tortoise = nums[tortoise]
            check = nums[check]

            if tortoise == check:
                break
                
        return check
