package com.ferhatelmas;

import java.io.BufferedReader;
import java.io.FileReader;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/26/12
 * Time: 10:40 PM
 * To change this template use File | Settings | File Templates.
 */
public class Question67 {

    public static void main(String[] args) throws Exception {
        
        int[][] triangle = new int[100][100];

        BufferedReader br = new BufferedReader(new FileReader("triangle.txt"));
        
        String line;
        int i=0;
        
        while((line=br.readLine()) != null) {
            
            String[] values = line.split(" ");
            
            for(int j=0; j<values.length; j++) {
                
                triangle[i][j] = Integer.parseInt(values[j]);
                
            }

            i++;
        }
        br.close();

        for(i=triangle.length-1; i>0; i--) {
            
            for(int j=i-1; j>=0; j--) {
                
                triangle[i-1][j] += Math.max(triangle[i][j], triangle[i][j+1]);
                
            }
            
        }

        System.out.println(triangle[0][0]);

    }

}
