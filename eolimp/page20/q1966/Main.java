package page20.q1966;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    print(n);
    for(int i=2*n+1; i>0; i--)
      System.out.print('*');
    System.out.println();
    print(n);
  }

  private static void print(int n) {
    for(int i=0; i<n; i++) {
      for(int j=0; j<n; j++)
        System.out.print('.');
      System.out.print('*');
      for(int j=0; j<n; j++)
        System.out.print('.');
      System.out.println();
    }
  }
}
