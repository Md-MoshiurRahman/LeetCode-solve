/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaproblems;

class Solution {
    public int strStr(String haystack, String needle) {
        if(needle.equals(""))
        {
            return 0;
        }
        int index = haystack.indexOf(needle);
        return index;
    }
}

public class ImplementstrStr {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.strStr("hello","ll"));
    }
}
