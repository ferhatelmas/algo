package com.ferhatelmas.eolimp.page88.q2732;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    for(int i=1, t=in.nextInt(); i<=t; i++) {
      int ns[] = new int[3];
      for(int j=0; j<ns.length; j++) ns[j] = in.nextInt();
      Arrays.sort(ns);
      String s;
      if(ns[0] <= ns[2] - ns[1] || ns[2] >= ns[0] + ns[1]) s = "invalid!";
      else if(ns[0] == ns[1] && ns[1] == ns[2]) s = "equilateral";
      else if(ns[0] == ns[1] || ns[0] == ns[2] || ns[1] == ns[2]) s = "isosceles";
      else s = "scalene";

      System.out.println("Case #" + i + ": " + s);
    }
  }
}
