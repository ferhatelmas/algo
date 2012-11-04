package com.ferhatelmas.eolimp.page30.q912;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    String[] s = new Scanner(System.in).nextLine().split("\\.{3}");

    String[] tmp;
    int cnt = 0;
    for(String ss : s) {
      tmp = ss.split("[!\\.?:]");
      for(String sss : tmp) if(sss.length()>0) cnt++;
    }
    System.out.println(cnt);
  }

}