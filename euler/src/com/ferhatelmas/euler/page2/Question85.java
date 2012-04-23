package com.ferhatelmas.euler.page2;

public class Question85 {

    private static int target = 2000000;

    public static void main(String[] args) {

        int min = Integer.MAX_VALUE, area = -1;

        for(int i=2; i<101; i++) {
            for(int j=2; j<101; j++) {
                int diff = Math.abs(target - (((i * (i-1))/2) * ((j * (j-1))/2)));
                if(diff < min) {
                    min = diff;
                    area = (i-1) * (j-1);
                }
            }
        }
        System.out.println(area);
    }

}
