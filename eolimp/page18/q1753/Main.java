package page18.q1753;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int n;
    while((n = in.nextInt()) != 0) {
      String s = Integer.toBinaryString(n);
      System.out.println(Integer.parseInt(s.substring(s.lastIndexOf('1')), 2));
    }
  }
}
