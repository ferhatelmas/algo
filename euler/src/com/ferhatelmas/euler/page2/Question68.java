package com.ferhatelmas.euler.page2;

import java.util.HashSet;

public class Question68 {

    private static long max;

    public static void main(String[] args) {

        HashSet<Integer> set = new HashSet<Integer>();
        for(int i=1; i<=10; i++) set.add(i);

        getMaxGon(new int[10], set, 0);
        System.out.println(max);
    }

    private static void getMaxGon(int[] result, HashSet<Integer> set, int offset) {

        if(offset == 10) if(isCorrect(result)) setMax(result);

        for(int i=1; i<=10; i++) {
            if(set.contains(i)) {
                result[offset] = i;
                set.remove(i);
                getMaxGon(result, set, offset + 1);
                set.add(i);
            }
        }

    }

    private static boolean isCorrect(int[] result) {

        // otherwise we have a string of 17
        if(result[1] == 10 ||
           result[2] == 10 ||
           result[4] == 10 ||
           result[6] == 10 ||
           result[8] == 10) return false;

        // solution constraint
        if(result[0] > result[3] ||
           result[0] > result[5] ||
           result[0] > result[7] ||
           result[0] > result[9]) return false;

        // sum constraint
        int t = result[0] + result[1] + result[2];
        for(int i=2; i<10; i+=2) {
            if(i != 8 && t != result[i] + result[i+1] + result[i+2]) return false;
            else if(i == 8 && t != result[i] + result[i+1] + result[1]) return false;
        }

        return true;
    }

    private static void setMax(int[] result) {

        StringBuilder sb = new StringBuilder();
        sb.append(result[0]);
        sb.append(result[1]);
        sb.append(result[2]);
        sb.append(result[3]);
        sb.append(result[2]);
        sb.append(result[4]);
        sb.append(result[5]);
        sb.append(result[4]);
        sb.append(result[6]);
        sb.append(result[7]);
        sb.append(result[6]);
        sb.append(result[8]);
        sb.append(result[9]);
        sb.append(result[8]);
        sb.append(result[1]);

        //for(int i : result) sb.append(i);
        long tmp = Long.parseLong(sb.toString());
        if(tmp > max) max = tmp;

    }

}
