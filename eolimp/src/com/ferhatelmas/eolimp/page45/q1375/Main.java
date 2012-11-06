package com.ferhatelmas.eolimp.page45.q1375;

import java.util.Scanner;


public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int n = in.nextInt();
    String[] res = new String[n];

    for(int i=0; i<n; i++) {

      int pro = in.nextInt();
      if(pro == 0) res[i] = String.valueOf(0);
      else {
        StringBuilder sb = new StringBuilder();

        while(pro != 0) {

          if(pro%2 == 0) sb.append('0');
          else {
            sb.append('1');
            pro -= 1;
          }
          pro /= -2;
        }
        res[i] = sb.reverse().toString();
      }

    }

    for(int i=0; i<n; i++)
      System.out.println("Case #"+ (i+1) + ": " + res[i]);
  }

}