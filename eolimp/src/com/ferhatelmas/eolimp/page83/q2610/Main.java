package com.ferhatelmas.eolimp.page83.q2610;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int k = new Scanner(System.in).nextInt();
    StringBuilder sb = new StringBuilder().append('9');
    for(int i=1, p=9; i<k; i++) {
      for(int j=9; j>-1; j--) {
        if(j != p) {
          sb.append(j);
          p = j;
          break;
        }
      }
    }
    System.out.println(sb.toString());
  }
}
