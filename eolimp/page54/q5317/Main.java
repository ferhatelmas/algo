package page54.q5317;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s = Integer.toBinaryString(in.nextInt());
    int k = in.nextInt(), l = s.length();
    System.out.println(k < l ? s.charAt(l-k-1) : '0');
  }
}
