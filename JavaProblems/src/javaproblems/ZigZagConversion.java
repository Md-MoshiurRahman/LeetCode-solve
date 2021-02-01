/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaproblems;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public String convert(String s, int numRows) {
        if(numRows==1 || s.length()<= numRows)
        {
            return s;
        }
        
        List<StringBuilder> rows = new ArrayList<>();
        for (int i = 0; i < numRows; i++)
            rows.add(new StringBuilder());
        int direction = 1;
        int i = 0;
        for(char c : s.toCharArray())
        {
            
            rows.get(i).append(c);
            i += direction;
            if(i == numRows-1 || i==0)
            {
                direction *= -1;
            }
        }
        
        StringBuilder ret = new StringBuilder();
        for (StringBuilder row : rows)
        {
            ret.append(row);
        }
        return ret.toString();
    }
}
public class ZigZagConversion {
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(s.convert("PAYPALISHIRING",3));
    }
}
