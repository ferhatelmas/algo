package com.ferhatelmas.eolimp.page37.q1124;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    int n = new Scanner(System.in).nextInt();

    for(int i=0; i<n; i++) {
      System.out.print("a");
      for(int j=0; j<n-i-1; j++) System.out.print(" ");
      for(int j=0; j<i+1; j++) System.out.print((char)(j + (int)'a'));
      System.out.println();
    }

  }

}