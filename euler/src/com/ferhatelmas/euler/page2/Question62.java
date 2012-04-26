package com.ferhatelmas.euler.page2;

import java.util.HashMap;

public class Question62 {

    private static HashMap<String, Long[]> counter = new HashMap<String, Long[]>();

    public static void main(String[] args) {

        int start = 1;
        long val;
        while((val=isFive(start)) == -1) {
            start++;
        }
        System.out.println(val);
    }

    private static long isFive(long n) {

        long tmp = n*n*n;
        char[] c = String.valueOf(tmp).toCharArray();
        for(int i=0; i<c.length-1; i++) {
            for(int j=i+1; j<c.length; j++) {
                if(c[i] < c[j]) {
                    char ch = c[i];
                    c[i] = c[j];
                    c[j] = ch;
                }
            }
        }
        String key = new String(c);
        if(counter.containsKey(key)) {
            Long[] val = counter.get(key);
            if(val[1] == 4) return val[0];
            else val[1]++;
        } else {
            Long[] val = new Long[2];
            val[0] = tmp;
            val[1] = 1L;
            counter.put(key, val);
        }
        return -1;
    }
}
