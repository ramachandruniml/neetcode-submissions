class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = Counter(nums)
        buckets = defaultdict(list)
        
        for num, freq in counts.items():
            buckets[freq].append(num)

        res=[]

        for freq in range(len(nums), 0, -1):
            if freq in buckets:
                for num in buckets[freq]:
                    res.append(num)

                if len(res)==k:
                    return res 
        return res

        
