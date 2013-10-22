package page10.q939;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = new Scanner(System.in).next();
    int sum = 0;
    for(char c : s.toCharArray()) sum += c - '0';
    System.out.println(sum * sum);
  }
}
