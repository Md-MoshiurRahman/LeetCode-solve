/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaproblems;

class Solution {
    public String longestPalindrome(String s) {
        int n = s.length();
        boolean table[][] = new boolean[n][n]; 
        
        int maxlength = 1;
        for(int i=0;i<n;i++)
        {
            table[i][i] = true;
        }
        
        int start = 0;
        for(int i=0;i<n-1;i++)
        {
            if(s.charAt(i)==s.charAt(i+1))
            {
                table[i][i+1] = true;
                maxlength = 2;
                start = i;
            }
        }
        
        for(int k =3;k<=n;k++)
        {
            for(int i=0;i<n-(k-1);i++)
            {
                int j = i + (k-1);
                if(s.charAt(i)==s.charAt(j) && table[i+1][j-1]==true)
                {
                    table[i][j] = true;
                    if(k>maxlength)
                    {
                        maxlength = k;
                        start = i;
                    }
                }
            }
        }
        
        
        return s.substring(start, start+maxlength);        
    }
}

public class LongestPalindromicSubstring {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.longestPalindrome("babad"));
    }
}
