package com.ferhatelmas.eolimp.page5.q138;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    int n = new Scanner(System.in).nextInt(), sum = 0;
    int[] cash = {500, 200, 100, 50, 20, 10};

    for(int c : cash) {
      int cnt = n/c;
      n -= cnt*c;
      sum += cnt;
    }

    System.out.println(n == 0 ? sum : -1);
  }

}