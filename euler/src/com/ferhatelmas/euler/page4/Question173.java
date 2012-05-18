package com.ferhatelmas.euler.page4;

public class Question173 {

    public static void main(String[] args) {

        int minLimit = 3, maxLimit = 1000000,
                p = maxLimit/4+1, cnt = p-2;

        for(int i=5; i<=p; i++) {
            int total = (i-1)*4, j = i-2, w = total-8;
            while(j >= minLimit && total + w <= maxLimit) {
                cnt++;
                total += w;
                j -= 2;
                w -= 8;
            }
        }
        System.out.println(cnt);
    }

}
