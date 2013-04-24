package com.ferhatelmas.eolimp.page3.q83;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    String[] parts = new Scanner(System.in).next().split("/");
    StringBuilder sb = new StringBuilder();
    int d = Integer.parseInt(parts[0]) + 1;
    sb.append(Integer.toString(Integer.parseInt(parts[0]), d));
    sb.append("/");
    sb.append(Integer.toString(Integer.parseInt(parts[1]), d));
    sb.append("/");
    sb.append(Integer.toString(Integer.parseInt(parts[2]), d));
    System.out.println(sb.toString().toUpperCase());
  }
}
