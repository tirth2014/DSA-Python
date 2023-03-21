class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score,reverse=True)
        n = len(score)
        res = [""]*n

        for i in range(n):
            if score[i] == sorted_score[0]:
                res[i] = "Gold Medal"

            elif score[i] == sorted_score[1]:
                res[i] = "Silver Medal"

            elif score[i] == sorted_score[2]:
                res[i] = "Bronze Medal"

            else:
                res[i] = str(sorted_score.index(score[i]) + 1)
        
        return res
      
      
      
# Use a dictionary which maps scores to ranks
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score)[::-1]
        medals = ["Gold Medal","Silver Medal","Bronze Medal"] + list(map(str, range(4,len(score)+1)))
        # list(map(str, range(4,len(score)+1))) = [str(i) for i in range(4,len(score))]

        mapped_dt = dict(zip(sorted_score,medals))

        return [mapped_dt[sc] for sc in score]
      

# 2-liner
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dt = {n:i>2 and str(i+1) or ["Gold","Silver","Bronze"][i]+" Medal" for i,n in enumerate(sorted(score)[::-1])}
        
        return [dt[num] for num in score]
        
        
