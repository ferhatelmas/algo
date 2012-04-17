package com.ferhatelmas.euler.page3;

public class Question112 {

    public static void main(String[] args) {

        int bouncy = 0, i=1;

        while((double)bouncy/i < 0.99) {

            i++;
            if(isBouncy(i)) bouncy++;

        }
        System.out.println(i);
    }

    private static boolean isBouncy(int n) {

        String s = String.valueOf(n);

        boolean plus = false, minus = false;

        char c = s.charAt(0);
        for(int i=1; i<s.length(); i++) {

            char t = s.charAt(i);
            if(c-t < 0) minus = true;
            else if(c-t > 0) plus = true;

            c = t;
        }

        return plus && minus;

    }

}
