package com.ferhatelmas.eolimp.page82.q2538;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s;
    while(!(s = in.nextLine()).equals("0")) System.out.println(encode(s));
  }

  private static String encode(String s) {
    char curr = ' ';
    int cnt = 0;
    StringBuilder sb = new StringBuilder();
    for(char c : s.toCharArray()) {
      if(c == curr) {
        cnt++;
      } else {
        if(curr != ' ') sb.append(cnt).append(curr);
        curr = c;
        cnt = 1;
      }
    }
    if(cnt > 0) sb.append(cnt).append(curr);
    return sb.toString();
  }
}
