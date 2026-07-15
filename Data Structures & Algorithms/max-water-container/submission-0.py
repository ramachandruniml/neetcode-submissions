import random
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l=0 #pointer at starting index 0
        r=len(heights)-1 #second pointer at last index 
        res=0

        while l<r:
            #take min of the heights at both pointers and multiply by the index difference between then 
            area = min(heights[l], heights[r])*(r-l)
            #set result to whatever the max of either res or updated area is  
            res = max(res, area)
            
            
            if heights[l]<=heights[r]:
                # move first pointer to the right
                l+=1
            else:
                # move last pointer to the left 
                r-=1
        return res 