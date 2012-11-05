package com.ferhatelmas.eolimp.page15.q441;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int n=in.nextInt(), round, max = in.nextInt(), tmp, tmpRound;

    round=getRound(max);
    for(int i=0; i<n-1; i++) {
      tmp = in.nextInt();
      tmpRound = getRound(tmp);
      if(round < tmpRound) {
        round=tmpRound;
        max=tmp;
      } else if(round==tmpRound && tmp<max) {
        max=tmp;
      }
    }

    System.out.println(max);
  }

  private static int getRound(int val) {
    String s = String.valueOf(val);
    int cnt = 0;
    for(int i=s.length()-1; i>-1; i--) {
      if(s.charAt(i)=='0') cnt++;
      else break;
    }
    return cnt;
  }

}