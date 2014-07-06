package page22.q2162;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = new Scanner(System.in).nextLine().replaceAll("\\s", "");
    boolean b = new StringBuilder(s).reverse().toString().equals(s);
    System.out.println(b ? "YES" : "NO");
  }
}
