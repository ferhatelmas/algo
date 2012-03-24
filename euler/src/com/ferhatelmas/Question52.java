package com.ferhatelmas;

import java.util.Arrays;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/9/12
 * Time: 3:57 AM
 * To change this template use File | Settings | File Templates.
 */
public class Question52 {

    public static void main(String[] args) {
        
        int i = 1;
        
        while(!isPerm(i)) {
            i++;
        }

        System.out.println(i);
        
    }
    
    private static boolean isPerm(int n) {
        
        char[] ch = String.valueOf(n).toCharArray();
        Arrays.sort(ch);
        String x = new String(ch);
        
        ch = String.valueOf(2*n).toCharArray();
        Arrays.sort(ch);
        String x2 = new String(ch);
        
        if(!x.equals(x2)) return false;
        
        ch = String.valueOf(3*n).toCharArray();
        Arrays.sort(ch);
        String x3 = new String(ch);

        if(!x2.equals(x3)) return false;

        ch = String.valueOf(4*n).toCharArray();
        Arrays.sort(ch);
        String x4 = new String(ch);

        if(!x3.equals(x4)) return false;

        ch = String.valueOf(5*n).toCharArray();
        Arrays.sort(ch);
        String x5 = new String(ch);

        if(!x4.equals(x5)) return false;

        ch = String.valueOf(6*n).toCharArray();
        Arrays.sort(ch);
        String x6 = new String(ch);

        return x5.equals(x6);

    }
    
}
