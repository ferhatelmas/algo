package page23.q2207;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s[] = in.nextLine().split(":");
    int n[] = new int[s.length];
    for(int i=0; i<s.length; i++) n[i] = Integer.parseInt(s[i]);

    System.out.printf("%02d:%02d\n", n[0], n[1]);
    int t = in.nextInt();
    while(t-- > 1) {
      int dt = in.nextInt() + n[1];
      n[1] = dt % 60;
      n[0] = (n[0] + dt/60) % 24;
      System.out.printf("%02d:%02d\n", n[0], n[1]);
    }
  }
}
