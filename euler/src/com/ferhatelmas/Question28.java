package com.ferhatelmas;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/2/12
 * Time: 4:32 AM
 * To change this template use File | Settings | File Templates.
 */
public class Question28 {

    private static int scale = 1001;
    
    public static void main(String[] args) {
        
        int[][] block = new int[scale][scale];

        for(int i=0; i<scale; i++) {

            for(int j=0; j<scale; j++) {

                block[i][j] = -1;

            }

        }

        int val = scale*scale+1;
        int i=0, j = scale;

        while(val > 1) {

            //left
            while(j-1>=0 && block[i][j-1] == -1) {
                j--;
                val--;
                block[i][j] = val;
            }

            //down
            while(i+1<scale && block[i+1][j] == -1) {
                i++;
                val--;
                block[i][j] = val;
            }

            //right
            while(j+1<scale && block[i][j+1] == -1) {
                j++;
                val--;
                block[i][j] = val;
            }

            //up
            while(i-1>=0 && block[i-1][j] == -1) {
                i--;
                val--;
                block[i][j] = val;
            }

        }

        long sum = 0;

        for(i=0, j=0; i<scale; i++, j++) {

            sum += block[i][j];

        }

        for(i=0, j=scale-1; i<scale; i++, j--) {

            sum += block[i][j];

        }

        sum -= block[scale/2][scale/2];

        System.out.println(sum);

        /*for(i=0; i<scale; i++) {

            for(j=0; j<scale; j++) {

                System.out.print(block[i][j] + "-");

            }

            System.out.println();
        }*/

    }
    
}
