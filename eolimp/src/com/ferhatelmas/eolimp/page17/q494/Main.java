package com.ferhatelmas.eolimp.page17.q494;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in=new Scanner(System.in);
    String s;

    int cnt = 0;
    while(in.hasNext()) {
      s = in.next();
      for(int i=0; i<s.length(); i++) {
        char c=s.charAt(i);
        if(c=='A' || c=='E' || c=='I' || c=='O' || c=='U' || c=='Y') cnt++;
      }
    }
    System.out.println(cnt);
  }

}