package com.ferhatelmas;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 1/20/12
 * Time: 11:55 PM
 * To change this template use File | Settings | File Templates.
 */
public class Question2 {

    public static void main(String[] args) {

        long sum = 0;
        
        int curr = 0;
        int first = 1;
        int second = 2;

        sum = 2;
        curr = first + second;

        while(true) {
            first = second;
            second = curr;
            curr = first + second;
            if(curr > 4000000) break;
            if(curr%2 == 0) sum += curr;
        }

        System.out.println(sum);

    }


}
