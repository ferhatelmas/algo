package page53.q5233;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n[] = new int[9];
    for(int i=0; i<n.length; i++)
      n[i] = in.nextInt();
    System.out.println(getMagicNumber(n));
  }

  private static int getMagicNumber(int n[]) {
    return ((n[0]*n[4]*n[8]) + (n[1]*n[5]*n[6]) + (n[2]*n[3]*n[7])) -
        ((n[2]*n[4]*n[6]) + (n[1]*n[3]*n[8]) + (n[0]*n[5]*n[7]));
  }
}
