package com.ferhatelmas.eolimp.page44.q1312;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int[] dim = new int[3], door = new int[2];
    for(int i=0; i<dim.length; i++) dim[i] = in.nextInt();
    for(int i=0; i<door.length; i++) door[i] = in.nextInt();
    Arrays.sort(dim);
    Arrays.sort(door);
    System.out.println(dim[0] <= door[0] && dim[1] <= door[1] ? "YES" : "NO");
  }
}
