package page25.q2440;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), ns[] = new int[10], c;

    while(n-- > 0) {
      c = in.nextInt();
      for(int i=0; i<ns.length; i++) ns[i] = in.nextInt();
      Arrays.sort(ns);
      System.out.println(c + " " + ns[7]);
    }
  }
}
