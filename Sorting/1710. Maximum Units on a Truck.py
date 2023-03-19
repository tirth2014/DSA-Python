# Greedy Algorithm
# Time Complexity = O(n log n)
# Space Complexity = O(n) as py3 uses tim sort
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes,key=lambda x: x[1],reverse=True)
        max_units = 0
        i = 0
#         Greedily take as many boxes as we want from available boxes of particular type till truckSize becomes zero or till there are no boxes left.
        while truckSize > 0 and i<len(boxTypes):
            arri = boxTypes[i]
            selected_boxes = min(arri[0],truckSize)
            max_units += selected_boxes*arri[1]
            truckSize -= selected_boxes
            i+=1
        return max_units

    
"""
Time complexity is O(n log n), where n is the length of the boxTypes list. 
The heapify operation takes O(n) time and each heappop operation takes O(log n) time. 
The while loop will run at most n times, since we remove one box type from the heap in each iteration, so the overall time complexity is O(n log n).

Space complexity is O(n)

Approach:-
Negate the values of the second element of each box type when adding them to the heap, 
so that the smallest value of the negated second elements will correspond to the box type with the largest second element. 
Then, when you remove and return the box types from the heap using heapq.heappop, you can negate the second element again to get the correct value.
"""
import heapq

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        heap = [(-boxes[1], boxes[0]) for boxes in boxTypes]
        heapq.heapify(heap)
        max_units = 0
        while truckSize > 0 and heap:
            boxes = heapq.heappop(heap)
            boxes = (-boxes[0], boxes[1])
            selected_boxes = min(truckSize, boxes[1])
            max_units += selected_boxes * boxes[0]
            truckSize -= selected_boxes
        return max_units    
