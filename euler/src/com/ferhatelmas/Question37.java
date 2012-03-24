package com.ferhatelmas;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/4/12
 * Time: 8:59 PM
 * To change this template use File | Settings | File Templates.
 */
public class Question37 {

    private static List<Integer> list = new ArrayList<Integer>();

    public static void main(String[] args) {

        int i=11, cnt = 0, sum = 0;

        while(true) {

            if(isTruncatable(i)) {
                list.add(i);
                cnt++;
                sum += i;
                if(cnt == 11) break;
            }
            i++;

        }

        System.out.println(sum);

    }
    
    private static boolean isTruncatable(int num) {
        
        if(!isPrime(num)) return false;
        
        String s = String.valueOf(num);
        
        for(int i=1; i<s.length(); i++) {

            if(!isPrime(Integer.parseInt(s.substring(i)))) return false;

        }

        for(int i=s.length()-1; i>0; i--) {

            if(!isPrime(Integer.parseInt(s.substring(0, i)))) return false;

        }

        return true;
        
    }

    private static boolean isPrime(int num) {

        if(num < 2) return false;

        for(int i=2; i<=Math.sqrt(num); i++) {

            if(num%i == 0) return false;

        }

        return true;

    }

}
