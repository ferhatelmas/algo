package com.ferhatelmas.eolimp.page31.q935;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    String s = new Scanner(System.in).nextLine();
    if(s.length() > 3) s = s.substring(s.length()-3);
    for(char c : s.toCharArray()) System.out.println(c);
  }

}
