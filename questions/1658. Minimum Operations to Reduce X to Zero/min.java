class Solution {
    public int minOperations(int[] nums, int x) {
        int target = -x, sum = 0, res = Integer.MIN_VALUE;
        for(int i: nums) target+=i;
        if(target == 0) return nums.length;
        HashMap<Integer, Integer> map = new HashMap();
        map.put(0, -1);
        for(int i = 0; i < nums.length; i++){
            sum += nums[i];
            if(map.containsKey(sum - target)){
                res = Math.max(res, i - map.get(sum - target));
            }
            map.put(sum, i);
        }
        return res == Integer.MIN_VALUE?-1:nums.length - res;
    }
}
