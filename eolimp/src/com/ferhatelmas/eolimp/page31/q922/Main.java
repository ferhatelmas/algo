package com.ferhatelmas.eolimp.page31.q922;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    ArrayList<Integer> list = new ArrayList<Integer>();
    Scanner in = new Scanner(System.in);

    int n = in.nextInt();
    for(int i=0; i<n-1; i++)
      list.add(in.nextInt());

    list.add(0, in.nextInt());

    for(int i=0; i<n-1; i++)
      System.out.print(list.get(i) + " ");

    System.out.println(list.get(list.size()-1));
  }

}