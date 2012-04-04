package com.ferhatelmas.euler;

import java.io.File;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Question22 {

    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(new File("names.txt"));

        sc.useDelimiter(",");

        ArrayList<String> list = new ArrayList<String>();

        while(sc.hasNext()) {

            String s = sc.next();

            s = s.substring(1, s.length()-1);

            list.add(s);

        }

        Object[] s = list.toArray();

        Arrays.sort(s);

        long sum = 0;

        for(int i=0; i<s.length; i++) {

            sum += getVal((String)s[i])*(i+1);
            
        }

        System.out.println(sum);

    }

    static int getVal(String s) {

        int sum = 0;
        for(int i=0; i<s.length(); i++) {

            sum += s.charAt(i) - 'A' + 1;

        }

        return sum;

    }

}
