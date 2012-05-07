package com.ferhatelmas.euler.page2;

public class Question91 {

    public static void main(String[] args) {

        int limit = 50, cnt = 0;

        for(int i=0; i<=limit; i++) {
            for(int j=0; j<=limit; j++) {
                for(int k=0; k<=limit; k++) {
                    for(int m=0; m<=limit; m++) {

                        if(!(i == k && j == m) && !(i == 0 && j == 0) && !(k == 0 && m == 0)) {
                            double d1 = Math.sqrt(i*i + j*j);
                            double d2 = Math.sqrt(k*k + m*m);
                            double d3 = Math.sqrt((i-k)*(i-k) + (j-m)*(j-m));

                            double max = Math.max(d1, Math.max(d2, d3));
                            double min1, min2;

                            if(d1 < max) {
                                min1 = d1;
                                min2 = Math.min(d2, d3);
                            } else {
                                min1 = d2;
                                min2 = d3;
                            }

                            if(Math.abs(max - Math.sqrt(min1*min1 + min2*min2)) < 0.0001) cnt++;
                        }
                    }
                }
            }
        }

        System.out.println(cnt/2);

    }

}
