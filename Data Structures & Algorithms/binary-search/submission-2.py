class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            # Prevents potential integer overflow
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1  # Target is in the left half
            else:
                start = mid + 1  # Target is in the right half

        return -1