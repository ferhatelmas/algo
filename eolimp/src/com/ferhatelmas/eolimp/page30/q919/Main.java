package com.ferhatelmas.eolimp.page30.q919;

import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

  public static void main(String[] args) {

    int i, n, cnt=0;
    double d, sum=0;
    Scanner in = new Scanner(System.in);
    n=in.nextInt();
    for(i=0; i<n; i++) {
      d=Double.parseDouble(in.next());
      if((i+1)%3==0 && d>0) {
        cnt++;
        sum+=d;
      }
    }
    System.out.println(cnt + " " + new DecimalFormat("#########0.00").format(sum).replace(",", "."));
  }

}