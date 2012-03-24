package com.ferhatelmas;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/4/12
 * Time: 7:04 PM
 * To change this template use File | Settings | File Templates.
 */
public class Question33 {


    public static void main(String[] args) {

        List<Integer> list = new ArrayList<Integer>();

        for(int i=10; i<100; i++) {
            
            for(int j=i+1; j<100; j++) {
                
                double d = ((double)i)/j;
                
                if(isSame(i, j, d)) {
                    
                    list.add(i);
                    list.add(j);
                    System.out.println("i: " + i + " j: " + j);
                }
                
            }
            
        }

        int j=0, num = 1, dem = 1;
        
        for(int i : list) {
            
            if(j%2 == 0) num *= i;
            else dem *= i;
            
        }

        System.out.println((float)num/dem);
        
    }
    
    private static boolean isSame(int i, int j, double d) {
        
        String si = String.valueOf(i);
        String sj = String.valueOf(j);

        if(si.charAt(0) != sj.charAt(1) && si.charAt(1) != sj.charAt(0)) return false;
        else if(si.charAt(0) == sj.charAt(1)) {
            if(Double.parseDouble(si.substring(1))/Double.parseDouble(sj.substring(0, 1)) == d) return true;
            else return false;
        } else {
            if(Double.parseDouble(si.substring(0, 1))/Double.parseDouble(sj.substring(1)) == d) return true;
            else return false;
        }
    }
                                  
}
