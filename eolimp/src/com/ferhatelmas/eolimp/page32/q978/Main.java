package com.ferhatelmas.eolimp.page32.q978;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int n = in.nextInt(), m = in.nextInt();
    int[] nodes = new int[n+1];
    for(int i=0; i<nodes.length; i++) nodes[i] = i;
    while(m-- > 0) {
      int a = in.nextInt(), b = in.nextInt();
      if(nodes[a] != nodes[b]) {
        System.out.println(a + " " + b);
        int c = nodes[a], d = nodes[b];
        for(int i=0; i<nodes.length; i++)
          if(nodes[i] == c || nodes[i] == d) nodes[i] = c;
      }
    }
  }
}
