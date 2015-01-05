package page74.q7337;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int ns[] = new int[3];
    for(int i=0; i<ns.length; i++) ns[i] = in.nextInt();
    Arrays.sort(ns);
    System.out.println(ns[0] + ns[2]);
  }
}
