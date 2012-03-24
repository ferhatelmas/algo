package com.ferhatelmas;

import java.io.BufferedReader;
import java.io.FileReader;
import java.math.BigInteger;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/24/12
 * Time: 12:25 AM
 * To change this template use File | Settings | File Templates.
 */
public class Question99 {

    //comments are the part of the actual calculation
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new FileReader("base_exp.txt"));

        double max = 0;
        //BigInteger max = new BigInteger("0");
        int lineNumber = 1, maxLineNumber = -1;
        String line;
        
        while((line = br.readLine()) != null) {

            String[] parts = line.split(",");

            double d = Integer.parseInt(parts[1]) * Math.log10(Integer.parseInt(parts[0]));
            
            //BigInteger base = new BigInteger(parts[0]);
            //base = base.pow(Integer.parseInt(parts[1]));

            if(d > max) {
                max = d;
                maxLineNumber = lineNumber;
            }

            //if(base.compareTo(max) == 1) {
            //    max = base;
            //    maxLineNumber = lineNumber;
            //}

            lineNumber++;
        }

        System.out.println(maxLineNumber);
    }
    
}
