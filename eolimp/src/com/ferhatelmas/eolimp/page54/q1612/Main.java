package com.ferhatelmas.eolimp.page54.q1612;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    char[] c = Integer.toBinaryString(new Scanner(System.in).nextInt()).toCharArray();
    for(int i=c.length-1; i>=0; i--) if(c[i] == '1') { c[i] = '0'; break; }
    System.out.println(Integer.parseInt(new String(c), 2));
  }
}
