package page10.q957;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int sum = 0;
    for(char c : new Scanner(System.in).nextLine().toCharArray())
      sum += c - '0';
    System.out.printf(Locale.US, "%.3f\n", Math.sqrt(sum));
  }
}
