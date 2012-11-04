package com.ferhatelmas.eolimp.page30.q909;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main{

  public static void main(String[]args) throws Exception {

    String[] s = new BufferedReader(new InputStreamReader(System.in)).readLine().split(" ");
    int cnt = 0;
    for(String ss : s)
      if(!ss.contains("[^0-9]") && !ss.contains("-")) cnt++;

    System.out.println(cnt);
  }


}