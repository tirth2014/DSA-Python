# Time Complexity = O(n log n)
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes,key=lambda x: x[1],reverse=True)
        max_units = 0
        i = 0
        while truckSize > 0 and i<len(boxTypes):
            arri = boxTypes[i]
            selected_boxes = min(arri[0],truckSize)
            max_units += selected_boxes*arri[1]
            truckSize -= selected_boxes
            i+=1
        return max_units
