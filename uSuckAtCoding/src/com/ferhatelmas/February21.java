package com.ferhatelmas;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 2/21/12
 * Time: 9:31 PM
 * To change this template use File | Settings | File Templates.
 */
public class February21 {

    public static void main(String[] args) {

        System.out.println(getFirstNonRepeated("abcac"));
        
    }
    
    private static int getFirstNonRepeated(String input) {

        int length = input.length();

        for(int i=0; i<length; i++) {

            boolean repeated = false;

            for(int j=0; j<length; j++) {
                
                if(input.charAt(i) == input.charAt(j) && i != j) {
                    repeated = true;
                    break;
                }
                
            }

            if(!repeated) return i;
        }

        return -1;

    }
    
}
