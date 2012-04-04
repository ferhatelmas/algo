package com.ferhatelmas.euler;

public class Question14 {

    public static void main(String[] args) {

        int max = 0, cnt;
        long val, maxVal = 0;

        for(int i=2; i<1000000; i++) {

            cnt = 1;
            val = i;

            while(val>1) {

                if(val%2==0) val /= 2;
                else val = 3*val+1;
                cnt++;

            }

            if(cnt > max) {
                max = cnt;
                maxVal = i;
            }

            //System.out.println("Number: " + i + " --> " + cnt);

        }

        System.out.println("RESULT");
        System.out.println(max);
        System.out.println(maxVal);

    }

}
