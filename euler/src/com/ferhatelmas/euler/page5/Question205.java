package com.ferhatelmas.euler.page5;

import java.util.HashMap;

public class Question205 {

    private static double peterDem = Math.pow(4, 9);
    private static double colinDem = Math.pow(6, 6);

    private static HashMap<Integer, Integer> peter = new HashMap<Integer, Integer>();
    private static HashMap<Integer, Integer> colin = new HashMap<Integer, Integer>();

    public static void main(String[] args) {

        generatePeter(1, 0);
        generateColin(1, 0);

        double prob = 0;
        for(int c : colin.keySet()) {
            for(int p : peter.keySet()) {
                if(p > c) {
                    prob += (colin.get(c)/colinDem) * (peter.get(p)/peterDem);
                }
            }
        }
        System.out.format("%.7f", prob);
    }

    private static void generatePeter(int cnt, int sum) {

        if(cnt == 10) {
            if(peter.containsKey(sum)) {
                int tmp = peter.remove(sum);
                peter.put(sum, ++tmp);
            } else {
                peter.put(sum, 1);
            }
            return;
        }

        for(int i=1; i<5; i++) {
            generatePeter(cnt+1, sum+i);
        }

    }

    private static void generateColin(int cnt, int sum) {

        if(cnt == 7) {
            if(colin.containsKey(sum)) {
                int tmp = colin.remove(sum);
                colin.put(sum, ++tmp);
            } else {
                colin.put(sum, 1);
            }
            return;
        }

        for(int i=1; i<7; i++) {
            generateColin(cnt+1, sum+i);
        }

    }
}
