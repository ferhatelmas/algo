package com.ferhatelmas.eolimp.page83.q2607;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int odd = 0, even = 0, i = 0;
    for(char c : new Scanner(System.in).next().toCharArray())
      if(i++%2 == 0) even += c - '0';
      else odd += c - '0';
    System.out.println(odd * even);
  }
}
