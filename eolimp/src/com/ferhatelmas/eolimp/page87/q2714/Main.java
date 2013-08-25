package com.ferhatelmas.eolimp.page87.q2714;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s = in.nextLine();
    int c1 = in.nextInt(), c2 = in.nextInt(), cnt = 0, l = s.length();
    for(char c : s.toCharArray()) if(c >= 'a' && c <= 'z') cnt++;
    System.out.println(Math.min(c1 * cnt, c2 * (l-cnt)));
  }
}
