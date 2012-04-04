package com.ferhatelmas.euler;

import java.io.BufferedReader;
import java.io.FileReader;

public class Question59 {

    public static void main(String[] args) throws Exception {

        String[] numberss = new BufferedReader(new FileReader("cipher1.txt")).readLine().split(",");
        
        int[] numbers = new int[numberss.length];

        for(int i=0; i<numbers.length; i++) {

            numbers[i] = Integer.parseInt(numberss[i]);

        }
        
        int sum = 0;

        for(int i=97; i<123; i++) {
            
            for(int j=97; j<123; j++) {
                
                for(int k=97; k<123; k++) {

                    boolean candidate = true;

                    for(int z=0; z<numbers.length; z+=3) {
                        
                        if(checkValidity(numbers[z], i) ||
                            (z+1 < numbers.length &&
                           checkValidity(numbers[z+1], j)) ||
                            (z+2 < numbers.length &&
                           checkValidity(numbers[z+2], k))) {

                            candidate = false;

                            break;

                        }

                    }

                    if(candidate) {

                        for(int x=0; x<numbers.length; x+=3) {

                            sum += (numbers[x] ^ i);
                            if(x+1 < numbers.length) sum += (numbers[x+1] ^ j);
                            if(x+2 < numbers.length) sum += (numbers[x+2] ^ k);

                        }

                        System.out.println(sum);
                        System.exit(0);

                    }
                    
                }
                
            }
            
        }

    }

    private static boolean checkValidity(int num, int key) {

        int check = num ^ key;

        return check<32 || (check>34 && check<39) || (check>59 && check<63)
                || (check == 64) || (check>90 && check<97) || check>122;

    }

}
