package page21.q2015;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    boolean r = false;
    for(int i=0; i<n; i++)
      r ^= in.nextInt() == 1;
    System.out.println(r ? "Second" : "First");
  }
}
