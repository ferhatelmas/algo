package com.ferhatelmas;

/**
 * Created by IntelliJ IDEA.
 * User: felmas
 * Date: 1/27/12
 * Time: 11:49 PM
 * To change this template use File | Settings | File Templates.
 */
public class Question15 {
    
    public static void main(String[] args) {
        
        long cnt = traverse(4, 4);

        System.out.println(cnt);
        
    }
    
    private static long traverse(int left, int right) {
        
        if(right == 0 || left == 0) return 1;
        
        return traverse(left, right-1) + traverse(left-1, right);

    }
    
}
