package com.ferhatelmas;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 1/20/12
 * Time: 11:52 PM
 * To change this template use File | Settings | File Templates.
 */
public class Question1 {

    public static void main(String[] args) {

        int sum = 0;
        for(int i=1; i<1000; i++) {
            if(i%3 == 0 || i%5 == 0) sum += i;
        }

        System.out.println(sum);
    }

}
