package com.ferhatelmas;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 1/21/12
 * Time: 2:48 AM
 * To change this template use File | Settings | File Templates.
 */
public class Question9 {

    public static void main(String[] args) {
        
        for(int i=1; i<500; i++) {
            
            for(int j=1; j<=i; j++) {
            
                int c = 1000-i-j;
                
                if(c*c==i*i+j*j) {
                    System.out.println(c*i*j);
                    System.exit(0);
                }
                
            }
            
        }
        
    }
    
}
