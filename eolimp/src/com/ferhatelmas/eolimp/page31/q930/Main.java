package com.ferhatelmas.eolimp.page31.q930;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {

  public static void main(String[] args) throws Exception {

    String numbers="0123456789", s = new BufferedReader(new InputStreamReader(System.in)).readLine();
    StringBuilder sb = new StringBuilder();
    int cnt=0;

    for(int i=0; i<10; i++) {
      if(!s.contains(numbers.subSequence(i,i+1))) {
        cnt++;
        sb.append(numbers.charAt(i));
      }
    }

    System.out.println(cnt);
    for(int i=0; i<sb.length()-1; i++)
      System.out.print(sb.charAt(i) + " ");

    if(sb.length() > 0) System.out.println(sb.charAt(sb.length()-1));
  }

}