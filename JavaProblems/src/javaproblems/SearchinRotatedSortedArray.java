/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaproblems;

class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        int pivot = findPivot(nums, 0, n-1);  
        if (pivot == -1)
        {
            return binarySearch(nums, 0, n - 1, target); 
        }
        
        if (nums[pivot] == target)
        {
            return pivot;
        }
             
        if (nums[0] <= target)
        {
            return binarySearch(nums, 0, pivot - 1, target);
        }
             
        return binarySearch(nums, pivot + 1, n - 1, target);
    }
    
    int findPivot(int arr[], int low, int high) 
    { 
        // base cases 
        if (high < low) 
            return -1; 
        if (high == low) 
            return low; 
  
        /* low + (high - low)/2; */
        int mid = (low + high) / 2; 
        if (mid < high && arr[mid] > arr[mid + 1]) 
            return mid; 
        if (mid > low && arr[mid] < arr[mid - 1]) 
            return (mid - 1); 
        if (arr[low] >= arr[mid]) 
            return findPivot(arr, low, mid - 1); 
        return findPivot(arr, mid + 1, high); 
    }
    
    int binarySearch(int arr[], int low, int high, int key) 
    { 
        if (high < low) 
            return -1; 
  
        /* low + (high - low)/2; */
        int mid = (low + high) / 2; 
        if (key == arr[mid]) 
            return mid; 
        if (key > arr[mid]) 
            return binarySearch(arr, (mid + 1), high, key); 
        return binarySearch(arr, low, (mid - 1), key); 
    }
}

public class SearchinRotatedSortedArray {
    public static void main(String[] args) {
        Solution s = new Solution();
        int[] nums = {4,5,6,7,0,1,2};
        System.out.println(s.search(nums,0));
    }
}
