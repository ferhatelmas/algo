package com.ferhatelmas.eolimp.page28.q837;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    char[] cs = new Scanner(System.in).next().toCharArray();
    Arrays.sort(cs);
    perm("", new String(cs));
  }

  private static void perm(String p, String src) {
    int n = src.length();
    if(n == 0) System.out.println(p);
    else
      for(int i=0; i<n; i++)
        perm(p + src.charAt(i), src.substring(0, i) + src.substring(i+1));
  }
}
