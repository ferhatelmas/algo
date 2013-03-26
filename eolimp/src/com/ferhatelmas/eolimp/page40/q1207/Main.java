package com.ferhatelmas.eolimp.page40.q1207;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    int[] cache = new int[1000001];
    Arrays.fill(cache, -1);
    cache[0] = 1;

    int i;
    Scanner in = new Scanner(System.in);
    while((i=in.nextInt()) != -1) {
      if(cache[i] == -1) fillUntil(cache, i);
      System.out.println(cache[i]);
    }
  }

  private static void fillUntil(int[] cache, int k) {
    for(int i=1; i<=k; i++) {
      cache[i] = (cache[(int)(i-Math.sqrt(i))] +
                 cache[(int)Math.log(i)] +
                 cache[(int)(i*Math.pow(Math.sin(i), 2))]) % 1000000;
    }
  }
}
