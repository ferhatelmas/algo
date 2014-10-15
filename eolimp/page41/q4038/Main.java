package page41.q4038;

import java.util.Arrays;
import java.util.Scanner;

// memory-limit
public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int ns[] = new int[10001];
    Arrays.fill(ns, 0);

    in.nextLine();
    for(String s : in.nextLine().split("\\s"))
      ns[Integer.parseInt(s)]++;

    boolean b = false;
    for(int i=0; i<ns.length; i++) {
      while(ns[i]-- > 0) {
        if(!b) b = !b;
        else System.out.print(" ");
        System.out.print(i);
      }
    }
    System.out.println();
  }
}
