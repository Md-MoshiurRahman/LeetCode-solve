/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaproblems;

class Solution {
    public int divide(int dividend, int divisorI) {
        int signDs = getSign(divisorI);
        int signDd = getSign(dividend);
        double divisor = (double)divisorI * signDs;
        
        double q = 0;
        double rem = 0;
        char[] chars = String.valueOf(dividend).toCharArray();
        for(char c : chars){
            if(c=='-'){
                continue;
            }
            rem = rem * 10 + (c - '0');
            int tempQ = 0;
            while(rem>=divisor){
                tempQ++;
                rem-=divisor;
            }
            q=q*10 + tempQ;
        }
        if(q*signDs*signDd > Integer.MAX_VALUE){
            return Integer.MAX_VALUE;
        }
        return (int)(q*signDs*signDd);
    }
    
    private int getSign(int num){
        if(num<0){
            return -1;
        }
        return 1;
    }
}
public class DivideTwoIntegers {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.divide(-2147483648,1));
    }
}

