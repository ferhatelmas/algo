package com.ferhatelmas.euler.page2;

import java.util.ArrayList;
import java.util.HashMap;

public class Question61 {

    private static HashMap<Integer, ArrayList<Integer>> cache = new HashMap<Integer, ArrayList<Integer>>();

    public static void main(String[] args) {

        fillCache();
        System.out.println(getOrderedList(new ArrayList<Integer>(), new ArrayList<Integer>()));
    }

    private static int getOrderedList(ArrayList<Integer> res, ArrayList<Integer> usedLists) {

        if(usedLists.size() == 6) {
            if(isEqualEnd(res.get(res.size()-1), res.get(0))) {
                int sum = 0;
                for(int i : res) sum += i;
                return sum;
            } else {
                return -1;
            }
        }

        for(int i=5; i>=0; i--) {
            if(usedLists.contains(i)) continue;
            for(int j : cache.get(i)) {
                if(usedLists.size() != 0 && !isEqualEnd(res.get(res.size()-1), j)) continue;
                res.add(j);
                usedLists.add(i);
                int sum = getOrderedList(res, usedLists);
                if(sum != -1) return sum;
                usedLists.remove(usedLists.size()-1);
                res.remove(res.size()-1);
            }
        }
        return -1;
    }

    private static boolean isEqualEnd(int a, int b) {
        return String.valueOf(a).substring(2).equals(String.valueOf(b).substring(0, 2));
    }

    private static void fillCache() {

        ArrayList<Integer> triangle   = new ArrayList<Integer>();
        ArrayList<Integer> square     = new ArrayList<Integer>();
        ArrayList<Integer> pentagonal = new ArrayList<Integer>();
        ArrayList<Integer> hexagonal  = new ArrayList<Integer>();
        ArrayList<Integer> heptagonal = new ArrayList<Integer>();
        ArrayList<Integer> octagonal  = new ArrayList<Integer>();

        int tmp;
        for(int i=1; i<150; i++) {
            tmp = (i*(i+1))/2;
            if(tmp>=1000 && tmp<10000) triangle.add(tmp);
            tmp = i*i;
            if(tmp>=1000 && tmp<10000) square.add(tmp);
            tmp = (i*(3*i-1))/2;
            if(tmp>=1000 && tmp<10000) pentagonal.add(tmp);
            tmp = i*(2*i-1);
            if(tmp>=1000 && tmp<10000) hexagonal.add(tmp);
            tmp = (i*(5*i-3))/2;
            if(tmp>=1000 && tmp<10000) heptagonal.add(tmp);
            tmp = i*(3*i-2);
            if(tmp>=1000 && tmp<10000) octagonal.add(tmp);
        }
        cache.put(0, triangle);
        cache.put(1, square);
        cache.put(2, pentagonal);
        cache.put(3, hexagonal);
        cache.put(4, heptagonal);
        cache.put(5, octagonal);
    }



}
