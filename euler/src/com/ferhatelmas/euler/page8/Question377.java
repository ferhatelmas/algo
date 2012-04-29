package com.ferhatelmas.euler.page8;

import java.util.regex.Pattern;

public class Question377 {

    private static Pattern pattern = Pattern.compile("0");

    public static void main(String[] args) {

        long l = 1;

        for(int i=0; i<17; i++) l *=  13;

        System.out.println(l);

    }

}
