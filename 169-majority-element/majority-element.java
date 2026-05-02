class Solution {
    public int majorityElement(int[] nums) 
    {
        int candidate = nums[0];
        int count = 0; 

        for (int i = 0; i < nums.length; i++)
        {
            if (count == 0)
            {
                System.out.println('e');
                candidate = nums[i];
            }

            if (nums[i] == candidate)
            {
                count++;
            }

            else
            {
                count--;
            }

        }

        return candidate;
    }
}