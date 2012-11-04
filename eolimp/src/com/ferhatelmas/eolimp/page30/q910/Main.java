package com.ferhatelmas.eolimp.page30.q910;

import java.util.Scanner;
import java.text.DecimalFormat;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int n = Integer.parseInt(in.next().trim());
    int i, cnt = 0;
    double sum = 0, tmp;
    for(i=0; i<n; i++) {
      tmp = Double.parseDouble(in.next().trim());
      if(tmp>0) {
        sum += tmp;
        cnt++;
      }
    }

    if(cnt>0) System.out.println(new DecimalFormat("#########0.00").format(sum/cnt).replace(",", "."));
    else System.out.println("Not Found");
  }

}