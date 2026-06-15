class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output=[]
        size= len(nums)
        total=1
        for i in range(size):
            newArray = nums
            popped_Element =newArray.pop(i)
            #math.prod() multiplies all elements in array together
            total = math.prod(newArray)
            print(total)
            output.insert(i, total)
            newArray.insert(i, popped_Element)
            
        
        return output