package com.ferhatelmas.euler.page2;

import java.util.ArrayList;
import java.util.List;

public class Question95 {

    private static int[] cache = new int[1000001];
    private static int maxCycle = 0;
    private static int minValue = -1;

    public static void main(String[] args) {

        fillCache();

        for(int i=1; i<cache.length; i++) {
            getCycle(i);
        }
        System.out.println(minValue);
    }

    private static void getCycle(int n) {

        List<Integer> list = new ArrayList<Integer>();

        while(!list.contains(n)) {
            list.add(n);
            n = cache[n];
            if(n >= cache.length) return;
        }

        int cnt = list.size()-list.indexOf(n);
        if(cnt > maxCycle) {
            maxCycle = cnt;
            minValue = getMin(list, list.indexOf(n));
        }
    }

    private static int getMin(List<Integer> list, int offset) {
        int min = Integer.MAX_VALUE;
        for(int i=offset; i<list.size(); i++) {
            if(list.get(i) < min) min = list.get(i);
        }
        return min;
    }

    private static void fillCache() {

        for(int i=1; i<= cache.length/2; i++) {
            for(int j=2*i; j<cache.length; j+=i) {
                cache[j] += i;
            }
        }

    }

}
