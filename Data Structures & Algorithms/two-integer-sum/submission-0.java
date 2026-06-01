class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        int finalI=0;
        int finalJ=0;

        for(int i=0;i<nums.length;i++){
            for(int j=0;j<nums.length;j++){
                if(i!=j){
                    if(nums[i]+nums[j]==target){
                        finalI=i;
                        finalJ=j;
                    }
                }
            }
        }
        int[] finalOutput = {finalJ, finalI};

        return finalOutput;
    }
}
