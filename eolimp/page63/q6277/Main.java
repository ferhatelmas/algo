package page63.q6277;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), c = 0;

    while(n >= 1.2) {
      c++;
      n -= 1;
    }
    System.out.println(c);
  }
}
