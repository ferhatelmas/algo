package com.ferhatelmas.euler.page2;

import java.io.BufferedReader;
import java.io.FileReader;

public class Question81 {

    public static void main(String[] args) throws Exception{

        int[][] matrix = new int[80][80];

        BufferedReader br = new BufferedReader(new FileReader("matrix.txt"));
        
        for(int i=0; i<matrix.length; i++) {
            
            String[] line = br.readLine().split(",");

            for(int j=0; j<matrix[0].length; j++) {

                matrix[i][j] = Integer.parseInt(line[j]);

            }
            
        }

        System.out.println(getSum(matrix));

    }
    
    private static int getSum(int[][] matrix) {
        
        for(int i=matrix.length-2; i>=0; i--) {

            matrix[matrix.length-1][i] += matrix[matrix.length-1][i+1];
            matrix[i][matrix[0].length-1] += matrix[i+1][matrix[0].length-1];
        }

        for(int i=matrix.length-2; i>=0; i--) {
            for(int j=matrix[0].length-2; j>=0; j--) {

                matrix[i][j] += Math.min(matrix[i][j+1], matrix[i+1][j]);

            }
        }

        return matrix[0][0];
        
    }

}
