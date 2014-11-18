package page46.q4538;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), c = 1, s = 0;
    while(s + c <= n) {
      s += c;
      c++;
    }
    System.out.println(c-1);
  }
}
