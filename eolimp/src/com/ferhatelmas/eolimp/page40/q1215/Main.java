package com.ferhatelmas.eolimp.page40.q1215;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt();

    while(t-- > 0) {
      int n = in.nextInt(), c1 = 0, c2 = 0;
      in.nextLine();
      for(int i=0; i<n;i ++) {
        String s = in.nextLine();
        if(s.equals("R S") || s.equals("S P") || s.equals("P R")) c1++;
        else if(s.equals("S R") || s.equals("P S") || s.equals("R P")) c2++;
      }
      if(c1 > c2) System.out.println("Player 1");
      else if(c1 < c2) System.out.println("Player 2");
      else System.out.println("TIE");
    }
  }
}
