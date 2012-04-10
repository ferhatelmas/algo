package com.ferhatelmas.euler.page6;

import java.util.HashSet;

public class Question265 {

    private static int N = 5;
    
    private static HashSet<String> circles = new HashSet<String>();
    private static HashSet<String> current = new HashSet<String>();

    public static void main(String[] args) {
        String prefix = "";
        for(int i=0; i<N; i++) prefix += "0";
        generateCircles("");
        long sum = 0;
        for(String s : circles) {
            if(s.startsWith(prefix))
                sum += getNumber(s);
        }
        System.out.println(sum);
    }

    private static long getNumber(String s) {
        long l = 0;
        for(byte b: s.getBytes()) l = (l << 1) | (b & 1);
        return l;
    }
    
    private static void generateCircles(String s) {
        
        int len = s.length();
        if(len > N) {
            current.clear();
            for(int i=0; i<=len-N; i++) {
                String ss = s.substring(i, i+N);
                if(current.contains(ss)) return;
                else current.add(ss);
            }
            if(len == (1<<N)) {
                for(int i=1; i<N; i++) {
                    String ss = s.substring(len-N+i) + s.substring(0, i);
                    if(current.contains(ss)) return;
                    else current.add(ss);
                }
                circles.add(s);
                return;
            }
        }
        
        generateCircles(s + "0");
        generateCircles(s + "1");
        
    }

}
