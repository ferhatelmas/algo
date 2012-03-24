package com.ferhatelmas;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 1/21/12
 * Time: 1:52 AM
 * To change this template use File | Settings | File Templates.
 */
public class Question6 {

    public static void main(String[] args) {

        long sum = 0;
        for(int i=1; i<=100; i++) {
            sum += i*i;
        }
        System.out.println(5050*5050-sum);

    }

}
