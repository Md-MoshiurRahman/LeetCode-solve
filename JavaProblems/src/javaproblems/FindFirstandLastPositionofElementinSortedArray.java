/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaproblems;

class Solution {

    public int[] searchRange(int[] nums, int target) {
        int res[]={-1,-1};
        res[0]=first(nums, target, nums.length);
        res[1]=last(nums, target, nums.length);
        return res;
    }

    int first(int nums[], int target, int n) {
        int low = 0, high = n - 1,res = -1;
        while (low <= high) {
            // Normal Binary Search Logic
            int mid = (low + high) / 2;
            if (nums[mid] > target) {
                high = mid - 1;
            } else if (nums[mid] < target) {
                low = mid + 1;
            } // If arr[mid] is same as 
            // x, we update res and 
            // move to the left half.
            else {
                res = mid;
                high = mid - 1;
            }
        }
        return res;
    }

    int last(int arr[], int x, int n) {
        int low = 0, high = n - 1,res = -1;
        while (low <= high) {
            // Normal Binary Search Logic
            int mid = (low + high) / 2;
            if (arr[mid] > x)
            {
                high = mid - 1;
            } 
            else if (arr[mid] < x)
            {
                low = mid + 1;
            } // If arr[mid] is same as x,
            // we update res and move to 
            // the right half.
            else {
                res = mid;
                low = mid + 1;
            }
        }
        return res;
    }
}

public class FindFirstandLastPositionofElementinSortedArray {

    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {5,7,7,8,8,10};
        int[] result = s.searchRange(nums, 6);
        for(int res: result)
        {
            System.out.print(res+" ");
        }
        
    }
}
