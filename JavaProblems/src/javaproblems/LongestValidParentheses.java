/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaproblems;

import java.util.Stack;

class Solution {
    public int longestValidParentheses(String s) {
        int n = s.length();
        Stack<Integer> stk = new Stack<>();
        stk.push(-1);
        int result = 0;
        for (int i = 0; i < n; i++)
        {
            if (s.charAt(i) == '(')
            {
                stk.push(i);
            } 
            else
            {
                if (!stk.empty())
                {
                    stk.pop();
                }
                if (!stk.empty())
                {
                    result = Math.max(result, i - stk.peek());
                } 
                else
                {
                    stk.push(i);
                    System.out.println(stk.peek());
                }
            }
        }
        return result;
    }
}
public class LongestValidParentheses {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.longestValidParentheses("(()"));
        System.out.println(s.longestValidParentheses("()(()"));
    }
}
