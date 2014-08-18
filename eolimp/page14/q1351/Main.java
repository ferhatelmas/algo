package page14.q1351;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int max = 0;
    for(char c : new Scanner(System.in).next().toCharArray())
      max = Math.max(c - '0', max);
    System.out.println(max);
  }
}
