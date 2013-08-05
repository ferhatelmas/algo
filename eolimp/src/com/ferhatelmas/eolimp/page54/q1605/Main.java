package com.ferhatelmas.eolimp.page54.q1605;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    boolean f = false;
    for(char c : new Scanner(System.in).next().toCharArray())
      if(c >= '0' && c <= '9')
        if(!f) f = !f;
        else { System.out.println(c); return; }
  }
}
