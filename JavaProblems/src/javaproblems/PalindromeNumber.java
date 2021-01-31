/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaproblems;

class Solution {
    public boolean isPalindrome(int x) {
        if(x<0)
        {
           return false; 
        }
        
        int y = x;
        int z = 0;
        while(y!=0)
        {
            int temp = y%10;
            y /= 10;
            z = z*10 + temp;
        }
        return x==z;
        
    }
}

public class PalindromeNumber {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.isPalindrome(-121));
        
    }
}
