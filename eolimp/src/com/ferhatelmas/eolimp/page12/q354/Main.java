package com.ferhatelmas.eolimp.page12.q354;

import java.util.Scanner;
import java.util.TreeSet;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    TreeSet<Integer> set = new TreeSet<Integer>();
    int n = in.nextInt();

    for(int i=0; i<n; i++)
      set.add(in.nextInt());

    int i = 1;
    while(i <= n) {
      if(set.contains(i)) i++;
      else {
        System.out.println(i);
        return;
      }
    }
    System.out.println(0);
  }

}
