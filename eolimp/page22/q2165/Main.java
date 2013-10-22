package page22.q2165;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    String s = new Scanner(System.in).nextLine().trim();
    System.out.println(s.replaceAll("\\s{2,}", " "));
  }
}
