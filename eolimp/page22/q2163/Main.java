package page22.q2163;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int sum = 0;
    for(char c : new Scanner(System.in).nextLine().toCharArray()) {
      sum += c - '0';
    }
    System.out.println(sum%3 == 0 ? "YES" : "NO");
  }
}
