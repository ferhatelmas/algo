package com.ferhatelmas.euler.page1;

public class Question31 {

    private static int[] coins = {200, 100, 50, 20, 10, 5, 2, 1};
    private static int cnt = 0;
    
    public static void main(String[] args) {

        produce(200, 200);

        System.out.println(cnt);

    }
    
    private static void produce(int n, int max) {
    
        if(n == 0) {
            cnt++;
            return;
        }

        if(n<0) return;
        
        for(int i=0; i<coins.length; i++) {

            if(coins[i] <= max) produce(n-coins[i], coins[i]);
            
        }

    }

}
