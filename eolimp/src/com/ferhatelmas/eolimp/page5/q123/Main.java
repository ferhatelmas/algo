package com.ferhatelmas.eolimp.page5.q123;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), cnt = 0;
    while(n > 0) {
      n /= 5;
      cnt += n;
    }
    System.out.println(cnt);
  }
}
