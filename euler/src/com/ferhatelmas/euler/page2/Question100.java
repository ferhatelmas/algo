package com.ferhatelmas.euler.page2;

public class Question100 {

    private static long limit = 1000000000000L;

    public static void main(String[] args) {

        long total = 120, blue = 85, tmp;

        while(total < limit) {

            tmp = 3*blue + 2*total - 2;
            total = 4*blue + 3*total -3;
            blue = tmp;

        }
        System.out.println(blue);
    }
}
