package com.ferhatelmas;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class Question35 {

    private static List<Integer> work = new ArrayList<Integer>();
    private static HashSet<Integer> grand = new HashSet<Integer>();

    public static void main(String[] args) {

        for(int i=2; i<1000000; i++) {

            work.clear();
            perm(String.valueOf(i));
            boolean flag = true;
            for(int p : work) {

                if(!isPrime(p)) {
                    flag = false;
                    break;
                }

            }

            if(flag) {

                for(int p : work) grand.add(p);

            }

        }

        for(int p : grand) System.out.println(p);

        System.out.println();
        System.out.println(grand.size());
    }

    private static boolean isPrime(int num) {


        for(int i=2; i<=Math.sqrt(num); i++) {
            
            if(num%i == 0) return false;
            
        }
        
        return true;

    }


    public  static void perm(String s) { 
        
        work.add(Integer.parseInt(s));
        for(int i=1; i<s.length(); i++) {
            work.add(Integer.parseInt(s.substring(i).concat(s.substring(0, i))));
        }
    
    }

}
