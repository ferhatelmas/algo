package com.ferhatelmas.eolimp.page44.q1326;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws Exception{
    int n = new Scanner(System.in).nextInt();
    if(n>=3) System.out.println(n*(n-1)*(n-2));
    else System.out.println(n);
  }

}