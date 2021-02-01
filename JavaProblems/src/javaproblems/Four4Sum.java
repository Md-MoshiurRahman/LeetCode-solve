/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaproblems;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import javax.naming.spi.DirStateFactory;



class Solution {
    static class pair {
        int first, second;
        public pair(int first, int second)
        {
            this.first = first;
            this.second = second;
        }
    }
    
    public List<List<Integer>> fourSum(int[] nums, int target) {
        int n=nums.length;
        List<List<Integer>> result = new ArrayList<>();
        HashMap<Integer, List<pair>> mp = new HashMap<Integer, List<pair>>();
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if(mp.containsKey(nums[i] + nums[j]))
                {
                    List<pair> pairlist = new ArrayList<>();
                    pairlist = mp.get(nums[i] + nums[j]);
                    pairlist.add(new pair(i, j));
                    mp.put(nums[i] + nums[j], pairlist);
                }
                else
                {
                    List<pair> pairlist = new ArrayList<>();
                    pairlist.add(new pair(i, j));
                    mp.put(nums[i] + nums[j], pairlist);
                }
            }
        }
        
        for(int i=0; i<n-1; i++)
        {
            for(int j=i+1; j<n; j++)
            {
                int sum = nums[i] + nums[j];
                if(mp.containsKey(target - sum))
                {
                    List pairlist = mp.get(target - sum);
                    for(int k=0;k<pairlist.size();k++)
                    {
                        pair p =(pair) pairlist.get(k);
                        if(p.first!=i && p.first!=j && p.second!=i && p.second!=j)
                        {
                            List<Integer> value = new ArrayList<>();
                            value.add(nums[i]);
                            value.add(nums[j]);
                            value.add(nums[p.first]);
                            value.add(nums[p.second]);
                            Collections.sort(value);
                            if(!result.contains(value))
                            {
                                result.add(value);
                            }
                        }
                        
                    }
                }
            }
        }
            
                 
        
        return result;
    }
    
    
}
public class Four4Sum {
    public static void main(String[] args) {
        Solution s = new Solution();
        int [] nums = {1,0,-1,0,-2,2};
        System.out.println(s.fourSum(nums,0));
    }
}
