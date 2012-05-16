package com.ferhatelmas.euler.page3;

import java.util.*;

public class Question124 {

    public static void main(String[] args) {

        Map<Integer, Integer> rads = new HashMap<Integer, Integer>();
        for(int i=1; i<=100000; i++) {
            rads.put(i, getRad(i));
        }

        SortedSet<Map.Entry<Integer, Integer>> sortedRads = entriesSortedByValues(rads);
        int i=0;
        for(Map.Entry<Integer, Integer> rad : sortedRads) {
            i++;

            if(i == 10000) {
                System.out.println(rad.getKey());
                break;
            }
        }
    }

    static int getRad(int n) {

        int mul = 1;
        for(int i=2; i<=n; i++) {
            if(n%i == 0) {
                mul *= i;
                n /= i;
                while(n%i == 0) {
                    n /= i;
                }
            }
        }

        return mul;
    }

    static <K,V extends Comparable<? super V>> SortedSet<Map.Entry<K,V>> entriesSortedByValues(Map<K,V> map) {
        SortedSet<Map.Entry<K,V>> sortedEntries = new TreeSet<Map.Entry<K,V>>(
                new Comparator<Map.Entry<K,V>>() {
                    @Override
                    public int compare(Map.Entry<K,V> e1, Map.Entry<K,V> e2) {
                        int res = e1.getValue().compareTo(e2.getValue());
                        return res != 0 ? res : 1; // Special fix to preserve items with equal values
                    }
                }
        );
        sortedEntries.addAll(map.entrySet());
        return sortedEntries;
    }

}
