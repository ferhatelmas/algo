package page2.q194;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    System.out.println(getSmallest(n) + " " + getLargest(n));
  }

  private static String getLargest(int n) {
    StringBuilder sb = new StringBuilder();
    for(int i=2; i<10; i++) {
      while(n%i == 0) {
        sb.append(i);
        n /= i;
      }
    }
    return n == 1 ? sb.reverse().toString() : "-1";
  }

  private static String getSmallest(int n) {
    StringBuilder sb = new StringBuilder();
    for(int i=9; i>1; i--) {
      while(n%i == 0) {
        sb.append(i);
        n /= i;
      }
    }
    return n == 1 ? sb.reverse().toString() : "-1";
  }
}
