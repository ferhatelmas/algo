package com.ferhatelmas.euler.page1;

import java.util.ArrayList;

public class Question23 {

    public static void main(String[] args) {

        ArrayList<Integer> list = new ArrayList<Integer>();

        for(int i=1; i<28124; i++) {

            int div = 0;

            for(int j=1; j<i; j++){

                if(i%j == 0) div += j;

            }

            if(div > i) list.add(i);

        }

        long sum = 0;
        for(int i=1; i<28124; i++) {

            boolean flag = false;

            for(int j : list) {

                if(list.contains(i-j)) flag = true;

            }

            if(!flag) sum += i;

        }

        System.out.println(sum);

    }

}
