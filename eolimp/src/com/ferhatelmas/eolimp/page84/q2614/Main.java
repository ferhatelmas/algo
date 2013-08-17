package com.ferhatelmas.eolimp.page84.q2614;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int t = new Scanner(System.in).nextInt(), c = 1;
    StringBuilder sb = new StringBuilder();
    while(t > 0) {
      int cnt = Math.min(t, c);
      for(int i=0; i<cnt; i++) sb.append(c).append(" ");
      c++;
      t -= cnt;
    }
    System.out.println(sb.substring(0, sb.length()-1));
  }
}
