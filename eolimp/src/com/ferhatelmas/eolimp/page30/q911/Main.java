package com.ferhatelmas.eolimp.page30.q911;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    double a = in.nextInt();
    double b = in.nextInt();
    double c = in.nextInt();
    double delta=b*b-4*a*c;
    if(delta<0) System.out.println("No roots");
    else if(delta==0) System.out.println("One root: " + (int)(-b/(2*a)));
    else {
      double d1=((-b+Math.sqrt(delta))/(2*a));
      double d2=((-b-Math.sqrt(delta))/(2*a));

      if(d1<d2) System.out.println("Two roots: " + (int)d1 + " " + (int)d2);
      else System.out.println("Two roots: " + (int)d2 + " " + (int)d1);
    }

  }

}