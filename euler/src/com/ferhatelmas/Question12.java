package com.ferhatelmas;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 1/21/12
 * Time: 3:35 AM
 * To change this template use File | Settings | File Templates.
 */
public class Question12 {

    public static void main(String[] args) {

        int sum = 0;

        for(int i=1; i<Integer.MAX_VALUE; i++) {

            sum += i;
            int cnt = 0;
            for(int j=1; j<=sum; j++) {

                if(sum % j == 0) cnt++;

            }

            if(cnt > 500) {
                System.out.println(sum);
                System.exit(0);
            }

        }

    }

}
