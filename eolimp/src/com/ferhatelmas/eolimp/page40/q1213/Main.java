package com.ferhatelmas.eolimp.page40.q1213;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in).useDelimiter("\\s|\\^");
    int a = in.nextInt(), b = in.nextInt(), c = in.nextInt(), d = in.nextInt();
    System.out.println(b*Math.log(a) > d*Math.log(c) ? a + "^" + b : c + "^" + d);
  }
}
