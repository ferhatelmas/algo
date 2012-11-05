package com.ferhatelmas.eolimp.page17.q496;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in=new Scanner(System.in);

    int n = in.nextInt(), len, i, j;
    boolean[] res = new boolean[n];

    String s1, s2;
    for(i=0; i<n; i++) {
      s1 = in.next();
      s2 = in.next();

      if(s1.length()!=s2.length()) res[i]=false;
      else {
        len = s1.length();
        for(j=0; j<len; j++) {
          if(s1.charAt(j)!=s2.charAt(len-1-j)) {
            res[i]=false;
            break;
          }
        }
        res[i]=true;
      }
    }

    for(boolean b : res)
      System.out.println(b ? "Yes" : "No");
  }

}