package com.ferhatelmas.euler.page1;

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
