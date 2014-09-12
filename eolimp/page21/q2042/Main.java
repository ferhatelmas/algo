package page21.q2042;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = (int)Math.ceil(new Scanner(System.in).nextInt()/3.0);
    String s[] = {"First", "Second", "Third", "Fourth"};
    System.out.println(s[n-1]);
  }
}
