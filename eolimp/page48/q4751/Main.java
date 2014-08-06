package page48.q4751;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), d1 = 0, d2 = 0, s;
    for(int i=0; i<n; i++) {
      for(int j=0; j<n; j++) {
        s = in.nextInt();
        if(i == j) d1 += s;
        if(i+j == n-1) d2 += s;
      }
    }
    System.out.println(d1 + " " + d2);
  }
}
