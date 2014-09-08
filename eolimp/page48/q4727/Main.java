package page48.q4727;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = new Scanner(System.in).next();
    int i = s.indexOf('f');
    if(i < 0) {
      System.out.println(-2);
    } else {
      int j = s.indexOf('f', i+1);
      System.out.println(j < 0 ? -1 : j);
    }
  }
}
