package com.ferhatelmas.eolimp.page30.q915;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int a=in.nextInt(), b=in.nextInt(), c=in.nextInt();

    if(a>b && a>c) {

      if(a*a == (b*b+c*c)) System.out.println("YES");
      else System.out.println("NO");

    } else if(b>a && b>c) {

      if(b*b == (a*a+c*c)) System.out.println("YES");
      else System.out.println("NO");

    } else if(c>a && c>b) {

      if(c*c == (b*b+a*a)) System.out.println("YES");
      else System.out.println("NO");

    } else {

      System.out.println("NO");

    }

  }

}