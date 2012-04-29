package com.ferhatelmas.euler.page3;

import java.util.ArrayList;

public class Question122 {

    public static void main(String[] args) {
        int sum = 0;
        for(int i=19; i<=19; i++) {
            sum += getMin(i);
        }
        System.out.println(sum);
    }

    private static int getMin(int n) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        list.add(1);

        if(isEqual(list,n) == 0) return 0;

        while(true) {

            int len = list.size();
            for(int i=len-1; i>=0; i--) {
                for(int j=i; j>=0; j--) {
                    list.add(i+j);
                    int r = isEqual(list, n);
                    if(r != -1) return len+r;
                    list.remove(len);
                }
            }


            list.add(2*list.get(len-1));
        }
    }

    private static int isEqual(ArrayList<Integer> list, int n) {
        int len = list.size();
        for(int i=len-1; i>=0; i--) {
            for(int j=i; j>=0; j--) {
                if(list.get(i)+list.get(j) == n) {
                    if(i==j) return 1;
                    else return 0;
                }
            }
        }
        return -1;
    }

}
