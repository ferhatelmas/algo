package com.ferhatelmas.eolimp.page1.q19;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    String s = new Scanner(System.in).next();
    int sum;

    if(s.length()%2 == 0) sum = 0;
    else sum = 1;
    for(int i=0; i<s.length()/2; i++)
      if(s.charAt(i) == s.charAt(s.length()-i-1)) sum++;

    System.out.println(sum);
  }

}