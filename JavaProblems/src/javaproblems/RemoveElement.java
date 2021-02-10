/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaproblems;

class Solution {
    public int removeElement(int[] nums, int val) {
        int back=0, front=0;
        while(front<nums.length)
        {
            if(nums[front]==val)
            {
               front++;
            }
            else
            {
                nums[back]=nums[front];
                back++;
                front++;
            }
        }
        return back;
    }
}

public class RemoveElement {
    public static void main(String[] args) {
        Solution s = new Solution();
        int [] nums = {0,1,2,2,3,0,4,2};
        System.out.println(s.removeElement(nums,2));
    }
}
