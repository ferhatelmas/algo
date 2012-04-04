package com.ferhatelmas.euler;

public class Question17 {

    public static void main(String[] args) {
        
        int cnt = 0, tmp;
        for(int i=1; i<1000; i++) {

            tmp = i;
            if(tmp>99) {

                cnt +=7;

                if(tmp%100 != 0) cnt += 3;

                cnt += getUnder30(tmp/100);

            }

            tmp %= 100;

            if(tmp>29) {
                cnt += getTenth(tmp/10);
                cnt += getUnder30(tmp%10);
            } else if(tmp<30){
                cnt += getUnder30(tmp);
            }

        }

        System.out.println(cnt+11);
        
    }
    
    static int getTenth(int i) {

        int cnt = 0;

        switch (i) {
            case 3: cnt+= 6; break;
            case 4: cnt+= 5; break;
            case 5: cnt+= 5; break;
            case 6: cnt+= 5; break;
            case 7: cnt+= 7; break;
            case 8: cnt+= 6; break;
            case 9: cnt+= 6; break;
        }
        return cnt;
    }
    
    static int getUnder30(int i) {

        int cnt = 0;
        
        switch (i) {
            case 0: cnt+= 0; break;
            case 1: cnt+= 3; break;
            case 2: cnt+= 3; break;
            case 3: cnt+= 5; break;
            case 4: cnt+= 4; break;
            case 5: cnt+= 4; break;
            case 6: cnt+= 3; break;
            case 7: cnt+= 5; break;
            case 8: cnt+= 5; break;
            case 9: cnt+= 4; break;
            case 10: cnt+= 3; break;
            case 11: cnt+= 6; break;
            case 12: cnt+= 6; break;
            case 13: cnt+= 8; break;
            case 14: cnt+= 8; break;
            case 15: cnt+= 7; break;
            case 16: cnt+= 7; break;
            case 17: cnt+= 9; break;
            case 18: cnt+= 8; break;
            case 19: cnt+= 8; break;
            case 20: cnt+= 6; break;
            case 21: cnt+= 9; break;
            case 22: cnt+= 9; break;
            case 23: cnt+= 11; break;
            case 24: cnt+= 10; break;
            case 25: cnt+= 10; break;
            case 26: cnt+= 9; break;
            case 27: cnt+= 11; break;
            case 28: cnt+= 11; break;
            case 29: cnt+= 10; break;

        }
        
        return cnt;
        
    }
    
}
