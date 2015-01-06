package page74.q7367;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    double n = new Scanner(System.in).nextInt(), s = 10.0, c = 10.0;
    int i = 1;
    while(s < n) {
      c *= 1.1;
      s += c;
      i++;
    }
    System.out.println(i);
  }
}
