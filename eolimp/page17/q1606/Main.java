package page17.q1606;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = String.valueOf(Math.abs(new Scanner(System.in).nextInt()));
    System.out.println(s.charAt(0) + s.charAt(s.length()-1) - 2 * '0');
  }
}
