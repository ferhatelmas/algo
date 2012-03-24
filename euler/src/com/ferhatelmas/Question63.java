package com.ferhatelmas;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/23/12
 * Time: 11:49 PM
 * To change this template use File | Settings | File Templates.
 */
public class Question63 {

    public static void main(String[] args) {

        int n = 1;
        int pow = 0;
        int cnt = 0;

        while(pow < 10) {

            pow = (int)Math.ceil(Math.pow(10, (n-1)/(double)n));
            cnt += 10-pow;
            
            n++;

        }

        System.out.println(cnt);

    }
    
}
